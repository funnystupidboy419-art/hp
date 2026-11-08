# -*- coding: utf-8 -*-
"""根拠カード（別紙）。A3横に切り取り式のカードを並べる。

生徒は手に入れた順にカードを増やしていく。空のカードは、自分で見つけた
ことがらを書き足すためのもの。
"""
import io, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))

# (番号, 命題, 手に入れる時, 教科書)
CARDS = [
    ("⑪", "二等辺三角形の2つの底角は等しい", "第2時", "p.150-151"),
    ("⑫", "二等辺三角形の頂角の二等分線は、底辺を垂直に2等分する", "第2時", "p.152"),
    ("⑬", "2つの角が等しい三角形は、二等辺三角形である", "第3時", "p.154"),
    ("⑭", "直角三角形で、斜辺と1つの鋭角がそれぞれ等しければ合同である", "第5時", "p.159"),
    ("⑮", "直角三角形で、斜辺と他の1辺がそれぞれ等しければ合同である", "第5時", "p.159"),
    ("⑯", "平行四辺形の2組の対辺はそれぞれ等しい", "第7時", "p.164"),
    ("⑰", "平行四辺形の2組の対角はそれぞれ等しい", "第7時", "p.164"),
    ("⑱", "平行四辺形の2つの対角線はそれぞれの中点で交わる", "第7時", "p.164"),
    ("⑲", "2組の対辺がそれぞれ等しい四角形は平行四辺形である", "第8時", "p.168"),
    ("⑳", "2組の対角がそれぞれ等しい四角形は平行四辺形である", "第8時", "p.168"),
    ("㉑", "2つの対角線がそれぞれの中点で交わる四角形は平行四辺形である", "第8時", "p.168"),
    ("㉒", "1組の対辺が平行で、その長さが等しい四角形は平行四辺形である", "第8時", "p.168"),
    ("㉓", "平行線にはさまれ、共通な底辺をもつ三角形の面積は等しい", "時数未定", "p.—"),
]
BLANKS = 2   # 自分で見つけたことがらを書くカード

