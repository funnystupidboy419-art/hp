# -*- coding: utf-8 -*-
"""第3時 逆と反例（学校図書『数学2』p.153-154）教師主導
   ④で第1時のふせんの問題を回収する（教科書 p.154 問6）。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a3_sheet import build, angle_arc, angle_deg, tick, grid, z, rz, bz, fig, memo

A, B, C, D = (100, 20), (40, 122), (160, 122), (100, 122)
f1 = "".join([
    '<polygon class="l" points="100,20 40,122 160,122"/>',
    angle_arc(B, C, A, 20), angle_arc(C, A, B, 20),
    '<text class="t" x="30" y="132">B</text><text class="t" x="164" y="132">C</text>',
    '<text class="t" x="100" y="14" text-anchor="middle">A</text>',
])
f2 = "".join([
    '<polygon class="l" points="100,20 40,122 160,122"/>',
    '<line class="l" x1="100" y1="20" x2="100" y2="122"/>',
    angle_arc(B, C, A, 20), angle_arc(C, A, B, 20),
    angle_arc(A, B, D, 22), angle_arc(A, B, D, 26),
    angle_arc(A, D, C, 22), angle_arc(A, D, C, 26),
    '<g class="ft">%s%s</g>' % (tick(A, B, cls="ftline"), tick(A, C, cls="ftline")),
    '<text class="t" x="30" y="132">B</text><text class="t" x="164" y="132">C</text>',
    '<text class="t" x="100" y="14" text-anchor="middle">A</text>',
    '<text class="t" x="100" y="136" text-anchor="middle">D</text>',
])
# 第1時と同じふせんの図（回収）
tA, tB, tC = (68.6, 38), (40, 112), (150, 112)
assert abs(math.hypot(tA[0]-tC[0], tA[1]-tC[1]) - math.hypot(tB[0]-tC[0], tB[1]-tC[1])) < 0.2
assert abs(angle_deg(tA, tB, tC) - angle_deg(tB, tA, tC)) < 0.1
f3 = "".join([
    '<line class="d" x1="8" y1="38" x2="205" y2="38"/>',
    '<line class="d" x1="8" y1="112" x2="205" y2="112"/>',
    '<polygon class="l" points="68.6,38 40,112 150,112" fill="var(--band)"/>',
    '<g class="ft">%s%s%s%s</g>' % (angle_arc(tA, tB, tC, 18, "ftline"), angle_arc(tB, tA, tC, 18, "ftline"),
                                    tick(tC, tA, cls="ftline"), tick(tC, tB, cls="ftline")),
    '<text class="t" x="12" y="34">ℓ</text><text class="t" x="12" y="124">m</text>',
    '<text class="t" x="66" y="32">A</text>',
    '<text class="t" x="31" y="124">B</text><text class="t" x="154" y="124">C</text>',
    '<text class="t" x="52" y="78">折り目</text>',
    '<text class="t" x="118" y="70">折り返した辺</text>',
])

SHEET = dict(
    title="逆はいつでも正しいか",
    ji="第3時",
    pg="学校図書『数学2』p.153-154／1節 三角形（全17時間・この時間は先生と進む）",
    goal="あることがらの逆をつくり、正しいかどうかを証明か反例で決められる。",
    katari="⑪は「二等辺三角形ならば、2つの角が等しい」。<b>ひっくり返したら</b>どうでしょう。"
           "「2つの角が等しいならば、二等辺三角形」。似ていますが<b>別のことがら</b>です。"
           "別のことがらなら、もう一度たしかめないといけません。",
    cards_title="今日手に入れるカードは ⑬ の1枚",
    cards_hint="①②③と⑪⑫は使ってよい。⑬は、③(1) で証明してから使えるようになる。",
    cards=[("①②③", "三角形の合同条件（4章）"),
           ("⑪", "二等辺三角形の2つの底角は等しい"),
           ("⑫", "二等辺三角形の頂角の二等分線は、底辺を垂直に2等分する"),
           ("⑬", "今日 ③(1) で手に入れる")],
    footer="中学2年 数学　5章 三角形・四角形（全17時間）　第3時 逆と反例／A3横",
    blocks=[
"""    <p class="inst">カード⑪⑫を、隣の人に1つずつ言う。</p>
    <ol>
      <li>言えなかった番号 %s</li>
      <li>⑪を「〜ならば、〜である」の形に書きかえる
        %s</li>
    </ol>
    <div class="spacer"></div>
    <p class="inst">「〜ならば」の前が<b>仮定</b>、後ろが<b>結論</b>。</p>"""
% (z("", "w"),
   bz(18, "△ABC で AB＝AC ならば、∠B＝∠C である。")),

"""    <p>ことがらの<b>仮定と結論を入れかえた</b>ものを、そのことがらの<b>逆</b>という。</p>
    <p class="inst">⑪の　仮定 %s　／　結論 %s</p>
    <p class="inst">⑪の逆 → %s</p>
    %s
    <p class="inst">図1は ∠B＝∠C <b>だけ</b>がわかっている三角形。
      AB＝AC といえるか、見た目で決めずに確かめる。</p>
    <div class="spacer"></div>
    <p class="inst" style="border-top:1px dotted var(--rule); padding-top:5px">
      <b>今日の問い</b>　逆は、いつでも正しいといえるか。</p>"""
% (z("AB＝AC", "w"), z("∠B＝∠C", "w"), z("∠B＝∠C ならば AB＝AC", "ww"),
   fig("0 0 200 142", f1, "図1　∠B＝∠C だけがわかっている")),

"""    <ol>
      <li><b>∠B＝∠C ならば AB＝AC を証明する。</b>（図2）
        %s
        <span class="inst">使う合同条件</span>%s
        %s</li>
      <li>次の3つの<b>逆をつくり</b>、正しいかどうか調べる。
        <span class="inst">正しくないものは<b>反例を1つ</b>あげる（1つで足りる）。</span>
        <p class="inst" style="margin-top:4px">ア　△ABC≡△DEF ならば、∠A＝∠D である<br>
          イ　a＝b ならば、a<sup>2</sup>＝b<sup>2</sup> である<br>
          ウ　正三角形ならば、二等辺三角形である</p>
        %s
        <p style="margin-top:5px">正しい逆はいくつありましたか %s</p></li>
    </ol>"""
% (fig("0 0 200 150", f2, "図2　∠A の二等分線と辺BC との交点を D とする"),
   z("③"),
   bz(42, "△ABD と △ACD において<br>"
          "AD は ∠A の二等分線だから　∠BAD＝∠CAD　……(a)<br>"
          "仮定より　∠B＝∠C　……(b)<br>"
          "(a)(b)と三角形の内角の和から　∠ADB＝∠ADC　……(c)<br>"
          "AD は共通　……(d)<br>"
          "(a)(c)(d)より、<b>カード③</b>（1組の辺とその両端の角）から　△ABD≡△ACD<br>"
          "対応する辺は等しいから　AB＝AC　■　→ <b>カード⑬</b>"),
   bz(38, "アの逆「∠A＝∠D ならば △ABC≡△DEF」…… <b>正しくない</b>。"
          "反例: 1つの角だけ等しく大きさのちがう2つの三角形（大小の三角定規）。<br>"
          "イの逆「a<sup>2</sup>＝b<sup>2</sup> ならば a＝b」…… <b>正しくない</b>。反例: a＝2、b＝−2。<br>"
          "ウの逆「二等辺三角形ならば、正三角形である」…… <b>正しくない</b>。反例: 3辺が 5、5、8 の三角形。<br>"
          "→ 正しい逆は<b>0個</b>。もとが正しくても、逆が正しいとは限らない。"),
   z("0")),

"""    <p><b>第1時のふせんを思い出す。</b>重なった部分は二等辺三角形になりそうでした。<br>
      <b>そうなることを証明しなさい。</b></p>
    %s
    <p class="inst">折り目は AB。辺 AC は、折り返す前は <b>ℓ の上</b>にあった。</p>
    %s
    %s"""
% (fig("0 0 215 132", f3, "ℓ∥m。AB が折り目、AC が折り返した辺"),
   bz(46, "折り返す前、辺 AC があった位置を AE とする（E は ℓ 上）。<br>"
          "折り返しただけだから　∠BAC＝∠BAE　……(a)<br>"
          "ℓ∥m で<b>錯角</b>は等しいから　∠BAE＝∠ABC　……(b)<br>"
          "(a)(b)より　∠BAC＝∠ABC<br>"
          "2つの角が等しいから、<b>カード⑬</b>より △ABC は二等辺三角形（CA＝CB）　■<br>"
          "※ 教科書 p.154 問6。今日つくった⑬が、第1時の宿題の答えになる。"),
   memo("<b>この時間で教師主導はおわり。第4時からは学び合い。</b><br>"
        "<b>介入点（5分）</b>　③(2) に入って10分ほどで全体を止め、"
        "「反例は1つ見つければ終わり。たくさん探さなくてよい」を言う。<br>"
        "④が第1時の回収。<b>ここまで到達させたい。</b>錯角（4章）と⑬（今日）の2つがそろって"
        "はじめて解ける問題で、カードが増える意味がいちばん出る。<br>"
        "<b>削り順</b>　③(2) のウ → ③(1) の清書。死守するのは ③(1) と ④。")),
])

if __name__ == "__main__":
    print(build(SHEET, sys.argv[1]), "bytes")
