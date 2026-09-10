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
            q.append((x, y)); seen.add((x, y))
for y in range(h):
    for x in (0, w - 1):
        if is_bg(x, y):
            q.append((x, y)); seen.add((x, y))
while q:
    x, y = q.popleft()
    r, g, b, a = px[x, y]
    px[x, y] = (r, g, b, 0)
    for nx, ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
        if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in seen and is_bg(nx, ny):
            seen.add((nx, ny)); q.append((nx, ny))

bbox = im.getbbox()
if bbox:
    l, t, r, b = bbox
    pad = 10
    l = max(0, l-pad); t = max(0, t-pad); r = min(w, r+pad); b = min(h, b+pad)
    im = im.crop((l, t, r, b))
im.save(dst, 'WEBP', quality=88, method=6)

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

# --- Stable global fixes ---
s = re.sub(r'assets/partners/suzuki\.webp\?v=[0-9-]+', 'assets/partners/suzuki.webp?v=20260910-8', s)
s = re.sub(r'(<img class="hero-buru" src=")[^"]+(" alt="まちこが ぶる">)', r'\1assets/buru-hero-transparent.webp?v=20260910-1\2', s, count=1)
s = re.sub(r'\.hero-buru\{width:min\(380px,92%\);height:430px;[^}]*\}', '.hero-buru{width:min(380px,92%);height:430px;object-fit:contain;object-position:center center;border-radius:0;border:0;background:transparent;box-shadow:none}', s, count=1)
s = re.sub(r'\.hero-buru\{width:210px;height:245px;[^}]*\}', '.hero-buru{width:210px;height:245px;border-radius:0;object-fit:contain;background:transparent;border:0;box-shadow:none}', s, count=1)
s = s.replace('BURU', 'BUL')
s = s.replace('>実例を見る<', '>実績・事例を見る<')
s = s.replace('>今やらないと？<', '>なぜ今？<')

# WHY NOW copy
for old, new in {
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
}.items():
    s = s.replace(old, new)

# --- Emphasize PR POINT 01 ---
s = re.sub(r'\.pr-card\.one\{[^}]*\}', '.pr-card.one{background:linear-gradient(135deg,#0b5ea8,#0aa095);border:2px solid rgba(240,217,149,.78);box-shadow:0 16px 36px rgba(12,139,134,.28)}', s, count=1)
s = re.sub(r'\.pr-card\.two\{[^}]*\}', '.pr-card.two{background:linear-gradient(135deg,rgba(89,67,35,.92),rgba(143,105,42,.90))}', s, count=1)
if '.pr-card.one .label' not in s:
    s = s.replace('.pr-card .label{font-size:.68rem;font-weight:900;letter-spacing:.12em;color:#fff}', '.pr-card .label{font-size:.68rem;font-weight:900;letter-spacing:.12em;color:#fff}.pr-card.one .label{color:#fff1b8}.pr-card.one strong{font-size:1.36rem}')

