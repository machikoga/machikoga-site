from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

# Do not preload sample videos until the user chooses to play them.
s = s.replace('preload="metadata"', 'preload="none"')

# Replace the rotating hero playlist with one lightweight looping video on desktop.
# Mobile / Save-Data / slow connections use the poster only.
hero_js = r'''const heroItem={src:'videos/massugu-v50.mp4',poster:'posters/massugu-v50.jpg'};
const root=document.getElementById('heroSlides');
if(root){
  root.style.backgroundImage="url('"+heroItem.poster+"')";
  root.style.backgroundSize='cover';
  root.style.backgroundPosition='center';
  root.style.backgroundRepeat='no-repeat';

  const conn=navigator.connection||navigator.mozConnection||navigator.webkitConnection;
  const saveData=!!(conn&&conn.saveData);
  const slow=!!(conn&&/^(slow-2g|2g)$/.test(conn.effectiveType||''));
  const mobile=window.matchMedia('(max-width: 780px)').matches;

  if(!mobile&&!saveData&&!slow){
    const v=document.createElement('video');
    v.muted=true;
    v.autoplay=true;
    v.loop=true;
    v.playsInline=true;
    v.preload='metadata';
    v.poster=heroItem.poster;
    v.src=heroItem.src;
    v.setAttribute('muted','');
    v.setAttribute('autoplay','');
    v.setAttribute('loop','');
    v.setAttribute('playsinline','');
    v.setAttribute('webkit-playsinline','');
    root.appendChild(v);
    v.play().catch(()=>{});
  }
}
'''

pattern = r"const heroVideos=.*?(?=</script>)"
if not re.search(pattern, s, flags=re.S):
    raise SystemExit('Hero video script not found')
s = re.sub(pattern, hero_js + '\n', s, count=1, flags=re.S)

css = r'''
/* V68 HOSTING BANDWIDTH OPTIMIZATION */
.hero-media{
  background-color:#03142d;
  background-size:cover;
  background-position:center;
  background-repeat:no-repeat;
}
@media(max-width:780px){
  .hero-media{
    background-position:center center!important;
  }
}
'''

s = re.sub(r'/\* V68 HOSTING BANDWIDTH OPTIMIZATION \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

for token in [
    "const heroItem={src:'videos/massugu-v50.mp4'",
    'preload="none"',
    'V68 HOSTING BANDWIDTH OPTIMIZATION',
]:
    if token not in s:
        raise SystemExit(f'Missing bandwidth optimization token: {token}')
