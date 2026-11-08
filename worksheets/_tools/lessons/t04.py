# -*- coding: utf-8 -*-
"""第4時 2つの角が等しい三角形（逆と反例）（学校図書『数学2』p.153-154）"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a3_sheet import build, angle_arc, angle_deg, tick, grid, z, rz, fig

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

SHEET = dict(
    title="逆はいつでも正しいか",
    ji="第4時",
    pg="学校図書『数学2』p.153-154／1節 三角形（全18時間）",
    goal="あることがらの逆をつくり、それが正しいかどうかを証明か反例で決められる。",
    katari="⑪は「二等辺三角形ならば、2つの角が等しい」です。では<b>ひっくり返したら</b>どうでしょう。"
           "「2つの角が等しいならば、二等辺三角形」。似ていますが、<b>別のことがら</b>です。"
           "別のことがらなら、もう一度たしかめないといけません。",
    cards_title="根拠カード — 今日の新しいカードは ⑬ の1枚",
    cards_hint="①②③⑪⑫は見てよい。⑬は、今日 ③(1) で証明してから使えるようになる。",
    cards=[("①", "3組の辺がそれぞれ等しい（4章）"),
           ("②", "2組の辺とその間の角がそれぞれ等しい（4章）"),
           ("③", "1組の辺とその両端の角がそれぞれ等しい（4章）"),
           ("⑪", "二等辺三角形の2つの底角は等しい"),
           ("⑫", "二等辺三角形の頂角の二等分線は、底辺を垂直に2等分する"),
           ("⑬", "<b>2つの角が等しい三角形は、二等辺三角形である</b>（今日つくるカード）")],
    footer="中学2年 数学　5章 三角形・四角形（全18時間）　第4時 逆と反例／A3横・5ブロック",
    memo="<b>ここから学び合い。</b><br>"
         "<b>介入点（5分）</b>　④に入って10分ほどで全体を止め、"
         "「反例は1つ見つければ終わり。たくさん探さなくてよい」を言う。<br>"
         "<b>削り順</b>　③(2) を宿題 → ④のウと最後の問いを宿題。"
         "死守するのは ③(1) と ④のイ。イ（a＝2、b＝−2）で「1つで足りる」が一番伝わる。",
    blocks=[
"""    <p class="inst">カード⑪⑫を、隣の人に1つずつ言う。</p>
    <ol>
      <li>⑪ 二等辺三角形の2つの%sは等しい</li>
      <li>⑫ 二等辺三角形の%sの二等分線は、底辺を%sする</li>
      <li>⑪を「〜ならば、〜である」の形に書きかえる
        %s</li>
    </ol>
    <div class="spacer"></div>
    <p class="inst">「〜ならば」の前が<b>仮定</b>、後ろが<b>結論</b>。</p>"""
% (z("底角"), z("頂角"), z("垂直に2等分", "w"),
   rz(2, "△ABC で AB＝AC ならば、∠B＝∠C である。")),

"""    <p>ことがらの<b>仮定と結論を入れかえた</b>ものを、そのことがらの<b>逆</b>という。</p>
    <p class="inst">⑪の　仮定 %s　／　結論 %s</p>
    <p class="inst">⑪の逆 → %s</p>
    %s
    <div class="spacer"></div>
    <p class="inst" style="border-top:1px dotted var(--rule); padding-top:5px">
      <b>今日の問い</b>　逆は、いつでも正しいといえるか。</p>"""
% (z("AB＝AC", "w"), z("∠B＝∠C", "w"), z("∠B＝∠C ならば AB＝AC", "ww"),
   fig("0 0 200 142", f1, "図1　∠B＝∠C だけがわかっている")),

"""    <p class="inst">図1は ∠B＝∠C <b>だけ</b>がわかっている三角形。AB＝AC といえるか、見た目で決めずに確かめる。</p>
    <ol>
      <li><b>∠B＝∠C ならば AB＝AC を証明する。</b>（図2）
        %s
        <span class="inst">書く前に</span>　<span class="cn">使う合同条件</span>%s
        <span class="cn">選んだ理由</span>%s
        %s</li>
      <li>2つの内角が次のような三角形のうち、<b>二等辺三角形をすべて選ぶ</b>。
        <br>㋐ 40°、100°　㋑ 50°、70°　㋒ 150°、20°　㋓ 120°、30°
        <br>答 %s　<span class="cn">カード</span>%s
        %s</li>
    </ol>"""
% (fig("0 0 200 150", f2, "図2　∠A の二等分線と辺BC との交点を D とする"),
   z("③"), z("ADの両端の角が言えるから", "ww"),
   rz(6, "△ABD と △ACD において<br>"
         "AD は ∠A の二等分線だから　∠BAD＝∠CAD　……(a)<br>"
         "仮定より　∠B＝∠C　……(b)<br>"
         "(a)(b)と三角形の内角の和から　∠ADB＝∠ADC　……(c)<br>"
         "AD は共通　……(d)<br>"
         "(a)(c)(d)より、<b>カード③</b>（1組の辺とその両端の角）から　△ABD≡△ACD<br>"
         "対応する辺は等しいから　AB＝AC　■"),
   z("㋐と㋓", "w"), z("⑬"),
   rz(2, "㋐ 残りは40° → 40,40,100 で二等辺／㋑ 60° → 50,60,70 でちがう<br>"
         "㋒ 10° → 150,20,10 でちがう／㋓ 30° → 120,30,30 で二等辺")),

"""    <p><b>次の3つの逆をつくり、正しいかどうか調べなさい。</b><br>
      <span class="inst">正しくないものは、<b>反例を1つ</b>あげなさい（1つで足ります）。</span></p>
    <p class="inst">ア　△ABC≡△DEF ならば、∠A＝∠D である<br>
      イ　a＝b ならば、a<sup>2</sup>＝b<sup>2</sup> である<br>
      ウ　正三角形ならば、二等辺三角形である</p>
    %s
    <div class="gridbox"><svg viewBox="0 0 230 100" role="img" aria-label="反例をかく方眼">%s</svg></div>
    <p style="margin-top:6px"><b>3つのうち、正しい逆はいくつありましたか。</b>%s<br>
      <span class="inst">逆が正しいかどうかは、何を調べれば決まりますか。</span></p>
    %s
"""
% (rz(5, "アの逆「∠A＝∠D ならば △ABC≡△DEF」…… <b>正しくない</b>。"
         "反例: 1つの角だけ等しく大きさのちがう2つの三角形（大小の三角定規など）。<br>"
         "イの逆「a<sup>2</sup>＝b<sup>2</sup> ならば a＝b」…… <b>正しくない</b>。反例: a＝2、b＝−2。<br>"
         "ウの逆「二等辺三角形ならば、正三角形である」…… <b>正しくない</b>。"
         "反例: 3辺が 5、5、8 の三角形。"),
   grid(230, 100, 23),
   z("0"),
   rz(3, "正しい逆は0個。<br>"
         "決め方: <b>証明できれば正しい。反例が1つでも見つかれば正しくない。</b><br>"
         "もとのことがらが正しくても、逆が正しいとは限らない。⑬は逆が正しかった"
         "めずらしい例で、だからわざわざ証明した。")),

None,
])

if __name__ == "__main__":
    print(build(SHEET, sys.argv[1]), "bytes")
