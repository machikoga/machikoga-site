from pathlib import Path
import re

p = Path('public/index.html')
s = p.read_text(encoding='utf-8')

css = r'''
/* V68 MOBILE OVERFLOW FIX */
html, body {
  width: 100%;
  max-width: 100%;
  overflow-x: hidden;
}

body { position: relative; }

*, *::before, *::after { box-sizing: border-box; }

img, picture, video, canvas, svg, iframe {
  max-width: 100%;
}

.container,
.section,
.hero,
.hero-in,
.hero-copy,
.hero-side,
.section-head,
.empathy-grid,
.why-premium-head,
.why-reasons,
.why-conclusion,
.core-grid,
.offer-grid,
.results-highlight,
.trio-stage,
.partner-system,
.compare-grid,
.plan-grid,
.other-service-grid,
.ai-final-inner,
.ai-contrast,
.ai-values,
.ai-final-message {
  min-width: 0;
  max-width: 100%;
}

.container > *,
.section > *,
.hero-in > *,
.section-head > *,
.empathy-grid > *,
.why-premium-head > *,
.why-reasons > *,
.why-conclusion > *,
.core-grid > *,
.offer-grid > *,
.results-highlight > *,
.trio-stage > *,
.compare-grid > *,
.plan-grid > *,
.other-service-grid > *,
.ai-contrast > *,
.ai-values > * {
  min-width: 0;
}

/* ---------------------------------------------------------
   PC: empathy / owner-focus section
   Prevent the left headline and the right focus copy colliding.
---------------------------------------------------------- */
@media (min-width: 781px) {
  .empathy-grid {
    grid-template-columns: minmax(0,.92fr) minmax(0,1.28fr) !important;
    gap: 20px !important;
  }

  .empathy-card,
  .buru-tip-final,
  .buru-tip {
    min-width: 0 !important;
    overflow: hidden !important;
  }

  .empathy-card h3 {
    max-width: 100% !important;
    font-size: clamp(2rem,3.05vw,3.25rem) !important;
    line-height: 1.08 !important;
    letter-spacing: -.04em !important;
    white-space: normal !important;
    word-break: normal !important;
    overflow-wrap: anywhere !important;
  }

  .focus-message,
  .focus-message span,
  .focus-message em {
    max-width: 100% !important;
  }

  .focus-message em {
    white-space: normal !important;
    font-size: clamp(2.15rem,3.55vw,3.75rem) !important;
    line-height: 1.06 !important;
    overflow-wrap: anywhere !important;
  }

  .buru-tip-final p,
  .buru-tip p {
    max-width: 100% !important;
    overflow-wrap: anywhere !important;
  }
}

/* ---------------------------------------------------------
   Mobile: one-column, safe widths, natural wrapping
---------------------------------------------------------- */
@media (max-width: 780px) {
  html, body {
    width: 100% !important;
    max-width: 100% !important;
    overflow-x: hidden !important;
  }

  .container,
  .ai-final-inner {
    width: calc(100% - 32px) !important;
    max-width: calc(100% - 32px) !important;
    margin-left: auto !important;
    margin-right: auto !important;
  }

  .section,
  .hero,
  .proof-wrap,
  .quick,
  .empathy,
  .why,
  .why-premium,
  .ai,
  .ai-final,
  .infra,
  .services,
  .offer,
  .results,
  .tools,
  .compare,
  .pricing,
  .other-services,
  .about,
  .cta {
    width: 100% !important;
    max-width: 100% !important;
    overflow-x: hidden !important;
  }

  .hero-in,
  .section-head,
  .empathy-grid,
  .why-premium-head,
  .why-reasons,
  .why-conclusion,
  .core-grid,
  .service-layout,
  .offer-grid,
  .results-highlight,
  .trio-stage,
  .partner-system,
  .compare-grid,
  .plan-grid,
  .other-service-grid,
  .ai-contrast,
  .ai-values,
  .ai-values-premium,
  .easy-wrap,
  .fan-flow,
  .showcase-grid,
  .about-wrap {
    display: grid !important;
    grid-template-columns: minmax(0,1fr) !important;
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
  }

  .hero-copy,
  .hero-side,
  .empathy-card,
  .buru-tip,
  .buru-tip-final,
  .why-card,
  .why-reason,
  .why-conclusion,
  .risk-box,
  .core-card,
  .service-main,
  .service-side,
  .service-mini,
  .offer-card,
  .result-impact,
  .trio-person,
  .compare-card,
  .setup-card,
  .plan-card,
  .other-service-card,
  .ai-stock,
  .ai-contrast-card,
  .ai-value,
  .ai-final-message {
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
  }

  /* Large text: force wrap instead of clipping to the right. */
  .hero-line,
  .focus-message,
  .focus-message span,
  .focus-message em,
  .result-long-line,
  .market-prices b,
  .compare-price-accent,
  .core-emphasis,
  .role-main span,
  .why-premium-head h2,
  .why-conclusion h3,
  .ai-final-title,
  .ai-final-message strong,
  .ai-final-message span {
    white-space: normal !important;
    max-width: 100% !important;
    overflow-wrap: anywhere !important;
    word-break: normal !important;
  }

  /* ⑤ WEB / 社長 section */
  .empathy-grid {
    gap: 18px !important;
  }

  .empathy-card,
  .buru-tip-final,
  .buru-tip {
    padding: 24px 20px !important;
    border-radius: 24px !important;
    overflow: hidden !important;
  }

  .empathy-card h3 {
    font-size: clamp(2rem,10.2vw,2.85rem) !important;
    line-height: 1.10 !important;
    letter-spacing: -.04em !important;
    white-space: normal !important;
    overflow-wrap: anywhere !important;
  }

  .buru-tip-final {
    display: grid !important;
    grid-template-columns: 1fr !important;
    gap: 16px !important;
  }

  .buru-tip-final img,
  .buru-tip img {
    width: 112px !important;
    height: 112px !important;
    margin: 0 !important;
  }

  .focus-message span {
    font-size: clamp(1.8rem,8.5vw,2.35rem) !important;
    line-height: 1.08 !important;
  }

  .focus-message em {
    margin-top: 8px !important;
    font-size: clamp(2.15rem,10.4vw,3rem) !important;
    line-height: 1.08 !important;
  }

  .buru-tip-final p,
  .buru-tip p {
    font-size: .95rem !important;
    line-height: 1.8 !important;
    overflow-wrap: anywhere !important;
  }

  /* ④ WHY NOW */
  .why-premium-head {
    gap: 18px !important;
    margin-bottom: 24px !important;
  }

  .why-premium-head h2 {
    margin-top: 8px !important;
    font-size: clamp(2.55rem,11vw,3.45rem) !important;
    line-height: 1.06 !important;
    letter-spacing: -.05em !important;
    text-wrap: balance !important;
  }

  .why-premium-lead {
    padding: 0 !important;
    max-width: 100% !important;
    font-size: 1rem !important;
    line-height: 1.85 !important;
  }

  .why-reasons {
    gap: 16px !important;
  }

  .why-reason {
    min-height: 0 !important;
    padding: 22px 20px !important;
  }

  .why-reason h3 {
    font-size: 1.45rem !important;
    white-space: normal !important;
    overflow-wrap: anywhere !important;
    word-break: normal !important;
  }

  .why-conclusion {
    padding: 24px 20px !important;
    gap: 20px !important;
  }

  .why-conclusion h3 {
    font-size: clamp(2rem,9.5vw,2.75rem) !important;
    line-height: 1.12 !important;
  }

  .why-entry-grid {
    grid-template-columns: 1fr 1fr !important;
    gap: 8px !important;
  }

  /* ②③ AI section */
  .ai-final {
    padding-left: 0 !important;
    padding-right: 0 !important;
  }

  .ai-final-title {
    width: 100% !important;
    font-size: clamp(2.15rem,9.7vw,3rem) !important;
    line-height: 1.08 !important;
    letter-spacing: -.045em !important;
    text-wrap: balance !important;
  }

  .ai-final-lead {
    width: 100% !important;
    max-width: 100% !important;
    font-size: 1rem !important;
    line-height: 1.82 !important;
    overflow-wrap: anywhere !important;
  }

  .ai-stock {
    padding: 18px !important;
  }

  .ai-stock p {
    font-size: .95rem !important;
    line-height: 1.8 !important;
    overflow-wrap: anywhere !important;
  }

  .ai-contrast {
    gap: 10px !important;
  }

  .ai-contrast-card {
    padding: 22px 20px !important;
  }

  .ai-contrast-card strong,
  .ai-contrast-card small {
    max-width: 100% !important;
    white-space: normal !important;
    overflow-wrap: anywhere !important;
  }

  .ai-values {
    gap: 12px !important;
  }

  .ai-value {
    min-height: 0 !important;
    padding: 20px !important;
  }

  .ai-final-message {
    padding: 28px 20px !important;
    border-radius: 24px !important;
    overflow: hidden !important;
  }

  .ai-final-message span {
    font-size: clamp(1.9rem,8.8vw,2.65rem) !important;
    line-height: 1.10 !important;
    letter-spacing: -.04em !important;
  }

  .ai-final-message strong {
    font-size: clamp(1.65rem,7.7vw,2.35rem) !important;
    line-height: 1.14 !important;
    letter-spacing: -.035em !important;
  }

  h1, h2, h3,
  .lead,
  .hero-bubble-main,
  .hero-bubble-sub,
  .compare-main-copy,
  .compare-subcopy,
  .other-service-body {
    max-width: 100% !important;
    overflow-wrap: anywhere !important;
  }

  .btn,
  .trio-cta,
  .other-service-link {
    max-width: 100% !important;
    white-space: normal !important;
    text-align: center !important;
  }

  .proof,
  .hero-pr,
  .risk-visual,
  .network-list,
  .buru-stats,
  .authority-box,
  .setup-items {
    max-width: 100% !important;
    min-width: 0 !important;
  }

  .proof,
  .hero-pr,
  .risk-visual,
  .network-list,
  .buru-stats,
  .authority-box {
    grid-template-columns: 1fr 1fr !important;
  }

  .support-row {
    display: flex !important;
    flex-wrap: wrap !important;
  }

  .support-row > *,
  .setup-items > *,
  .authority-mini > *,
  .chip-row > * {
    min-width: 0 !important;
    max-width: 100% !important;
  }

  .compare-summary {
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    grid-template-columns: 1fr !important;
  }

  .market-prices div,
  .compare-points div {
    min-width: 0 !important;
    max-width: 100% !important;
  }

  .hero-buru {
    width: min(320px,86vw) !important;
    height: auto !important;
  }

  .hero-bubble {
    width: 100% !important;
    max-width: 100% !important;
  }

  /* Quick links: wrap instead of visibly cutting off on iPhone. */
  .quick-in {
    display: flex !important;
    flex-wrap: wrap !important;
    overflow: visible !important;
    max-width: 100% !important;
  }

  .quick a {
    flex: 0 1 auto !important;
    min-width: 0 !important;
    max-width: 100% !important;
  }

  /* Fixed CTA must stay inside the viewport. */
  .mobile-actions,
  .mobile-cta,
  .sticky-cta,
  .floating-cta {
    left: 12px !important;
    right: 12px !important;
    width: auto !important;
    max-width: calc(100% - 24px) !important;
  }
}

@media (max-width: 430px) {
  .container,
  .ai-final-inner {
    width: calc(100% - 24px) !important;
    max-width: calc(100% - 24px) !important;
  }

  .why-premium-head h2 {
    font-size: clamp(2.35rem,10.5vw,2.85rem) !important;
  }

  .ai-final-title {
    font-size: clamp(2rem,9.2vw,2.65rem) !important;
  }

  .ai-final-message span {
    font-size: clamp(1.75rem,8.4vw,2.35rem) !important;
  }

  .ai-final-message strong {
    font-size: clamp(1.5rem,7.2vw,2.05rem) !important;
  }
}
'''

# Keep this as the last responsive override so later scripts cannot re-introduce overflow.
s = re.sub(r'/\* V68 MOBILE OVERFLOW FIX \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

required = [
    'V68 MOBILE OVERFLOW FIX',
    '.why-premium-head',
    '.ai-final-title',
    '.focus-message em',
    'grid-template-columns: minmax(0,1fr)',
]
for token in required:
    if token not in s:
        raise SystemExit(f'Missing responsive token: {token}')
