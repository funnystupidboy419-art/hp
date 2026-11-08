# -*- coding: utf-8 -*-
"""第2時 二等辺三角形の性質（学校図書『数学2』p.149-151）教師主導"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a3_sheet import build, angle_arc, angle_deg, tick, right_angle, z, rz, fig

A, B, C, D = (100, 18), (45, 124), (155, 124), (100, 124)
# ② の図は印を入れない。印が入っていると定義が図から読めてしまう。
f1 = "".join([
    '<polygon class="l" points="100,18 45,124 155,124"/>',
    '<g class="ft">%s%s</g>' % (tick(A, B, cls="ftline"), tick(A, C, cls="ftline")),
    '<text class="t" x="100" y="12" text-anchor="middle">A</text>',
    '<text class="t" x="35" y="134">B</text><text class="t" x="159" y="134">C</text>',
])
f2 = "".join([
    '<polygon class="l" points="100,18 45,124 155,124"/>',
    '<line class="l" x1="100" y1="18" x2="100" y2="124"/>',
    tick(A, B), tick(A, C),
    angle_arc(A, B, D, 22), angle_arc(A, D, C, 22),
    '<text class="t" x="100" y="12" text-anchor="middle">A</text>',
    '<text class="t" x="35" y="134">B</text><text class="t" x="159" y="134">C</text>',
    '<text class="t" x="100" y="138" text-anchor="middle">D</text>',
])
aA, aB, aC = (100, 20), (50.6, 126), (149.4, 126)
assert abs(angle_deg(aA, aB, aC) - 50) < 0.1
f_a = "".join([
    '<polygon class="l" points="100,20 50.6,126 149.4,126"/>',
    tick(aA, aB), tick(aA, aC), angle_arc(aA, aB, aC, 24),
    '<text class="t" x="100" y="54" text-anchor="middle">50°</text>',
    '<text class="t" x="100" y="14" text-anchor="middle">A</text>',
    '<text class="t" x="40" y="136">B</text><text class="t" x="153" y="136">C</text>',
    '<text class="t" x="58" y="120"><tspan font-style="italic">x</tspan></text>',
])
bA, bB, bC, bX = (100, 28), (24.5, 118), (175.5, 118), (208, 118)
assert abs(angle_deg(bA, bB, bC) - 80) < 0.1 and abs(angle_deg(bC, bA, bX) - 130) < 0.1
f_b = "".join([
    '<polygon class="l" points="100,28 24.5,118 175.5,118"/>',
    '<line class="l" x1="175.5" y1="118" x2="208" y2="118"/>',
    tick(bA, bB), tick(bA, bC), angle_arc(bC, bA, bX, 12),
    '<text class="t" x="100" y="22" text-anchor="middle">A</text>',
    '<text class="t" x="14" y="130">B</text><text class="t" x="172" y="132">C</text>',
    '<text class="t" x="176" y="104">130°</text>',
    '<text class="t" x="100" y="56" text-anchor="middle"><tspan font-style="italic">x</tspan></text>',
])
jA, jB, jC, jM = (65, 12), (25, 96), (105, 96), (65, 96)
f_m = "".join([
    '<polygon class="l" points="65,12 25,96 105,96"/>',
    '<line class="l" x1="65" y1="12" x2="65" y2="96"/>',
    tick(jA, jB), tick(jA, jC), tick(jB, jM, 2), tick(jM, jC, 2),
    '<text class="t" x="65" y="8" text-anchor="middle">A</text>',
    '<text class="t" x="16" y="106">B</text><text class="t" x="108" y="106">C</text>',
    '<text class="t" x="65" y="110" text-anchor="middle">M</text>',
])
f_h = "".join([
    '<polygon class="l" points="65,12 25,96 105,96"/>',
    '<line class="l" x1="65" y1="12" x2="65" y2="96"/>',
    tick(jA, jB), tick(jA, jC), right_angle(jM, jC, jA, 7),
    '<text class="t" x="65" y="8" text-anchor="middle">A</text>',
    '<text class="t" x="16" y="106">B</text><text class="t" x="108" y="106">C</text>',
    '<text class="t" x="65" y="110" text-anchor="middle">H</text>',
])

SHEET = dict(
    title="底角はなぜ等しいのか",
    ji="第2時",
    pg="学校図書『数学2』p.149-151／1節 三角形（全18時間・この時間は先生と進む）",
    goal="二等辺三角形の底角が等しいことを、合同を使って説明できる。",
    katari="「2つの角が同じ」は小学校で<b>確かめました</b>。今日やるのは、それが"
           "<b>どんな二等辺三角形でも</b>言えると示すことです。確かめたことと、証明したことはちがいます。",
    cards_title="根拠カード — 今日の新しいカードは ⑪ の1枚",
    cards_hint="①②③は見てよい。⑪は、今日の証明が終わってから使えるようになる。"
               "<b>証明が終わる前に ⑪ を根拠に使ってはいけない。</b>",
    cards=[("①", "3組の辺がそれぞれ等しい（4章）"),
           ("②", "2組の辺とその間の角がそれぞれ等しい（4章）"),
           ("③", "1組の辺とその両端の角がそれぞれ等しい（4章）"),
           ("⑪", "<b>二等辺三角形の2つの底角は等しい</b>（今日つくるカード）")],
    footer="中学2年 数学　5章 三角形・四角形（全18時間）　第2時 二等辺三角形の性質／A3横・5ブロック",
    memo="<b>この時間は先生と一緒に進む。</b>③(1) の〈考え方〉を全員で埋めてから書かせる。<br>"
         "<b>削り順</b>　③(2) を宿題 → ④② を宿題。死守するのは ③(1) と ④①。<br>"
         "④② を削ると第6時の伏線が消えるので、宿題にしてでも残す。",
    blocks=[
"""    <p class="inst">4章の合同条件。隣の人に1つ説明する。</p>
    <ol>
      <li>合同条件は全部で %s つ</li>
      <li>隣の人に説明した番号 %s</li>
    </ol>
    <div class="spacer"></div>
    <p class="inst">今日はこの3つのうち<b>どれか1つ</b>を使って証明する。</p>"""
% (z("3"), z("", "w")),

"""    <p><b>二等辺三角形の定義</b>を書く。</p>
    <p class="inst">%s を二等辺三角形という。</p>
    %s
    <p class="inst">図1の次の部分を、それぞれ何というか。</p>
    <p class="inst"><b>頂角</b>＝%s　<b>底辺</b>＝%s　<b>底角</b>＝%s</p>
    <p class="inst">書けたら、<b>等しい辺に自分で印をつける</b>。</p>
    <div class="spacer"></div>
    <p class="inst" style="border-top:1px dotted var(--rule); padding-top:5px">
      <b>今日の問い</b>　∠B＝∠C は、<b>どんな</b>二等辺三角形でも言えるか。</p>"""
% (z("2つの辺が等しい三角形", "ww"), fig("0 0 200 148", f1, "図1　AB＝AC"),
   z("∠A", "w"), z("BC", "w"), z("∠B と ∠C", "ww")),

"""    <ol>
      <li><b>∠B＝∠C を証明する。</b>
        <div class="think">
          <p class="th">考え方</p>
          <p>・∠B と ∠C が等しいというには、この2つを %s な2つの三角形の
            「対応する角」にすればよい。</p>
          <p>・そのために、△ABC を2つの三角形に分ける線を、頂点 A から1本ひく。</p>
          <p>・ひいた線は、2つの三角形に %s な辺になる。
            あと1組、等しいといえるものがいる。</p>
          <p>・だから、ひく線は %s</p>
        </div>
        %s
        <span class="inst">使う合同条件</span>%s
        <span class="inst">選んだ理由</span>%s
        %s</li>
      <li>∠<i>x</i> を求める。カードの番号も書く。
        <div class="figs">%s%s</div>
        (ア) <i>x</i>＝%s°　<span class="cn">カード</span>%s　
        (イ) <i>x</i>＝%s°　<span class="cn">カード</span>%s</li>
    </ol>"""
% (z("合同", "w"), z("共通", "w"), z("∠A の二等分線", "ww"),
   fig("0 0 200 150", f2, "図2　AD は ∠A の二等分線"),
   z("②"), z("辺2つとその間の角が言えるから", "ww"),
   rz(6, "△ABD と △ACD において<br>"
         "仮定より　AB＝AC　……(a)<br>"
         "AD は ∠A の二等分線だから　∠BAD＝∠CAD　……(b)<br>"
         "AD は共通　……(c)<br>"
         "(a)(b)(c)より、<b>カード②</b>（2組の辺とその間の角）から　△ABD≡△ACD<br>"
         "合同な図形では対応する角は等しいから　∠B＝∠C　■"),
   fig("0 0 200 145", f_a, "(ア)", "115px"), fig("0 0 215 145", f_b, "(イ)", "115px"),
   z("65"), z("⑪"), z("80"), z("⑪")),

"""    <p><b>補助線は、二等分線でなくてもよいのだろうか。</b></p>
    <div class="figs">%s%s</div>
    <ol class="circ">
      <li>(1) の図で、∠B＝∠C を証明できますか。できるなら書きなさい。
        %s</li>
      <li>(2) の図ではどうですか。<b>できないなら、なぜできないのかを書きなさい。</b>
        %s</li>
    </ol>
    <p class="hw">※ (1)(2) の図はまったく同じに見える。ちがうのは<b>何を仮定にしたか</b>。</p>"""
% (fig("0 0 130 118", f_m, "(1) AB＝AC、BM＝CM（2本線）", "110px"),
   fig("0 0 130 118", f_h, "(2) AB＝AC、AH⊥BC", "110px"),
   rz(3, "<b>できる。</b>△ABM と △ACM で、AB＝AC（仮定）、BM＝CM（仮定）、AM は共通。"
         "<b>カード①</b>（3組の辺）から合同。よって ∠B＝∠C。"),
   rz(3, "<b>いまの知識ではできない。</b>言えるのは AB＝AC、AH は共通、∠AHB＝∠AHC＝90° の3つ。"
         "辺2つと角1つだが、<b>その角が2辺の間にない</b>ので カード② は使えない。①③も足りない。<br>"
         "→ 合同と言うには<b>新しい条件</b>がいる。第6時「直角三角形の合同」でそれをつくる。")),
None,
])

if __name__ == "__main__":
    print(build(SHEET, sys.argv[1]), "bytes")
