from pathlib import Path
import re

try:
    from PIL import Image, ImageFilter, ImageChops
except Exception:
    Image = None

HTML = Path('public/index.html')
s = HTML.read_text(encoding='utf-8')

# ============================================================
# 1) HERO MASCOT: remove white fringe and blend into navy.
# ============================================================
if Image is not None:
    candidates = [
        Path('public/assets/buru-hero-transparent.webp'),
        Path('public/assets/buru-v67.webp'),
    ]
    src = next((x for x in candidates if x.exists()), None)
    if src:
        im = Image.open(src).convert('RGBA')
        px = im.load()
        w, h = im.size
        navy = (6, 26, 56)

        # Repaint only semi-transparent bright edge pixels that normally create a white halo.
        for y in range(h):
            for x in range(w):
                r, g, b, a = px[x, y]
                if 0 < a < 245:
                    brightness = (r + g + b) / 3
                    neutral = max(r, g, b) - min(r, g, b) < 85
                    if brightness > 145 and neutral:
                        px[x, y] = (navy[0], navy[1], navy[2], a)

        # Add a subtle 2-3px navy ring behind the alpha edge.
        alpha = im.getchannel('A')
        dilated = alpha.filter(ImageFilter.MaxFilter(7))
        ring = ImageChops.subtract(dilated, alpha)
        ring = ring.point(lambda v: min(205, int(v * 0.9)))
        under = Image.new('RGBA', im.size, navy + (0,))
        under.putalpha(ring)
        out = Image.alpha_composite(under, im)
        out_path = Path('public/assets/buru-hero-navy.webp')
        out.save(out_path, 'WEBP', quality=95, method=6)

s = re.sub(
    r'(<img class="hero-buru" src=")[^"]+(" alt="まちこが ぶる">)',
    r'\1assets/buru-hero-navy.webp?v=20260910-final\2',
    s,
    count=1,
)

# Hero speech bubble: explicit two-line hierarchy.
hero_bubble = '''<div class="hero-bubble"><p class="hero-bubble-main">頑張る量を増やすのではなく、<br><span>今の発信の価値を上げる。</span></p><p class="hero-bubble-sub">小金井で見つかり、選ばれる仕組みを一緒につくります。</p></div>'''
s = re.sub(r'<div class="hero-bubble">.*?</div>', hero_bubble, s, count=1, flags=re.S)

# ============================================================
# 2) EMPATHY: make the CEO-focus message the visual hero.
# ============================================================
buru_tip = '''<aside class="buru-tip buru-tip-final"><img src="assets/buru-v67.webp" alt="ぶる"><div><strong class="focus-message"><span>社長は、</span><em>本業に集中してください。</em></strong><p>投稿を増やすのではなく、今ある発信を「残る資産」に変える仕組みを、ぶるが設計します。</p></div></aside>'''
s = re.sub(r'<aside class="buru-tip">.*?</aside>', buru_tip, s, count=1, flags=re.S)

# ============================================================
# 3) WHY NOW: keep Japanese heading from awkward breaks.
# ============================================================
s = s.replace('<h2>なぜ、今整えるのか。</h2>', '<h2 class="why-balance-title">なぜ、今整えるのか。</h2>')

