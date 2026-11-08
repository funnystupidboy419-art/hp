# -*- coding: utf-8 -*-
"""第14時 活用・深めよう・単元を貫く課題（学校図書『数学2』p.177）学び合い"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a3_sheet import build, angle_arc, angle_deg, tick, par, z, bz, fig, memo

# 図1 活用1: 2つの二等分線の交点 D、D を通り BC に平行な直線
A1, B1, C1 = (100, 14), (30, 130), (180, 130)
D1, E1, F1 = (102.3, 89.2), (54.6, 89.2), (151.9, 89.2)
f1 = "".join(['<polygon class="l" points="100,14 30,130 180,130"/>',
              '<line class="d" x1="14" y1="89.2" x2="198" y2="89.2"/>',
              '<line class="l" x1="30" y1="130" x2="102.3" y2="89.2"/>',
              '<line class="l" x1="180" y1="130" x2="102.3" y2="89.2"/>',
              par(E1, F1), par(B1, C1),
              angle_arc(B1, C1, D1, 16), angle_arc(B1, D1, A1, 16),
              angle_arc(C1, D1, B1, 16), angle_arc(C1, A1, D1, 16),
              '<circle cx="102.3" cy="89.2" r="2.3" fill="var(--fig)"/>',
              '<text class="t" x="97" y="9">A</text><text class="t" x="20" y="141">B</text>',
              '<text class="t" x="184" y="141">C</text>',
              '<text class="t" x="104" y="86">D</text>',
              '<text class="t" x="46" y="86">E</text><text class="t" x="155" y="86">F</text>',
              '<text class="t" x="200" y="93">ℓ</text>'])
# 図2 深めよう: 線分 AB 上の点 C、正三角形 ACP と CBQ
A2, B2, C2 = (30, 120), (190, 120), (100, 120)
P2, Q2 = (65, 59.4), (145, 42.1)
assert abs(math.dist(A2, Q2) - math.dist(P2, B2)) < 0.5
f2 = "".join(['<line class="l" x1="20" y1="120" x2="200" y2="120"/>',
              '<polygon class="l" points="30,120 100,120 65,59.4"/>',
              '<polygon class="l" points="100,120 190,120 145,42.1"/>',
              '<line class="d" x1="30" y1="120" x2="145" y2="42.1"/>',
              '<line class="d" x1="65" y1="59.4" x2="190" y2="120"/>',
              '<g class="ft">%s%s</g>' % (tick(A2, Q2, 2, cls="ftline"), tick(P2, B2, 2, cls="ftline")),
              '<text class="t" x="22" y="132">A</text><text class="t" x="97" y="132">C</text>',
              '<text class="t" x="188" y="132">B</text>',
              '<text class="t" x="58" y="56">P</text><text class="t" x="148" y="40">Q</text>'])

SHEET = dict(
    title="条件を変えても成り立つか",
    ji="第14時",
    pg="学校図書『数学2』p.177／活用・深めよう（全14時間・学び合い）",
    goal="条件を変えたときに何が残り、何が変わるかを調べ、単元の課題に自分の答えを出せる。",
    katari="14時間かけて13枚のカードを集めました。最後に、単元の最初に出した問いに答えます。<br>"
           "<b>「かならずそうなる」と言えるのは、どんなときか。</b>"
           "今日は、<b>条件を変えてみて</b>そのことを考えます。",
    cards_title="使えるカード　①〜⑩（4章）／⑪〜㉓（5章・13枚）",
    cards_hint="今日は新しいカードを作らない。<b>持っているカードが、条件を変えても使えるか</b>を試す。",
    footer="中学2年 数学　5章 三角形・四角形（全14時間）　第14時 活用・深めよう／A3横",
    blocks=[
"""    <p class="inst">13枚のカードをならべて、隣の人と見くらべる。</p>
    <ol>
      <li>いちばん多く使ったカードの番号 %s</li>
      <li>一度も使わなかったカードの番号 %s</li>
      <li>そのカードは<b>いらない</b>のだろうか。%s</li>
    </ol>
    <div class="spacer"></div>
    <p class="inst">使わなかったカードにも、使う場面がある。</p>"""
% (z("", "w"), z("", "w"),
   bz(24, "いらないわけではない。問題の形が変われば出番が来る。<br>"
          "㉒がよく出たのは、平行四辺形を示す問題が多かったから。<br>"
          "⑫や⑮は、垂直や直角が出てくる問題で使う。")),

"""    <p>単元の最初に出した問い。</p>
    <p class="inst" style="font-size:13px; border-left:3px solid var(--accent); padding-left:9px">
      <b>「かならずそうなる」と言えるのは、どんなときか。</b></p>
    <p class="inst" style="margin-top:8px">この単元で何度も出てきた。<br>
      ・いくつか調べただけでは「<b>確かめた</b>」にすぎない（第1時・第2時）<br>
      ・逆はいつでも正しいとは限らない（第3時）<br>
      ・反例が1つあれば「正しくない」と決まる（第3時）<br>
      ・条件を1つ外すと成り立たなくなる（第3時・第8時）</p>
    <div class="spacer"></div>
    <p class="inst" style="border-top:1px dotted var(--rule); padding-top:5px">
      <b>今日の問い</b>　条件を変えたとき、<b>何が残って、何が変わる</b>のか。</p>""",

"""    <p class="inst">教科書 p.177【活用】1</p>
    <p>△ABC で ∠ABC の二等分線と ∠ACB の二等分線の交点を D とする。
      D を通り BC に平行な直線 ℓ をひき、辺 AB、AC との交点を E、F とする。</p>
    %s
    <ol>
      <li>EB＝ED を示すとき、仮定として使うのはどれですか。すべて選びなさい。<br>
        <span class="inst">㋐ BD は ∠ABC の二等分線である　㋑ CD は ∠ACB の二等分線である<br>
        ㋒ 直線 ℓ は点 D を通り、辺 BC に平行である　㋓ EB＝ED である</span><br>
        答 %s</li>
      <li><b>FC＝FD</b> を証明しなさい。%s</li>
      <li>△AEF のまわりの長さと等しいものはどれですか。
        <span class="inst">㋐ AB＋AC　㋑ AB＋BC　㋒ BC＋CA　㋓ AB＋BC＋CA</span>
        答 %s　理由 %s</li>
    </ol>"""
% (fig("0 0 210 150", f1, "図1　ℓ∥BC。BD、CD は角の二等分線", "140px"),
   z("㋐と㋒", "w"),
   bz(32, "CD は ∠ACB の二等分線だから　∠FCD＝∠DCB　……(a)<br>"
          "ℓ∥BC で錯角は等しいから　∠FDC＝∠DCB　……(b)<br>"
          "(a)(b)より　∠FCD＝∠FDC<br>"
          "2つの角が等しいから（<b>根拠⑬</b>）△FCD は FC＝FD の二等辺三角形　■"),
   z("㋐", "w"),
   bz(26, "EB＝ED、FC＝FD だから<br>"
          "AE＋EF＋FA＝AE＋(ED＋DF)＋FA＝AE＋EB＋FC＋FA＝AB＋AC")),

"""    <p class="inst">教科書 p.177 深めよう／第5時の問題（線分 AB 上に点 C、AC と CB を1辺とする
      正三角形 ACP、CBQ をつくると AQ＝PB）</p>
    %s
    <ol class="circ">
      <li><b>正三角形を正方形に変えても</b>、同じことが成り立ちますか。
        成り立つなら、証明のどこが変わるかを書きなさい。%s</li>
      <li><b>点 C を線分 AB の外</b>にとっても成り立ちますか。%s</li>
      <li><b>単元の課題に、いまのあなたの答えを書きなさい。</b><br>
        <span class="inst">「かならずそうなる」と言えるのは、どんなときか。</span>%s</li>
    </ol>
    %s"""
% (fig("0 0 210 142", f2, "図2　AQ＝PB（第5時）", "140px"),
   bz(26, "<b>成り立つ。</b>もとの証明は △QAC と △BPC で AC＝PC、QC＝BC、"
          "∠ACQ＝∠PCB（どちらも 60°＋∠QCP）から（根拠②）合同、だった。<br>"
          "正方形にすると 60° が 90° に変わるだけで、<b>∠ACQ＝∠PCB は同じ理由で成り立つ</b>。"
          "他は変わらない。"),
   bz(22, "<b>成り立つ。</b>∠ACQ と ∠PCB の作られ方は同じ。"
          "角のたし算がひき算に変わる場合があるが、等しいことは変わらない。"),
   bz(34, "例:「いくつか調べただけでは言えない。どの場合でも通る筋道を示したときに言える」<br>"
          "例:「反例が1つもないことを示せたとき。逆に反例が1つ見つかれば言えない」<br>"
          "例:「使った条件がどれも必要で、1つ外すと成り立たなくなるとき」<br>"
          "※ 正解を1つに決めない。<b>14時間でその子に残ったもの</b>が出ていればよい。"),
   memo("<b>最後の1時間。</b>③は教科書の活用問題。④が単元の締め。<br>"
        "④①②は「<b>何が変わって、何が変わらないか</b>」を言わせるのが目的。"
        "全部証明し直させない。<b>証明のどこが変わるか</b>だけでよい。<br>"
        "④③は評価の対象にしない。第1時のルーブリックを見ながら、"
        "自分がどこまで来たかを確かめさせる。<br>"
        "<b>削り順</b>　③3 → ④②。死守するのは ③2 と ④③。<br>"
        "④③にたどりつかない時間配分にはしない。<b>単元を閉じる問いなので必ず書かせる。</b>")),
])

if __name__ == "__main__":
    print(build(SHEET, sys.argv[1]), "bytes")
