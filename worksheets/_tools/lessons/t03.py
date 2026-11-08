# -*- coding: utf-8 -*-
"""第3時 二等辺三角形の頂角の二等分線（学校図書『数学2』p.152）"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a3_sheet import build, angle_arc, angle_deg, tick, right_angle, grid, z, rz, fig

# ---- 図1 二等辺三角形と頂角の二等分線 ----
A, B, C, D = (100, 18), (45, 124), (155, 124), (100, 124)
f1 = "".join([
    '<polygon class="l" points="100,18 45,124 155,124"/>',
    '<line class="l" x1="100" y1="18" x2="100" y2="124"/>',
    tick(A, B), tick(A, C),
    angle_arc(A, B, D, 22), angle_arc(A, D, C, 22),
    '<g class="ft">%s%s%s</g>' % (right_angle(D, C, A, 8, "ftline"), tick(B, D, 2, cls="ftline"), tick(D, C, 2, cls="ftline")),
    '<text class="t" x="100" y="12" text-anchor="middle">A</text>',
    '<text class="t" x="35" y="134">B</text><text class="t" x="159" y="134">C</text>',
    '<text class="t" x="100" y="138" text-anchor="middle">D</text>',
])

# ---- 図2 たこ形 ----
kA, kB, kC, kD, kO = (75, 14), (25, 70), (75, 130), (125, 70), (75, 70)
f3 = "".join([
    '<polygon class="l" points="75,14 25,70 75,130 125,70"/>',
    '<line class="l" x1="75" y1="14" x2="75" y2="130"/>',
    '<line class="l" x1="25" y1="70" x2="125" y2="70"/>',
    tick(kA, kB), tick(kA, kD), tick(kC, kB, 2), tick(kC, kD, 2),
    '<circle cx="75" cy="70" r="2.2" fill="var(--fig)"/>',
    '<text class="t" x="75" y="9" text-anchor="middle">A</text>',
    '<text class="t" x="14" y="74">B</text><text class="t" x="129" y="74">D</text>',
    '<text class="t" x="75" y="142" text-anchor="middle">C</text>',
    '<text class="t" x="79" y="66">O</text>',
])

# ---- 図3 長さと角 ----
gA, gB, gC, gD = (100, 16), (24.4, 124), (175.6, 124), (100, 124)
assert abs(angle_deg(gA, gB, gD) - 35) < 0.1, angle_deg(gA, gB, gD)
f2 = "".join([
    '<polygon class="l" points="100,16 24.4,124 175.6,124"/>',
    '<line class="l" x1="100" y1="16" x2="100" y2="124"/>',
    tick(gA, gB), tick(gA, gC),
    angle_arc(gA, gB, gD, 26), angle_arc(gA, gD, gC, 26),
    '<text class="t" x="84" y="48">35°</text>',
    '<text class="t" x="100" y="10" text-anchor="middle">A</text>',
    '<text class="t" x="14" y="134">B</text><text class="t" x="179" y="134">C</text>',
    '<text class="t" x="100" y="138" text-anchor="middle">D</text>',
    '<text class="t" x="100" y="148" text-anchor="middle">BC＝12cm</text>',
])

SHEET = dict(
    title="二等分線が2つ決めること",
    ji="第3時",
    pg="学校図書『数学2』p.152／1節 三角形（全18時間）",
    goal="前の時間の合同から、角だけでなく辺と垂直も導けることを説明できる。",
    katari="前の時間、△ABD≡△ACD を示しました。そこから取り出したのは ∠B＝∠C の<b>1つだけ</b>です。"
           "合同からは、ほかにも取り出せることがあります。<b>取り残しを拾う</b>のが今日の仕事です。",
    cards_title="根拠カード — 今日の新しいカードは ⑫ の1枚",
    cards_hint="①②③と⑪は見てよい。⑫は、今日 ③(1) で取り出してから使えるようになる。",
    cards=[("①", "3組の辺がそれぞれ等しい（4章）"),
           ("②", "2組の辺とその間の角がそれぞれ等しい（4章）"),
           ("③", "1組の辺とその両端の角がそれぞれ等しい（4章）"),
           ("⑪", "二等辺三角形の2つの底角は等しい"),
           ("⑫", "<b>二等辺三角形の頂角の二等分線は、底辺を垂直に2等分する</b>（今日つくるカード）")],
    footer="中学2年 数学　5章 三角形・四角形（全18時間）　第3時 頂角の二等分線／A3横・5ブロック",
    blocks=[
# ① 前時の復習
"""    <p class="inst">前の時間の証明を思い出す。ペアで1つ説明する。</p>
    <ol>
      <li>△ABD≡△ACD を示すのに使ったカードの番号 %s</li>
      <li>そのとき等しいと言った3つは<br>AB＝%s、∠BAD＝%s、%s は共通</li>
      <li>カード⑪の中身を書く
        %s</li>
    </ol>
    <div class="spacer"></div>
    <p class="inst">今日は、この<b>同じ合同</b>をもう一度使います。</p>"""
% (z("②"), z("AC"), z("∠CAD"), z("AD"), rz(2, "二等辺三角形の2つの底角は等しい")),

# ② 今日やること
"""    <p>△ABD≡△ACD から、∠B＝∠C のほかに<b>何がわかるか</b>。</p>
    %s
    <p class="inst">合同な図形では、対応する%sと対応する%sが等しい。<br>
      前の時間は「角」だけを使った。<b>辺はまだ使っていない。</b></p>
    <div class="spacer"></div>
    <p class="inst" style="border-top:1px dotted var(--rule); padding-top:5px">
      <b>今日の問い</b>　1つの合同から、いくつのことが言えるか。</p>"""
% (fig("0 0 200 150", f1, "図1　AB＝AC、AD は ∠A の二等分線"), z("辺"), z("角")),

# ③ 練習
"""    <ol>
      <li><b>△ABD≡△ACD から言えることを、全部あげる。</b>（図1）
        %s
        <p class="inst" style="margin-top:4px">∠ADB＝∠ADC から ∠ADB の大きさが決まる理由も書く。</p>
        %s</li>
      <li>図2で BD の長さと ∠B を求める。カードの番号も書く。
        %s
        BD＝%scm　%s%s　　∠B＝%s°　%s%s</li>
    </ol>"""
% (rz(4, "① ∠B＝∠C（前の時間に使った）<br>② BD＝CD（対応する辺）<br>"
         "③ ∠ADB＝∠ADC（対応する角）"),
   rz(2, "∠ADB＋∠ADC＝180°（一直線）で、しかも ∠ADB＝∠ADC だから ∠ADB＝90°。<br>"
         "②と③を合わせると「底辺を垂直に2等分する」＝<b>カード⑫</b>。"),
   fig("0 0 210 155", f3, "図2　AB＝AC、AD は ∠A の二等分線"),
   z("6"), '<span class="cn">カード</span>', z("⑫"),
   z("55"), '<span class="cn">カード</span>', z("⑫")),

# ④ JUMP
"""    <p class="inst">1人では届きません。となりと相談してよい。<b>どこまで自分で進めたか</b>を書く。</p>
    <p>四角形 ABCD は AB＝AD、CB＝CD です（図3。印の本数に注意）。</p>
    %s
    <ol class="circ">
      <li>AC は BD を<b>垂直に2等分する</b>ことを示しなさい。
        %s</li>
      <li><b>CB＝CD という条件を外して、AB＝AD だけにします。</b>
        それでも AC は BD を垂直に2等分するといえますか。
        いえないなら、そうならない図を方眼にかきなさい。
        <div class="gridbox"><svg viewBox="0 0 230 112" role="img" aria-label="作図用の方眼">%s</svg></div>
        %s</li>
    </ol>"""
% (fig("0 0 150 150", f2, "図3　AB＝AD（1本線）、CB＝CD（2本線）"),
   rz(4, "△ABC と △ADC で、AB＝AD、CB＝CD、AC は共通。<b>カード①</b>（3組の辺）から △ABC≡△ADC。<br>"
         "よって ∠BAC＝∠DAC。<br>"
         "△ABD は AB＝AD の二等辺三角形で、AC はその頂角 ∠BAD の二等分線。<br>"
         "だから <b>カード⑫</b> より、AC は BD を垂直に2等分する。"),
   grid(230, 112, 23),
   rz(3, "<b>いえない。</b>AB＝AD でも、点 C が BD の垂直二等分線上にないと AC は ∠BAD の"
         "二等分線にならない。<br>C を左右どちらかにずらした四角形をかけば反例になる。<br>"
         "→ CB＝CD という条件が、∠BAC＝∠DAC を言うために効いていた。")),

# ⑤ ふりかえり
"""    <ol>
      <li>今日つくったカードの番号 %s<br>
        <span class="inst tonly" style="color:var(--accent)">⑫ 二等辺三角形の頂角の二等分線は、底辺を垂直に2等分する</span></li>
      <li>今日は　聞いた ／ 聞かれた ／ どちらもなかった<br>
        <span class="inst">当てはまるものに丸。名前は書かない。</span></li>
      <li><b>⑪ と ⑫ は、同じ1つの合同から出てきました。何がちがいますか。</b>
        %s</li>
    </ol>
    <div class="spacer"></div>
    <p class="inst tonly" style="border-top:1px dotted var(--rule); padding-top:5px">
      <b>削り順</b>　③(2) を宿題 → ④② を宿題。<br>死守するのは ③(1) と ④①。</p>"""
% (z("⑫", "w"),
   rz(3, "⑪は「角」についての結論、⑫は「辺（2等分）」と「角（垂直）」についての結論。<br>"
         "1つの合同から取り出せることは1つではない、と気づけていればよい。")),
])

if __name__ == "__main__":
    print(build(SHEET, sys.argv[1]), "bytes")
