# -*- coding: utf-8 -*-
"""第6時 直角三角形の合同条件（学校図書『数学2』p.158-160）学び合い
   第2時 JUMP②「垂線では、辺2つと角1つが言えるのにその角が2辺の間にないから
   合同と言えない」の回収。"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from a3_sheet import build, angle_arc, angle_deg, tick, right_angle, grid, z, rz, fig

# ---- 図1 二等辺三角形と垂線（第2時の回収） ----
A, B, C, H = (100, 18), (45, 124), (155, 124), (100, 124)
f1 = "".join([
    '<polygon class="l" points="100,18 45,124 155,124"/>',
    '<line class="l" x1="100" y1="18" x2="100" y2="124"/>',
    tick(A, B), tick(A, C),
    right_angle(H, C, A, 8),
    '<text class="t" x="100" y="12" text-anchor="middle">A</text>',
    '<text class="t" x="35" y="134">B</text><text class="t" x="159" y="134">C</text>',
    '<text class="t" x="100" y="138" text-anchor="middle">H</text>',
])

# ---- ㋐〜㋓ 実寸で描く（1cm = 14px）。ラベルの数値は座標から検算する ----
SC = 14.0
def rtri(hyp=None, ang=None, leg=None, mirror=False, note=""):
    if ang is not None:
        a, b = hyp*math.cos(math.radians(ang)), hyp*math.sin(math.radians(ang))
    else:
        b, a = leg, math.sqrt(hyp*hyp - leg*leg)
    aw, bh = a*SC, b*SC
    if not mirror:
        P = (16, 16+bh); Q = (16+aw, 16+bh); R = (16, 16)
    else:
        P = (16+aw, 16+bh); Q = (16, 16+bh); R = (16+aw, 16)
    s = ['<polygon class="l" points="%.1f,%.1f %.1f,%.1f %.1f,%.1f"/>' % (P+Q+R),
         right_angle(P, Q, R, 7)]
    # 斜辺のラベル（QR の中点の外側）
    mx, my = (Q[0]+R[0])/2.0, (Q[1]+R[1])/2.0
    s.append('<text class="t" x="%.1f" y="%.1f" text-anchor="middle">%gcm</text>'
             % (mx + (10 if not mirror else -10), my - 4, hyp))
    if ang is not None:
        s.append(angle_arc(Q, P, R, 15))
        s.append('<text class="t" x="%.1f" y="%.1f" text-anchor="end">%g°</text>'
                 % (Q[0]-6, Q[1]-6, round(angle_deg(Q, P, R))))
    else:
        s.append('<text class="t" x="%.1f" y="%.1f" text-anchor="%s">%gcm</text>'
                 % (P[0] + (-4 if not mirror else 4), (P[1]+R[1])/2.0,
                    "end" if not mirror else "start", leg))
    return "".join(s)

f_a = rtri(hyp=6, ang=40)
f_b = rtri(hyp=6, leg=4)
f_c = rtri(hyp=5, ang=40)
f_d = rtri(hyp=6, leg=4, mirror=True)

# ---- 図2 JUMP（教科書 p.160 問4） ----
jA, jB, jC = (30, 30), (30, 120), (170, 120)
jD, jE = (105.7, 78.7), (79.1, 120)
assert abs(angle_deg(jB, jA, jC) - 90) < 0.1
assert abs(angle_deg(jD, jA, jE) - 90) < 0.1
assert abs(math.hypot(*(jA[i]-jB[i] for i in (0, 1))) -
           math.hypot(*(jA[i]-jD[i] for i in (0, 1)))) < 0.2   # AB＝AD
f2 = "".join([
    '<polygon class="l" points="30,30 30,120 170,120"/>',
    '<line class="l" x1="105.7" y1="78.7" x2="79.1" y2="120"/>',
    tick(jA, jB), tick(jA, jD),
    right_angle(jB, jC, jA, 8), right_angle(jD, jA, jE, 8),
    # 赤刷りだけに、2通りの補助線と結論の印を出す
    '<g class="ft">',
    '<line class="ftline" x1="30" y1="30" x2="79.1" y2="120" stroke-dasharray="4 3"/>',
    '<line class="ftline" x1="30" y1="120" x2="105.7" y2="78.7" stroke-dasharray="4 3"/>',
    tick(jB, jE, 2, cls="ftline"), tick(jD, jE, 2, cls="ftline"),
    '</g>',
    '<text class="t" x="22" y="26">A</text><text class="t" x="20" y="132">B</text>',
    '<text class="t" x="174" y="132">C</text>',
    '<text class="t" x="110" y="76">D</text><text class="t" x="76" y="132">E</text>',
])

SHEET = dict(
    title="足りない道具をつくる",
    ji="第6時",
    pg="学校図書『数学2』p.158-160／1節 三角形（全18時間・学び合い）",
    goal="直角三角形だけに使える合同条件をつくり、第2時にできなかった証明を完成させる。",
    katari="第2時の ④② で、こう確かめました。「垂線をひくと、辺2つと角1つは言えるのに、"
           "<b>その角が2辺の間にないから</b>合同と言えない」。あれは正しい判断でした。"
           "できなかったのは、<b>道具が足りなかった</b>からです。今日はその道具をつくります。",
    cards_title="根拠カード — 今日つくるのは ⑭ と ⑮ の2枚",
    cards_hint="①②③と⑪⑫⑬は見てよい。⑭⑮の中身は、③(1) で自分たちで書いてから使う。",
    cards=[("①", "3組の辺がそれぞれ等しい（4章）"),
           ("②", "2組の辺とその間の角がそれぞれ等しい（4章）"),
           ("③", "1組の辺とその両端の角がそれぞれ等しい（4章）"),
           ("⑪", "二等辺三角形の2つの底角は等しい"),
           ("⑫", "二等辺三角形の頂角の二等分線は、底辺を垂直に2等分する"),
           ("⑬", "2つの角が等しい三角形は、二等辺三角形である"),
           ("⑭", "直角三角形の合同条件・その1　<b>（今日 ③(1) で書く）</b>"),
           ("⑮", "直角三角形の合同条件・その2　<b>（今日 ③(1) で書く）</b>")],
    footer="中学2年 数学　5章 三角形・四角形（全18時間）　第6時 直角三角形の合同／A3横・5ブロック",
    blocks=[
"""    <p class="inst">第2時にできなかったことを思い出す。</p>
    %s
    <ol>
      <li>図1で言えることは3つ。AB＝AC、AH は%s、∠AHB＝∠AHC＝%s°</li>
      <li>それでも <b>△ABH≡△ACH</b> と言えなかった理由
        %s</li>
    </ol>"""
% (fig("0 0 200 148", f1, "図1　AB＝AC、AH⊥BC"), z("共通"), z("90"),
   rz(2, "辺2つと角1つだが、その角が<b>2辺の間にない</b>のでカード②が使えない。①③も足りない。")),

"""    <p>直角三角形には、<b>①②③のほかに使える条件がある。</b></p>
    <p class="inst">直角の向かい側の辺を %s という。</p>
    <p class="inst">辺2つと角1つでも、<b>その角が直角だとわかっている</b>なら、
      ふつうの三角形より少ない条件で決まるのではないか。</p>
    <div class="spacer"></div>
    <p class="inst" style="border-top:1px dotted var(--rule); padding-top:5px">
      <b>今日の問い</b>　直角三角形だけに使える条件は、どう書けばよいか。</p>"""
% z("斜辺", "w"),

"""    <ol>
      <li><b>直角三角形の合同条件を2つ、ことばで書く。</b>（教科書 p.159）<br>
        ⑭ 斜辺と1つの%sがそれぞれ等しい<br>
        ⑮ 斜辺と他の1%sがそれぞれ等しい<br>
        <span class="inst" style="margin-top:4px">書けたら図1にもどり、<b>カード⑪を使わずに</b>
        △ABH≡△ACH を示す。<br>（⑪を使うと ∠B＝∠C が先に出てしまい、第2時の宿題の答えにならない。）</span>
        %s</li>
      <li>次の4つから<b>合同な組を選び</b>、使ったカードの番号を書く。
        <div class="figs">%s%s%s%s</div>
        合同なのは %s　<span class="cn">カード</span>%s<br>
        <span class="inst">合同でない組は、なぜ合同といえないかを一言。</span>
        %s</li>
    </ol>"""
% (z("鋭角"), z("辺"),
   rz(5, "△ABH と △ACH において<br>"
         "仮定より　∠AHB＝∠AHC＝90°　……(a)<br>"
         "仮定より　AB＝AC（斜辺）　……(b)<br>"
         "AH は共通（他の1辺）　……(c)<br>"
         "(a)(b)(c)より、<b>カード⑮</b>（斜辺と他の1辺）から　△ABH≡△ACH　■<br>"
         "※ 第2時に「足りない」と言ったぶんが、⑮で埋まった。ここで全体を止める。"),
   fig("0 0 100 92", f_a, "㋐", "85px"), fig("0 0 100 92", f_b, "㋑", "85px"),
   fig("0 0 100 92", f_c, "㋒", "85px"), fig("0 0 100 92", f_d, "㋓", "85px"),
   z("㋑と㋓", "w"), z("⑮"),
   rz(2, "㋐と㋒ は鋭角が40°で等しいが<b>斜辺の長さがちがう</b>（6cmと5cm）ので合同ではない。<br>"
         "㋑と㋓ は向きがちがうだけ。斜辺6cmと他の1辺4cmが等しいので⑮で合同。")),

"""    <p class="inst">1人では届きません。となりと相談してよい。<b>どこまで自分で進めたか</b>を書く。</p>
    <p>∠B＝90° の直角三角形 ABC で、斜辺 AC 上に <b>AB＝AD</b> となる点 D をとる。
      D を通る AC の垂線と辺 BC との交点を E とする。
      <span class="inst">必要な線は自分でひいてよい。</span></p>
    %s
    <ol class="circ">
      <li><b>BE＝DE</b> を証明しなさい。
        %s</li>
      <li>同じことを、<b>⑭⑮を使わずに</b>証明できますか。できるなら書きなさい。
        %s</li>
    </ol>"""
% (fig("0 0 200 145", f2, "図2　∠B＝90°、AB＝AD、DE⊥AC"),
   rz(5, "A と E を結ぶ。<br>"
         "△ABE と △ADE において　∠ABE＝∠ADE＝90°　……(a)／"
         "仮定より AB＝AD（他の1辺）　……(b)／AE は共通（斜辺）　……(c)<br>"
         "(a)(b)(c)より、<b>カード⑮</b>から　△ABE≡△ADE<br>"
         "対応する辺は等しいから　BE＝DE　■"),
   rz(4, "<b>できる。</b>B と D を結ぶ。<br>"
         "AB＝AD だから △ABD は二等辺三角形で、<b>カード⑪</b>より ∠ABD＝∠ADB。<br>"
         "∠ABE＝∠ADE＝90° だから、そこから等しい角をひいて　∠EBD＝∠EDB。<br>"
         "2つの角が等しいから、<b>カード⑬</b>より △EBD は二等辺三角形。よって BE＝DE　■<br>"
         "※ ⑭⑮は<b>便利だが必須ではない</b>。同じ結論に2通りの道がある。")),

"""    <ol>
      <li>今日つくったカードの番号 %s</li>
      <li>今日は　聞いた ／ 聞かれた ／ どちらもなかった<br>
        <span class="inst">当てはまるものに丸。名前は書かない。</span></li>
      <li><b>第2時にできなかったことが、今日できました。何が増えたからですか。</b>
        %s</li>
    </ol>
    <div class="spacer"></div>
    <p class="inst tonly" style="border-top:1px dotted var(--rule); padding-top:5px">
      <b>削り順</b>　③(2) を宿題 → ④② を宿題。<br>死守するのは ③(1) と ④①。<br>
      <b>介入点（5分）</b>　③(1) が終わったところで全体を止め、
      「第2時にできなかったことが、いまできた」を全員で確認する。<br>
      ここを通さないと、カードが増える意味が伝わらない。<br>
      ④② まで届いた生徒がいたら、その別解を全体に紹介する。</p>"""
% (z("⑭⑮", "w"),
   rz(3, "使えるカードが2枚増えたから。<br>"
         "できなかったのは頭が悪かったからではなく、<b>道具が足りなかった</b>から。<br>"
         "足りないとわかったから、新しい道具をつくった。この順序に気づけていれば十分。")),
])

if __name__ == "__main__":
    print(build(SHEET, sys.argv[1]), "bytes")
