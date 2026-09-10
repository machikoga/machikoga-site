from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

section_html = r'''<section class="section ai-final" id="ai">
  <div class="ai-final-inner">
    <div class="ai-final-kicker">AI CANNOT CREATE THIS</div>
    <h2 class="ai-final-title">AIには作れない、<br>地域ビジネスの価値。</h2>
    <p class="ai-final-lead">AIは文章や画像を作れても、地域で積み上げてきた <strong>「本物の価値」</strong> までは作れません。</p>

    <div class="ai-stock">
      <span class="ai-stock-label">STOCK TYPE</span>
      <p>広告のように止めたら消える「フロー型」ではなく、SNS・Google・地域情報を積み上げる <strong>ストック型の経営資産</strong>へ。</p>
    </div>

    <div class="ai-contrast">
      <div class="ai-contrast-card ai-can">
        <span class="ai-contrast-label">AIが作れる</span>
        <strong>文章・画像・情報整理</strong>
        <small>速く、便利に、何度でも。</small>
      </div>
      <div class="ai-vs">VS</div>
      <div class="ai-contrast-card ai-cannot">
        <span class="ai-contrast-label">AIには作れない</span>
        <strong>地域で積み上げた5つの価値</strong>
        <small>その店・その場所にしかないもの。</small>
      </div>
    </div>

    <div class="ai-values">
      <article class="ai-value"><span class="ai-value-no">01</span><h3>土地</h3><p>その場所で商売してきた事実</p></article>
      <article class="ai-value"><span class="ai-value-no">02</span><h3>歴史</h3><p>店・会社が歩んできた背景</p></article>
      <article class="ai-value"><span class="ai-value-no">03</span><h3>時間・プロセス</h3><p>地域に積み重ねた信頼</p></article>
      <article class="ai-value"><span class="ai-value-no">04</span><h3>思い出</h3><p>お客様との体験・記憶</p></article>
      <article class="ai-value ai-value-featured"><span class="ai-value-no">05</span><h3>地域との<br>つながり</h3><p>小金井で育てた、本物の事業資産</p></article>
    </div>

    <div class="ai-final-message">
      <span>価値は、すでにある。</span>
      <strong>まちこがは、それを見つかる形にする。</strong>
    </div>
  </div>
</section>'''

