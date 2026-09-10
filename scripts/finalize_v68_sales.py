from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

# ---------- helpers ----------
def replace_section(section_id: str, html: str):
    global s
    pattern = rf'<section class="section [^"]*" id="{re.escape(section_id)}">.*?</section>'
    s, n = re.subn(pattern, html, s, count=1, flags=re.S)
    if n != 1:
        raise SystemExit(f'Could not replace section: {section_id}')

def remove_section_by_class(cls: str):
    global s
    s = re.sub(rf'<section class="section {re.escape(cls)}"[^>]*>.*?</section>', '', s, count=1, flags=re.S)

# ---------- small global copy changes ----------
s = s.replace('ぶるが全体を設計', 'ぶるが設計')
s = s.replace('ぶるが全体設計', 'ぶるが設計')
s = s.replace('>2つの仕事<', '>2つの価値<')
s = s.replace('>まちこがの武器<', '>パートナー<')

# Header: product first, then proof, then price.
s = re.sub(
    r'<nav class="nav">.*?</nav>',
    '<nav class="nav"><a href="#infra">2つの価値</a><a href="#services">サービス</a><a href="#results">実績</a><a href="#tools">パートナー</a><a href="#pricing">料金</a><a class="btn gold" href="#contact">無料相談</a></nav>',
    s,
    count=1,
    flags=re.S,
)

# Top proof: latest user-provided August 2026 numbers, with labels that explain the meaning.
proof_html = '''<div class="proof-wrap"><div class="container"><div class="proof">
<div class="proof-item"><strong>5,500人</strong><span>「ぶる」Instagramフォロワー｜2026.8</span></div>
<div class="proof-item"><strong>85%</strong><span>フォロワーの小金井エリア比率</span></div>
<div class="proof-item"><strong>21社</strong><span>小金井で実際に一緒に仕事</span></div>
<div class="proof-item"><strong>100件+</strong><span>投稿制作・支援実績</span></div>
</div></div></div>'''
s = re.sub(r'<div class="proof-wrap">.*?</div>\s*<div class="quick">', proof_html + '\n<div class="quick">', s, count=1, flags=re.S)

# Quick navigation.
s = re.sub(
    r'<div class="quick"><div class="container quick-in">.*?</div></div>',
    '<div class="quick"><div class="container quick-in"><a href="#empathy">こんな悩みありませんか</a><a href="#infra">2つの価値</a><a href="#services">サービス内容</a><a href="#results">成果</a><a href="#tools">強力なパートナー</a><a href="#easy">やることは3つ</a><a href="#pricing">料金</a></div></div>',
    s,
    count=1,
    flags=re.S,
)

# ---------- empathy / pain ----------
empathy_html = '''<section class="section empathy" id="empathy"><div class="container empathy-grid">
<article class="card empathy-card"><span class="kicker">FOR KOGANEI BUSINESS</span><h3>WEBを整えたい。<br><span class="gold">でも、担当者を雇うほどではない。</span></h3><p>Instagram、Googleマップ、口コミ、地域への発信。必要なのは分かっていても、日々の本業をしながら全部を設計・運用するのは大変です。</p></article>
<aside class="buru-tip"><img src="assets/buru-v67.webp" alt="ぶる"><div><strong>社長は、本業に集中してください。</strong><p>投稿を増やすのではなく、今ある発信を「残る資産」に変える仕組みを、ぶるが設計します。</p></div></aside>
</div></section>'''
replace_section('empathy', empathy_html)

# ---------- AI value: shorten to the five values from the deck ----------
ai_html = '''<section class="section ai" id="ai"><div class="container"><div class="section-head"><div><span class="kicker">AI CANNOT CREATE THIS</span><h2>AIには作れない、<br>地域ビジネスの価値。</h2></div><p class="lead">AIはコンテンツを作れても、あなたの店が積み上げてきたものまでは作れません。</p></div><div class="values-grid sales-five"><div class="value-card"><b>土地</b><span>その場所で商売してきた事実</span></div><div class="value-card"><b>歴史</b><span>店・会社が歩んできた背景</span></div><div class="value-card"><b>時間・プロセス</b><span>地域に積み重ねた信頼</span></div><div class="value-card"><b>思い出</b><span>お客様との体験・記憶</span></div><div class="value-card center"><b>地域とのつながり</b><span>小金井で育てた、本物の事業資産</span></div></div><div class="role-card"><div class="role-main"><span>価値は、すでにある。</span><span>まちこがは、それを見つかる形にする。</span></div></div></div></section>'''
replace_section('ai', ai_html)

