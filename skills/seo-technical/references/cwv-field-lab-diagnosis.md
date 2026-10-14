# Core Web Vitals — field vs lab diagnosis

## Contents

- Scope
- What a CWV verdict may claim
- Lab runs that can be compared
- Reconciling field and lab
- INP: locate the phase first
- CLS: the element that moved is often the victim
- LCP additions to the subparts table
- Perishable tooling notes
- Unverified
- Sources

## Scope

This file sits beside [performance-images-and-sitemaps-1.md](performance-images-and-sitemaps-1.md#lcp-subparts) (the LCP phase split) and the CWV bar in [rendering-and-sitemaps.md](rendering-and-sitemaps.md#core-web-vitals). Documented facts below cite web.dev, Chrome or tool docs read on 2026-10-12.

## What a CWV verdict may claim

- The thresholds are judged at the **75th percentile of page loads**, segmented across mobile and desktop: LCP good ≤ 2.5 s; INP good ≤ 200 ms; CLS good ≤ 0.1 `[documented: https://web.dev/articles/vitals, 2026-10-12]`. INP poor > 500 ms `[documented: https://web.dev/articles/inp, 2026-10-12]`; CLS poor > 0.25 `[documented: https://web.dev/articles/cls, 2026-10-12]`.
- LCP poor threshold: unverified [unverified: the 4 s figure appears only in an image alt text of the saved optimize-lcp page, not its text]; see ## Unverified.
- **Without runtime evidence there is no failing verdict.** Reading source code alone, list probable causes as hypotheses and name the exact measurement that would confirm each one `[practitioner]`.
- **No CrUX record means "unavailable", not "passing".** Localhost, staging, new, private and low-traffic URLs frequently have no record `[practitioner]`.
- **Say which scope the number has:** page-level, or the origin fallback. Origin data is context; it does not prove anything about one route `[practitioner]`.
- **Report phone and desktop separately**; never blend form factors `[practitioner]`.
- A `PerformanceObserver` reading from one browser session is a **lab observation**, never field data `[practitioner]`.
- **Do not announce a field improvement just after a deploy.** CrUX data is a 28-day rolling average, so either wait until new visits accumulate or use first-party RUM `[documented: https://developer.chrome.com/docs/crux/api, 2026-10-12]`.
- For production RUM, use the `web-vitals` library (its attribution build adds debugging data): it measures the metrics on real users in a way that matches how Chrome measures them and reports them to CrUX, PageSpeed Insights and Search Console `[documented: https://raw.githubusercontent.com/GoogleChrome/web-vitals/main/README.md, 2026-10-12]`.

## Lab runs that can be compared

`[practitioner]`

Write down with every lab figure: the final URL and page state, browser and Lighthouse versions, viewport / form factor, CPU and network throttling, cold or warm cache, and the auth, consent and experiment state. Default to mobile conditions on a public-site audit.

- To decide on a headline lab metric, take **at least 3 equivalent navigations and report the median plus the range**. Lighthouse itself recommends aggregate values such as the median over single runs (the median of 5 runs is twice as stable as 1 run) `[documented: https://raw.githubusercontent.com/GoogleChrome/lighthouse/main/docs/variability.md, 2026-10-12]`, and its throttling is simulated by default `[documented: https://raw.githubusercontent.com/GoogleChrome/lighthouse/main/docs/throttling.md, 2026-10-12]`.
- **Compare metric values, never the Lighthouse score** — the score's weighting changes between Lighthouse versions.
- **The Lighthouse SEO category is a hygiene checklist** of basic audits (meta description, descriptive link text, hreflang, canonical, HTTP status, robots.txt, tap targets, plus a manual structured-data check), each weighted equally `[documented: https://developer.chrome.com/docs/lighthouse/seo/, 2026-10-12]`. It is not a ranking score; a 100 there says the basics are present, nothing more `[practitioner]`. Lab data is not field CWV.

## Reconciling field and lab

| Field | Lab | Read it as |
|---|---|---|
| Poor | Poor | A reproducible problem — trace it and fix the dominant bottleneck |
| Poor | Good | The lab is missing real conditions — segment RUM by device, route, cache state, interaction |
| Good | Poor | The cold or throttled case is fragile — do not tell the client their users are failing |
| Unavailable | Any | Diagnose with the lab; recommend RUM where production impact matters |

Report layout: open with an evidence table whose columns are signal, scope and conditions, baseline, after, source (in that order); follow with measured failures → causes backed by a trace → hypotheses from source → fixes → verification status.

## INP: locate the phase first

`[documented: https://web.dev/articles/optimize-inp, 2026-10-12]`

| Phase | Evidence | Typical fix |
|---|---|---|
| **Input delay** | Long tasks already running on the main thread before the callback starts | Trim startup work, split long tasks, defer third parties |
| **Processing time** | The event callbacks and the synchronous work they trigger | Remove work, simplify handlers, move CPU-heavy work to a Worker |
| **Presentation delay** | Style, layout and paint after the handler, before the next frame | Reduce DOM scope and layout invalidation |

Working patterns: show visible feedback first, then yield (`scheduler.yield()`, with a `setTimeout` fallback) before the heavy part; move analytics to idle time. Chunk size comes from the trace, not from a fixed item count. Memoise only where a profile shows repeated work. Tie each long task back to the script URL that ran it; third parties often turn out to be the owners. Verify on a representative device / CPU profile by repeating the same interaction.

## CLS: the element that moved is often the victim

`[documented: https://web.dev/articles/optimize-cls, 2026-10-12]`

A shift's score is impact fraction × distance fraction `[documented: https://web.dev/articles/cls, 2026-10-12]`. Use the shifted-node and initiator evidence to find the cause rather than blaming the node that moved.

- Images and media reserve their intrinsic space (`width`/`height` or `aspect-ratio`). For embeds and ads, provide a stable container whose minimum height is **realistic** — a placeholder that collapses shifts the page too.
- Banners, consent UI, validation summaries and notifications never get inserted above visible content without a pre-sized slot; overlays are preferable.
- Font swaps: a metric-matched fallback using `size-adjust`, `ascent-override`, `descent-override` and `line-gap-override`, with values derived from the real font pair.
- Animate `transform` and `opacity`, never `top` or `height`.
- Exercise the real page states and viewports, not just the initial load.

## LCP additions to the subparts table

- Prefer an LCP image **discoverable in the HTML, as an `<img>` carrying `fetchpriority="high"`**; preload (with high fetch priority) when the resource is only referenced from CSS or JavaScript. High priority on more than one or two images makes priority setting unhelpful `[documented: https://web.dev/articles/optimize-lcp, 2026-10-12]`.
- **Speculation Rules (prerender)** speed up the *next* navigation; they do nothing for the current page's LCP. Eagerness levels: `conservative` (pointer or touch down), `moderate` (200 ms pointer hold, or pointerdown), `eager`, `immediate`. Caveats: over-speculation costs users bandwidth, memory and CPU, so scope document rules with `where`; analytics may fire at prerender time unless gated on `document.prerendering` / `prerenderingchange` `[documented: https://developer.chrome.com/docs/web-platform/prerender-pages#eagerness, 2026-10-12]`. Exclude logout, checkout and forms `[practitioner]`. Before widening it, measure the hit rate, the bytes and the server load, and re-read Chrome's eagerness docs before hardcoding any timing.

## Perishable tooling notes

Re-verify before quoting.

- Google plans to discontinue **CrUX real-world data in the PageSpeed Insights API** and recommends the CrUX API or CrUX History API instead; anything built from now on should call the CrUX API itself `[documented: https://developers.google.com/speed/docs/insights/v5/get-started, 2026-10-12]`. Once a date is confirmed, record it in [google-apis-and-quotas.md](google-apis-and-quotas.md) and in skill `seo-engine-policies` › google-updates-timeline.
- The CrUX API requires a Google Cloud API key `[documented: https://developer.chrome.com/docs/crux/api, 2026-10-12]`; an ordinary audit must not be blocked on having one.

## Unverified

- LCP poor threshold: LCP is poor above 4 s [unverified: the 4 s figure appears only in an image alt text of the saved optimize-lcp page, not its text]
- Speculation Rules cost and reach: every prerender costs roughly a full page load, and prerendering works in Chromium only [unverified: not stated on the saved prerender-pages page (2026-10-12)]
- CrUX Vis and History API key: CrUX Vis is the history view, and the CrUX History API also requires a Google Cloud key [unverified: not stated on the saved CrUX API page (2026-10-12); History API page not saved]

## Sources

- addyosmani/web-quality-skills@main skills/core-web-vitals/SKILL.md, addyosmani/web-quality-skills@skills/core-web-vitals/references/INP.md, addyosmani/web-quality-skills@skills/core-web-vitals/references/CLS.md, addyosmani/web-quality-skills@skills/performance/references/MEASUREMENT.md (phase-2 adapted file research/adapted/addyosmani__web-quality-skills/cwv-field-lab-diagnosis.md) — verdict rules, repeatable lab comparison, field/lab reconciliation table, INP phase table, CLS checklist, LCP and Speculation Rules notes, CrUX/PSI tooling note. INTEGRATE, MIT.
- GoogleChrome/lighthouse@README.md (phase-2 adapted file research/adapted/group-E__readme-tool-repos/tool-stack-by-job.md) — median of several runs, simulated throttling by default, SEO category as a hygiene checklist. INTEGRATE, Apache-2.0.
