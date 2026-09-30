from pathlib import Path
import re

p = Path("public/index.html")
s = p.read_text(encoding="utf-8")

# Remove previously injected versions so this stays idempotent.
s = re.sub(r'\s*<div class="yokota-drone-feature">.*?</div>\s*(?=<div class="sample-grid">)', '\n', s, count=1, flags=re.S)
s = re.sub(r'\s*<div class="external-drone-samples">.*?</div>\s*(?=</div></section>)', '\n', s, count=1, flags=re.S)

feature = """
<div class="external-drone-samples">
  <div class="external-drone-head">
    <span>DRONE FILM</span>
    <h3>CINEMATIC DRONE WORKS</h3>
  </div>
  <div class="external-drone-grid">
    <article class="video-card external-drone-card">
      <video controls playsinline preload="none" poster="posters/yokota-indoor-drone-sample.jpg">
        <source src="videos/yokota-indoor-drone-sample.mp4" type="video/mp4">
      </video>
      <div class="video-body">
        <h3>屋内マイクロドローン撮影</h3>
      </div>
    </article>
    <article class="video-card external-drone-card">
      <video controls playsinline preload="none" poster="posters/yokota-higashimurayama-drone-sample.jpg">
        <source src="videos/yokota-higashimurayama-drone-sample.mp4" type="video/mp4">
      </video>
      <div class="video-body">
        <h3>東村山｜企業版ふるさと納税 映像企画</h3>
      </div>
    </article>
  </div>
</div>
"""

m = re.search(r'(<section class="section samples" id="samples">.*?)(</div></section>)', s, flags=re.S)
if not m:
    raise SystemExit("Samples section not found")

section = m.group(1).rstrip() + "\n\n" + feature.strip() + "\n"
s = s[:m.start()] + section + m.group(2) + s[m.end():]

css = """
/* V68 EXTERNAL DRONE SAMPLES */
.external-drone-samples{
  margin-top:28px;
  padding:24px;
  border-radius:24px;
  background:linear-gradient(145deg,#061a38 0%,#0b3855 100%);
  border:1px solid rgba(199,162,83,.34);
}
.external-drone-head{
  margin-bottom:16px;
}
.external-drone-head>span{
  display:block;
  color:#f0d995;
  font-size:.64rem;
  font-weight:950;
  letter-spacing:.16em;
}
.external-drone-head h3{
  margin:7px 0 0;
  color:#fff;
  font-size:clamp(1.45rem,2.2vw,2rem);
  line-height:1.15;
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
  border-radius:20px;
}
.external-drone-card video{
  display:block;
  width:100%;
  aspect-ratio:16/9;
  object-fit:cover;
  background:#061a38;
}
.external-drone-card .video-body{
  min-height:62px;
  padding:15px 18px 16px!important;
  background:#fff!important;
  display:flex!important;
  align-items:center!important;
}
.external-drone-card .video-body h3{
  margin:0!important;
  color:#071a33!important;
  font-size:1rem!important;
  line-height:1.4!important;
  font-weight:900!important;
  letter-spacing:-.02em!important;
}
@media(max-width:780px){
  .external-drone-samples{
    padding:18px 14px;
    border-radius:20px;
  }
  .external-drone-grid{
    grid-template-columns:1fr;
    gap:12px;
  }
  .external-drone-card .video-body{
    min-height:58px;
  }
}
"""

s = re.sub(r'/\* V68 YOKOTA DRONE FEATURE \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = re.sub(r'/\* V68 EXTERNAL DRONE SAMPLES \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = s.replace("</style>", css + "\n</style>", 1)

for token in [
    "<h3>CINEMATIC DRONE WORKS</h3>",
    "<h3>屋内マイクロドローン撮影</h3>",
    "<h3>東村山｜企業版ふるさと納税 映像企画</h3>",
    "videos/yokota-indoor-drone-sample.mp4",
    "videos/yokota-higashimurayama-drone-sample.mp4",
    "V68 EXTERNAL DRONE SAMPLES",
]:
    if token not in s:
        raise SystemExit(f"Missing drone sample token: {token}")

for forbidden in [
    "\\n",
    "営業でご紹介している撮影サンプル",
    "以下2本は小金井以外で撮影したドローン映像です。小金井の撮影事例とは分けて、一覧の最後に掲載しています。",
    "横田淳氏 撮影",
]:
    if forbidden in feature:
        raise SystemExit(f"Forbidden drone sample text remains: {forbidden}")

p.write_text(s, encoding="utf-8")