# --- Replace partner section ---
tools_html = '''<section class="section tools" id="tools">
<div class="container">
<span class="kicker">BUL × POWERFUL PARTNERS</span>
<h2>ぶると強力なパートナーで、<br>小金井で強くなる仕組み。</h2>
<p class="lead trio-lead">まちこが／ぶるが事業全体の発信・集客設計を行い、必要に応じて各分野の第一線で活躍する専門パートナーと連携。<strong>Instagram・Google・地域メディア・動画をつなぎ、小金井で「見つかる・届く・伝わる」仕組みをつくります。</strong></p>
<div class="trio-stage">
<article class="trio-person suzuki"><div class="trio-photo"><img src="assets/partners/suzuki.webp?v=20260910-8" alt="鈴木智哉"></div><div class="trio-role">LOCAL MEDIA PARTNER</div><h3>鈴木智哉</h3><strong>「見つかる」を支える、地域ビジネスの実力者。</strong><p>株式会社C&amp;C代表。<strong>「令和の虎」の虎として出演。</strong>地域メディア「まちアカ」を全国へ展開し、地域検索・ニュース・Google連携など、地域で事業が見つかる仕組みを構築。ANAグループの地域創生プロジェクトなど、地域の魅力を全国へ届ける取り組みにも関わっています。</p><div class="authority-box"><div class="authority-item"><b>令和の虎</b><span>虎として出演</span></div><div class="authority-item"><b>165地域</b><span>まちアカ全国展開</span></div><div class="authority-item"><b>ANA</b><span>地域創生プロジェクト</span></div><div class="authority-item"><b>19店舗</b><span>飲食ブランドを1年で展開</span></div></div><a class="trio-cta" href="https://machi-aka.cc-corp.co.jp/koganei/" target="_blank" rel="noopener">まちアカを見る →</a></article>
<article class="trio-person buru-center"><div class="main-badge">MACHIKOGA / BUL</div><div class="trio-photo"><img src="assets/buru-v67.webp" alt="ぶる"></div><div class="trio-role">BUL / PRODUCER</div><h3>ぶる</h3><strong>小金井で強くなる仕組みを、全体から組み立てる。</strong><p><strong>小金井在住11年目。</strong>大手カフェチェーンの立ち上げで<strong>0→250店舗</strong>までの成長を経験。医療業界では<strong>200店舗規模の責任者</strong>として店舗運営・組織・集客改善に携わり、コンサルティング実績は<strong>100件以上。</strong></p><p>現在は小金井に特化し、Instagram・Google・まちアカ・地域発信・動画をつなぎ、外注して終わるのではなく、<strong>事業者自身の手元に残る「集客資産」を一緒に育てています。</strong></p><div class="buru-current"><span class="asof">2026年8月時点</span><div class="buru-stats"><div><b>5,500人</b><span>Instagramフォロワー</span></div><div><b>85%</b><span>小金井エリア</span></div><div><b>21社</b><span>小金井で一緒に仕事</span></div><div><b>100件以上</b><span>投稿実績</span></div></div></div><div class="authority-box buru-history"><div class="authority-item"><b>0→250店舗</b><span>大手カフェチェーン立ち上げ</span></div><div class="authority-item"><b>200店舗</b><span>医療業界の責任者</span></div><div class="authority-item"><b>100件+</b><span>コンサル実績</span></div><div class="authority-item"><b>小金井11年</b><span>地域密着</span></div></div><a class="trio-cta buru-instagram" href="https://www.instagram.com/machikoga/" target="_blank" rel="noopener">ぶるのInstagramを見る →</a></article>
<article class="trio-person yokota"><div class="trio-photo"><img src="assets/partners/yokota.webp" alt="横田淳"></div><div class="trio-role">DRONE PARTNER</div><h3>横田淳</h3><strong>「伝わる」を支える、ドローン映像の第一人者。</strong><p>株式会社ドローンエンタテインメント代表。<strong>ドローンレース元日本代表。</strong>Asia Drone Championships 2018 準優勝。FPV・マイクロドローンを使った映像表現で、観光地・企業・店舗・地域の魅力を「一目で伝わる映像」へ変えます。</p><p>「桜ドローンプロジェクト」は<strong>NHK「おはよう日本」・日本テレビ「ZIP!」・TBS「ひるおび！」</strong>など多数のメディアで紹介。全国各地の自治体とも連携しています。</p><div class="authority-box"><div class="authority-item"><b>日本代表</b><span>ドローンレース</span></div><div class="authority-item"><b>アジア2位</b><span>Asia Drone Championships</span></div><div class="authority-item"><b>100+</b><span>メディア掲載</span></div><div class="authority-item"><b>全国連携</b><span>自治体・地域プロジェクト</span></div></div><a class="trio-cta" href="#samples">動画事例を見る →</a></article>
</div>
<div class="partner-system"><div class="system-main"><span>中心</span><strong>ぶるが全体を設計</strong></div><div class="system-plus">＋</div><div class="system-partner"><span>強力なパートナー</span><strong>各分野のプロと連携</strong></div><div class="system-equal">＝</div><div class="system-result"><strong>小金井で見つかり、届き、選ばれる仕組み</strong></div></div>
<div class="section-cta"><a class="btn navy" href="#contact">ぶるに相談する</a></div>
</div>
</section>'''
s = re.sub(r'<section class="section tools" id="tools">.*?</section>(?=\s*<section class="section local-edge")', tools_html, s, count=1, flags=re.S)

