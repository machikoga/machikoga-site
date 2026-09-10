from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

why_html = '''<section class="section why why-premium" id="why"><div class="container">
<div class="why-premium-head"><div><span class="kicker">WHY NOW</span><h2>なぜ、今整えるのか。</h2></div><p class="why-premium-lead">お店の価値ではなく、<strong>「見つけられ方」</strong>で差がつく時代です。<br>SNS・Google・地域発信をつなぎ、選ばれる入口を整えます。</p></div>
<div class="why-reasons">
<article class="why-reason"><div class="why-reason-top"><span class="why-icon why-icon-ai">AI</span><span class="why-no">01</span></div><h3>AIに伝わる情報を増やす</h3><p>SNS・Google・写真・更新情報が揃うほど、AIにも店の特徴が伝わりやすくなります。</p><div class="why-outcome">情報を整える <b>→</b> 候補に入りやすくなる</div></article>
<article class="why-reason"><div class="why-reason-top"><span class="why-icon why-icon-google">G</span><span class="why-no">02</span></div><h3>Googleで、先に見つかる店へ</h3><p>検索・地図・口コミ・写真が整っているほど、比較のスタート地点に立ちやすくなります。</p><div class="why-outcome">見つかる <b>→</b> 良さを知ってもらえる</div></article>
<article class="why-reason"><div class="why-reason-top"><span class="why-icon why-icon-local">↗</span><span class="why-no">03</span></div><h3>地域の中で、選ばれる土台をつくる</h3><p>発信・検索・口コミがつながると、小金井の中で選ばれる理由が積み上がります。</p><div class="why-outcome">店の差だけでなく、<b>見つかり方の差</b></div></article>
</div>
<div class="why-conclusion"><div class="why-conclusion-copy"><span class="why-conclusion-label">THE POINT</span><h3>良い店だからこそ、<br><em>見つかる仕組み</em>まで整える。</h3><p>必要なのは、投稿数を増やすことではなく、<strong>小金井で見つかる入口を持つこと。</strong></p></div><div class="why-entry-grid"><div><span>01</span><b>Google検索</b></div><div><span>02</span><b>Googleマップ</b></div><div><span>03</span><b>Instagram</b></div><div><span>04</span><b>AI検索</b></div></div></div>
</div></section>'''

ai_html = '''<section class="section ai ai-premium" id="ai"><div class="container">
<div class="ai-premium-head"><div><span class="kicker">AI CANNOT CREATE THIS</span><h2>AIには作れない、<br>地域ビジネスの価値。</h2></div><p>AIは文章や画像を作れても、地域で積み上げてきた<strong>「本物の価値」</strong>までは作れません。</p></div>
<div class="ai-contrast"><div class="ai-contrast-side ai-can"><span>AIが作れる</span><strong>文章・画像・情報整理</strong><small>速く、便利に、何度でも。</small></div><div class="ai-vs"><span>VS</span></div><div class="ai-contrast-side ai-cannot"><span>AIには作れない</span><strong>地域で積み上げた5つの価値</strong><small>その店・その場所にしかないもの。</small></div></div>
<div class="ai-values-premium">
<article><span class="ai-value-no">01</span><h3>土地</h3><p>その場所で<br>商売してきた事実</p></article>
<article><span class="ai-value-no">02</span><h3>歴史</h3><p>店・会社が<br>歩んできた背景</p></article>
<article><span class="ai-value-no">03</span><h3>時間・プロセス</h3><p>地域に<br>積み重ねた信頼</p></article>
<article><span class="ai-value-no">04</span><h3>思い出</h3><p>お客様との<br>体験・記憶</p></article>
<article class="ai-value-special"><span class="ai-value-no">05</span><h3>地域との<br>つながり</h3><p>小金井で育てた、<br>本物の事業資産</p></article>
</div>
<div class="ai-final-message"><span>VALUE ALREADY EXISTS</span><h3><em>価値は、すでにある。</em><br>まちこがは、それを<br class="sp-only">見つかる形にする。</h3></div>
</div></section>'''

