from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

# -----------------------------------------------------------------------------
# 1) Public-facing terminology: explain the function, not the internal brand name.
# -----------------------------------------------------------------------------
s = s.replace('小金井専用ポータルサイト', '小金井ポータル')
s = s.replace('まちアカ', '小金井ポータル')

# Fold the strongest fan idea into the Instagram explanation so the standalone
# community section can be removed without losing the message.
s = s.replace(
    '楽しく、無理なく続けながら、小金井に強い発信力を育てます。',
    '1万人にバズるより、地域の100人に「また来たい」と思ってもらう。楽しく、無理なく、小金井に強い発信力を育てます。'
)

# -----------------------------------------------------------------------------
# 2) Reduce duplicated full sections.
#    - FAN/REPEAT is now inside the Instagram × Google section.
#    - Daily tasks become a compact block inside Services.
# -----------------------------------------------------------------------------
s = re.sub(r'<section class="section easy" id="easy">.*?</section>', '', s, count=1, flags=re.S)
s = re.sub(r'<section class="section community" id="community">.*?</section>', '', s, count=1, flags=re.S)

# Remove an old generated compact block if rerun.
s = re.sub(r'<div class="client-role-strip">.*?</div>\s*(?=</div></section>)', '', s, count=1, flags=re.S)

client_role = r'''
<div class="client-role-strip">
  <div class="client-role-copy">
    <span>YOUR PART</span>
    <h3>日々やることは、基本3つだけ。</h3>
    <p>仕組みはまちこがが設計。日々の運用は、無理なく続けられる形に絞ります。</p>
  </div>
  <div class="client-role-pills">
    <div><b>01</b><span>1日2分の<br>Google投稿</span></div>
    <div><b>02</b><span>口コミ依頼<br>＆ 返信</span></div>
    <div><b>03</b><span>ストーリーズ<br>投稿</span></div>
  </div>
</div>'''

m = re.search(r'(<section class="section services" id="services">.*?)(</div></section>)', s, re.S)
if not m:
    raise SystemExit('Services section not found for compact client role')
services_body = m.group(1)
if 'client-role-strip' not in services_body:
    services_body = services_body + client_role
s = s[:m.start()] + services_body + m.group(2) + s[m.end():]

# -----------------------------------------------------------------------------
# 3) Desktop + mobile navigation.
# -----------------------------------------------------------------------------
nav_html = (
    '<nav class="nav" aria-label="メインメニュー">'
    '<a href="#why">特徴</a>'
    '<a href="#infra">仕組み</a>'
    '<a href="#services">サービス</a>'
    '<a href="#results">実績</a>'
    '<a href="#pricing">料金</a>'
    '<a class="btn gold" href="#contact">無料相談</a>'
    '</nav>'
    '<button class="menu-toggle" id="menuToggle" type="button" aria-label="メニューを開く" aria-controls="mobileMenu" aria-expanded="false">'
    '<span></span><span></span><span></span>'
    '</button>'
)

# Replace nav + any prior generated toggle.
s = re.sub(
    r'<nav class="nav"[^>]*>.*?</nav>(?:<button class="menu-toggle".*?</button>)?',
    nav_html,
    s,
    count=1,
    flags=re.S,
)

# Remove prior generated mobile menu/backdrop if rerun.
s = re.sub(r'<div class="menu-backdrop" id="menuBackdrop".*?</div>', '', s, count=1, flags=re.S)
s = re.sub(r'<aside class="mobile-menu-panel" id="mobileMenu".*?</aside>', '', s, count=1, flags=re.S)

mobile_menu = r'''
<div class="menu-backdrop" id="menuBackdrop" aria-hidden="true"></div>
<aside class="mobile-menu-panel" id="mobileMenu" aria-hidden="true" aria-label="スマホメニュー">
  <div class="mobile-menu-label">MENU</div>
  <a href="#why"><span>01</span><b>特徴</b></a>
  <a href="#infra"><span>02</span><b>仕組み</b></a>
  <a href="#services"><span>03</span><b>サービス</b></a>
  <a href="#results"><span>04</span><b>実績</b></a>
  <a href="#pricing"><span>05</span><b>料金</b></a>
  <a class="mobile-menu-cta" href="#contact"><b>無料相談する</b><i>→</i></a>
</aside>
'''

header_end = '</header>'
if header_end not in s:
    raise SystemExit('Header end not found')
s = s.replace(header_end, header_end + mobile_menu, 1)

