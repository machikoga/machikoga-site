from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

# Remove any previously injected version of this two-video sample block.
s = re.sub(r'\s*<div class="yokota-drone-feature">.*?</div>\s*(?=<div class="sample-grid">)', '\n', s, count=1, flags=re.S)
s = re.sub(r'\s*<div class="external-drone-samples">.*?</div>\s*(?=</div></section>)', '\n', s, count=1, flags=re.S)

feature = r'''
<div class="external-drone-samples">
  <div class="external-drone-head">
    <span>OTHER DRONE SAMPLES</span>
    <h3>撮影サンプル</h3>
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

# Put the two samples at the very end of the DRONE & VIDEO SAMPLES section.
m = re.search(r'(<section class="section samples" id="samples">.*?)(</div></section>)', s, flags=re.S)
if not m:
    raise SystemExit('Samples section not found')
section = m.group(1)
section = section.rstrip() + '\n\n' + feature.strip() + '\n'
s = s[:m.start()] + section + m.group(2) + s[m.end():]

css = r'''
/* V68 EXTERNAL DRONE SAMPLES */
.external-drone-samples{
  margin-top:26px;
  padding:22px;
  border-radius:24px;
  background:linear-gradient(145deg,#061a38 0%,#0b3855 100%);
  border:1px solid rgba(199,162,83,.34);
}
.external-drone-head{
  margin-bottom:14px;
}
.external-drone-head>span{
  display:block;
  color:#f0d995;
  font-size:.64rem;
  font-weight:950;
  letter-spacing:.14em;
}
.external-drone-head h3{
  margin:6px 0 0;
  color:#fff;
  font-size:clamp(1.4rem,2.1vw,2rem);
  line-height:1.2;
  letter-spacing:-.03em;
}
.external-drone-grid{
  display:grid;
  grid-template-columns:repeat(2,minmax(0,1fr));
  gap:14px;
}
.external-drone-card{
  overflow:hidden;
  background:#fff;
  border:0!important;
}
.external-drone-card video{
  display:block;
  width:100%;
  aspect-ratio:16/9;
  object-fit:cover;
  background:#061a38;
}
.external-drone-card .video-body{
  padding:14px 16px 16px;
}
.external-drone-card .video-body h3{
  margin:0;
  font-size:1rem!important;
}
.external-drone-card .video-body p{
  margin-top:6px!important;
  font-size:.76rem!important;
  line-height:1.6!important;
}
@media(max-width:780px){
  .external-drone-samples{
    padding:17px 14px;
    border-radius:20px;
  }
  .external-drone-grid{
    grid-template-columns:1fr;
    gap:12px;
  }
}
'''

s = re.sub(r'/\* V68 YOKOTA DRONE FEATURE \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = re.sub(r'/\* V68 EXTERNAL DRONE SAMPLES \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

for token in [
    '<h3>DRONE FILM SHOWCASE</h3>',
    'videos/yokota-indoor-drone-sample.mp4',
    'videos/yokota-higashimurayama-drone-sample.mp4',
    'V68 EXTERNAL DRONE SAMPLES',
]:
    if token not in s:
        raise SystemExit(f'Missing drone sample token: {token}')

for forbidden in [
    '営業でご紹介している撮影サンプル',
    '以下2本は小金井以外で撮影したドローン映像です。小金井の撮影事例とは分けて、一覧の最後に掲載しています。',
    '横田淳氏 撮影',
]:
    if forbidden in s:
        raise SystemExit(f'Forbidden drone sample text remains: {forbidden}')
