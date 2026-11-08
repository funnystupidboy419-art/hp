# -*- coding: utf-8 -*-
"""第4時 証明を読む（学校図書『数学2』p.154-157）学び合い
   JUMP は練習プリント「図形の性質と証明①」の5 から。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a3_sheet import build, angle_arc, tick, z, rz, bz, fig, memo

A, B, C = (100, 16), (35, 126), (165, 126)
D, E = (57.8, 87.5), (142.2, 87.5)
f1 = "".join([
    '<polygon class="l" points="100,16 35,126 165,126"/>',
    '<line class="l" x1="35" y1="126" x2="142.2" y2="87.5"/>',
    '<line class="l" x1="165" y1="126" x2="57.8" y2="87.5"/>',
    tick(A, B), tick(A, C), tick(B, D, 2), tick(C, E, 2),
    '<text class="t" x="100" y="10" text-anchor="middle">A</text>',
    '<text class="t" x="25" y="136">B</text><text class="t" x="169" y="136">C</text>',
    '<text class="t" x="46" y="84">D</text><text class="t" x="146" y="84">E</text>',
])
t1, t2, t3 = (70, 16), (20, 104), (120, 104)
f2 = "".join([
    '<polygon class="l" points="70,16 20,104 120,104"/>',
    tick(t1, t2), tick(t1, t3), tick(t2, t3),
    '<text class="t" x="70" y="10" text-anchor="middle">A</text>',
    '<text class="t" x="10" y="114">B</text><text class="t" x="124" y="114">C</text>',
])
# JUMP: 辺AB, AC の中点 M, N。CM と BN の交点を D とする。
jA, jB, jC = (100, 16), (35, 126), (165, 126)
jM, jN, jD = (67.5, 71), (132.5, 71), (100, 89.3)
f3 = "".join([
    '<polygon class="l" points="100,16 35,126 165,126"/>',
    '<line class="l" x1="165" y1="126" x2="67.5" y2="71"/>',
    '<line class="l" x1="35" y1="126" x2="132.5" y2="71"/>',
    tick(jA, jB), tick(jA, jC),
    tick(jA, jM, 2), tick(jM, jB, 2), tick(jA, jN, 2), tick(jN, jC, 2),
    '<circle cx="100" cy="89.3" r="2.2" fill="var(--fig)"/>',
    '<g class="ft">%s%s</g>' % (tick(jD, jB, 3, cls="ftline"), tick(jD, jC, 3, cls="ftline")),
    '<text class="t" x="100" y="10" text-anchor="middle">A</text>',
    '<text class="t" x="25" y="136">B</text><text class="t" x="169" y="136">C</text>',
    '<text class="t" x="55" y="68">M</text><text class="t" x="137" y="68">N</text>',
    '<text class="t" x="104" y="86">D</text>',
])

SHEET = dict(
    title="証明は人に読まれる",
    ji="第4時",
    pg="学校図書『数学2』p.154-157／1節 三角形（全17時間・学び合い）",
    goal="自分の書いた証明が、ほかの人に読んでわかるものになっているか判断できる。",
    katari="今日から先生は教えません。わからなければ聞きに行き、聞かれたら答えてください。<br>"
           "今日の中心は<b>人の証明を読むこと</b>です。合っているかだけでなく、"
           "<b>読んでわかるか</b>を見ます。",
    cards_title="今日は新しいカードはない。持っているカードで進む",
    cards_hint="新しいカードが増えない回は、<b>持っているカードを選ぶ力</b>をつける回。",
    cards=[("①②③", "三角形の合同条件（4章）"),
           ("⑪", "二等辺三角形の2つの底角は等しい"),
           ("⑫", "二等辺三角形の頂角の二等分線は、底辺を垂直に2等分する"),
           ("⑬", "2つの角が等しい三角形は、二等辺三角形である")],
    footer="中学2年 数学　5章 三角形・四角形（全17時間）　第4時 証明を読む／A3横",
    blocks=[
"""    <p class="inst">カード⑪⑫⑬を隣の人に1つずつ言う。言えなかった番号を書く。</p>
    <ol>
      <li>言えなかった番号 %s</li>
      <li>⑬は、どのカードの「逆」でしたか %s</li>
    </ol>
    <div class="spacer"></div>
    <p class="inst">わからないことは<b>先生ではなく友だちに</b>聞く。</p>"""
% (z("", "w"), z("⑪")),

"""    <p>二等辺三角形 ABC の等しい辺 AB、AC 上に <b>BD＝CE</b> となる点 D、E をとり、
      B と E、C と D を結ぶ。</p>
    %s
    <p class="inst">このとき <b>BE＝CD</b> になりそうだ。これを証明する。</p>
    <div class="spacer"></div>
    <p class="inst" style="border-top:1px dotted var(--rule); padding-top:5px">
      <b>今日の問い</b>　書けた証明は、<b>ほかの人が読んでわかる</b>ものになっているか。</p>"""
% fig("0 0 200 146", f1, "図1　AB＝AC（1本線）、BD＝CE（2本線）"),

"""    <ol>
      <li><b>BE＝CD を証明する。</b>（図1）
        <span class="inst">使う合同条件</span>%s
        %s</li>
      <li><b>次は、ある人が書いた証明です。合ってはいますが、2か所足りません。</b>
        <div class="badproof">
          <p style="margin:0">△ABE と △ACD において</p>
          <p class="ind" style="margin:2px 0 0">仮定から　AB＝AC　……(a)</p>
          <p class="ind" style="margin:2px 0 0">仮定から　BD＝CE　……(b)</p>
          <p class="ind" style="margin:2px 0 0">(a)(b)から　AB−BD＝AC−CE</p>
          <p class="ind" style="margin:2px 0 0">AD＝AB−BD、AE＝AC−CE だから　AD＝AE　……(c)</p>
          <p class="ind" style="margin:2px 0 0">また　∠A は共通　……(d)</p>
          <p class="ind" style="margin:2px 0 0">よって (a)(c)(d) より　△ABE≡△ACD</p>
        </div>
        足りない2か所を書く。
        %s</li>
      <li>図2の正三角形で、∠A＝∠B＝∠C を証明する。
        <span class="inst">ヒント: 正三角形を「二等辺三角形」として<b>2通りに</b>見る。</span>
        %s
        %s</li>
    </ol>"""
% (z("②"),
   bz(36, "△ABE と △ACD において<br>"
          "仮定より　AB＝AC　……(a)<br>"
          "仮定より　BD＝CE。AD＝AB−BD、AE＝AC−CE だから　AD＝AE　……(b)<br>"
          "∠A は共通　……(c)<br>"
          "(a)(b)(c)より、<b>カード②</b>から　△ABE≡△ACD<br>"
          "対応する辺は等しいから　BE＝CD　■"),
   bz(22, "1つめ: <b>使った合同条件の名前（カード②）が書いていない。</b><br>"
          "2つめ: <b>最後の結論 BE＝CD が書いていない。</b>合同を示しただけで止まっている。"),
   fig("0 0 140 120", f2, "図2　AB＝BC＝CA", "105px"),
   bz(24, "AB＝AC の二等辺三角形とみると、カード⑪より　∠B＝∠C　……(a)<br>"
          "BA＝BC の二等辺三角形とみると、カード⑪より　∠A＝∠C　……(b)<br>"
          "(a)(b)より　∠A＝∠B＝∠C　■")),

"""    <p class="inst">練習プリント「図形の性質と証明①」の5 と同じ問題。</p>
    <p>AB＝AC の二等辺三角形 ABC で、辺 AB、AC の中点をそれぞれ M、N とし、
      CM と BN の交点を D とする。</p>
    %s
    <ol class="circ">
      <li>△MBC≡△NCB を証明しなさい。%s</li>
      <li><b>△DBC は二等辺三角形である。</b>そのことを説明しなさい。%s</li>
    </ol>
    %s"""
% (fig("0 0 200 146", f3, "図3　AM＝MB、AN＝NC（2本線）"),
   bz(34, "△MBC と △NCB において<br>"
          "AB＝AC で M、N はその中点だから　MB＝NC　……(a)<br>"
          "カード⑪より　∠MBC＝∠NCB　……(b)<br>"
          "BC は共通　……(c)<br>"
          "(a)(b)(c)より、<b>カード②</b>から　△MBC≡△NCB　■"),
   bz(30, "(1) の合同から、対応する角は等しいので　∠DCB＝∠DBC。<br>"
          "2つの角が等しいから、<b>カード⑬</b>より △DBC は二等辺三角形（DB＝DC）　■<br>"
          "※ ⑪で角を出し、⑬で三角形の形を決める。2枚を続けて使うのがこの問題。"),
   memo("<b>削り順</b>　③(3) を宿題 → ④② を宿題。死守するのは ③(1)(2)。<br>"
        "③(2) が今日の中心。全員が「読む人のために書く」に触れてから終わる。<br>"
        "足りない2つ＝使った合同条件の名前と、最後の結論 BE＝CD。計算そのものは正しい。<br>"
        "「正しいが、読めない」証明だと伝える。<br>"
        "④は⑪→⑬と2枚続けて使う。ここまで届いた生徒がいたら全体に紹介する。")),
])

if __name__ == "__main__":
    print(build(SHEET, sys.argv[1]), "bytes")
