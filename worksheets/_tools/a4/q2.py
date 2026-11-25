# -*- coding: utf-8 -*-
"""小テスト② 2節 四角形（第7〜10時の範囲）20点・10分

本番（リピートプリント）の形に寄せる: 大問2・3 平行四辺形の角と長さ、
大問4 平行四辺形になる条件をすべて選ぶ、大問6 証明の穴うめ。
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a4_sheet import (build, q, fig, memo, z, bz, score, NAME, pt_on, seg, poly, lab, labels,
                      angle_arc, angle_label, tick, par, check_angle)

# 1 角と長さ: AB=6、AD=10、∠B=70°、∠A の二等分線と BC の交点 E ----------------
k = 13.0                      # 1cm を 13 単位
B = (14, 104); C = (B[0] + 10*k, B[1])
A = (B[0] + 6*k*math.cos(math.radians(70)), B[1] - 6*k*math.sin(math.radians(70)))
D = (A[0] + 10*k, A[1]); E = (B[0] + 6*k, B[1])
check_angle(B, A, C, 70)
check_angle(A, B, E, 55); check_angle(A, E, D, 55)        # AE は ∠A の二等分線
check_angle(E, A, C, 125)
P1 = {"A": A, "B": B, "C": C, "D": D, "E": E}
f1 = (poly(A, D, C, B) + seg(A, E) + angle_arc(B, A, C, r=12) + angle_label(B, A, C, "70°", r=24)
      + angle_arc(A, B, E, r=12, cls="a") + angle_arc(A, E, D, r=15, cls="a")
      + angle_arc(E, A, C, r=13) + angle_label(E, A, C, "<tspan font-style='italic'>y</tspan>", r=25)
      + angle_arc(D, A, C, r=13) + angle_label(D, A, C, "<tspan font-style='italic'>x</tspan>", r=25)
      + lab(pt_on(A, B, .5), "6cm", dx=-16, cls="ts") + lab(pt_on(A, D, .5), "10cm", dy=-5, cls="ts")
      + labels(P1, ["A", "B", "C", "D"], d=9) + lab(E, "E", dy=14))

# 2 AD∥BC の四角形 ----------------------------------------------------------
A2, D2, C2, B2 = (44, 16), (112, 16), (138, 84), (14, 84)
f2 = (poly(A2, D2, C2, B2) + par(A2, D2) + par(B2, C2)
      + labels({"A": A2, "B": B2, "C": C2, "D": D2}, ["A", "B", "C", "D"], d=9))

# 3 穴うめ: 対角線 BD 上に BE=DF ---------------------------------------------
A3, D3, C3, B3 = (44, 14), (164, 14), (134, 100), (14, 100)
E3, F3 = pt_on(B3, D3, .28), pt_on(D3, B3, .28)
P3 = {"A": A3, "B": B3, "C": C3, "D": D3, "E": E3, "F": F3}
f3 = (poly(A3, D3, C3, B3) + seg(B3, D3) + seg(A3, E3) + seg(C3, F3)
      + tick(B3, E3, 2) + tick(D3, F3, 2)
      + labels(P3, ["A", "B", "C", "D"], d=9) + lab(E3, "E", dx=-2, dy=15) + lab(F3, "F", dx=2, dy=-6))

X, Y = "<i>x</i>", "<i>y</i>"
body = "".join([
q(1, "□ABCD で、∠A の二等分線と辺 BC の交点を E とする。AB＝6cm、AD＝10cm、∠B＝70° のとき、"
     "次の値を求めなさい。", "各2点【知】",
  '<div class="row c2" style="grid-template-columns:62mm 1fr; align-items:center">%s'
  '<ol class="sub"><li>∠%s＝%s°</li><li>EC の長さ　%s cm</li><li>∠%s＝%s°</li></ol></div>'
  % (fig("0 -6 186 132", f1), X, z("70"), z("4"), Y, z("125"))),

'<div class="row c2" style="grid-template-columns:1.1fr 1fr; align-items:start">',
q(2, "AD∥BC の四角形 ABCD に、次の条件を加える。<b>必ず平行四辺形になる</b>ものを"
     "すべて選びなさい。", "4点【知】",
  fig("0 -2 152 104", f2, "AD∥BC（図は条件を加える前）", 46)
  + '<p>㋐ AD＝BC　　㋑ AB＝DC　　㋒ ∠A＝∠C　　㋓ ∠A＝∠B</p><p>答　%s</p>' % z("㋐、㋒", "w")),
q(3, "□ABCD に次の条件を加えると、どんな四角形になりますか。", "各1点【知】",
  '<ol class="sub"><li>AC＝BD　　%s</li><li>AC⊥BD　　%s</li></ol>'
  % (z("長方形", "w"), z("ひし形", "w"))
  + '<p class="inst">AC、BD は対角線。</p>'),
'</div>',

q(4, "□ABCD の対角線 BD 上に、<b>BE＝DF</b> となる点 E、F をとる。"
     "AE＝CF であることを次のように証明した。ア〜エにあてはまることばや式を書きなさい。",
  "各2点【思】",
  '<div class="row c2" style="grid-template-columns:58mm 1fr; align-items:start">%s'
  '<div class="bz" style="padding:5px 8px; line-height:1.95">'
  '△ABE と △CDF において<br>'
  '仮定より　BE＝DF　……(a)<br>'
  '（ア）%s から　AB＝CD　……(b)<br>'
  'AB∥DC で、（イ）%s は等しいから　∠ABE＝（ウ）%s　……(c)<br>'
  '(a)(b)(c)より、（エ）%s がそれぞれ等しいから　△ABE≡△CDF<br>'
  '合同な図形では対応する辺は等しいから　AE＝CF</div></div>'
  % (fig("0 0 180 116", f3, "BE＝DF（2本線）"),
     z("平行四辺形の対辺は等しい", "ww"), z("錯角", "w"), z("∠CDF", "w"),
     z("2組の辺とその間の角", "ww"))),

memo("<b>本番との対応</b>　1→大問2・3（角と長さ）、2→大問4（条件をすべて選ぶ）、4→大問6（証明の穴うめ）。<br>"
     "2 の㋑は<b>等脚台形</b>が反例、㋓は ∠A＋∠B＝180° から両方 90° になるだけで台形のまま。"
     "㋒は ∠B＝180°−∠A＝180°−∠C＝∠D となり、2組の対角が等しい（根拠⑳）。<br>"
     "4 のアは「⑯」と番号だけ書いたら1点。ウは ∠CDB も正解。2 はすべて選べて4点、1つ過不足で2点。"),
])

SHEET = dict(
    kind="小テスト②", title="2節 四角形", right=NAME + score(20),
    lead="範囲　第7〜10時（平行四辺形の性質・なるための条件・特別な四角形）　時間　10分　□ABCD は平行四辺形 ABCD のこと　"
         "<b>知識・技能 12点／思考・判断・表現 8点</b>",
    body=body,
    footer="中学2年 数学　5章 三角形・四角形　小テスト② 2節／A4",
)

if __name__ == "__main__":
    print(build(SHEET, sys.argv[1]), "bytes")
