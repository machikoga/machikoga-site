from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

# Comparison: remove the fixed 18万円 starting-price message.
s = s.replace(
    '必要な土台をまとめて、<br><span class="compare-price-accent">参考18万円から。</span>',
    '必要な土台をまとめて、<br><span class="compare-price-accent">小金井地元価格で提案します。</span>'
)
s = s.replace(
    '必要な土台をまとめて、<br>参考18万円から。',
    '必要な土台をまとめて、<br>小金井地元価格で提案します。'
)
s = s.replace('参考18万円から。', '小金井地元価格で提案します。')

# Pricing: initial setup is custom-made rather than a fixed 180,000 yen.
s = s.replace('<h3>初期設計の参考</h3>', '<h3>初期設計</h3>')
s = re.sub(
    r'<div class="reference-price"><small>参考価格</small><strong>180,000円</strong><span>税込</span></div>',
    '<div class="reference-price custom-made"><small>料金</small><strong>オーダーメイド</strong><span>内容に合わせてご提案</span></div>',
    s,
    count=1,
)

# Safety net for older markup.
s = s.replace('<strong>180,000円<small>税込</small></strong>', '<strong class="custom-made-price">オーダーメイド<small>内容に合わせてご提案</small></strong>')

# Adjust note so it does not imply a fixed initial fee.
s = s.replace(
    '下記は参考価格です。必要な施策・撮影範囲・更新頻度・運用サポートに合わせて、内容も金額も個別にご提案します。',
    '必要な施策・撮影範囲・更新頻度・運用サポートに合わせて、内容も金額も個別にご提案します。'
)

css = r'''
/* V68 LOCAL PRICE COPY */
.compare-machikoga .compare-price-accent{color:#f0d995;display:inline-block;max-width:16em}
.pricing-final .reference-price.custom-made{min-width:240px;text-align:right}
.pricing-final .reference-price.custom-made strong{display:block;font-size:clamp(1.45rem,2.35vw,2.15rem)!important;color:#071d3f;white-space:nowrap}
.pricing-final .reference-price.custom-made span{display:block;margin-top:5px;color:#6b778b;font-size:.72rem;font-weight:700}
@media(max-width:780px){
  .pricing-final .reference-price.custom-made{text-align:left;min-width:0}
  .pricing-final .reference-price.custom-made strong{white-space:normal}
}
'''
if '/* V68 LOCAL PRICE COPY */' in s:
    s = re.sub(r'/\* V68 LOCAL PRICE COPY \*/.*?(?=</style>)', css.strip() + '\n', s, count=1, flags=re.S)
else:
    s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

for token in ['小金井地元価格で提案します。', 'オーダーメイド', 'V68 LOCAL PRICE COPY']:
    if token not in s:
        raise SystemExit(f'Missing local-price token: {token}')

if '参考18万円から。' in s:
    raise SystemExit('Old 18万円 copy still remains')
