from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

stage_match = re.search(
    r'(<div class="trio-stage compact-stage">)(.*?)(</div>\s*</div>\s*</section>)',
    s,
    re.S,
)
if not stage_match:
    raise SystemExit('Partner stage not found')

stage_inner = stage_match.group(2)
articles = re.findall(r'<article class="trio-person compact-person [^"]+">.*?</article>', stage_inner, re.S)
if len(articles) < 3:
    raise SystemExit('Partner cards not found')

buru = next((a for a in articles if 'buru-center' in a), None)
suzuki = next((a for a in articles if 'suzuki' in a), None)
yokota = next((a for a in articles if 'yokota' in a), None)
if not all([buru, suzuki, yokota]):
    raise SystemExit('One or more partner cards missing')

# Always rebuild in the desired order. This is safe to run repeatedly.
new_inner = '\n' + buru + '\n' + suzuki + '\n' + yokota + '\n'
s = s[:stage_match.start(2)] + new_inner + s[stage_match.end(2):]

css = r'''
/* V68 BURU FIRST */
.compact-stage{grid-template-columns:1.05fr 1fr 1fr!important}
.compact-stage .buru-center{order:1;transform:none!important}
.compact-stage .suzuki{order:2}
.compact-stage .yokota{order:3}
@media(max-width:780px){
  .compact-stage{grid-template-columns:1fr!important}
  .compact-stage .buru-center{order:1!important}
  .compact-stage .suzuki{order:2!important}
  .compact-stage .yokota{order:3!important}
}
'''

s = re.sub(r'/\* V68 BURU FIRST \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

stage = re.search(r'<div class="trio-stage compact-stage">(.*?)</div>\s*</div>\s*</section>', s, re.S)
if not stage:
    raise SystemExit('Partner stage not found after reorder')
chunk = stage.group(1)
if not (chunk.find('buru-center') < chunk.find('suzuki') < chunk.find('yokota')):
    raise SystemExit('Buru is not first after reorder')
