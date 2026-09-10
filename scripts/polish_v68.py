from pathlib import Path
from collections import deque
from PIL import Image
import re

# --- Generate transparent hero mascot from existing artwork ---
src = Path('public/assets/buru-v67.webp')
dst = Path('public/assets/buru-hero-transparent.webp')
im = Image.open(src).convert('RGBA')
px = im.load()
w, h = im.size

def is_bg(x, y):
    r, g, b, a = px[x, y]
    return a == 0 or (r >= 210 and g >= 210 and b >= 210)

q = deque()
seen = set()
for x in range(w):
    for y in (0, h - 1):
        if is_bg(x, y):
            q.append((x, y))
            seen.add((x, y))
for y in range(h):
    for x in (0, w - 1):
        if is_bg(x, y):
            q.append((x, y))
            seen.add((x, y))

while q:
    x, y = q.popleft()
    r, g, b, a = px[x, y]
    px[x, y] = (r, g, b, 0)
    for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
        if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in seen and is_bg(nx, ny):
            seen.add((nx, ny))
            q.append((nx, ny))

bbox = im.getbbox()
if bbox:
    l, t, r, b = bbox
    pad = 10
    l = max(0, l - pad)
    t = max(0, t - pad)
    r = min(w, r + pad)
    b = min(h, b + pad)
    im = im.crop((l, t, r, b))
im.save(dst, 'WEBP', quality=88, method=6)

# --- Patch HTML ---
p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

# Stable image refs
s = re.sub(r'assets/partners/suzuki\.webp\?v=[0-9-]+', 'assets/partners/suzuki.webp?v=20260910-8', s)
s = re.sub(
    r'(<img class="hero-buru" src=")[^"]+(" alt="まちこが ぶる">)',
    r'\1assets/buru-hero-transparent.webp?v=20260910-1\2',
    s,
    count=1,
)
s = re.sub(
    r'\.hero-buru\{width:min\(380px,92%\);height:430px;[^}]*\}',
    '.hero-buru{width:min(380px,92%);height:430px;object-fit:contain;object-position:center center;border-radius:0;border:0;background:transparent;box-shadow:none}',
    s,
    count=1,
)
s = re.sub(
    r'\.hero-buru\{width:210px;height:245px;[^}]*\}',
    '.hero-buru{width:210px;height:245px;border-radius:0;object-fit:contain;background:transparent;border:0;box-shadow:none}',
    s,
    count=1,
)

# Brand acronym
s = s.replace('BURU', 'BUL')

# Hero / navigation clarity
s = s.replace('>実例を見る<', '>実績・事例を見る<')
s = s.replace('>今やらないと？<', '>なぜ今？<')

# Make PR POINT 01 visually primary; keep POINT 02 supportive.
s = re.sub(
    r'\.pr-card\.one\{[^}]*\}',
    '.pr-card.one{background:linear-gradient(135deg,#0b5ea8,#0aa095);border:2px solid rgba(240,217,149,.78);box-shadow:0 16px 36px rgba(12,139,134,.28)}',
    s,
    count=1,
)
s = re.sub(
    r'\.pr-card\.two\{[^}]*\}',
    '.pr-card.two{background:linear-gradient(135deg,rgba(89,67,35,.92),rgba(143,105,42,.90))}',
    s,
    count=1,
)
if '.pr-card.one .label{color:#fff1b8}' not in s:
    s = s.replace('.pr-card .label{font-size:.68rem;font-weight:900;letter-spacing:.12em;color:#fff}', '.pr-card .label{font-size:.68rem;font-weight:900;letter-spacing:.12em;color:#fff}.pr-card.one .label{color:#fff1b8}.pr-card.one strong{font-size:1.36rem}')

