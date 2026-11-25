# -*- coding: utf-8 -*-
"""宿題プリント② 2節 四角形（第7〜10時）

角と長さ → 対角線の性質の表 → 平行四辺形になるものを選ぶ → 証明2本（㉒と定義）。
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a4_sheet import (build, q, fig, memo, z, bz, NAME, pt_on, seg, poly, lab, labels, meet,
                      angle_arc, angle_label, tick, par, check_angle)

XT, YT = "<tspan font-style='italic'>x</tspan>", "<tspan font-style='italic'>y</tspan>"
X, Y = "<i>x</i>", "<i>y</i>"

def pg(angB, AB, BC, k=11.0, B=(14, 92)):
    C = (B[0] + BC*k, B[1])
    A = (B[0] + AB*k*math.cos(math.radians(angB)), B[1] - AB*k*math.sin(math.radians(angB)))
    D = (A[0] + BC*k, A[1])
    return A, B, C, D

def L(A, B, C, D):
    return labels({"A": A, "B": B, "C": C, "D": D}, "ABCD", d=9)

# (1) ∠A=115° → ∠B=65°、∠C=115°
A, B, C, D = pg(65, 6, 8); check_angle(A, B, D, 115)
f1 = (poly(A, D, C, B) + angle_arc(A, B, D, 11) + angle_label(A, B, D, "115°", 24)
      + angle_arc(B, A, C, 11) + angle_label(B, A, C, XT, 21)
      + angle_arc(C, B, D, 11) + angle_label(C, B, D, YT, 21) + L(A, B, C, D))
# (2) AC=12cm、AB=7cm → OC=6cm、CD=7cm
A, B, C, D = pg(62, 5.6, 8.4); O = pt_on(A, C, .5)
f2 = (poly(A, D, C, B) + seg(A, C) + seg(B, D) + lab(pt_on(A, B, .5), "7cm", dx=-15, cls="ts")
      + lab(pt_on(O, C, .5), XT, dx=8, dy=-1, cls="ts") + lab(pt_on(D, C, .5), YT, dx=9, cls="ts")
      + L(A, B, C, D) + lab(O, "O", dy=-6))
# (3) ∠BAC=40°、∠ACB=30° → ∠D=110°、∠CAD=30°
AB = 6.0; BC = AB * math.sin(math.radians(40)) / math.sin(math.radians(30))
A, B, C, D = pg(110, AB, BC, k=13.0, B=(40, 94))
check_angle(A, B, C, 40); check_angle(C, A, B, 30); check_angle(D, A, C, 110)
f3 = (poly(A, D, C, B) + seg(A, C) + angle_arc(A, B, C, 14) + angle_label(A, B, C, "40°", 27)
      + angle_arc(C, A, B, 16) + angle_label(C, A, B, "30°", 30)
      + angle_arc(D, A, C, 10) + angle_label(D, A, C, XT, 20)
      + angle_arc(A, C, D, 22) + angle_label(A, C, D, YT, 32) + L(A, B, C, D))

# 4(1) AB、CD の中点 E、F
A, B, C, D = pg(64, 5.6, 8.6, k=10.5, B=(12, 84)); E = pt_on(A, B, .5); F = pt_on(C, D, .5)
g1 = (poly(A, D, C, B) + seg(E, D) + seg(B, F) + tick(A, E) + tick(E, B) + tick(C, F, 2) + tick(F, D, 2)
      + L(A, B, C, D) + lab(E, "E", dx=-9, dy=2) + lab(F, "F", dx=9, dy=4))
# 4(2) ∠A、∠C の二等分線
A, B, C, D = pg(60, 5, 9, k=10.5, B=(12, 84))
E = (B[0] + 5*10.5, B[1]); F = (D[0] - 5*10.5, D[1])
check_angle(A, B, E, 60); check_angle(A, E, D, 60); check_angle(C, D, F, 60); check_angle(C, F, B, 60)
g2 = (poly(A, D, C, B) + seg(A, E) + seg(C, F)
      + angle_arc(A, B, E, 12, "a") + angle_arc(A, E, D, 15, "a")
      + angle_arc(C, D, F, 12, "a") + angle_arc(C, D, F, 15, "a") + angle_arc(C, F, B, 16, "a") + angle_arc(C, F, B, 19, "a")
      + L(A, B, C, D) + lab(E, "E", dy=14) + lab(F, "F", dy=-5))

def cell(n, f, cap, a):
    return '<div class="cell"><span class="sn">(%d)</span>%s<p>%s</p></div>' % (n, fig(f[0], f[1], cap, 48), a)

T = ('<table style="margin-top:4px"><tr><th></th><th class="c">それぞれの中点で交わる</th>'
     '<th class="c">長さが等しい</th><th class="c">垂直に交わる</th></tr>'
     + "".join('<tr><th>%s</th>%s</tr>' % (n, "".join('<td class="c">%s</td>' % z(v) for v in vs))
               for n, vs in [("平行四辺形", "○××"), ("長方形", "○○×"), ("ひし形", "○×○"), ("正方形", "○○○")])
     + '</table>')

body = "".join([
q(1, "□ABCD で、%s、%s の値を求めなさい。" % (X, Y), "",
  '<div class="row c3">%s%s%s</div>'
  % (cell(1, ("0 -6 170 118", f1), "", "%s＝%s°　%s＝%s°" % (X, z("65"), Y, z("115"))),
     cell(2, ("0 -6 170 118", f2), "O は対角線の交点。AC＝12cm", "%s＝%s cm　%s＝%s cm" % (X, z("6"), Y, z("7"))),
     cell(3, ("0 -6 170 118", f3), "∠BAC＝40°、∠ACB＝30°", "%s＝%s°　%s＝%s°" % (X, z("110"), Y, z("30"))))),

'<div class="row c2" style="align-items:start">',
q(2, "対角線の性質。いつでも成り立つものに○、そうでないものに×。", "", T),
q(3, "四角形 ABCD が<b>必ず平行四辺形になる</b>ものをすべて選びなさい。O は対角線の交点。", "",
  '<p>㋐ AB＝DC、AD＝BC<br>㋑ AB∥DC、AD＝BC<br>㋒ OA＝OC、OB＝OD<br>'
  '㋓ ∠A＝∠C、∠B＝∠D<br>㋔ AB∥DC、AB＝DC<br>㋕ AD∥BC、∠A＝∠B</p>'
  '<p>答　%s</p>' % z("㋐、㋒、㋓、㋔", "ww")),
'</div>',

q(4, "次のことを証明しなさい。根拠は、内容をことばで書いてから（根拠○）。", "",
  '<div class="row c2" style="align-items:start">'
  '<div class="cell"><p><span class="sn">(1)</span> □ABCD の辺 AB、CD の中点を E、F とする。'
  '<b>四角形 EBFD は平行四辺形</b>である。</p>%s%s</div>'
  '<div class="cell"><p><span class="sn">(2)</span> □ABCD で、∠A、∠C の二等分線が辺 BC、AD と交わる点を'
  ' E、F とする。<b>四角形 AECF は平行四辺形</b>である。</p>%s%s</div></div>'
  % (fig("0 0 176 100", g1, "", 50),
     bz(54, "平行四辺形の対辺は等しいから（根拠⑯）　AB＝CD<br>"
            "E、F は AB、CD の中点だから　EB＝(1/2)AB、DF＝(1/2)CD<br>"
            "よって　EB＝DF　……(a)<br>"
            "AB∥DC だから、その一部である　EB∥DF　……(b)<br>"
            "(a)(b)より、1組の対辺が平行でその長さが等しいから（根拠㉒）"
            "四角形 EBFD は平行四辺形　■"),
     fig("0 0 176 100", g2, "", 50),
     bz(54, "AD∥BC だから　AF∥EC　……(a)<br>"
            "平行四辺形の対角は等しいから（根拠⑰）∠A＝∠C。その半分どうしで　∠EAF＝∠FCE<br>"
            "AD∥BC で錯角は等しいから　∠AEB＝∠EAF<br>"
            "よって　∠AEB＝∠FCE。同位角が等しいから　AE∥FC　……(b)<br>"
            "(a)(b)より、2組の対辺がそれぞれ平行だから（定義）四角形 AECF は平行四辺形　■"))),

memo("<b>つまずき</b>　1(3) の ∠D は ∠B と等しい（180°−40°−30°）。<br>"
     "3 の㋑は等脚台形、㋕は ∠A＝∠B＝90° の台形が反例。<br>"
     "4(2) は「平行」を示す2本目に<b>同位角</b>を使う。∠AEB と ∠FCE が同じ向きの角になっているか図で確かめさせる。"),
])

SHEET = dict(
    kind="宿題②", title="2節 四角形",
    lead="範囲　第7〜10時　　使うカード　⑯〜㉒ と 4章の ①〜⑩・1節の ⑪〜⑮　　"
         "<b>わからないところは、次の時間に誰かに聞く。</b>",
    body=body,
    footer="中学2年 数学　5章 三角形・四角形　宿題プリント② 2節／A4",
)

if __name__ == "__main__":
    print(build(SHEET, sys.argv[1]), "bytes")
