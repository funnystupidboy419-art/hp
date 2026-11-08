# -*- coding: utf-8 -*-
"""第5時 直角三角形の合同条件（学校図書『数学2』p.158-160）学び合い
   第2時 ④②「垂線では、その角が2辺の間にないから合同と言えない」の回収。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a3_sheet import build, angle_arc, angle_deg, tick, right_angle, z, rz, bz, fig, memo

A, B, C, H = (100, 18), (45, 124), (155, 124), (100, 124)
f1 = "".join([
    '<polygon class="l" points="100,18 45,124 155,124"/>',
    '<line class="l" x1="100" y1="18" x2="100" y2="124"/>',
    tick(A, B), tick(A, C), right_angle(H, C, A, 8),
    '<text class="t" x="100" y="12" text-anchor="middle">A</text>',
    '<text class="t" x="35" y="134">B</text><text class="t" x="159" y="134">C</text>',
    '<text class="t" x="100" y="138" text-anchor="middle">H</text>',
])

# 図2 なぜ⑭が使えるのか。合同な2つの直角三角形（∠C＝∠F＝90°、斜辺 AB＝DE、∠B＝∠E）
pB, pC, pA = (15, 100), (95, 100), (95, 35)
qE, qF, qD = (135, 100), (215, 100), (215, 35)
assert abs(angle_deg(pC, pB, pA) - 90) < .1 and abs(angle_deg(qF, qE, qD) - 90) < .1
assert abs(angle_deg(pB, pA, pC) - angle_deg(qE, qD, qF)) < .1
f2 = "".join([
    '<polygon class="l" points="15,100 95,100 95,35"/>',
    '<polygon class="l" points="135,100 215,100 215,35"/>',
    right_angle(pC, pB, pA, 7), right_angle(qF, qE, qD, 7),
    tick(pA, pB), tick(qD, qE),
    angle_arc(pB, pC, pA, 15), angle_arc(qE, qF, qD, 15),
    '<text class="t" x="93" y="31">A</text><text class="t" x="6" y="110">B</text>',
    '<text class="t" x="97" y="110">C</text>',
    '<text class="t" x="213" y="31">D</text><text class="t" x="126" y="110">E</text>',
    '<text class="t" x="217" y="110">F</text>',
])

# 図3 なぜ⑮が使えるのか。等しい辺 AC と DF を重ね、裏返して並べた図
rA, rB, rC, rE = (100, 30), (38, 120), (100, 120), (162, 120)
assert abs(angle_deg(rC, rB, rA) - 90) < .1
assert abs(((rA[0]-rB[0])**2+(rA[1]-rB[1])**2) - ((rA[0]-rE[0])**2+(rA[1]-rE[1])**2)) < 1
f3 = "".join([
    '<polygon class="l" points="100,30 38,120 162,120"/>',
    '<line class="l" x1="100" y1="30" x2="100" y2="120"/>',
    tick(rA, rB), tick(rA, rE),
    right_angle(rC, rE, rA, 8),
    '<text class="t" x="100" y="24" text-anchor="middle">A（＝D）</text>',
    '<text class="t" x="28" y="130">B</text><text class="t" x="166" y="130">E</text>',
    '<text class="t" x="100" y="134" text-anchor="middle">C（＝F）</text>',
])

jA, jB, jC, jD, jE = (30, 30), (30, 120), (170, 120), (105.7, 78.7), (79.1, 120)
assert abs(angle_deg(jB, jA, jC) - 90) < 0.1 and abs(angle_deg(jD, jA, jE) - 90) < 0.1
assert abs(math.hypot(jA[0]-jB[0], jA[1]-jB[1]) - math.hypot(jA[0]-jD[0], jA[1]-jD[1])) < 0.2
f2 = "".join([
    '<polygon class="l" points="30,30 30,120 170,120"/>',
    '<line class="l" x1="105.7" y1="78.7" x2="79.1" y2="120"/>',
    tick(jA, jB), tick(jA, jD),
    right_angle(jB, jC, jA, 8), right_angle(jD, jA, jE, 8),
    '<g class="ft">',
    '<line class="ftline" x1="30" y1="30" x2="79.1" y2="120" stroke-dasharray="4 3"/>',
    '<line class="ftline" x1="30" y1="120" x2="105.7" y2="78.7" stroke-dasharray="4 3"/>',
    tick(jB, jE, 2, cls="ftline"), tick(jD, jE, 2, cls="ftline"), '</g>',
    '<text class="t" x="22" y="26">A</text><text class="t" x="20" y="132">B</text>',
    '<text class="t" x="174" y="132">C</text>',
    '<text class="t" x="110" y="76">D</text><text class="t" x="76" y="132">E</text>',
])

SHEET = dict(
    title="足りない道具をつくる",
    ji="第5時",
    pg="学校図書『数学2』p.158-160／1節 三角形（全17時間・学び合い）",
    goal="直角三角形の合同条件が、なぜ使ってよいのかを説明でき、それを使って証明できる。",
    katari="第2時に「辺2つと角1つでは合同といえない」と確かめました。"
           "ところが直角三角形には、<b>辺2つと角1つで合同といえる</b>条件があります。"
           "ずるいようですが、ちゃんと理由があります。<b>今日はその理由を確かめます。</b>",
    cards_title="今日手に入れるカードは ⑭ と ⑮ の2枚（別紙のカードを用意）",
    cards_hint="①②③と⑪⑫⑬は使ってよい。⑭⑮は、③(1)(2) で「なぜ使えるのか」を確かめてから使う。",
    cards=[("①②③", "三角形の合同条件（4章）"),
           ("⑪⑫⑬", "二等辺三角形について"),
           ("⑭", "直角三角形の合同条件・その1　<b>（今日 ③(1) で書く）</b>"),
           ("⑮", "直角三角形の合同条件・その2　<b>（今日 ③(1) で書く）</b>")],
    footer="中学2年 数学　5章 三角形・四角形（全17時間）　第5時 直角三角形の合同／A3横",
    blocks=[
"""    <p class="inst">第2時にできなかったことを思い出す。</p>
    %s
    <ol>
      <li>図1で言えることは3つ。AB＝AC、AH は%s、∠AHB＝∠AHC＝%s°</li>
      <li>それでも <b>△ABH≡△ACH</b> と言えなかった理由
        %s</li>
    </ol>"""
% (fig("0 0 200 148", f1, "図1　AB＝AC、AH⊥BC"), z("共通"), z("90"),
   bz(20, "辺2つと角1つだが、その角が<b>2辺の間にない</b>のでカード②が使えない。①③も足りない。")),

"""    <p class="inst">直角の向かい側の辺を %s という。</p>
    <p>直角三角形には、①②③のほかに次の2つが使える。</p>
    <p class="inst" style="margin-top:4px">
      ⑭ 斜辺と1つの%sがそれぞれ等しい<br>
      ⑮ 斜辺と他の1%sがそれぞれ等しい</p>
    <p class="inst" style="margin-top:6px">どちらも<b>辺2つ・角1つ</b>しか言っていない。
      ふつうの三角形なら、それだけでは合同といえなかった。</p>
    <div class="spacer"></div>
    <p class="inst" style="border-top:1px dotted var(--rule); padding-top:5px">
      <b>今日の問い</b>　なぜ直角三角形だけ、<b>これで合同といってよい</b>のか。</p>"""
% (z("斜辺", "w"), z("鋭角"), z("辺")),

"""    <ol>
      <li><b>⑭はなぜ使えるのか。</b><br>
        <span class="inst">∠C＝∠F＝90°、AB＝DE（斜辺）、∠B＝∠E のとき。</span>
        %s
        <div class="think">
          <p class="th">考え方</p>
          <p>・三角形の内角の和は180°。∠C＝∠F＝90° で ∠B＝∠E なら、
            残りの ∠A と ∠D は %s。</p>
          <p>・すると AB＝DE の<b>両端の角</b>がそれぞれ等しい。</p>
          <p>・だから、すでに持っているカード %s で合同といえる。</p>
        </div>
        %s</li>
      <li><b>⑮はなぜ使えるのか。</b>（図3）<br>
        <span class="inst">△ABC と △DEF で ∠C＝∠F＝90°、AB＝DE（斜辺）、AC＝DF（他の1辺）。<br>
        △DEF を裏返して、等しい辺 AC と DF を重ねると、図3 のように B、C(F)、E が一直線に並ぶ。</span>
        %s
        %s</li>
      <li><b>⑮を使って証明する。</b>図1 にもどり、<b>カード⑪を使わずに</b>
        △ABH≡△ACH を示す。
        <span class="inst">（⑪を使うと ∠B＝∠C が先に出て、第2時の宿題の答えにならない。）</span>
        %s</li>
    </ol>"""
% (fig("0 0 230 118", f2, "図2　∠C＝∠F＝90°、AB＝DE、∠B＝∠E"),
   z("等しい", "w"), z("③"),
   bz(16, "∠A＝180−90−∠B、∠D＝180−90−∠E で ∠B＝∠E だから ∠A＝∠D。<br>"
          "AB＝DE とその両端の角 ∠A＝∠D、∠B＝∠E より、<b>カード③</b>から △ABC≡△DEF。<br>"
          "→ だから「斜辺と1つの鋭角」と書いてよい＝<b>カード⑭</b>"),
   fig("0 0 200 142", f3, "図3　AC と DF を重ねて裏返した"),
   bz(26, "AB＝AE だから △ABE は二等辺三角形。<b>カード⑪</b>より ∠B＝∠E。<br>"
          "△ABC と △AEC で、AB＝AE（斜辺）、∠B＝∠E、∠ACB＝∠ACE＝90° だから、"
          "いま確かめた<b>カード⑭</b>で合同。<br>"
          "→ だから「斜辺と他の1辺」と書いてよい＝<b>カード⑮</b><br>"
          "※ ⑮は⑭から、⑭は③から出てきた。<b>新しい条件ではなく、近道</b>をつくったことになる。"),
   bz(30, "△ABH と △ACH において<br>"
          "仮定より　∠AHB＝∠AHC＝90°　……(a)<br>"
          "仮定より　AB＝AC（斜辺）　……(b)<br>"
          "AH は共通（他の1辺）　……(c)<br>"
          "(a)(b)(c)より、<b>カード⑮</b>から　△ABH≡△ACH　■")),

"""    <p>∠B＝90° の直角三角形 ABC で、斜辺 AC 上に <b>AB＝AD</b> となる点 D をとる。
      D を通る AC の垂線と辺 BC との交点を E とする。
      <span class="inst">必要な線は自分でひいてよい。</span></p>
    %s
    <ol class="circ">
      <li><b>BE＝DE</b> を証明しなさい。%s</li>
      <li>同じことを、<b>⑭⑮を使わずに</b>証明できますか。できるなら書きなさい。%s</li>
    </ol>
    %s"""
% (fig("0 0 200 145", f2, "図2　∠B＝90°、AB＝AD、DE⊥AC"),
   bz(32, "A と E を結ぶ。<br>"
          "△ABE と △ADE において　∠ABE＝∠ADE＝90°　……(a)／"
          "仮定より AB＝AD（他の1辺）　……(b)／AE は共通（斜辺）　……(c)<br>"
          "(a)(b)(c)より、<b>カード⑮</b>から　△ABE≡△ADE<br>"
          "対応する辺は等しいから　BE＝DE　■"),
   bz(30, "<b>できる。</b>B と D を結ぶ。<br>"
          "AB＝AD だから △ABD は二等辺三角形で、<b>カード⑪</b>より ∠ABD＝∠ADB。<br>"
          "∠ABE＝∠ADE＝90° だから、そこから等しい角をひいて　∠EBD＝∠EDB。<br>"
          "2つの角が等しいから、<b>カード⑬</b>より △EBD は二等辺三角形。よって BE＝DE　■"),
   memo("<b>介入点（5分）</b>　③(1) が終わったところで全体を止め、"
        "「⑮は⑭から、⑭は③から出てきた。新しい条件ではなく<b>近道</b>だ」を全員で確認する。<br>"
        "そのあと ③(3) で、第2時にできなかったことができるのを確かめる。<br>"
        "ここを通さないと、カードが増える意味が伝わらない。<br>"
        "④② が出たら「⑭⑮は便利だが必須ではない。同じ結論に2通りの道がある」とまとめる。<br>"
        "<b>削り順</b>　④② を宿題 → ③(3) を宿題。死守するのは ③(1)(2) と ④①。<br>"
        "識別の練習（合同な直角三角形を選ぶ）は練習プリント③の1 を使う。")),
])

if __name__ == "__main__":
    print(build(SHEET, sys.argv[1]), "bytes")