# Replace the two sections as complete components.
s, n1 = re.subn(r'<section class="section why[^\"]*" id="why">.*?</section>', why_html, s, count=1, flags=re.S)
s, n2 = re.subn(r'<section class="section ai[^\"]*" id="ai">.*?</section>', ai_html, s, count=1, flags=re.S)
if n1 != 1 or n2 != 1:
    raise SystemExit(f'Could not replace WHY/AI sections: why={n1}, ai={n2}')

css = r'''
/* V68 WHY AI PREMIUM */

/* ---------- WHY NOW ---------- */
.why-premium{background:linear-gradient(180deg,#ffffff 0%,#f4f7fb 100%)}
.why-premium-head{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(320px,.85fr);gap:56px;align-items:end;margin-bottom:34px}
.why-premium-head h2{margin-top:10px;max-width:9em;color:var(--navy);font-size:clamp(3rem,5.7vw,5.4rem);line-height:.98;letter-spacing:-.06em;word-break:keep-all;overflow-wrap:normal;text-wrap:balance}
.why-premium-lead{padding-bottom:7px;color:#53647c;font-size:1.02rem;line-height:1.95;max-width:560px}
.why-premium-lead strong{color:var(--navy);font-size:1.08em}
.why-reasons{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.why-reason{position:relative;min-height:330px;padding:26px 26px 23px;border-radius:28px;background:#fff;border:1px solid #dae3ed;box-shadow:0 18px 42px rgba(5,25,57,.075);overflow:hidden;display:flex;flex-direction:column}
.why-reason:before{content:"";position:absolute;inset:0 0 auto;height:5px;background:linear-gradient(90deg,#0b5ea8,#0aa095)}
.why-reason:nth-child(3):before{background:linear-gradient(90deg,#b47718,#e3b94f)}
.why-reason-top{display:flex;align-items:center;justify-content:space-between;gap:12px}
.why-icon{display:grid;place-items:center;width:76px;height:76px;border-radius:23px;color:#fff;font-size:1.52rem;font-weight:950;box-shadow:0 15px 30px rgba(5,25,57,.16)}
.why-icon-ai{background:linear-gradient(145deg,#133c7c,#2b70c7)}
.why-icon-google{background:linear-gradient(145deg,#0c7184,#14aaa1)}
.why-icon-local{background:linear-gradient(145deg,#986616,#d7a93e)}
.why-no{color:#aeb9c8;font-size:.68rem;font-weight:900;letter-spacing:.14em}
.why-reason h3{margin-top:21px;color:var(--navy);font-size:clamp(1.32rem,1.9vw,1.72rem);line-height:1.3;letter-spacing:-.025em;word-break:keep-all}
.why-reason p{margin-top:12px;color:#617087;font-size:.91rem;line-height:1.8}
.why-outcome{margin-top:auto;padding-top:17px;border-top:1px dashed #d9e1eb;color:#52637a;font-size:.78rem;font-weight:850}
.why-outcome b{color:#0a6570}
.why-conclusion{margin-top:22px;padding:30px 32px;border-radius:30px;background:linear-gradient(135deg,#061a38 0%,#0a3567 67%,#0a6670 100%);color:#fff;display:grid;grid-template-columns:1.15fr .85fr;gap:30px;align-items:center;box-shadow:0 24px 58px rgba(5,25,57,.16);position:relative;overflow:hidden}
.why-conclusion:before{content:"";position:absolute;inset:0 0 auto;height:5px;background:linear-gradient(90deg,#f0d995,#0aa095)}
.why-conclusion-label{display:inline-flex;padding:5px 9px;border-radius:999px;background:rgba(240,217,149,.12);border:1px solid rgba(240,217,149,.32);color:#f0d995;font-size:.61rem;font-weight:900;letter-spacing:.12em}
.why-conclusion h3{margin-top:11px;color:#fff;font-size:clamp(2rem,3.6vw,3.35rem);line-height:1.12;letter-spacing:-.045em;word-break:keep-all}
.why-conclusion h3 em{font-style:normal;color:#f0d995}
.why-conclusion p{margin-top:12px;color:rgba(255,255,255,.75);font-size:.9rem;line-height:1.75}
.why-conclusion p strong{color:#fff}
.why-entry-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.why-entry-grid div{min-height:76px;padding:13px 15px;border-radius:17px;background:rgba(255,255,255,.09);border:1px solid rgba(255,255,255,.12);display:flex;align-items:center;gap:10px}
.why-entry-grid span{display:grid;place-items:center;width:29px;height:29px;border-radius:10px;background:rgba(240,217,149,.12);color:#f0d995;font-size:.6rem;font-weight:900}
.why-entry-grid b{color:#fff;font-size:.82rem}

/* ---------- AI VALUE ---------- */
.ai-premium{background:radial-gradient(circle at 8% 4%,rgba(240,217,149,.13),transparent 26%),radial-gradient(circle at 92% 15%,rgba(12,139,134,.19),transparent 30%),linear-gradient(145deg,#031632 0%,#08295b 56%,#0a4f65 100%);color:#fff}
.ai-premium-head{display:grid;grid-template-columns:minmax(0,1.18fr) minmax(300px,.82fr);gap:54px;align-items:end}
.ai-premium-head h2{margin-top:10px;max-width:10em;color:#fff;font-size:clamp(3rem,5.7vw,5.25rem);line-height:1;letter-spacing:-.06em;word-break:keep-all;overflow-wrap:normal;text-wrap:balance}
.ai-premium-head>p{padding-bottom:8px;color:rgba(255,255,255,.77);font-size:1rem;line-height:1.9;max-width:510px}
.ai-premium-head>p strong{color:#f0d995}
.ai-contrast{display:grid;grid-template-columns:1fr 72px 1fr;gap:14px;align-items:stretch;margin-top:34px}
.ai-contrast-side{padding:22px 24px;border-radius:24px;display:flex;flex-direction:column;justify-content:center;min-height:132px}
.ai-can{background:rgba(255,255,255,.075);border:1px solid rgba(255,255,255,.15)}
.ai-cannot{background:linear-gradient(145deg,#fffdf7,#f5f8ff);border:1px solid rgba(240,217,149,.9);box-shadow:0 18px 40px rgba(0,0,0,.12)}
.ai-contrast-side>span{font-size:.66rem;font-weight:900;letter-spacing:.1em;color:#f0d995}
.ai-cannot>span{color:#9b6a26}
.ai-contrast-side strong{margin-top:7px;font-size:clamp(1.28rem,2vw,1.7rem);line-height:1.25;color:#fff;letter-spacing:-.02em}
.ai-cannot strong{color:#071d3f}
.ai-contrast-side small{margin-top:7px;color:rgba(255,255,255,.58);font-size:.72rem}
.ai-cannot small{color:#758196}
.ai-vs{display:grid;place-items:center;position:relative}
.ai-vs:before{content:"";position:absolute;top:0;bottom:0;width:1px;background:linear-gradient(180deg,transparent,rgba(240,217,149,.5),transparent)}
.ai-vs span{position:relative;z-index:1;display:grid;place-items:center;width:48px;height:48px;border-radius:50%;background:#061a38;border:1px solid rgba(240,217,149,.45);color:#f0d995;font-size:.76rem;font-weight:950;box-shadow:0 10px 24px rgba(0,0,0,.18)}
.ai-values-premium{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-top:26px}
.ai-values-premium article{position:relative;min-height:196px;padding:24px 20px;border-radius:24px;background:linear-gradient(180deg,rgba(255,255,255,.095),rgba(255,255,255,.055));border:1px solid rgba(255,255,255,.16);overflow:hidden}
.ai-values-premium article:after{content:"";position:absolute;width:120px;height:120px;border-radius:50%;right:-58px;bottom:-62px;background:rgba(255,255,255,.035)}
.ai-value-no{display:grid;place-items:center;width:34px;height:34px;border-radius:11px;background:rgba(240,217,149,.12);border:1px solid rgba(240,217,149,.28);color:#f0d995;font-size:.66rem;font-weight:900}
.ai-values-premium h3{margin-top:18px;color:#fff;font-size:1.34rem;line-height:1.25;letter-spacing:-.02em;word-break:keep-all}
.ai-values-premium p{margin-top:9px;color:rgba(255,255,255,.67);font-size:.8rem;line-height:1.65}
.ai-values-premium .ai-value-special{background:linear-gradient(145deg,#fffdf7,#eef5ff);border:2px solid rgba(240,217,149,.78);transform:translateY(-7px);box-shadow:0 22px 46px rgba(0,0,0,.16)}
.ai-values-premium .ai-value-special .ai-value-no{background:#071d3f;border:0;color:#f0d995}
.ai-values-premium .ai-value-special h3{color:#071d3f}
.ai-values-premium .ai-value-special p{color:#65738a}
.ai-final-message{position:relative;margin-top:24px;padding:34px 38px 37px;border-radius:30px;background:linear-gradient(180deg,#fff,#f7faff);border:1px solid #dce5f0;box-shadow:0 26px 60px rgba(0,0,0,.16);overflow:hidden;text-align:left}
.ai-final-message:before{content:"";position:absolute;inset:0 0 auto;height:6px;background:linear-gradient(90deg,#c7a253,#f0d995,#0aa095)}
.ai-final-message>span{color:#8c7750;font-size:.61rem;font-weight:950;letter-spacing:.15em}
.ai-final-message h3{margin-top:8px;color:#071d3f;font-size:clamp(2.25rem,4.4vw,4.35rem);line-height:1.08;letter-spacing:-.055em;word-break:keep-all;overflow-wrap:normal;text-wrap:balance}
.ai-final-message h3 em{font-style:normal;color:#a36a17}

@media(max-width:1000px){
  .why-premium-head,.ai-premium-head{grid-template-columns:1fr;gap:18px;align-items:start}
  .why-premium-lead,.ai-premium-head>p{max-width:760px;padding-bottom:0}
  .why-conclusion{grid-template-columns:1fr}
  .ai-values-premium{grid-template-columns:repeat(3,1fr)}
  .ai-values-premium .ai-value-special{transform:none}
}
@media(max-width:780px){
  .why-premium-head h2,.ai-premium-head h2{font-size:clamp(2.55rem,11.7vw,4rem);max-width:none}
  .why-reasons{grid-template-columns:1fr}
  .why-reason{min-height:auto;padding:22px 20px}
  .why-icon{width:66px;height:66px;border-radius:20px;font-size:1.3rem}
  .why-conclusion{padding:25px 21px;border-radius:25px}
  .why-entry-grid{grid-template-columns:1fr 1fr}
  .ai-contrast{grid-template-columns:1fr;gap:10px}
  .ai-vs{height:40px}
  .ai-vs:before{left:0;right:0;top:50%;bottom:auto;width:auto;height:1px;background:linear-gradient(90deg,transparent,rgba(240,217,149,.45),transparent)}
  .ai-vs span{width:42px;height:42px}
  .ai-values-premium{grid-template-columns:1fr 1fr}
  .ai-values-premium article{min-height:166px}
  .ai-values-premium .ai-value-special{grid-column:1/-1}
  .ai-final-message{padding:28px 21px 30px;border-radius:25px}
  .ai-final-message h3{font-size:clamp(2rem,9vw,3rem)}
}
@media(max-width:430px){
  .why-entry-grid{grid-template-columns:1fr}
  .ai-values-premium{grid-template-columns:1fr}
  .ai-values-premium .ai-value-special{grid-column:auto}
}
'''

# Replace prior premium block if rerun, otherwise append at the end of the main style tag.
if '/* V68 WHY AI PREMIUM */' in s:
    s = re.sub(r'/\* V68 WHY AI PREMIUM \*/.*?(?=</style>)', css.strip() + '\n', s, count=1, flags=re.S)
else:
    s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

required = [
    'why-premium', '良い店だからこそ', '見つかる仕組み',
    'ai-premium', 'VALUE ALREADY EXISTS', '地域で積み上げた5つの価値',
    'V68 WHY AI PREMIUM'
]
for token in required:
    if token not in s:
        raise SystemExit(f'Missing WHY/AI final token: {token}')
