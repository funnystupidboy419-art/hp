"""A3横5ブロック・ワークシートのビルダ。

使い方: lessons/tNN.py で SHEET を定義し、build(SHEET, 出力パス) を呼ぶ。

記法の約束（18枚で統一する）
- 証明の式番号 …… (a)(b)(c)
- 選択肢 …………… ㋐㋑㋒㋓
- ことがらの見出し … ア イ ウ
- JUMP の小問 ……… ol.circ（①②）
- カード番号 ……… ①〜⑩（4章）／⑪〜㉓（5章）
番号の体系どうしがぶつかると、解答の「①②③より」がカード番号と読めてしまう。

時間配分は既定で ①5 ②5 ③20 ④15 ⑤5（合計50分）。
⑤のふりかえりはタブレットのアプリで行うので、紙はコード欄だけ。
blocks[4] に None を渡すと既定の⑤が入る。教師用のメモは sheet["memo"] に書く。

④に「1人では届きません」「となりと相談してよい」「どこまで自分で進めたか」は書かない。
学び合いでは当たり前のことなので、毎回書くと紙が重くなる。
教師主導の回など配分を変えるときは sheet["mins"] で上書きする（合計50分を検査する）。
ブロック名を変えるときは sheet["names"]。

宿題・削り順・ねらいの運用メモは、⑤ の tonly（赤刷りのみ）に置く。
生徒に見せる注意書きだけ .hw を使う。

図形は必ずこのモジュールの幾何ヘルパ経由で描く。
角の弧を手で書かないこと（sweep-flag を間違えると弧が反対側に出る。
見た目では気づきにくく、実際に第2時と A4版 v2 で起きた）。
"""
import math, os, io

HERE = os.path.dirname(os.path.abspath(__file__))

def _css():
    with io.open(os.path.join(HERE, "_style.css"), encoding="utf-8") as f:
        return f.read()

# ---------------------------------------------------------------- 幾何ヘルパ

def _u(v):
    n = math.hypot(*v)
    return (v[0]/n, v[1]/n)

def _arc_mid(p0, p1, r, large, sweep):
    """SVG F.6.5 の端点→中心変換。弧の中点を返す。"""
    (x1, y1), (x2, y2) = p0, p1
    dx2, dy2 = (x1-x2)/2.0, (y1-y2)/2.0
    rx = ry = r
    lam = dx2*dx2/(rx*rx) + dy2*dy2/(ry*ry)
    if lam > 1:
        rx *= math.sqrt(lam); ry *= math.sqrt(lam)
    num = rx*rx*ry*ry - rx*rx*dy2*dy2 - ry*ry*dx2*dx2
    den = rx*rx*dy2*dy2 + ry*ry*dx2*dx2
    c = math.sqrt(max(num/den, 0.0))
    if large == sweep:
        c = -c
    cx = c*rx*dy2/ry + (x1+x2)/2.0
    cy = -c*ry*dx2/rx + (y1+y2)/2.0
    a1 = math.atan2((y1-cy)/ry, (x1-cx)/rx)
    a2 = math.atan2((y2-cy)/ry, (x2-cx)/rx)
    d = a2 - a1
    if sweep == 0 and d > 0: d -= 2*math.pi
    if sweep == 1 and d < 0: d += 2*math.pi
    am = a1 + d/2
    return (cx + rx*math.cos(am), cy + ry*math.sin(am))

def angle_arc(V, P1, P2, r=20, cls="a"):
    """頂点 V の、V→P1 と V→P2 がはさむ角に弧を描く。

    sweep-flag は、弧の中点が二等分線の向きに来る側を計算で選ぶ。
    どちらでも合わない場合は例外（描かないほうが安全）。
    """
    u1, u2 = _u((P1[0]-V[0], P1[1]-V[1])), _u((P2[0]-V[0], P2[1]-V[1]))
    A = (V[0]+r*u1[0], V[1]+r*u1[1])
    B = (V[0]+r*u2[0], V[1]+r*u2[1])
    bis = _u((u1[0]+u2[0], u1[1]+u2[1]))
    want = (V[0]+r*bis[0], V[1]+r*bis[1])
    best = None
    for sweep in (0, 1):
        m = _arc_mid(A, B, r, 0, sweep)
        d = math.hypot(m[0]-want[0], m[1]-want[1])
        if best is None or d < best[0]:
            best = (d, sweep)
    if best[0] > r*0.25:
        raise ValueError("角の弧の向きが決まりません: V=%s P1=%s P2=%s" % (V, P1, P2))
    return ('<path class="%s" d="M%.1f,%.1f A%g,%g 0 0 %d %.1f,%.1f"/>'
            % (cls, A[0], A[1], r, r, best[1], B[0], B[1]))

