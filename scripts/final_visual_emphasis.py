from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

# ------------------------------------------------------------
# 1) Keep headings from breaking awkwardly.
# ------------------------------------------------------------
s = s.replace('<h2>なぜ、今整えるのか。</h2>', '<h2 class="why-balance-title">なぜ、今整えるのか。</h2>')
s = s.replace('<div class="role-main"><span>価値は、すでにある。</span><span>まちこがは、それを見つかる形にする。</span></div>', '<div class="role-main counter-copy"><span>価値は、すでにある。</span><span>まちこがは、それを見つかる形にする。</span></div>')

# ------------------------------------------------------------
# 2) Make the two core PR points visually explicit.
#    PR POINT 01 is the main product promise, so it gets the
#    premium/dominant treatment. PR POINT 02 remains strong but
#    is intentionally quieter.
# ------------------------------------------------------------
s = s.replace(
    '<h3>小金井で強い、<br>自前の情報インフラ。</h3>',
    '<h3>小金井で強い、<br><span class="core-emphasis core-emphasis-one">自前の情報インフラ。</span></h3>'
)
s = s.replace(
    '<h3>同じ1回の発信を、<br>小金井で数倍強くする。</h3>',
    '<h3>同じ1回の発信を、<br><span class="core-emphasis core-emphasis-two">小金井で数倍強くする。</span></h3>'
)

