from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

section = r'''<section class="section dual-platform-section" id="dual-platform"><div class="container dual-platform-inner">
  <div class="dual-platform-kicker">INSTAGRAM × GOOGLE</div>
  <div class="dual-platform-head dual-simple-head">
    <h2>InstagramとGoogle。<br>両方を、同時に育てる。</h2>
    <p>役割は違う。でも、<strong>片方だけでは弱い。</strong><br>ぶるは初期設計から運用方法まで、一緒に整えます。</p>
  </div>

  <div class="dual-simple-stack">
    <article class="dual-simple-card dual-simple-instagram">
      <div class="dual-simple-icon">Instagram</div>
      <div class="dual-simple-copy">
        <span>FAN / REPEAT</span>
        <h3>地域で、好きになってもらう。</h3>
        <ul>
          <li>楽しく、無理なく、みんなで続ける</li>
          <li>小金井に強い発信力を育てる</li>
          <li>自前の情報発信インフラをつくる</li>
        </ul>
      </div>
    </article>

    <div class="dual-simple-plus">＋</div>

    <article class="dual-simple-card dual-simple-google">
      <div class="dual-simple-icon">Google</div>
      <div class="dual-simple-copy">
        <span>SEARCH / MAP</span>
        <h3>地域で、見つけてもらう。</h3>
        <ul>
          <li>Google・AIにじわじわ認知させる</li>
          <li>地図から消えない検索資産を育てる</li>
          <li>グルメサイト頼みから抜け出す</li>
        </ul>
      </div>
    </article>
  </div>

  <div class="dual-simple-result">
    <span>THE POINT</span>
    <h3>Instagramで<strong>「ファン」</strong>をつくる。<br>Googleで<strong>「入口」</strong>をつくる。</h3>
    <p>両方を育てて、<b>小金井で圧倒的に強い自前の発信力</b>をつくる。</p>
  </div>
</div></section>'''

css = r'''
/* V74 DUAL PLATFORM SIMPLE */
.dual-platform-section{background:linear-gradient(180deg,#f8fafc,#f2f5f9);overflow:hidden}
.dual-platform-kicker{display:flex;align-items:center;gap:11px;color:#b48635;font-size:.76rem;font-weight:950;letter-spacing:.14em;margin-bottom:16px}.dual-platform-kicker:before{content:"";width:30px;height:2px;background:#c7a253;border-radius:99px}
.dual-simple-head{display:grid;grid-template-columns:1.12fr .88fr;gap:40px;align-items:end;margin-bottom:30px}
.dual-simple-head h2{color:var(--navy);font-size:clamp(2.8rem,5vw,4.9rem);line-height:1.03;letter-spacing:-.055em}
.dual-simple-head p{color:#5d6b80;font-size:1rem;line-height:1.85}.dual-simple-head p strong{color:var(--navy)}
.dual-simple-stack{display:grid;gap:14px}
.dual-simple-card{display:grid;grid-template-columns:190px 1fr;gap:26px;align-items:center;padding:28px;border-radius:28px;background:#fff;box-shadow:0 16px 40px rgba(5,25,57,.07);border:1px solid #dfe6ee}
.dual-simple-instagram{border-left:6px solid #d84673}.dual-simple-google{border-left:6px solid #4285f4}
.dual-simple-icon{height:118px;border-radius:22px;display:grid;place-items:center;color:#fff;font-size:1.25rem;font-weight:950;letter-spacing:-.02em}
.dual-simple-instagram .dual-simple-icon{background:linear-gradient(135deg,#833ab4,#e1306c,#f77737)}
.dual-simple-google .dual-simple-icon{background:linear-gradient(135deg,#4285f4,#34a853)}
.dual-simple-copy>span{display:block;color:#8a96a8;font-size:.68rem;font-weight:900;letter-spacing:.12em}
.dual-simple-copy h3{margin:7px 0 0;color:var(--navy);font-size:clamp(1.65rem,2.5vw,2.35rem);line-height:1.15}
.dual-simple-copy ul{margin:15px 0 0;padding:0;list-style:none;display:grid;gap:8px}
.dual-simple-copy li{position:relative;padding-left:19px;color:#40536c;font-size:.92rem;line-height:1.6}
.dual-simple-copy li:before{content:"✓";position:absolute;left:0;top:0;color:#b48635;font-weight:900}
.dual-simple-plus{text-align:center;color:var(--navy);font-size:2.3rem;font-weight:900;line-height:1}
.dual-simple-result{margin-top:20px;padding:30px;border-radius:28px;background:linear-gradient(135deg,#061a38,#0a3567);color:#fff;text-align:center}
.dual-simple-result>span{display:inline-flex;padding:6px 10px;border-radius:999px;border:1px solid rgba(240,217,149,.35);color:#f0d995;font-size:.65rem;font-weight:900;letter-spacing:.1em}
.dual-simple-result h3{margin:12px 0 0;color:#fff;font-size:clamp(1.9rem,3.5vw,3.2rem);line-height:1.15}
.dual-simple-result h3 strong{color:#f0d995}
.dual-simple-result p{margin:11px 0 0;color:rgba(255,255,255,.78);font-size:1rem}.dual-simple-result p b{color:#fff}
@media(max-width:900px){.dual-simple-head{grid-template-columns:1fr}.dual-simple-card{grid-template-columns:1fr}.dual-simple-icon{height:84px}}
@media(max-width:780px){.dual-platform-section{padding:64px 0}.dual-simple-head{gap:16px;margin-bottom:24px}.dual-simple-head h2{font-size:clamp(2rem,9vw,2.8rem);line-height:1.08}.dual-simple-head h2 br{display:none}.dual-simple-head p{font-size:.94rem}.dual-simple-card{padding:22px 18px;border-radius:24px;gap:18px}.dual-simple-copy h3{font-size:1.7rem}.dual-simple-result{padding:24px 18px}.dual-simple-result h3{font-size:1.7rem}}
'''

# Remove old generated component if this script is re-run.
s = re.sub(r'<section class="section dual-platform-section" id="dual-platform">.*?</section>', '', s, count=1, flags=re.S)
s = re.sub(r'/\* V68 DUAL PLATFORM \*/.*?(?=</style>)', '', s, count=1, flags=re.S)

# Insert immediately before the 4-service section, regardless of later visual classes.
m = re.search(r'<section class="section services[^"]*" id="services">', s)
if not m:
    raise SystemExit('Services section not found')
s = s[:m.start()] + section + '\n' + s[m.start():]

# Keep CSS in the main style block so the section remains clean and responsive.
s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

for token in ['id="dual-platform"', 'INSTAGRAM × GOOGLE', '地域で、好きになってもらう。', '地域で、見つけてもらう。', '小金井で圧倒的に強い自前の発信力', 'V74 DUAL PLATFORM SIMPLE']:
    if token not in s:
        raise SystemExit(f'Missing dual-platform token: {token}')
