from pathlib import Path
import re

p=Path("public/index.html")
s=p.read_text(encoding="utf-8")

section=r'''<section class="section stock-ai-simple stock-v72" id="ai">
  <div class="container">
    <div class="stock-v72-head">
      <span class="stock-v72-kicker">FLOW → STOCK</span>
      <h2>消える広告より、<br><em>残る広告塔。</em></h2>
      <p>単発でお金をかけ続ける集客から、積み上がる集客へ。</p>
    </div>

    <div class="stock-v72-compare">
      <article class="stock-v72-card stock-v72-flow">
        <div class="stock-v72-label">フロー型｜掛け捨て</div>
        <h3>チラシ・グルメサイト・<br>インフルエンサー広告</h3>
        <ul>
          <li>お金をかけている間だけ見られる</li>
          <li>止めると集客も止まりやすい</li>
          <li>一過性で、資産として残りにくい</li>
        </ul>
        <strong>消費されて終わる情報</strong>
      </article>

      <div class="stock-v72-arrow">→</div>

      <article class="stock-v72-card stock-v72-stock">
        <div class="stock-v72-label">ストック型｜将来の経営資産</div>
        <h3>SNS・Google・<br>自前の情報インフラ</h3>
        <ul>
          <li>情報が残り続ける</li>
          <li>見つかる入口が増えていく</li>
          <li>時間とともに信頼が積み上がる</li>
        </ul>
        <strong>永続的に働く、無料の広告塔へ</strong>
      </article>
    </div>

    <div class="stock-v72-core">
      <span>OWNED MEDIA INFRASTRUCTURE</span>
      <h3>自前の情報発信インフラを育てる。</h3>
      <p>積み上がった発信は、やがてあなたの代わりに働き続ける広告塔になる。</p>
    </div>

    <div class="stock-v72-local">
      <p>AIには作れない価値が、小金井にはある。</p>
      <strong>土地・歴史・時間・思い出・地域とのつながりを、<br>ネット上から消えない資産にする。</strong>
    </div>

    <div class="stock-v72-footer">小金井で長く強い集客を、一緒につくる。</div>
  </div>
</section>'''

