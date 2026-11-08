# -*- coding: utf-8 -*-
"""第9時 平行四辺形の練習（学校図書『数学2』p.165-169）学び合い
   ステップ式にしない。問題を多く、余白は書ける高さで。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a3_sheet import build_practice, angle_arc, angle_deg, tick, par, z, bz, fig, memo

A, D, B, C = (50, 24), (190, 24), (20, 118), (160, 118)
lab = ('<text class="t" x="44" y="18">A</text><text class="t" x="192" y="18">D</text>'
       '<text class="t" x="10" y="130">B</text><text class="t" x="164" y="130">C</text>')
pg = ('<polygon class="l" points="50,24 190,24 160,118 20,118"/>'
      + par(A, D) + par(B, C) + par(A, B, 2) + par(D, C, 2) + lab)

# 図1 AE＝CF（E は AD 上、F は BC 上）
E, F = (100, 24), (110, 118)
f1 = (pg + '<line class="l" x1="100" y1="24" x2="20" y2="118"/>'
         + '<line class="l" x1="110" y1="118" x2="190" y2="24"/>'
         + tick(A, E, 2) + tick(C, F, 2)
         + '<text class="t" x="97" y="18">E</text><text class="t" x="107" y="130">F</text>')
# 図2 AE＝CF から 四角形 AECF
f2 = (pg + '<line class="l" x1="100" y1="24" x2="160" y2="118"/>'
         + '<line class="l" x1="110" y1="118" x2="50" y2="24"/>'
         + tick(A, E, 2) + tick(C, F, 2)
         + '<text class="t" x="97" y="18">E</text><text class="t" x="107" y="130">F</text>')
# 図3 ∠A の二等分線と BC の交点 E
jE = (118.7, 118)
f3 = (pg + '<line class="l" x1="50" y1="24" x2="118.7" y2="118"/>'
         + angle_arc(A, D, jE, 20) + angle_arc(A, jE, B, 20)
         + '<text class="t" x="116" y="130">E</text>')
# 図4 O を通る直線と AD、BC の交点 P、Q
O, P, Q = (105, 71), (140, 24), (70, 118)
f4 = (pg + '<line class="d" x1="50" y1="24" x2="160" y2="118"/>'
         + '<line class="d" x1="190" y1="24" x2="20" y2="118"/>'
         + '<line class="l" x1="140" y1="24" x2="70" y2="118"/>'
         + '<circle cx="105" cy="71" r="2.3" fill="var(--fig)"/>'
         + '<text class="t" x="109" y="68">O</text>'
         + '<text class="t" x="138" y="18">P</text><text class="t" x="62" y="130">Q</text>')
# 角と長さ
gA, gD, gB, gC = (50, 24), (190, 24), (15.8, 118), (155.8, 118)
assert abs(angle_deg(gA, gB, gD) - 110) < 0.3
f5 = "".join(['<polygon class="l" points="50,24 190,24 155.8,118 15.8,118"/>',
              par(gA, gD), par(gB, gC), par(gA, gB, 2), par(gD, gC, 2),
              angle_arc(gA, gB, gD, 20),
              '<text class="t" x="62" y="44">110°</text>',
              '<text class="t" x="24" y="108"><tspan font-style="italic">x</tspan></text>',
              '<text class="t" x="136" y="108"><tspan font-style="italic">y</tspan></text>',
              '<text class="t" x="44" y="18">A</text><text class="t" x="192" y="18">D</text>',
              '<text class="t" x="6" y="130">B</text><text class="t" x="160" y="130">C</text>'])
f6 = (pg + '<line class="d" x1="50" y1="24" x2="160" y2="118"/>'
         + '<line class="d" x1="190" y1="24" x2="20" y2="118"/>'
         + '<circle cx="105" cy="71" r="2.3" fill="var(--fig)"/>'
         + '<text class="t" x="109" y="68">O</text>'
         + '<text class="t" x="118" y="20">6cm</text>'
         + '<text class="t" x="66" y="48">5cm</text>'
         + '<text class="t" x="86" y="132"><tspan font-style="italic">x</tspan> cm</text>'
         + '<text class="t" x="140" y="96"><tspan font-style="italic">y</tspan> cm</text>')

SHEET = dict(
    title="平行四辺形の練習",
    ji="第9時",
    pg="学校図書『数学2』p.165-169／2節 四角形（全14時間・学び合い）",
    goal="平行四辺形の性質（⑯⑰⑱）と、なるための条件（⑲〜㉒）を、自分で選んで使える。",
    katari="今日は新しいことをしません。<b>手に入れた7枚を、自分で選んで使う</b>日です。"
           "できるところから手をつけてよい。全部できた人は、まだの人のところへ行ってください。"
           "<b>全員が終わるのがゴール</b>です。",
    cards_title="使えるカード　①②③（4章）／⑪〜⑮（1節）／⑯〜㉒（2節）",
    cards_hint="証明の根拠は<b>内容をことばで書いてから（根拠○）</b>。"
               "<b>性質</b>（平行四辺形だから○○）と<b>条件</b>（○○だから平行四辺形）の"
               "どちらを使うのかを、毎回はっきりさせる。",
    footer="中学2年 数学　5章 三角形・四角形（全14時間）　第9時 平行四辺形の練習／A3横",
    cols=[
("ことばの確認",
 """    <ol>
      <li>平行四辺形の<b>定義</b>を書きなさい。%s</li>
      <li>平行四辺形の<b>性質</b>を3つ書きなさい。%s</li>
      <li>四角形が平行四辺形になるための<b>条件</b>を5つ書きなさい。%s</li>
      <li>「平行四辺形ならば、対角線はそれぞれの中点で交わる」の<b>逆</b>を書きなさい。
        また、その逆は正しいですか。%s</li>
    </ol>"""
 % (bz(14, "2組の対辺がそれぞれ平行である四角形"),
    bz(26, "⑯ 2組の対辺はそれぞれ等しい／⑰ 2組の対角はそれぞれ等しい／"
           "⑱ 2つの対角線はそれぞれの中点で交わる"),
    bz(38, "❶ 2組の対辺がそれぞれ平行（定義）／❷ 2組の対辺がそれぞれ等しい（⑲）／"
           "❸ 2組の対角がそれぞれ等しい（⑳）／❹ 2つの対角線がそれぞれの中点で交わる（㉑）／"
           "❺ 1組の対辺が平行でその長さが等しい（㉒）"),
    bz(30, "逆:「2つの対角線がそれぞれの中点で交わる四角形は、平行四辺形である」<br>"
           "<b>正しい</b>（根拠㉑）。性質の逆が条件になっている。<br>"
           "※ ⑯⑰⑱の逆が ⑲⑳㉑。逆がどれも正しいのは、この単元ではめずらしい。"))),

("角と長さを求める",
 """    <ol>
      <li>%s∠<i>x</i>＝%s°　∠<i>y</i>＝%s°</li>
      <li>%s<i>x</i>＝%s　<i>y</i>＝%s
        <span class="inst">使った根拠を番号とことばで言えるようにする。</span></li>
      <li>平行四辺形のとなり合う2つの角の和は何度になりますか。
        また、その理由を書きなさい。%s</li>
    </ol>"""
 % (fig("0 0 215 142", f5, "図1", "150px"), z("70"), z("110"),
    fig("0 0 215 142", f6, "図2　O は対角線の交点", "150px"), z("6"), z("5"),
    bz(26, "180°。AD∥BC だから、∠A と ∠B は平行線の<b>同側内角</b>で、和は180°。<br>"
           "（⑰を使って ∠A＋∠B＋∠C＋∠D＝360° から出してもよい。）"))),

("証明（性質を使う）",
 """    <ol>
      <li>□ABCD の辺 AD、BC 上に <b>AE＝CF</b> となる点 E、F をとる。
        <b>EB＝FD</b> を証明しなさい。
        %s%s</li>
      <li>□ABCD で、∠A の二等分線と辺 BC との交点を E とする。
        <b>BE＝BA</b> を証明しなさい。
        %s%s</li>
    </ol>"""
 % (fig("0 0 215 140", f1, "図3　AE＝CF", "150px"),
    bz(40, "△ABE と △CDF において<br>"
           "⑯より　AB＝CD　……(a)<br>"
           "仮定より　AE＝CF　……(b)<br>"
           "⑰より　∠EAB＝∠FCD　……(c)<br>"
           "(a)(b)(c)より、2組の辺とその間の角がそれぞれ等しいから（<b>根拠②</b>）　△ABE≡△CDF<br>"
           "対応する辺は等しいから　EB＝FD　■"),
    fig("0 0 215 140", f3, "図4　AE は ∠A の二等分線", "150px"),
    bz(36, "AD∥BC で錯角は等しいから　∠DAE＝∠AEB　……(a)<br>"
           "AE は ∠A の二等分線だから　∠DAE＝∠BAE　……(b)<br>"
           "(a)(b)より　∠BAE＝∠AEB<br>"
           "2つの角が等しい三角形は二等辺三角形だから（<b>根拠⑬</b>）　△ABE は BA＝BE の二等辺三角形<br>"
           "よって BE＝BA　■　※ 1節のカードがここで効く。"))),

("証明（条件を使う）",
 """    <ol>
      <li>□ABCD の辺 AD、BC 上に <b>AE＝CF</b> となる点 E、F をとる。
        <b>四角形 AECF は平行四辺形である。</b>証明しなさい。
        %s%s</li>
      <li>□ABCD の対角線の交点 O を通る直線が、辺 AD、BC と交わる点を P、Q とする。
        <b>四角形 APCQ は平行四辺形である。</b>証明しなさい。
        %s%s</li>
    </ol>
    %s"""
 % (fig("0 0 215 140", f2, "図5　AE＝CF", "150px"),
    bz(34, "AD∥BC だから、その一部である　AE∥FC　……(a)<br>"
           "仮定より　AE＝CF　……(b)<br>"
           "(a)(b)より、1組の対辺が平行でその長さが等しいから（<b>根拠㉒</b>）"
           "四角形 AECF は平行四辺形　■<br>"
           "※ 左の「証明（性質を使う）1」と同じ図。<b>示したいものがちがうと、使う根拠も変わる。</b>"),
    fig("0 0 215 140", f4, "図6　O は対角線の交点", "150px"),
    bz(38, "△AOP と △COQ において、⑱より AO＝CO、対頂角は等しく、AD∥BC の錯角も等しいから"
           "（根拠③）△AOP≡△COQ。よって PO＝QO。<br>"
           "対角線 AC と PQ について、AO＝CO、PO＝QO だから、"
           "2つの対角線がそれぞれの中点で交わる（<b>根拠㉑</b>）。<br>"
           "よって四角形 APCQ は平行四辺形　■"),
    memo("<b>ステップを踏ませない。</b>できるところから手をつけてよい。"
         "終わった生徒を、まだの生徒のところへ動かす。<b>全員が終わるのがゴール。</b><br>"
         "<b>見取りの要</b>　「証明（性質を使う）1」と「証明（条件を使う）1」は<b>同じ図</b>。"
         "示したいものがちがうと使う根拠が変わる、に気づけているかを見る。<br>"
         "つまずき: 角・長さで止まる＝⑯⑰が入っていない／"
         "「条件を使う」で止まる＝性質と条件の区別がついていない。<br>"
         "<b>削り順</b>　「条件を使う」2 →「角と長さ」3。死守するのは各列の1問目。"))),
])

if __name__ == "__main__":
    print(build_practice(SHEET, sys.argv[1]), "bytes")
