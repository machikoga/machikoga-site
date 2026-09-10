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

body {
  position: relative;
}

img, video, svg, iframe {
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
.why-grid,
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
.why-grid > *,
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

@media (max-width: 780px) {
  html, body {
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
  .ai,
  .ai-final,
  .infra,
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
    overflow-x: clip !important;
  }

  .hero-in,
  .section-head,
  .empathy-grid,
  .why-grid,
  .core-grid,
  .offer-grid,
  .results-highlight,
  .trio-stage,
  .partner-system,
  .compare-grid,
  .plan-grid,
  .other-service-grid,
  .ai-contrast,
  .ai-values {
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
  }

  .hero-copy,
  .hero-side,
  .empathy-card,
  .buru-tip,
  .why-card,
  .risk-box,
  .core-card,
  .offer-card,
  .result-impact,
  .trio-person,
  .compare-card,
  .setup-card,
  .plan-card,
  .other-service-card,
  .ai-contrast-card,
  .ai-value,
  .ai-final-message {
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
  }

  .hero-line,
  .focus-message em,
  .result-long-line,
  .market-prices b,
  .compare-price-accent,
  .core-emphasis,
  .role-main span,
  .ai-final-title,
  .ai-final-message strong,
  .ai-final-message span {
    white-space: normal !important;
    overflow-wrap: anywhere !important;
    word-break: normal !important;
  }

  h1, h2, h3,
  .lead,
  .hero-bubble-main,
  .hero-bubble-sub,
  .focus-message,
  .compare-main-copy,
  .compare-subcopy,
  .other-service-body,
  .ai-stock p,
  .ai-contrast-card strong,
  .ai-contrast-card small,
  .ai-value h3,
  .ai-value p {
    max-width: 100% !important;
    overflow-wrap: anywhere;
  }

  .btn,
  .trio-cta,
  .other-service-link {
    max-width: 100% !important;
    white-space: normal !important;
    text-align: center;
  }

  .hero-pr,
  .proof,
  .risk-visual,
  .network-list,
  .buru-stats,
  .authority-box,
  .setup-items,
  .support-row,
  .fan-flow {
    max-width: 100% !important;
    min-width: 0 !important;
  }

  .proof,
  .hero-pr,
  .risk-visual,
  .network-list,
  .buru-stats,
  .authority-box,
  .setup-items,
  .fan-flow {
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
    width: min(320px, 86vw) !important;
    height: auto !important;
  }

  .hero-bubble {
    width: 100% !important;
    max-width: 100% !important;
  }

  .quick-in {
    max-width: 100%;
  }
}
'''

# Keep this as the last responsive override so later scripts cannot re-introduce overflow.
s = re.sub(r'/\* V68 MOBILE OVERFLOW FIX \*/.*?(?=</style>)', '', s, count=1, flags=re.S)
s = s.replace('</style>', css + '\n</style>', 1)

p.write_text(s, encoding='utf-8')

if 'V68 MOBILE OVERFLOW FIX' not in s:
    raise SystemExit('Mobile overflow CSS was not inserted')
