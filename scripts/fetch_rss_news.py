#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""教育ニュース RSS フィード自動取得スクリプト.

文部科学省の公式 RSS フィード（https://www.mext.go.jp/rss.html）から
直近3日以内のニュースを収集し、JSON フォーマットに変換する。

出力フォーマット: update_news.py --input-json で取り込める形式

使い方::

    python scripts/fetch_rss_news.py                    # JSON を stdout に出力
    python scripts/fetch_rss_news.py > /tmp/items.json  # ファイルに保存
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import urljoin, urlparse

try:
    from zoneinfo import ZoneInfo
    JST = ZoneInfo("Asia/Tokyo")
except Exception:
    JST = _dt.timezone(_dt.timedelta(hours=9))

try:
    import feedparser
except ImportError:
    print(
        "Error: feedparser が必要です。"
        "pip install feedparser で インストールしてください。",
        file=sys.stderr,
    )
    sys.exit(1)

# --------------------------------------------------------------------------
# 定数
# --------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent

# RSS フィード URL（文部科学省の公式フィード）
RSS_FEEDS = {
    "文部科学省": "https://www.mext.go.jp/rss.html",
}

# カテゴリーマッピング（キーワード → category ID）
KEYWORD_TO_CATEGORY = {
    "不登校": "futoko",
    "いじめ": "ijime",
    "教育政策": "policy",
    "学習指導要領": "curriculum",
    "子どもの権利": "childrights",
    "教員不足": "teachershort",
    "働き方改革": "workstyle",
    "AI": "ai",
    "ICT": "ict",
    "授業": "lesson",
    "学級経営": "classroom",
    "生徒指導": "guidance",
    "特別支援": "sen",
    "学力": "achievement",
    "教育格差": "equity",
    "入試": "admission",
    "学校制度": "schoolsystem",
}

DEFAULT_LOOKBACK_DAYS = 3
DEFAULT_MAX_ITEMS = 5

# ロギング
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
)
logger = logging.getLogger(__name__)


# --------------------------------------------------------------------------
# RSS 取得・パース
# --------------------------------------------------------------------------


def fetch_rss(url: str, lookback_days: int = DEFAULT_LOOKBACK_DAYS) -> List[Dict[str, Any]]:
    """RSS フィードから最新記事を取得する.

    Args:
        url: RSS フィード URL
        lookback_days: 何日前までの記事を対象にするか

    Returns:
        記事情報のリスト（最新順）
    """
    logger.info(f"RSS を取得中: {url}")

    try:
        feed = feedparser.parse(url)
    except Exception as e:
        logger.error(f"RSS パース エラー: {e}")
        return []

    if feed.bozo and feed.bozo_exception:
        logger.warning(f"RSS パース警告: {feed.bozo_exception}")

    entries = feed.get("entries", [])
    logger.info(f"取得した項目数: {len(entries)}")

    now_jst = _dt.datetime.now(JST)
    cutoff_date = now_jst - _dt.timedelta(days=lookback_days)

    items = []
    for entry in entries:
        # 公開日を取得（最初に見つかったタイムスタンプを使用）
        pub_date = None
        for date_key in ["published_parsed", "updated_parsed"]:
            if date_key in entry:
                try:
                    parsed_time = entry[date_key]
                    dt = _dt.datetime.fromtimestamp(
                        _dt.datetime.fromtimestamp(0).timestamp()
                    )
                    # feedparser の struct_time を datetime に変換
                    dt = _dt.datetime(
                        year=parsed_time.tm_year,
                        month=parsed_time.tm_mon,
                        day=parsed_time.tm_mday,
                        hour=parsed_time.tm_hour,
                        minute=parsed_time.tm_min,
                        second=parsed_time.tm_sec,
                        tzinfo=_dt.timezone.utc,
                    )
                    pub_date = dt
                    break
                except Exception:
                    pass

        # 日付が取得できない場合は現在時刻を使用
        if not pub_date:
            pub_date = _dt.datetime.now(_dt.timezone.utc)

        # ローカル時間に変換
        pub_date_local = pub_date.astimezone(JST).date()

        # 日付フィルタ
        if pub_date_local < cutoff_date.date():
            continue

        # 記事情報を抽出
        title = entry.get("title", "").strip()
        link = entry.get("link", "").strip()
        summary = entry.get("summary", "").strip()

        if not title or not link:
            continue

        # タイトルから HTML タグを削除
        title = feedparser._FeedParserMixin._sanitize_html(title, "utf-8")
        summary = feedparser._FeedParserMixin._sanitize_html(summary, "utf-8")

        items.append({
            "title": title,
            "link": link,
            "summary": summary,
            "published_date": pub_date_local.isoformat(),
        })

    logger.info(f"フィルタ後: {len(items)} 件（直近 {lookback_days} 日以内）")
    return items


