from pathlib import Path

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

css = '''
/* V68 BURU TIP EMPHASIS */
.buru-tip{padding:34px 36px!important;grid-template-columns:112px 1fr!important;gap:24px!important;align-items:center!important}
.buru-tip img{width:112px!important;height:112px!important}
.buru-tip strong{font-size:clamp(1.5rem,2.15vw,2.05rem)!important;line-height:1.35!important;letter-spacing:-.02em!important;color:#fff!important}
.buru-tip p{margin-top:12px!important;font-size:clamp(1rem,1.25vw,1.13rem)!important;line-height:1.8!important;color:rgba(255,255,255,.82)!important;max-width:760px!important}
@media(max-width:780px){.buru-tip{grid-template-columns:76px 1fr!important;padding:24px 20px!important;gap:16px!important}.buru-tip img{width:76px!important;height:76px!important}.buru-tip strong{font-size:1.28rem!important}.buru-tip p{font-size:.92rem!important;line-height:1.7!important}}
'''
if '/* V68 BURU TIP EMPHASIS */' not in s:
    s = s.replace('</style>', css + '</style>', 1)

p.write_text(s, encoding='utf-8')

if '/* V68 BURU TIP EMPHASIS */' not in s:
    raise SystemExit('Buru tip emphasis CSS not applied')
