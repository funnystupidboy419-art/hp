# -*- coding: utf-8 -*-
"""小テスト① 1節 三角形（第2〜6時の範囲）20点・10分

本番（リピートプリント）の形に寄せる: 大問1 角度、大問5 直角三角形の合同。
証明は記述で書かせる（本番は穴うめだが、授業では記述で書く方針）。
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a4_sheet import (build, q, fig, memo, z, bz, score, NAME, iso, foot, pt_on, seg, poly,
                      lab, labels, angle_arc, angle_label, tick, right_angle, check_angle)

# 1 角度 --------------------------------------------------------------
def tri(apex, mark_at, mark_txt, x_at, extra="", D=None):
    A = (60, 14)
    B, C = iso(A, apex, 92)
    P = {"A": A, "B": B, "C": C}
    s = poly(A, B, C) + tick(A, B) + tick(A, C)
    names = ["A", "B", "C"]
    if D:
        P["D"] = (C[0] + 34, C[1]); s += seg(C, P["D"]); names.append("D")
    ang = {"A": (A, B, C), "B": (B, A, C), "C": (C, A, B)}
    if D:
        ang["Cx"] = (C, A, P["D"])
    V, P1, P2 = ang[mark_at]
    s += angle_arc(V, P1, P2, r=13) + angle_label(V, P1, P2, mark_txt, r=25)
    V, P1, P2 = ang[x_at]
    s += angle_arc(V, P1, P2, r=11) + angle_label(V, P1, P2, "<tspan font-style='italic'>x</tspan>", r=22)
    s += labels(P, ["A", "B", "C"], center=((A[0]+B[0]+C[0])/3, (A[1]+B[1]+C[1])/3), d=9)
    if D:
        s += lab(P["D"], "D", dy=14)
    return s, P

f1a, P = tri(40, "A", "40°", "B");             check_angle(P["A"], P["B"], P["C"], 40)
f1b, P = tri(50, "B", "65°", "A");             check_angle(P["B"], P["A"], P["C"], 65)
f1c, P = tri(40, "Cx", "110°", "A", D=True);   check_angle(P["C"], P["A"], P["D"], 110)

# 2 合同な直角三角形 ---------------------------------------------------
A2 = (72, 12); B2, C2 = iso(A2, 50, 112)
D2 = foot(B2, A2, C2); E2 = foot(C2, A2, B2)
P2 = {"A": A2, "B": B2, "C": C2, "D": D2, "E": E2}
cen2 = ((A2[0]+B2[0]+C2[0])/3, (A2[1]+B2[1]+C2[1])/3)
f2 = (poly(A2, B2, C2) + seg(B2, D2) + seg(C2, E2) + tick(A2, B2) + tick(A2, C2)
      + right_angle(D2, B2, C2, s=7) + right_angle(E2, C2, B2, s=7)
      + labels(P2, ["A", "B", "C", "D", "E"], center=cen2, d=9))

# 4 証明 ---------------------------------------------------------------
A4 = (72, 12); B4, C4 = iso(A4, 44, 118)
D4 = pt_on(A4, B4, 0.52); E4 = pt_on(A4, C4, 0.52)
P4 = {"A": A4, "B": B4, "C": C4, "D": D4, "E": E4}
cen4 = ((A4[0]+B4[0]+C4[0])/3, (A4[1]+B4[1]+C4[1])/3)
f4 = (poly(A4, B4, C4) + seg(D4, C4) + seg(E4, B4) + tick(D4, B4, 2) + tick(E4, C4, 2)
      + labels(P4, ["A", "B", "C", "D", "E"], center=cen4, d=9))

X = "<i>x</i>"
body = "".join([
q(1, "次の図で、∠%s の大きさを求めなさい。同じ印の辺は等しい。" % X, "各2点【知】",
  '<div class="row c3">'
  '<div class="cell"><span class="sn">(1)</span>%s<p>∠%s＝%s°</p></div>'
  '<div class="cell"><span class="sn">(2)</span>%s<p>∠%s＝%s°</p></div>'
  '<div class="cell"><span class="sn">(3)</span>%s<p>∠%s＝%s°</p></div></div>'
  % (fig("0 0 120 112", f1a, "", 42), X, z("70"),
     fig("0 0 120 112", f1b, "", 42), X, z("50"),
     fig("0 0 140 112", f1c, "D は辺 BC の延長上", 48), X, z("40"))),

'<div class="row c2" style="grid-template-columns:1fr 1.05fr; align-items:start">',
q(2, "AB＝AC の二等辺三角形 ABC で、頂点 B、C から辺 AC、AB に垂線 BD、CE をひく。",
  "各2点【知】",
  fig("0 0 150 126", f2, "", 50)
  + '<ol class="sub"><li>△DBC と合同な三角形を答えなさい（頂点の順をそろえる）。<br>%s</li>'
    '<li>(1) で使った合同条件を書きなさい。<br>%s</li></ol>'
  % (z("△ECB", "w"), z("斜辺と1つの鋭角がそれぞれ等しい", "ww"))),
q(3, "次のことがらの逆を書き、正しいかどうかを答えなさい。", "4点【知】",
  '<p>「<i>x</i>＝2、<i>y</i>＝3 ならば、<i>x</i>＋<i>y</i>＝5 である」</p>'
  '<ol class="sub"><li>逆<br>%s</li>'
  '<li>正しいか。正しくなければ<b>反例</b>を1つあげなさい。%s</li></ol>'
  % (bz(13, "<i>x</i>＋<i>y</i>＝5 ならば、<i>x</i>＝2、<i>y</i>＝3 である"),
     bz(13, "正しくない。反例: <i>x</i>＝1、<i>y</i>＝4（和は5だが <i>x</i>≠2）"))),
'</div>',

q(4, "AB＝AC の二等辺三角形 ABC の辺 AB、AC 上に、<b>BD＝CE</b> となる点 D、E をとる。"
     "このとき <b>DC＝EB</b> であることを証明しなさい。", "6点【思】",
  '<div class="row c2" style="grid-template-columns:52mm 1fr; align-items:start">%s%s</div>'
  '<p class="inst">根拠は、内容をことばで書いてから（根拠○）と書く。番号だけで書かない。</p>'
  % (fig("0 0 150 128", f4, "AB＝AC、BD＝CE（2本線）"),
     bz(52, "△DBC と △ECB において<br>"
            "仮定より　DB＝EC　……(a)<br>"
            "BC は共通　……(b)<br>"
            "二等辺三角形の底角は等しいから（根拠⑪）　∠DBC＝∠ECB　……(c)<br>"
            "(a)(b)(c)より、2組の辺とその間の角がそれぞれ等しいから（根拠②）　△DBC≡△ECB<br>"
            "合同な図形では対応する辺は等しいから　DC＝EB　■"))),

memo("<b>採点</b>　4 は6点＝三角形の組1、等しいこと3つ各1（根拠をことばで書けていること。番号だけは0.5）、合同条件1、結論1。"
     "<b>本番との対応</b>　1→大問1、2→大問5。"),
])

SHEET = dict(
    kind="小テスト①", title="1節 三角形", right=NAME + score(20),
    lead="範囲　第2〜6時（二等辺三角形・逆と反例・直角三角形の合同）　時間　10分　"
         "<b>知識・技能 14点／思考・判断・表現 6点</b>",
    body=body,
    footer="中学2年 数学　5章 三角形・四角形　小テスト① 1節／A4",
)

if __name__ == "__main__":
    print(build(SHEET, sys.argv[1]), "bytes")