# ---------- Core value / PR points ----------
infra_html = '''<section class="section infra" id="infra"><div class="container"><div class="section-head"><div><span class="kicker">TWO CORE VALUES</span><h2>投稿代行ではなく、<br>自前の情報インフラをつくる。</h2></div><p class="lead">広告のように止めたら消える「フロー型」ではなく、SNS・Google・地域情報を積み上げる<strong>ストック型の経営資産</strong>へ。</p></div><div class="core-grid">
<article class="core-card one core-primary"><span class="core-label">PR POINT 01</span><h3>小金井で強い、<br>自前の情報インフラ。</h3><p>Instagram・Googleマップ・まちアカ・ぶる・動画をバラバラにせず、<strong>自分たちで発信し、見つけてもらい、また来てもらえる土台</strong>としてつなぎます。</p><div class="asset-note"><b>積み上げるほど、御社に残る。</b><span>集客・採用・イベント・新商品。自分のメディアを持てば、いつでも発信できます。</span></div><div class="network-list"><div>Instagram</div><div>Googleマップ</div><div>まちアカ</div><div>ぶる・地域発信</div></div></article>
<article class="core-card two"><span class="core-label">PR POINT 02</span><h3>同じ1回の発信を、<br>小金井で数倍強くする。</h3><p>1つずつ別々に投稿するのではなく、情報の行き先をつなげて接点を増やします。</p><div class="one-post"><strong>1回の発信</strong><div class="branches"><div class="branch">Instagram</div><div class="branch">Google</div><div class="branch">まちアカ</div><div class="branch">地域メディア</div></div></div><div class="bigline">頑張る量ではなく、1回の価値を上げる。</div></article>
</div></div></section>'''
replace_section('infra', infra_html)

# ---------- Product / service ----------
services_html = '''<section class="section services" id="services"><div class="container"><span class="kicker">ONE PACKAGE</span><h2>小金井で必要なWEB施策を、<br>4つの柱で一つの仕組みに。</h2><p class="lead service-intro">別々の業者に頼むのではなく、地域で「見つかる → 伝わる → ファンになる」までをまとめて設計します。</p>
<div class="offer-grid">
<article class="offer-card"><span class="offer-no">01</span><h3>まちアカ掲載</h3><p>小金井の事業者ポータルサイトに掲載。地域名×キーワードの入口を増やし、地域全体で「見つかる力」を積み上げます。</p><b>地域SEO・ニュース投稿</b></article>
<article class="offer-card"><span class="offer-no">02</span><h3>Googleマップ / MEO</h3><p>プロフィール・最新情報・口コミ依頼・返信を整備。まちアカのニュース投稿とGoogleの情報をつなぎます。</p><b>検索・地図・口コミ</b></article>
<article class="offer-card"><span class="offer-no">03</span><h3>Instagram</h3><p>プロフィール、ピン留め、世界観、ストーリーズ導線を初期設計。薄いバズではなく、小金井のファンを育てます。</p><b>新規 → フォロー → リピート</b></article>
<article class="offer-card"><span class="offer-no">04</span><h3>空間3Dビュー</h3><p>店舗・施設の広さ、動線、空気感を20秒で伝える映像へ。Googleマップ上での見せ方も強化します。</p><b>動画・ドローン・Google</b></article>
</div>
<div class="included-strip"><div><strong>さらに初期設計に含まれるもの</strong><span>カスタムAI構築 / 口コミPOP / インタビュー / 掲載ページ制作 / 写真・動画撮影 / Google連携作業</span></div><a class="btn navy" href="#pricing">料金を見る</a></div>
</div></section>'''
replace_section('services', services_html)

