# -*- coding: utf-8 -*-
"""A4縦1枚の紙面（単元計画・小テスト・宿題プリント）を作る。

A3 のワークシートと同じく、1つのソースから生徒用と赤刷りを作る。
答え欄は a3_sheet の z() / bz() をそのまま使う（赤刷りで赤字になる）。
図の部品（角の弧・等しい印・平行の印・直角記号）も a3_sheet のものを使う。

    python3 -I worksheets/_tools/a4/q1.py out.html
    python3 -I worksheets/_tools/make_pdf.py <出力先> <名前> out.html
"""
import io, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from a3_sheet import angle_arc, angle_deg, tick, par, right_angle, z, bz  # noqa: F401

CSS = r"""
:root{
  --paper:#f7f5f1; --surface:#fffefb; --ink:#23201d; --graphite:#6b6560;
  --rule:#d6cfc4; --fig:#35617f; --accent:#b0392b; --accent-soft:#f1e3e0; --band:#edeae3;
  --serif:"Shippori Mincho B1","Hiragino Mincho ProN","Yu Mincho",serif;
  --sans:"Zen Kaku Gothic New","Hiragino Sans","Yu Gothic",sans-serif;
}
@media (prefers-color-scheme:dark){ :root:not([data-theme="light"]){
  --paper:#191715; --surface:#221f1c; --ink:#ece7df; --graphite:#a69d93;
  --rule:#3d382f; --fig:#8ab6d4; --accent:#e0705a; --accent-soft:#3a2723; --band:#262320; } }
:root[data-theme="dark"]{
  --paper:#191715; --surface:#221f1c; --ink:#ece7df; --graphite:#a69d93;
  --rule:#3d382f; --fig:#8ab6d4; --accent:#e0705a; --accent-soft:#3a2723; --band:#262320; }
*{box-sizing:border-box}
body{margin:0; background:var(--paper); color:var(--ink); font-family:var(--sans);
  font-size:13px; line-height:1.65; -webkit-text-size-adjust:100%}
.page{max-width:820px; margin:0 auto; padding:20px 16px 40px; display:flex; flex-direction:column}

/* 見出し */
.hd{display:flex; flex-wrap:wrap; align-items:flex-end; gap:4px 14px; border-bottom:2px solid var(--ink); padding-bottom:6px}
.hd .kind{font-family:var(--serif); font-weight:700; font-size:13px; background:var(--ink); color:var(--surface);
  padding:2px 8px; white-space:nowrap}
.hd h1{font-family:var(--serif); font-weight:700; font-size:20px; margin:0; flex:1 1 220px; min-width:0}
.hd .nm{display:flex; gap:10px; font-size:12px; color:var(--graphite); align-items:flex-end}
.hd .nm span{display:flex; align-items:flex-end; gap:3px; white-space:nowrap}
.hd .nm u{display:inline-block; width:38px; border-bottom:1px solid var(--rule); text-decoration:none; height:1.3em}
.hd .nm u.w{width:100px}
.hd .score{border:1.5px solid var(--ink); padding:2px 8px; font-size:12px; white-space:nowrap}
.hd .score i{display:inline-block; width:34px}
.lead{margin:5px 0 0; font-size:12px; color:var(--graphite)}
.lead b{color:var(--ink)}

/* 問題 */
.q{margin-top:10px; break-inside:avoid}
.q>h3{margin:0; font-size:13.5px; font-weight:700; display:flex; gap:7px; align-items:baseline}
.q>h3 .n{flex:none; background:var(--ink); color:var(--surface); font-size:12px; min-width:1.6em; text-align:center;
  padding:0 4px}
.q>h3 .t{flex:1; min-width:0}
.q>h3 .pt{flex:none; font-size:11px; font-weight:500; color:var(--graphite); white-space:nowrap}
.q p{margin:4px 0 0}
.inst{font-size:11.5px; color:var(--graphite)}
.row{display:grid; gap:6px 10px; margin-top:5px}
.c2{grid-template-columns:1fr 1fr}
.c3{grid-template-columns:repeat(3,1fr)}
.c4{grid-template-columns:repeat(4,1fr)}
@media (max-width:560px){ .c2,.c3,.c4{grid-template-columns:1fr 1fr} }
.cell{min-width:0}
.cell>.sn{font-size:12px; color:var(--graphite)}
ol.sub{margin:4px 0 0; padding:0; list-style:none; counter-reset:s}
ol.sub>li{position:relative; padding-left:2.1em; counter-increment:s; margin-top:4px}
ol.sub>li::before{content:"(" counter(s) ")"; position:absolute; left:0; top:0; color:var(--graphite); font-size:12px}
.blank{display:inline-block; border-bottom:1px solid var(--rule); min-width:9em}

/* 答え欄（a3_sheet の z / bz と同じクラス） */
.z{display:inline-block; min-width:2.6em; padding:0 .3em; border-bottom:1px solid var(--ink);
  text-align:center; color:transparent; font-weight:700}
.z.w{min-width:6em}
.z.ww{min-width:10em; text-align:left}
body.teacher .z{color:var(--accent); border-bottom-color:var(--accent-soft)}
.bz{border:1px solid var(--rule); background:var(--surface); margin-top:4px}
.bz .ans{display:none; margin:0; padding:5px 7px; color:var(--accent); font-size:12px; line-height:1.55}
body.teacher .bz .ans{display:block}
body.teacher .bz{border-color:var(--accent-soft)}
.tonly{display:none}
body.teacher .tonly{display:block}
.memo{border-top:1px dotted var(--rule); margin-top:8px; padding-top:4px; font-size:11.5px; color:var(--accent)}

/* 表 */
table{border-collapse:collapse; width:100%; font-size:12px}
th,td{border:1px solid var(--rule); padding:3px 5px; vertical-align:top; text-align:left}
th{background:var(--band); font-weight:700; white-space:nowrap}
td.c,th.c{text-align:center}
.tag{display:inline-block; font-size:10px; font-weight:700; border:1px solid currentColor; padding:0 3px; line-height:1.3}
.box{border:1px solid var(--rule); background:var(--surface); padding:6px 9px; margin-top:8px}
.box h2{font-family:var(--serif); font-size:14px; margin:0 0 3px}

/* 図 */
figure{margin:2px 0 0}
figure svg{display:block; width:100%; height:auto; margin:0 auto}
figcaption{font-size:10.5px; color:var(--graphite); text-align:center}
svg .l{fill:none; stroke:var(--fig); stroke-width:1.6; stroke-linejoin:round}
svg .d{fill:none; stroke:var(--fig); stroke-width:1.1; stroke-dasharray:4 3}
svg .t{fill:var(--ink); font-family:var(--sans); font-size:12px}
svg .ts{fill:var(--ink); font-family:var(--sans); font-size:10.5px}
svg .m{fill:none; stroke:var(--accent); stroke-width:1.5}
svg .a{fill:none; stroke:var(--accent); stroke-width:1.2}
svg .ft{display:none}
body.teacher svg .ft{display:inline}
svg .ftline{fill:none; stroke:var(--accent); stroke-width:2}
svg .dot{fill:var(--fig)}
.spacer{flex:1; min-height:4px}
footer{margin-top:8px; padding-top:4px; border-top:1px solid var(--rule); font-size:10.5px; color:var(--graphite);
  display:flex; justify-content:space-between; gap:8px; flex-wrap:wrap}

@page{size:A4 portrait; margin:10mm}
@media print{
  :root,:root[data-theme]{--paper:#fff; --surface:#fff; --ink:#000; --graphite:#555;
    --rule:#999; --fig:#000; --accent:#000; --accent-soft:#e6e6e6; --band:#efefef}
  :root body.teacher{--accent:#c0251a}
  body.teacher .z, body.teacher .bz .ans, body.teacher svg .ftline, body.teacher .memo
    {-webkit-print-color-adjust:exact; print-color-adjust:exact}
  html,body{height:100%}
  body{font-size:9.8pt; line-height:1.5}
  .page{max-width:none; padding:0; height:100%}
  .hd h1{font-size:14pt}
  .hd .kind, .q>h3 .n{-webkit-print-color-adjust:exact; print-color-adjust:exact}
  .q{margin-top:3.2mm}
  .q>h3{font-size:10.4pt}
  .q>h3 .pt{font-size:8.4pt}
  .lead, .inst{font-size:8.6pt}
  .z{min-width:2.2em}
  .z.w{min-width:5em}
  .z.ww{min-width:8.5em}
  table{font-size:8.4pt}
  th,td{padding:1.2mm 1.5mm}
  .box h2{font-size:10.4pt}
  svg .t{font-size:12px}
  figcaption{font-size:8pt}
  footer{font-size:7.8pt}
  body.teacher .bz .ans{font-size:8.4pt; line-height:1.42; padding:3px 6px}
  .memo{font-size:8.4pt}
}
"""

