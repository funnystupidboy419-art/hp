# -*- coding: utf-8 -*-
"""第2時 二等辺三角形の性質（学校図書『数学2』p.149-152）教師主導
   ⑪と⑫を、同じ1つの合同から取り出す。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a3_sheet import build, angle_arc, angle_deg, tick, right_angle, z, rz, bz, fig, memo

A, B, C, D = (100, 18), (45, 124), (155, 124), (100, 124)
# ② の図は印を入れない。印があると定義が図から読めてしまう。印は生徒が自分で書く。
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
    '<g class="ft">%s%s%s</g>' % (right_angle(D, C, A, 8, "ftline"),
                                  tick(B, D, 2, cls="ftline"), tick(D, C, 2, cls="ftline")),
    '<text class="t" x="100" y="12" text-anchor="middle">A</text>',
    '<text class="t" x="35" y="134">B</text><text class="t" x="159" y="134">C</text>',
    '<text class="t" x="100" y="138" text-anchor="middle">D</text>',
])
aA, aB, aC = (100, 20), (50.6, 126), (149.4, 126)
assert abs(angle_deg(aA, aB, aC) - 50) < 0.1
f_a = "".join([
    '<polygon class="l" points="100,20 50.6,126 149.4,126"/>',
    tick(aA, aB), tick(aA, aC),
    angle_arc(aA, aB, aC, 24), angle_arc(aB, aC, aA, 17),
    '<text class="t" x="100" y="54" text-anchor="middle">50°</text>',
    '<text class="t" x="100" y="14" text-anchor="middle">A</text>',
    '<text class="t" x="40" y="136">B</text><text class="t" x="153" y="136">C</text>',
    '<text class="t" x="63" y="117"><tspan font-style="italic">x</tspan></text>',
])
bA, bB, bC, bX = (100, 28), (24.5, 118), (175.5, 118), (208, 118)
assert abs(angle_deg(bA, bB, bC) - 80) < 0.1 and abs(angle_deg(bC, bA, bX) - 130) < 0.1
f_b = "".join([
    '<polygon class="l" points="100,28 24.5,118 175.5,118"/>',
    '<line class="l" x1="175.5" y1="118" x2="208" y2="118"/>',
    tick(bA, bB), tick(bA, bC),
    angle_arc(bC, bA, bX, 12), angle_arc(bA, bB, bC, 20),
    '<text class="t" x="100" y="22" text-anchor="middle">A</text>',
    '<text class="t" x="14" y="130">B</text><text class="t" x="172" y="132">C</text>',
    '<text class="t" x="176" y="104">130°</text>',
    '<text class="t" x="100" y="58" text-anchor="middle"><tspan font-style="italic">x</tspan></text>',
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
    pg="学校図書『数学2』p.149-152／1節 三角形（全14時間・この時間は先生と進む）",
    goal="二等辺三角形の底角が等しいことを合同から説明し、同じ合同から他のことも取り出せる。",
    katari="「2つの角が同じ」は小学校で<b>確かめました</b>。今日やるのは、それが"
           "<b>どんな二等辺三角形でも</b>言えると示すことです。<br>"
           "そして、1回の証明から取り出せることは<b>1つだけではありません</b>。",
    cards_title="今日手に入れるカードは ⑪ と ⑫ の2枚（別紙のカードを用意）",
    cards_hint="4章の ①②③ は使ってよい。⑪⑫ は、③で取り出してから使えるようになる。",
    cards=[("①", "3組の辺がそれぞれ等しい（4章）"),
           ("②", "2組の辺とその間の角がそれぞれ等しい（4章）"),
           ("③", "1組の辺とその両端の角がそれぞれ等しい（4章）"),
           ("⑪⑫", "二等辺三角形について。今日 ③ で取り出す")],
    footer="中学2年 数学　5章 三角形・四角形（全14時間）　第2時 二等辺三角形の性質／A3横",
    blocks=[
# ①
"""    <p class="inst">三角形の合同条件を<b>3種類、自分で書く</b>。</p>
    %s
    <p class="inst" style="margin-top:6px">書けたら、<b>隣の人に暗唱する</b>。
      見ないで言えたら合格。言えなかったものに印をつけておく。</p>
    <div class="spacer"></div>
    <p class="inst">今日はこの3つのうち、<b>どれか1つ</b>を使って証明する。</p>"""
% rz(6, "① 3組の辺がそれぞれ等しい<br>② 2組の辺とその間の角がそれぞれ等しい<br>"
        "③ 1組の辺とその両端の角がそれぞれ等しい"),

# ②
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

# ③
"""    <ol>
      <li><b>∠B＝∠C を証明する。</b>
        <div class="think">
          <p class="th">考え方</p>
          <p>・∠B と ∠C が等しいというには、この2つを %s な2つの三角形の
            「対応する角」にすればよい。</p>
          <p>・そのために、△ABC を2つの三角形に分ける線を、頂点 A から1本ひく。</p>
          <p>・ひいた線は、2つの三角形に %s な辺になる。あと1組、等しいといえるものがいる。</p>
          <p>・だから、ひく線は %s</p>
        </div>
        %s
        <span class="inst">使う条件をことばで</span>%s
        %s</li>
      <li><b>いま示した合同から、ほかに辺や角で等しくなるところを書き出そう。</b>
        %s</li>
      <li>∠<i>x</i> を求める。
        <div class="figs">%s%s</div>
        (ア) <i>x</i>＝%s°　　(イ) <i>x</i>＝%s°</li>
    </ol>"""
% (z("合同", "w"), z("共通", "w"), z("∠A の二等分線", "ww"),
   fig("0 0 200 150", f2, "図2　AD は ∠A の二等分線"),
   z("②"),
   bz(40, "△ABD と △ACD において<br>"
          "仮定より　AB＝AC　……(a)<br>"
          "AD は ∠A の二等分線だから　∠BAD＝∠CAD　……(b)<br>"
          "AD は共通　……(c)<br>"
          "(a)(b)(c)より、2組の辺とその間の角がそれぞれ等しいから（<b>根拠②</b>）　△ABD≡△ACD<br>"
          "合同な図形では対応する角は等しいから　∠B＝∠C　■　→ これが<b>根拠⑪</b>"),
   bz(26, "BD＝CD（対応する辺）／∠ADB＝∠ADC（対応する角）<br>"
          "∠ADB＋∠ADC＝180°（一直線）で、しかも等しいから ∠ADB＝90°。<br>"
          "合わせると「頂角の二等分線は底辺を<b>垂直に2等分する</b>」→ これが<b>根拠⑫</b>"),
   fig("0 0 200 145", f_a, "(ア)", "115px"), fig("0 0 215 145", f_b, "(イ)", "115px"),
   z("65"), z("80")),

# ④
"""    <p><b>補助線は、二等分線でなくてもよいのだろうか。</b></p>
    <div class="figs">%s%s</div>
    <ol class="circ">
      <li>(1) の図で、∠B＝∠C を証明できますか。できるなら書きなさい。
        %s</li>
      <li>(2) の図ではどうですか。<b>できないなら、なぜできないのかを書きなさい。</b>
        %s</li>
    </ol>
    <p class="hw">※ (1)(2) の図はまったく同じに見える。ちがうのは<b>何を仮定にしたか</b>。</p>
    %s"""
% (fig("0 0 130 118", f_m, "(1) AB＝AC、BM＝CM（2本線）", "110px"),
   fig("0 0 130 118", f_h, "(2) AB＝AC、AH⊥BC", "110px"),
   bz(26, "<b>できる。</b>△ABM と △ACM で、AB＝AC（仮定）、BM＝CM（仮定）、AM は共通。"
          "3組の辺がそれぞれ等しいから（<b>根拠①</b>）合同。よって ∠B＝∠C。"),
   bz(26, "<b>いまの知識ではできない。</b>言えるのは AB＝AC、AH は共通、∠AHB＝∠AHC＝90° の3つ。"
          "辺2つと角1つだが、<b>その角が2辺の間にない</b>ので 「2組の辺とその間の角」（根拠②）は使えない。①③も足りない。<br>"
          "→ 第5時「直角三角形の合同」で、この足りないぶんをつくる。"),
   memo("<b>この時間は先生と一緒に進む。</b>③(1) の〈考え方〉を全員で埋めてから書かせる。<br>"
        "③(2) が今日のもう1つの山。<b>1回の合同から取り出せることは1つではない。</b><br>"
        "<b>削り順</b>　③(3) を宿題 → ④② を宿題。死守するのは ③(1)(2) と ④①。<br>"
        "④② を削ると第5時の伏線が消えるので、宿題にしてでも残す。")),
])

if __name__ == "__main__":
    print(build(SHEET, sys.argv[1]), "bytes")