# --- Replace results section with proof-oriented layout ---
results_html = '''<section class="section results machikoga-results" id="results"><div class="container"><span class="kicker">MACHIKOGA RESULTS</span><h2>小金井で、<br>実際に成果が出ています。</h2><p class="lead results-lead">集客だけではありません。<strong>新規来店・採用・認知・Google・アカウント立ち上げまで。</strong>まちこがが一緒に取り組んだ成果の一部です。</p><div class="results-highlight">
<article class="result-impact"><span class="result-type">飲食店</span><small>集客コンサル</small><strong>2ヶ月で<br>ランチ客数120%</strong></article>
<article class="result-impact"><span class="result-type">求人</span><small>アルバイト募集投稿</small><strong>投稿後1日で<br>6名応募</strong><p>採用決定</p></article>
<article class="result-impact"><span class="result-type">整体院</span><small>店舗アピール投稿</small><strong>翌日<br>新規顧客5名</strong><p>保存10</p></article>
<article class="result-impact"><span class="result-type">カフェ</span><small>新規アカウント立ち上げ</small><strong>3ヶ月で<br>小金井フォロワー300人</strong><p>1日1組「Instagramを見た」で新規来店</p></article>
<article class="result-impact"><span class="result-type">ドローン</span><small>Google閲覧数</small><strong>1週間で<br>過去の閲覧数を突破</strong><p>閲覧数トップへ</p></article>
<article class="result-impact"><span class="result-type">看護師採用</span><small>訪問ナース紹介</small><strong>看護師<br>2名採用</strong></article>
</div><details class="results-more"><summary>その他の成果を見る ＋</summary><div class="results-list"><div class="result-row"><b>美容室</b><span>店舗アピール投稿</span><strong>周年イベント翌日 新規来客4名</strong></div><div class="result-row"><b>スポーツスクール</b><span>会員募集</span><strong>翌日 新規体験4名・保存11</strong></div><div class="result-row"><b>ラーメン店</b><span>特集記事掲載</span><strong>混雑が続出するほど反響</strong></div><div class="result-row"><b>小金井ゆるっと会</b><span>地域交流イベント</span><strong>定期開催へ。地域コミュニティ形成</strong></div><div class="result-row"><b>ハウスクリーニング</b><span>新規アカウント立ち上げ</span><strong>3ヶ月で多摩エリアフォロワー700人</strong></div><div class="result-row"><b>バンド</b><span>新規アカウント立ち上げ</span><strong>初期設計から東京都・大阪へ認知拡大</strong></div></div></details><p class="results-note">※成果事例は一部抜粋です。数値・実績は2026年8月時点を含みます。</p></div></section>'''
s = re.sub(r'<section class="section results(?: machikoga-results)?" id="results">.*?</section>(?=\s*<section class="section samples")', results_html, s, count=1, flags=re.S)

# Final CTA reassurance
if '相談だけでも大丈夫です。' not in s:
    old_cta = '<div class="cta-actions"><a class="btn line" href="https://lin.ee/XkEC3Il" target="_blank" rel="noopener">LINEで無料相談</a><a class="btn white" href="https://www.instagram.com/machikoga/" target="_blank" rel="noopener">Instagram DMで相談</a></div>'
    s = s.replace(old_cta, old_cta + '<small class="cta-note">相談だけでも大丈夫です。今の発信を見ながら、優先順位を一緒に整理します。</small>')

# Mobile dock
s = s.replace('>LINE相談<', '>LINEで相談<')
s = re.sub(r'\.mobile-dock\{position:fixed;left:[^}]+\}', '.mobile-dock{position:fixed;left:12px;right:12px;bottom:max(8px,env(safe-area-inset-bottom));z-index:120;display:none;gap:6px}', s, count=1)
s = re.sub(r'\.mobile-dock a\{[^}]+\}', '.mobile-dock a{flex:1;min-height:42px;font-size:.76rem;padding:0 8px;box-shadow:0 8px 20px rgba(3,18,42,.18)}', s, count=1)
s = s.replace('.section{padding:72px 0}', '.section{padding:66px 0}')
s = s.replace('footer{padding-bottom:82px}', 'footer{padding-bottom:68px}')

