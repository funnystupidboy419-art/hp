#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""教育時事アーカイブ — サイトとデータの検証.

GitHub Actions で「更新の直後」に実行し、壊れたものを公開しないための門番。
1つでも問題があれば非ゼロで終了する（ワークフローはそこで commit を中止する）。

チェック内容:
  1. data/news.json  … スキーマ、文字数、URL の安全性、ID/URL の重複
  2. index.html      … タグの対応、必須要素の存在、参照先ファイルの存在
  3. assets/js, css  … 参照されているファイルが実在するか
  4. リポジトリ全体  … API キーらしき文字列が混入していないか

使い方::

    python scripts/validate_site.py
    python scripts/validate_site.py --root . --strict
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent

VOID_ELEMENTS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}

REQUIRED_ELEMENT_IDS = [
    "last-updated", "entry-count", "footer-generator",
    "q", "month", "sort", "category-chips", "result-count", "reset",
    "loading", "error", "empty", "noresult", "archive", "tpl-entry",
]

REQUIRED_ENTRY_FIELDS = [
    "id", "collected_date", "title", "one_line",
    "what_happened", "why_important", "question",
    "categories", "importance", "sources",
]

MAX_LENGTHS = {
    "title": 90,
    "one_line": 90,
    "what_happened": 520,
    "why_important": 460,
    "question": 220,
}

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
# 実際の鍵をここに書かないよう、断片を連結して検出パターンを作る
SECRET_RE = re.compile(r"sk-" + r"ant-" + r"[A-Za-z0-9_\-]{12,}")
SCAN_SUFFIXES = {".py", ".js", ".html", ".css", ".json", ".yml", ".yaml", ".md", ".txt"}

# --------------------------------------------------------------------------
# 個人情報の検出
#
# 検査するのは「公開される中身」だけ（data/news.json・index.html・assets/）。
# スクリプトや CLAUDE.md まで見ると、この検出パターン自体を拾ってしまう。
#
# ERROR = 誤検出がまず起きない形（連絡先）。出たら push しない。
# WARN  = 手がかりであって断定ではない形。出たら人間が中身を見て判断する。
#         --strict を付けると警告もエラー扱いになる。
# --------------------------------------------------------------------------
PUBLISHED_FILES = ["data/news.json", "index.html"]
PUBLISHED_DIRS = ["assets"]

PERSONAL_ERROR_PATTERNS = [
    (
        re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}"),
        "メールアドレスらしき文字列",
    ),
    (
        re.compile(r"0\d{1,4}-\d{1,4}-\d{4}"),
        "電話番号らしき文字列",
    ),
]

# 「〜さん」の前に来ても人名とは限らない語
HONORIFIC_STOPWORDS = {
    "皆", "みな", "みなさ", "お子", "生徒", "児童", "学生", "先生", "保護者",
    "担任", "教員", "職員", "校長", "教頭", "本人", "当事者", "利用者",
}

PERSONAL_WARN_PATTERNS = [
    (
        re.compile(r"[0-9０-９一二三四五六七八九]{1,2}\s*年\s*[0-9０-９一二三四五六七八九]{1,2}\s*組"),
        "学級が特定される表記（◯年◯組）",
    ),
    (
        re.compile(r"(?:児童|生徒|園児)\s*[A-ZＡ-Ｚ](?![A-Za-zＡ-Ｚａ-ｚ])"),
        "個人を指す記号（児童A など）",
    ),
    (
        re.compile(r"([一-龥]{2,4})\s*(?:さん|くん|君|ちゃん)"),
        "人名＋敬称らしき表記",
    ),
    (
        re.compile(r"(?<!\d)\d{12}(?!\d)"),
        "12桁の数字（個人番号の桁数）",
    ),
]


class Problems:
    def __init__(self) -> None:
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


# --------------------------------------------------------------------------
# HTML
# --------------------------------------------------------------------------


class TagBalanceParser(HTMLParser):
    """開始/終了タグの対応と id 属性の収集を行う簡易パーサ。"""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: List[tuple] = []
        self.ids: List[str] = []
        self.errors: List[str] = []
        self.srcs: List[str] = []

    def handle_starttag(self, tag: str, attrs: List[tuple]) -> None:
        attr_map = {k: (v or "") for k, v in attrs}
        if "id" in attr_map:
            self.ids.append(attr_map["id"])
        for key in ("src", "href"):
            value = attr_map.get(key, "")
            if value and not value.startswith(("http://", "https://", "data:", "#", "//")):
                self.srcs.append(value)
        if tag not in VOID_ELEMENTS:
            self.stack.append((tag, self.getpos()))

    def handle_startendtag(self, tag: str, attrs: List[tuple]) -> None:
        attr_map = {k: (v or "") for k, v in attrs}
        if "id" in attr_map:
            self.ids.append(attr_map["id"])

    def handle_endtag(self, tag: str) -> None:
        if tag in VOID_ELEMENTS:
            return
        if not self.stack:
            self.errors.append(f"{self.getpos()[0]}行目: 対応する開始タグの無い </{tag}>")
            return
        open_tag, pos = self.stack[-1]
        if open_tag == tag:
            self.stack.pop()
            return
        # 直近のスタックから探して、間に閉じ忘れがあれば報告
        for depth in range(len(self.stack) - 1, -1, -1):
            if self.stack[depth][0] == tag:
                for unclosed, upos in self.stack[depth + 1:]:
                    self.errors.append(f"{upos[0]}行目: <{unclosed}> が閉じられていません")
                del self.stack[depth:]
                return
        self.errors.append(f"{self.getpos()[0]}行目: 予期しない </{tag}>")


