from pathlib import Path
import re

p=Path("public/index.html")
s=p.read_text(encoding="utf-8")

section=r'''<section class="section stock-ai-simple stock-v73" id="ai">
  <div class="container">
    <div class="stock-v73-head">
      <span class="stock-v73-kicker">FLOW → STOCK</span>
      <h2>消える広告より、<br><em>残る広告塔。</em></h2>
      <p>単発でお金をかけ続ける集客から、自前に積み上がる集客へ。</p>
    </div>

    <div class="stock-v73-compare">
      <article class="stock-v73-card stock-v73-flow">
        <div class="stock-v73-label">フロー型｜掛け捨て</div>
        <h3>チラシ・グルメサイト・<br>インフルエンサー広告</h3>
        <ul>
          <li>お金をかけている間だけ見られる</li>
          <li>止めると集客も止まりやすい</li>
          <li>一過性で、資産として残りにくい</li>
        </ul>
      </article>

      <div class="stock-v73-arrow">→</div>

      <article class="stock-v73-card stock-v73-stock">
        <div class="stock-v73-label">ストック型｜将来の経営資産</div>
        <h3>SNS・Google・<br>自前の情報インフラ</h3>
        <ul>
          <li>情報が残り続ける</li>
          <li>見つかる入口が増えていく</li>
          <li>時間とともに信頼が積み上がる</li>
        </ul>
        <strong>永続的に働く、無料の広告塔へ</strong>
      </article>
    </div>

    <div class="stock-v73-infra">
      <span>OWNED MEDIA INFRASTRUCTURE</span>
      <h3>自前の情報発信インフラを育てる。</h3>
    </div>

    <div class="stock-v73-ai">
      <span>LOCAL VALUE</span>
      <h3>AIには作れない価値が、<br><em>小金井にはすでにある！</em></h3>
      <p>土地・歴史・時間・思い出・地域とのつながり。<br>それを、ネット上から消えない資産にする。</p>
    </div>
  </div>
</section>'''

