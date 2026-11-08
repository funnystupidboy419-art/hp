# -*- coding: utf-8 -*-
"""第5時 BE＝CD と正三角形（学校図書『数学2』p.154-157）学び合い"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a3_sheet import build, angle_arc, angle_deg, tick, grid, z, rz, fig

A, B, C = (100, 16), (35, 126), (165, 126)
D = (57.8, 87.5)   # B から AB 上に 0.35
E = (142.2, 87.5)  # C から AC 上に 0.35
f1 = "".join([
    '<polygon class="l" points="100,16 35,126 165,126"/>',
    '<line class="l" x1="35" y1="126" x2="142.2" y2="87.5"/>',
    '<line class="l" x1="165" y1="126" x2="57.8" y2="87.5"/>',
    tick(A, B), tick(A, C),
    tick(B, D, 2), tick(C, E, 2),
    '<text class="t" x="100" y="10" text-anchor="middle">A</text>',
    '<text class="t" x="25" y="136">B</text><text class="t" x="169" y="136">C</text>',
    '<text class="t" x="46" y="84">D</text><text class="t" x="146" y="84">E</text>',
])
t1, t2, t3 = (70, 16), (20, 104), (120, 104)
f2 = "".join([
    '<polygon class="l" points="70,16 20,104 120,104"/>',
    tick(t1, t2), tick(t1, t3), tick(t2, t3),
    '<text class="t" x="70" y="10" text-anchor="middle">A</text>',
    '<text class="t" x="10" y="114">B</text><text class="t" x="124" y="114">C</text>',
])

SHEET = dict(
    title="証明は人に読まれる",
    ji="第5時",
    pg="学校図書『数学2』p.154-157／1節 三角形（全18時間・学び合い）",
    goal="自分の書いた証明が、ほかの人に読んでわかるものになっているか判断できる。",
    katari="今日も先生は教えません。わからなければ聞きに行き、聞かれたら答えてください。"
           "今日の中心は<b>人の証明を読むこと</b>です。合っているかだけでなく、"
           "<b>読んでわかるか</b>を見ます。",
    cards_title="根拠カード — 今日は新しいカードはない。持っているカードで進む",
    cards_hint="①②③と⑪⑫⑬は見てよい。新しいカードが増えない回は、"
               "<b>持っているカードを選ぶ力</b>をつける回。",
    cards=[("①", "3組の辺がそれぞれ等しい（4章）"),
           ("②", "2組の辺とその間の角がそれぞれ等しい（4章）"),
           ("③", "1組の辺とその両端の角がそれぞれ等しい（4章）"),
           ("⑪", "二等辺三角形の2つの底角は等しい"),
           ("⑫", "二等辺三角形の頂角の二等分線は、底辺を垂直に2等分する"),
           ("⑬", "2つの角が等しい三角形は、二等辺三角形である")],
    footer="中学2年 数学　5章 三角形・四角形（全18時間）　第5時 証明を読む／A3横・5ブロック",
    blocks=[
"""    <p class="inst">カード⑪⑫⑬をペアで1つずつ言う。言えなかった番号を書く。</p>
    <ol>
      <li>言えなかった番号 %s</li>
      <li>⑬は、どのカードの「逆」でしたか %s</li>
    </ol>
    <div class="spacer"></div>
    <p class="inst">わからないことは<b>先生ではなく友だちに</b>聞く。</p>"""
% (z("", "w"), z("⑪")),

"""    <p>二等辺三角形 ABC の等しい辺 AB、AC 上に <b>BD＝CE</b> となる点 D、E をとり、
      B と E、C と D を結ぶ。</p>
    %s
    <p class="inst">このとき <b>BE＝CD</b> になりそうだ。これを証明する。</p>
    <div class="spacer"></div>
    <p class="inst" style="border-top:1px dotted var(--rule); padding-top:5px">
      <b>今日の問い</b>　書けた証明は、<b>ほかの人が読んでわかる</b>ものになっているか。</p>"""
% fig("0 0 200 146", f1, "図1　AB＝AC（1本線）、BD＝CE（2本線）"),

"""    <ol>
      <li><b>BE＝CD を証明する。</b>（図1）<br>
        <span class="inst">書く前に</span>　<span class="cn">使う合同条件</span>%s
        <span class="cn">どの2つの三角形か</span>%s
        %s</li>
      <li><b>次は、ある人が書いた証明です。合ってはいますが、2か所足りません。</b>
        <div class="badproof" style="font-size:11px">
          <p style="margin:0">△ABE と △ACD において</p>
          <p style="margin:2px 0 0;padding-left:1em">仮定から　AB＝AC　……(a)</p>
          <p style="margin:2px 0 0;padding-left:1em">仮定から　BD＝CE　……(b)</p>
          <p style="margin:2px 0 0;padding-left:1em">(a)(b)から　AB−BD＝AC−CE</p>
          <p style="margin:2px 0 0;padding-left:1em">AD＝AB−BD、AE＝AC−CE だから　AD＝AE　……(c)</p>
          <p style="margin:2px 0 0;padding-left:1em">また　∠A は共通　……(d)</p>
          <p style="margin:2px 0 0;padding-left:1em">よって (a)(c)(d) より　△ABE≡△ACD</p>
        </div>
        足りない2か所を書く。
        %s</li>
      <li>図2の正三角形で、∠A＝∠B＝∠C を証明する。<br>
        <span class="inst">ヒント: 正三角形を「二等辺三角形」として<b>2通りに</b>見る。</span>
        %s
        %s</li>
    </ol>"""
% (z("②"), z("△ABE と △ACD", "ww"),
   rz(5, "△ABE と △ACD において<br>"
         "仮定より　AB＝AC　……(a)<br>"
         "仮定より　BD＝CE。AD＝AB−BD、AE＝AC−CE だから　AD＝AE　……(b)<br>"
         "∠A は共通　……(c)<br>"
         "(a)(b)(c)より、<b>カード②</b>（2組の辺とその間の角）から　△ABE≡△ACD<br>"
         "合同な図形では対応する辺は等しいから　BE＝CD　■"),
   rz(3, "1つめ: <b>使った合同条件の名前（カード②）が書いていない</b>。"
         "どれを使ったのかが読む人にわからない。<br>"
         "2つめ: <b>最後の結論 BE＝CD が書いていない</b>。合同を示しただけで止まっている。<br>"
         "※ 計算そのものは正しい。「正しいが、読めない」証明だと伝える。"),
   fig("0 0 140 120", f2, "図2　AB＝BC＝CA"),
   rz(4, "AB＝AC の二等辺三角形とみると、カード⑪より　∠B＝∠C　……(a)<br>"
         "BA＝BC の二等辺三角形とみると、カード⑪より　∠A＝∠C　……(b)<br>"
         "(a)(b)より　∠A＝∠B＝∠C　■<br>"
         "※ 同じ図を<b>2通りに見る</b>のがこの問題の山。")),

"""    <p class="inst">1人では届きません。となりと相談してよい。<b>どこまで自分で進めたか</b>を書く。</p>
    <p>図1では、点 D、E を<b>辺 AB、AC の上</b>にとりました。<br>
      <b>辺の延長上にとっても、BE＝CD といえますか。</b></p>
    <ol class="circ">
      <li>D、E を延長上にとった図を、方眼にかきなさい。
        <div class="gridbox"><svg viewBox="0 0 230 112" role="img" aria-label="作図用の方眼">%s</svg></div></li>
      <li>いえるなら、③(1) の証明の<b>どこが変わりますか</b>。変わらないならそう書きなさい。
        %s</li>
    </ol>"""
% (grid(230, 112, 23),
   rz(3, "<b>いえる。</b>証明はほとんど変わらない。<br>"
         "変わるのは (b) の作り方だけ。延長上なら AD＝AB＋BD、AE＝AC＋CE となり、"
         "たし算になるが、やはり AD＝AE が言える。<br>"
         "(a)(c) と結論はそのまま。<b>同じ筋道が別の場合にも通る</b>ことを確かめるのがこの問題。")),

"""    <ol>
      <li>今日使ったカードの番号 %s</li>
      <li>今日は　聞いた ／ 聞かれた ／ どちらもなかった<br>
        <span class="inst">当てはまるものに丸。名前は書かない。</span></li>
      <li><b>③(2) で足りなかった2つは、なぜ必要なのですか。</b>
        %s</li>
    </ol>
    <div class="spacer"></div>
    <p class="inst tonly" style="border-top:1px dotted var(--rule); padding-top:5px">
      <b>削り順</b>　③(3) を宿題 → ④② を宿題。<br>死守するのは ③(1)(2)。<br>
      ③(2) が今日の中心。全員が「読む人のために書く」に触れてから終わる。</p>"""
% (z("②⑪", "w"),
   rz(3, "証明は自分のためのメモではなく、<b>人に読ませるもの</b>だから。<br>"
         "条件の名前がないと、なぜ合同といえるのかを読む人が自分で探すことになる。<br>"
         "結論がないと、何を示したかったのかがわからない。")),
])

if __name__ == "__main__":
    print(build(SHEET, sys.argv[1]), "bytes")
