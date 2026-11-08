# -*- coding: utf-8 -*-
"""第8時 平行四辺形の性質②③（学校図書『数学2』p.164-165）学び合い
   第7時の④で出した「対角が等しい」を⑰として確定し、対角線の性質⑱を導く。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a3_sheet import build, angle_arc, angle_deg, tick, par, z, bz, fig, memo

A, D, B, C = (50, 24), (190, 24), (20, 118), (160, 118)
O = (105, 71)
base = ('<polygon class="l" points="50,24 190,24 160,118 20,118"/>'
        + par(A, D) + par(B, C) + par(A, B, 2) + par(D, C, 2)
        + '<text class="t" x="44" y="18">A</text><text class="t" x="192" y="18">D</text>'
        + '<text class="t" x="10" y="130">B</text><text class="t" x="164" y="130">C</text>')
f1 = base + '<line class="d" x1="50" y1="24" x2="160" y2="118"/>' + \
     angle_arc(B, A, C, 16) + angle_arc(D, C, A, 16)
f2 = (base + '<line class="l" x1="50" y1="24" x2="160" y2="118"/>'
      + '<line class="l" x1="190" y1="24" x2="20" y2="118"/>'
      + '<circle cx="105" cy="71" r="2.3" fill="var(--fig)"/>'
      + '<text class="t" x="109" y="68">O</text>'
      + '<g class="ft">%s%s%s%s</g>' % (tick(A, O, 3, cls="ftline"), tick(O, C, 3, cls="ftline"),
                                        tick(B, O, 4, cls="ftline"), tick(O, D, 4, cls="ftline")))
# 角を求める（∠A＝110°）
gA, gD, gB, gC = (50, 24), (190, 24), (15.8, 118), (155.8, 118)
assert abs(angle_deg(gA, gB, gD) - 110) < 0.3
f3 = "".join([
    '<polygon class="l" points="50,24 190,24 155.8,118 15.8,118"/>',
    par(gA, gD), par(gB, gC), par(gA, gB, 2), par(gD, gC, 2),
    angle_arc(gA, gB, gD, 20),
    '<text class="t" x="44" y="18">A</text><text class="t" x="192" y="18">D</text>',
    '<text class="t" x="6" y="130">B</text><text class="t" x="160" y="130">C</text>',
    '<text class="t" x="62" y="44">110°</text>',
    '<text class="t" x="24" y="108"><tspan font-style="italic">x</tspan></text>',
    '<text class="t" x="138" y="108"><tspan font-style="italic">y</tspan></text>',
])
# JUMP: O を通る直線と AD、BC の交点 P、Q
P, Q = (140, 24), (70, 118)
f4 = (base + '<line class="d" x1="50" y1="24" x2="160" y2="118"/>'
      + '<line class="d" x1="190" y1="24" x2="20" y2="118"/>'
      + '<line class="l" x1="140" y1="24" x2="70" y2="118"/>'
      + '<circle cx="105" cy="71" r="2.3" fill="var(--fig)"/>'
      + '<text class="t" x="109" y="68">O</text>'
      + '<text class="t" x="138" y="18">P</text><text class="t" x="62" y="130">Q</text>'
      + '<g class="ft">%s%s</g>' % (tick(P, O, 2, cls="ftline"), tick(O, Q, 2, cls="ftline")))

SHEET = dict(
    title="1本の対角線で何が見えるか",
    ji="第8時",
    pg="学校図書『数学2』p.164-165／2節 四角形（全17時間・学び合い）",
    goal="平行四辺形の対角と対角線の性質を導き、3枚を選んで使える。",
    katari="前の時間の最後に、<b>向かい合う角も等しい</b>ことを示した人がいました。"
           "今日はそれをカードにします。さらに、<b>対角線を2本ひく</b>と何が見えるかを調べます。",
    cards_title="今日手に入れるカードは ⑰ と ⑱ の2枚（別紙のカードを用意）",
    cards_hint="①②③と⑪〜⑯は使ってよい。⑰⑱は、③(1)(2) で導いてから使う。",
    footer="中学2年 数学　5章 三角形・四角形（全17時間）　第8時 平行四辺形の性質②③／A3横",
    blocks=[
"""    <p class="inst">前の時間に手に入れたカード⑯を、隣の人に言う。</p>
    <ol>
      <li>⑯の中身 %s</li>
      <li>⑯を導くときに、四角形に何をひきましたか %s</li>
    </ol>
    <div class="spacer"></div>
    <p class="inst">今日も<b>対角線</b>が主役。1本ひくか、2本ひくかで見えるものが変わる。</p>"""
% (bz(16, "平行四辺形の2組の対辺はそれぞれ等しい"), z("対角線", "w")),

"""    <p>定義で決めたのは<b>平行なことだけ</b>。前の時間に、そこから<b>辺の長さ</b>が決まった。</p>
    <p class="inst">では、角はどうか。対角線の交わり方はどうか。</p>
    %s
    <div class="spacer"></div>
    <p class="inst" style="border-top:1px dotted var(--rule); padding-top:5px">
      <b>今日の問い</b>　定義からあと何が決まるのか。<b>どこまで決まってしまうのか。</b></p>"""
% fig("0 0 215 140", f2, "図1　対角線2本の交点を O とする"),

"""    <ol>
      <li><b>∠ABC＝∠CDA を証明する。</b>（対角線 AC をひく）
        %s
        %s</li>
      <li><b>AO＝CO、BO＝DO を証明する。</b>（図1。対角線2本）
        <span class="inst">ヒント: 対角線が交わってできる、向かい合った2つの三角形を見る。</span>
        %s</li>
      <li>⑯⑰を使って ∠<i>x</i>、∠<i>y</i> を求める。
        %s
        ∠<i>x</i>＝%s°　∠<i>y</i>＝%s°</li>
    </ol>"""
% (fig("0 0 215 140", f1, "図2　対角線 AC をひいた", "128px"),
   bz(36, "△ABC と △CDA において<br>"
          "⑯より　AB＝CD、BC＝DA　……(a)(b)<br>"
          "AC は共通　……(c)<br>"
          "(a)(b)(c)より、3組の辺がそれぞれ等しいから（<b>根拠①</b>）　△ABC≡△CDA<br>"
          "対応する角は等しいから　∠ABC＝∠CDA　■　→ これが<b>根拠⑰</b>"),
   bz(40, "△AOD と △COB において<br>"
          "⑯より　AD＝CB　……(a)<br>"
          "AD∥BC で錯角は等しいから　∠OAD＝∠OCB　……(b)、∠ODA＝∠OBC　……(c)<br>"
          "(a)(b)(c)より、1組の辺とその両端の角がそれぞれ等しいから（<b>根拠③</b>）　△AOD≡△COB<br>"
          "対応する辺は等しいから　AO＝CO、DO＝BO　■　→ これが<b>根拠⑱</b>"),
   fig("0 0 215 142", f3, "図3", "128px"),
   z("70"), z("110")),

"""    <p>平行四辺形 ABCD の対角線の交点 O を通る直線をひき、
      辺 AD、BC との交点をそれぞれ P、Q とする。</p>
    <p><b>PO＝QO</b> を証明しなさい。（教科書 p.165 問6）</p>
    %s
    <p class="inst">※ 直線のひき方を変えても成り立つか、最後に確かめる。</p>
    %s
    %s"""
% (fig("0 0 215 140", f4, "図4　O を通る直線と AD、BC の交点が P、Q"),
   bz(46, "△AOP と △COQ において<br>"
          "⑱より　AO＝CO　……(a)<br>"
          "対頂角は等しいから　∠AOP＝∠COQ　……(b)<br>"
          "AD∥BC で錯角は等しいから　∠OAP＝∠OCQ　……(c)<br>"
          "(a)(b)(c)より、1組の辺とその両端の角がそれぞれ等しいから（<b>根拠③</b>）　△AOP≡△COQ<br>"
          "対応する辺は等しいから　PO＝QO　■<br>"
          "※ 直線をどうひいても、同じ証明が通る。O が<b>対称の中心</b>になっている。"),
   memo("<b>型</b>　なぜ使えるか（③(1)(2)）→ 使う（③(3)）→ 応用（④）。<br>"
        "③(1) は第7時の④の回収。できていた生徒の証明をそのまま使ってよい。<br>"
        "③(2) は「向かい合った2つの三角形」に気づけるかが山。"
        "△AOD と △COB、または △AOB と △COD のどちらでもよい。<br>"
        "④は「直線をどうひいても成り立つ」＝O が対称の中心、まで言えると第13時が楽になる。<br>"
        "<b>削り順</b>　③(3) を宿題 → ④を宿題。死守するのは ③(1)(2)。")),
])

if __name__ == "__main__":
    print(build(SHEET, sys.argv[1]), "bytes")