css=r'''
<style id="stock-ai-simple-style">
.stock-v73{padding:92px 0!important;background:linear-gradient(145deg,#031735,#082c60)!important;color:#fff!important}
.stock-v73 .container{max-width:1120px!important}
.stock-v73-head{text-align:left!important}
.stock-v73-kicker{display:inline-flex!important;align-items:center!important;gap:12px!important;color:#f0d995!important;font-size:.76rem!important;font-weight:900!important;letter-spacing:.16em!important}
.stock-v73-kicker:before,.stock-v73-kicker:after{content:""!important;width:34px!important;height:2px!important;background:#f0d995!important}
.stock-v73-head h2{margin:16px 0 0!important;color:#fff!important;font-size:clamp(2.8rem,5.8vw,5.4rem)!important;line-height:1.03!important;letter-spacing:-.055em!important}
.stock-v73-head h2 em{font-style:normal!important;color:#f0c45a!important}
.stock-v73-head p{margin:14px 0 0!important;color:rgba(255,255,255,.78)!important;font-size:1.05rem!important;font-weight:800!important}

.stock-v73-compare{display:grid!important;grid-template-columns:1fr 70px 1fr!important;gap:18px!important;align-items:center!important;margin-top:34px!important}
.stock-v73-card{min-height:315px!important;padding:28px!important;border-radius:28px!important;display:flex!important;flex-direction:column!important}
.stock-v73-flow{background:rgba(255,255,255,.08)!important;border:1px solid rgba(255,255,255,.16)!important}
.stock-v73-stock{background:#fff8e8!important;border:1px solid #efd89d!important;color:#071d3f!important}
.stock-v73-label{display:inline-flex!important;align-self:flex-start!important;padding:7px 11px!important;border-radius:999px!important;background:rgba(255,255,255,.10)!important;color:#f0d995!important;font-size:.72rem!important;font-weight:900!important}
.stock-v73-stock .stock-v73-label{background:#c99426!important;color:#fff!important}
.stock-v73-card h3{margin:18px 0 0!important;font-size:clamp(1.45rem,2.5vw,2.15rem)!important;line-height:1.25!important;color:inherit!important}
.stock-v73-card ul{margin:22px 0 0!important;padding:0!important;list-style:none!important;display:grid!important;gap:12px!important}
.stock-v73-card li{position:relative!important;padding-left:25px!important;font-size:.98rem!important;line-height:1.55!important;color:inherit!important}
.stock-v73-card li:before{position:absolute!important;left:0!important;top:0!important;font-weight:900!important}
.stock-v73-flow li:before{content:"×"!important;color:#c9d3df!important}
.stock-v73-stock li:before{content:"✓"!important;color:#b77e10!important}
.stock-v73-stock strong{margin-top:auto!important;padding-top:22px!important;color:#a56f0a!important;font-size:1.18rem!important}
.stock-v73-arrow{text-align:center!important;font-size:3.2rem!important;font-weight:900!important;color:#f0d995!important}

.stock-v73-infra{margin-top:24px!important;padding:26px!important;border-radius:26px!important;background:#fff8e8!important;border:1px solid #efd89d!important;text-align:center!important;box-shadow:0 14px 30px rgba(188,130,19,.10)!important}
.stock-v73-infra span{display:block!important;color:#a56f0a!important;font-size:.7rem!important;font-weight:900!important;letter-spacing:.14em!important}
.stock-v73-infra h3{margin:7px 0 0!important;color:#071d3f!important;font-size:clamp(1.8rem,3.4vw,3.1rem)!important;line-height:1.15!important}

.stock-v73-ai{margin-top:20px!important;padding:32px 28px!important;border-radius:28px!important;background:#fff8e8!important;border:1px solid #efd89d!important;text-align:center!important;color:#071d3f!important}
.stock-v73-ai>span{display:block!important;color:#a56f0a!important;font-size:.72rem!important;font-weight:900!important;letter-spacing:.14em!important}
.stock-v73-ai h3{margin:8px 0 0!important;color:#071d3f!important;font-size:clamp(2rem,4vw,3.8rem)!important;line-height:1.08!important;letter-spacing:-.04em!important}
.stock-v73-ai h3 em{font-style:normal!important;color:#c68d1d!important}
.stock-v73-ai p{margin:14px 0 0!important;color:#526178!important;font-size:1rem!important;line-height:1.75!important;font-weight:700!important}

@media(max-width:820px){
  .stock-v73{padding:68px 0!important}
  .stock-v73-compare{grid-template-columns:1fr!important}
  .stock-v73-arrow{transform:rotate(90deg)!important;line-height:1!important}
  .stock-v73-card{min-height:auto!important}
}
@media(max-width:560px){
  .stock-v73-head h2{font-size:clamp(2.2rem,11vw,3.4rem)!important}
  .stock-v73-card,.stock-v73-infra,.stock-v73-ai{padding:22px 18px!important}
}
</style>'''

# Replace AI section.
ai_pattern=r'<section class="section (?:ai|ai-final)[^"]*" id="ai">.*?</section>'
s,n=re.subn(ai_pattern,section,s,count=1,flags=re.S)
if n!=1:
    raise SystemExit("AI section replacement failed")

# Remove separate infra section because its message is now consolidated here.
infra_pattern=r'<section class="section infra" id="infra">.*?</section>'
s,n2=re.subn(infra_pattern,'',s,count=1,flags=re.S)
if n2 not in (0,1):
    raise SystemExit("Infra section removal failed")

# Remove prior simple stock CSS if rerun and append final CSS in head.
s=re.sub(r'<style id="stock-ai-simple-style">.*?</style>','',s,flags=re.S)
if '</head>' not in s:
    raise SystemExit("Missing </head>")
s=s.replace('</head>',css+'\n</head>',1)

p.write_text(s,encoding="utf-8")

required=[
  '消える広告より、<br><em>残る広告塔。</em>',
  'チラシ・グルメサイト・<br>インフルエンサー広告',
  'SNS・Google・<br>自前の情報インフラ',
  '永続的に働く、無料の広告塔へ',
  '自前の情報発信インフラを育てる。',
  'AIには作れない価値が、<br><em>小金井にはすでにある！</em>',
  'ネット上から消えない資産にする。',
  'id="stock-ai-simple-style"'
]
for token in required:
    if token not in s:
        raise SystemExit(f"Missing stock-ai token: {token}")
