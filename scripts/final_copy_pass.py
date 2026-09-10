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
# 2) Other services final wording
# ------------------------------------------------------------
s = s.replace('<h3>取材・広告・その他</h3>', '<h3>取材・広告・HP作成など、なんでも相談。</h3>')
s = s.replace(
    '取材依頼、広告・PRのご相談、地域イベント、コラボ企画など。内容がまだ固まっていなくても大丈夫です。',
    '取材依頼、広告・PR、ホームページ作成、地域イベント、コラボ企画など。内容がまだ固まっていなくても大丈夫です。'
)

# ------------------------------------------------------------
# 3) Service wording - make Machiaka understandable on first read
# ------------------------------------------------------------
s = s.replace('<h3>まちアカ掲載</h3>', '<h3>小金井専用ポータルサイト</h3>')
s = s.replace('<h3>小金井ポータル掲載</h3>', '<h3>小金井専用ポータルサイト</h3>')
s = s.replace('まちアカ掲載', '小金井ポータル掲載')

# ------------------------------------------------------------
# 4) Comparison section before pricing
#    Uses the market-guide figures from the user's own sales deck.
# ------------------------------------------------------------
compare_html = '''<section class="section compare" id="compare"><div class="container"><span class="kicker">COST & LOCAL SUPPORT</span><h2>一般的な相場と比べても、<br>かなり始めやすい。</h2><p class="lead compare-lead">WEB・SNS・Google・撮影を別々に頼むのではなく、必要なものだけをまとめて設計。しかも、小金井を知るぶるが一緒に伴走します。</p><div class="compare-grid"><article class="compare-card compare-market"><span class="compare-label">一般的な相場目安</span><h3>施策ごとに別々に頼むと、<br>費用も管理も増えやすい。</h3><div class="market-prices"><div><b>10〜50万円</b><span>Googleマップ初期設計</span></div><div><b>10〜50万円</b><span>Instagram初期設計</span></div><div><b>50万円〜</b><span>サイト構築</span></div></div><p>制作会社・SNS運用・Google対策・撮影など、窓口が分かれるほど地域の情報共有や管理コストも増えがちです。</p></article><article class="compare-card compare-machikoga"><span class="compare-label">まちこが</span><h3>必要な土台をまとめて、<br>参考18万円から。</h3><div class="compare-points"><div><b>必要な施策だけ</b><span>全部を契約する必要なし</span></div><div><b>地域導線を一括設計</b><span>Instagram × Google × 小金井</span></div><div><b>ぶるが伴走</b><span>小金井在住11年目・地域目線</span></div></div><strong class="compare-main-copy">大きく作るより、必要なところから。<br>小金井を知るぶるが、一緒に育てます。</strong></article></div><small class="compare-note">※相場は当社説明資料で使用している一般的な目安です。内容・範囲・事業者により異なります。まちこがの表示金額も参考価格で、実際はご相談内容に合わせて個別にご提案します。</small></div></section>'''

if 'id="compare"' in s:
    s = re.sub(r'<section class="section compare" id="compare">.*?</section>', compare_html, s, count=1, flags=re.S)
else:
    marker = '<section class="section pricing'
    idx = s.find(marker)
    if idx != -1:
        s = s[:idx] + compare_html + '\n' + s[idx:]

# ------------------------------------------------------------
# 5) Pricing final copy - reference / custom-order first
# ------------------------------------------------------------
s = s.replace('料金は、事業に合わせて<br>オーダーメイド。', '料金は、事業に合わせて<br>オーダーメイド。')
s = s.replace('下記は参考価格です。必要な施策・撮影範囲・更新頻度・運用サポートに合わせて、内容も金額も個別にご提案します。', '下記は参考価格です。必要な施策・撮影範囲・更新頻度・運用サポートに合わせて、内容も金額も個別にご提案します。')

# ------------------------------------------------------------
# 6) Final CTA - preserve copy, align left through CSS
# ------------------------------------------------------------

