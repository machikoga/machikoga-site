from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

# Keep sample videos lazy: only load when the visitor chooses to play them.
s = s.replace('preload="metadata"', 'preload="none"')

# Restore the 9-video rotating hero playlist on BOTH desktop and mobile.
# Only the currently playing hero video is loaded; the next one starts after "ended".
hero_js = r'''const heroVideos=[
  {src:'videos/rokko-v47.mp4',poster:'posters/rokko-v47.jpg'},
  {src:'videos/kamokyu-v47.mp4',poster:'posters/kamokyu-v47.jpg'},
  {src:'videos/nijiiro-v47.mp4',poster:'posters/nijiiro-v47.jpg'},
  {src:'videos/cercle-v47.mp4',poster:'posters/cercle-v47.jpg'},
  {src:'videos/sukkiri-v50.mp4',poster:'posters/sukkiri-v50.jpg'},
  {src:'videos/massugu-v50.mp4',poster:'posters/massugu-v50.jpg'},
  {src:'videos/zendokai-v50.mp4',poster:'posters/zendokai-v50.jpg'},
  {src:'videos/tekkaba-v50.mp4',poster:'posters/tekkaba-v50.jpg'},
  {src:'videos/agreco-v50.mp4',poster:'posters/agreco-v50.jpg'}
];
function shuffle(list){
  const a=[...list];
  for(let i=a.length-1;i>0;i--){
    const j=Math.floor(Math.random()*(i+1));
    [a[i],a[j]]=[a[j],a[i]];
  }
  return a;
}
const playlist=shuffle(heroVideos);
const root=document.getElementById('heroSlides');
if(root){
  const first=playlist[0];
  root.style.backgroundImage="url('"+first.poster+"')";
  root.style.backgroundSize='cover';
  root.style.backgroundPosition='center';
  root.style.backgroundRepeat='no-repeat';

  const v=document.createElement('video');
  v.muted=true;
  v.autoplay=true;
  v.playsInline=true;
  v.preload='metadata';
  v.setAttribute('muted','');
  v.setAttribute('autoplay','');
  v.setAttribute('playsinline','');
  v.setAttribute('webkit-playsinline','');
  root.appendChild(v);

  let p=0;
  const play=()=>{
    const item=playlist[p%playlist.length];
    root.style.backgroundImage="url('"+item.poster+"')";
    v.poster=item.poster;
    v.src=item.src;
    v.load();
    v.play().catch(()=>{});
  };

  v.addEventListener('ended',()=>{
    p=(p+1)%playlist.length;
    play();
  });
  v.addEventListener('error',()=>{
    p=(p+1)%playlist.length;
    setTimeout(play,180);
  });

  const resume=()=>v.play().catch(()=>{});
  document.addEventListener('touchstart',resume,{once:true,passive:true});
  document.addEventListener('click',resume,{once:true});

  play();
}
'''

# Handle either the original playlist script or the temporary single-video script.
patterns = [
    r"const heroVideos=.*?(?=</script>)",
    r"const heroItem=.*?(?=</script>)",
]
matched = False
for pattern in patterns:
    if re.search(pattern, s, flags=re.S):
        s = re.sub(pattern, hero_js + '\n', s, count=1, flags=re.S)
        matched = True
        break
if not matched:
    raise SystemExit('Hero video script not found')

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
    "const heroVideos=[",
    "videos/agreco-v50.mp4",
    "v.addEventListener('ended'",
    'preload="none"',
    'V68 HOSTING BANDWIDTH OPTIMIZATION',
]:
    if token not in s:
        raise SystemExit(f'Missing hero restore token: {token}')
