from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

css = r'''
/* V68 FINAL LAYOUT CLEANUP */

/* TWO CORE VALUES: keep the explanation under the title on desktop too */
#infra .section-head{
  display:block!important;
  width:100%!important;
  max-width:100%!important;
}
#infra .section-head>div{
  width:100%!important;
  max-width:960px!important;
}
#infra .section-head h2{
  width:100%!important;
  max-width:960px!important;
  margin-top:10px!important;
  font-size:clamp(2.7rem,4.9vw,4.8rem)!important;
  line-height:1.05!important;
  letter-spacing:-.055em!important;
  word-break:normal!important;
  overflow-wrap:normal!important;
  text-wrap:balance!important;
}
#infra .section-head .lead{
  width:100%!important;
  max-width:900px!important;
  margin-top:22px!important;
  padding-bottom:0!important;
  font-size:1.02rem!important;
  line-height:1.9!important;
}

/* Keep the two value cards stable after the stacked heading */
#infra .core-grid{
  margin-top:34px!important;
}
#infra .core-card{
  min-width:0!important;
}

@media(max-width:780px){
  /* TWO CORE VALUES mobile */
  #infra{
    padding-top:60px!important;
  }
  #infra .section-head{
    display:block!important;
  }
  #infra .section-head h2{
    max-width:100%!important;
    font-size:clamp(2rem,9vw,2.55rem)!important;
    line-height:1.12!important;
    letter-spacing:-.04em!important;
    word-break:normal!important;
    overflow-wrap:anywhere!important;
    line-break:strict!important;
    text-wrap:balance!important;
  }
  #infra .section-head h2 br{
    display:none!important;
  }
  #infra .section-head .lead{
    max-width:100%!important;
    margin-top:20px!important;
    font-size:.98rem!important;
    line-height:1.82!important;
    overflow-wrap:anywhere!important;
  }
  #infra .core-grid{
    grid-template-columns:1fr!important;
    gap:18px!important;
    margin-top:28px!important;
  }
  #infra .core-card{
    width:100%!important;
    max-width:100%!important;
    padding:24px 20px!important;
  }
  #infra .core-card h3{
    max-width:100%!important;
    font-size:clamp(1.85rem,8.4vw,2.35rem)!important;
    line-height:1.14!important;
    overflow-wrap:anywhere!important;
  }

  /* Hero mascot */
  .hero-side{
    width:100%!important;
    max-width:100%!important;
    overflow:hidden!important;
  }
  .hero-side .hero-buru{
    width:180px!important;
    max-width:52vw!important;
    height:205px!important;
    max-height:205px!important;
    object-fit:contain!important;
    object-position:center!important;
    margin:0 auto!important;
  }

  /* TOP HERO BACKGROUND VIDEO:
     On phones show the whole 16:9 frame instead of cropping/zooming it
     to the portrait screen. PC remains unchanged. */
  .hero-media{
    background:#03142d!important;
    overflow:hidden!important;
  }
  .hero-media video{
    position:absolute!important;
    inset:0 0 auto 0!important;
    width:100%!important;
    height:56.25vw!important;
    min-height:180px!important;
    max-height:250px!important;
    object-fit:contain!important;
    object-position:center center!important;
    transform:none!important;
    filter:saturate(.92) contrast(1.04) brightness(.78)!important;
  }
  .hero-overlay{
    background:linear-gradient(
      180deg,
      rgba(3,18,42,.34) 0%,
      rgba(3,18,42,.62) 180px,
      rgba(3,18,42,.91) 280px,
      rgba(3,18,42,.97) 100%
    )!important;
  }

  /* Video examples lower on the page */
  #samples .sample-grid,
  #samples .more-grid{
    grid-template-columns:1fr!important;
    gap:16px!important;
    width:100%!important;
    max-width:100%!important;
  }
  #samples .video-card{
    width:100%!important;
    max-width:100%!important;
    margin:0 auto!important;
  }
  #samples .video-card video{
    display:block!important;
    width:100%!important;
    height:auto!important;
    max-height:210px!important;
    aspect-ratio:16/9!important;
    object-fit:cover!important;
    object-position:center!important;
  }
  #samples .video-body{
    padding:12px 14px!important;
  }
  #samples .video-body h3{
    font-size:1.05rem!important;
  }
  #samples .video-body p{
    font-size:.8rem!important;
    line-height:1.55!important;
  }
}

@media(max-width:430px){
  #infra .section-head h2{
    font-size:clamp(1.9rem,8.7vw,2.25rem)!important;
  }
  .hero-side .hero-buru{
    width:165px!important;
    max-width:48vw!important;
    height:190px!important;
    max-height:190px!important;
  }
  .hero-media video{
    height:56.25vw!important;
    min-height:0!important;
    max-height:242px!important;
  }
  #samples .video-card video{
    max-height:195px!important;
  }
}
'''

# Idempotent final override; keep it at the end of the first style block.
s = re.sub(r'/\* V68 FINAL LAYOUT CLEANUP \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

for token in ['V68 FINAL LAYOUT CLEANUP', '#infra .section-head', '#samples .video-card video', '.hero-side .hero-buru', 'TOP HERO BACKGROUND VIDEO']:
    if token not in s:
        raise SystemExit(f'Missing final layout token: {token}')
