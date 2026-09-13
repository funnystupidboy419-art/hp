# CLAUDE.md — このリポジトリでの作業ルール

教員向けの教育時事サイト。公開URL: https://funnystupidboy419-art.github.io/hp/

## 絶対に守ること

1. **記事の内容で `index.html` を編集しない。** ニュースの追加・修正は `data/news.json` に対してのみ行う。
   HTML は表示の枠であり、内容は `assets/js/app.js` が JSON から描画する。
2. **`data/news.json` を手で書き換えない。** 必ず `scripts/update_news.py` を通す。
   サニタイズ・重複排除・ID採番・アトミック書き込みがこのスクリプトに集約されている。
3. **過去記事を消さない。** 追記のみ。
4. **push 前に必ず `python scripts/validate_site.py` を通す。** 失敗したら push しない。
5. **児童生徒・保護者・個々の教職員など、個人が特定される情報は書かない。**
6. **候補の承認を得てから書き込む。** `scripts/update_news.py` を実行する前に、
   候補の見出しと出典 URL を提示して承認を得る。判断は人、整形は機械。

---

# 毎朝の更新手順

手順の本体は `.claude/commands/news.md` にある。**会話では `/news` と打つ。**

`/news` が行うこと:

1. 既存記事の見出しと URL を読み、再掲を防ぐ
2. 直近3日の教育ニュースを調べる（下調べは `news-scout` サブエージェントに任せてよい）
3. **候補の一覧を提示して、承認を待つ** ← ここで必ず止まる
4. 承認されたものだけを記事にし、`/tmp/items.json` に書き出す
5. `update_news.py --dry-run` → 保存 → `validate_site.py` → commit / push
6. 追加した記事と、見送った理由を報告

選定基準・情報源の優先順位・JSON の書式・カテゴリー一覧も、すべてコマンド本体に書いてある。

手順を変えたいときは `.claude/commands/news.md` を直す。
**この CLAUDE.md に手順を書き戻さない。** 二重管理になり、食い違ったときにどちらが正か分からなくなる。

---

# 開発時のメモ

```bash
python3 scripts/test_update_news.py    # オフラインテスト（APIキー不要）
python3 scripts/validate_site.py       # データ・HTML・秘密情報の検証
python3 -m http.server 8000            # ローカル表示 http://localhost:8000/
```

- `.github/workflows/daily-education-news.yml` は **API キー方式の自動更新**（現在は Secret 未設定のため動かない）。
  Claude Code の定期実行で運用している間は不要だが、将来の切り替え用に残してある。
- `.github/workflows/validate.yml` は push/PR ごとに走る検証。API キー不要。
- ブランチは `main` のみ。GitHub Pages は `main` / root から公開している。

## `.claude/` の中身

| ファイル | 役割 |
|---|---|
| `.claude/commands/news.md` | `/news` の本体。毎朝の更新手順はここが正。 |
| `.claude/agents/news-scout.md` | 下調べ専用のサブエージェント。候補一覧だけを返し、検索ログを本体の会話に持ち込まない。 |
| `.claude/settings.json` | Stop フック。作業終了時に `validate_site.py` を自動実行し、失敗したら終了コード2で終われなくする。 |

フックは Claude Code の起動時に読み込まれる。設定を変えた直後のセッションでは効かないので、
`/hooks` で確認するか、セッションを開き直すこと。
