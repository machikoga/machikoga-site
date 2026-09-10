from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

# ------------------------------------------------------------
# 1) Brand motto in the hero
# ------------------------------------------------------------
hero_start = s.find('<section class="hero"')
hero_end = s.find('</section>', hero_start)
if hero_start != -1 and hero_end != -1:
    hero = s[hero_start:hero_end]
    if 'hero-motto' not in hero:
        hero = hero.replace('<span class="kicker">KOGANEI LOCAL BRANDING</span>', '<div class="hero-motto">小金井をオモロく。</div><span class="kicker">KOGANEI LOCAL BRANDING</span>', 1)
    s = s[:hero_start] + hero + s[hero_end:]

# ------------------------------------------------------------
# 2) Fix awkward line breaks in the hero bubble
# ------------------------------------------------------------
hero_bubble = '''<div class="hero-bubble"><p class="hero-bubble-main">頑張る量を増やすのではなく、<br><span>今の発信の価値を上げる。</span></p><p class="hero-bubble-sub">小金井で見つかり、選ばれる仕組みを一緒につくります。</p></div>'''
s = re.sub(r'<div class="hero-bubble">.*?</div>', hero_bubble, s, count=1, flags=re.S)

# ------------------------------------------------------------
# 3) CEO focus card: force a clean two-line headline
# ------------------------------------------------------------
s = re.sub(
    r'<strong class="focus-message">.*?</strong>',
    '<strong class="focus-message"><span>社長は、</span><em>本業に集中してください。</em></strong>',
    s,
    count=1,
    flags=re.S,
)

# ------------------------------------------------------------
# 4) Long result copy: control the cafe card line breaks
# ------------------------------------------------------------
s = s.replace(
    '3ヶ月で<br>小金井フォロワー300人',
    '3ヶ月で<br><span class="result-long-line">小金井フォロワー</span><br><span class="result-big-number">300人</span>'
)
s = s.replace(
    '3ヶ月で小金井フォロワー300人',
    '3ヶ月で<br><span class="result-long-line">小金井フォロワー</span><br><span class="result-big-number">300人</span>'
)

# ------------------------------------------------------------
# 5) Service wording - clear first-read language
# ------------------------------------------------------------
s = s.replace('<h3>まちアカ掲載</h3>', '<h3>小金井専用ポータルサイト</h3>')
s = s.replace('<h3>小金井ポータル掲載</h3>', '<h3>小金井専用ポータルサイト</h3>')
s = s.replace('まちアカ掲載', '小金井ポータル掲載')

# ------------------------------------------------------------
# 6) Other services wording
# ------------------------------------------------------------
s = s.replace('<h3>取材・広告・その他</h3>', '<h3>取材・広告・HP作成など、なんでも相談。</h3>')
s = s.replace(
    '取材依頼、広告・PRのご相談、地域イベント、コラボ企画など。内容がまだ固まっていなくても大丈夫です。',
    '取材依頼、広告・PR、ホームページ作成、地域イベント、コラボ企画など。内容がまだ固まっていなくても大丈夫です。'
)

# ------------------------------------------------------------
# 7) Comparison section - all-in-one value, with public market ranges
# ------------------------------------------------------------
compare_html = '''<section class="section compare" id="compare"><div class="container"><span class="kicker">ALL-IN-ONE COST</span><h2>別々に頼むより、<br>まとめるから始めやすい。</h2><p class="lead compare-lead">SNS・Googleマップ・WEB・撮影を別会社へ分けると、費用も窓口も増えがちです。まちこがは、小金井で必要な導線をひとつにまとめ、必要な分だけ設計します。</p><div class="compare-grid"><article class="compare-card compare-market"><span class="compare-label">一般的な別発注の目安</span><h3>それぞれ外注すると、<br>費用が積み重なります。</h3><div class="market-prices"><div><b>月5〜50万円</b><span>SNS運用代行</span></div><div><b>月1〜5万円</b><span>MEO / Googleマップ対策</span></div><div><b>50〜100万円</b><span>企業サイト制作の一例</span></div><div><b>別途</b><span>写真・動画撮影など</span></div></div><p>依頼範囲や会社によって大きく変わりますが、施策ごとに会社を分けると、初期費用と月額費用が重なりやすくなります。</p></article><article class="compare-card compare-machikoga"><span class="compare-label">まちこが｜ALL IN ONE</span><h3>必要な土台をまとめて、<br><span class="compare-price-accent">参考18万円から。</span></h3><div class="compare-points"><div><b>一括設計</b><span>Instagram × Google × 小金井ポータル</span></div><div><b>必要な分だけ</b><span>全部を契約する必要はありません</span></div><div><b>地域を知る伴走者</b><span>小金井在住11年目のぶるが一緒に進めます</span></div></div><strong class="compare-main-copy">安いだけではなく、<br>小金井で使える形まで一緒につくる。</strong><p class="compare-subcopy">大きな制作会社に丸投げするのではなく、地域の現場を知る人と、必要なところから始められます。</p></article></div><div class="compare-summary"><span>一般的な別発注</span><b>複数社・複数費用・複数窓口</b><i>→</i><span>まちこが</span><strong>必要な施策を、ひとつの窓口で。</strong></div><small class="compare-note">※一般的な相場は2026年公開の相場記事を参考にした目安です。SNS運用：月5〜50万円程度、MEO：月1〜5万円程度、企業サイト：50〜100万円程度の例があります。内容・範囲・事業者により異なります。参考：Epace、株式会社オークス、Web幹事。まちこがの金額も参考価格で、実際は内容に合わせて個別にご提案します。</small></div></section>'''

