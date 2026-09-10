from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

section = r'''<section class="section dual-platform-section" id="dual-platform"><div class="container dual-platform-inner">
  <div class="dual-platform-kicker">INSTAGRAM × GOOGLE</div>
  <div class="dual-platform-head">
    <h2>片方だけでは、もったいない。<br>InstagramとGoogleを、同時に育てる。</h2>
    <p>Instagramは<strong>好きになってもらう場所</strong>。Googleは<strong>見つけてもらう場所</strong>。2つを同時に積み上げることで、広告のように消えない<strong>地域の情報資産</strong>を育てます。</p>
  </div>

  <div class="dual-platform-main">
    <article class="platform-card platform-instagram">
      <div class="platform-top"><span class="platform-badge">INSTAGRAM</span><span class="platform-mini">FAN / REPEAT</span></div>
      <h3>地域で、好きになってもらう。</h3>
      <p class="platform-sub">楽しく、無理なく続けながら、小金井に強い発信力を育てます。</p>
      <div class="platform-highlight">自前の情報発信インフラをつくる。</div>
      <ul><li>楽しく無理なく、みんなで続けられる形へ</li><li>小金井に強い発信力を持たせる</li><li>地域で好きになってもらう導線を育てる</li><li>自分たちで発信できる力を残す</li></ul>
      <div class="platform-flow"><span>発信する</span><b>→</b><span>知ってもらう</span><b>→</b><span>好きになる</span><b>→</b><span>また来る</span></div>
    </article>

    <div class="platform-cross"><div>×</div><span>バラバラではなく<br>同時に積み上げる</span></div>

    <article class="platform-card platform-google">
      <div class="platform-top"><span class="platform-badge">GOOGLE</span><span class="platform-mini">SEARCH / MAP</span></div>
      <h3>地域で、見つけてもらう。</h3>
      <p class="platform-sub">Googleマップ・検索・口コミ・最新情報を整え、小金井で探している人の入口をつくります。</p>
      <div class="platform-highlight">地図から消えない仕組みを動かす。</div>
      <ul><li>GoogleやAIに、お店の存在と価値を伝える</li><li>特定のグルメサイトだけに頼らない導線へ</li><li>小金井からの流出を防ぎ、地域への流入をつくる</li><li>広告を止めても残る検索・地図の資産へ</li></ul>
      <div class="platform-flow"><span>検索される</span><b>→</b><span>見つかる</span><b>→</b><span>比較される</span><b>→</b><span>選ばれる</span></div>
    </article>
  </div>

  <div class="dual-platform-summary">
    <div class="dual-summary-main"><span>LOCAL ASSET</span><h3>Instagramで<em>「ファン」</em>をつくる。<br>Googleで<em>「入口」</em>をつくる。</h3><p>両方を育てて、小金井で見つかり、選ばれ、また来てもらえる<strong>事業の資産</strong>へ。</p></div>
    <div class="dual-summary-side"><span>WHY IT MATTERS</span><ul><li>発信と検索をつなげる</li><li>片方だけでは届かない人に届く</li><li>広告を止めても残るストック型資産になる</li><li>小金井で強い自前の情報インフラになる</li></ul></div>
  </div>
</div></section>'''

