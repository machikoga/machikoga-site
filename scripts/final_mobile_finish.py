from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

css = r'''
/* V68 FINAL MOBILE FINISH */

/* Emphasize the two key strategy sentences with platform colors. */
#dual-platform .platform-instagram .platform-sub{
  color:#b52655!important;
  font-weight:800!important;
}
#dual-platform .platform-google .platform-sub{
  color:#1459ad!important;
  font-weight:800!important;
}

@media(max-width:780px){
  /* Keep the mobile header / hamburger menu fixed at the top while scrolling. */
  .header{
    position:fixed!important;
    top:0!important;
    left:0!important;
    right:0!important;
    width:100%!important;
    z-index:220!important;
    background:rgba(3,16,38,.97)!important;
    backdrop-filter:blur(14px)!important;
    -webkit-backdrop-filter:blur(14px)!important;
  }
  .header-in{
    height:64px!important;
  }
  .hero{
    padding-top:64px!important;
  }
  .menu-toggle{
    position:relative!important;
    z-index:221!important;
  }
  .mobile-menu-panel{
    top:72px!important;
    z-index:210!important;
  }
  .menu-backdrop{
    z-index:200!important;
  }

  /* Keep the 5,500 / 85% stats card fully visible below the hero. */
  .proof-wrap{
    position:relative!important;
    z-index:5!important;
    padding-top:16px!important;
    background:#fff!important;
    overflow:visible!important;
  }
  .proof{
    transform:none!important;
    margin-top:0!important;
    width:100%!important;
    max-width:100%!important;
    border-radius:24px!important;
    overflow:hidden!important;
  }
  .proof-item{
    min-height:132px!important;
    padding:22px 10px 18px!important;
    display:flex!important;
    flex-direction:column!important;
    justify-content:center!important;
    align-items:center!important;
  }
  .proof-item strong{
    margin:0!important;
    font-size:clamp(2rem,10vw,2.7rem)!important;
    line-height:1!important;
  }
  .proof-item span{
    margin-top:12px!important;
    max-width:95%!important;
    font-size:.72rem!important;
    line-height:1.55!important;
    text-align:center!important;
  }

  #dual-platform .platform-instagram .platform-sub,
  #dual-platform .platform-google .platform-sub{
    padding:12px 14px!important;
    border-radius:15px!important;
    line-height:1.72!important;
  }
  #dual-platform .platform-instagram .platform-sub{
    background:rgba(181,38,85,.07)!important;
  }
  #dual-platform .platform-google .platform-sub{
    background:rgba(20,89,173,.07)!important;
  }
}

@media(max-width:430px){
  .proof-wrap{
    padding-top:14px!important;
  }
  .proof-item{
    min-height:126px!important;
    padding:20px 8px 16px!important;
  }
  .proof-item strong{
    font-size:clamp(1.9rem,9.5vw,2.45rem)!important;
  }
}
'''

s = re.sub(r'/\* V68 FINAL MOBILE FINISH \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

for token in ['V68 FINAL MOBILE FINISH', '.proof-wrap', '.platform-instagram .platform-sub', '.platform-google .platform-sub', 'position:fixed!important', '.menu-toggle']:
    if token not in s:
        raise SystemExit(f'Missing final mobile finish token: {token}')