# -----------------------------------------------------------------------------
# 4) CSS: compact, premium menu + compact service operation block.
# -----------------------------------------------------------------------------
css = r'''
/* V68 FINAL STRUCTURE + MENU */
.menu-toggle{display:none;width:46px;height:46px;border:1px solid rgba(255,255,255,.18);border-radius:15px;background:rgba(255,255,255,.08);padding:0;align-items:center;justify-content:center;flex-direction:column;gap:5px;cursor:pointer}
.menu-toggle span{display:block;width:20px;height:2px;border-radius:99px;background:#fff;transition:.22s ease}
.menu-toggle[aria-expanded="true"] span:nth-child(1){transform:translateY(7px) rotate(45deg)}
.menu-toggle[aria-expanded="true"] span:nth-child(2){opacity:0}
.menu-toggle[aria-expanded="true"] span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
.menu-backdrop{position:fixed;inset:0;z-index:180;background:rgba(2,12,30,.56);backdrop-filter:blur(5px);opacity:0;pointer-events:none;transition:.22s ease}
.mobile-menu-panel{position:fixed;z-index:190;top:74px;left:14px;right:14px;padding:16px;border-radius:24px;background:linear-gradient(145deg,#061a38,#0a315e);border:1px solid rgba(240,217,149,.22);box-shadow:0 24px 70px rgba(2,12,30,.32);transform:translateY(-14px) scale(.985);opacity:0;pointer-events:none;transition:.24s ease}
.mobile-menu-label{padding:4px 8px 12px;color:#f0d995;font-size:.66rem;font-weight:900;letter-spacing:.16em}
.mobile-menu-panel>a{display:flex;align-items:center;gap:14px;min-height:52px;padding:0 12px;border-top:1px solid rgba(255,255,255,.09);color:#fff}
.mobile-menu-panel>a span{display:grid;place-items:center;width:29px;height:29px;border-radius:10px;background:rgba(240,217,149,.10);color:#f0d995;font-size:.62rem;font-weight:900}
.mobile-menu-panel>a b{font-size:.94rem}
.mobile-menu-panel .mobile-menu-cta{margin-top:10px;min-height:54px;border:0;border-radius:18px;background:linear-gradient(135deg,#d2af62,#9b6a26);justify-content:space-between;padding:0 18px}
.mobile-menu-panel .mobile-menu-cta i{font-style:normal;font-size:1.2rem}
body.menu-open .menu-backdrop{opacity:1;pointer-events:auto}
body.menu-open .mobile-menu-panel{opacity:1;pointer-events:auto;transform:none}
body.menu-open{overflow:hidden}

.client-role-strip{margin-top:18px;padding:22px 24px;border-radius:24px;background:linear-gradient(135deg,#071d3f,#0a4663);color:#fff;display:grid;grid-template-columns:minmax(0,.88fr) minmax(0,1.12fr);gap:22px;align-items:center;box-shadow:0 18px 44px rgba(5,25,57,.12)}
.client-role-copy>span{display:inline-flex;padding:5px 9px;border-radius:999px;background:rgba(240,217,149,.13);border:1px solid rgba(240,217,149,.26);color:#f0d995;font-size:.62rem;font-weight:900;letter-spacing:.12em}
.client-role-copy h3{margin-top:9px;color:#fff;font-size:clamp(1.45rem,2.2vw,2rem);line-height:1.2;letter-spacing:-.03em}
.client-role-copy p{margin-top:8px;color:rgba(255,255,255,.72);font-size:.82rem;line-height:1.7}
.client-role-pills{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:9px}
.client-role-pills div{min-width:0;padding:14px 12px;border-radius:17px;background:rgba(255,255,255,.09);border:1px solid rgba(255,255,255,.10);display:grid;grid-template-columns:30px 1fr;gap:9px;align-items:center}
.client-role-pills b{display:grid;place-items:center;width:30px;height:30px;border-radius:10px;background:rgba(240,217,149,.13);color:#f0d995;font-size:.64rem}
.client-role-pills span{color:#fff;font-size:.78rem;font-weight:850;line-height:1.45}

@media(max-width:780px){
  .header-in{gap:10px}
  .menu-toggle{display:flex;flex:0 0 auto}
  .mobile-menu-panel{top:72px}
  .client-role-strip{grid-template-columns:1fr;padding:20px;border-radius:22px;gap:16px}
  .client-role-pills{grid-template-columns:1fr 1fr 1fr;gap:7px}
  .client-role-pills div{display:flex;flex-direction:column;align-items:flex-start;gap:8px;padding:12px 10px}
  .client-role-pills span{font-size:.72rem}
}
@media(max-width:430px){
  .brand small{font-size:.62rem}
  .client-role-pills{grid-template-columns:1fr}
  .client-role-pills div{flex-direction:row;align-items:center}
  .client-role-pills span br{display:none}
}
'''

s = re.sub(r'/\* V68 FINAL STRUCTURE \+ MENU \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = s.replace('</style>', css + '\n</style>', 1)

# -----------------------------------------------------------------------------
# 5) JS for mobile menu (idempotent).
# -----------------------------------------------------------------------------
s = re.sub(r'<script id="mobileMenuScript">.*?</script>', '', s, count=1, flags=re.S)
js = r'''
<script id="mobileMenuScript">
(() => {
  const button = document.getElementById('menuToggle');
  const panel = document.getElementById('mobileMenu');
  const backdrop = document.getElementById('menuBackdrop');
  if (!button || !panel || !backdrop) return;
  const setOpen = (open) => {
    document.body.classList.toggle('menu-open', open);
    button.setAttribute('aria-expanded', String(open));
    button.setAttribute('aria-label', open ? 'メニューを閉じる' : 'メニューを開く');
    panel.setAttribute('aria-hidden', String(!open));
    backdrop.setAttribute('aria-hidden', String(!open));
  };
  button.addEventListener('click', () => setOpen(button.getAttribute('aria-expanded') !== 'true'));
  backdrop.addEventListener('click', () => setOpen(false));
  panel.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setOpen(false)));
  document.addEventListener('keydown', e => { if (e.key === 'Escape') setOpen(false); });
})();
</script>
'''
s = s.replace('</body>', js + '\n</body>', 1)

p.write_text(s, encoding='utf-8')

checks = [
    '小金井ポータル',
    'id="menuToggle"',
    'id="mobileMenu"',
    'client-role-strip',
    'href="#why">特徴',
    'V68 FINAL STRUCTURE + MENU',
]
for token in checks:
    if token not in s:
        raise SystemExit(f'Missing final structure token: {token}')
if 'id="community"' in s or 'id="easy"' in s:
    raise SystemExit('Duplicate standalone sections still present')
if '>まちアカ<' in s:
    raise SystemExit('Old visible machiaka label still present')
