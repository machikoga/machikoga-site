from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

compare_html = '''<section class="section compare" id="compare"><div class="container">
<span class="kicker">ALL-IN-ONE DESIGN</span>
<h2>別々に頼むより、<br>ひとつにつなぐ。</h2>
<p class="lead compare-lead">SNS・Googleマップ・WEB・撮影を別々に管理するのではなく、小金井で必要な導線をひとつの設計にまとめます。</p>
<div class="compare-grid">
  <article class="compare-card compare-market">
    <span class="compare-label">一般的な別発注</span>
    <h3>施策ごとに分けると、<br>窓口も管理も増えやすい。</h3>
    <div class="market-prices">
      <div><b>SNS運用</b><span>別契約・別担当</span></div>
      <div><b>Google / MEO</b><span>別契約・別担当</span></div>
      <div><b>WEB</b><span>別制作・別管理</span></div>
      <div><b>写真・動画</b><span>必要時に別手配</span></div>
    </div>
    <p>それぞれを個別に頼むと、情報や方針が分かれ、更新や管理の手間も増えやすくなります。</p>
  </article>
  <article class="compare-card compare-machikoga">
    <span class="compare-label">まちこが｜ALL IN ONE</span>
    <h3>必要な土台をまとめて、<br><span class="compare-price-accent">小金井で使える形に。</span></h3>
    <div class="compare-points">
      <div><b>一括設計</b><span>Instagram × Google × 小金井ポータル</span></div>
      <div><b>必要な分だけ</b><span>今の状況に合わせて組み立てます</span></div>
      <div><b>地域を知る伴走者</b><span>小金井を知るぶるが一緒に進めます</span></div>
    </div>
    <strong class="compare-main-copy">安さだけではなく、<br>小金井で使える仕組みを一緒につくる。</strong>
    <p class="compare-subcopy">新サービス開始に向けて、提供内容・プランを再設計しています。</p>
  </article>
</div>
<div class="compare-summary"><span>一般的な別発注</span><b>複数社・複数窓口</b><i>→</i><span>まちこが</span><strong>必要な施策を、ひとつの窓口で。</strong></div>
</div></section>'''

pricing_html = '''<section class="section pricing pricing-final" id="pricing"><div class="container">
<span class="kicker">NEW SERVICE / PRICE</span>
<h2>新サービス開始に向けて、<br>プラン・料金を再設計中です。</h2>
<p class="lead pricing-lead">現在、より使いやすいサービス構成へ見直しを進めています。必要な施策・撮影範囲・更新頻度・運用サポートに合わせて、内容を個別にご提案します。</p>
<div class="custom-note">
  <strong>まず「何が必要か」を一緒に整理します。</strong>
  <span>Instagram・Google・小金井ポータル・撮影など、必要なものだけを組み合わせます。</span>
</div>
<div class="setup-card setup-card-final">
  <div>
    <span>SERVICE DESIGN</span>
    <h3>内容はオーダーメイド</h3>
    <p>新サービスの詳細・プランは順次ご案内します。ご相談時点の最新内容でご提案します。</p>
  </div>
  <div class="reference-price custom-made">
    <small>STATUS</small>
    <strong>新プラン準備中</strong>
    <span>最新内容は個別にご案内</span>
  </div>
</div>
<div class="setup-items setup-items-final">
  <span>Googleマップ</span><span>Instagram</span><span>小金井ポータル</span><span>カスタムAI</span><span>口コミ導線</span><span>掲載ページ制作</span><span>写真・動画・空間3D</span><span>Google連携</span>
</div>
<div class="price-note price-note-final">
  <span>※新サービス開始予定のため、現在プラン・料金を改定しています。</span>
  <span>※最新の内容はお問い合わせ時にご案内します。</span>
</div>
<div class="section-cta"><a class="btn gold" href="#contact">新サービスについて相談する</a></div>
</div></section>'''

if 'id="compare"' in s:
    s = re.sub(r'<section class="section compare" id="compare">.*?</section>', compare_html, s, count=1, flags=re.S)

if 'id="pricing"' in s:
    s = re.sub(r'<section class="section pricing[^"]*" id="pricing">.*?</section>', pricing_html, s, count=1, flags=re.S)

# Safety sweep: remove any remaining visible currency amounts reintroduced by earlier build scripts.
patterns = [
    r'月\s*\d[\d,]*(?:〜\d[\d,]*)?万円(?:程度)?',
    r'\d[\d,]*(?:〜\d[\d,]*)?万円(?:程度|から)?',
    r'\d[\d,]*円(?:/月)?',
]
for pat in patterns:
    s = re.sub(pat, '', s)

css = r'''
/* V68 NO PRICE AMOUNTS */
.pricing-final .reference-price.custom-made strong{
  font-size:clamp(1.5rem,2.4vw,2.15rem)!important;
  white-space:normal!important;
}
.pricing-final .reference-price.custom-made{
  min-width:220px;
}
.compare-price-accent{
  color:#f0d995!important;
}
@media(max-width:780px){
  .pricing-final .reference-price.custom-made{
    min-width:0;
    text-align:left!important;
  }
}
'''
s = re.sub(r'/\* V68 NO PRICE AMOUNTS \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

for token in [
    '新サービス開始に向けて',
    '新プラン準備中',
    '内容はオーダーメイド',
    'V68 NO PRICE AMOUNTS',
]:
    if token not in s:
        raise SystemExit(f'Missing no-price token: {token}')

if re.search(r'\d[\d,]*円|\d[\d,]*(?:〜\d[\d,]*)?万円', s):
    raise SystemExit('Currency amount still remains in public/index.html')
