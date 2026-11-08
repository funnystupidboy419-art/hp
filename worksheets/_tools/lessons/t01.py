# -*- coding: utf-8 -*-
"""第1時 章の扉・単元の見通し（学校図書『数学2』p.148-149）教師主導の回"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a3_sheet import build, angle_arc, angle_deg, tick, grid, z, rz, fig

# 帯を折ったとき重なってできる三角形
tA, tB, tC = (102.5, 38), (55, 112), (150, 112)
assert abs(((tA[0]-tB[0])**2+(tA[1]-tB[1])**2) - ((tA[0]-tC[0])**2+(tA[1]-tC[1])**2)) < 1e-6
f1 = "".join([
    '<line class="d" x1="8" y1="38" x2="205" y2="38"/>',
    '<line class="d" x1="8" y1="112" x2="205" y2="112"/>',
    '<polygon class="l" points="102.5,38 55,112 150,112" fill="var(--band)"/>',
    '<g class="ft">%s%s%s%s</g>' % (angle_arc(tB, tC, tA, 18, "ftline"), angle_arc(tC, tA, tB, 18, "ftline"),
                                    tick(tA, tB, cls="ftline"), tick(tA, tC, cls="ftline")),
    '<text class="t" x="12" y="34">ℓ</text><text class="t" x="12" y="124">m</text>',
    '<text class="t" x="102.5" y="32" text-anchor="middle">A</text>',
    '<text class="t" x="46" y="124">B</text><text class="t" x="154" y="124">C</text>',
    '<text class="t" x="100" y="90" text-anchor="middle">重なった部分</text>',
])

SHEET = dict(
    title="カードを13枚あつめる",
    ji="第1時",
    pg="学校図書『数学2』p.148-149／5章の扉（全18時間・この時間は先生と進む）",
    goal="この単元で何を手に入れるのかがわかり、証明の書き方を思い出す。",
    katari="これから18時間かけて、<b>根拠カードを13枚あつめます。</b>カードは先生が配るのではなく、"
           "みなさんが証明して手に入れます。第4時からは、先生は教えません。"
           "<b>全員が13枚使えるようになる</b>のがゴールです。",
    cards_title="この単元で手に入れる13枚（いまは1枚も使えなくてよい）",
    cards_hint="⑪〜㉓は、これから自分たちで証明して手に入れるカード。"
               "①〜⑩は4章ですでに持っている。今日はそのうち①②③を思い出す。",
    cards=[("①", "3組の辺がそれぞれ等しい（4章・持っている）"),
           ("②", "2組の辺とその間の角がそれぞれ等しい（4章・持っている）"),
           ("③", "1組の辺とその両端の角がそれぞれ等しい（4章・持っている）"),
           ("⑪〜⑬", "二等辺三角形について（第2〜4時）"),
           ("⑭⑮", "直角三角形の合同について（第6時）"),
           ("⑯〜⑱", "平行四辺形の性質について（第8〜9時）"),
           ("⑲〜㉒", "平行四辺形になるための条件について（第11〜13時）"),
           ("㉓", "平行線と面積について（第16時）")],
    footer="中学2年 数学　5章 三角形・四角形（全18時間）　第1時 単元の見通し／A3横・5ブロック",
    mins=[5, 15, 15, 10, 5],
    names=["4章の思い出し", "この単元でやること", "証明の型を思い出す", "やってみる", "ふりかえり"],
    blocks=[
# ①
"""    <p class="inst">合同条件を3つ。思い出せなければ上の一覧を見てよい。</p>
    <ol>
      <li>%s組の辺がそれぞれ等しい</li>
      <li>%s組の辺とその間の角がそれぞれ等しい</li>
      <li>1組の辺とその%sの角がそれぞれ等しい</li>
    </ol>
    <div class="spacer"></div>
    <p class="inst">この3つが、18時間ずっと土台になる。</p>"""
% (z("3"), z("2"), z("両端", "w")),

# ②
"""    <p><b>ゴール</b>　18時間後に、13枚のカードを<b>全員が</b>使えるようになっている。</p>
    <p class="inst">カードは、証明して手に入れる。配られるのではない。</p>
    <p style="margin-top:8px"><b>第4時からの進め方</b></p>
    <ol>
      <li>先生は教えない。%s（はい／いいえ）</li>
      <li>わからないときは %s に行く</li>
      <li>聞かれたら %s</li>
      <li>自分が終わっても、まだの人がいたら %s</li>
    </ol>
    <p class="inst" style="margin-top:6px">ノートに名前は書く。
      <b>だれができた・できないを紙に書かない。</b></p>
    <div class="spacer"></div>
    <p class="inst" style="border-top:1px dotted var(--rule); padding-top:5px">
      <b>先生が教えるのは第3時まで。</b>そのあとの15時間は、みなさんで進める。</p>"""
% (z("はい", "w"), z("聞きに", "w"), z("答える", "w"), z("まだ終わっていない", "ww")),

# ③
"""    <p class="inst">4章で書いた証明の型。空らんをうめる。</p>
    <div class="badproof">
      <p style="margin:0">△ABC と △DEF において</p>
      <p class="ind" style="margin:2px 0 0;padding-left:1.2em">%s より　AB＝DE　……(a)</p>
      <p class="ind" style="margin:2px 0 0;padding-left:1.2em">%s より　∠B＝∠E　……(b)</p>
      <p class="ind" style="margin:2px 0 0;padding-left:1.2em">仮定より　BC＝EF　……(c)</p>
      <p class="ind" style="margin:2px 0 0;padding-left:1.2em">(a)(b)(c)より、<b>カード%s</b>から</p>
      <p class="ind" style="margin:2px 0 0;padding-left:1.2em">△ABC≡△DEF</p>
      <p class="ind" style="margin:2px 0 0;padding-left:1.2em">合同な図形では%sは等しいから　AC＝DF</p>
    </div>
    <p class="inst" style="margin-top:6px"><b>いちばん大事なのは、根拠を書く列。</b>
      「仮定より」と書けるのは、<b>問題文に書いてあることだけ</b>。</p>"""
% (z("仮定", "w"), z("仮定", "w"), z("②"), z("対応する辺", "ww"),
   ),

# ④
"""    <p class="inst">ふせんを1枚、下の図のように1回折る。<b>重なった部分</b>を見る。</p>
    %s
    <ol class="circ">
      <li>重なった部分は、どんな三角形になりましたか。%s</li>
      <li><b>どんな折り方でも、そうなりますか。</b>ならない折り方があれば、どんな折り方か書く。
        %s</li>
    </ol>"""
% (fig("0 0 215 132", f1, "ℓ と m は、ふせんの2つの辺（平行）"),
   z("二等辺三角形", "ww"),
   rz(3, "折り線が帯を横切るかぎり、いつでも二等辺三角形になる。<br>"
         "理由（第2時以降で扱う）: ℓ∥m の錯角と、折り返しで重なる角が等しいので、2つの角が等しくなる。<br>"
         "ここでは「いつでもそうなりそうだ」まででよい。<b>「いつでも」を示すのが証明</b>だと伝える。")),

# ⑤
"""    <ol>
      <li>5章のカードで、いま使えるのは %s枚</li>
      <li>18時間後は %s枚</li>
    </ol>
    <div class="spacer"></div>
    <p class="inst tonly" style="border-top:1px dotted var(--rule); padding-top:5px">
      <b>この時間の役割</b>　ゴールの提示と約束。急がない。<br>
      ③で「仮定より」の意味を1回言っておくと、第2時が速い。<b>問題文にないものを「仮定より」と
      書いた時点で、その証明は通らない</b>——ここを1回だけ強く言う。<br>
      ④は結論を出さずに終えてよい。「いつでも」が第2時からの仕事。<br>
      <b>削り順</b>　④② → ③の後半。死守するのは ② の約束と ③ の根拠の列。</p>"""
% (z("0"), z("13")),
])

if __name__ == "__main__":
    print(build(SHEET, sys.argv[1]), "bytes")