# --- Inject / refresh authority and results CSS ---
css = r'''
/* V68 AUTHORITY + RESULTS */
section[id]{scroll-margin-top:88px}
.section-cta{text-align:center;margin-top:24px}
.cta-note{display:block;margin-top:14px;color:rgba(255,255,255,.64);font-size:.82rem}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:3px solid #f0d995;outline-offset:3px}
.tools{background:radial-gradient(circle at 50% 10%,rgba(199,162,83,.10),transparent 28%),#f4f6f9}
.trio-lead{max-width:900px;margin-top:16px}.trio-lead strong{color:var(--navy)}
.buru-center{transform:translateY(-14px);border:2px solid rgba(199,162,83,.65)!important;box-shadow:0 30px 70px rgba(5,25,57,.17)!important}
.main-badge{display:inline-flex;margin-bottom:14px;padding:7px 13px;border-radius:999px;background:linear-gradient(135deg,#d2af62,#9b6a26);color:#fff;font-size:.66rem;font-weight:900;letter-spacing:.11em}
.authority-box{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:17px}.authority-item{padding:11px 8px;border-radius:15px;background:#f3f6fa;border:1px solid #e3e9f0;text-align:center}.authority-item b{display:block;color:var(--navy);font-size:1rem;line-height:1.2}.authority-item span{display:block;margin-top:4px;color:#718097;font-size:.64rem;font-weight:800;line-height:1.4}.buru-history .authority-item{background:#fffaf0;border-color:#ead9ad}
.buru-current{margin-top:18px;padding:17px;border-radius:20px;background:linear-gradient(145deg,#071d3f,#0b396d);color:#fff}.asof{display:block;margin-bottom:10px;color:#ead085;font-size:.68rem;font-weight:900;letter-spacing:.08em}.buru-stats{display:grid;grid-template-columns:1fr 1fr;gap:10px}.buru-stats div{padding:11px 8px;border-radius:14px;background:rgba(255,255,255,.08);text-align:center}.buru-stats b{display:block;color:#fff;font-size:1.18rem}.buru-stats span{display:block;margin-top:3px;color:rgba(255,255,255,.68);font-size:.64rem;font-weight:800}.buru-instagram{background:linear-gradient(135deg,#101b3d,#304e8f)!important;color:#fff!important;border:0!important}
.partner-system{max-width:1000px;margin:28px auto 0;padding:22px;display:flex;align-items:center;justify-content:center;gap:13px;flex-wrap:wrap;border-radius:24px;background:#071d3f;color:#fff}.partner-system span{display:block;color:#d2af62;font-size:.65rem;font-weight:900;letter-spacing:.08em}.partner-system strong{display:block;margin-top:2px;font-size:.95rem}.system-plus,.system-equal{color:#ead085;font-size:1.6rem;font-weight:900}.system-result{color:#ead085}
.machikoga-results{background:linear-gradient(180deg,#fff,#f4f7fb)}.results-lead{max-width:850px;margin-top:15px}.results-highlight{display:grid;grid-template-columns:repeat(3,1fr);gap:15px;margin-top:32px}.result-impact{padding:24px;border-radius:24px;background:#fff;border:1px solid var(--line);box-shadow:var(--shadow2)}.result-type{display:inline-flex;padding:5px 10px;border-radius:999px;background:#071d3f;color:#fff;font-size:.68rem;font-weight:900}.result-impact small{display:block;margin-top:12px;color:#7c899a;font-weight:800}.result-impact>strong{display:block;margin-top:7px;color:#b12222;font-size:1.65rem;line-height:1.2}.result-impact p{margin-top:7px;color:var(--text);font-size:.82rem}.results-more{margin-top:22px}.results-more summary{display:inline-flex;padding:11px 16px;border-radius:999px;background:#071d3f;color:#fff;cursor:pointer;font-size:.82rem;font-weight:900;list-style:none}.results-more summary::-webkit-details-marker{display:none}.results-list{display:grid;gap:8px;margin-top:16px}.result-row{display:grid;grid-template-columns:170px 220px 1fr;gap:12px;padding:13px 16px;border-radius:15px;background:#fff;border:1px solid var(--line);align-items:center}.result-row b{color:var(--navy)}.result-row span{color:var(--text);font-size:.82rem}.result-row strong{color:#b12222;font-size:.88rem}.results-note{margin-top:16px;color:#8490a0;font-size:.72rem}
@media(max-width:780px){.buru-center{transform:none}.authority-box,.buru-stats{grid-template-columns:1fr 1fr}.partner-system{display:grid;grid-template-columns:1fr;text-align:center;gap:8px}.system-plus,.system-equal{font-size:1.2rem}.results-highlight{grid-template-columns:1fr}.result-impact{padding:21px}.result-row{grid-template-columns:1fr;gap:3px}.section-cta{margin-top:18px}.section-cta .btn{width:100%;max-width:360px}.cta-note{font-size:.76rem;line-height:1.6}}
'''
# Remove older polish blocks to prevent duplicates.
s = re.sub(r'/\* V68 CONVERSION POLISH \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = re.sub(r'/\* V68 AUTHORITY \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = re.sub(r'/\* V68 AUTHORITY \+ RESULTS \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = s.replace('</style>', css + '</style>', 1)

p.write_text(s, encoding='utf-8')

checks = [
    (dst.exists() and dst.stat().st_size > 0, 'Transparent mascot asset was not generated'),
    ('assets/buru-hero-transparent.webp?v=20260910-1' in s, 'Hero mascot source was not updated'),
    ('BURU' not in s, 'BURU remains in public/index.html'),
    ('BUL × POWERFUL PARTNERS' in s, 'Partner section was not updated'),
    ('ぶるのInstagramを見る →' in s, 'BUL Instagram link missing'),
    ('21社' in s and '100件以上' in s, 'BUL latest proof missing'),
    ('MACHIKOGA RESULTS' in s, 'Results section missing'),
    ('2ヶ月で<br>ランチ客数120%' in s, 'Results proof missing'),
]
for ok, message in checks:
    if not ok:
        raise SystemExit(message)