# ============================================================
# 4) COUNTER AI: make the logic instantly understandable.
# ============================================================
ai_start = s.find('<section class="section ai" id="ai">')
ai_end = s.find('</section>', ai_start)
if ai_start != -1 and ai_end != -1:
    ai_end += len('</section>')
    ai = s[ai_start:ai_end]
    ai = ai.replace(
        'AIはコンテンツを作れても、あなたの店が積み上げてきたものまでは作れません。',
        'AIは文章や画像を作れても、地域で積み上げてきた「本物の価値」までは作れません。'
    )
    contrast = '''<div class="counter-ai-contrast"><div class="ai-can"><span>AIが作れる</span><strong>文章・画像・情報整理</strong></div><div class="ai-vs">VS</div><div class="ai-cannot"><span>AIには作れない</span><strong>地域で積み上げた5つの価値</strong></div></div>'''
    if 'counter-ai-contrast' not in ai:
        ai = ai.replace('<div class="values-grid sales-five">', contrast + '<div class="values-grid sales-five">', 1)

    replacements = {
        '<div class="value-card"><b>土地</b>': '<div class="value-card"><span class="value-no">01</span><b>土地</b>',
        '<div class="value-card"><b>歴史</b>': '<div class="value-card"><span class="value-no">02</span><b>歴史</b>',
        '<div class="value-card"><b>時間・プロセス</b>': '<div class="value-card"><span class="value-no">03</span><b>時間・プロセス</b>',
        '<div class="value-card"><b>思い出</b>': '<div class="value-card"><span class="value-no">04</span><b>思い出</b>',
        '<div class="value-card center"><b>地域とのつながり</b>': '<div class="value-card center"><span class="value-no">05</span><b>地域との<br>つながり</b>',
    }
    for old, new in replacements.items():
        ai = ai.replace(old, new)

    ai = ai.replace(
        '<div class="role-main"><span>価値は、すでにある。</span><span>まちこがは、それを見つかる形にする。</span></div>',
        '<div class="role-main counter-copy"><span>価値は、すでにある。</span><span>まちこがは、それを見つかる形にする。</span></div>'
    )
    s = s[:ai_start] + ai + s[ai_end:]

# ============================================================
# 5) PR POINT 01 / 02: strongest sales section.
# ============================================================
s = s.replace(
    '<h3>小金井で強い、<br>自前の情報インフラ。</h3>',
    '<h3>小金井で強い、<br><span class="core-emphasis core-emphasis-one">自前の情報インフラ。</span></h3>'
)
s = s.replace(
    '<h3>同じ1回の発信を、<br>小金井で数倍強くする。</h3>',
    '<h3>同じ1回の発信を、<br><span class="core-emphasis core-emphasis-two">小金井で数倍強くする。</span></h3>'
)
# Remove duplicate four boxes under POINT 01 only.
s = s.replace('<div class="network-list"><div>Instagram</div><div>Googleマップ</div><div>まちアカ</div><div>ぶる・地域発信</div></div>', '')
s = s.replace('<div class="network-list"><div>Instagram</div><div>Googleマップ</div><div>小金井ポータル</div><div>ぶる・地域発信</div></div>', '')

# ============================================================
# 6) SERVICE WORDING: make Machiaka understandable to first-time visitors.
# ============================================================
s = s.replace('<h3>まちアカ掲載</h3>', '<h3>小金井専用ポータルサイト</h3>')
s = s.replace(
    '小金井の事業者ポータルサイトに掲載。地域名×キーワードの入口を増やし、地域全体で「見つかる力」を積み上げます。',
    '小金井の事業者と一緒に育てる地域情報サイト「まちアカ」に掲載。地域名×業種の検索入口を増やし、小金井で「見つかる力」を積み上げます。'
)
s = s.replace('まちアカ初期設計', '小金井ポータル初期設計')
s = s.replace('<li>まちアカ掲載</li>', '<li>小金井ポータル掲載</li>')

# ============================================================
# 7) PARTNER AUTHORITY: product first, authority visual and compact.
# ============================================================
tools_start = s.find('<section class="section tools')
tools_end = s.find('</section>', tools_start)
if tools_start != -1 and tools_end != -1:
    tools_end += len('</section>')
    tools = s[tools_start:tools_end]
    yokota_start = tools.find('<article class="trio-person compact-person yokota">')
    yokota_end = tools.find('</article>', yokota_start)
    if yokota_start != -1 and yokota_end != -1:
        yokota_end += len('</article>')
        y = tools[yokota_start:yokota_end]
        authority = '''<div class="authority-mini authority-yokota"><span>ドローン日本の第一人者</span><span>世界大会</span><span>万博</span><span>Coca-Cola</span><span>HONDA</span><span>BMW</span><span>NTTデータ</span><span>自治体連携</span></div>'''
        y = re.sub(r'<div class="authority-mini(?: [^"]*)?">.*?</div>', authority, y, count=1, flags=re.S)
        tools = tools[:yokota_start] + y + tools[yokota_end:]
    s = s[:tools_start] + tools + s[tools_end:]

