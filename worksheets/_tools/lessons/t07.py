# -*- coding: utf-8 -*-
"""第7時 平行四辺形の定義と性質①（学校図書『数学2』p.162-164）学び合い
   なぜ「2組の対辺が等しい」といえるのかを導いてから使う。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a3_sheet import build, angle_arc, angle_deg, tick, par, z, bz, fig, memo

A, D, B, C = (50, 24), (190, 24), (20, 118), (160, 118)
O = (105, 71)
f1 = "".join([
    '<polygon class="l" points="50,24 190,24 160,118 20,118"/>',
    par(A, D), par(B, C), par(A, B, 2), par(D, C, 2),
    '<text class="t" x="44" y="18">A</text><text class="t" x="192" y="18">D</text>',
    '<text class="t" x="10" y="130">B</text><text class="t" x="164" y="130">C</text>',
])
f2 = "".join([
    '<polygon class="l" points="50,24 190,24 160,118 20,118"/>',
    '<line class="l" x1="20" y1="118" x2="190" y2="24"/>',
    par(A, D), par(B, C), par(A, B, 2), par(D, C, 2),
    '<g class="ft">%s%s</g>' % (tick(A, B, 3, cls="ftline"), tick(D, C, 3, cls="ftline")),
    '<text class="t" x="44" y="18">A</text><text class="t" x="192" y="18">D</text>',
    '<text class="t" x="10" y="130">B</text><text class="t" x="164" y="130">C</text>',
])
# 長さを求める
f3 = "".join([
    '<polygon class="l" points="50,24 190,24 160,118 20,118"/>',
    par(A, D), par(B, C), par(A, B, 2), par(D, C, 2),
    '<text class="t" x="44" y="18">A</text><text class="t" x="192" y="18">D</text>',
    '<text class="t" x="10" y="130">B</text><text class="t" x="164" y="130">C</text>',
    '<text class="t" x="120" y="18">7cm</text>',
    '<text class="t" x="18" y="76">5cm</text>',
    '<text class="t" x="86" y="132"><tspan font-style="italic">x</tspan> cm</text>',
    '<text class="t" x="168" y="76"><tspan font-style="italic">y</tspan> cm</text>',
])
# JUMP: ∠ABC＝∠CDA
f4 = "".join([
    '<polygon class="l" points="50,24 190,24 160,118 20,118"/>',
    '<line class="d" x1="50" y1="24" x2="160" y2="118"/>',
    par(A, D), par(B, C), par(A, B, 2), par(D, C, 2),
    angle_arc(B, A, C, 16), angle_arc(D, C, A, 16),
    '<text class="t" x="44" y="18">A</text><text class="t" x="192" y="18">D</text>',
    '<text class="t" x="10" y="130">B</text><text class="t" x="164" y="130">C</text>',
])

SHEET = dict(
    title="対辺はなぜ等しいのか",
    ji="第7時",
    pg="学校図書『数学2』p.162-164／2節 四角形（全17時間・学び合い）",
    goal="平行四辺形の2組の対辺が等しいことを、定義から導いて使える。",
    katari="平行四辺形は「<b>2組の対辺がそれぞれ平行</b>」と決めただけです。"
           "辺の長さについては何も言っていません。それなのに、向かい合う辺は同じ長さに見えます。"
           "<b>平行だというだけで、長さまで決まってしまうのか</b>を確かめます。",
    cards_title="今日手に入れるカードは ⑯ の1枚（別紙のカードを用意）",
    cards_hint="①②③（4章）と ⑪〜⑮ は使ってよい。平行線の<b>錯角</b>（4章）も使う。",
    footer="中学2年 数学　5章 三角形・四角形（全17時間）　第7時 平行四辺形の性質①／A3横",
    blocks=[
"""    <p class="inst">1節で手に入れたカードを、隣の人に1つ言う。</p>
    <ol>
      <li>いちばん自信のないカードの番号 %s</li>
      <li>4章の復習。2直線が平行のとき、等しくなる角を2つ。
        %s</li>
    </ol>
    <div class="spacer"></div>
    <p class="inst">今日は<b>錯角</b>をよく使う。</p>"""
% (z("", "w"), bz(16, "同位角、錯角")),

"""    <p><b>平行四辺形の定義</b>を書く。</p>
    <p class="inst">%s である四角形を平行四辺形という。</p>
    %s
    <p class="inst">定義で決めているのは<b>平行なことだけ</b>。
      長さについても角についても、まだ何も言っていない。</p>
    <div class="spacer"></div>
    <p class="inst" style="border-top:1px dotted var(--rule); padding-top:5px">
      <b>今日の問い</b>　平行だというだけで、<b>向かい合う辺の長さ</b>まで決まるのか。</p>"""
% (z("2組の対辺がそれぞれ平行", "ww"), fig("0 0 215 140", f1, "図1　平行四辺形 ABCD")),

"""    <ol>
      <li><b>AB＝DC、AD＝BC を証明する。</b>（図2）
        <div class="think">
          <p class="th">考え方</p>
          <p>・辺の長さをいうには、その辺を<b>対応する辺</b>にもつ合同な三角形がいる。</p>
          <p>・四角形のままでは三角形がない。だから %s をひいて2つに分ける。</p>
          <p>・ひいた線は2つの三角形に %s な辺になる。</p>
          <p>・あとは角。<b>平行</b>だから %s が等しい。</p>
        </div>
        %s
        %s</li>
      <li>⑯を使って <i>x</i>、<i>y</i> を求める。
        %s
        <i>x</i>＝%s　<i>y</i>＝%s</li>
    </ol>"""
% (z("対角線", "w"), z("共通", "w"), z("錯角", "w"),
   fig("0 0 215 140", f2, "図2　対角線 BD をひいた"),
   bz(44, "対角線 BD をひく。△ABD と △CDB において<br>"
          "BD は共通　……(a)<br>"
          "AB∥DC で錯角は等しいから　∠ABD＝∠CDB　……(b)<br>"
          "AD∥BC で錯角は等しいから　∠ADB＝∠CBD　……(c)<br>"
          "(a)(b)(c)より、1組の辺とその両端の角がそれぞれ等しいから（<b>根拠③</b>）　△ABD≡△CDB<br>"
          "対応する辺は等しいから　AB＝DC、AD＝BC　■　→ これが<b>根拠⑯</b>"),
   fig("0 0 215 142", f3, "図3　平行四辺形 ABCD", "130px"),
   z("7"), z("5")),

"""    <p>平行四辺形では、<b>向かい合う角</b>も等しく見える。</p>
    <p><b>∠ABC＝∠CDA</b> を証明しなさい。（図4）</p>
    %s
    <p class="inst">※ まだ「対角は等しい」というカードは持っていない。
      いま手に入れた⑯と、4章のカードだけで示す。</p>
    %s
    %s"""
% (fig("0 0 215 140", f4, "図4　∠ABC と ∠CDA"),
   bz(44, "対角線 AC をひく。△ABC と △CDA において<br>"
          "いま証明した⑯より　AB＝CD、BC＝DA　……(a)(b)<br>"
          "AC は共通　……(c)<br>"
          "(a)(b)(c)より、3組の辺がそれぞれ等しいから（<b>根拠①</b>）　△ABC≡△CDA<br>"
          "対応する角は等しいから　∠ABC＝∠CDA　■<br>"
          "※ 対角線 BD をひき、∠ABD＝∠CDB と ∠DBC＝∠BDA をたす方法でもよい。"),
   memo("<b>型</b>　なぜ使えるか（③(1)）→ 使う（③(2)）→ 応用（④）。<br>"
        "③(1) が今日の中心。<b>四角形を対角線で三角形に分ける</b>という手が、"
        "2節のあいだずっと効く。ここで全員に通す。<br>"
        "④は次の時間に⑰として手に入れるものを、先に自力で出させる問題。"
        "できた生徒の証明を第8時の最初に使う。<br>"
        "<b>削り順</b>　③(2) を宿題 → ④を宿題。死守するのは ③(1)。")),
])

if __name__ == "__main__":
    print(build(SHEET, sys.argv[1]), "bytes")