pattern = r'<section class="section (?:ai|ai-final)[^"]*" id="ai">.*?</section>'
s, n = re.subn(pattern, section_html, s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('AI section not found or replaced more than once')

css = r'''
/* V68 AI SECTION EXACT FINAL */
.ai-final{
  position:relative;
  overflow:hidden;
  padding:96px 0;
  background:
    radial-gradient(circle at 12% 8%,rgba(240,217,149,.14),transparent 25%),
    radial-gradient(circle at 92% 18%,rgba(24,184,174,.15),transparent 28%),
    linear-gradient(145deg,#031735 0%,#082c60 58%,#0a5267 100%);
  color:#fff;
}
.ai-final *{box-sizing:border-box}
.ai-final-inner{width:min(1180px,calc(100% - 48px));margin:0 auto}
.ai-final-kicker{display:flex;align-items:center;gap:10px;margin-bottom:18px;color:#f0d995;font-size:.76rem;font-weight:900;letter-spacing:.15em}
.ai-final-kicker:before{content:"";width:28px;height:2px;border-radius:10px;background:#f0d995}
.ai-final-title{margin:0;max-width:900px;color:#fff;font-size:clamp(3.1rem,6.4vw,6.2rem);line-height:1.02;letter-spacing:-.065em;font-weight:900;word-break:keep-all;overflow-wrap:normal;text-wrap:balance}
.ai-final-lead{max-width:780px;margin:26px 0 0;color:rgba(255,255,255,.84);font-size:clamp(1.02rem,1.45vw,1.22rem);line-height:1.85}
.ai-final-lead strong{color:#f0d995;font-weight:900}
.ai-stock{max-width:850px;margin-top:24px;padding:20px 24px;border:1px solid rgba(240,217,149,.24);border-radius:20px;background:rgba(255,255,255,.075);backdrop-filter:blur(8px)}
.ai-stock-label{display:inline-flex;padding:6px 10px;border-radius:999px;background:#f0d995;color:#071d3f;font-size:.65rem;font-weight:900;letter-spacing:.1em}
.ai-stock p{margin:10px 0 0;color:rgba(255,255,255,.86);font-size:1.02rem;line-height:1.8}.ai-stock strong{color:#fff;font-size:1.08em;font-weight:900}
.ai-contrast{display:grid;grid-template-columns:1fr 76px 1fr;gap:16px;align-items:stretch;margin-top:42px}.ai-contrast-card{padding:25px 26px;border-radius:24px}.ai-can{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15)}.ai-cannot{background:linear-gradient(145deg,#fffdf8,#f5f8fc);border:2px solid rgba(240,217,149,.75);box-shadow:0 20px 48px rgba(0,0,0,.15)}
.ai-contrast-label{display:block;margin-bottom:8px;font-size:.68rem;font-weight:900;letter-spacing:.08em;color:#f0d995}.ai-cannot .ai-contrast-label{color:#9b6a26}.ai-contrast-card strong{display:block;font-size:clamp(1.35rem,2vw,1.8rem);line-height:1.3;letter-spacing:-.025em}.ai-can strong{color:#fff}.ai-cannot strong{color:#071d3f}.ai-contrast-card small{display:block;margin-top:6px;font-size:.85rem;line-height:1.6}.ai-can small{color:rgba(255,255,255,.63)}.ai-cannot small{color:#68758a}.ai-vs{display:flex;align-items:center;justify-content:center;color:#f0d995;font-size:1.1rem;font-weight:900;letter-spacing:.06em}
.ai-values{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-top:30px}.ai-value{min-height:190px;padding:22px;border-radius:24px;background:linear-gradient(180deg,rgba(255,255,255,.10),rgba(255,255,255,.055));border:1px solid rgba(255,255,255,.15);box-shadow:inset 0 1px 0 rgba(255,255,255,.05)}.ai-value-no{display:inline-flex;align-items:center;justify-content:center;min-width:38px;height:32px;padding:0 9px;border-radius:11px;background:rgba(240,217,149,.12);border:1px solid rgba(240,217,149,.3);color:#f0d995;font-size:.7rem;font-weight:900}.ai-value h3{margin:20px 0 0;color:#fff;font-size:1.45rem;line-height:1.25;letter-spacing:-.02em;word-break:keep-all}.ai-value p{margin:9px 0 0;color:rgba(255,255,255,.65);font-size:.83rem;line-height:1.7}.ai-value-featured{background:linear-gradient(145deg,#fffdf8,#edf5ff);border:2px solid rgba(240,217,149,.78);transform:translateY(-7px);box-shadow:0 20px 44px rgba(0,0,0,.16)}.ai-value-featured .ai-value-no{background:#071d3f;border:0;color:#f0d995}.ai-value-featured h3{color:#071d3f}.ai-value-featured p{color:#617087}
.ai-final-message{position:relative;margin-top:32px;padding:44px 48px;border-radius:32px;overflow:hidden;background:linear-gradient(180deg,#fff,#f7f9fd);border:1px solid #dce5ef;box-shadow:0 28px 60px rgba(0,0,0,.17)}.ai-final-message:before{content:"";position:absolute;top:0;left:0;right:0;height:6px;background:linear-gradient(90deg,#c7a253,#f0d995,#1ab7aa)}.ai-final-message span{display:block;margin:0;color:#a36c1b;font-size:clamp(2.4rem,4.7vw,4.8rem);line-height:1.05;letter-spacing:-.055em;font-weight:900}.ai-final-message strong{display:block;margin-top:8px;color:#071d3f;font-size:clamp(2rem,4vw,4rem);line-height:1.08;letter-spacing:-.05em;font-weight:900;word-break:keep-all;text-wrap:balance}
@media(max-width:1000px){.ai-values{grid-template-columns:repeat(3,1fr)}.ai-value-featured{transform:none}}
@media(max-width:780px){.ai-final{padding:68px 0}.ai-final-inner{width:min(100% - 34px,1180px)}.ai-final-title{font-size:clamp(2.6rem,12vw,4.1rem);line-height:1.03}.ai-final-lead{margin-top:20px;font-size:1rem;line-height:1.8}.ai-stock{padding:17px}.ai-stock p{font-size:.94rem}.ai-contrast{grid-template-columns:1fr;gap:10px}.ai-vs{height:30px}.ai-values{grid-template-columns:1fr}.ai-value{min-height:auto}.ai-final-message{padding:30px 22px;border-radius:25px}.ai-final-message span{font-size:clamp(2rem,10vw,3rem)}.ai-final-message strong{font-size:clamp(1.65rem,8vw,2.6rem)}}
'''

# Remove old exact-final CSS block if rerun, then append this one before the first closing style tag.
s = re.sub(r'/\* V68 AI SECTION EXACT FINAL \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

for token in ['AIには作れない、<br>地域ビジネスの価値。','STOCK TYPE','地域で積み上げた5つの価値','価値は、すでにある。','まちこがは、それを見つかる形にする。','V68 AI SECTION EXACT FINAL']:
    if token not in s:
        raise SystemExit(f'Missing AI final token: {token}')
