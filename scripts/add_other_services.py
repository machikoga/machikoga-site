from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

section = '''<section class="section other-services" id="other-services"><div class="container"><span class="kicker">OTHER SUPPORT</span><h2>講座・セミナー・取材も。<br>小金井の発信なら、何でもご相談ください。</h2><p class="lead other-services-lead">メインの集客支援とは別に、学びたい・伝えたい・広めたいというご相談にも対応しています。</p><div class="other-service-grid"><article class="other-service-card"><div class="other-service-photo"><img src="assets/sns-course.webp" alt="SNS講座の様子"></div><div class="other-service-body"><span class="other-service-tag">SNS COURSE</span><h3>SNS講座</h3><p>Instagram・Google・地域発信を、自分たちで続けられる形に。実践しながら身につける講座です。</p><a class="other-service-link" href="#contact">SNS講座について相談する →</a></div></article><article class="other-service-card"><div class="other-service-photo"><img src="assets/sns-ai-seminar.webp" alt="SNS・AIセミナーの様子"></div><div class="other-service-body"><span class="other-service-tag">SNS × AI SEMINAR</span><h3>SNS・AIセミナー</h3><p>SNS・AI・Google活用などを、地域ビジネスの現場目線でわかりやすく。企業・団体・イベントでの登壇もご相談ください。</p><a class="other-service-link" href="#contact">セミナーについて相談する →</a></div></article><article class="other-service-card other-service-consult"><div class="other-service-consult-visual"><img src="assets/buru-v67.webp" alt="ぶる"></div><div class="other-service-body"><span class="other-service-tag">OPEN CONSULTATION</span><h3>取材・広告・その他</h3><p>取材依頼、広告・PRのご相談、地域イベント、コラボ企画など。内容がまだ固まっていなくても大丈夫です。</p><strong class="other-service-any">何でもご相談ください。</strong><a class="other-service-link" href="#contact">まず相談する →</a></div></article></div></div></section>'''

# Replace if rerun; otherwise insert before ABOUT.
if 'id="other-services"' in s:
    s = re.sub(r'<section class="section other-services" id="other-services">.*?</section>', section, s, count=1, flags=re.S)
else:
    marker = '<section class="section about">'
    if marker in s:
        s = s.replace(marker, section + '\n' + marker, 1)
    else:
        marker = '<section class="section cta" id="contact">'
        if marker not in s:
            raise SystemExit('Could not find insertion point for other services')
        s = s.replace(marker, section + '\n' + marker, 1)

css = r'''
/* V68 OTHER SERVICES */
.other-services{background:linear-gradient(180deg,#f7f9fc 0%,#fff 100%)}
.other-services h2{max-width:13em;color:var(--navy);word-break:keep-all;text-wrap:balance}
.other-services-lead{max-width:820px;margin-top:16px}
.other-service-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:34px;align-items:stretch}
.other-service-card{display:flex;flex-direction:column;min-width:0;background:#fff;border:1px solid var(--line);border-radius:28px;overflow:hidden;box-shadow:0 18px 44px rgba(5,25,57,.09);position:relative}
.other-service-card:before{content:"";position:absolute;inset:0 0 auto;height:5px;background:linear-gradient(90deg,#0b5ea8,#0aa095,#f0d995);z-index:2}
.other-service-photo{aspect-ratio:16/9;overflow:hidden;background:#0b2348}
.other-service-photo img{width:100%;height:100%;object-fit:cover}
.other-service-body{padding:24px 24px 26px;display:flex;flex-direction:column;flex:1;text-align:left}
.other-service-tag{display:inline-flex;align-self:flex-start;padding:6px 10px;border-radius:999px;background:#071d3f;color:#f0d995;font-size:.64rem;font-weight:900;letter-spacing:.09em}
.other-service-body h3{margin-top:14px;color:var(--navy);font-size:1.55rem;line-height:1.25;letter-spacing:-.02em}
.other-service-body p{margin-top:10px;color:var(--text);font-size:.9rem;line-height:1.75}
.other-service-link{margin-top:auto;padding-top:18px;color:#0b6478;font-size:.82rem;font-weight:900}
.other-service-consult{background:linear-gradient(145deg,#061a38,#0a3567 62%,#0a5e68);color:#fff;border-color:rgba(240,217,149,.28)}
.other-service-consult:before{background:linear-gradient(90deg,#f0d995,#c7a253,#40c9bd)}
.other-service-consult-visual{height:180px;display:grid;place-items:center;padding-top:14px}
.other-service-consult-visual img{width:150px;height:150px;object-fit:contain;filter:drop-shadow(0 14px 26px rgba(0,0,0,.22))}
.other-service-consult .other-service-tag{background:rgba(255,255,255,.10);border:1px solid rgba(240,217,149,.28)}
.other-service-consult .other-service-body h3{color:#fff}
.other-service-consult .other-service-body p{color:rgba(255,255,255,.74)}
.other-service-any{display:block;margin-top:14px;color:#f0d995;font-size:1.12rem}
.other-service-consult .other-service-link{color:#fff}
@media(max-width:900px){.other-service-grid{grid-template-columns:1fr 1fr}.other-service-consult{grid-column:1/-1}.other-service-consult{display:grid;grid-template-columns:220px 1fr;align-items:center}.other-service-consult-visual{height:100%}}
@media(max-width:780px){.other-service-grid{grid-template-columns:1fr}.other-service-consult{grid-column:auto;display:flex}.other-service-consult-visual{height:160px}.other-service-body{padding:21px 20px 23px}.other-service-body h3{font-size:1.4rem}}
'''

# Refresh CSS block if rerun.
if '/* V68 OTHER SERVICES */' in s:
    s = re.sub(r'/\* V68 OTHER SERVICES \*/.*?(?=</style>)', css.strip() + '\n', s, count=1, flags=re.S)
else:
    s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

for token in ['SNS講座','SNS・AIセミナー','取材・広告・その他','何でもご相談ください。','assets/sns-course.webp','assets/sns-ai-seminar.webp']:
    if token not in s:
        raise SystemExit(f'Missing other-services token: {token}')