def angle_deg(V, P1, P2):
    """頂点 V の角の大きさ（度）。ラベルに書く数値は必ずこれで出す。"""
    u1 = _u((P1[0]-V[0], P1[1]-V[1])); u2 = _u((P2[0]-V[0], P2[1]-V[1]))
    return math.degrees(math.acos(max(-1.0, min(1.0, u1[0]*u2[0]+u1[1]*u2[1]))))

def tick(P, Q, n=1, L=4.5, gap=3.0, cls="m"):
    """線分 PQ の中点に、等しいことを示す斜線を n 本引く。"""
    u = _u((Q[0]-P[0], Q[1]-P[1]))
    per = (u[1], -u[0])
    mx, my = (P[0]+Q[0])/2.0, (P[1]+Q[1])/2.0
    out = []
    for i in range(n):
        off = (i - (n-1)/2.0) * gap
        cx, cy = mx + u[0]*off, my + u[1]*off
        out.append('<line class="%s" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
                   % (cls, cx-per[0]*L, cy-per[1]*L, cx+per[0]*L, cy+per[1]*L))
    return "".join(out)

def right_angle(V, P1, P2, s=8, cls="a"):
    """頂点 V の直角記号。V→P1 と V→P2 の方向に一辺 s の L 字を描く。"""
    u1 = _u((P1[0]-V[0], P1[1]-V[1])); u2 = _u((P2[0]-V[0], P2[1]-V[1]))
    a = (V[0]+s*u1[0], V[1]+s*u1[1])
    c = (V[0]+s*u2[0], V[1]+s*u2[1])
    b = (a[0]+s*u2[0], a[1]+s*u2[1])
    return ('<polyline class="%s" points="%.1f,%.1f %.1f,%.1f %.1f,%.1f"/>'
            % (cls, a[0], a[1], b[0], b[1], c[0], c[1]))

def grid(w=160, h=120, step=20):
    """作図用の方眼。中央線だけ濃くする。"""
    out = ['<rect class="g" x="0.5" y="0.5" width="%g" height="%g"/>' % (w-1, h-1)]
    thin, thick = [], []
    for x in range(step, w, step):
        (thick if abs(x-w/2) < 1 else thin).append(
            '<line x1="%g" y1="0" x2="%g" y2="%g"/>' % (x, x, h))
    for y in range(step, h, step):
        (thick if abs(y-h/2) < 1 else thin).append(
            '<line x1="0" y1="%g" x2="%g" y2="%g"/>' % (y, w, y))
    out.append('<g class="g">%s</g>' % "".join(thin))
    out.append('<g class="gm">%s</g>' % "".join(thick))
    return "".join(out)

# ---------------------------------------------------------------- 部品

def z(ans="", cls=""):
    """答えの欄。生徒用は空白、赤刷りは赤字。ans を空にすると自由回答欄。"""
    return '<span class="z %s">%s</span>' % (cls, ans)

def rz(lines, ans=""):
    """罫線の記述欄。赤刷りでは ans が出る。"""
    body = "".join('<div class="ln"></div>' for _ in range(lines))
    a = '<p class="ans">%s</p>' % ans if ans else ""
    return '<div class="rz">%s%s</div>' % (body, a)

def fig(view, body, caption, flex=None):
    st = ' style="flex:1 1 %s; min-width:0"' % flex if flex else ""
    return ('<figure%s><svg viewBox="%s" role="img" aria-label="%s">%s</svg>'
            '<figcaption>%s</figcaption></figure>'
            % (st, view, caption, body, caption))