# ---------- Partner authority: compact, product stays the hero ----------
tools_html = '''<section class="section tools compact-partners" id="tools"><div class="container"><span class="kicker">POWERFUL PARTNERS</span><h2>ぶるを支える、<br>強力なパートナー。</h2><div class="partner-intro">ぶるが設計 <b>＋</b> 各分野のプロと連携 <b>＝</b> 小金井で見つかり、届き、選ばれる仕組み</div>
<div class="trio-stage compact-stage">
<article class="trio-person compact-person suzuki"><div class="trio-photo"><img src="assets/partners/suzuki.webp?v=20260910-8" alt="鈴木智哉"></div><div class="trio-role">LOCAL MEDIA</div><h3>鈴木智哉</h3><strong>地域ビジネス・メディア</strong><div class="authority-mini"><span>令和の虎・虎</span><span>3年で3ブランド26店舗</span><span>凛々堂｜広告費0円・1年19店舗</span><span>ANAKUMA CAFE｜5ヶ月1万人</span><span>ANAグループ連携セミナー</span></div><a class="trio-cta" href="https://machi-aka.cc-corp.co.jp/koganei/" target="_blank" rel="noopener">まちアカを見る →</a></article>
<article class="trio-person compact-person buru-center"><div class="main-badge">まちこが / ぶる</div><div class="trio-photo"><img src="assets/buru-v67.webp" alt="ぶる"></div><div class="trio-role">PRODUCER</div><h3>ぶる</h3><strong>仕組みを設計する人</strong><div class="authority-mini main"><span>小金井在住11年目</span><span>大手カフェ｜0→250店舗</span><span>医療業界｜200店舗規模責任者</span><span>店舗・SNSコンサル100件+</span><span>小金井21社・投稿100件+｜2026.8</span></div><a class="trio-cta buru-instagram" href="https://www.instagram.com/machikoga/" target="_blank" rel="noopener">ぶるのInstagramを見る →</a></article>
<article class="trio-person compact-person yokota"><div class="trio-photo"><img src="assets/partners/yokota.webp" alt="横田淳"></div><div class="trio-role">DRONE / VISUAL</div><h3>横田淳</h3><strong>ドローン映像の第一人者</strong><div class="authority-mini"><span>世界大会</span><span>万博</span><span>Coca-Cola</span><span>HONDA</span><span>NTTデータ / BMW</span></div><a class="trio-cta" href="#samples">動画事例を見る →</a></article>
</div></div></section>'''
replace_section('tools', tools_html)

# Remove the redundant local-edge section; its message is now integrated into the product flow.
remove_section_by_class('local-edge')

# ---------- Results: keep proof-oriented content, tighten heading ----------
s = s.replace('<h2>小金井で、<br>実際に成果が出ています。</h2>', '<h2>小金井で、<br>成果が出ています。</h2>')
s = s.replace('まちこがが一緒に取り組んだ成果の一部です。', '集客・採用・認知・Googleまで。実際に一緒に取り組んだ成果の一部です。')

# ---------- Easy-operation section inserted after samples ----------
easy_html = '''<section class="section easy" id="easy"><div class="container"><div class="easy-wrap"><div><span class="kicker">KEEP IT SIMPLE</span><h2>やっていただくことは、<br>基本この3つ。</h2><p class="lead">御社専用の記事作成AIを使いながら、日々の運用をシンプルにします。</p></div><div class="easy-list"><div><b>01</b><strong>1日2分のGoogle投稿</strong><span>最新情報を止めない</span></div><div><b>02</b><strong>口コミ依頼 ＆ 口コミ返信</strong><span>信頼をストックする</span></div><div><b>03</b><strong>ストーリーズ投稿</strong><span>既存ファンとの関係を育てる</span></div></div></div><div class="support-row"><span>カスタムAI</span><span>LINEチャット</span><span>定期ZOOM勉強・相談会</span><span>事例共有</span></div></div></section>'''
# insert once right after samples section
if 'id="easy"' not in s:
    s = re.sub(r'(<section class="section samples" id="samples">.*?</section>)', r'\1\n' + easy_html, s, count=1, flags=re.S)