def check_html(root: Path, problems: Problems) -> None:
    path = root / "index.html"
    if not path.exists():
        problems.error("index.html が見つかりません")
        return

    html_text = path.read_text(encoding="utf-8")

    parser = TagBalanceParser()
    parser.feed(html_text)
    parser.close()

    for err in parser.errors:
        problems.error(f"index.html: {err}")
    for tag, pos in parser.stack:
        problems.error(f"index.html: {pos[0]}行目: <{tag}> が閉じられていません")

    ids = set(parser.ids)
    for required in REQUIRED_ELEMENT_IDS:
        if required not in ids:
            problems.error(f"index.html: 必須の要素 id='{required}' がありません")

    duplicates = [i for i in parser.ids if parser.ids.count(i) > 1]
    for dup in sorted(set(duplicates)):
        problems.error(f"index.html: id='{dup}' が重複しています")

    if "<!DOCTYPE html>" not in html_text and "<!doctype html>" not in html_text:
        problems.error("index.html: DOCTYPE 宣言がありません")
    if 'lang="ja"' not in html_text:
        problems.warn("index.html: <html lang=\"ja\"> が見当たりません")
    if "viewport" not in html_text:
        problems.error("index.html: viewport メタタグがありません（レスポンシブ表示に必要）")

    for ref in parser.srcs:
        target = root / ref.split("?", 1)[0].split("#", 1)[0]
        if not target.exists():
            problems.error(f"index.html: 参照先が存在しません: {ref}")

    # app.js が参照する id が HTML 側にあるか
    app_js = root / "assets" / "js" / "app.js"
    if app_js.exists():
        js_text = app_js.read_text(encoding="utf-8")
        for match in re.finditer(r"getElementById\(\s*'([^']+)'\s*\)", js_text):
            if match.group(1) not in ids:
                problems.error(
                    f"assets/js/app.js が参照する id='{match.group(1)}' が index.html にありません"
                )


# --------------------------------------------------------------------------
# データ
# --------------------------------------------------------------------------


def check_url(url: Any) -> Optional[str]:
    if not isinstance(url, str) or not url.strip():
        return "URL が空です"
    if any(ch.isspace() for ch in url):
        return "URL に空白が含まれています"
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        return f"許可されないスキーム: {parsed.scheme or '(なし)'}"
    if not parsed.netloc or "." not in parsed.netloc:
        return "ホスト名が不正です"
    return None


