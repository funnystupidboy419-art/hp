# -*- coding: utf-8 -*-
"""第6時 1節の確かめよう（学校図書『数学2』p.161）学び合い
   ステップ式にしない。練習問題を多く並べ、余白は書ける分だけ取る。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a3_sheet import build_practice, angle_arc, angle_deg, tick, right_angle, z, bz, fig, memo

def iso(A, B, C, lab, extra=""):
    return "".join(['<polygon class="l" points="%g,%g %g,%g %g,%g"/>' % (A+B+C),
                    tick(A, B), tick(A, C), extra] + lab)

# 角を求める 4問
a1 = iso((100,20),(50.6,126),(149.4,126),
    [angle_arc((100,20),(50.6,126),(149.4,126),24),
     '<text class="t" x="100" y="54" text-anchor="middle">50°</text>',
     angle_arc((50.6,126),(149.4,126),(100,20),17),
     '<text class="t" x="63" y="117"><tspan font-style="italic">x</tspan></text>',
     '<text class="t" x="100" y="14" text-anchor="middle">A</text>',
     '<text class="t" x="40" y="136">B</text><text class="t" x="153" y="136">C</text>'])
a2 = iso((100,20),(65.6,126),(134.4,126),
    [angle_arc((65.6,126),(134.4,126),(100,20),17),
     '<text class="t" x="78" y="117">72°</text>',
     angle_arc((100,20),(65.6,126),(134.4,126),22),
     '<text class="t" x="100" y="50" text-anchor="middle"><tspan font-style="italic">x</tspan></text>',
     '<text class="t" x="100" y="14" text-anchor="middle">A</text>',
     '<text class="t" x="55" y="136">B</text><text class="t" x="138" y="136">C</text>'])
a3 = iso((100,22),(46.8,122),(153.2,122),
    [angle_arc((153.2,122),(100,22),(195,122),12),
     '<text class="t" x="154" y="108">118°</text>',
     angle_arc((100,22),(46.8,122),(153.2,122),22),
     '<text class="t" x="100" y="52" text-anchor="middle"><tspan font-style="italic">x</tspan></text>',
     '<text class="t" x="100" y="16" text-anchor="middle">A</text>',
     '<text class="t" x="37" y="132">B</text><text class="t" x="150" y="134">C</text>'],
    '<line class="l" x1="153.2" y1="122" x2="195" y2="122"/>')
a4 = iso((100,16),(65.6,122),(134.4,122),
    [angle_arc((100,16),(65.6,122),(134.4,122),22),
     '<text class="t" x="100" y="46" text-anchor="middle">36°</text>',
     angle_arc((121.3,81.5),(65.6,122),(134.4,122),15),
     '<text class="t" x="108" y="92"><tspan font-style="italic">x</tspan></text>',
     '<text class="t" x="100" y="10" text-anchor="middle">A</text>',
     '<text class="t" x="55" y="132">B</text><text class="t" x="138" y="132">C</text>',
     '<text class="t" x="124" y="78">D</text>'],
    '<line class="l" x1="65.6" y1="122" x2="121.3" y2="81.5"/>')

# 証明1: AD＝AE、BE と CD の交点 P
pA, pB, pC = (100,16), (35,126), (165,126)
pD, pE, pP = (70.75,65.5), (129.25,65.5), (100,84.3)
f_p = "".join([
    '<polygon class="l" points="100,16 35,126 165,126"/>',
    '<line class="l" x1="35" y1="126" x2="129.25" y2="65.5"/>',
    '<line class="l" x1="165" y1="126" x2="70.75" y2="65.5"/>',
    tick(pA,pB), tick(pA,pC), tick(pA,pD,2), tick(pA,pE,2),
    '<circle cx="100" cy="84.3" r="2.2" fill="var(--fig)"/>',
    '<text class="t" x="100" y="10" text-anchor="middle">A</text>',
    '<text class="t" x="25" y="136">B</text><text class="t" x="169" y="136">C</text>',
    '<text class="t" x="59" y="62">D</text><text class="t" x="133" y="62">E</text>',
    '<text class="t" x="104" y="81">P</text>'])

# 証明2: 四角形ABCD、AB＝AD、∠B＝∠D＝90°
qA, qB, qC, qD = (100,20), (48.3,56.2), (100,130), (151.7,56.2)
assert abs(angle_deg(qB,qA,qC)-90) < .2 and abs(angle_deg(qD,qA,qC)-90) < .2
f_q = "".join([
    '<polygon class="l" points="100,20 48.3,56.2 100,130 151.7,56.2"/>',
    '<line class="d" x1="100" y1="20" x2="100" y2="130"/>',
    tick(qA,qB), tick(qA,qD),
    right_angle(qB,qA,qC,7), right_angle(qD,qC,qA,7),
    '<text class="t" x="100" y="14" text-anchor="middle">A</text>',
    '<text class="t" x="38" y="54">B</text><text class="t" x="156" y="54">D</text>',
    '<text class="t" x="100" y="142" text-anchor="middle">C</text>'])

# 証明3: AB＝DC、∠BAC＝∠CDB＝90°
rB, rC, rA, rD = (30,120), (190,120), (44.5,74.1), (175.5,74.1)
assert abs(angle_deg(rA,rB,rC)-90) < .2 and abs(angle_deg(rD,rC,rB)-90) < .2
f_r = "".join([
    '<line class="l" x1="30" y1="120" x2="190" y2="120"/>',
    '<line class="l" x1="30" y1="120" x2="44.5" y2="74.1"/>',
    '<line class="l" x1="44.5" y1="74.1" x2="190" y2="120"/>',
    '<line class="l" x1="190" y1="120" x2="175.5" y2="74.1"/>',
    '<line class="l" x1="175.5" y1="74.1" x2="30" y2="120"/>',
    tick(rA,rB), tick(rD,rC),
    right_angle(rA,rB,rC,7), right_angle(rD,rC,rB,7),
    '<text class="t" x="38" y="70">A</text><text class="t" x="178" y="70">D</text>',
    '<text class="t" x="20" y="130">B</text><text class="t" x="194" y="130">C</text>'])

SHEET = dict(
    title="1節の確かめよう",
    ji="第6時",
    pg="学校図書『数学2』p.161／1節 三角形 確かめよう（全17時間・学び合い）",
    goal="1節で手に入れた5枚のカード（⑪〜⑮）を、自分で選んで使える。",
    katari="今日は新しいことをしません。<b>手に入れた5枚を、自分で選んで使う</b>日です。"
           "全部できた人は、まだの人のところへ行ってください。<b>全員が終わるのがゴール</b>です。",
    cards_title="使えるカード　①②③（4章）と ⑪⑫⑬⑭⑮（1節）",
    cards_hint="別紙のカードを机に並べて解く。根拠は<b>内容をことばで書いてから（根拠○）</b>。",
    footer="中学2年 数学　5章 三角形・四角形（全17時間）　第6時 1節の確かめよう／A3横",
    cols=[
("ことばの確認",
 """    <ol>
      <li>二等辺三角形の<b>定義</b>を書きなさい。%s</li>
      <li>正三角形の<b>定義</b>を書きなさい。%s</li>
      <li>直角三角形の合同条件を2つ書きなさい。
        %s</li>
      <li>「二等辺三角形ならば、2つの底角は等しい」の<b>逆</b>を書きなさい。
        また、その逆は正しいですか。
        %s</li>
      <li>「仮定」と「結論」のちがいを、自分のことばで書きなさい。%s</li>
      <li>正三角形の3つの角が等しいのはなぜですか。%s</li>
    </ol>"""
 % (bz(16, "2つの辺が等しい三角形"),
    bz(16, "3つの辺が等しい三角形"),
    bz(24, "① 斜辺と1つの鋭角がそれぞれ等しい<br>② 斜辺と他の1辺がそれぞれ等しい"),
    bz(32, "逆:「2つの角が等しい三角形ならば、二等辺三角形である」<br>"
           "<b>正しい</b>（根拠⑬）。第3時に証明した。<br>"
           "※ 逆がいつでも正しいわけではない、も言えていれば◎"),
    bz(26, "すでに分かっていることが<b>仮定</b>、これから示すことが<b>結論</b>。<br>"
           "語順や言い方ではなく、証明のどちら側に置かれるかで決まる。"),
    bz(30, "正三角形を「AB＝AC の二等辺三角形」とみると、二等辺三角形の底角は"
           "等しいから（根拠⑪）∠B＝∠C。<br>"
           "「BA＝BC の二等辺三角形」とみると、同じく ∠A＝∠C。<br>"
           "よって ∠A＝∠B＝∠C。<b>同じ図を2通りに見る</b>のがこつ。"))),

("角を求める",
 """    <ol>
      <li>%s∠<i>x</i>＝%s°</li>
      <li>%s∠<i>x</i>＝%s°</li>
      <li>%s∠<i>x</i>＝%s°</li>
      <li>BD は ∠B の二等分線。%s∠<i>x</i>＝%s°</li>
    </ol>
    <p class="inst">使った根拠を、番号だけでなく<b>ことば</b>でも言えるようにする。</p>"""
 % (fig("0 0 200 145", a1, "AB＝AC"), z("65"),
    fig("0 0 200 145", a2, "AB＝AC"), z("36"),
    fig("0 0 205 142", a3, "AB＝AC"), z("56"),
    fig("0 0 200 142", a4, "AB＝AC", "120px"), z("72"))),

("証明（二等辺三角形）",
 """    <p class="inst">AB＝AC の二等辺三角形 ABC の辺 AB、AC 上に AD＝AE となる点 D、E をとり、
      B と E、C と D を結ぶ。BE と CD の交点を P とする。</p>
    %s
    <ol>
      <li><b>BE＝CD</b> を証明しなさい。%s</li>
      <li>△PBC はどんな三角形ですか。<b>理由も書きなさい。</b>%s</li>
    </ol>"""
 % (fig("0 0 200 146", f_p, "AB＝AC（1本線）、AD＝AE（2本線）"),
    bz(48, "△ABE と △ACD において<br>"
           "仮定より　AB＝AC　……(a)<br>"
           "仮定より　AE＝AD　……(b)<br>"
           "∠A は共通　……(c)<br>"
           "(a)(b)(c)より、2組の辺とその間の角がそれぞれ等しいから（<b>根拠②</b>）　△ABE≡△ACD<br>"
           "対応する辺は等しいから　BE＝CD　■"),
    bz(44, "<b>PB＝PC の二等辺三角形。</b><br>"
           "(1) の合同から ∠ABE＝∠ACD。二等辺三角形の底角は等しいから（根拠⑪）∠ABC＝∠ACB。<br>"
           "差をとって ∠PBC＝∠PCB。<br>"
           "2つの角が等しい三角形は二等辺三角形だから（<b>根拠⑬</b>）、△PBC は二等辺三角形　■"))),

("証明（直角三角形）",
 """    <ol>
      <li>四角形 ABCD で <b>AB＝AD、∠B＝∠D＝90°</b> のとき、<b>BC＝DC</b> を証明しなさい。
        %s%s</li>
      <li><b>AB＝DC、∠BAC＝∠CDB＝90°</b> のとき、<b>AC＝DB</b> を証明しなさい。
        %s%s</li>
    </ol>
    %s"""
 % (fig("0 0 200 150", f_q, "AB＝AD、∠B＝∠D＝90°", "130px"),
    bz(44, "A と C を結ぶ。<br>"
           "△ABC と △ADC において　∠ABC＝∠ADC＝90°　……(a)<br>"
           "仮定より　AB＝AD（他の1辺）　……(b)／AC は共通（斜辺）　……(c)<br>"
           "(a)(b)(c)より、斜辺と他の1辺がそれぞれ等しいから（<b>根拠⑮</b>）　△ABC≡△ADC<br>"
           "対応する辺は等しいから　BC＝DC　■"),
    fig("0 0 215 140", f_r, "AB＝DC、∠BAC＝∠CDB＝90°", "130px"),
    bz(44, "△ABC と △DCB において　∠BAC＝∠CDB＝90°　……(a)<br>"
           "仮定より　AB＝DC（他の1辺）　……(b)／BC は共通（斜辺）　……(c)<br>"
           "(a)(b)(c)より、斜辺と他の1辺がそれぞれ等しいから（<b>根拠⑮</b>）　△ABC≡△DCB<br>"
           "対応する辺は等しいから　AC＝DB　■"),
    memo("<b>この時間はステップを踏ませない。</b>できるところから手をつけてよい。<br>"
         "終わった生徒を、まだの生徒のところへ動かす。<b>全員が終わるのがゴール。</b><br>"
         "つまずきの見取り: 「角を求める」で止まる＝⑪が入っていない。"
         "「証明（二等辺三角形）(2)」で止まる＝⑪→⑬の2枚続けが弱い。"
         "「証明（直角三角形）」で止まる＝補助線（AC を結ぶ）が出ていない。<br>"
         "<b>削り順</b>　証明（直角三角形）の2 → 角を求めるの4。死守するのは「ことばの確認」と各証明の1問目。"))),
])

if __name__ == "__main__":
    print(build_practice(SHEET, sys.argv[1]), "bytes")