_TPL = """<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Shippori+Mincho+B1:wght@600;700&family=Zen+Kaku+Gothic+New:wght@400;500;700&display=swap">
<style>{css}</style>
<div class="page">
<header class="hd">
  <span class="kind">{kind}</span>
  <h1>{title}</h1>
  {right}
</header>
<p class="lead">{lead}</p>
{body}
<div class="spacer"></div>
<footer><span>{footer}</span><span>組・番・名前の記入欄以外に個人情報は記載しないこと</span></footer>
</div>
"""

NAME = ('<span class="nm"><span>組<u></u></span><span>番<u></u></span>'
        '<span>名前<u class="w"></u></span></span>')


def score(total):
    return '<span class="score">得点 <i></i>／%d点</span>' % total


def build(sheet, out_path):
    """sheet = dict(kind, title, lead, body, footer, right(省略可))"""
    html = _TPL.format(css=CSS, right=sheet.get("right", NAME), **{
        k: sheet[k] for k in ("kind", "title", "lead", "body", "footer")})
    with io.open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    return len(html.encode("utf-8"))


# ---------------------------------------------------------------- 問題の部品

def q(n, text, pt, body):
    """大問。n=番号、pt=配点と観点（例 '各2点【知】'）。"""
    return ('<section class="q"><h3><span class="n">%s</span><span class="t">%s</span>'
            '<span class="pt">%s</span></h3>%s</section>' % (n, text, pt, body))


