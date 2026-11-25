# -*- coding: utf-8 -*-
"""宿題プリント③ 3節 平行線と面積（第11時）

見つける（DE∥BC）→ 作りかえる（四角形を三角形に）→ 比で使う → 発展（どこでも 1/2）。
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a4_sheet import (build, q, fig, memo, z, bz, NAME, pt_on, seg, poly, lab, labels, meet, area,
                      par, dot)

# 1 DE∥BC、BE と CD の交点 O ----------------------------------------------
A, B, C = (82, 12), (14, 108), (164, 108)
D, E = pt_on(A, B, .42), pt_on(A, C, .42)
O = meet(B, E, C, D)
for s1, s2 in [((D, B, C), (E, B, C)), ((D, B, E), (D, C, E)), ((D, B, O), (E, C, O)), ((A, B, E), (A, C, D))]:
    assert abs(area(*s1) - area(*s2)) < 1e-6
f1 = (poly(A, B, C) + seg(D, E) + seg(B, E) + seg(C, D) + par(D, E) + par(B, C)
      + labels({"A": A, "B": B, "C": C}, "ABC", d=9)
      + lab(D, "D", dx=-9, dy=2) + lab(E, "E", dx=9, dy=2) + lab(O, "O", dy=15))

# 2 四角形 ABCD と面積の等しい △PCD（P は直線 BC 上） -----------------------
A2, B2, C2, D2 = (100, 30), (70, 118), (180, 118), (165, 22)
P2 = meet(A2, (A2[0] + D2[0] - B2[0], A2[1] + D2[1] - B2[1]), B2, C2)
assert abs(area(A2, B2, C2, D2) - area(P2, C2, D2)) < 1e-6 and 5 < P2[0] < B2[0]
f2 = ('<line class="d" x1="2" y1="118" x2="196" y2="118"/>' + poly(A2, B2, C2, D2)
      + labels({"A": A2, "B": B2, "C": C2, "D": D2}, "ABCD", d=9)
      + '<g class="ft">' + seg(B2, D2, "a") + seg(A2, P2, "a") + seg(P2, D2, "ftline")
      + dot(P2) + lab(P2, "P", dy=14) + '</g>')

# 3 面積比 BE:EC=1:2、CF:FD=1:1 -----------------------------------------------
A3, D3, C3, B3 = (52, 12), (182, 12), (152, 98), (22, 98)
E3, F3 = pt_on(B3, C3, 1/3), pt_on(C3, D3, .5)
S = area(A3, B3, C3, D3)
for t, want in [((A3, B3, E3), 1/6), ((A3, F3, D3), 1/4), ((E3, C3, F3), 1/6), ((A3, E3, F3), 5/12)]:
    assert abs(area(*t) / S - want) < 1e-9
f3 = (poly(A3, D3, C3, B3) + seg(A3, E3) + seg(A3, F3) + seg(E3, F3)
      + labels({"A": A3, "B": B3, "C": C3, "D": D3}, "ABCD", d=9)
      + lab(E3, "E", dy=14) + lab(F3, "F", dx=9, dy=2))

# 4 内部の点 P：△PAB＋△PCD は □ABCD の 1/2 -----------------------------------
A4, D4, C4, B4 = (50, 12), (172, 12), (146, 94), (24, 94)
P4 = (110, 44)
assert abs(area(P4, A4, B4) + area(P4, C4, D4) - area(A4, B4, C4, D4) / 2) < 1e-6
f4 = (poly(A4, D4, C4, B4) + seg(P4, A4) + seg(P4, B4) + seg(P4, C4) + seg(P4, D4) + dot(P4)
      + '<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" style="fill:var(--band)"/>' % (P4 + A4 + B4)
      + '<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" style="fill:var(--band)"/>' % (P4 + C4 + D4)
      + poly(A4, D4, C4, B4) + seg(P4, A4) + seg(P4, B4) + seg(P4, C4) + seg(P4, D4)
      + labels({"A": A4, "B": B4, "C": C4, "D": D4}, "ABCD", d=9) + lab(P4, "P", dy=-6))

body = "".join([
q(1, "△ABC の辺 AB、AC 上に、<b>DE∥BC</b> となる点 D、E をとり、BE と CD の交点を O とする。"
     "面積の等しい三角形の組を<b>4つ</b>見つけなさい。", "",
  '<div class="row c2" style="grid-template-columns:58mm 1fr; align-items:start">%s'
  '<div><p>%s と %s　　%s と %s</p><p>%s と %s　　%s と %s</p>'
  '<p class="inst">ヒント　1組見つけたら、そこから<b>共通な部分をひく・たす</b>と次が見つかる。</p><p>そのうち2組について、理由を書きなさい。根拠は内容をことばで書いてから（根拠○）。</p>%s</div></div>'
  % (fig("0 0 178 122", f1, "DE∥BC"),
     z("△DBC"), z("△EBC"), z("△DBE"), z("△DCE"), z("△DBO"), z("△ECO"), z("△ABE"), z("△ACD"),
     bz(20, "DE∥BC だから、平行線にはさまれ共通な底辺をもつ三角形の面積は等しい（根拠㉓）。"
            "→ △DBC＝△EBC（底辺 BC）、△DBE＝△DCE（底辺 DE）。<br>"
            "△DBO＝△ECO は、△DBC と △EBC から共通な △OBC をひく。"
            "△ABE＝△ACD は、△ADE に △DBE と △DCE をたす。"))),

q(2, "四角形 ABCD と面積の等しい <b>△PCD</b> を、点 P を直線 BC 上にとってかきなさい。"
     "かき方も書きなさい。", "",
  '<div class="row c2" style="grid-template-columns:70mm 1fr; align-items:start">%s%s</div>'
  % (fig("0 0 200 134", f2, "点線は直線 BC"),
     bz(46, "対角線 BD をひく。点 A を通り BD に平行な直線をひき、直線 BC との交点を P とする。"
            "P と D を結ぶ。<br>"
            "理由: AP∥BD だから、平行線にはさまれ共通な底辺 BD をもつ △ABD と △PBD の面積は等しい（根拠㉓）。"
            "四角形 ABCD＝△ABD＋△BCD＝△PBD＋△BCD＝△PCD"))),

'<div class="row c2" style="align-items:start">',
q(3, "□ABCD で、<b>BE：EC＝1：2</b>、<b>CF：FD＝1：1</b> のとき、次の面積は □ABCD の何倍ですか。", "",
  fig("0 -4 196 122", f3, "", 58)
  + '<ol class="sub" style="display:grid; grid-template-columns:1fr 1fr; gap:0 10px">'
    '<li>△ABE　%s</li><li>△AFD　%s</li><li>△ECF　%s</li><li>△AEF　%s</li></ol><p class="inst">(3)(4) の求め方</p>%s'
  % (z("1/6 倍", "w"), z("1/4 倍", "w"), z("1/6 倍", "w"), z("5/12 倍", "w"),
     bz(24, "(3) △ECF：△BCF＝EC：BC＝2：3、△BCF：△BCD＝CF：CD＝1：2、△BCD＝1/2 だから "
            "(2/3)×(1/2)×(1/2)＝1/6<br>(4) 1−1/6−1/4−1/6＝5/12"))),
q(4, "<b>発展</b>　□ABCD の内部に点 P をとる。<b>△PAB＋△PCD</b> の面積は、□ABCD の面積の何倍ですか。"
     "理由も書きなさい。", "",
  fig("0 0 196 106", f4, "P は □ABCD の内部のどこでもよい", 62)
  + '<p>答　%s</p>%s'
  % (z("1/2 倍", "w"),
     bz(30, "AB と DC を底辺とみると、2つの三角形の高さの和は、AB と DC の間の距離（□ABCD の高さ）"
            "に等しい。平行四辺形の対辺は等しいから（根拠⑯）AB＝DC。<br>△PAB＋△PCD＝AB×（高さの和）÷2＝□ABCD÷2。"
            "<b>P がどこにあっても変わらない。</b>"))),
'</div>',

memo("<b>つまずき</b>　1 は2組で止まる生徒が多い。「共通な部分をひく」で △DBO＝△ECO、"
     "「同じものをたす」で △ABE＝△ACD が出る（第11時③(2)㋑と同じ操作）。<br>"
     "2 は第11時④の逆向き（P を B の外側にとる）。<b>どの対角線をひくか</b>を自分で決めるのがねらい。<br>"
     "4 は P を辺の近くに動かして確かめさせると、「どこでも 1/2」が実感できる。"),
])

SHEET = dict(
    kind="宿題③", title="3節 平行線と面積",
    lead="範囲　第11時　　使うカード　㉓ と ⑯（平行四辺形の対辺）　　"
         "<b>わからないところは、次の時間に誰かに聞く。</b>",
    body=body,
    footer="中学2年 数学　5章 三角形・四角形　宿題プリント③ 3節／A4",
)

if __name__ == "__main__":
    print(build(SHEET, sys.argv[1]), "bytes")