if 'id="compare"' in s:
    s = re.sub(r'<section class="section compare" id="compare">.*?</section>', compare_html, s, count=1, flags=re.S)
else:
    marker = '<section class="section pricing'
    idx = s.find(marker)
    if idx != -1:
        s = s[:idx] + compare_html + '\n' + s[idx:]

# ------------------------------------------------------------
# 8) Final typography / controlled line breaks / comparison design
# ------------------------------------------------------------
css = r'''
/* V68 FINAL COPY PASS */
.hero-motto{display:inline-flex;margin-bottom:10px;padding:6px 12px;border-radius:999px;background:rgba(240,217,149,.12);border:1px solid rgba(240,217,149,.35);color:#f0d995;font-size:.82rem;font-weight:900;letter-spacing:.05em}

/* Consistent alignment */
.cta-in,.pricing-final,.other-services,.compare,.offer-card,.result-impact,.empathy-card,.setup-card-final,.plan-card{text-align:left!important}
.cta-actions{justify-content:flex-start!important}.cta-note{display:block;text-align:left!important}.other-service-body{text-align:left!important}
.section h2,.section h3{word-break:keep-all;overflow-wrap:normal;text-wrap:balance}

/* Hero bubble: two clean lines */
.hero-bubble{width:min(480px,100%)!important;max-width:480px!important;padding:20px 22px!important}
.hero-bubble-main{font-size:clamp(1.15rem,1.55vw,1.52rem)!important;line-height:1.45!important;letter-spacing:-.02em!important}
.hero-bubble-main span{display:inline-block!important;white-space:nowrap!important;color:#f0d995!important;font-size:1.08em!important}
.hero-bubble-sub{font-size:.86rem!important;line-height:1.6!important}

/* CEO card: exactly two headline rows on desktop */
.focus-message{display:block!important;line-height:1.02!important;letter-spacing:-.04em!important}
.focus-message span{display:block!important;font-size:clamp(1.8rem,2.8vw,2.7rem)!important;color:#fff!important}
.focus-message em{display:block!important;margin-top:6px!important;font-size:clamp(2.05rem,3.55vw,3.45rem)!important;color:#f0d995!important;font-style:normal!important;white-space:nowrap!important}
.buru-tip-final p{margin-top:18px!important;max-width:34em!important;font-size:.94rem!important;line-height:1.75!important}

/* Result cards: prevent ugly single-character wraps */
.result-impact>strong{font-size:clamp(1.35rem,2vw,1.75rem)!important;line-height:1.28!important}
.result-long-line{display:inline-block;white-space:nowrap;font-size:.94em}
.result-big-number{display:inline-block;font-size:1.35em;line-height:1.05}

/* Comparison */
.compare{background:linear-gradient(180deg,#fff 0%,#f4f7fb 100%)}
.compare h2{max-width:11em;color:var(--navy)}
.compare-lead{max-width:900px;margin-top:16px}
.compare-grid{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:32px;align-items:stretch}
.compare-card{padding:30px;border-radius:30px;border:1px solid var(--line);box-shadow:0 18px 44px rgba(5,25,57,.08)}
.compare-market{background:#fff}
.compare-machikoga{background:linear-gradient(145deg,#061a38 0%,#0a3567 62%,#0a6570 100%);color:#fff;border-color:rgba(240,217,149,.35)}
.compare-label{display:inline-flex;padding:6px 10px;border-radius:999px;background:#eef2f7;color:#516078;font-size:.67rem;font-weight:900;letter-spacing:.08em}
.compare-machikoga .compare-label{background:#f0d995;color:#061a38}
.compare-card h3{margin-top:14px;font-size:clamp(1.55rem,2.4vw,2.2rem);line-height:1.24;color:var(--navy)}
.compare-machikoga h3{color:#fff}.compare-price-accent{color:#f0d995}
.market-prices,.compare-points{display:grid;gap:9px;margin-top:20px}
.market-prices div,.compare-points div{display:grid;grid-template-columns:minmax(120px,.72fr) 1fr;align-items:center;gap:14px;padding:14px 16px;border-radius:17px;background:#f5f7fa;border:1px solid #e2e8ef}
.market-prices b{font-size:1.22rem;color:#9b6a26;white-space:nowrap}.market-prices span{font-size:.8rem;color:#66748a;font-weight:800}
.compare-points div{background:rgba(255,255,255,.09);border-color:rgba(255,255,255,.12)}
.compare-points b{color:#f0d995}.compare-points span{color:rgba(255,255,255,.76);font-size:.8rem}
.compare-market p{margin-top:18px;color:var(--text);font-size:.86rem}.compare-main-copy{display:block;margin-top:21px;padding-top:18px;border-top:1px solid rgba(255,255,255,.18);font-size:clamp(1.2rem,1.8vw,1.55rem);line-height:1.5;color:#fff}.compare-subcopy{margin-top:10px;color:rgba(255,255,255,.73);font-size:.86rem;line-height:1.7}
.compare-summary{display:grid;grid-template-columns:auto auto 34px auto 1fr;gap:12px;align-items:center;margin-top:18px;padding:16px 18px;border-radius:18px;background:#071d3f;color:#fff;font-size:.8rem}.compare-summary span{color:#f0d995;font-weight:900}.compare-summary b{font-weight:800}.compare-summary i{font-style:normal;text-align:center;color:#46c5b8;font-size:1.2rem}.compare-summary strong{font-size:1rem}
.compare-note{display:block;margin-top:12px;color:#7b8798;font-size:.66rem;line-height:1.6}

/* Other services / general text balance */
.other-service-photo{aspect-ratio:16/9!important;background:#0b2348}.other-service-photo img{width:100%;height:100%;object-fit:cover;image-rendering:auto}.other-service-body h3{font-size:clamp(1.35rem,2vw,1.7rem);line-height:1.3}.offer-card p,.result-impact p,.plan-card p,.other-service-body p{line-height:1.7}.offer-card,.result-impact,.plan-card,.other-service-card{min-width:0}
.pricing-final .reference-price strong{font-size:clamp(1.45rem,2.2vw,2rem)!important}.pricing-final .plan-card h3{font-size:clamp(1.35rem,2vw,1.75rem)!important}.pricing-final .plan-card h3 small{font-size:.68rem!important;color:#9b6a26!important}

@media(max-width:980px){
  .focus-message em{white-space:normal!important}
  .compare-grid{grid-template-columns:1fr}
  .compare-summary{grid-template-columns:1fr;gap:5px}.compare-summary i{transform:rotate(90deg)}
}
@media(max-width:780px){
  .hero-motto{font-size:.73rem}
  .hero-bubble{max-width:100%!important}
  .hero-bubble-main{font-size:1.05rem!important}
  .hero-bubble-main span{white-space:normal!important}
  .focus-message span{font-size:1.65rem!important}.focus-message em{font-size:2.2rem!important}
  .compare-card{padding:22px 20px}
  .market-prices div,.compare-points div{grid-template-columns:1fr;gap:3px}
  .market-prices b{white-space:normal}
  .cta-actions{display:grid!important;grid-template-columns:1fr!important;width:100%}.cta-actions .btn{width:100%}
}
'''

if '/* V68 FINAL COPY PASS */' in s:
    s = re.sub(r'/\* V68 FINAL COPY PASS \*/.*?(?=</style>)', css.strip() + '\n', s, count=1, flags=re.S)
else:
    s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

required = [
    '今の発信の価値を上げる。',
    '本業に集中してください。',
    'result-big-number',
    'ALL-IN-ONE COST',
    '月5〜50万円',
    '月1〜5万円',
    '参考18万円から',
    '小金井在住11年目',
    'V68 FINAL COPY PASS',
]
for item in required:
    if item not in s:
        raise SystemExit(f'Missing final copy token: {item}')
