# -*- coding: utf-8 -*-
"""単元計画 A4 1枚（教師用）。14時間の流れ・カード・説明サイン・評価・小テストと宿題の時期。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a4_sheet import build

# (時, 内容, 教科書, カード, 主な活動, 説明サイン, 評価, 配るもの・小テスト)
ROWS = [
 (1, "単元のゴール・見方考え方・ルーブリック・証明の型", "p.148-149", "—",
  "ふせんを折り、重なった部分を見る（結論は出さない）", "どこに目をつけたか", "態○", ""),
 (2, "二等辺三角形の性質", "p.149-152", "⑪⑫",
  "底角が等しいことを合同から証明。JUMP 補助線は二等分線でなくてよいか", "どの合同を使ったか", "知○ 思○", ""),
 (3, "逆と反例・二等辺三角形になるための条件", "p.153-154", "⑬",
  "逆をつくり、反例で判定。JUMP 第1時のふせんの回収", "反例を見せる", "知○ 思○", ""),
 (4, "証明を読む・書く", "p.154-157", "—",
  "足りない証明を直す。JUMP 練習プリント①の5", "自分の証明を読み上げる", "思◎", ""),
 (5, "直角三角形の合同", "p.158-160", "⑭⑮",
  "⑭⑮はなぜ使えるか（③・⑪にもちこむ）。JUMP ⑭⑮を使わずに", "どの合同条件にもちこんだか", "知○ 思○", ""),
 (6, "確かめよう（1節）", "p.161", "—",
  "演習14問（カードを自分で選ぶ）", "カードを選んだ理由", "知◎", "宿題① 配布"),
 (7, "平行四辺形の性質", "p.162-165", "⑯⑰⑱",
  "定義から性質を導く。JUMP 対角線がそれぞれの中点で交わる", "定義だけから導いたか", "思○", "小テスト①"),
 (8, "平行四辺形になるための条件", "p.166-169", "⑲〜㉒",
  "㉒を丁寧に（例2・問8）。練習とJUMP", "あと何がいえればよいか", "思○", ""),
 (9, "平行四辺形の練習", "p.165-169", "—",
  "演習（性質と条件の使い分け）", "性質と条件を分けて", "知◎", ""),
 (10, "特別な四角形", "p.170-172", "—",
  "長方形・ひし形・正方形を定義と対角線で。たくさん書き出す", "定義にもどって", "知○ 思○", "宿題② 配布"),
 (11, "平行線と面積", "3節", "㉓",
  "等積変形。AC∥EF（3組の平行線）。2枚目 発展プリント（面積比）", "どの平行線を使ったか", "知○ 思○",
  "小テスト②<br>宿題③ 配布"),
 (12, "確かめよう（2節・3節）", "p.173", "—",
  "演習（性質と条件を区別して選ぶ）", "選ばなかったものの反例", "知◎", "小テスト③"),
 (13, "章末の問題（基本・応用）", "p.175-176", "—",
  "演習（13枚から選ぶ）", "カードを選んだ理由", "思◎", ""),
 (14, "深めよう・単元を貫く課題の検討", "p.177", "—",
  "条件を変えて何が残るか。課題に自分の答えを書く", "どこが変わり、どこが残るか", "思◎ 態◎", ""),
]

who = lambda n: '<span class="tag" style="color:var(--accent)">教師</span>' if n <= 3 else ""
rows = "".join(
    '<tr><td class="c"><b>%d</b></td><td>%s %s <span class="inst">%s</span></td><td class="c">%s</td>'
    '<td>%s <span class="inst">／サイン: %s</span></td><td class="c">%s</td><td class="c">%s</td></tr>'
    % (n, t, who(n), pg, c, act, sg, ev, dist or "")
    for n, t, pg, c, act, sg, ev, dist in ROWS)

body = """
<style>
.row>*{min-width:0}
.plan td,.plan th{line-height:1.32}
@media print{ .plan{font-size:7.9pt} .plan td,.plan th{padding:.7mm 1.2mm} .box p{font-size:8.6pt; line-height:1.42} .box h2{font-size:9.6pt} .plan .inst{font-size:7.4pt} }
</style>
<div class="row c2" style="grid-template-columns:1.25fr 1fr; align-items:stretch; margin-top:6px">
<div class="box" style="margin-top:0"><h2>単元の目標</h2>
<p style="margin:0"><b>知識・技能</b>　二等辺三角形・直角三角形・平行四辺形の性質や条件、平行線と面積の関係を理解し、
角や長さを求めたり、根拠を明らかにして証明を書いたりできる。<br>
<b>思考・判断・表現</b>　根拠となることがらを選んで筋道立てて証明できる。逆を考えて反例で判断し、
条件を変えたときに何が成り立つかを考えられる。<br>
<b>主体的に学習に取り組む態度</b>　証明のよさに気づき、学び合いの中で自分の考えを説明し、
人の説明を吟味して考えを深めようとしている。</p></div>
<div class="box" style="margin-top:0"><h2>単元を貫く課題</h2>
<p style="margin:0; font-family:var(--serif); font-weight:700">「かならずそうなる」と言えるのは、どんなときか。</p>
<p class="inst" style="margin:2px 0 0">第1時に問い、第3時で回収、第14時に自分の答え。</p>
<h2 style="margin-top:5px">進め方</h2>
<p style="margin:0"><b>第1〜3時は教師</b>、第4時から<b>学び合い</b>。各時間に<b>説明サイン</b>
（男女1名ずつに説明し、納得できたらサイン）。カード⑪〜㉓は証明して手に入れた順に増やす。</p></div>
</div>

