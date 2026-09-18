from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

# 1) AI: make all five values equal and show them as one visual flow.
ai_values = r'''<div class="ai-values-bridge"><span>この5つが</span><strong>「地域で積み上げた5つの価値」</strong><b>01 → 02 → 03 → 04 → 05</b></div>
<div class="ai-values ai-value-diagram">
  <article class="ai-value"><span class="ai-value-no">01</span><h3>土地</h3><p>その場所で商売してきた事実</p></article>
  <div class="ai-value-arrow" aria-hidden="true">→</div>
  <article class="ai-value"><span class="ai-value-no">02</span><h3>歴史</h3><p>店・会社が歩んできた背景</p></article>
  <div class="ai-value-arrow" aria-hidden="true">→</div>
  <article class="ai-value"><span class="ai-value-no">03</span><h3>時間・プロセス</h3><p>地域に積み重ねた信頼</p></article>
  <div class="ai-value-arrow" aria-hidden="true">→</div>
  <article class="ai-value"><span class="ai-value-no">04</span><h3>思い出</h3><p>お客様との体験・記憶</p></article>
  <div class="ai-value-arrow" aria-hidden="true">→</div>
  <article class="ai-value"><span class="ai-value-no">05</span><h3>地域との<br>つながり</h3><p>小金井で育てた、本物の事業資産</p></article>
</div>'''

s = re.sub(r'<div class="ai-values[^"]*">.*?</div>\s*(?=<div class="ai-final-message">)', ai_values + '\n', s, count=1, flags=re.S)

# 2) ALL-IN-ONE section: use the user's strongest approved message.
compare_html = r'''<section class="section compare compare-compact compare-allinone" id="compare"><div class="container">
  <span class="kicker">ALL-IN-ONE SUPPORT</span>
  <h2>あちこちに頼まなくていい。<br>まちこがなら、オールインワン。</h2>
  <p class="lead compare-lead">本来は、SNS・Google・WEB・撮影をそれぞれ別の業者に頼む必要があります。<br>そのたびに費用も、手間も、確認事項も増えていきます。<br><strong>まちこがなら、小金井で必要な発信導線を、ひとつの窓口でまとめて整えます。</strong></p>

  <div class="compare-compact-row compare-allinone-row">
    <div class="compare-mini compare-mini-market">
      <span>一般的な別発注</span>
      <strong>SNS / Google / WEB / 撮影を<br>それぞれ別で依頼</strong>
      <small>費用が分かれる / やり取りが増える / 方針がズレやすい</small>
    </div>

    <div class="compare-arrow">→</div>

    <div class="compare-mini compare-mini-machikoga">
      <span>まちこが</span>
      <strong>小金井の発信を、<br>ひとつにまとめる。</strong>
      <small>設計・制作・運用まで、オールインワン。</small>
    </div>
  </div>
</div></section>'''

if not re.search(r'<section class="section compare[^"]*" id="compare">.*?</section>', s, flags=re.S):
    raise SystemExit('Compare section not found')
s = re.sub(r'<section class="section compare[^"]*" id="compare">.*?</section>', compare_html, s, count=1, flags=re.S)