# WHY NOW copy polish
replacements = {
    '今やらないと、どうなる？': 'なぜ、今整えるのか。',
    'お店の価値が落ちるのではありません。<strong>見つけられ方の差</strong>で、静かに周辺地域や競合へ流れていきます。': 'お店の価値ではなく、<strong>見つけられ方</strong>で差がつく時代です。SNS・Google・地域発信をつなぎ、選ばれる入口を整えます。',
    'AIに認識されにくくなる': 'AIに伝わる情報を増やす',
    'SNS・Google・写真・更新情報が少ないと、AIが街や事業を理解する材料が不足します。': 'SNS・Google・写真・更新情報をつなぐと、AIが事業の特徴を理解しやすくなります。',
    '情報が薄い → 候補に入りにくい': '情報を整える → 候補に入りやすくなる',
    'Googleで先に見つかる店へ': 'Googleで、先に見つかる店へ',
    '検索・地図・口コミ・写真が整っている店は、比較のスタート地点から有利です。': '検索・地図・口コミ・写真が整っているほど、比較のスタート地点に立ちやすくなります。',
    '見つからない → 良さを知る前に離脱': '見つかる → 良さを知ってもらえる',
    '周辺地域へ静かに流れる': '地域の中で選ばれる土台をつくる',
    '発信が強い地域・店舗が先に候補になると、地元のお客様も自然にそちらへ動きます。': '発信・検索・口コミがつながると、小金井の中で見つかり、選ばれる理由が積み上がります。',
    '良い店でも、「先に見つかる場所」に人は流れる。': '良い店だからこそ、見つかる仕組みまで整える。',
    'AI・Googleの変化に合わせ、検索・地図・SNSの情報をつなげておくことが、これからの地域ビジネスの土台になります。': 'Instagram・Google・まちアカ・地域発信をつなげておくことが、これからの地域ビジネスの土台になります。',
    '必要に応じて、Instagram・講座・セミナーまで広げます。': 'まずは今ある発信を整え、必要に応じてInstagram強化・講座・セミナーまで広げます。',
    '今ある発信を、事業で使える武器へ。Instagram・Google・地域導線まで、無理なく続く形に整えます。': '今ある発信を、事業で使える武器へ。外注して終わりではなく、Instagram・Google・地域導線を無理なく続く形に整えます。',
    'SNSと同時にGoogleを整え、地図・検索・口コミ・AIの候補から小金井の事業が見えなくならない仕組みを育てます。': 'SNSとGoogleを同時に整え、地図・検索・口コミ・AIからも見つけてもらえる土台を育てます。',
}
for old, new in replacements.items():
    s = s.replace(old, new)

# Partner network section: BUL is the producer; Suzuki and Yokota are specialist partners.
old_team_heading = '<span class="kicker">KOGANEI TEAM</span><h2>鈴木 × ぶる × 横田。小金井を強くする3人タッグ。</h2><p class="lead trio-lead">見つける・届ける・伝える。それぞれの強みを一つのチームとして使います。</p>'
new_team_heading = '<span class="kicker">BUL PARTNER NETWORK</span><h2>ぶるが組み立てる、小金井で強くなる仕組み。</h2><p class="lead trio-lead">まちこが／ぶるが全体を設計し、必要に応じて「見つかる」の鈴木智哉、「伝わる」の横田淳と連携。各分野のプロを、事業に必要な形でつなぎます。</p>'
s = s.replace(old_team_heading, new_team_heading)

# Replace the three cards in one shot so hierarchy and achievements are clear.
team_pattern = re.compile(
    r'<div class="trio-stage"><article class="trio-person suzuki">.*?</article><article class="trio-person buru-center">.*?</article><article class="trio-person yokota">.*?</article></div>',
    re.S,
)
team_html = '''<div class="trio-stage">
<article class="trio-person suzuki"><div class="trio-photo"><img src="assets/partners/suzuki.webp?v=20260910-8" alt="鈴木智哉"></div><a class="trio-role" href="https://machi-aka.cc-corp.co.jp/koganei/" target="_blank" rel="noopener">LOCAL MEDIA PARTNER ↗</a><h3>鈴木智哉</h3><strong>「見つかる」を支える、地域メディアのプロ。</strong><p>株式会社C&amp;C代表。「令和の虎」で虎として出演し、地域メディア「まちアカ」を主宰。地域検索・ニュース・Google連携の接点を広げます。</p><div class="chip-row"><span class="chip">令和の虎・虎</span><span class="chip">まちアカ165地域</span><span class="chip">凛々堂 1年19店舗</span></div><a class="trio-cta" href="https://machi-aka.cc-corp.co.jp/koganei/" target="_blank" rel="noopener">まちアカを見る →</a></article>
<article class="trio-person buru-center"><div class="trio-photo"><img src="assets/buru-v67.webp" alt="ぶる"></div><div class="trio-role">BUL / PRODUCER</div><h3>ぶる</h3><strong>仕組み全体を組み立て、小金井に「届く」をつくる。</strong><p>地域に根ざしたSNS設計と伴走支援で、Instagram・Google・まちアカ・動画をつなぎ、事業者自身に発信資産が残る仕組みを育てます。</p><div class="chip-row"><span class="chip">5,500人</span><span class="chip">85%小金井</span><span class="chip">契約19件</span><span class="chip">投稿約90件</span></div><a class="trio-cta" href="https://www.instagram.com/machikoga/" target="_blank" rel="noopener">ぶるのInstagramを見る →</a></article>
<article class="trio-person yokota"><div class="trio-photo"><img src="assets/partners/yokota.webp" alt="横田淳"></div><a class="trio-role" href="#samples">DRONE PARTNER ↓</a><h3>横田淳</h3><strong>「伝わる」を支える、ドローン映像の第一人者。</strong><p>株式会社ドローンエンタテインメント代表。ドローンレース元日本代表、Asia Drone Championships 2018 準優勝。TVCM・映画・PVなどの撮影実績を持ち、空間の魅力を一目で伝えます。</p><div class="chip-row"><span class="chip">元日本代表</span><span class="chip">アジア大会 準優勝</span><span class="chip">全国150自治体</span></div><a class="trio-cta" href="#samples">動画事例を見る →</a></article>
</div>'''
s = team_pattern.sub(team_html, s, count=1)