<section class="q"><h3><span class="n">1</span><span class="t">指導計画（全14時間）</span>
<span class="pt">評価　◎ 記録に残す　○ 指導に生かす</span></h3>
<table class="plan" style="margin-top:4px">
<tr><th class="c">時</th><th>学習内容・教科書</th><th class="c">カード</th><th>主な活動／説明サイン</th>
<th class="c">評価</th><th class="c">小テスト・宿題</th></tr>
%s
<tr><td class="c"><b>後</b></td><td colspan="5"><b>単元テスト</b>（リピートプリント 5章）　知識・技能 68点／思考・判断・表現 32点</td></tr>
</table></section>

<div class="row c2" style="grid-template-columns:1.25fr 1fr; align-items:start">
<section class="q"><h3><span class="n">2</span><span class="t">評価計画</span><span class="pt"></span></h3>
<table class="plan" style="margin-top:4px">
<tr><th>観点</th><th>主な評価場面</th></tr>
<tr><td><b>知識・技能</b></td><td>確かめよう（第6・12時）・練習（第9時）、小テスト①〜③の【知】、単元テスト（68点）</td></tr>
<tr><td><b>思考・判断<br>・表現</b></td><td>証明を書く時間（第4・13・14時）のワークシート、説明サイン、小テスト①〜③の【思】、単元テスト（32点・証明の穴うめ）</td></tr>
<tr><td><b>態度</b></td><td>第1・14時の記述（単元を貫く課題）、アプリのふりかえり、説明サインでの説明・吟味</td></tr>
</table></section>
<section class="q"><h3><span class="n">3</span><span class="t">日程の目安（週3時間）</span><span class="pt"></span></h3>
<p style="margin:4px 0 0; font-size:8.4pt; line-height:1.6">11/23の週 第1〜3時（教師）／11/30の週 第4〜6時<br>12/7の週 第7〜9時／12/14の週 第10〜12時<br>12/21の週 第13・14時／1/8〜1/22 単元テスト・予備</p>
<p class="inst" style="margin:2px 0 0">祝日・行事で前後する。学び合いが速ければ前倒し。</p></section>
</div>
""" % rows

SHEET = dict(
    kind="単元計画", title="5章 三角形・四角形（全14時間）",
    right='<span class="nm"><span>学校図書『中学校 数学2』p.148〜177</span></span>',
    lead="中学2年 数学　小テスト（10分・20点）と宿題プリントは節ごとに3回。根拠カード（A4 1枚）は第2時に配る。",
    body=body,
    footer="中学2年 数学　5章 三角形・四角形　単元計画／A4",
)

if __name__ == "__main__":
    print(build(SHEET, sys.argv[1]), "bytes")
