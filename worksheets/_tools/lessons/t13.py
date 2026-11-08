# -*- coding: utf-8 -*-
"""第13時 5章のまとめの問題（基本・応用）（学校図書『数学2』p.175-176）学び合い"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a3_sheet import build_practice, angle_arc, angle_deg, tick, par, right_angle, z, bz, fig, memo

# 基本2 ∠A＝36°、∠B の二等分線と AC の交点 D
A2, B2, C2, D2 = (100, 16), (65.6, 122), (134.4, 122), (121.3, 81.5)
f1 = "".join(['<polygon class="l" points="100,16 65.6,122 134.4,122"/>',
              '<line class="l" x1="65.6" y1="122" x2="121.3" y2="81.5"/>',
              tick(A2, B2), tick(A2, C2),
              angle_arc(A2, B2, C2, 22),
              '<text class="t" x="100" y="46" text-anchor="middle">36°</text>',
              '<text class="t" x="100" y="10" text-anchor="middle">A</text>',
              '<text class="t" x="55" y="132">B</text><text class="t" x="138" y="132">C</text>',
              '<text class="t" x="124" y="78">D</text>'])
# 基本3 □ABCD、A・C から対角線 BD への垂線
A3, D3, B3, C3 = (50, 24), (190, 24), (20, 118), (160, 118)
E3, F3 = (82.8, 83.3), (127.2, 58.7)
f2 = "".join(['<polygon class="l" points="50,24 190,24 160,118 20,118"/>',
              '<line class="l" x1="20" y1="118" x2="190" y2="24"/>',
              '<line class="l" x1="50" y1="24" x2="82.8" y2="83.3"/>',
              '<line class="l" x1="160" y1="118" x2="127.2" y2="58.7"/>',
              par(A3, D3), par(B3, C3), par(A3, B3, 2), par(D3, C3, 2),
              right_angle(E3, B3, A3, 7), right_angle(F3, D3, C3, 7),
              '<text class="t" x="44" y="18">A</text><text class="t" x="192" y="18">D</text>',
              '<text class="t" x="10" y="130">B</text><text class="t" x="164" y="130">C</text>',
              '<text class="t" x="72" y="92">E</text><text class="t" x="130" y="54">F</text>'])
# 基本4 M は BC の中点、MD⊥AB、ME⊥AC
A4, B4, C4, M4 = (100, 20), (30, 125), (170, 125), (100, 125)
D4, E4 = (51.5, 92.7), (148.5, 92.7)
f3 = "".join(['<polygon class="l" points="100,20 30,125 170,125"/>',
              '<line class="l" x1="100" y1="125" x2="51.5" y2="92.7"/>',
              '<line class="l" x1="100" y1="125" x2="148.5" y2="92.7"/>',
              tick(B4, M4, 2), tick(M4, C4, 2),
              right_angle(D4, A4, M4, 7), right_angle(E4, M4, A4, 7),
              '<g class="ft">%s%s</g>' % (tick(M4, D4, 3, cls="ftline"), tick(M4, E4, 3, cls="ftline")),
              '<text class="t" x="97" y="14">A</text><text class="t" x="20" y="136">B</text>',
              '<text class="t" x="174" y="136">C</text>',
              '<text class="t" x="97" y="137">M</text>',
              '<text class="t" x="40" y="90">D</text><text class="t" x="152" y="90">E</text>'])
# 応用3 二等辺三角形、P から AB、AC に平行
A5, B5, C5, P5 = (100, 16), (30, 126), (170, 126), (110, 126)
Q5, R5 = (140, 78.9), (70, 63.1)
f4 = "".join(['<polygon class="l" points="100,16 30,126 170,126"/>',
              '<line class="l" x1="110" y1="126" x2="140" y2="78.9"/>',
              '<line class="l" x1="110" y1="126" x2="70" y2="63.1"/>',
              tick(A5, B5), tick(A5, C5),
              par(P5, Q5), par(A5, B5), par(P5, R5, 2), par(A5, C5, 2),
              '<text class="t" x="97" y="10">A</text><text class="t" x="20" y="137">B</text>',
              '<text class="t" x="174" y="137">C</text>',
              '<text class="t" x="107" y="138">P</text>',
              '<text class="t" x="144" y="76">Q</text><text class="t" x="58" y="61">R</text>'])

SHEET = dict(
    title="章末の問題（基本・応用）",
    ji="第13時",
    pg="学校図書『数学2』p.175-176／5章のまとめの問題（全14時間・学び合い）",
    goal="5章で手に入れた13枚のカードを、問題に応じて選んで使える。",
    katari="単元のまとめです。<b>どのカードを使うかは書いてありません。</b>"
           "自分で選びます。迷ったら、まず<b>何を示したいのか</b>をはっきりさせること。"
           "全部できた人は、まだの人のところへ行ってください。",
    cards_title="使えるカード　①〜⑩（4章）／⑪〜㉓（5章・13枚）",
    cards_hint="根拠は<b>内容をことばで書いてから（根拠○）</b>。"
               "示したいものが「長さ」なのか「角」なのか「平行四辺形であること」なのかで、"
               "選ぶカードが変わる。",
    footer="中学2年 数学　5章 三角形・四角形（全14時間）　第13時 章末（基本・応用）／A3横",
    cols=[
("ことばの確認",
 """    <p class="inst">教科書 p.175 まとめの問題【基本】1</p>
    <ol>
      <li>二等辺三角形の %s の二等分線は、底辺を垂直に2等分する。</li>
      <li>2つの直角三角形は、斜辺と %s、または斜辺と %s
        がそれぞれ等しければ合同である。</li>
      <li>平行四辺形の2つの対角線は、それぞれの %s で交わる。</li>
      <li>長方形は、%s と定義される。</li>
    </ol>
    <p class="inst" style="margin-top:8px">書けなかったものを、カードで確かめて写す。</p>
    %s"""
 % (z("頂角", "w"), z("1つの鋭角", "w"), z("他の1辺", "w"), z("中点", "w"),
    z("4つの角が等しい四角形", "ww"),
    bz(44, "ここは3分で終わらせる。書けなかったカードの番号だけ控えさせ、先へ進ませる。<br>"
           "この列で止まっている生徒がいたら、まず別紙のカードを机に並べさせる。"))),

("角と図形の判断",
 """    <p class="inst">教科書 p.175【基本】2・4</p>
    <ol>
      <li>頂角 ∠A＝36° の二等辺三角形 ABC で、∠B の二等分線と辺 AC の交点を D とする。
        %s
        ㋐ ∠BDC の大きさ %s°<br>
        ㋑ △BCD はどんな三角形ですか。<b>理由も書きなさい。</b>%s</li>
      <li>△ABC の辺 BC の中点 M から、辺 AB、AC へ垂線 MD、ME を引く。
        <b>MD＝ME ならば、△ABC はどんな三角形ですか。</b>証明しなさい。
        %s%s</li>
    </ol>"""
 % (fig("0 0 200 142", f1, "AB＝AC、BD は ∠B の二等分線", "150px"), z("72"),
    bz(30, "∠B＝∠C＝(180−36)÷2＝72°。∠DBC＝36°。<br>"
           "∠BDC＝180−36−72＝72°。よって ∠BDC＝∠BCD＝72°。<br>"
           "2つの角が等しいから（<b>根拠⑬</b>）△BCD は DB＝DC の二等辺三角形。"),
    fig("0 0 200 145", f3, "BM＝CM、MD⊥AB、ME⊥AC", "150px"),
    bz(34, "△BDM と △CEM において　∠BDM＝∠CEM＝90°　……(a)<br>"
           "仮定より BM＝CM（斜辺）　……(b)／MD＝ME（他の1辺）　……(c)<br>"
           "(a)(b)(c)より、斜辺と他の1辺がそれぞれ等しいから（<b>根拠⑮</b>）△BDM≡△CEM<br>"
           "対応する角は等しいから ∠B＝∠C。<br>"
           "2つの角が等しいから（<b>根拠⑬</b>）△ABC は AB＝AC の<b>二等辺三角形</b>　■"))),

("証明（平行四辺形）",
 """    <p class="inst">教科書 p.175【基本】3</p>
    <p>□ABCD の頂点 A、C から対角線 BD に垂線 AE、CF を引く。</p>
    %s
    <ol>
      <li><b>△ABE≡△CDF</b> を証明しなさい。%s</li>
      <li><b>四角形 AECF は平行四辺形である。</b>証明しなさい。%s</li>
    </ol>"""
 % (fig("0 0 215 140", f2, "AE⊥BD、CF⊥BD"),
    bz(40, "△ABE と △CDF において　∠AEB＝∠CFD＝90°　……(a)<br>"
           "⑯より AB＝CD（斜辺）　……(b)<br>"
           "AB∥DC で錯角は等しいから　∠ABE＝∠CDF　……(c)<br>"
           "(a)(b)(c)より、斜辺と1つの鋭角がそれぞれ等しいから（<b>根拠⑭</b>）△ABE≡△CDF　■"),
    bz(38, "(1) より　AE＝CF　……(a)<br>"
           "AE⊥BD、CF⊥BD だから、同じ直線に垂直な2直線は平行なので　AE∥CF　……(b)<br>"
           "(a)(b)より、1組の対辺が平行でその長さが等しいから（<b>根拠㉒</b>）"
           "四角形 AECF は平行四辺形　■"))),

("応用",
 """    <p class="inst">教科書 p.176【応用】3</p>
    <p>二等辺三角形 ABC の底辺 BC 上の点 P から、辺 AB、AC に平行な直線を引き、
      辺 AC、AB との交点をそれぞれ Q、R とする。</p>
    <p><b>PQ＋PR＝AB</b> を証明しなさい。</p>
    %s
    %s
    %s"""
 % (fig("0 0 200 148", f4, "PQ∥AB、PR∥AC"),
    bz(56, "四角形 ARPQ は、2組の対辺がそれぞれ平行だから平行四辺形（定義）。<br>"
           "よって　PQ＝AR　……(a)<br>"
           "PR∥AC で錯角は等しいから ∠RPB＝∠ACB。"
           "⑪より ∠ABC＝∠ACB だから ∠RPB＝∠RBP。<br>"
           "2つの角が等しいから（<b>根拠⑬</b>）△RBP は RB＝RP の二等辺三角形。"
           "よって　PR＝RB　……(b)<br>"
           "(a)(b)より　PQ＋PR＝AR＋RB＝AB　■<br>"
           "※ <b>平行四辺形（2節）と二等辺三角形（1節）を1つの図で使う</b>。"
           "5章全体がつながる問題。"),
    memo("<b>ステップを踏ませない。</b>できる列から手をつけてよい。<br>"
         "「ことばの確認」は3分で切り上げさせる。ここで時間を使わせない。<br>"
         "<b>見取り</b>　「証明（平行四辺形）」2で ㉒ が出るか＝第8時がきいているか。<br>"
         "「応用」は1節と2節を1つの図で使う。届いた生徒を全体に紹介する。<br>"
         "<b>削り順</b>　応用 → 角と図形の判断2。死守するのは「証明（平行四辺形）」。"))),
])

if __name__ == "__main__":
    print(build_practice(SHEET, sys.argv[1]), "bytes")
