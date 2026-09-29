from pathlib import Path

p = Path("public/index.html")
s = p.read_text(encoding="utf-8")

marker = '<div class="sample-grid">'
if marker not in s:
    raise SystemExit("sample-grid not found")

indoor = '''<article class="video-card drone-new-sample">
  <video controls playsinline preload="metadata">
    <source src="videos/yokota-indoor-drone-sample.mp4" type="video/mp4">
  </video>
  <div class="video-body">
    <h3>屋内マイクロドローン撮影</h3>
    <p>空間の中を滑らかに巡るドローン映像。</p>
  </div>
</article>'''

higashi = '''<article class="video-card drone-new-sample">
  <video controls playsinline preload="metadata">
    <source src="videos/yokota-higashimurayama-drone-sample.mp4" type="video/mp4">
  </video>
  <div class="video-body">
    <h3>東村山｜企業版ふるさと納税 映像企画</h3>
    <p>地域の魅力を映像で伝えるプロモーションサンプル。</p>
  </div>
</article>'''

# Remove previous copies if the script is re-run.
for src in [
    "videos/yokota-indoor-drone-sample.mp4",
    "videos/yokota-higashimurayama-drone-sample.mp4",
]:
    while src in s:
        start = s.rfind('<article class="video-card', 0, s.find(src))
        end = s.find('</article>', s.find(src))
        if start < 0 or end < 0:
            break
        s = s[:start] + s[end + len('</article>'):]

s = s.replace(marker, marker + indoor + higashi, 1)
p.write_text(s, encoding="utf-8")

for token in [
    "屋内マイクロドローン撮影",
    "東村山｜企業版ふるさと納税 映像企画",
    "videos/yokota-indoor-drone-sample.mp4",
    "videos/yokota-higashimurayama-drone-sample.mp4",
]:
    if token not in s:
        raise SystemExit(f"missing token: {token}")
