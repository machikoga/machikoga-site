from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

pattern = re.compile(
    r'(<div class="trio-stage compact-stage">\s*)'
    r'(<article class="trio-person compact-person suzuki">.*?</article>)\s*'
    r'(<article class="trio-person compact-person buru-center">.*?</article>)\s*'
    r'(<article class="trio-person compact-person yokota">.*?</article>)'
    r'(\s*</div>)',
    re.S,
)

m = pattern.search(s)
if not m:
    raise SystemExit('Partner section order pattern not found')

prefix, suzuki, buru, yokota, suffix = m.groups()
s = s[:m.start()] + prefix + buru + '\n' + suzuki + '\n' + yokota + suffix + s[m.end():]

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