# ---------- Community: make the philosophy directly support the sale ----------
community_html = '''<section class="section community" id="community"><div class="container"><span class="kicker">DON'T CHASE BUZZ</span><h2>1万人にバズるより、<br>100人の「また来る人」を。</h2><p class="lead fan-lead">目指すのは、全国に散らばった薄いフォロワーではなく、地域で店を愛し、通い、紹介してくれるファン。さらに応援までしてくれるエバンジェリストを育てます。</p><div class="fan-flow"><div><span>PARTICIPANT</span><b>フォロワー</b></div><div><span>FAN</span><b>来店・反応</b></div><div><span>LOYAL</span><b>リピート</b></div><div class="fan-top"><span>EVANGELIST</span><b>紹介・応援</b></div></div></div></section>'''
replace_section('community', community_html)

# Remove lecture/seminar showcase from this sales page; it distracts from the core product.
remove_section_by_class('showcase')

# ---------- Pricing inserted before about ----------
pricing_html = '''<section class="section pricing" id="pricing"><div class="container"><span class="kicker">PRICE</span><h2>まず土台をつくり、<br>必要な運用だけを選べます。</h2><p class="lead pricing-lead">初期設計でGoogle・Instagram・まちアカの土台をまとめて構築。その後は事業の状況に合わせて月額プランを選択できます。</p>
<div class="setup-card"><div><span>INITIAL SETUP</span><h3>初期設計</h3><p>Googleマップ初期設計 / Instagram初期設計 / まちアカ初期設計</p></div><strong>180,000円<small>税込</small></strong></div>
<div class="setup-items"><span>概要・メニュー見直し</span><span>口コミPOP</span><span>カスタムAI構築</span><span>プロフィール見直し</span><span>ピン留め投稿</span><span>プロフィール投稿18枚</span><span>インタビュー</span><span>掲載ページ制作</span><span>写真・動画・空間3D撮影</span><span>Google連携作業</span></div>
<div class="plan-grid"><article class="plan-card"><span class="plan-label">掲載プラン</span><h3>9,800円<small>/月・税込</small></h3><p>まず地域の入口を持ちたい方へ。</p><ul><li>まちアカ掲載</li><li>ZOOM勉強・相談会</li></ul></article><article class="plan-card featured"><span class="plan-label">スタンダード</span><h3>19,800円<small>/月・税込</small></h3><p>自分で発信しながら、Googleと地域導線を育てたい方へ。</p><ul><li>まちアカ掲載</li><li>ニュース投稿</li><li>Googleマップ連携投稿</li><li>カスタムAI利用</li><li>ZOOM勉強・相談会</li></ul></article><article class="plan-card"><span class="plan-label">運用代行</span><h3>59,800円<small>/月・税込</small></h3><p>日々の発信まで任せたい方へ。</p><ul><li>スタンダード内容</li><li>空間3Dビュー利用</li><li>週5回ニュース投稿代行</li><li>ZOOM勉強・相談会</li></ul></article></div>
<div class="price-note"><span>オプション：予約機能（準備中）+7,980円/月 / 採用募集導線 +1,000円/月</span><span>初期オプション：開業支援 +28,000円 / ゼロ立ち上げ +18,000円</span><span>※月額は1ヶ月ごと自動更新・原則クレジットカード払い　※撮影データの著作権はまちアカに帰属</span></div><div class="section-cta"><a class="btn gold" href="#contact">自分に合うプランを相談する</a></div></div></section>'''
if 'id="pricing"' not in s:
    s = s.replace('<section class="section about">', pricing_html + '\n<section class="section about">', 1)
else:
    replace_section('pricing', pricing_html)

# About: shorter brand story.
s = re.sub(
    r'<section class="section about">.*?</section>',
    '<section class="section about"><div class="container about-wrap"><article class="about-visual"><img src="assets/buru-v67.webp" alt="ぶる"></article><div class="about-copy"><span class="kicker">ABOUT MACHIKOGA</span><h2>一店が強くなると、<br>小金井も強くなる。</h2><p>小金井で頑張る事業者が、ちゃんと見つかり、選ばれ、続いていく。そのための情報インフラを、事業者さんと一緒に育てます。</p></div></div></section>',
    s,
    count=1,
    flags=re.S,
)

