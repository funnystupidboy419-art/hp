# -*- coding: utf-8 -*-
"""第12時 2節・3節の確かめよう（学校図書『数学2』p.173）学び合い
   ステップ式にしない。問題を多く、余白は書ける高さで。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a3_sheet import build_practice, angle_arc, angle_deg, tick, par, z, bz, fig, memo

A, D, B, C = (50, 24), (190, 24), (20, 118), (160, 118)
lab = ('<text class="t" x="44" y="18">A</text><text class="t" x="192" y="18">D</text>'
       '<text class="t" x="10" y="130">B</text><text class="t" x="164" y="130">C</text>')
pg = ('<polygon class="l" points="50,24 190,24 160,118 20,118"/>'
      + par(A, D) + par(B, C) + par(A, B, 2) + par(D, C, 2) + lab)
# 一般の四角形＋対角線（判定用）
f1 = "".join(['<polygon class="l" points="50,24 190,24 160,118 20,118"/>',
              '<line class="l" x1="50" y1="24" x2="160" y2="118"/>',
              '<line class="l" x1="190" y1="24" x2="20" y2="118"/>',
              '<circle cx="105" cy="71" r="2.3" fill="var(--fig)"/>',
              '<text class="t" x="109" y="68">O</text>', lab])
# 角と長さ
gA, gD, gB, gC = (50, 24), (190, 24), (15.8, 118), (155.8, 118)
assert abs(angle_deg(gA, gB, gD) - 110) < 0.3
f2 = "".join(['<polygon class="l" points="50,24 190,24 155.8,118 15.8,118"/>',
              par(gA, gD), par(gB, gC), par(gA, gB, 2), par(gD, gC, 2),
              angle_arc(gA, gB, gD, 20),
              '<text class="t" x="62" y="44">110°</text>',
              '<text class="t" x="24" y="108"><tspan font-style="italic">x</tspan></text>',
              '<text class="t" x="136" y="108"><tspan font-style="italic">y</tspan></text>',
              '<text class="t" x="44" y="18">A</text><text class="t" x="192" y="18">D</text>',
              '<text class="t" x="6" y="130">B</text><text class="t" x="160" y="130">C</text>'])
# □ABCD の辺 AD、BC 上に AE＝CF
E, F = (100, 24), (110, 118)
f3 = (pg + '<line class="l" x1="100" y1="24" x2="20" y2="118"/>'
         + '<line class="l" x1="110" y1="118" x2="190" y2="24"/>'
         + tick(A, E, 2) + tick(C, F, 2)
         + '<text class="t" x="97" y="18">E</text><text class="t" x="107" y="130">F</text>')
# △ABC の AB、AC の中点 D、E、DE の延長上に DE＝EF
mA, mB, mC = (100, 20), (30, 125), (170, 125)
mD, mE, mF = (65, 72.5), (135, 72.5), (205, 72.5)
f4 = "".join(['<polygon class="l" points="100,20 30,125 170,125"/>',
              '<line class="l" x1="65" y1="72.5" x2="205" y2="72.5"/>',
              '<line class="l" x1="170" y1="125" x2="205" y2="72.5"/>',
              tick(mA, mD), tick(mD, mB), tick(mA, mE, 2), tick(mE, mC, 2),
              tick(mD, mE, 3), tick(mE, mF, 3),
              '<text class="t" x="97" y="14">A</text><text class="t" x="20" y="136">B</text>',
              '<text class="t" x="168" y="137">C</text>',
              '<text class="t" x="55" y="70">D</text><text class="t" x="132" y="68">E</text>',
              '<text class="t" x="207" y="70">F</text>'])
# 台形と対角線
tA, tD, tB, tC = (66, 22), (158, 22), (18, 122), (196, 122)
f5 = "".join(['<polygon class="l" points="66,22 158,22 196,122 18,122"/>',
              '<line class="l" x1="66" y1="22" x2="196" y2="122"/>',
              '<line class="l" x1="158" y1="22" x2="18" y2="122"/>',
              par(tA, tD), par(tB, tC),
              '<circle cx="110.3" cy="56.1" r="2.3" fill="var(--fig)"/>',
              '<text class="t" x="60" y="16">A</text><text class="t" x="160" y="16">D</text>',
              '<text class="t" x="8" y="134">B</text><text class="t" x="199" y="134">C</text>',
              '<text class="t" x="114" y="53">O</text>'])
# 四角形を三角形に（等積変形）
f6 = "".join(['<line class="l" x1="20" y1="120" x2="218" y2="120"/>',
              '<polygon class="l" points="55,40 30,120 120,120 165,70"/>',
              '<g class="ft">'
              '<line class="ftline" x1="55" y1="40" x2="120" y2="120" stroke-dasharray="4 3"/>'
              '<line class="ftline" x1="165" y1="70" x2="205.6" y2="120" stroke-dasharray="4 3"/>'
              '<line class="ftline" x1="55" y1="40" x2="205.6" y2="120"/>'
              '<circle cx="205.6" cy="120" r="2.4" fill="var(--accent)"/>'
              '<text class="t" x="203" y="133" fill="var(--accent)">P</text></g>',
              '<text class="t" x="49" y="34">A</text><text class="t" x="20" y="133">B</text>',
              '<text class="t" x="117" y="133">C</text><text class="t" x="169" y="68">D</text>'])

SHEET = dict(
    title="2節・3節の確かめよう",
    ji="第12時",
    pg="学校図書『数学2』p.173 ほか／2節・3節 確かめよう（全14時間・学び合い）",
    goal="⑯〜㉓ を自分で選んで使える。性質と条件を区別して使える。",
    katari="今日は新しいことをしません。<b>手に入れた13枚から選んで使う</b>日です。"
           "できるところから手をつけてよい。全部できた人は、まだの人のところへ行ってください。"
           "<b>全員が終わるのがゴール</b>です。",
    cards_title="使えるカード　①〜⑩（4章）／⑪〜⑮（1節）／⑯〜㉓（2節・3節）",
    cards_hint="根拠は<b>内容をことばで書いてから（根拠○）</b>。"
               "<b>性質</b>（平行四辺形だから○○）と<b>条件</b>（○○だから平行四辺形）を区別する。",
    footer="中学2年 数学　5章 三角形・四角形（全14時間）　第12時 2節・3節の確かめよう／A3横",
    cols=[
("ことばの確認",
 """    <ol>
      <li>平行四辺形の<b>定義</b>を書きなさい。%s</li>
      <li>平行四辺形の<b>性質</b>を3つ書きなさい。%s</li>
      <li>平行四辺形になるための<b>条件</b>を5つ書きなさい。%s</li>
      <li>正方形の対角線には、どんな性質がありますか。%s</li>
      <li>形がちがっても面積が等しくなるのは、どんなときですか。%s</li>
    </ol>"""
 % (bz(13, "2組の対辺がそれぞれ平行である四角形"),
    bz(24, "⑯ 2組の対辺はそれぞれ等しい／⑰ 2組の対角はそれぞれ等しい／"
           "⑱ 2つの対角線はそれぞれの中点で交わる"),
    bz(34, "❶2組の対辺がそれぞれ平行（定義）／❷2組の対辺がそれぞれ等しい（⑲）／"
           "❸2組の対角がそれぞれ等しい（⑳）／❹対角線がそれぞれの中点で交わる（㉑）／"
           "❺1組の対辺が平行でその長さが等しい（㉒）"),
    bz(22, "長さが等しく、垂直に交わる。それぞれの中点で交わる（平行四辺形の性質⑱も持つ）。"),
    bz(22, "平行な2直線にはさまれ、底辺が共通のとき。高さが等しいから（根拠㉓）。"))),

("判定と計算",
 """    <ol>
      <li>四角形 ABCD が<b>必ず平行四辺形になる</b>のはどれですか。すべて選びなさい。
        （O は対角線の交点）
        %s
        <p class="inst">㋐ AD∥BC、AB＝DC　㋑ AB∥DC、AB＝DC<br>
          ㋒ AO＝CO、BO＝DO　㋓ AO＝BO、CO＝DO</p>
        答 %s
        %s</li>
      <li>%s∠<i>x</i>＝%s°　∠<i>y</i>＝%s°</li>
    </ol>"""
 % (fig("0 0 215 140", f1, "四角形 ABCD", "150px"), z("㋑と㋒", "w"),
    bz(30, "㋐ ×。AD∥BC と AB＝DC は<b>別の組</b>なので等脚台形になりうる。<br>"
           "㋑ ○。1組の対辺が平行でその長さが等しい（根拠㉒）。<br>"
           "㋒ ○。対角線がそれぞれの中点で交わる（根拠㉑）。<br>"
           "㋓ ×。AO＝BO、CO＝DO では中点になるとは限らない。"),
    fig("0 0 215 142", f2, "平行四辺形", "150px"), z("70"), z("110"))),

("証明（平行四辺形）",
 """    <ol>
      <li>□ABCD の辺 AD、BC 上に <b>AE＝CF</b> となる点 E、F をとる。
        <b>BE＝DF</b> を証明しなさい。
        %s%s</li>
      <li>△ABC の辺 AB、AC の中点を D、E とし、DE の延長上に <b>DE＝EF</b> となる点 F をとる。
        %s
        ㋐ <b>四角形 ADCF は平行四辺形である。</b>証明しなさい。%s
        ㋑ <b>DF＝BC</b> を証明しなさい。%s</li>
    </ol>"""
 % (fig("0 0 215 140", f3, "AE＝CF", "150px"),
    bz(32, "△ABE と △CDF において、⑯より AB＝CD、仮定より AE＝CF、"
           "⑰より ∠EAB＝∠FCD。<br>"
           "2組の辺とその間の角がそれぞれ等しいから（<b>根拠②</b>）△ABE≡△CDF。<br>"
           "対応する辺は等しいから BE＝DF　■"),
    fig("0 0 225 145", f4, "AD＝DB、AE＝EC、DE＝EF", "150px"),
    bz(30, "対角線 AC と DF について、E は AC の中点（仮定）、E は DF の中点（DE＝EF）。<br>"
           "2つの対角線がそれぞれの中点で交わるから（<b>根拠㉑</b>）"
           "四角形 ADCF は平行四辺形　■"),
    bz(30, "㋐より AD∥FC、AD＝FC。D は AB の中点だから DB＝AD＝FC、"
           "また DB∥FC。<br>"
           "1組の対辺が平行でその長さが等しいから（<b>根拠㉒</b>）四角形 DBCF は平行四辺形。<br>"
           "よって DF＝BC　■　※ ㉒を2回つづけて使う。"))),

("面積",
 """    <ol>
      <li>AD∥BC の台形 ABCD で、対角線の交点を O とする。
        <b>△ABO＝△DCO</b>（面積が等しい）を説明しなさい。
        %s%s</li>
      <li>四角形 ABCD がある。直線 BC 上に点 P をとって、<b>△ABP の面積を
        四角形 ABCD の面積と等しく</b>したい。P はどこにとればよいですか。
        %s%s</li>
    </ol>
    %s"""
 % (fig("0 0 215 142", f5, "AD∥BC", "150px"),
    bz(28, "AD∥BC だから（根拠㉓）△ABC＝△DBC。<br>"
           "どちらからも共通部分の △OBC をひくと △ABO＝△DCO　■"),
    fig("0 0 225 142", f6, "四角形 ABCD と直線 BC", "150px"),
    bz(32, "対角線 AC をひき、D を通り AC に平行な直線と直線 BC との交点を P とする。<br>"
           "AC∥DP だから（根拠㉓）△ACD＝△ACP。<br>"
           "四角形 ABCD＝△ABC＋△ACD＝△ABC＋△ACP＝△ABP　■"),
    memo("<b>ステップを踏ませない。</b>できるところから。終わった生徒を動かす。<br>"
         "<b>見取り</b>　「判定と計算」1の㋐で×にできるか＝第3時の反例の考え方が残っているか。<br>"
         "「証明」2㋑は㉒を2回つづけて使う。ここまで届いた生徒を全体に紹介する。<br>"
         "「面積」2は第11時④と同じ問題。<b>できるようになったかの確認</b>に使う。<br>"
         "<b>削り順</b>　証明2㋑ → 面積2。死守するのは「ことばの確認」と各列の1問目。"))),
])

if __name__ == "__main__":
    print(build_practice(SHEET, sys.argv[1]), "bytes")