def check_data(root: Path, problems: Problems) -> Dict[str, Any]:
    path = root / "data" / "news.json"
    if not path.exists():
        problems.error("data/news.json が見つかりません")
        return {}

    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        problems.error(f"data/news.json が JSON として壊れています: {exc}")
        return {}

    if not isinstance(doc, dict):
        problems.error("data/news.json: トップレベルがオブジェクトではありません")
        return {}

    meta = doc.get("meta")
    if not isinstance(meta, dict):
        problems.error("data/news.json: meta がありません")
        meta = {}
    last_updated = meta.get("last_updated")
    if last_updated is not None and not DATE_RE.match(str(last_updated)):
        problems.error(f"data/news.json: meta.last_updated の形式が不正です: {last_updated!r}")

    categories = doc.get("categories")
    if not isinstance(categories, list) or not categories:
        problems.error("data/news.json: categories が空です")
        category_ids = set()
    else:
        category_ids = set()
        for cat in categories:
            if not isinstance(cat, dict) or "id" not in cat or "label" not in cat:
                problems.error(f"data/news.json: categories の要素が不正です: {cat!r}")
                continue
            category_ids.add(cat["id"])

    entries = doc.get("entries")
    if not isinstance(entries, list):
        problems.error("data/news.json: entries が配列ではありません")
        return doc

    seen_ids: Dict[str, int] = {}
    seen_urls: Dict[str, str] = {}

    for index, entry in enumerate(entries):
        where = f"entries[{index}]"
        if not isinstance(entry, dict):
            problems.error(f"data/news.json: {where} がオブジェクトではありません")
            continue

        for field in REQUIRED_ENTRY_FIELDS:
            if field not in entry:
                problems.error(f"data/news.json: {where} に {field} がありません")

        entry_id = str(entry.get("id", ""))
        if not entry_id:
            problems.error(f"data/news.json: {where} の id が空です")
        elif entry_id in seen_ids:
            problems.error(
                f"data/news.json: id='{entry_id}' が重複しています "
                f"(entries[{seen_ids[entry_id]}] と {where})"
            )
        else:
            seen_ids[entry_id] = index

        for field in ("collected_date",):
            value = str(entry.get(field, ""))
            if not DATE_RE.match(value):
                problems.error(f"data/news.json: {where}.{field} の形式が不正です: {value!r}")

        published = str(entry.get("published_date", ""))
        if published and not DATE_RE.match(published):
            problems.error(f"data/news.json: {where}.published_date の形式が不正です: {published!r}")

        for field, limit in MAX_LENGTHS.items():
            value = entry.get(field)
            if not isinstance(value, str) or not value.strip():
                problems.error(f"data/news.json: {where}.{field} が空です")
                continue
            if len(value) > limit:
                problems.error(
                    f"data/news.json: {where}.{field} が長すぎます（{len(value)} > {limit}）"
                )
            if "<" in value or ">" in value:
                problems.error(f"data/news.json: {where}.{field} に HTML 記号が含まれています")

        cats = entry.get("categories")
        if not isinstance(cats, list) or not cats:
            problems.error(f"data/news.json: {where}.categories が空です")
        else:
            for cid in cats:
                if category_ids and cid not in category_ids:
                    problems.error(f"data/news.json: {where} の未定義カテゴリー: {cid!r}")

        importance = entry.get("importance")
        if not isinstance(importance, int) or not 1 <= importance <= 5:
            problems.error(f"data/news.json: {where}.importance が 1〜5 ではありません: {importance!r}")

        sources = entry.get("sources")
        if not isinstance(sources, list) or not sources:
            problems.error(f"data/news.json: {where}.sources が空です（出典必須）")
            continue
        for sindex, src in enumerate(sources):
            if not isinstance(src, dict):
                problems.error(f"data/news.json: {where}.sources[{sindex}] が不正です")
                continue
            reason = check_url(src.get("url"))
            if reason:
                problems.error(f"data/news.json: {where}.sources[{sindex}]: {reason}")
                continue
            url = src["url"]
            if url in seen_urls and seen_urls[url] != entry_id:
                problems.error(
                    f"data/news.json: 出典 URL が別記事と重複しています: {url} "
                    f"({seen_urls[url]} と {entry_id})"
                )
            seen_urls.setdefault(url, entry_id)

    return doc


# --------------------------------------------------------------------------
# 秘密情報
# --------------------------------------------------------------------------


def check_secrets(root: Path, problems: Problems) -> None:
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in SCAN_SUFFIXES:
            continue
        if any(part in {".git", "node_modules", ".venv"} for part in path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if SECRET_RE.search(text):
            problems.error(
                f"{path.relative_to(root)}: API キーらしき文字列が含まれています。"
                "GitHub Secrets を使用してください。"
            )


# --------------------------------------------------------------------------
# 個人情報
# --------------------------------------------------------------------------


def iter_published_files(root: Path) -> List[Path]:
    """公開される中身のファイルだけを返す。"""
    paths: List[Path] = []
    for name in PUBLISHED_FILES:
        path = root / name
        if path.is_file():
            paths.append(path)
    for name in PUBLISHED_DIRS:
        directory = root / name
        if not directory.is_dir():
            continue
        for path in sorted(directory.rglob("*")):
            if path.is_file() and path.suffix.lower() in SCAN_SUFFIXES:
                paths.append(path)
    return paths


def check_personal_info(root: Path, problems: Problems) -> None:
    for path in iter_published_files(root):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        rel = path.relative_to(root)

        for pattern, label in PERSONAL_ERROR_PATTERNS:
            match = pattern.search(text)
            if match:
                problems.error(
                    f"{rel}: {label}が含まれています（{match.group(0)}）。"
                    "個人が特定される情報は公開しないでください。"
                )

        for pattern, label in PERSONAL_WARN_PATTERNS:
            for match in pattern.finditer(text):
                if pattern.groups and match.group(1) in HONORIFIC_STOPWORDS:
                    continue
                problems.warn(
                    f"{rel}: {label}が見つかりました（{match.group(0)}）。"
                    "個人が特定されないか確認してください。"
                )
                break


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="サイトとデータの検証")
    parser.add_argument("--root", default=str(REPO_ROOT))
    parser.add_argument("--strict", action="store_true", help="警告もエラー扱いにする")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    problems = Problems()

    print(f"[validate] ルート: {root}")

    doc = check_data(root, problems)
    check_html(root, problems)
    check_secrets(root, problems)
    check_personal_info(root, problems)

    entries = doc.get("entries", []) if isinstance(doc, dict) else []
    print(f"[validate] 記事数: {len(entries)}")
    print(f"[validate] 最終更新: {(doc.get('meta') or {}).get('last_updated')}")

    for warning in problems.warnings:
        print(f"[warn ] {warning}")
    for error in problems.errors:
        print(f"[ERROR] {error}")

    failed = bool(problems.errors) or (args.strict and bool(problems.warnings))
    if failed:
        print(f"[validate] 失敗: エラー {len(problems.errors)} 件 / 警告 {len(problems.warnings)} 件")
        return 1

    print(f"[validate] OK（警告 {len(problems.warnings)} 件）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
