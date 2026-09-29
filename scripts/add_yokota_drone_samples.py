from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

# Remove any previously injected external drone sample block.
s = re.sub(r'\s*<div class="yokota-drone-feature">.*?</div>\s*(?=<div class="sample-grid">)', '\n', s, count=1, flags=re.S)
s = re.sub(r'\s*<div class="external-drone-samples">.*?</div>\s*(?=</div></section>)', '\n', s, count=1, flags=re.S)

feature = r'''
<div class="external-drone-samples">
  <div class="external-drone-head">
    <span>OTHER DRONE SAMPLES</span>
    <h3>営業でご紹介している撮影サンプル</h3>
    <p>以下2本は小金井以外で撮影したドローン映像です。小金井の撮影事例とは分けて、一覧の最後に掲載しています。</p>
  </div>
  <div class="external-drone-grid">
    <article class="video-card external-drone-card">
      <video controls playsinline preload="none" poster="posters/yokota-indoor-drone-sample.jpg">
        <source src="videos/yokota-indoor-drone-sample.mp4" type="video/mp4">
      </video>
      <div class="video-body">
        <h3>屋内マイクロドローン撮影</h3>
        <p>空間の中を滑らかに巡る、臨場感のある撮影サンプル。</p>
      </div>
    </article>
    <article class="video-card external-drone-card">
      <video controls playsinline preload="none" poster="posters/yokota-higashimurayama-drone-sample.jpg">
        <source src="videos/yokota-higashimurayama-drone-sample.mp4" type="video/mp4">
      </video>
      <div class="video-body">
        <h3>東村山｜企業版ふるさと納税 映像企画</h3>
        <p>地域の魅力を映像で伝える、ドローンを活用したプロモーションサンプル。</p>
      </div>
    </article>
  </div>
</div>
'''

# Append the two non-Koganei samples to the very bottom of the DRONE & VIDEO SAMPLES section.
m = re.search(r'(<section class="section samples" id="samples">.*?)(</div></section>)', s, flags=re.S)
if not m:
    raise SystemExit('samples section not found')
section = m.group(1)
section = re.sub(r'\s*<div class="external-drone-samples">.*$', '', section, flags=re.S)
replacement = section + feature + m.group(2)
s = s[:m.start()] + replacement + s[m.end():]

css = r'''
/* V68 EXTERNAL DRONE SAMPLES */
.external-drone-samples{
  margin-top:28px;
  padding:22px;
  border-radius:24px;
  background:linear-gradient(145deg,#061a38 0%,#0b3855 100%);
  border:1px solid rgba(199,162,83,.30);
  box-shadow:0 18px 40px rgba(5,25,57,.10);
}
.external-drone-head{
  display:grid;
  grid-template-columns:minmax(0,.78fr) minmax(0,1.22fr);
  gap:8px 24px;
  align-items:end;
  margin-bottom:16px;
}
.external-drone-head>span{
  grid-column:1/-1;
  color:#f0d995;
  font-size:.64rem;
  font-weight:950;
  letter-spacing:.14em;
}
.external-drone-head h3{
  margin:0;
  color:#fff;
  font-size:clamp(1.35rem,2.2vw,2rem);
  line-height:1.18;
  letter-spacing:-.03em;
}
.external-drone-head p{
  margin:0;
  color:rgba(255,255,255,.72);
  font-size:.8rem;
  line-height:1.7;
}
.external-drone-grid{
  display:grid;
  grid-template-columns:repeat(2,minmax(0,1fr));
  gap:14px;
}
.external-drone-card{
  position:relative;
  overflow:hidden;
  background:#fff;
  border:0!important;
}
.external-drone-card video{
  display:block;
  width:100%;
  aspect-ratio:16/9;
  object-fit:contain;
  background:#020b18;
}
.external-drone-card .video-body{
  padding:14px 16px 16px!important;
}
.external-drone-card .video-body h3{
  margin:0!important;
  color:#071d3f!important;
  font-size:1rem!important;
  line-height:1.35!important;
}
.external-drone-card .video-body p{
  margin-top:5px!important;
  color:#68758a!important;
  font-size:.75rem!important;
  line-height:1.55!important;
}
@media(max-width:780px){
  .external-drone-samples{
    padding:16px 13px;
    border-radius:19px;
  }
  .external-drone-head{
    grid-template-columns:1fr;
    gap:7px;
  }
  .external-drone-head>span{
    grid-column:auto;
  }
  .external-drone-head h3{
    font-size:1.35rem;
  }
  .external-drone-grid{
    grid-template-columns:1fr;
    gap:11px;
  }
}
'''

s = re.sub(r'/\* V68 YOKOTA DRONE FEATURE \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = re.sub(r'/\* V68 EXTERNAL DRONE SAMPLES \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = s.replace('</style>', css + '\n</style>', 1)

# Ensure no photographer attribution remains visible.
s = s.replace('横田淳氏 撮影', '').replace('横田氏 撮影', '')

p.write_text(s, encoding='utf-8')

for token in [
    '営業でご紹介している撮影サンプル',
    '小金井以外で撮影したドローン映像',
    '屋内マイクロドローン撮影',
    '東村山｜企業版ふるさと納税 映像企画',
    'V68 EXTERNAL DRONE SAMPLES',
]:
    if token not in s:
        raise SystemExit(f'Missing sample token: {token}')
if '横田淳氏 撮影' in s or '横田氏 撮影' in s:
    raise SystemExit('Photographer attribution still present')