css=r'''
<style id="stock-ai-simple-style">
.stock-v72{padding:92px 0!important;background:linear-gradient(145deg,#031735,#082c60)!important;color:#fff!important}
.stock-v72 .container{max-width:1120px!important}
.stock-v72-head{text-align:center!important}
.stock-v72-kicker{display:inline-flex!important;align-items:center!important;gap:12px!important;color:#f0d995!important;font-size:.76rem!important;font-weight:900!important;letter-spacing:.16em!important}
.stock-v72-kicker:before,.stock-v72-kicker:after{content:""!important;width:34px!important;height:2px!important;background:#f0d995!important}
.stock-v72-head h2{margin:16px 0 0!important;color:#fff!important;font-size:clamp(2.8rem,5.8vw,5.4rem)!important;line-height:1.03!important;letter-spacing:-.055em!important}
.stock-v72-head h2 em{font-style:normal!important;color:#f0c45a!important}
.stock-v72-head p{margin:14px 0 0!important;color:rgba(255,255,255,.78)!important;font-size:1.08rem!important;font-weight:800!important}

.stock-v72-compare{display:grid!important;grid-template-columns:1fr 70px 1fr!important;gap:18px!important;align-items:center!important;margin-top:34px!important}
.stock-v72-card{min-height:330px!important;padding:28px!important;border-radius:28px!important;display:flex!important;flex-direction:column!important}
.stock-v72-flow{background:rgba(255,255,255,.08)!important;border:1px solid rgba(255,255,255,.16)!important}
.stock-v72-stock{background:linear-gradient(145deg,#fffdf7,#fff4d9)!important;border:1px solid rgba(240,196,90,.55)!important;color:#071d3f!important}
.stock-v72-label{display:inline-flex!important;align-self:flex-start!important;padding:7px 11px!important;border-radius:999px!important;background:rgba(255,255,255,.10)!important;color:#f0d995!important;font-size:.72rem!important;font-weight:900!important}
.stock-v72-stock .stock-v72-label{background:#c99426!important;color:#fff!important}
.stock-v72-card h3{margin:18px 0 0!important;font-size:clamp(1.45rem,2.5vw,2.15rem)!important;line-height:1.25!important;color:inherit!important}
.stock-v72-card ul{margin:22px 0 0!important;padding:0!important;list-style:none!important;display:grid!important;gap:12px!important}
.stock-v72-card li{position:relative!important;padding-left:25px!important;font-size:.98rem!important;line-height:1.55!important;color:inherit!important}
.stock-v72-card li:before{position:absolute!important;left:0!important;top:0!important;font-weight:900!important}
.stock-v72-flow li:before{content:"×"!important;color:#c9d3df!important}
.stock-v72-stock li:before{content:"✓"!important;color:#b77e10!important}
.stock-v72-card>strong{margin-top:auto!important;padding-top:22px!important;font-size:1.18rem!important}
.stock-v72-flow>strong{color:#dfe7f1!important}
.stock-v72-stock>strong{color:#a56f0a!important}
.stock-v72-arrow{text-align:center!important;font-size:3.2rem!important;font-weight:900!important;color:#f0d995!important}

.stock-v72-core{margin-top:24px!important;padding:30px 28px!important;border-radius:28px!important;background:rgba(255,255,255,.09)!important;border:1px solid rgba(255,255,255,.16)!important;text-align:center!important}
.stock-v72-core span{display:block!important;color:#f0d995!important;font-size:.7rem!important;font-weight:900!important;letter-spacing:.14em!important}
.stock-v72-core h3{margin:8px 0 0!important;color:#fff!important;font-size:clamp(1.9rem,3.5vw,3.3rem)!important;line-height:1.15!important}
.stock-v72-core p{margin:10px 0 0!important;color:rgba(255,255,255,.78)!important;font-size:1rem!important;font-weight:700!important}

.stock-v72-local{margin-top:20px!important;padding:30px 26px!important;border-radius:28px!important;background:#fff!important;color:#071d3f!important;text-align:center!important;box-shadow:0 22px 48px rgba(0,0,0,.18)!important}
.stock-v72-local p{margin:0!important;color:#a36c1b!important;font-size:1.15rem!important;font-weight:900!important}
.stock-v72-local strong{display:block!important;margin-top:8px!important;color:#071d3f!important;font-size:clamp(1.55rem,3vw,2.8rem)!important;line-height:1.25!important}
.stock-v72-footer{margin-top:18px!important;text-align:center!important;color:#f0d995!important;font-size:1.08rem!important;font-weight:900!important}

@media(max-width:820px){
  .stock-v72{padding:68px 0!important}
  .stock-v72-compare{grid-template-columns:1fr!important}
  .stock-v72-arrow{transform:rotate(90deg)!important;line-height:1!important}
  .stock-v72-card{min-height:auto!important}
}
@media(max-width:560px){
  .stock-v72-head h2{font-size:clamp(2.2rem,11vw,3.4rem)!important}
  .stock-v72-card,.stock-v72-core,.stock-v72-local{padding:22px 18px!important}
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
  '消える広告より、<br><em>残る広告塔。</em>',
  'チラシ・グルメサイト・<br>インフルエンサー広告',
  'SNS・Google・<br>自前の情報インフラ',
  '永続的に働く、無料の広告塔へ',
  '自前の情報発信インフラを育てる。',
  'AIには作れない価値が、小金井にはある。',
  'ネット上から消えない資産にする。',
  'id="stock-ai-simple-style"'
]
for token in required:
    if token not in s:
        raise SystemExit(f"Missing stock-ai token: {token}")
