from pathlib import Path
import re

p = Path("public/index.html")
s = p.read_text(encoding="utf-8")

section = r'''<section class="section reach-design reach-v71" id="reach-design">
  <div class="container">
    <div class="reach-v71-head">
      <span class="reach-v71-kicker">REACH DESIGN</span>
      <h2>投稿をかっこよくしても、<br><em>小金井で強くなれるとは限らない。</em></h2>
    </div>

    <div class="reach-v71-choice">
      <article class="reach-v71-card reach-v71-ng">
        <span class="reach-v71-mark">×</span>
        <div>
          <small>STEP 01</small>
          <h3>投稿をかっこよくする</h3>
          <p class="reach-v71-card-note">でも、届く先が同じなら小金井での強さは変わらない。</p>
        </div>
      </article>

      <div class="reach-v71-arrow">→</div>

      <article class="reach-v71-card reach-v71-ok">
        <span class="reach-v71-mark">○</span>
        <div>
          <small>STEP 02</small>
          <h3>設計を見直して、<br>いつもの投稿をする</h3>
          <p class="reach-v71-card-note">投稿回数を増やさず、届け方だけを変える。</p>
        </div>
      </article>
    </div>

    <div class="reach-v71-result">
      <p>届けたい人に、ちゃんと届けられる。</p>
      <strong><span>いつもの投稿が、</span><em>数倍パワーアップ。</em></strong>
    </div>
  </div>
</section>'''

css = r'''
<style id="reach-v70-style">
/* V71 SIMPLE REACH DESIGN */
.reach-v71{background:#fff!important;padding:82px 0!important}
.reach-v71 .container{max-width:1120px!important}
.reach-v71-head{text-align:left!important;margin-bottom:30px!important}
.reach-v71-kicker{display:inline-flex!important;align-items:center!important;gap:12px!important;color:#0b2b55!important;font-size:.76rem!important;font-weight:900!important;letter-spacing:.18em!important}
.reach-v71-kicker:before,.reach-v71-kicker:after{content:""!important;width:34px!important;height:2px!important;background:#c99426!important}
.reach-v71-head h2{margin:14px 0 0!important;color:#0b2348!important;font-size:clamp(2.4rem,5vw,4.8rem)!important;line-height:1.05!important;letter-spacing:-.05em!important}
.reach-v71-head h2 em{font-style:normal!important;color:#c68d1d!important}
.reach-v71-choice{display:grid!important;grid-template-columns:1fr 70px 1fr!important;gap:18px!important;align-items:center!important;margin-top:28px!important}
.reach-v71-card{display:flex!important;align-items:center!important;gap:20px!important;min-height:170px!important;padding:28px!important;border-radius:28px!important;border:1px solid #e1e7ee!important;box-shadow:0 18px 42px rgba(5,25,57,.08)!important}
.reach-v71-ng{background:#f5f7fa!important}
.reach-v71-ok{background:linear-gradient(135deg,#fff8e8,#fffdf7)!important;border-color:#eed79d!important;box-shadow:0 20px 46px rgba(188,130,19,.12)!important}
.reach-v71-mark{width:64px!important;height:64px!important;border-radius:50%!important;display:grid!important;place-items:center!important;flex:0 0 auto!important;font-size:2.2rem!important;font-weight:900!important}
.reach-v71-ng .reach-v71-mark{background:#dfe5ec!important;color:#6b7b8e!important}
.reach-v71-ok .reach-v71-mark{background:#c99426!important;color:#fff!important}
.reach-v71-card small{display:block!important;font-size:.68rem!important;font-weight:900!important;letter-spacing:.13em!important;color:#7b8798!important}
.reach-v71-card h3{margin:8px 0 0!important;color:#0b2348!important;font-size:clamp(1.45rem,2.5vw,2.15rem)!important;line-height:1.25!important;letter-spacing:-.025em!important}.reach-v71-card-note{margin:9px 0 0!important;color:#66758a!important;font-size:.88rem!important;line-height:1.55!important;font-weight:700!important}
.reach-v71-arrow{text-align:center!important;color:#0b2348!important;font-size:3.2rem!important;font-weight:900!important}
.reach-v71-result{margin-top:24px!important;padding:34px 28px!important;border-radius:28px!important;background:linear-gradient(145deg,#071d3f,#0b3567)!important;color:#fff!important;text-align:center!important;box-shadow:0 24px 54px rgba(5,25,57,.18)!important}
.reach-v71-result p{margin:0!important;color:rgba(255,255,255,.88)!important;font-size:clamp(1.1rem,2vw,1.5rem)!important;font-weight:800!important}
.reach-v71-result strong{display:flex!important;justify-content:center!important;align-items:baseline!important;gap:.22em!important;margin-top:6px!important;color:#fff!important;font-size:clamp(2rem,4.2vw,4rem)!important;line-height:1.08!important;letter-spacing:-.04em!important;white-space:nowrap!important}.reach-v71-result strong span,.reach-v71-result strong em{display:inline-block!important}
.reach-v71-result em{font-style:normal!important;color:#f0c45a!important}
@media(max-width:820px){
  .reach-v71-choice{grid-template-columns:1fr!important}
  .reach-v71-arrow{transform:rotate(90deg)!important;line-height:1!important}
}
@media(max-width:820px){.reach-v71-result strong{white-space:normal!important}}
@media(max-width:560px){
  .reach-v71{padding:64px 0!important}
  .reach-v71-head h2{font-size:clamp(2rem,10vw,3rem)!important}
  .reach-v71-card{min-height:auto!important;padding:22px 18px!important}
  .reach-v71-mark{width:54px!important;height:54px!important;font-size:1.8rem!important}
  .reach-v71-result{padding:26px 18px!important;overflow:hidden!important}
  .reach-v71-result p{font-size:1rem!important;line-height:1.45!important}
  .reach-v71-result strong{display:block!important;font-size:clamp(1.75rem,8.5vw,2.45rem)!important;line-height:1.08!important;white-space:normal!important}
  .reach-v71-result strong span,.reach-v71-result strong em{display:block!important;width:100%!important}
  .reach-v71-result strong em{margin-top:4px!important}
}
</style>'''

# Replace current reach section, regardless of version
pattern = r'<section class="section reach-design[^"]*" id="reach-design">.*?</section>'
if re.search(pattern, s, flags=re.S):
    s = re.sub(pattern, section, s, count=1, flags=re.S)
else:
    marker = '<section class="section dual-platform-section" id="dual-platform">'
    if marker not in s:
        raise SystemExit("Could not locate REACH DESIGN insertion point")
    s = s.replace(marker, section + "\n" + marker, 1)

# Remove any prior final style block and append the deploy-safe CSS immediately before </head>
s = re.sub(r'<style id="reach-v70-style">.*?</style>', '', s, flags=re.S)
if '</head>' not in s:
    raise SystemExit("Missing </head>")
s = s.replace('</head>', css + '\n</head>', 1)

p.write_text(s, encoding="utf-8")

required = [
    '投稿をかっこよくする',
    '小金井で強くなれるとは限らない。',
    '設計を見直して、<br>いつもの投稿をする',
    '<span>いつもの投稿が、</span><em>数倍パワーアップ。</em>',
    'id="reach-v70-style"'
]
for token in required:
    if token not in s:
        raise SystemExit(f"Missing final reach token: {token}")