# ---------------------------------------------------------------- 組み立て

_TPL = """<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Shippori+Mincho+B1:wght@600;700&family=Zen+Kaku+Gothic+New:wght@400;500;700&display=swap">
<style>
{css}
</style>

<div class="wrap">

<header>
  <div class="hdr">
    <span class="ji">{ji}</span>
    <span class="pg">{pg}</span>
    <span class="goal"><b>めあて</b>　{goal}</span>
    <span class="nm"><span>組<u></u></span><span>番<u></u></span><span>名前<u style="width:88px"></u></span></span>
  </div>
  <p class="katari"><b>語り</b>　{katari}</p>
</header>

<div class="bar">
  <button id="mode" type="button" aria-pressed="false">赤刷り（教師用）にする</button>
  <button id="print" type="button">印刷する</button>
  <span class="barnote">印刷は A3・横。いま表示している側（生徒用／赤刷り）がそのまま印刷されます。</span>
</div>

<div class="cards">
  <h3>{cards_title}</h3>
  <ul>
{cards}
  </ul>
  <p class="hint">{cards_hint}</p>
</div>

<div class="blocks">
{blocks}
</div>

<footer>
  <span>{footer}</span>
  <span>印刷して配る前提の紙。生徒にこの URL を渡さないこと（答えがページ内に入っている）<br>組・番・名前の記入欄以外に個人情報は記載しないこと</span>
</footer>
</div>

<script>
(function(){{
  var b=document.body, m=document.getElementById('mode');
  m.addEventListener('click',function(){{
    var on=b.classList.toggle('teacher');
    m.setAttribute('aria-pressed',String(on));
    m.textContent = on ? '生徒用にもどす' : '赤刷り（教師用）にする';
  }});
  document.getElementById('print').addEventListener('click',function(){{ window.print(); }});
}})();
</script>
"""

_BLOCK = """  <section class="bk">
    <h2><span class="n">{n}</span>{name}<span class="min">{min}分</span></h2>
{body}
  </section>
"""

_NAMES = ["前時の復習", "今日やること", "練習", "JUMP課題", "ふりかえり"]

# ⑤ はどの回も同じ。ふりかえりはタブレットのアプリで行うので、紙はコード欄だけ。
_REFLECT = """    <p class="inst">ふりかえりは<b>タブレットのアプリ</b>で行う。</p>
    <p style="margin-top:8px">今日のコード</p>
    <div class="codebox"><span></span><span></span><span></span><span></span></div>
    <p class="inst" style="margin-top:6px">黒板のコードを写してから、アプリに入力する。</p>
    <div class="spacer"></div>
{memo}"""

def reflect(memo):
    """⑤ブロック。memo は赤刷りだけに出る教師用のメモ（削り順・介入点など）。"""
    m = ('    <p class="inst tonly" style="border-top:1px dotted var(--rule); padding-top:5px">%s</p>'
         % memo) if memo else ""
    return _REFLECT.format(memo=m)
_MINS = [5, 5, 20, 15, 5]

def build(sheet, out_path):
    mins = sheet.get("mins", _MINS)
    if sheet["blocks"][4] is None:                 # ⑤ を既定（アプリでふりかえり）にする
        sheet["blocks"][4] = reflect(sheet.get("memo", ""))
    assert sum(mins) == 50, "5ブロックの合計が50分になっていません: %s" % (mins,)
    names = sheet.get("names", _NAMES)
    blocks = "".join(
        _BLOCK.format(n="①②③④⑤"[i], name=names[i], min=mins[i], body=sheet["blocks"][i])
        for i in range(5))
    cards = "\n".join('    <li><i>%s</i>%s</li>' % (c[0], c[1]) for c in sheet["cards"])
    html = _TPL.format(css=_css(), blocks=blocks, cards=cards, **{
        k: sheet[k] for k in
        ("title", "ji", "pg", "goal", "katari", "cards_title", "cards_hint", "footer")})
    with io.open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    return len(html.encode("utf-8"))