def categorize_article(title: str, summary: str) -> List[str]:
    """タイトルと要約からカテゴリーを推測する.

    Args:
        title: 記事タイトル
        summary: 記事要約

    Returns:
        カテゴリー ID のリスト（最大3個）
    """
    text = f"{title} {summary}".lower()
    categories = set()

    for keyword, category_id in KEYWORD_TO_CATEGORY.items():
        if keyword.lower() in text:
            categories.add(category_id)

    # デフォルトは 'policy'
    if not categories:
        categories.add("policy")

    return list(categories)[:3]  # 最大3個


def convert_to_update_format(
    items: List[Dict[str, Any]],
    max_items: int = DEFAULT_MAX_ITEMS,
) -> Dict[str, Any]:
    """RSS 項目を update_news.py のフォーマットに変換する.

    Args:
        items: RSS から取得した項目
        max_items: 最大何件まで含めるか

    Returns:
        update_news.py で取り込めるフォーマット
    """
    formatted_items = []

    for item in items[:max_items]:
        # ニュース本文の生成（RSS のサマリーを使用）
        what_happened = item["summary"][:300] if item["summary"] else item["title"]

        # 教員への関連性の解釈（RSS には含まれていないため、簡易版）
        why_important = "文部科学省からの公式発表です。教育現場への影響の可能性があります。"

        # 問い
        question = "この発表があなたの学校・学級・授業にどのような影響を与える可能性がありますか？"

        formatted_items.append({
            "title": item["title"][:90],
            "one_line": item["title"][:90],
            "what_happened": what_happened[:520],
            "why_important": why_important[:460],
            "question": question[:220],
            "published_date": item["published_date"],
            "importance": 3,  # RSS のみではスコア付けできないため、デフォルト値
            "categories": categorize_article(item["title"], item["summary"]),
            "sources": [
                {
                    "title": item["title"],
                    "publisher": "文部科学省",
                    "url": item["link"],
                }
            ],
        })

    return {"items": formatted_items}


# --------------------------------------------------------------------------
# メイン
# --------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="教育ニュース RSS フィード自動取得"
    )
    parser.add_argument(
        "--lookback-days",
        type=int,
        default=DEFAULT_LOOKBACK_DAYS,
        help=f"何日前までのニュースを対象にするか（デフォルト: {DEFAULT_LOOKBACK_DAYS}）",
    )
    parser.add_argument(
        "--max-items",
        type=int,
        default=DEFAULT_MAX_ITEMS,
        help=f"最大何件まで取得するか（デフォルト: {DEFAULT_MAX_ITEMS}）",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="出力先ファイル（省略時は stdout）",
    )
    args = parser.parse_args()

    all_items = []

    # RSS フィード取得
    for publisher, url in RSS_FEEDS.items():
        try:
            items = fetch_rss(url, lookback_days=args.lookback_days)
            all_items.extend(items)
        except Exception as e:
            logger.error(f"{publisher} からの取得に失敗: {e}")

    if not all_items:
        logger.warning("新しいニュースが見つかりませんでした")
        output = {"items": []}
    else:
        # 日付順でソート（新しい順）
        all_items.sort(key=lambda x: x["published_date"], reverse=True)
        output = convert_to_update_format(all_items, max_items=args.max_items)

    # JSON を出力
    output_json = json.dumps(output, ensure_ascii=False, indent=2)

    if args.output:
        Path(args.output).write_text(output_json, encoding="utf-8")
        logger.info(f"出力: {args.output}")
    else:
        print(output_json)

    return 0


if __name__ == "__main__":
    sys.exit(main())
