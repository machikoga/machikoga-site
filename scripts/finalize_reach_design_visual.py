from pathlib import Path
import re

p = Path("public/index.html")
s = p.read_text(encoding="utf-8")

section = r'''<section class="section reach-design reach-v70" id="reach-design">
  <div class="container">
    <div class="reach-v70-head">
      <span class="reach-v70-kicker">REACH DESIGN</span>
      <h2>いい投稿を作るだけでは、<br>まだ足りない。</h2>
      <p class="reach-v70-sub">必要なのは <strong>「誰に届けるか」</strong> を先に設計すること。</p>
      <p class="reach-v70-note">かっこよく投稿して満足しても、届く先が変わらなければ意味がない。</p>
      <div class="reach-v70-alert">
        <b>これをしないと意味がない。</b>
        <span>ぶるは、投稿そのものより「届け方」を変えるお手伝いをします。</span>
      </div>
    </div>

    <div class="reach-v70-compare">
      <article class="reach-v70-panel reach-v70-bad">
        <div class="reach-v70-panel-title">投稿だけを工夫する</div>
        <div class="reach-v70-panel-body">
          <div class="reach-v70-phone" aria-hidden="true">
            <div class="reach-v70-phone-screen">
              <span class="reach-v70-sun"></span>
              <span class="reach-v70-mountain"></span>
              <span class="reach-v70-line l1"></span>
              <span class="reach-v70-line l2"></span>
            </div>
            <div class="reach-v70-people"><i></i><i></i><i></i></div>
          </div>
          <div class="reach-v70-list bad">
            <div><span>×</span><b>見た目で満足する</b></div>
            <div><span>×</span><b>届く先はいつも同じ</b></div>
            <div><span>×</span><b>良い投稿が埋もれる</b></div>
          </div>
        </div>
      </article>

      <div class="reach-v70-arrow" aria-hidden="true">›</div>

      <article class="reach-v70-panel reach-v70-good">
        <div class="reach-v70-panel-title">ぶるが届け方を設計する</div>
        <div class="reach-v70-panel-body">
          <div class="reach-v70-network" aria-hidden="true">
            <div class="reach-v70-center">▶</div>
            <span class="n1">Instagram</span>
            <span class="n2">Google</span>
            <span class="n3">検索</span>
            <span class="n4">口コミ</span>
            <span class="n5">地域</span>
          </div>
          <div class="reach-v70-list good">
            <div><span>✓</span><b>新しい人に見つけてもらえる</b></div>
            <div><span>✓</span><b>Google・検索・口コミから届く</b></div>
            <div><span>✓</span><b>同じ投稿でも反応が変わる</b></div>
          </div>
        </div>
      </article>
    </div>

    <div class="reach-v70-bottom">
      <div class="reach-v70-steps">
        <article>
          <small>01</small>
          <div class="reach-v70-icon reach-v70-target">◎</div>
          <b>誰に届けるか決める</b>
        </article>
        <div class="reach-v70-step-arrow" aria-hidden="true">›</div>
        <article>
          <small>02</small>
          <div class="reach-v70-chips"><span>Instagram</span><span>Google</span><span>検索</span></div>
          <b>見つかる入口を増やす</b>
        </article>
        <div class="reach-v70-step-arrow" aria-hidden="true">›</div>
        <article>
          <small>03</small>
          <div class="reach-v70-icon">↻</div>
          <b>同じ発信を何度も届ける</b>
        </article>
      </div>

      <aside class="reach-v70-result">
        <span>ぶるが少し手伝うだけで</span>
        <strong>届き方は<em>数倍</em>に。</strong>
        <p>投稿の質だけでなく、届け方で差がつきます。</p>
      </aside>
    </div>

    <p class="reach-v70-closing">みんな投稿を工夫している時代。だからこそ、届け方の設計で差がつく。</p>
    <div class="reach-v70-cta">バズらせない。届けたい人に、深く届ける。 <span>→</span></div>
  </div>
</section>'''

