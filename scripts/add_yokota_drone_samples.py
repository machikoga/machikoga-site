from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

# Remove prior injected block if present so the script is idempotent.
s = re.sub(r'\s*<div class="yokota-drone-feature">.*?</div>\s*(?=<div class="sample-grid">)', '\n', s, count=1, flags=re.S)

feature = r'''
<div class="yokota-drone-feature">
  <div class="yokota-drone-head">
    <span>YOKOTA DRONE WORKS</span>
    <h3>ドローン日本の第一人者<br>横田淳氏 撮影サンプル</h3>
    <p>空間を縫うマイクロドローンから、地域プロモーション映像まで。実際の撮影サンプルをご覧ください。</p>
  </div>
  <div class="yokota-drone-grid">
    <article class="video-card yokota-video-card">
      <div class="yokota-video-badge">横田淳氏 撮影</div>
      <video controls playsinline preload="none" poster="posters/yokota-indoor-drone-sample.jpg">
        <source src="videos/yokota-indoor-drone-sample.mp4" type="video/mp4">
      </video>
      <div class="video-body">
        <h3>マイクロドローン｜空間撮影</h3>
        <p>屋内を立体的に抜ける、臨場感のあるドローン映像。</p>
      </div>
    </article>
    <article class="video-card yokota-video-card">
      <div class="yokota-video-badge">横田淳氏 撮影</div>
      <video controls playsinline preload="none" poster="posters/yokota-higashimurayama-drone-sample.jpg">
        <source src="videos/yokota-higashimurayama-drone-sample.mp4" type="video/mp4">
      </video>
      <div class="video-body">
        <h3>東村山｜企業版ふるさと納税 映像企画</h3>
        <p>地域の魅力を空から伝えるプロモーション映像。</p>
      </div>
    </article>
  </div>
</div>
'''

needle = '<div class="sample-grid">'
if needle not in s:
    raise SystemExit('sample-grid not found')
s = s.replace(needle, feature + '\n' + needle, 1)

css = r'''
/* V68 YOKOTA DRONE FEATURE */
.yokota-drone-feature{
  margin-top:28px;
  padding:24px;
  border-radius:26px;
  background:linear-gradient(145deg,#061a38 0%,#0b3855 100%);
  border:1px solid rgba(199,162,83,.34);
  box-shadow:0 20px 46px rgba(5,25,57,.12);
}
.yokota-drone-head{
  display:grid;
  grid-template-columns:minmax(0,.72fr) minmax(0,1.28fr);
  gap:8px 24px;
  align-items:end;
  margin-bottom:18px;
}
.yokota-drone-head>span{
  grid-column:1/-1;
  color:#f0d995;
  font-size:.66rem;
  font-weight:950;
  letter-spacing:.14em;
}
.yokota-drone-head h3{
  margin:0;
  color:#fff;
  font-size:clamp(1.55rem,2.5vw,2.3rem);
  line-height:1.16;
  letter-spacing:-.035em;
}
.yokota-drone-head p{
  margin:0;
  color:rgba(255,255,255,.72);
  font-size:.84rem;
  line-height:1.75;
}
.yokota-drone-grid{
  display:grid;
  grid-template-columns:repeat(2,minmax(0,1fr));
  gap:14px;
}
.yokota-video-card{
  position:relative;
  overflow:hidden;
  background:#fff;
  border:0!important;
}
.yokota-video-card video{
  display:block;
  width:100%;
  aspect-ratio:16/9;
  object-fit:cover;
  background:#061a38;
}
.yokota-video-badge{
  position:absolute;
  top:12px;
  left:12px;
  z-index:2;
  padding:7px 10px;
  border-radius:999px;
  background:rgba(6,26,56,.90);
  border:1px solid rgba(240,217,149,.55);
  color:#f0d995;
  font-size:.62rem;
  font-weight:950;
  letter-spacing:.05em;
  backdrop-filter:blur(8px);
}
.yokota-video-card .video-body h3{
  font-size:1rem!important;
}
.yokota-video-card .video-body p{
  font-size:.76rem!important;
  line-height:1.6!important;
}
@media(max-width:780px){
  .yokota-drone-feature{
    padding:18px 14px;
    border-radius:20px;
  }
  .yokota-drone-head{
    grid-template-columns:1fr;
    gap:8px;
  }
  .yokota-drone-head>span{
    grid-column:auto;
  }
  .yokota-drone-head h3{
    font-size:1.55rem;
  }
  .yokota-drone-grid{
    grid-template-columns:1fr;
    gap:12px;
  }
}
'''

s = re.sub(r'/\* V68 YOKOTA DRONE FEATURE \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

for token in [
    '横田淳氏 撮影サンプル',
    'videos/yokota-indoor-drone-sample.mp4',
    'videos/yokota-higashimurayama-drone-sample.mp4',
    'V68 YOKOTA DRONE FEATURE',
]:
    if token not in s:
        raise SystemExit(f'Missing Yokota sample token: {token}')