# ============================================================
# 8) PRICING: reference only, order-made service, amounts secondary.
# ============================================================
pricing_html = '''<section class="section pricing pricing-final" id="pricing"><div class="container"><span class="kicker">PRICE GUIDE</span><h2>料金は、事業に合わせて<br>オーダーメイド。</h2><p class="lead pricing-lead">下記は参考価格です。必要な施策・撮影範囲・更新頻度・運用サポートに合わせて、内容も金額も個別にご提案します。</p><div class="custom-note"><strong>まず「何が必要か」を一緒に整理します。</strong><span>全部を入れる必要はありません。今の発信・人員・予算に合わせて組み立てます。</span></div><div class="setup-card setup-card-final"><div><span>INITIAL SETUP / REFERENCE</span><h3>初期設計の参考</h3><p>Googleマップ / Instagram / 小金井ポータルなど、必要な土台をまとめて設計。</p></div><div class="reference-price"><small>参考価格</small><strong>180,000円</strong><span>税込</span></div></div><div class="setup-items setup-items-final"><span>Googleマップ初期設計</span><span>Instagram初期設計</span><span>小金井ポータル</span><span>カスタムAI</span><span>口コミ導線</span><span>掲載ページ制作</span><span>写真・動画・空間3D</span><span>Google連携</span></div><div class="plan-grid plan-grid-final"><article class="plan-card"><span class="plan-label">掲載・地域導線</span><h3><small>参考</small> 9,800円/月</h3><p>まず小金井で見つかる入口を持ちたい場合の一例。</p></article><article class="plan-card featured"><span class="plan-label">スタンダード</span><h3><small>参考</small> 19,800円/月</h3><p>自分で発信しながら、Googleと地域導線を育てる場合の一例。</p></article><article class="plan-card"><span class="plan-label">運用サポート</span><h3><small>参考</small> 59,800円/月</h3><p>日々の更新・投稿までサポートする場合の一例。</p></article></div><div class="price-note price-note-final"><span>※表示金額は参考です。サービス内容・撮影・更新頻度などにより変わります。</span><span>※御社の課題と予算に合わせて、必要なものだけを組み合わせます。</span></div><div class="section-cta"><a class="btn gold" href="#contact">まず必要な内容を相談する</a></div></div></section>'''
s = re.sub(r'<section class="section pricing[^"]*" id="pricing">.*?</section>', pricing_html, s, count=1, flags=re.S)

