from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

compare_html = '''<section class="section compare compare-compact" id="compare"><div class="container">
<span class="kicker">ALL-IN-ONE DESIGN</span>
<h2>必要な発信を、<br>ひとつにつなぐ。</h2>
<p class="lead compare-lead">SNS・Google・WEB・撮影をバラバラにせず、小金井で使えるひとつの導線として設計します。</p>
<div class="compare-compact-row">
  <div class="compare-mini compare-mini-market">
    <span>一般的な別発注</span>
    <strong>SNS / Google / WEB / 撮影が分散</strong>
  </div>
  <div class="compare-arrow">→</div>
  <div class="compare-mini compare-mini-machikoga">
    <span>まちこが</span>
    <strong>必要な施策を、ひとつの窓口で。</strong>
  </div>
</div>
</div></section>'''

pricing_html = '''<section class="section pricing pricing-final pricing-new-plan" id="pricing"><div class="container">
<span class="kicker">NEW KOGANEI PORTAL</span>
<h2>小金井ポータルを、<br>大幅パワーアップします。</h2>
<p class="lead pricing-lead">新サービスとして、小金井ポータルそのものを大きく進化させる新プランを計画中です。さらに、新しい使い方を広げる追加オプションもあわせて計画しています。</p>
<div class="new-plan-grid">
  <article class="new-plan-card new-plan-main">
    <span>MAIN UPDATE</span>
    <h3>新プラン計画中</h3>
    <p>小金井ポータルをもっと強く、もっと使いやすく。地域で「見つかる・伝わる・選ばれる」を支えるサービスへ大幅アップデートします。</p>
  </article>
  <article class="new-plan-card new-plan-option">
    <span>NEW OPTIONS</span>
    <h3>追加オプションも計画中</h3>
    <p>事業や目的に合わせて、必要な機能・サポートを追加できる新しい形も検討しています。詳細は決まり次第ご案内します。</p>
  </article>
</div>
<div class="price-note price-note-final">
  <span>※新サービス開始予定のため、現在プラン・料金を改定しています。</span>
  <span>※最新情報はお問い合わせ時にご案内します。</span>
</div>
<div class="section-cta"><a class="btn gold" href="#contact">新サービスについて相談する</a></div>
</div></section>'''

if 'id="compare"' in s:
    s = re.sub(r'<section class="section compare[^"]*" id="compare">.*?</section>', compare_html, s, count=1, flags=re.S)

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
.pricing-new-plan .new-plan-grid{
  display:grid;
  grid-template-columns:1.15fr .85fr;
  gap:16px;
  margin-top:26px;
}
.pricing-new-plan .new-plan-card{
  min-width:0;
  padding:24px 24px 22px;
  border-radius:24px;
  border:1px solid rgba(255,255,255,.14);
  background:rgba(255,255,255,.08);
}
.pricing-new-plan .new-plan-card>span{
  display:inline-flex;
  padding:6px 10px;
  border-radius:999px;
  background:rgba(240,217,149,.13);
  color:#f0d995;
  font-size:.64rem;
  font-weight:900;
  letter-spacing:.1em;
}
.pricing-new-plan .new-plan-card h3{
  margin-top:12px;
  color:#fff;
  font-size:clamp(1.55rem,2.4vw,2.15rem);
  line-height:1.18;
}
.pricing-new-plan .new-plan-card p{
  margin-top:10px;
  color:rgba(255,255,255,.76);
  font-size:.9rem;
  line-height:1.75;
}
.pricing-new-plan .new-plan-main{
  background:linear-gradient(145deg,rgba(240,217,149,.12),rgba(255,255,255,.06));
  border-color:rgba(240,217,149,.28);
}
.compare-price-accent{
  color:#f0d995!important;
}
.compare-compact{
  padding:58px 0!important;
  background:linear-gradient(180deg,#fff,#f5f7fa)!important;
}
.compare-compact h2{
  max-width:9em!important;
  margin-top:10px!important;
  font-size:clamp(2.25rem,4vw,3.8rem)!important;
}
.compare-compact .compare-lead{
  max-width:760px!important;
  margin-top:14px!important;
}
.compare-compact-row{
  display:grid!important;
  grid-template-columns:minmax(0,1fr) 42px minmax(0,1fr)!important;
  gap:12px!important;
  align-items:center!important;
  margin-top:24px!important;
}
.compare-mini{
  min-width:0!important;
  padding:18px 20px!important;
  border-radius:20px!important;
  border:1px solid var(--line)!important;
  background:#fff!important;
}
.compare-mini span{
  display:block!important;
  margin-bottom:6px!important;
  color:#758197!important;
  font-size:.68rem!important;
  font-weight:900!important;
  letter-spacing:.06em!important;
}
.compare-mini strong{
  display:block!important;
  color:var(--navy)!important;
  font-size:1rem!important;
  line-height:1.55!important;
}
.compare-mini-machikoga{
  background:linear-gradient(135deg,#071d3f,#0a5a67)!important;
  border-color:rgba(240,217,149,.28)!important;
}
.compare-mini-machikoga span{color:#f0d995!important}
.compare-mini-machikoga strong{color:#fff!important}
.compare-arrow{
  text-align:center!important;
  color:#0c8b86!important;
  font-size:1.35rem!important;
  font-weight:900!important;
}
@media(max-width:780px){
  .pricing-final .reference-price.custom-made{
    min-width:0;
    text-align:left!important;
  }
  .pricing-new-plan .new-plan-grid{
    grid-template-columns:1fr;
  }
  .pricing-new-plan .new-plan-card{
    padding:20px;
    border-radius:20px;
  }
  .compare-compact{
    padding:48px 0!important;
  }
  .compare-compact-row{
    grid-template-columns:1fr!important;
    gap:8px!important;
  }
  .compare-arrow{
    transform:rotate(90deg)!important;
  }
}
'''
s = re.sub(r'/\* V68 NO PRICE AMOUNTS \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

for token in [
    '小金井ポータルを、',
    '大幅パワーアップします。',
    '新プラン計画中',
    '追加オプションも計画中',
    'V68 NO PRICE AMOUNTS',
]:
    if token not in s:
        raise SystemExit(f'Missing no-price token: {token}')

if re.search(r'\d[\d,]*円|\d[\d,]*(?:〜\d[\d,]*)?万円', s):
    raise SystemExit('Currency amount still remains in public/index.html')