# Reframe the relationship below the cards and the CTA.
s = s.replace(
    '<div class="trio-result"><span>見つかる</span><b>×</b><span>届く</span><b>×</b><span>伝わる</span><strong>＝ 小金井で選ばれる</strong></div>',
    '<div class="trio-result"><span>ぶるが全体設計</span><b>＋</b><span>専門パートナー</span><strong>＝ 小金井で選ばれる仕組み</strong></div>'
)
s = s.replace('3人タッグに相談する', 'ぶるに相談する')

# Reassuring note on final CTA
if '相談だけでも大丈夫です。' not in s:
    old_cta = '<div class="cta-actions"><a class="btn line" href="https://lin.ee/XkEC3Il" target="_blank" rel="noopener">LINEで無料相談</a><a class="btn white" href="https://www.instagram.com/machikoga/" target="_blank" rel="noopener">Instagram DMで相談</a></div>'
    new_cta = old_cta + '<small class="cta-note">相談だけでも大丈夫です。今の発信を見ながら、優先順位を一緒に整理します。</small>'
    s = s.replace(old_cta, new_cta)

# Mobile dock wording and spacing
s = s.replace('>LINE相談<', '>LINEで相談<')
s = re.sub(
    r'\.mobile-dock\{position:fixed;left:[^}]+\}',
    '.mobile-dock{position:fixed;left:12px;right:12px;bottom:max(8px,env(safe-area-inset-bottom));z-index:120;display:none;gap:6px}',
    s,
    count=1,
)
s = re.sub(
    r'\.mobile-dock a\{[^}]+\}',
    '.mobile-dock a{flex:1;min-height:42px;font-size:.76rem;padding:0 8px;box-shadow:0 8px 20px rgba(3,18,42,.18)}',
    s,
    count=1,
)
s = s.replace('.section{padding:72px 0}', '.section{padding:66px 0}')
s = s.replace('footer{padding-bottom:82px}', 'footer{padding-bottom:68px}')

# UX/accessibility polish
polish_css = '''
/* V68 CONVERSION POLISH */
section[id]{scroll-margin-top:88px}
.section-cta{text-align:center;margin-top:24px}
.cta-note{display:block;margin-top:14px;color:rgba(255,255,255,.64);font-size:.82rem}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:3px solid #f0d995;outline-offset:3px}
@media(max-width:780px){.section-cta{margin-top:18px}.section-cta .btn{width:100%;max-width:360px}.cta-note{font-size:.76rem;line-height:1.6}}
'''
if '/* V68 CONVERSION POLISH */' not in s:
    s = s.replace('</style>', polish_css + '</style>', 1)

p.write_text(s, encoding='utf-8')

# Sanity checks
checks = [
    (dst.exists() and dst.stat().st_size > 0, 'Transparent mascot asset was not generated'),
    ('assets/buru-hero-transparent.webp?v=20260910-1' in s, 'Hero mascot source was not updated'),
    ('assets/partners/suzuki.webp?v=20260910-8' in s, 'Suzuki cache-bust replacement was not applied'),
    ('BURU' not in s, 'BURU remains in public/index.html'),
    ('BUL / PRODUCER' in s, 'BUL producer label was not applied'),
    ('ぶるが組み立てる、小金井で強くなる仕組み。' in s, 'Partner network heading was not applied'),
    ('ぶるのInstagramを見る' in s, 'BUL Instagram link was not added'),
    ('まちアカ165地域' in s, 'Suzuki achievements were not added'),
    ('アジア大会 準優勝' in s, 'Yokota achievements were not added'),
    ('契約19件' in s and '投稿約90件' in s, 'BUL achievements were not added'),
    ('ぶるに相談する' in s, 'BUL consultation CTA was not applied'),
    ('なぜ、今整えるのか。' in s, 'WHY NOW copy polish was not applied'),
]
for ok, message in checks:
    if not ok:
        raise SystemExit(message)