# ============================================================
# 9) MASTER CSS: hierarchy, alignment, balance, mobile.
# ============================================================
css = r'''
/* V68 FINAL MASTER POLISH */

/* Alignment system: text cards left; identity / metric UI centered only where useful. */
.section-head,.empathy-card,.offer-card,.result-impact,.pricing-final,.setup-card-final,.plan-card{ text-align:left; }
.compact-person{ text-align:center; }
.compact-person .authority-mini{ justify-content:center; }
.role-card,.partner-intro{ text-align:center; }

/* HERO mascot + message */
.hero-buru{filter:drop-shadow(0 0 2px #061a38) drop-shadow(0 18px 34px rgba(0,0,0,.28))!important}
.hero-bubble{max-width:430px!important;padding:21px 24px!important;border-radius:22px!important;background:rgba(7,29,63,.94)!important}
.hero-bubble-main{margin:0!important;font-size:clamp(1.35rem,1.8vw,1.95rem)!important;line-height:1.3!important;font-weight:900!important;letter-spacing:-.025em!important;color:#fff!important}
.hero-bubble-main span{color:#f0d995!important}
.hero-bubble-sub{margin:9px 0 0!important;font-size:.92rem!important;line-height:1.65!important;color:rgba(255,255,255,.78)!important}

/* EMPATHY: make the core owner benefit impossible to miss */
.empathy-grid{grid-template-columns:.82fr 1.18fr!important;gap:20px!important;align-items:stretch!important}
.buru-tip-final{padding:34px 34px!important;grid-template-columns:120px 1fr!important;background:linear-gradient(135deg,#061a38 0%,#0a3567 62%,#0a5e68 100%)!important;border:1px solid rgba(240,217,149,.24)!important}
.buru-tip-final img{width:120px!important;height:120px!important}
.focus-message{display:block!important;line-height:1.02!important;letter-spacing:-.045em!important}
.focus-message span{display:block!important;color:#fff!important;font-size:clamp(1.55rem,2.2vw,2.4rem)!important}
.focus-message em{display:block!important;margin-top:4px!important;color:#f0d995!important;font-size:clamp(2.35rem,4.1vw,4.4rem)!important;font-style:normal!important;font-weight:900!important}
.buru-tip-final p{margin-top:16px!important;color:rgba(255,255,255,.80)!important;font-size:1rem!important;line-height:1.8!important}

/* WHY NOW */
.why .section-head{grid-template-columns:minmax(500px,1.15fr) minmax(300px,.75fr)!important;gap:32px!important}
.why-balance-title{max-width:none!important;word-break:keep-all!important;overflow-wrap:normal!important;text-wrap:balance!important;font-size:clamp(3rem,5.1vw,4.9rem)!important;line-height:1.02!important}
.why-grid{gap:18px!important}.why-card{padding:28px 26px 24px!important;border-radius:26px!important;background:linear-gradient(180deg,#fff,#f8fbff)!important;box-shadow:0 14px 34px rgba(6,26,56,.07)!important}
.why-card .mark{width:90px!important;height:90px!important;border-radius:26px!important;margin-bottom:20px!important;font-size:1.75rem!important;box-shadow:0 16px 32px rgba(6,26,56,.16)!important}
.why-grid .why-card:nth-child(1) .mark{background:linear-gradient(135deg,#123d7b,#266fca)!important}.why-grid .why-card:nth-child(2) .mark{background:linear-gradient(135deg,#0b607d,#11a9a3)!important}.why-grid .why-card:nth-child(3) .mark{background:linear-gradient(135deg,#8e6220,#d4a948)!important}
.why-card h3{font-size:1.45rem!important;line-height:1.35!important}.why-card p{font-size:.94rem!important;line-height:1.75!important}.why-card .small{font-size:.82rem!important}

/* COUNTER AI: logic first, five values second */
.ai{background:radial-gradient(circle at 10% 8%,rgba(240,217,149,.18),transparent 24%),radial-gradient(circle at 90% 20%,rgba(12,139,134,.18),transparent 30%),linear-gradient(145deg,#031735,#082b5f 55%,#0b4769)!important}
.ai .section-head{grid-template-columns:1.15fr .75fr!important;gap:34px!important}.ai .section-head h2{max-width:none!important;word-break:keep-all!important;text-wrap:balance!important}.ai .section-head .lead{font-size:1.05rem!important;line-height:1.85!important}
.counter-ai-contrast{display:grid;grid-template-columns:1fr auto 1fr;gap:14px;align-items:center;margin:30px 0 22px}.counter-ai-contrast>div:not(.ai-vs){padding:18px 20px;border-radius:20px}.ai-can{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.13)}.ai-cannot{background:linear-gradient(135deg,#fffaf0,#fff);border:1px solid rgba(240,217,149,.65);color:#071d3f}.counter-ai-contrast span{display:block;font-size:.68rem;font-weight:900;letter-spacing:.08em;color:#f0d995}.ai-cannot span{color:#9b6a26}.counter-ai-contrast strong{display:block;margin-top:5px;font-size:1.25rem}.ai-vs{color:#f0d995;font-size:1.05rem;font-weight:900}
.sales-five{grid-template-columns:repeat(5,1fr)!important;gap:12px!important}.sales-five .value-card{min-height:158px!important;padding:20px 18px!important}.sales-five .value-card:before{display:none!important}.value-no{display:inline-grid;place-items:center;width:36px;height:36px;margin-bottom:14px;border-radius:12px;background:rgba(240,217,149,.14);border:1px solid rgba(240,217,149,.28);color:#f0d995;font-size:.68rem;font-weight:900}.sales-five .value-card b{font-size:1.33rem!important}.sales-five .value-card span:not(.value-no){font-size:.84rem!important}.sales-five .value-card.center{transform:none!important}.sales-five .value-card.center .value-no{background:#071d3f;color:#f0d995;border:0}.sales-five .value-card.center b{font-size:1.25rem!important;line-height:1.3!important}
.role-card{margin-top:22px!important;padding:34px 30px!important}.counter-copy span:first-child{font-size:clamp(2.25rem,3.8vw,4.2rem)!important}.counter-copy span:last-child{font-size:clamp(1.85rem,3.1vw,3.4rem)!important}

/* PR POINTS: same family, POINT 01 clearly primary */
.core-grid{grid-template-columns:1.06fr .94fr!important;gap:20px!important;align-items:stretch!important}.core-card{min-height:100%!important}
.core-card.one.core-primary{background:radial-gradient(circle at 95% 0%,rgba(12,139,134,.30),transparent 34%),linear-gradient(145deg,#061a38,#0a3970 58%,#096d73)!important;color:#fff!important;border:3px solid rgba(240,217,149,.82)!important;box-shadow:0 28px 68px rgba(6,26,56,.24)!important;transform:none!important}.core-card.one.core-primary:before{height:7px!important;background:linear-gradient(90deg,#f0d995,#c7a253,#35c4b9)!important}.core-card.one.core-primary .core-label{background:#f0d995!important;color:#061a38!important}.core-card.one.core-primary h3{color:#fff!important}.core-card.one.core-primary p{color:rgba(255,255,255,.82)!important}.core-card.one.core-primary .asset-note{margin-top:22px!important;background:rgba(3,16,38,.62)!important;border:1px solid rgba(255,255,255,.12)!important}.core-card.one.core-primary .asset-note b{color:#f0d995!important}.core-emphasis-one{color:#f7dc87!important}.core-emphasis-one:after{background:linear-gradient(90deg,#f0d995,#4ad1c6)!important;opacity:.95!important}
.core-card.two{background:linear-gradient(145deg,#082d5a,#0b6d74)!important;color:#fff!important;border:1px solid rgba(89,205,196,.45)!important;box-shadow:0 22px 52px rgba(6,26,56,.16)!important}.core-card.two:before{height:7px!important;background:linear-gradient(90deg,#1aa8a1,#62d4ca)!important}.core-card.two .core-label{background:#0b3d70!important;color:#fff!important}.core-card.two h3,.core-card.two .bigline{color:#fff!important}.core-card.two p{color:rgba(255,255,255,.82)!important}.core-card.two .one-post{background:rgba(255,255,255,.10)!important;border:1px solid rgba(255,255,255,.12)!important}.core-card.two .branch{background:rgba(255,255,255,.13)!important;color:#fff!important}.core-emphasis-two{color:#7ee2d8!important}.core-emphasis-two:after{background:#7ee2d8!important;opacity:.28!important}

/* Service cards */
.offer-card h3{font-size:1.28rem!important;line-height:1.35!important}.offer-card p{font-size:.86rem!important;line-height:1.72!important}.offer-card b{font-size:.76rem!important}.offer-no{width:44px!important;height:44px!important}

/* Partner chips: authority without taking over the product */
.authority-yokota{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:7px!important}.authority-yokota span{border-radius:13px!important;padding:8px 9px!important;white-space:normal!important}.compact-person{padding:20px 17px!important}.compact-person .trio-photo{width:108px!important;height:108px!important}.compact-person h3{font-size:1.35rem!important}.compact-person>strong{font-size:.86rem!important}

/* Results: smaller cards, larger outcomes */
.results-highlight{gap:12px!important}.result-impact{padding:19px 18px 18px!important;border-radius:20px!important;min-height:178px!important;display:flex!important;flex-direction:column!important;align-items:flex-start!important}.result-type{font-size:.64rem!important}.result-impact small{margin-top:10px!important;font-size:.76rem!important}.result-impact>strong{margin-top:7px!important;font-size:clamp(1.55rem,2.25vw,2.15rem)!important;line-height:1.16!important;letter-spacing:-.03em!important}.result-impact p{font-size:.78rem!important;margin-top:7px!important}.result-row{padding:11px 14px!important}.result-row strong{font-size:.84rem!important}

/* Pricing: reference / custom, numbers secondary */
.pricing-final{background:linear-gradient(145deg,#061a38,#0a315e)!important}.pricing-final h2{font-size:clamp(2.35rem,4.6vw,4.5rem)!important}.pricing-lead{max-width:850px!important;color:rgba(255,255,255,.82)!important}.custom-note{display:flex;align-items:center;justify-content:space-between;gap:22px;margin-top:24px;padding:18px 20px;border-radius:20px;background:rgba(240,217,149,.10);border:1px solid rgba(240,217,149,.24)}.custom-note strong{font-size:1.05rem;color:#f0d995}.custom-note span{font-size:.8rem;color:rgba(255,255,255,.72)}.setup-card-final{margin-top:18px!important;padding:20px 22px!important}.setup-card-final h3{font-size:1.35rem!important}.reference-price{text-align:right}.reference-price small{display:block;color:#9b6a26;font-size:.65rem;font-weight:900}.reference-price strong{display:block;font-size:1.45rem!important;line-height:1.25}.reference-price span{font-size:.68rem;color:#6b778b}.setup-items-final{margin-top:10px!important}.setup-items-final span{font-size:.65rem!important;padding:6px 9px!important}.plan-grid-final{margin-top:18px!important}.plan-grid-final .plan-card{padding:20px!important}.plan-grid-final .plan-card.featured{transform:none!important}.plan-grid-final .plan-card h3{font-size:1.25rem!important}.plan-grid-final .plan-card h3 small{font-size:.64rem!important;color:#9b6a26}.plan-grid-final .plan-card p{font-size:.76rem!important;line-height:1.65!important}.price-note-final{font-size:.68rem!important;margin-top:14px!important}

@media(max-width:1050px){.empathy-grid{grid-template-columns:1fr!important}.core-grid{grid-template-columns:1fr!important}.why .section-head,.ai .section-head{grid-template-columns:1fr!important}.sales-five{grid-template-columns:repeat(3,1fr)!important}.counter-ai-contrast{grid-template-columns:1fr!important}.ai-vs{text-align:center}}
@media(max-width:780px){.hero-bubble{max-width:100%!important}.hero-bubble-main{font-size:1.18rem!important}.empathy-card{padding:24px!important}.buru-tip-final{grid-template-columns:84px 1fr!important;padding:22px 18px!important}.buru-tip-final img{width:84px!important;height:84px!important}.focus-message span{font-size:1.2rem!important}.focus-message em{font-size:clamp(1.9rem,8.5vw,2.8rem)!important}.why-balance-title{font-size:clamp(2.35rem,10vw,3.5rem)!important}.why-card .mark{width:72px!important;height:72px!important}.sales-five{grid-template-columns:1fr 1fr!important}.core-card{padding:25px 21px!important}.authority-yokota{grid-template-columns:1fr 1fr!important}.results-highlight{grid-template-columns:1fr!important}.result-impact{min-height:auto!important}.custom-note{align-items:flex-start;flex-direction:column}.setup-card-final{align-items:flex-start!important;flex-direction:column!important}.reference-price{text-align:left}.plan-grid-final{grid-template-columns:1fr!important}}
@media(max-width:430px){.sales-five{grid-template-columns:1fr!important}.authority-yokota{grid-template-columns:1fr!important}.buru-tip-final{grid-template-columns:1fr!important}.buru-tip-final img{margin:0!important}}
'''

marker = '/* V68 FINAL MASTER POLISH */'
if marker in s:
    s = re.sub(r'/\* V68 FINAL MASTER POLISH \*/.*?(?=</style>)', css.strip() + '\n', s, count=1, flags=re.S)
else:
    s = s.replace('</style>', css + '\n</style>', 1)

HTML.write_text(s, encoding='utf-8')

required = [
    'buru-hero-navy.webp?v=20260910-final',
    'focus-message',
    'counter-ai-contrast',
    'core-emphasis-one',
    '小金井専用ポータルサイト',
    'Coca-Cola', 'HONDA', 'BMW', 'NTTデータ',
    '参考価格です',
    'V68 FINAL MASTER POLISH',
]
for item in required:
    if item not in s:
        raise SystemExit(f'Missing final master item: {item}')