# ------------------------------------------------------------
# 3) Final CSS layer. Inject once; if already present, refresh it.
# ------------------------------------------------------------
css = r'''
/* V68 FINAL VISUAL EMPHASIS */

/* ---- WHY NOW: readable heading + visual cards ---- */
.why-balance-title{
  max-width:9.2em;
  word-break:keep-all;
  overflow-wrap:normal;
  text-wrap:balance;
  line-height:1.02;
}
.why-grid{gap:18px}
.why-card{
  position:relative;
  padding:30px 28px 26px;
  border-radius:28px;
  border:1px solid #d9e3ef;
  background:linear-gradient(180deg,#fff 0%,#f8fbff 100%);
  box-shadow:0 16px 38px rgba(6,26,56,.07);
  overflow:hidden;
}
.why-card:before{
  content:"";
  position:absolute;
  top:0;left:0;right:0;
  height:5px;
  background:linear-gradient(90deg,#1659a8,#0d9b99);
}
.why-card .mark{
  width:84px;
  height:84px;
  border-radius:24px;
  margin-bottom:22px;
  font-size:1.65rem;
  letter-spacing:-.02em;
  box-shadow:0 14px 28px rgba(6,26,56,.18);
}
.why-grid .why-card:nth-child(1) .mark{
  background:linear-gradient(135deg,#113b7a,#2468bd);
}
.why-grid .why-card:nth-child(2) .mark{
  background:linear-gradient(135deg,#0c607b,#10a6a0);
}
.why-grid .why-card:nth-child(3) .mark{
  background:linear-gradient(135deg,#8d6222,#d0a449);
}
.why-card h3{
  font-size:clamp(1.42rem,2.1vw,1.9rem);
  line-height:1.28;
  letter-spacing:-.025em;
}
.why-card p{
  font-size:.98rem;
  line-height:1.8;
}
.why-card .small{
  margin-top:18px;
  padding-top:15px;
  font-size:.86rem;
  color:#52647d;
}

/* ---- COUNTER AI: more dramatic and easier to scan ---- */
.ai{
  background:
    radial-gradient(circle at 12% 8%,rgba(240,217,149,.18),transparent 25%),
    radial-gradient(circle at 90% 18%,rgba(12,139,134,.16),transparent 30%),
    linear-gradient(145deg,#031735 0%,#082b5f 52%,#0b4769 100%);
}
.ai .section-head h2{
  max-width:10em;
  word-break:keep-all;
  overflow-wrap:normal;
  text-wrap:balance;
}
.sales-five{
  gap:14px;
}
.sales-five .value-card{
  position:relative;
  min-height:172px;
  padding:25px 22px 20px;
  border-radius:24px;
  background:linear-gradient(180deg,rgba(255,255,255,.10),rgba(255,255,255,.055));
  border:1px solid rgba(255,255,255,.16);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 16px 35px rgba(0,0,0,.08);
}
.sales-five .value-card:before{
  content:"COUNTER AI";
  display:inline-flex;
  margin-bottom:15px;
  padding:4px 8px;
  border-radius:999px;
  background:rgba(240,217,149,.14);
  border:1px solid rgba(240,217,149,.26);
  color:#f0d995;
  font-size:.56rem;
  font-weight:900;
  letter-spacing:.1em;
}
.sales-five .value-card b{
  font-size:1.48rem;
  color:#fff;
}
.sales-five .value-card span{
  font-size:.92rem;
  line-height:1.65;
  color:rgba(255,255,255,.72);
}
.sales-five .value-card.center{
  background:linear-gradient(145deg,#fffdf7,#edf5ff);
  border:2px solid rgba(240,217,149,.76);
  transform:translateY(-8px);
  box-shadow:0 22px 46px rgba(0,0,0,.18);
}
.sales-five .value-card.center:before{
  content:"ONLY HERE";
  background:#0b2b58;
  border:0;
  color:#f0d995;
}
.sales-five .value-card.center b{color:#071d3f}
.sales-five .value-card.center span{color:#586a82}
.role-card{
  position:relative;
  margin-top:26px;
  padding:38px 34px 34px;
  border-radius:32px;
  overflow:hidden;
  background:linear-gradient(180deg,#fff,#f7faff);
  border:1px solid #dce5f0;
  box-shadow:0 26px 58px rgba(0,0,0,.17);
}
.role-card:before{
  content:"";
  position:absolute;
  left:0;right:0;top:0;
  height:6px;
  background:linear-gradient(90deg,#c7a253,#f0d995,#0c8b86);
}
.counter-copy{
  display:grid;
  gap:7px;
  text-align:center;
}
.counter-copy span{
  display:block;
  word-break:keep-all;
  overflow-wrap:normal;
  text-wrap:balance;
}
.counter-copy span:first-child{
  color:#9b6a26;
  font-size:clamp(2.25rem,4vw,4.5rem);
  line-height:1.04;
}
.counter-copy span:last-child{
  color:#071d3f;
  font-size:clamp(1.9rem,3.5vw,3.8rem);
  line-height:1.08;
}

/* ---- THE MOST IMPORTANT PART: two core selling points ---- */
.core-grid{
  gap:22px;
  align-items:stretch;
}
.core-card{
  min-height:100%;
}
.core-card.one.core-primary{
  position:relative;
  background:
    radial-gradient(circle at 95% 0%,rgba(14,172,166,.32),transparent 34%),
    linear-gradient(145deg,#061a38 0%,#0a3970 58%,#096d73 100%);
  color:#fff;
  border:2px solid rgba(240,217,149,.78);
  box-shadow:0 28px 68px rgba(6,26,56,.22),0 0 0 5px rgba(199,162,83,.08);
  transform:translateY(-6px);
}
.core-card.one.core-primary:before{
  height:7px;
  background:linear-gradient(90deg,#f0d995,#c7a253,#35c4b9);
}
.core-card.one.core-primary .core-label{
  display:inline-flex;
  padding:6px 11px;
  border-radius:999px;
  color:#061a38;
  background:#f0d995;
  font-size:.74rem;
}
.core-card.one.core-primary h3,
.core-card.one.core-primary p{
  color:#fff;
}
.core-card.one.core-primary p{color:rgba(255,255,255,.82)}
.core-card.one.core-primary .asset-note{
  background:rgba(3,16,38,.58);
  border:1px solid rgba(255,255,255,.12);
}
.core-card.one.core-primary .asset-note b{color:#f0d995}
.core-card.one.core-primary .network-list div{
  background:rgba(255,255,255,.10);
  border-color:rgba(255,255,255,.14);
  color:#fff;
}
.core-emphasis{
  display:inline;
  position:relative;
  z-index:1;
}
.core-emphasis-one{
  color:#f7dc87;
  text-shadow:0 2px 18px rgba(240,217,149,.16);
}
.core-emphasis-one:after{
  content:"";
  position:absolute;
  left:0;right:0;bottom:-5px;
  height:7px;
  border-radius:999px;
  background:linear-gradient(90deg,#f0d995,#4ad1c6);
  opacity:.9;
  z-index:-1;
}
.core-card.two{
  background:linear-gradient(145deg,#f8fbff,#edf7f7);
  color:#071d3f;
  border:1px solid #cfe1e7;
  box-shadow:0 18px 46px rgba(6,26,56,.09);
}
.core-card.two:before{
  background:linear-gradient(90deg,#0f5fa5,#0c8b86);
}
.core-card.two .core-label{
  display:inline-flex;
  padding:6px 11px;
  border-radius:999px;
  background:#0a3a70;
  color:#fff;
}
.core-card.two h3{color:#071d3f}
.core-card.two p{color:#526178}
.core-card.two .one-post{
  background:linear-gradient(145deg,#0a315e,#0a6f73);
  color:#fff;
}
.core-card.two .branch{
  background:rgba(255,255,255,.13);
  color:#fff;
}
.core-card.two .bigline{color:#071d3f}
.core-emphasis-two{
  color:#087e84;
  text-shadow:0 2px 12px rgba(12,139,134,.12);
}
.core-emphasis-two:after{
  content:"";
  position:absolute;
  left:0;right:0;bottom:-5px;
  height:6px;
  border-radius:999px;
  background:linear-gradient(90deg,#0c8b86,#4cb8d2);
  opacity:.25;
  z-index:-1;
}

@media(max-width:900px){
  .why-balance-title{max-width:none}
  .sales-five{grid-template-columns:1fr 1fr}
  .sales-five .value-card.center{grid-column:1/-1;transform:none}
}
@media(max-width:780px){
  .why-card{padding:22px 20px 20px}
  .why-card .mark{width:72px;height:72px;border-radius:20px;font-size:1.4rem}
  .why-card h3{font-size:1.42rem}
  .sales-five{grid-template-columns:1fr}
  .sales-five .value-card{min-height:auto}
  .role-card{padding:28px 18px 24px}
  .counter-copy span:first-child{font-size:clamp(2rem,10vw,3rem)}
  .counter-copy span:last-child{font-size:clamp(1.55rem,8vw,2.6rem)}
  .core-card.one.core-primary{transform:none}
  .core-card h3{font-size:clamp(1.85rem,8vw,2.55rem)}
}
'''

marker = '/* V68 FINAL VISUAL EMPHASIS */'
if marker in s:
    s = re.sub(r'/\* V68 FINAL VISUAL EMPHASIS \*/.*?(?=</style>)', css.strip() + '\n', s, count=1, flags=re.S)
else:
    s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

required = [
    'why-balance-title',
    'counter-copy',
    'core-emphasis-one',
    'core-emphasis-two',
    'V68 FINAL VISUAL EMPHASIS',
]
for item in required:
    if item not in s:
        raise SystemExit(f'Missing visual-emphasis marker: {item}')