css = r'''
/* V68 USER REQUESTED FINAL REFINEMENT */

/* AI five values: equal importance, one continuous visual story */
.ai-final .ai-cannot{
  position:relative!important;
  background:linear-gradient(145deg,#2b5f86 0%,#1e6e78 100%)!important;
  border:1px solid rgba(240,217,149,.30)!important;
  color:#fff!important;
  box-shadow:0 16px 34px rgba(0,0,0,.12)!important;
}
.ai-final .ai-cannot .ai-contrast-label{
  color:#f0d995!important;
}
.ai-final .ai-cannot strong,
.ai-final .ai-cannot small{
  color:#fff!important;
}
.ai-final .ai-cannot small{
  opacity:.72!important;
}
.ai-final .ai-cannot:after{
  content:"";
  position:absolute;
  left:50%;
  bottom:-34px;
  width:2px;
  height:34px;
  transform:translateX(-50%);
  background:linear-gradient(#f0d995,rgba(240,217,149,.25));
}
.ai-final .ai-values-bridge{
  position:relative;
  z-index:2;
  width:max-content;
  max-width:calc(100% - 32px);
  margin:32px auto -6px;
  padding:10px 16px;
  border-radius:999px;
  display:flex;
  align-items:center;
  justify-content:center;
  gap:9px;
  flex-wrap:wrap;
  background:linear-gradient(145deg,#2b5f86 0%,#1e6e78 100%);
  border:1px solid rgba(240,217,149,.30);
  box-shadow:0 10px 24px rgba(0,0,0,.10);
  color:#fff;
}
.ai-final .ai-values-bridge span{
  color:#f0d995;
  font-size:.66rem;
  font-weight:950;
  letter-spacing:.08em;
}
.ai-final .ai-values-bridge strong{
  color:#fff;
  font-size:.88rem;
  line-height:1.35;
}
.ai-final .ai-values-bridge b{
  color:#f0d995;
  font-size:.72rem;
  letter-spacing:.05em;
}
.ai-final .ai-value-diagram{
  display:grid!important;
  grid-template-columns:minmax(0,1fr) 26px minmax(0,1fr) 26px minmax(0,1fr) 26px minmax(0,1fr) 26px minmax(0,1fr)!important;
  gap:10px!important;
  align-items:stretch!important;
  margin-top:26px!important;
}
.ai-final .ai-value-diagram .ai-value{
  min-width:0!important;
  min-height:172px!important;
  padding:22px 18px 20px!important;
  border-radius:22px!important;
  background:linear-gradient(145deg,#2b5f86 0%,#1e6e78 100%)!important;
  border:1px solid rgba(240,217,149,.24)!important;
  color:#fff!important;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.06),0 14px 30px rgba(0,0,0,.08)!important;
  transform:none!important;
}
.ai-final .ai-value-diagram .ai-value:nth-of-type(5){
  background:linear-gradient(145deg,#2b5f86 0%,#1e6e78 100%)!important;
  border:1px solid rgba(240,217,149,.24)!important;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.06),0 14px 30px rgba(0,0,0,.08)!important;
}
.ai-final .ai-value-diagram .ai-value-no{
  display:grid!important;
  place-items:center!important;
  width:42px!important;
  height:42px!important;
  margin:0 0 14px!important;
  border-radius:13px!important;
  background:#f0d995!important;
  border:0!important;
  color:#071d3f!important;
  font-size:.72rem!important;
  font-weight:950!important;
}
.ai-final .ai-value-diagram .ai-value h3{
  margin:0!important;
  color:#fff!important;
  font-size:clamp(1.05rem,1.38vw,1.38rem)!important;
  line-height:1.28!important;
  letter-spacing:-.02em!important;
  white-space:normal!important;
  word-break:keep-all!important;
  overflow-wrap:anywhere!important;
}
.ai-final .ai-value-diagram .ai-value:nth-of-type(5) h3{
  font-size:clamp(.98rem,1.2vw,1.2rem)!important;
  line-height:1.26!important;
}
.ai-final .ai-value-diagram .ai-value p{
  margin-top:9px!important;
  color:rgba(255,255,255,.72)!important;
  font-size:.75rem!important;
  line-height:1.65!important;
}
.ai-final .ai-value-arrow{
  display:flex!important;
  align-items:center!important;
  justify-content:center!important;
  color:#f0d995!important;
  font-size:1.4rem!important;
  font-weight:950!important;
}

/* Results: tighter, faster to scan */
.machikoga-results .results-featured{
  gap:10px!important;
  margin-top:22px!important;
}
.machikoga-results .results-featured .result-impact{
  min-height:0!important;
  padding:17px 16px 15px!important;
  border-radius:18px!important;
}
.machikoga-results .results-featured .result-impact:before{
  top:11px!important;
  right:11px!important;
  font-size:.52rem!important;
}
.machikoga-results .results-featured .result-type{
  padding:4px 8px!important;
  font-size:.61rem!important;
}
.machikoga-results .results-featured .result-impact small{
  margin-top:9px!important;
  font-size:.7rem!important;
}
.machikoga-results .results-featured .result-impact>strong{
  margin-top:6px!important;
  font-size:clamp(1.15rem,1.65vw,1.55rem)!important;
  line-height:1.22!important;
}
.machikoga-results .results-featured .result-impact p{
  margin-top:6px!important;
  font-size:.7rem!important;
}
.machikoga-results .results-highlight{
  gap:10px!important;
  margin-top:12px!important;
}
.machikoga-results .results-highlight .result-impact{
  min-height:0!important;
  padding:16px 15px 14px!important;
  border-radius:18px!important;
}
.machikoga-results .results-highlight .result-type{
  padding:4px 8px!important;
  font-size:.61rem!important;
}
.machikoga-results .results-highlight .result-impact small{
  margin-top:8px!important;
  font-size:.7rem!important;
}
.machikoga-results .results-highlight .result-impact>strong{
  margin-top:5px!important;
  font-size:clamp(1.15rem,1.7vw,1.5rem)!important;
  line-height:1.2!important;
}
.machikoga-results .results-highlight .result-impact p{
  margin-top:5px!important;
  font-size:.7rem!important;
}

/* All-in-one: clearly show cost/effort fragmentation vs one-stop support */
.compare-allinone{
  padding:58px 0!important;
  background:linear-gradient(180deg,#fff,#f5f7fa)!important;
}
.compare-allinone h2{
  max-width:12em!important;
  margin-top:10px!important;
  color:#071d3f!important;
  font-size:clamp(2.35rem,4.8vw,4.55rem)!important;
  line-height:1.05!important;
  letter-spacing:-.05em!important;
}
.compare-allinone .compare-lead{
  max-width:940px!important;
  margin-top:18px!important;
  color:#5f6d82!important;
  line-height:1.9!important;
}
.compare-allinone .compare-lead strong{
  color:#071d3f!important;
}
.compare-allinone-row{
  margin-top:24px!important;
  grid-template-columns:minmax(0,1fr) 52px minmax(0,1fr)!important;
  gap:14px!important;
}
.compare-allinone .compare-mini{
  padding:20px 22px!important;
  border-radius:22px!important;
}
.compare-allinone .compare-mini span{
  margin-bottom:8px!important;
  font-size:.64rem!important;
}
.compare-allinone .compare-mini strong{
  font-size:1.08rem!important;
  line-height:1.5!important;
}
.compare-allinone .compare-mini small{
  display:block!important;
  margin-top:8px!important;
  color:#7a879a!important;
  font-size:.72rem!important;
  line-height:1.6!important;
}
.compare-allinone .compare-mini-machikoga small{
  color:rgba(255,255,255,.72)!important;
}
.compare-allinone .compare-arrow{
  display:flex!important;
  align-items:center!important;
  justify-content:center!important;
  font-size:1.65rem!important;
}

@media(max-width:1050px){
  .ai-final .ai-cannot:after{
    height:24px;
    bottom:-24px;
  }
  .ai-final .ai-values-bridge{
    width:auto;
    margin:24px 12px -2px;
    border-radius:18px;
    padding:11px 13px;
  }
  .ai-final .ai-values-bridge b{
    width:100%;
    text-align:center;
  }
  .ai-final .ai-value-diagram{
    grid-template-columns:1fr!important;
    gap:8px!important;
  }
  .ai-final .ai-value-arrow{
    min-height:22px!important;
    transform:rotate(90deg)!important;
  }
  .ai-final .ai-value-diagram .ai-value{
    min-height:0!important;
  }
}
@media(max-width:780px){
  .compare-allinone{
    padding:48px 0!important;
  }
  .compare-allinone h2{
    font-size:clamp(2.05rem,9vw,2.8rem)!important;
    line-height:1.1!important;
  }
  .compare-allinone .compare-lead br{
    display:none!important;
  }
  .compare-allinone-row{
    grid-template-columns:1fr!important;
    gap:8px!important;
  }
  .compare-allinone .compare-arrow{
    transform:rotate(90deg)!important;
    min-height:24px!important;
  }
  .machikoga-results .results-featured,
  .machikoga-results .results-highlight{
    gap:8px!important;
  }
  .machikoga-results .results-featured .result-impact,
  .machikoga-results .results-highlight .result-impact{
    padding:15px 14px 13px!important;
    border-radius:16px!important;
  }
}
'''

s = re.sub(r'/\* V68 USER REQUESTED FINAL REFINEMENT \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

for token in [
    'ai-values-bridge',
    'ai-value-diagram',
    'ALL-IN-ONE SUPPORT',
    'あちこちに頼まなくていい。',
    '費用が分かれる / やり取りが増える / 方針がズレやすい',
    '設計・制作・運用まで、オールインワン。',
    'V68 USER REQUESTED FINAL REFINEMENT',
]:
    if token not in s:
        raise SystemExit(f'Missing refinement token: {token}')
