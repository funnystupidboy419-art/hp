# -*- coding: utf-8 -*-
"""第11時 平行線と面積（3節）学び合い
   ㉓ を導き、四角形を面積の等しい三角形に直すところまで。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a3_sheet import build, angle_arc, tick, par, right_angle, z, bz, fig, memo

# 図1 ℓ∥m、底辺 BC 共通、頂点が ℓ 上
B1, C1, A1, D1 = (40, 120), (160, 120), (70, 30), (140, 30)
f1 = "".join([
    '<line class="d" x1="8" y1="30" x2="205" y2="30"/>',
    '<line class="d" x1="8" y1="120" x2="205" y2="120"/>',
    '<polygon class="l" points="70,30 40,120 160,120"/>',
    '<polygon class="l" points="140,30 40,120 160,120"/>',
    par((8, 30), (205, 30)), par((8, 120), (205, 120)),
    '<g class="ft"><line class="ftline" x1="70" y1="30" x2="70" y2="120" stroke-dasharray="4 3"/>'
    + '<line class="ftline" x1="140" y1="30" x2="140" y2="120" stroke-dasharray="4 3"/></g>',
    '<text class="t" x="12" y="26">ℓ</text><text class="t" x="12" y="132">m</text>',
    '<text class="t" x="64" y="24">A</text><text class="t" x="138" y="24">D</text>',
    '<text class="t" x="30" y="132">B</text><text class="t" x="164" y="132">C</text>',
])
# 図2 AD∥BC の台形と対角線
tA, tD, tB, tC = (66, 22), (158, 22), (18, 122), (196, 122)
f2 = "".join([
    '<polygon class="l" points="66,22 158,22 196,122 18,122"/>',
    '<line class="l" x1="66" y1="22" x2="196" y2="122"/>',
    '<line class="l" x1="158" y1="22" x2="18" y2="122"/>',
    par(tA, tD), par(tB, tC),
    '<circle cx="110.3" cy="56.1" r="2.3" fill="var(--fig)"/>',
    '<text class="t" x="60" y="16">A</text><text class="t" x="160" y="16">D</text>',
    '<text class="t" x="8" y="134">B</text><text class="t" x="199" y="134">C</text>',
    '<text class="t" x="114" y="53">O</text>',
])
# 図3 AC∥EF（E は AD 上、F は DC 上。AE:ED=3:2、DF:FC=2:3）
pA, pB, pC, pD = (60, 24), (20, 120), (150, 120), (190, 24)
pE, pF = (138, 24), (174, 62.4)
f3 = "".join([
    '<polygon class="l" points="60,24 190,24 150,120 20,120"/>',
    '<line class="l" x1="60" y1="24" x2="150" y2="120"/>',    # AC
    '<line class="l" x1="138" y1="24" x2="174" y2="62.4"/>',  # EF
    '<line class="l" x1="60" y1="24" x2="174" y2="62.4"/>',   # AF
    '<line class="l" x1="150" y1="120" x2="138" y2="24"/>',   # CE
    '<line class="l" x1="20" y1="120" x2="138" y2="24"/>',    # BE
    '<line class="l" x1="20" y1="120" x2="174" y2="62.4"/>',  # BF
    par(pA, pC, 2), par(pE, pF, 2),
    '<text class="t" x="52" y="18">A</text><text class="t" x="133" y="18">E</text>',
    '<text class="t" x="192" y="18">D</text><text class="t" x="178" y="62">F</text>',
    '<text class="t" x="10" y="132">B</text><text class="t" x="148" y="132">C</text>',
])

# 図4 四角形 ABCD を面積の等しい三角形に（JUMP）
qA, qB, qC, qD, qP = (55, 40), (30, 120), (120, 120), (165, 70), (205.6, 120)
f4 = "".join([
    '<line class="l" x1="20" y1="120" x2="218" y2="120"/>',
    '<polygon class="l" points="55,40 30,120 120,120 165,70"/>',
    '<g class="ft">'
    '<line class="ftline" x1="55" y1="40" x2="120" y2="120" stroke-dasharray="4 3"/>'
    '<line class="ftline" x1="165" y1="70" x2="205.6" y2="120" stroke-dasharray="4 3"/>'
    '<line class="ftline" x1="55" y1="40" x2="205.6" y2="120"/>'
    '<circle cx="205.6" cy="120" r="2.4" fill="var(--accent)"/>'
    '<text class="t" x="203" y="133" fill="var(--accent)">P</text></g>',
    '<text class="t" x="49" y="34">A</text><text class="t" x="20" y="133">B</text>',
    '<text class="t" x="117" y="133">C</text><text class="t" x="169" y="68">D</text>',
])

SHEET = dict(
    title="形はちがうが、面積は同じ",
    ji="第11時",
    pg="学校図書『数学2』3節 平行線と面積（全14時間・学び合い）",
    goal="平行線にはさまれた三角形の面積が等しいことを説明し、図形を同じ面積のまま作りかえられる。",
    katari="ここまでは「形が同じ（合同）」を調べてきました。今日は<b>形はちがうのに面積は同じ</b>"
           "という話です。これができると、<b>四角形を、面積を変えずに三角形に直す</b>ことができます。",
    cards_title="今日手に入れるカードは ㉓ の1枚（別紙のカードを用意）",
    cards_hint="三角形の面積＝底辺×高さ÷2（小学校）。<b>高さ</b>がどこなのかを毎回確かめる。",
    footer="中学2年 数学　5章 三角形・四角形（全14時間）　第11時 平行線と面積／A3横",
    blocks=[
"""    <p class="inst">小学校の復習。隣の人に言う。</p>
    <ol>
      <li>三角形の面積＝%s</li>
      <li>平行四辺形の面積＝%s</li>
    </ol>
    <p class="inst" style="margin-top:6px"><b>高さ</b>とは、底辺から向かい合う頂点までの
      %s の長さ。</p>
    <div class="spacer"></div>
    <p class="inst">今日は、この「高さ」が主役。</p>"""
% (z("底辺×高さ÷2", "ww"), z("底辺×高さ", "ww"), z("垂線", "w")),

"""    <p>図1 で、△ABC と △DBC をくらべる。</p>
    %s
    <p class="inst">形はちがう。頂点の位置もちがう。<br>
      でも、底辺 BC は %s で、ℓ∥m だから高さも %s。</p>
    <div class="spacer"></div>
    <p class="inst" style="border-top:1px dotted var(--rule); padding-top:5px">
      <b>今日の問い</b>　形がちがっても面積が等しくなるのは、<b>どんなとき</b>か。</p>"""
% (fig("0 0 215 142", f1, "図1　ℓ∥m。底辺 BC は共通"), z("共通", "w"), z("等しい", "w")),

"""    <ol>
      <li><b>△ABC＝△DBC（面積が等しい）といえる理由を書きなさい。</b>（図1）
        %s
        <p class="inst" style="margin-top:3px">※ ここでの「＝」は<b>面積が等しい</b>という意味。
          合同ではない。</p></li>
      <li>AD∥BC の台形 ABCD で、対角線の交点を O とする。
        %s
        ㋐ △ABC と面積の等しい三角形は %s　根拠 %s<br>
        ㋑ <b>△ABO＝△DCO</b> を説明しなさい。
        %s</li>
      <li>□ABCD で、E は辺 AD 上、F は辺 DC 上にあり、<b>AC∥EF</b> である。
        %s
        ㋐ <b>△ACF と面積の等しい三角形を3つ</b>答えなさい。<br>
        　%s　%s　%s
        <span class="inst">それぞれ<b>どの平行線</b>を使ったか。</span>%s</li>
    </ol>"""
% (bz(22, "ℓ∥m だから、A と D から BC までの距離（高さ）は等しい。<br>"
          "底辺 BC は共通なので、底辺×高さ÷2 が等しい。よって面積が等しい。"
          "　→ これが<b>根拠㉓</b>"),
   fig("0 0 215 142", f2, "図2　AD∥BC", "128px"),
   z("△DBC", "w"), z("㉓"),
   bz(26, "AD∥BC だから（根拠㉓）△ABC＝△DBC。<br>"
          "どちらからも共通部分の △OBC をひくと<br>"
          "△ABC−△OBC＝△ABO、△DBC−△OBC＝△DCO<br>"
          "よって △ABO＝△DCO　■"),
   fig("0 0 215 142", f3, "図3　AC∥EF", "128px").replace(
       "<svg ", '<svg style="max-width:240px" ', 1),
   z("△ACE", "w"), z("△ABE", "w"), z("△BCF", "w"),
   bz(20, "△ACE … <b>AC∥EF</b>。底辺 AC が共通で、頂点 F と E が EF 上。<br>"
          "△ABE … <b>AD∥BC</b>。底辺 AE が共通で、頂点 C と B が BC 上（△ACE とくらべる）。<br>"
          "△BCF … <b>AB∥DC</b>。底辺 CF が共通で、頂点 A と B が AB 上。<br>"
          "3つとも根拠は<b>㉓</b>。<b>使う平行線が3組ちがう</b>のがこの問題のおもしろさ。"),
   ),

"""    <p class="inst">練習プリント⑥の4 と同じ問題。</p>
    <p>四角形 ABCD がある。直線 BC 上に点 P をとって、<b>△ABP の面積を
      四角形 ABCD の面積と等しく</b>したい。</p>
    <p><b>点 P をどのような位置にとればよいか、答えなさい。</b></p>
    %s
    <p class="inst">※ 四角形を、面積を変えずに三角形に直す。これを<b>等積変形</b>という。</p>
    %s
    %s"""
% (fig("0 0 225 142", f4, "図4　四角形 ABCD と直線 BC"),
   bz(40, "対角線 AC をひく。点 D を通り AC に平行な直線をひき、"
          "直線 BC との交点を P とする。<br>"
          "AC∥DP だから（根拠㉓）△ACD＝△ACP。<br>"
          "四角形 ABCD＝△ABC＋△ACD、△ABP＝△ABC＋△ACP だから<br>"
          "四角形 ABCD＝△ABP　■<br>"
          "※ <b>動かすのは頂点 D だけ</b>。AC を軸にして D を直線 BC 上までずらした、と見る。"),
   memo("<b>型</b>　なぜいえるか（③(1)）→ 使う（③(2)(3)）→ 応用（④）。<br>"
        "③(1) は「高さが等しい」の一言にたどりつけばよい。ℓ∥m から垂線の長さが等しい。<br>"
        "③(2)㋑ は<b>共通部分をひく</b>という操作が要。<br>"
        "③(3) は<b>同じ㉓を、ちがう平行線で3回使う</b>問題。3つ出たら「どの平行線を使った？」と必ず聞く。ここが今日いちばん考えるところ。<br>"
        "④が今日のチャレンジ。<b>D を AC に平行に動かす</b>と気づけるかどうか。"
        "届いた生徒に黒板でやらせると、全体が一気に分かる。<br>"
        "発展: 五角形を四角形に、四角形を三角形に、と続けられる（土地の境界線の引き直し）。<br>"
        "<b>削り順</b>　③(2)㋐ を省く。死守するのは ③(1)(2)㋑(3) と ④。<br>"
        "<b>2枚目</b>（発展プリント）に、この続き（面積比と、その逆向き）を用意してある。")),
])

if __name__ == "__main__":
    print(build(SHEET, sys.argv[1]), "bytes")