css = r'''
/* V68 DUAL PLATFORM */
.dual-platform-section{background:radial-gradient(circle at 8% 0%,rgba(199,162,83,.12),transparent 28%),radial-gradient(circle at 94% 14%,rgba(12,139,134,.10),transparent 30%),linear-gradient(180deg,#f8fafc,#f2f5f9);overflow:hidden}
.dual-platform-inner{min-width:0}
.dual-platform-kicker{display:flex;align-items:center;gap:11px;color:#b48635;font-size:.76rem;font-weight:950;letter-spacing:.14em;margin-bottom:16px}.dual-platform-kicker:before{content:"";width:30px;height:2px;background:#c7a253;border-radius:99px}
.dual-platform-head{display:grid;grid-template-columns:minmax(0,1.18fr) minmax(0,.82fr);gap:42px;align-items:end;margin-bottom:34px}.dual-platform-head>*{min-width:0}.dual-platform-head h2{color:var(--navy);font-size:clamp(2.8rem,5.1vw,5rem);line-height:1.04;letter-spacing:-.055em;word-break:keep-all;overflow-wrap:normal}.dual-platform-head p{color:#5d6b80;font-size:1rem;line-height:1.9}.dual-platform-head p strong{color:var(--navy)}
.dual-platform-main{display:grid;grid-template-columns:minmax(0,1fr) 96px minmax(0,1fr);gap:18px;align-items:stretch}.platform-card{min-width:0;padding:30px 28px 27px;border-radius:30px;background:#fff;box-shadow:0 18px 50px rgba(5,25,57,.08);position:relative;overflow:hidden}.platform-instagram{border:1px solid rgba(220,72,115,.18)}.platform-google{border:1px solid rgba(66,133,244,.20)}.platform-card:before{content:"";position:absolute;inset:0 0 auto;height:5px}.platform-instagram:before{background:linear-gradient(90deg,#833ab4,#fd1d1d,#fcb045)}.platform-google:before{background:linear-gradient(90deg,#4285f4,#34a853,#fbbc05)}
.platform-top{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}.platform-badge{display:inline-flex;padding:8px 13px;border-radius:999px;color:#fff;font-size:.68rem;font-weight:950;letter-spacing:.09em}.platform-instagram .platform-badge{background:linear-gradient(135deg,#833ab4,#e1306c,#f77737)}.platform-google .platform-badge{background:linear-gradient(135deg,#4285f4,#34a853)}.platform-mini{color:#8793a5;font-size:.64rem;font-weight:900;letter-spacing:.09em}
.platform-card h3{margin-top:18px;color:var(--navy);font-size:clamp(1.65rem,2.4vw,2.35rem);line-height:1.15;letter-spacing:-.035em}.platform-sub{margin-top:11px;color:#617087;font-size:.92rem;line-height:1.78}.platform-highlight{margin-top:15px;padding:13px 15px;border-radius:16px;font-weight:950;line-height:1.5}.platform-instagram .platform-highlight{background:#fff1f5;color:#b52655}.platform-google .platform-highlight{background:#edf5ff;color:#1459ad}
.platform-card ul{margin:18px 0 0;padding:0;list-style:none;display:grid;gap:8px}.platform-card li{position:relative;padding-left:17px;color:#304560;font-size:.86rem;line-height:1.65}.platform-card li:before{content:"";position:absolute;left:0;top:.68em;width:6px;height:6px;border-radius:50%;background:#c7a253}
.platform-flow{display:flex;align-items:center;flex-wrap:wrap;gap:7px;margin-top:20px;padding-top:17px;border-top:1px dashed #dfe6ee}.platform-flow span{padding:8px 10px;border-radius:999px;background:#f1f4f8;color:#193456;font-size:.72rem;font-weight:900}.platform-flow b{color:#9aabbd;font-size:.78rem}
.platform-cross{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:9px;text-align:center;color:var(--navy)}.platform-cross div{display:grid;place-items:center;width:72px;height:72px;border-radius:50%;background:linear-gradient(145deg,#071d3f,#0c6d75);color:#fff;font-size:1.8rem;font-weight:900;box-shadow:0 14px 32px rgba(5,25,57,.16)}.platform-cross span{font-size:.68rem;line-height:1.55;font-weight:900;color:#63738b}
.dual-platform-summary{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:16px;margin-top:20px}.dual-platform-summary>*{min-width:0}.dual-summary-main{padding:29px 28px;border-radius:28px;background:linear-gradient(135deg,#061a38,#0a3b69 62%,#0a7075);color:#fff;box-shadow:0 20px 50px rgba(5,25,57,.15)}.dual-summary-main>span,.dual-summary-side>span{display:inline-flex;padding:6px 10px;border-radius:999px;font-size:.62rem;font-weight:950;letter-spacing:.1em}.dual-summary-main>span{background:rgba(240,217,149,.14);color:#f0d995}.dual-summary-main h3{margin-top:11px;font-size:clamp(1.8rem,2.8vw,2.8rem);line-height:1.18;letter-spacing:-.04em}.dual-summary-main h3 em{font-style:normal;color:#f0d995}.dual-summary-main p{margin-top:12px;color:rgba(255,255,255,.78);font-size:.9rem;line-height:1.75}.dual-summary-main p strong{color:#fff}.dual-summary-side{padding:27px 25px;border-radius:28px;background:#fff;border:1px solid #dfe6ee}.dual-summary-side>span{background:#eef2f7;color:#193456}.dual-summary-side ul{list-style:none;margin:15px 0 0;padding:0;display:grid;gap:10px}.dual-summary-side li{position:relative;padding-left:17px;color:#40536c;font-size:.86rem;line-height:1.6}.dual-summary-side li:before{content:"";position:absolute;left:0;top:.68em;width:6px;height:6px;border-radius:50%;background:#c7a253}
@media(max-width:1050px){.dual-platform-head{grid-template-columns:1fr}.dual-platform-main{grid-template-columns:1fr}.platform-cross{flex-direction:row}.platform-cross span{text-align:left}.dual-platform-summary{grid-template-columns:1fr}}
@media(max-width:780px){.dual-platform-section{padding:64px 0}.dual-platform-head{gap:18px;margin-bottom:25px}.dual-platform-head h2{font-size:clamp(2rem,9vw,2.65rem);line-height:1.1;letter-spacing:-.045em;word-break:normal;overflow-wrap:anywhere}.dual-platform-head h2 br{display:none}.dual-platform-head p{font-size:.94rem;line-height:1.82}.dual-platform-main{gap:15px}.platform-card{padding:24px 20px;border-radius:24px}.platform-card h3{font-size:1.72rem}.platform-sub{font-size:.9rem}.platform-highlight{font-size:.93rem}.platform-card li{font-size:.84rem}.platform-cross{justify-content:flex-start;padding:2px 4px}.platform-cross div{width:54px;height:54px;font-size:1.35rem}.platform-cross span{font-size:.68rem}.dual-platform-summary{gap:14px}.dual-summary-main,.dual-summary-side{padding:23px 20px;border-radius:23px}.dual-summary-main h3{font-size:1.65rem}.platform-flow{gap:6px}.platform-flow span{font-size:.68rem;padding:7px 9px}}
'''

# Remove old generated component if this script is re-run.
s = re.sub(r'<section class="section dual-platform-section" id="dual-platform">.*?</section>', '', s, count=1, flags=re.S)
s = re.sub(r'/\* V68 DUAL PLATFORM \*/.*?(?=</style>)', '', s, count=1, flags=re.S)

# Insert immediately before the 4-service section.
needle = '<section class="section services" id="services">'
if needle not in s:
    raise SystemExit('Services section not found')
s = s.replace(needle, section + '\n' + needle, 1)

# Keep CSS in the main style block so the section remains clean and responsive.
s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

for token in ['id="dual-platform"', 'INSTAGRAM × GOOGLE', 'Instagramで<em>「ファン」</em>', 'Googleで<em>「入口」</em>', 'V68 DUAL PLATFORM']:
    if token not in s:
        raise SystemExit(f'Missing dual-platform token: {token}')