def fig(view, body, caption="", width_mm=None):
    st = ' style="max-width:%gmm"' % width_mm if width_mm else ""
    cap = "<figcaption>%s</figcaption>" % caption if caption else ""
    return '<figure><svg viewBox="%s" role="img" aria-label="%s"%s>%s</svg>%s</figure>' % (
        view, caption or "図", st, body, cap)


def memo(text):
    """赤刷りだけに出す教師メモ。"""
    return '<p class="memo tonly">%s</p>' % text


# ---------------------------------------------------------------- 図の計算

def pt_on(P, Q, t):
    return (P[0] + (Q[0]-P[0])*t, P[1] + (Q[1]-P[1])*t)


def foot(P, A, B):
    """P から直線 AB への垂線の足。"""
    ax, ay = B[0]-A[0], B[1]-A[1]
    t = ((P[0]-A[0])*ax + (P[1]-A[1])*ay) / float(ax*ax + ay*ay)
    return (A[0]+ax*t, A[1]+ay*t)


def meet(P1, P2, P3, P4):
    """直線 P1P2 と直線 P3P4 の交点。"""
    x1, y1 = P1; x2, y2 = P2; x3, y3 = P3; x4, y4 = P4
    d = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if abs(d) < 1e-9:
        raise ValueError("平行で交わらない")
    t = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4)) / d
    return (x1 + t*(x2-x1), y1 + t*(y2-y1))


def area(*P):
    s = 0.0
    for i in range(len(P)):
        x1, y1 = P[i]; x2, y2 = P[(i+1) % len(P)]
        s += x1*y2 - x2*y1
    return abs(s) / 2


def iso(A, apex_deg, leg):
    """頂点 A が上、底辺が水平な二等辺三角形 ABC（AB=AC=leg、∠A=apex_deg）。"""
    h = math.radians(apex_deg / 2.0)
    B = (A[0] - leg*math.sin(h), A[1] + leg*math.cos(h))
    C = (A[0] + leg*math.sin(h), A[1] + leg*math.cos(h))
    return B, C


def seg(P, Q, cls="l"):
    return '<line class="%s" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (cls, P[0], P[1], Q[0], Q[1])


def poly(*P, cls="l"):
    return '<polygon class="%s" points="%s"/>' % (cls, " ".join("%.1f,%.1f" % p for p in P))


def lab(P, s, dx=0, dy=0, cls="t", anchor="middle"):
    """点のラベル。dx, dy で点からずらす（文字の基準は中央・ベースライン）。"""
    return '<text class="%s" x="%.1f" y="%.1f" text-anchor="%s">%s</text>' % (
        cls, P[0]+dx, P[1]+dy, anchor, s)


def away(P, center, d=10):
    """center から見て P の外側に d だけ離した位置（ラベル置き場）。文字高さぶん下げる。"""
    vx, vy = P[0]-center[0], P[1]-center[1]
    n = math.hypot(vx, vy) or 1.0
    return (P[0] + vx/n*d, P[1] + vy/n*d + 4)


def labels(pts, names, center=None, d=10):
    """names の各点に、図形の中心から外向きにラベルを置く。"""
    if center is None:
        xs = [pts[n][0] for n in names]; ys = [pts[n][1] for n in names]
        center = (sum(xs)/len(xs), sum(ys)/len(ys))
    return "".join(lab(away(pts[n], center, d), n) for n in names)


def angle_label(V, P1, P2, text, r=24, cls="ts"):
    """角の内側（二等分線の向き）に文字を置く。"""
    u1 = ((P1[0]-V[0]), (P1[1]-V[1])); n1 = math.hypot(*u1)
    u2 = ((P2[0]-V[0]), (P2[1]-V[1])); n2 = math.hypot(*u2)
    b = (u1[0]/n1 + u2[0]/n2, u1[1]/n1 + u2[1]/n2); nb = math.hypot(*b)
    return lab((V[0] + b[0]/nb*r, V[1] + b[1]/nb*r + 4), text, cls=cls)


def dot(P, r=2.2):
    return '<circle class="dot" cx="%.1f" cy="%.1f" r="%g"/>' % (P[0], P[1], r)


def check_angle(V, P1, P2, want, tol=0.6):
    """図の角が、問題文の値と一致しているかを確かめる（ずれていたら止める）。"""
    got = angle_deg(V, P1, P2)
    if abs(got - want) > tol:
        raise ValueError("図の角が合わない: %.2f° (期待 %s°)" % (got, want))
    return got