# Final CTA: one clear next action.
cta_html = '''<section class="section cta" id="contact"><div class="container cta-in"><span class="kicker">FREE CONSULTATION</span><h2>まず、今の発信を<br>一緒に見てみませんか。</h2><p>Instagram・Googleマップ・地域導線を見ながら、「今のままで良いところ」「直すところ」「これから作る資産」を整理します。</p><div class="cta-actions"><a class="btn line" href="https://lin.ee/XkEC3Il" target="_blank" rel="noopener">LINEで無料相談</a><a class="btn white" href="https://www.instagram.com/machikoga/" target="_blank" rel="noopener">Instagramを見る</a></div><small class="cta-note">相談だけでも大丈夫です。無理な売り込みはしません。</small></div></section>'''
replace_section('contact', cta_html)

# ---------- Final visual system ----------
final_css = r'''
/* V68 SALES FINAL */
.service-intro,.pricing-lead,.fan-lead{max-width:860px;margin-top:16px}
.offer-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:32px}.offer-card{position:relative;padding:28px 22px 24px;border:1px solid var(--line);border-radius:24px;background:#fff;box-shadow:var(--shadow2);overflow:hidden}.offer-card:before{content:"";position:absolute;inset:0 0 auto;height:4px;background:linear-gradient(90deg,#0b5ea8,#0aa095)}.offer-no{display:inline-grid;place-items:center;width:42px;height:42px;border-radius:14px;background:#071d3f;color:#f0d995;font-weight:900}.offer-card h3{margin-top:16px;color:var(--navy);font-size:1.35rem}.offer-card p{margin-top:9px;color:var(--text);font-size:.88rem}.offer-card b{display:block;margin-top:15px;padding-top:12px;border-top:1px dashed var(--line);color:#0d6d78;font-size:.78rem}.included-strip{margin-top:18px;padding:20px 22px;border-radius:22px;background:#f5f1e7;border:1px solid #eadbb9;display:flex;align-items:center;justify-content:space-between;gap:18px}.included-strip strong{display:block;color:var(--navy)}.included-strip span{display:block;margin-top:5px;color:#657185;font-size:.82rem}
.compact-partners{padding-top:78px;padding-bottom:78px}.partner-intro{margin:18px 0 28px;padding:15px 18px;border-radius:18px;background:#071d3f;color:#fff;text-align:center;font-weight:900}.partner-intro b{color:#f0d995;margin:0 8px}.compact-stage{align-items:stretch}.compact-person{padding:22px 18px!important}.compact-person .trio-photo{width:118px;height:118px;margin-bottom:12px}.compact-person.buru-center{transform:translateY(-6px)!important}.compact-person h3{font-size:1.42rem}.compact-person>strong{font-size:.9rem}.authority-mini{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin-top:13px}.authority-mini span{padding:7px 9px;border-radius:999px;background:#f1f4f8;border:1px solid #e1e7ef;color:#3f506a;font-size:.67rem;font-weight:900;line-height:1.25}.authority-mini.main span{background:#fff8ea;border-color:#e9d5a6;color:#55462e}.compact-person .trio-cta{margin-top:14px}
.easy{background:linear-gradient(180deg,#fff,#f6f8fb)}.easy-wrap{display:grid;grid-template-columns:.85fr 1.15fr;gap:28px;align-items:center}.easy-list{display:grid;gap:10px}.easy-list div{display:grid;grid-template-columns:48px 1fr auto;gap:12px;align-items:center;padding:17px 18px;border-radius:18px;background:#fff;border:1px solid var(--line);box-shadow:var(--shadow2)}.easy-list b{display:grid;place-items:center;width:42px;height:42px;border-radius:13px;background:#071d3f;color:#f0d995}.easy-list strong{color:var(--navy)}.easy-list span{color:#748197;font-size:.77rem}.support-row{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin-top:22px}.support-row span{padding:8px 12px;border-radius:999px;background:#071d3f;color:#fff;font-size:.72rem;font-weight:900}
.sales-five{grid-template-columns:repeat(5,1fr)}
.fan-lead{color:#5a6577}.fan-flow{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:28px}.fan-flow div{padding:20px;border-radius:20px;background:#fff;border:1px solid rgba(6,26,56,.08);text-align:center}.fan-flow span{display:block;color:#9b6a26;font-size:.65rem;font-weight:900;letter-spacing:.08em}.fan-flow b{display:block;margin-top:6px;color:var(--navy)}.fan-flow .fan-top{background:#071d3f}.fan-flow .fan-top b{color:#fff}.fan-flow .fan-top span{color:#f0d995}
.pricing{background:linear-gradient(145deg,#061a38,#0a315e);color:#fff}.pricing h2,.pricing .lead{color:#fff}.setup-card{display:flex;align-items:center;justify-content:space-between;gap:20px;margin-top:30px;padding:25px 28px;border-radius:24px;background:#fff;color:var(--navy)}.setup-card span{font-size:.68rem;font-weight:900;letter-spacing:.1em;color:#9b6a26}.setup-card h3{font-size:1.6rem}.setup-card p{margin-top:5px;color:#6b778b;font-size:.82rem}.setup-card>strong{font-size:2.2rem;white-space:nowrap}.setup-card small{font-size:.75rem;margin-left:5px}.setup-items{display:flex;flex-wrap:wrap;gap:7px;margin-top:12px}.setup-items span{padding:7px 10px;border-radius:999px;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.13);font-size:.7rem;font-weight:800}.plan-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:24px}.plan-card{padding:26px;border-radius:24px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14)}.plan-card.featured{background:#fff;color:var(--navy);transform:translateY(-7px);box-shadow:0 20px 50px rgba(0,0,0,.2)}.plan-label{display:inline-flex;padding:5px 9px;border-radius:999px;background:#c7a253;color:#fff;font-size:.67rem;font-weight:900}.plan-card h3{margin-top:12px;font-size:2rem}.plan-card h3 small{font-size:.72rem;margin-left:3px}.plan-card p{margin-top:7px;color:#d5dfed;font-size:.82rem}.plan-card.featured p{color:#657185}.plan-card ul{margin:15px 0 0;padding:0;list-style:none;display:grid;gap:7px}.plan-card li{font-size:.8rem}.plan-card li:before{content:"✓";color:#f0d995;font-weight:900;margin-right:7px}.plan-card.featured li:before{color:#0c8b86}.price-note{display:grid;gap:4px;margin-top:17px;color:rgba(255,255,255,.66);font-size:.7rem}.pricing .section-cta{margin-top:24px}
.core-primary{border:2px solid rgba(11,94,168,.35)!important;box-shadow:0 22px 52px rgba(11,94,168,.13)!important}.core-primary:before{height:7px;background:linear-gradient(90deg,#0b5ea8,#0aa095,#f0d995)!important}
@media(max-width:1050px){.offer-grid{grid-template-columns:1fr 1fr}.sales-five{grid-template-columns:repeat(3,1fr)}.easy-wrap{grid-template-columns:1fr}.plan-grid{grid-template-columns:1fr}.plan-card.featured{transform:none}}
@media(max-width:780px){.offer-grid{grid-template-columns:1fr}.included-strip{align-items:flex-start;flex-direction:column}.included-strip .btn{width:100%}.compact-partners{padding-top:58px;padding-bottom:58px}.compact-person .trio-photo{width:108px;height:108px}.partner-intro{font-size:.78rem}.sales-five{grid-template-columns:1fr 1fr}.easy-list div{grid-template-columns:44px 1fr}.easy-list span{grid-column:2}.fan-flow{grid-template-columns:1fr 1fr}.setup-card{align-items:flex-start;flex-direction:column}.setup-card>strong{font-size:1.9rem}.plan-grid{grid-template-columns:1fr}.pricing .section-cta .btn{width:100%}}
@media(max-width:430px){.sales-five,.fan-flow{grid-template-columns:1fr}.authority-mini span{font-size:.64rem}}
'''
# Replace previous final style block if rerun; otherwise inject before </style>.
s = re.sub(r'/\* V68 SALES FINAL \*/.*?(?=</style>)', '', s, flags=re.S)
s = s.replace('</style>', final_css + '</style>', 1)

p.write_text(s, encoding='utf-8')

# sanity checks
required = [
    '投稿代行ではなく、<br>自前の情報インフラをつくる。',
    'まちアカ掲載', 'Googleマップ / MEO', '空間3Dビュー',
    'ぶるを支える、<br>強力なパートナー。',
    'Coca-Cola', 'HONDA', 'NTTデータ / BMW',
    '基本この3つ。', '180,000円', '19,800円', '59,800円', '9,800円',
    'LINEで無料相談',
]
for item in required:
    if item not in s:
        raise SystemExit(f'Missing final sales item: {item}')