css = r'''
<style id="reach-v70-style">
/* V70 REACH DESIGN VISUAL — final deploy-safe styles */
.reach-v70{background:#fff!important;padding:86px 0!important}
.reach-v70 .container{max-width:1180px!important}
.reach-v70-head{text-align:center!important;max-width:1100px!important;margin:0 auto 30px!important}
.reach-v70-kicker{display:inline-flex!important;align-items:center!important;gap:12px!important;color:#0b2b55!important;font-size:.76rem!important;font-weight:900!important;letter-spacing:.18em!important}
.reach-v70-kicker:before,.reach-v70-kicker:after{content:""!important;width:34px!important;height:2px!important;background:#c99426!important}
.reach-v70-head h2{margin:14px 0 0!important;color:#0b2348!important;font-size:clamp(2.45rem,5.2vw,5.1rem)!important;line-height:1.03!important;letter-spacing:-.055em!important}
.reach-v70-sub{margin:15px 0 0!important;color:#0b2348!important;font-size:clamp(1.2rem,2.1vw,2rem)!important;font-weight:800!important;line-height:1.5!important}
.reach-v70-sub strong{color:#c68d1d!important}
.reach-v70-note{margin:8px 0 0!important;color:#334863!important;font-size:1rem!important}
.reach-v70-alert{margin:18px auto 0!important;display:flex!important;align-items:center!important;justify-content:center!important;gap:20px!important;flex-wrap:wrap!important}
.reach-v70-alert b{padding:10px 18px!important;border-radius:14px!important;background:#fff5df!important;color:#b57908!important;font-size:1.25rem!important;box-shadow:inset 0 0 0 1px #f3dfb2!important}
.reach-v70-alert span{color:#243954!important;font-weight:800!important}

.reach-v70-compare{display:grid!important;grid-template-columns:minmax(0,1fr) 42px minmax(0,1fr)!important;align-items:center!important;gap:12px!important;margin-top:10px!important}
.reach-v70-panel{border-radius:28px!important;padding:18px!important;background:#f5f7fa!important;border:1px solid #e3e9f0!important;box-shadow:0 18px 40px rgba(5,25,57,.08)!important;overflow:hidden!important}
.reach-v70-good{background:#fff8e8!important;border-color:#f1dfb3!important}
.reach-v70-panel-title{padding:12px 16px!important;border-radius:999px!important;background:#e6ebf1!important;color:#0b2348!important;text-align:center!important;font-size:1.35rem!important;font-weight:900!important}
.reach-v70-good .reach-v70-panel-title{background:linear-gradient(90deg,#efc45d,#efd180)!important}
.reach-v70-panel-body{display:grid!important;grid-template-columns:.82fr 1.18fr!important;gap:16px!important;align-items:center!important;padding:22px 6px 6px!important}

.reach-v70-phone{position:relative!important;min-height:185px!important;display:grid!important;place-items:center!important}
.reach-v70-phone-screen{position:relative!important;width:98px!important;height:150px!important;border:3px solid #0b2b55!important;border-radius:16px!important;background:#fff!important;box-shadow:0 8px 20px rgba(6,26,56,.08)!important;z-index:2!important}
.reach-v70-sun{position:absolute!important;right:16px!important;top:36px!important;width:18px!important;height:18px!important;border-radius:50%!important;background:#d8a128!important}
.reach-v70-mountain{position:absolute!important;left:18px!important;top:62px!important;width:56px!important;height:40px!important;background:linear-gradient(145deg,#cdd8e5 50%,#aebfd1 50%)!important;clip-path:polygon(0 100%,38% 30%,55% 58%,72% 42%,100% 100%)!important}
.reach-v70-line{position:absolute!important;left:18px!important;height:5px!important;border-radius:999px!important;background:#d9e1ea!important}.reach-v70-line.l1{width:58px!important;bottom:28px!important}.reach-v70-line.l2{width:42px!important;bottom:17px!important}
.reach-v70-people{position:absolute!important;bottom:9px!important;left:0!important;right:0!important;display:flex!important;justify-content:space-between!important;z-index:1!important}
.reach-v70-people i{display:block!important;width:48px!important;height:58px!important;border-radius:50% 50% 18px 18px!important;background:#d7dfe8!important}
.reach-v70-list{display:grid!important;gap:16px!important}
.reach-v70-list div{display:flex!important;align-items:center!important;gap:11px!important}
.reach-v70-list span{width:38px!important;height:38px!important;border-radius:50%!important;display:grid!important;place-items:center!important;font-size:1.35rem!important;font-weight:900!important;flex:0 0 auto!important}
.reach-v70-list.bad span{background:#e3e8ef!important;color:#0b2348!important}
.reach-v70-list.good span{background:#c99426!important;color:#fff!important}
.reach-v70-list b{color:#0b2348!important;font-size:1rem!important;line-height:1.4!important}
.reach-v70-arrow,.reach-v70-step-arrow{font-size:3rem!important;color:#0b2348!important;text-align:center!important;font-weight:500!important}

.reach-v70-network{position:relative!important;height:190px!important;display:grid!important;place-items:center!important}
.reach-v70-center{width:96px!important;height:70px!important;border-radius:12px!important;background:#0b2b55!important;color:#fff!important;display:grid!important;place-items:center!important;font-size:1.9rem!important;box-shadow:0 8px 18px rgba(6,26,56,.18)!important}
.reach-v70-network span{position:absolute!important;padding:7px 10px!important;border-radius:999px!important;background:#fff!important;border:1px solid #e5d8b8!important;font-size:.68rem!important;font-weight:900!important;color:#0b2348!important;box-shadow:0 5px 13px rgba(6,26,56,.07)!important}
.reach-v70-network .n1{top:4px!important;left:50%!important;transform:translateX(-50%)!important}.reach-v70-network .n2{top:38px!important;right:4px!important}.reach-v70-network .n3{bottom:22px!important;right:8px!important}.reach-v70-network .n4{top:42px!important;left:2px!important}.reach-v70-network .n5{bottom:24px!important;left:12px!important}

.reach-v70-bottom{display:grid!important;grid-template-columns:1.7fr .85fr!important;gap:18px!important;margin-top:18px!important}
.reach-v70-steps{display:grid!important;grid-template-columns:1fr 28px 1fr 28px 1fr!important;align-items:stretch!important}
.reach-v70-steps article{min-height:170px!important;padding:18px!important;border-radius:22px!important;background:#fff!important;border:1px solid #e4e9ef!important;box-shadow:0 12px 28px rgba(5,25,57,.07)!important;display:flex!important;flex-direction:column!important;justify-content:space-between!important}
.reach-v70-steps small{color:#bf8617!important;font-size:1.2rem!important;font-weight:900!important}
.reach-v70-icon{font-size:3.4rem!important;color:#0b2b55!important;line-height:1!important}
.reach-v70-chips{display:flex!important;gap:5px!important;flex-wrap:wrap!important}.reach-v70-chips span{padding:7px 9px!important;border-radius:999px!important;background:#f3f6f9!important;color:#0b2b55!important;font-size:.66rem!important;font-weight:900!important}
.reach-v70-steps b{font-size:.9rem!important;color:#0b2348!important;line-height:1.45!important}
.reach-v70-result{border-radius:24px!important;padding:24px!important;background:linear-gradient(145deg,#071d3f,#0b3567)!important;color:#fff!important;display:flex!important;flex-direction:column!important;justify-content:center!important;box-shadow:0 18px 42px rgba(5,25,57,.18)!important}
.reach-v70-result>span{font-size:1rem!important;font-weight:900!important}
.reach-v70-result strong{margin-top:4px!important;font-size:clamp(2rem,3.5vw,3.5rem)!important;line-height:1.05!important;letter-spacing:-.04em!important;color:#fff!important}
.reach-v70-result em{font-style:normal!important;color:#f0c45a!important;font-size:1.18em!important}
.reach-v70-result p{margin:14px 0 0!important;padding-top:12px!important;border-top:1px solid rgba(255,255,255,.28)!important;color:rgba(255,255,255,.84)!important;font-size:.9rem!important}
.reach-v70-closing{text-align:center!important;margin:20px 0 0!important;color:#0b2348!important;font-size:1.03rem!important;font-weight:900!important}
.reach-v70-cta{width:min(620px,100%)!important;margin:12px auto 0!important;padding:13px 22px!important;border-radius:999px!important;background:linear-gradient(90deg,#bc8213,#d7a72e)!important;color:#fff!important;text-align:center!important;font-weight:900!important;box-shadow:0 10px 24px rgba(188,130,19,.22)!important}
.reach-v70-cta span{margin-left:14px!important}

@media(max-width:900px){
  .reach-v70{padding:66px 0!important}
  .reach-v70-compare{grid-template-columns:1fr!important}
  .reach-v70-arrow{transform:rotate(90deg)!important;line-height:1!important}
  .reach-v70-bottom{grid-template-columns:1fr!important}
  .reach-v70-steps{grid-template-columns:1fr!important;gap:0!important}
  .reach-v70-step-arrow{transform:rotate(90deg)!important;height:30px!important;line-height:30px!important}
  .reach-v70-panel-body{grid-template-columns:1fr!important}
  .reach-v70-network{height:170px!important}
}
@media(max-width:560px){
  .reach-v70-head h2{font-size:clamp(2rem,10vw,3rem)!important}
  .reach-v70-panel{padding:14px!important}
  .reach-v70-panel-title{font-size:1.08rem!important}
  .reach-v70-alert{align-items:stretch!important}
  .reach-v70-alert b,.reach-v70-alert span{width:100%!important;text-align:center!important}
  .reach-v70-list b{font-size:.9rem!important}
  .reach-v70-result{padding:20px!important}
  .reach-v70-closing{font-size:.9rem!important}
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
    'これをしないと意味がない。',
    'ぶるが届け方を設計する',
    '届き方は<em>数倍</em>に。',
    'id="reach-v70-style"'
]
for token in required:
    if token not in s:
        raise SystemExit(f"Missing final reach token: {token}")