CSS = """
:root{
  --paper:#f7f5f1; --surface:#fffefb; --ink:#23201d; --graphite:#6b6560;
  --rule:#d6cfc4; --accent:#b0392b; --band:#edeae3;
  --serif:"Shippori Mincho B1","Hiragino Mincho ProN","Yu Mincho",serif;
  --sans:"Zen Kaku Gothic New","Hiragino Sans","Yu Gothic",sans-serif;
}
@media (prefers-color-scheme:dark){ :root:not([data-theme="light"]){
  --paper:#191715; --surface:#221f1c; --ink:#ece7df; --graphite:#a69d93;
  --rule:#3d382f; --accent:#e0705a; --band:#262320; } }
:root[data-theme="dark"]{
  --paper:#191715; --surface:#221f1c; --ink:#ece7df; --graphite:#a69d93;
  --rule:#3d382f; --accent:#e0705a; --band:#262320; }
*{box-sizing:border-box}
body{margin:0; background:var(--paper); color:var(--ink); font-family:var(--sans);
  font-size:13px; line-height:1.7; -webkit-text-size-adjust:100%}
.wrap{padding:18px 16px 40px; max-width:1500px; margin:0 auto}
h1{font-family:var(--serif); font-size:clamp(20px,4vw,26px); margin:0; text-wrap:balance}
.sub{margin:4px 0 0; font-size:12.5px; color:var(--graphite)}
.bar{display:flex; gap:9px; margin:14px 0 0}
button{font-family:var(--sans); font-size:12.5px; color:var(--ink); background:var(--surface);
  border:1px solid var(--rule); border-radius:2px; padding:6px 13px; cursor:pointer}
button:hover{border-color:var(--accent); color:var(--accent)}
button:focus-visible{outline:2px solid var(--accent); outline-offset:2px}

.deck{display:grid; gap:8px; margin-top:16px;
  grid-template-columns:repeat(auto-fill,minmax(150px,1fr))}
.card{border:1.4px dashed var(--rule); border-radius:5px; background:var(--surface);
  padding:9px 10px 7px; display:flex; flex-direction:column; min-height:150px; position:relative}
.card .no{font-family:var(--serif); font-weight:700; font-size:23px; color:var(--accent); line-height:1}
.card .no small{font-family:var(--sans); font-size:9.5px; font-weight:700; color:var(--graphite);
  letter-spacing:.1em; margin-left:5px; vertical-align:3px}
.card .txt{margin:7px 0 0; font-size:12.5px; line-height:1.55; flex:1}
.card .foot{border-top:1px dotted var(--rule); margin-top:7px; padding-top:4px;
  font-size:9.5px; color:var(--graphite); display:flex; justify-content:space-between; gap:6px}
.card .mirror{position:absolute; right:9px; bottom:18px; font-family:var(--serif);
  font-weight:700; font-size:14px; color:var(--rule); transform:rotate(180deg)}
.card.blank .txt{border-bottom:1px solid var(--rule); min-height:1.6em}
.card.blank .txt+.txt{margin-top:9px}
.card.blank .no{color:var(--graphite)}
.note{margin-top:16px; font-size:12px; color:var(--graphite); border-left:3px solid var(--accent);
  padding-left:10px}

@page{size:A3 landscape; margin:9mm}
@media print{
  :root,:root[data-theme]{--paper:#fff; --surface:#fff; --ink:#000; --graphite:#555;
    --rule:#999; --accent:#000; --band:#f2f2f2}
  body{font-size:10pt}
  .wrap{max-width:none; padding:0}
  .bar{display:none}
  h1{font-size:14pt}
  .deck{grid-template-columns:repeat(5,1fr); gap:5mm; margin-top:7mm}
  .card{min-height:76mm; break-inside:avoid; border-color:#777}
  .card .no{font-size:20pt}
  .card .txt{font-size:10pt}
  .note{margin-top:6mm; font-size:9pt}
}
"""

def card(no, txt, when, page):
    return ('<div class="card"><div class="no">%s<small>5章</small></div>'
            '<p class="txt">%s</p>'
            '<div class="foot"><span>手に入れた日 ____ / ____</span><span>%s・%s</span></div>'
            '<span class="mirror">%s</span></div>' % (no, txt, when, page, no))

def blank(i):
    return ('<div class="card blank"><div class="no">？<small>自分で</small></div>'
            '<p class="txt">&nbsp;</p><p class="txt">&nbsp;</p><p class="txt">&nbsp;</p>'
            '<div class="foot"><span>手に入れた日 ____ / ____</span><span>自分で見つけた</span></div></div>')

HTML = """<title>根拠カード 5章</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Shippori+Mincho+B1:wght@600;700&family=Zen+Kaku+Gothic+New:wght@400;500;700&display=swap">
<style>%s</style>
<div class="wrap">
  <h1>根拠カード　5章 三角形・四角形</h1>
  <p class="sub">証明で「〜だから」と書けることがら。手に入れた順に増えていく。
    4章で手に入れた ①〜⑩（合同条件など）と合わせて使う。</p>
  <div class="bar"><button id="print" type="button">印刷する（A3・横）</button></div>
  <div class="deck">%s</div>
  <p class="note">切り取って、手に入れた順に並べる。<b>まだ手に入れていないカードは使えない。</b><br>
    白いカードは、自分で見つけたことがらを書くためのもの。</p>
</div>
<script>document.getElementById('print').addEventListener('click',function(){window.print();});</script>
"""

def build(out_path):
    deck = "".join(card(*c) for c in CARDS) + "".join(blank(i) for i in range(BLANKS))
    html = HTML % (CSS, deck)
    io.open(out_path, "w", encoding="utf-8").write(html)
    return len(html.encode("utf-8"))

if __name__ == "__main__":
    print(build(sys.argv[1]), "bytes /", len(CARDS), "枚 +", BLANKS, "枚（白）")