# ------------------------------------------------------------
# 7) Final typography / alignment / visual hierarchy
# ------------------------------------------------------------
css = r'''
/* V68 FINAL COPY PASS */
.hero-motto{display:inline-flex;margin-bottom:10px;padding:6px 12px;border-radius:999px;background:rgba(240,217,149,.12);border:1px solid rgba(240,217,149,.35);color:#f0d995;font-size:.82rem;font-weight:900;letter-spacing:.05em}

/* Text alignment system */
.cta-in,.pricing-final,.other-services,.compare,.offer-card,.result-impact,.empathy-card,.setup-card-final,.plan-card{text-align:left!important}
.cta-actions{justify-content:flex-start!important}
.cta-note{display:block;text-align:left!important}
.other-service-body{text-align:left!important}

/* Headings should break by phrase, not character */
.section h2,.section h3{word-break:keep-all;overflow-wrap:normal;text-wrap:balance}

/* Comparison */
.compare{background:linear-gradient(180deg,#fff 0%,#f4f7fb 100%)}
.compare h2{max-width:12em;color:var(--navy)}
.compare-lead{max-width:860px;margin-top:16px}
.compare-grid{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:32px;align-items:stretch}
.compare-card{padding:30px;border-radius:28px;border:1px solid var(--line);box-shadow:0 18px 44px rgba(5,25,57,.08)}
.compare-market{background:#fff}
.compare-machikoga{background:linear-gradient(145deg,#061a38 0%,#0a3567 62%,#0a6570 100%);color:#fff;border-color:rgba(240,217,149,.35)}
.compare-label{display:inline-flex;padding:6px 10px;border-radius:999px;background:#eef2f7;color:#516078;font-size:.67rem;font-weight:900;letter-spacing:.08em}
.compare-machikoga .compare-label{background:#f0d995;color:#061a38}
.compare-card h3{margin-top:14px;font-size:clamp(1.55rem,2.4vw,2.25rem);line-height:1.25;color:var(--navy)}
.compare-machikoga h3{color:#fff}
.market-prices,.compare-points{display:grid;gap:9px;margin-top:20px}
.market-prices div,.compare-points div{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:13px 15px;border-radius:16px;background:#f5f7fa;border:1px solid #e2e8ef}
.market-prices b{font-size:1.2rem;color:#9b6a26}.market-prices span{font-size:.78rem;color:#66748a;font-weight:800;text-align:right}
.compare-points div{background:rgba(255,255,255,.09);border-color:rgba(255,255,255,.12)}
.compare-points b{color:#f0d995}.compare-points span{color:rgba(255,255,255,.72);font-size:.78rem;text-align:right}
.compare-market p{margin-top:18px;color:var(--text);font-size:.86rem}
.compare-main-copy{display:block;margin-top:21px;padding-top:18px;border-top:1px solid rgba(255,255,255,.18);font-size:1.08rem;line-height:1.55;color:#fff}
.compare-note{display:block;margin-top:13px;color:#7b8798;font-size:.68rem;line-height:1.6}

/* Other services image quality and proportions */
.other-service-photo{aspect-ratio:16/9!important;background:#0b2348}
.other-service-photo img{width:100%;height:100%;object-fit:cover;image-rendering:auto}
.other-service-grid .other-service-card:nth-child(1) .other-service-photo img{object-position:center 42%}
.other-service-grid .other-service-card:nth-child(2) .other-service-photo img{object-position:center center}
.other-service-body h3{font-size:clamp(1.35rem,2vw,1.7rem);line-height:1.3}

/* Card text balance */
.offer-card p,.result-impact p,.plan-card p,.other-service-body p{line-height:1.7}
.offer-card,.result-impact,.plan-card,.other-service-card{min-width:0}

/* Pricing: amounts are references, not the hero */
.pricing-final .reference-price strong{font-size:clamp(1.45rem,2.2vw,2rem)!important}
.pricing-final .plan-card h3{font-size:clamp(1.35rem,2vw,1.75rem)!important}
.pricing-final .plan-card h3 small{font-size:.68rem!important;color:#9b6a26!important}

@media(max-width:900px){.compare-grid{grid-template-columns:1fr}}
@media(max-width:780px){
  .hero-motto{font-size:.73rem}
  .compare-card{padding:22px 20px}
  .market-prices div,.compare-points div{align-items:flex-start;flex-direction:column;gap:3px}
  .market-prices span,.compare-points span{text-align:left}
  .cta-actions{display:grid!important;grid-template-columns:1fr!important;width:100%}
  .cta-actions .btn{width:100%}
}
'''

if '/* V68 FINAL COPY PASS */' in s:
    s = re.sub(r'/\* V68 FINAL COPY PASS \*/.*?(?=</style>)', css.strip() + '\n', s, count=1, flags=re.S)
else:
    s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

required = [
    '小金井をオモロく。',
    '小金井専用ポータルサイト',
    '一般的な相場と比べても',
    '小金井在住11年目',
    '取材・広告・HP作成など、なんでも相談。',
    'V68 FINAL COPY PASS',
]
for item in required:
    if item not in s:
        raise SystemExit(f'Missing final copy token: {item}')
