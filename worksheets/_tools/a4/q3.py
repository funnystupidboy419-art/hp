# -*- coding: utf-8 -*-
"""小テスト③ 3節 平行線と面積（第11時の範囲）20点・10分

本番（リピートプリント）には出ないが、もう1種類のテストの大問4(2)に面積が出る。
㉓ を「見つける」「理由を言う」「使って作りかえる」「比で使う」の4つで確かめる。
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a4_sheet import (build, q, fig, memo, z, bz, score, NAME, pt_on, seg, poly, lab, labels,
                      par, meet, area, dot)

# 1・2 台形 AD∥BC と対角線 ----------------------------------------------------
A, D, C, B = (52, 14), (118, 14), (150, 96), (12, 96)
O = meet(A, C, B, D)
f1 = (poly(A, D, C, B) + seg(A, C) + seg(B, D) + par(A, D) + par(B, C)
      + labels({"A": A, "B": B, "C": C, "D": D}, ["A", "B", "C", "D"], d=9)
      + lab(O, "O", dy=14))

# 3 境界線の引き直し -------------------------------------------------------
TL, TR, BR, BL = (10, 10), (200, 10), (200, 120), (10, 120)
E, P, F = (80, 10), (150, 62), (110, 120)
Q = meet(P, (P[0]+F[0]-E[0], P[1]+F[1]-E[1]), BL, BR)
assert abs(area(TL, E, P, F, BL) - area(TL, E, Q, BL)) < 1e-6
f3 = (poly(TL, TR, BR, BL) + '<polyline class="l" points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" '
      'style="stroke-width:2.4"/>' % (E + P + F)
      + dot(E) + dot(P) + dot(F)
      + lab(E, "E", dx=-9, dy=13) + lab(P, "P", dx=9, dy=2) + lab(F, "F", dy=13)
      + lab((55, 72), "田", cls="ts") + lab((180, 45), "畑", cls="ts")
      + '<g class="ft">' + seg(E, F, "a") + seg(P, Q, "a") + seg(E, Q, "ftline")
      + lab(Q, "Q", dy=13) + '</g>')

# 4 面積比 BE:EC=1:3 --------------------------------------------------------
A4, D4, C4, B4 = (50, 14), (178, 14), (148, 96), (20, 96)
E4 = pt_on(B4, C4, .25)
assert abs(area(A4, B4, E4) / area(A4, B4, C4, D4) - 1/8) < 1e-9
assert abs(area(A4, E4, D4) / area(A4, B4, C4, D4) - 1/2) < 1e-9
f4 = (poly(A4, D4, C4, B4) + seg(A4, E4) + seg(E4, D4)
      + labels({"A": A4, "B": B4, "C": C4, "D": D4}, ["A", "B", "C", "D"], d=9)
      + lab(E4, "E", dy=14))

body = "".join([
'<div class="row c2" style="grid-template-columns:66mm 1fr; align-items:start">',
fig("0 0 164 112", f1, "AD∥BC。O は対角線の交点"),
'<div>',
q(1, "左の図で、<b>面積の等しい三角形</b>の組を3つ答えなさい。", "各2点【知】",
  '<p>%s と %s</p><p>%s と %s</p><p>%s と %s</p>'
  % (z("△ABC", "w"), z("△DBC", "w"), z("△ABD", "w"), z("△ACD", "w"),
     z("△ABO", "w"), z("△DCO", "w"))),
q(2, "△ABC と △DBC の面積が等しい理由を書きなさい。", "4点【知】",
  bz(30, "△ABC と △DBC は<b>底辺 BC が共通</b>。AD∥BC だから、A と D から BC までの距離"
         "（<b>高さ</b>）が等しい。底辺と高さが等しいので面積が等しい（根拠㉓）。")),
'</div></div>',

q(3, "田と畑の境界が、折れ線 E―P―F になっている。それぞれの面積を変えずに、"
     "点 E と<b>下の辺上の点 Q</b> を結ぶ、まっすぐな境界に引き直したい。", "5点【思】",
  '<div class="row c2" style="grid-template-columns:80mm 1fr; align-items:start">%s'
  '<div><p>Q の決め方を書き、図に Q と新しい境界をかき入れなさい。三角定規を使ってよい。</p>%s</div></div>'
  % (fig("0 0 212 136", f3, "長方形の土地。E、F は辺上の点"),
     bz(58, "線分 EF をひく。点 P を通り EF に平行な直線をひき、下の辺との交点を Q とする。"
            "<b>線分 EQ が新しい境界。</b><br>"
            "理由: EF∥PQ だから、底辺 EF が共通な △EPF と △EQF の面積は等しい（根拠㉓）。"
            "田から △EPF を取って △EQF を足すことになるので、田の面積は変わらない。"))),

q(4, "□ABCD の辺 BC 上に、<b>BE：EC＝1：3</b> となる点 E をとる。", "5点【思】",
  '<div class="row c2" style="grid-template-columns:70mm 1fr; align-items:start">%s'
  '<ol class="sub"><li>△ABE の面積は □ABCD の面積の何倍ですか。（2点）　%s</li>'
  '<li>△AED の面積は □ABCD の面積の何倍ですか。理由も書きなさい。（3点）　%s%s</li></ol></div>'
  % (fig("0 -2 196 120", f4),
     z("1/8 倍", "w"), z("1/2 倍", "w"),
     bz(34, "△AED は底辺 AD、高さは AD と BC の間の距離で、□ABCD と<b>底辺も高さも同じ</b>。"
            "三角形は ÷2 なので 1/2 倍。E が BC 上のどこにあっても変わらない。"))),

memo("<b>ねらい</b>　1 見つける → 2 理由を言う → 3 使って作りかえる → 4 比で使う。<br>"
     "3 は Q の位置がずれても、EF と平行な線をひく手順が書けていれば3点。理由まで書けて5点。<br>"
     "4(1) は △ABC＝(1/2)□ABCD、BE：BC＝1：4 で (1/4)×(1/2)＝1/8。"
     "4(2) で「BE：EC を使う」と考えた答案は、E がどこでも同じになることに気づかせる。"),
])

SHEET = dict(
    kind="小テスト③", title="3節 平行線と面積", right=NAME + score(20),
    lead="範囲　第11時（平行線と面積・等積変形・面積比）　時間　10分　根拠は内容をことばで書いてから（根拠○）　"
         "<b>知識・技能 10点／思考・判断・表現 10点</b>",
    body=body,
    footer="中学2年 数学　5章 三角形・四角形　小テスト③ 3節／A4",
)

if __name__ == "__main__":
    print(build(SHEET, sys.argv[1]), "bytes")
