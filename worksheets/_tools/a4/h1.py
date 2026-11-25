# -*- coding: utf-8 -*-
"""宿題プリント① 1節 三角形（第2〜6時）

授業の練習の続き。角度 → ことば → 逆と反例 → 証明 の順。
証明は⑪⑬（二等辺三角形）と⑮⑬（直角三角形）を1本ずつ。
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a4_sheet import (build, q, fig, memo, z, bz, NAME, iso, foot, pt_on, seg, poly, lab, labels,
                      meet, angle_arc, angle_label, tick, right_angle, check_angle)

X = "<i>x</i>"
XT = "<tspan font-style='italic'>x</tspan>"

def base(apex, leg=92, ax=58):
    A = (ax, 13); B, C = iso(A, apex, leg)
    return A, B, C, ((A[0]+B[0]+C[0])/3, (A[1]+B[1]+C[1])/3)

# (1) ∠A=52° → ∠B=64°
A, B, C, cen = base(52); check_angle(A, B, C, 52); check_angle(B, A, C, 64)
f1 = (poly(A, B, C) + tick(A, B) + tick(A, C) + angle_arc(A, B, C, 12) + angle_label(A, B, C, "52°", 25)
      + angle_arc(B, A, C, 11) + angle_label(B, A, C, XT, 21) + labels({"A": A, "B": B, "C": C}, "ABC", cen, 9))
# (2) ∠C=72° → ∠A=36°
A, B, C, cen = base(36); check_angle(C, A, B, 72)
f2 = (poly(A, B, C) + tick(A, B) + tick(A, C) + angle_arc(C, A, B, 11) + angle_label(C, A, B, "72°", 23)
      + angle_arc(A, B, C, 14) + angle_label(A, B, C, XT, 27) + labels({"A": A, "B": B, "C": C}, "ABC", cen, 9))
# (3) ∠A=40°、BD は ∠B の二等分線 → ∠BDC=75°
A, B, C, cen = base(40)
D = meet(B, (B[0] + math.cos(math.radians(35)), B[1] - math.sin(math.radians(35))), A, C)
check_angle(B, A, D, 35); check_angle(B, D, C, 35); check_angle(D, B, C, 75)
f3 = (poly(A, B, C) + seg(B, D) + tick(A, B) + tick(A, C) + angle_arc(A, B, C, 12) + angle_label(A, B, C, "40°", 25)
      + angle_arc(B, A, D, 16, "a") + angle_arc(B, D, C, 19, "a")
      + angle_arc(D, B, C, 10) + angle_label(D, B, C, XT, 20)
      + labels({"A": A, "B": B, "C": C}, "ABC", cen, 9) + lab(D, "D", dx=8, dy=2))
# (4) ∠A=40°、AC 上の D で BD=BC → ∠ABD=30°
A, B, C, cen = base(40)
D = meet(B, (B[0] + math.cos(math.radians(40)), B[1] - math.sin(math.radians(40))), A, C)
assert abs(math.dist(B, D) - math.dist(B, C)) < 1e-6
check_angle(B, A, D, 30)
f4 = (poly(A, B, C) + seg(B, D) + tick(A, B) + tick(A, C) + tick(B, D, 2) + tick(B, C, 2)
      + angle_arc(A, B, C, 12) + angle_label(A, B, C, "40°", 25)
      + angle_arc(B, A, D, 16) + angle_label(B, A, D, XT, 27)
      + labels({"A": A, "B": B, "C": C}, "ABC", cen, 9) + lab(D, "D", dx=8, dy=2))

# 4(1) ∠B、∠C の二等分線の交点 P
A, B, C, cen = base(50, 110, 72)
P = meet(B, (B[0] + math.cos(math.radians(32.5)), B[1] - math.sin(math.radians(32.5))),
         C, (C[0] - math.cos(math.radians(32.5)), C[1] - math.sin(math.radians(32.5))))
check_angle(B, A, P, 32.5); check_angle(C, A, P, 32.5)
g1 = (poly(A, B, C) + seg(B, P) + seg(P, C) + tick(A, B) + tick(A, C)
      + angle_arc(B, A, P, 17, "a") + angle_arc(B, P, C, 21, "a")
      + angle_arc(C, A, P, 17, "a") + angle_arc(C, P, B, 21, "a")
      + labels({"A": A, "B": B, "C": C}, "ABC", cen, 9) + lab(P, "P", dy=-6))
# 4(2) BC の中点 M から垂線 MD、ME
A, B, C, cen = base(56, 110, 72)
M = pt_on(B, C, .5); Dd = foot(M, A, B); Ee = foot(M, A, C)
g2 = (poly(A, B, C) + seg(M, Dd) + seg(M, Ee) + tick(B, M) + tick(M, C)
      + tick(M, Dd, 2) + tick(M, Ee, 2) + right_angle(Dd, M, B, 6) + right_angle(Ee, M, C, 6)
      + labels({"A": A, "B": B, "C": C, "D": Dd, "E": Ee}, "ABCDE", cen, 9) + lab(M, "M", dy=14))

def cell(n, f, ans):
    return ('<div class="cell"><span class="sn">(%d)</span>%s<p>∠%s＝%s°</p></div>' % (n, f, X, z(ans)))

body = "".join([
q(1, "次の図で、∠%s の大きさを求めなさい。同じ印の辺・角は等しい。" % X, "",
  '<div class="row c4">%s%s%s%s</div>'
  % (cell(1, fig("0 0 118 114", f1, "", 36), "64"), cell(2, fig("0 0 118 114", f2, "", 36), "36"),
     cell(3, fig("0 0 118 114", f3, "BD は ∠B の二等分線", 36), "75"),
     cell(4, fig("0 0 118 114", f4, "BD＝BC", 36), "30"))),

'<div class="row c2" style="align-items:start">',
q(2, "ことばで答えなさい。", "",
  '<ol class="sub"><li>二等辺三角形の定義　%s</li><li>正三角形の定義　%s</li>'
  '<li>直角三角形の合同条件（2つ）%s</li></ol>'
  % (bz(7, "2つの辺が等しい三角形"), bz(7, "3つの辺が等しい三角形"),
     bz(12, "斜辺と1つの鋭角がそれぞれ等しい（⑭）<br>斜辺と他の1辺がそれぞれ等しい（⑮）"))),
q(3, "逆を書き、正しいかどうか答えなさい。正しくなければ反例を1つ。", "",
  '<ol class="sub"><li><i>x</i>＞3 ならば <i>x</i>＞2　%s</li>'
  '<li>正三角形ならば、3つの角は等しい　%s</li>'
  '<li>△ABC≡△DEF ならば、2つの三角形の面積は等しい　%s</li></ol>'
  % (bz(9, "逆 <i>x</i>＞2 ならば <i>x</i>＞3。正しくない。反例 <i>x</i>＝2.5"),
     bz(9, "逆 3つの角が等しい三角形は正三角形。正しい"),
     bz(9, "逆 面積が等しいならば合同。正しくない。反例 底辺4・高さ3 と 底辺6・高さ2 の三角形"))),
'</div>',

q(4, "次のことを証明しなさい。根拠は、内容をことばで書いてから（根拠○）。", "",
  '<div class="row c2" style="align-items:start">'
  '<div class="cell"><p><span class="sn">(1)</span> AB＝AC の二等辺三角形 ABC で、∠B、∠C の二等分線の'
  '交点を P とする。<b>△PBC は二等辺三角形</b>である。</p>%s%s</div>'
  '<div class="cell"><p><span class="sn">(2)</span> △ABC の辺 BC の中点 M から辺 AB、AC に垂線 MD、ME をひく。'
  '<b>MD＝ME ならば AB＝AC</b> である。</p>%s%s</div></div>'
  % (fig("0 0 144 130", g1, "", 38),
     bz(44, "BP、CP はそれぞれ ∠B、∠C の二等分線だから　∠PBC＝(1/2)∠ABC、∠PCB＝(1/2)∠ACB<br>"
            "二等辺三角形の底角は等しいから（根拠⑪）　∠ABC＝∠ACB<br>"
            "よって　∠PBC＝∠PCB<br>"
            "2つの角が等しい三角形は二等辺三角形だから（根拠⑬）、"
            "△PBC は PB＝PC の二等辺三角形である　■"),
     fig("0 0 144 130", g2, "", 38),
     bz(44, "△BDM と △CEM において<br>"
            "仮定より　∠BDM＝∠CEM＝90°　……(a)<br>"
            "M は BC の中点だから　BM＝CM（斜辺）　……(b)<br>"
            "仮定より　MD＝ME　……(c)<br>"
            "(a)(b)(c)より、直角三角形の斜辺と他の1辺がそれぞれ等しいから（根拠⑮）　△BDM≡△CEM<br>"
            "対応する角は等しいから　∠B＝∠C<br>"
            "2つの角が等しい三角形は二等辺三角形だから（根拠⑬）　AB＝AC　■"))),

memo("<b>つまずき</b>　1(3) は外角（40°＋35°）。1(4) は △BCD も二等辺三角形で、2回使う。"
     "4(2) は結論の AB＝AC を図から読まない（それを示すのが問題）。"),
])

SHEET = dict(
    kind="宿題①", title="1節 三角形",
    lead="範囲　第2〜6時　　使うカード　⑪〜⑮ と 4章の ①〜⑩　　"
         "<b>わからないところは、次の時間に誰かに聞く。</b>",
    body=body,
    footer="中学2年 数学　5章 三角形・四角形　宿題プリント① 1節／A4",
)

if __name__ == "__main__":
    print(build(SHEET, sys.argv[1]), "bytes")
