from pathlib import Path
import re

p=Path("public/index.html")
s=p.read_text(encoding="utf-8")

section=r'''<section class="section stock-ai-simple" id="ai">
  <div class="container">
    <div class="stock-ai-head">
      <span class="stock-ai-kicker">STOCK ASSET × LOCAL VALUE</span>
      <h2>消える発信から、<br><em>残る資産へ。</em></h2>
    </div>

    <div class="stock-ai-flow">
      <article class="stock-ai-card stock-ai-flowtype">
        <span class="stock-ai-mark">×</span>
        <div>
          <small>FLOW TYPE</small>
          <h3>投稿・広告は<br>流れて消える</h3>
        </div>
      </article>

      <div class="stock-ai-arrow">→</div>

      <article class="stock-ai-card stock-ai-stocktype">
        <span class="stock-ai-mark">○</span>
        <div>
          <small>STOCK TYPE</small>
          <h3>SNS・Google・地域情報を<br>積み上げる</h3>
        </div>
      </article>
    </div>

    <div class="stock-ai-infra">
      <span>OWNED MEDIA INFRASTRUCTURE</span>
      <strong>自前の情報発信インフラを持つ。</strong>
      <p>土地・歴史・時間・思い出・地域とのつながり。</p>
    </div>

    <div class="stock-ai-result">
      <p>AIには作れない価値が、小金井にはある。</p>
      <strong>それを、ネット上から消えない資産にする。</strong>
    </div>
  </div>
</section>'''

css=r'''
<style id="stock-ai-simple-style">
.stock-ai-simple{padding:92px 0!important;background:linear-gradient(145deg,#031735,#082c60)!important;color:#fff!important}
.stock-ai-simple .container{max-width:1120px!important}
.stock-ai-head{text-align:center!important}
.stock-ai-kicker{display:inline-flex!important;align-items:center!important;gap:12px!important;color:#f0d995!important;font-size:.76rem!important;font-weight:900!important;letter-spacing:.16em!important}
.stock-ai-kicker:before,.stock-ai-kicker:after{content:""!important;width:34px!important;height:2px!important;background:#f0d995!important}
.stock-ai-head h2{margin:16px 0 0!important;color:#fff!important;font-size:clamp(2.8rem,5.8vw,5.4rem)!important;line-height:1.03!important;letter-spacing:-.055em!important}
.stock-ai-head h2 em{font-style:normal!important;color:#f0c45a!important}
.stock-ai-flow{display:grid!important;grid-template-columns:1fr 70px 1fr!important;gap:18px!important;align-items:center!important;margin-top:34px!important}
.stock-ai-card{min-height:170px!important;padding:28px!important;border-radius:28px!important;display:flex!important;align-items:center!important;gap:20px!important}
.stock-ai-flowtype{background:rgba(255,255,255,.08)!important;border:1px solid rgba(255,255,255,.16)!important}
.stock-ai-stocktype{background:linear-gradient(145deg,#fffdf7,#fff4d9)!important;border:1px solid rgba(240,196,90,.55)!important;color:#071d3f!important}
.stock-ai-mark{width:64px!important;height:64px!important;border-radius:50%!important;display:grid!important;place-items:center!important;flex:0 0 auto!important;font-size:2.2rem!important;font-weight:900!important}
.stock-ai-flowtype .stock-ai-mark{background:rgba(255,255,255,.12)!important;color:#c9d3df!important}
.stock-ai-stocktype .stock-ai-mark{background:#c99426!important;color:#fff!important}
.stock-ai-card small{display:block!important;font-size:.68rem!important;font-weight:900!important;letter-spacing:.14em!important;color:#b9c7d7!important}
.stock-ai-stocktype small{color:#a67518!important}
.stock-ai-card h3{margin:8px 0 0!important;font-size:clamp(1.5rem,2.5vw,2.2rem)!important;line-height:1.25!important;letter-spacing:-.025em!important;color:inherit!important}
.stock-ai-arrow{text-align:center!important;font-size:3.2rem!important;font-weight:900!important;color:#f0d995!important}
.stock-ai-infra{margin-top:24px!important;padding:28px!important;border-radius:28px!important;background:rgba(255,255,255,.09)!important;border:1px solid rgba(255,255,255,.16)!important;text-align:center!important}
.stock-ai-infra span{display:block!important;color:#f0d995!important;font-size:.7rem!important;font-weight:900!important;letter-spacing:.14em!important}
.stock-ai-infra strong{display:block!important;margin-top:7px!important;color:#fff!important;font-size:clamp(1.8rem,3.5vw,3.2rem)!important;line-height:1.15!important}
.stock-ai-infra p{margin:10px 0 0!important;color:rgba(255,255,255,.72)!important;font-size:1rem!important}
.stock-ai-result{margin-top:20px!important;padding:32px 28px!important;border-radius:28px!important;background:#fff!important;color:#071d3f!important;text-align:center!important;box-shadow:0 22px 48px rgba(0,0,0,.18)!important}
.stock-ai-result p{margin:0!important;font-size:clamp(1.05rem,1.8vw,1.4rem)!important;font-weight:800!important;color:#526178!important}
.stock-ai-result strong{display:block!important;margin-top:6px!important;font-size:clamp(1.8rem,3.7vw,3.5rem)!important;line-height:1.15!important;letter-spacing:-.035em!important;color:#071d3f!important}
@media(max-width:820px){
  .stock-ai-simple{padding:68px 0!important}
  .stock-ai-flow{grid-template-columns:1fr!important}
  .stock-ai-arrow{transform:rotate(90deg)!important;line-height:1!important}
}
@media(max-width:560px){
  .stock-ai-head h2{font-size:clamp(2.2rem,11vw,3.4rem)!important}
  .stock-ai-card{min-height:auto!important;padding:22px 18px!important}
  .stock-ai-mark{width:54px!important;height:54px!important;font-size:1.8rem!important}
  .stock-ai-infra,.stock-ai-result{padding:24px 18px!important}
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
if n2!=1:
    raise SystemExit("Infra section removal failed")

# Remove prior simple stock CSS if rerun and append final CSS in head.
s=re.sub(r'<style id="stock-ai-simple-style">.*?</style>','',s,flags=re.S)
if '</head>' not in s:
    raise SystemExit("Missing </head>")
s=s.replace('</head>',css+'\n</head>',1)

p.write_text(s,encoding="utf-8")

required=[
  '消える発信から、<br><em>残る資産へ。</em>',
  '投稿・広告は<br>流れて消える',
  'SNS・Google・地域情報を<br>積み上げる',
  '自前の情報発信インフラを持つ。',
  'AIには作れない価値が、小金井にはある。',
  'それを、ネット上から消えない資産にする。',
  'id="stock-ai-simple-style"'
]
for token in required:
    if token not in s:
        raise SystemExit(f"Missing stock-ai token: {token}")
