# Strategy playbooks by site stage and type

## Contents

- How to use these playbooks
- New domain
- Comparison or marketplace
- Local
- Publisher
- SaaS
- YMYL
- Multi-locale and EEA
- Which engines to prioritise per market
- Sources

## How to use these playbooks

- Every step names its improvement lane (L1 eligibility · L2 demand and intent · L3 usefulness and trust · L4 on-page and SERP packaging · L5 page experience · L6 authority and distribution · L7 measurement). Work the lanes in order: a later-lane step waits while an earlier lane's gate fails (skill `seo-optimizer` › audit-output-and-templates § Improvement lanes). The gate order is in the same file (skill `seo-optimizer` › audit-output-and-templates § Gate order).
- Every step carries one evidence label and one policy gate. The gate is an engine-page pointer; the step is planned only if it passes.
- No playbook forecasts traffic. Forecasts come only from the client's own GSC demand and funnel.
- Every rollout needs a pre-declared baseline, window and revert trigger (skill `seo-evidence` › experiments-and-revert-2 § Revert triggers).

## New domain

No links, no history; a 6-month plan.

| # | Lane | When | Step | Label | Policy gate |
|---|---|---|---|---|---|
| 1 | L1 | Day 1 | Verify Google Search Console and Bing Webmaster Tools; submit the sitemap in both; switch on IndexNow pings for add, update and delete (Bing documents IndexNow; Google does not) | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] | skill `seo-engine-policies` › bing §4; skill `seo-engine-policies` › google §4 |
| 2 | L1 | Day 1 | Check that GSC "Search generative AI" reads include (REPORT §7 idea 2) | [documented: https://support.google.com/webmasters/answer/16908024?hl=en, 2026-10-11] | skill `seo-engine-policies` › google-ai §8 row 18 |
| 3 | L1 | Week 1 | Crawl, render and index check on every template; robots.txt allows Googlebot, Bingbot and the AI search bots you want | [practitioner: anonymised sources · consensus · 2 thr / 237 · newest 2026-07-19] | skill `seo-engine-policies` › google §8 row 17; skill `seo-engine-policies` › openai §8 row 18 |
| 4 | L2 | Month 1 | Pick one narrow topic cluster (10–20 queries, one owner page each) where big sites are thin; long tail before head terms (skill `seo-content` › keyword-research-1) | [practitioner: anonymised sources · consensus · 2 thr / 39 · newest 2022] | skill `seo-engine-policies` › google §5 row 2 (one page per distinct intent) |
| 5 | L3 | Months 1–2 | Write the cluster with first-hand data; a human reviews every AI draft | [practitioner: anonymised sources · consensus · 4 thr / 24 · newest 2026-05-23] | skill `seo-engine-policies` › google-ai §5 row 6; skill `seo-engine-policies` › bing §5 row 6 |
| 6 | L4 | Month 2 | Titles, H1, answer-first intro; schema only for what is visible | [measured: EXPERIMENTAL, n=1, c=1] (#2) | skill `seo-engine-policies` › google §5 row 4; skill `seo-engine-policies` › google §5 row 15 |
| 7 | L6 | Months 2–3 | One linkable asset (dataset, calculator or study), pitched to the few writers who cover the topic (skill `seo-authority` › authority-links-and-pr) | [measured: MAINSTREAM, n=8, c=0] (#15, bundle) | skill `seo-engine-policies` › google §5 row 5; skill `seo-engine-policies` › bing §5 row 5 |
| 8 | L6 | Month 3 | Internal links from the asset and the strongest pages into the cluster | [practitioner: anonymised sources · consensus · 5 thr / 21 · newest 2026-08] | skill `seo-engine-policies` › google §5 row 3 (no hidden links) |
| 9 | L7 | Every change | Measurement window: baseline, 28 days per side with matched weekdays, revert trigger declared before shipping | [unvalidated house heuristic] | skill `seo-engine-policies` › google §5 row 1 (test variants show bots and users the same page) |
| 10 | L2 | Months 4–6 | Open cluster 2 only when cluster 1 pages are indexed and earn impressions | [practitioner: anonymised sources · consensus · 14 thr / 324 · newest 2026-08-27] | skill `seo-engine-policies` › google §5 row 6 |
| 11 | L7 | Monthly | Report GSC and Bing baselines and test verdicts only; no traffic forecast | [practitioner: anonymised sources · consensus · 6 thr / 107 · newest 2024-08] | skill `seo-engine-policies` › google §6 (engines may demote or drop a site, so no forecast holds) |

## Comparison or marketplace

| # | Lane | Step | Label | Policy gate |
|---|---|---|---|---|
| 1 | L1 | Filter and sort URLs: one canonical per offer set; trim near-duplicate templated pages | [practitioner: anonymised sources · consensus · 11 thr / 152 · newest 2026-08] | skill `seo-engine-policies` › bing §5 row 2 |
| 2 | L2 | One page per comparison intent (provider vs provider, plan type, region) | [practitioner: anonymised sources · consensus · 6 thr / 18 · newest 2026-07-29] | skill `seo-engine-policies` › google §5 row 2 |
| 3 | L3 | Each page adds original value: live data, date, method, what is excluded; ≥3 differentiators beyond the swapped variable (skill `seo-content` › comparison-pages) | [practitioner: anonymised sources · consensus · 6 thr / 50 · newest 2026-06-14] | skill `seo-engine-policies` › google §5 row 14; skill `seo-engine-policies` › bing §5 row 14 |
| 4 | L3 | Publish the method page with a "what we deliberately don't do" block, audited quarterly against the live site (REPORT §7 idea 16) | [unvalidated house heuristic] | skill `seo-engine-policies` › google §5 row 15 (claims about reviews and ratings must match markup) |
| 5 | L4 | Title tests: dynamic lowest price only with a staleness guard; static price tokens are AVOID (#157, #158) | [measured: MAINSTREAM, n=3, c=2] (#155, one publisher) | skill `seo-engine-policies` › google §5 row 4 |
| 6 | L6 | Data page per vertical as the link asset (REPORT §7 idea 9) | [measured: MAINSTREAM, n=8, c=0] (#15, bundle) | skill `seo-engine-policies` › google §5 row 5 |
| 7 | L7 | Revert also on any wrong price or rate in changed content, whatever the traffic | [unvalidated house heuristic] | skill `seo-engine-policies` › google §5 row 15 (offer markup must match the visible price) |

## Local

| # | Lane | Step | Label | Policy gate |
|---|---|---|---|---|
| 1 | L1 | One page per real location; name, address and phone identical on page, LocalBusiness JSON-LD, business profile and directories (skill `seo-content` › local-and-maps-seo) | [measured: MAINSTREAM, n=7, c=not printed] (#118) | skill `seo-engine-policies` › google §5 row 15 |
| 2 | L2 | City or service-area pages only where a real place or service exists | [hypothesis] | skill `seo-engine-policies` › google §5 row 2 |
| 3 | L3 | Distinct local detail per page; merge repetitive regional pages | [measured: MAINSTREAM, n=6, c=not printed] (#19, bundle) | skill `seo-engine-policies` › google §5 row 6 |
| 4 | L6 | Ask every real customer for a review; never buy or self-write | [measured: MAINSTREAM, n=8, c=not printed] (#119, bundle) | skill `seo-engine-policies` › google §5 row 15; skill `seo-engine-policies` › yandex §5 row 15 |
| 5 | L7 | Measure calls, directions and local-pack presence apart from organic clicks | [hypothesis] | skill `seo-engine-policies` › google §5 row 1 |

## Publisher

| # | Lane | Step | Label | Policy gate |
|---|---|---|---|---|
| 1 | L4 | Visible article title as the H1; true publish and update dates | [measured: EXPERIMENTAL, n=1, c=1] (#76) | skill `seo-engine-policies` › google §5 row 15 |
| 2 | L3 | Refresh facts on decaying posts before writing new ones; date-only bumps are not a refresh | [measured: MAINSTREAM, n=5, c=not printed] (#56, bundle) | skill `seo-engine-policies` › google §5 row 15 |
| 3 | L3 | Bylines linking to real author pages | [measured: MAINSTREAM, n=7, c=1] (#60) | skill `seo-engine-policies` › google §5 row 15 |
| 4 | L3 | Inline citations to sources | [measured: EXPERIMENTAL, n=1, c=0] (#62) | skill `seo-engine-policies` › google §5 row 5 |
| 5 | L6 | Guest work only in real trade publications; never host third-party sections for their ranking | [practitioner: anonymised sources · consensus · 2 thr / 18 · newest 2025-04] | skill `seo-engine-policies` › google §5 row 5; skill `seo-engine-policies` › google §5 row 12 |
| 6 | L7 | Split any decline by intent before diagnosing; AI Overviews cut informational clicks | [practitioner: anonymised sources · consensus · 11 thr / 363 · newest 2025-06] | skill `seo-engine-policies` › google-ai §8 row 18 |

## SaaS

| # | Lane | Step | Label | Policy gate |
|---|---|---|---|---|
| 1 | L1 | Server-render docs and marketing pages so AI crawlers can read them | [practitioner: anonymised sources · consensus · 3 thr / 13 · newest 2026-03-11] | skill `seo-engine-policies` › google §5 row 1 |
| 2 | L2 | One page per job or feature intent; integration and alternatives pages only with real content | [practitioner: anonymised sources · consensus · 6 thr / 18 · newest 2026-07-29] | skill `seo-engine-policies` › google §5 row 2 |
| 3 | L3 | Merge repetitive feature pages into hubs; 301 the rest | [measured: MAINSTREAM, n=6, c=not printed] (#19, bundle) | skill `seo-engine-policies` › bing §5 row 2 |
| 4 | L3 | Fair, dated competitor comparisons; no review markup about yourself | [unvalidated house heuristic] | skill `seo-engine-policies` › google §5 row 15 |
| 5 | L4 | Answer-first docs and help pages | [measured: EXPERIMENTAL, n=1, c=1] (#2) | skill `seo-engine-policies` › google §5 row 4 |
| 6 | L6 | Original usage-data study as the link asset | [measured: MAINSTREAM, n=8, c=0] (#15, bundle) | skill `seo-engine-policies` › google §5 row 5 |

## YMYL

Money, health, legal and safety topics.

| # | Lane | Step | Label | Policy gate |
|---|---|---|---|---|
| 1 | L3 | Every number sourced to a primary document and dated; legal gate before a precise credit, insurance or investment figure (REPORT §7 idea 11) | [unvalidated house heuristic] | skill `seo-engine-policies` › google §5 row 15 |
| 2 | L3 | Byline linking to an author page (#60 measured bylines only, not qualifications or reviewers) | [measured: MAINSTREAM, n=7, c=1] (#60) | skill `seo-engine-policies` › google §5 row 15 |
| 3 | L3 | Named, qualified authors and reviewers; methodology page with a published "what we deliberately don't do" block, audited against the live site (REPORT §7 idea 16) | [unvalidated house heuristic] | skill `seo-engine-policies` › google §5 row 15; skill `seo-engine-policies` › yandex §5 row 15 |
| 4 | L3 | One definition per statutory term across guides (REPORT §7 idea 10); human review of AI text (skill `seo-content` › publishing-gates) | [unvalidated house heuristic] | skill `seo-engine-policies` › google-ai §5 row 6 |
| 5 | L4 | No superlatives or guarantees in titles and descriptions; the claims owner decides (the claims-review process) | [hypothesis] | skill `seo-engine-policies` › google §5 row 4 |
| 6 | L7 | Revert on any wrong figure, whatever the traffic | [unvalidated house heuristic] | skill `seo-engine-policies` › google §5 row 15 |

## Multi-locale and EEA

| # | Lane | Step | Label | Policy gate |
|---|---|---|---|---|
| 1 | L1 | One locale per URL; hreflang with return links; one GSC property per country domain (skill `seo-technical` › international-and-hreflang) | [practitioner: anonymised sources · consensus · 8 thr / 47 · newest 2026-05] | skill `seo-engine-policies` › bing §5 row 2 |
| 2 | L2 | Query research per market; never assume the same intent across languages | [practitioner: anonymised sources · consensus · 6 thr / 18 · newest 2026-07-29] | skill `seo-engine-policies` › google §5 row 2 |
| 3 | L3 | Localise, do not machine-translate: market vocabulary (pt-PT, not pt-BR), local prices, local law | [measured: EXPERIMENTAL, n=not printed (≤2 by mark), c=not printed] (#101) | skill `seo-engine-policies` › yandex §5 row 6; skill `seo-engine-policies` › naver §5 row 6 |
| 4 | L1 | Register each market's own console and submission channel (next section), e.g. Naver Search Advisor with IndexNow for Korean | [documented: https://searchadvisor.naver.com/guide/indexnow-about, 2026-10-11] | skill `seo-engine-policies` › naver §4; skill `seo-engine-policies` › seznam §4 |
| 5 | L7 | Measure per locale (per property or country filter), each with its own window | [unvalidated house heuristic] | skill `seo-engine-policies` › google §5 row 1 |

## Which engines to prioritise per market

EU and Portugal first. Market relevance is copied from each engine page's front-matter line (all last_verified 2026-10-11); no market-share figure is given because no dated source for one was read. Full grid: skill `seo-engine-policies` › engine-matrix.

| Engine page | Market relevance (front-matter) | Console | Crawler to allow | IndexNow | Pointer |
|---|---|---|---|---|---|
| google | global | Search Console | Googlebot | not documented | skill `seo-engine-policies` › google §4; skill `seo-engine-policies` › google §8 row 17 |
| google-ai | global | GSC Search generative AI setting = include | Googlebot (Google-Extended is a training token, not Search) | not documented | skill `seo-engine-policies` › google-ai §8 row 17; skill `seo-engine-policies` › google-ai §8 row 18 |
| bing | global; index also feeds Copilot | Bing Webmaster Tools | Bingbot | documented | skill `seo-engine-policies` › bing §4; skill `seo-engine-policies` › bing §8 row 17 |
| microsoft-copilot | global; grounded in the Bing index | BWT AI Performance | Bingbot; avoid NOCACHE/NOARCHIVE on pages meant for Copilot | via Bing | skill `seo-engine-policies` › microsoft-copilot §4; skill `seo-engine-policies` › microsoft-copilot §8 row 18 |
| bing-syndication (DuckDuckGo, Ecosia, Yahoo, Qwant) | privacy-minded searchers in PT/EU; Ecosia EUSP in FR | none (Qwant: sitemap) | DuckDuckBot, DuckAssistBot, Qwantbot; rest follows Bing | not documented; never claim IndexNow reaches DuckDuckGo | skill `seo-engine-policies` › bing-syndication §4; skill `seo-engine-policies` › bing-syndication §8 row 17 |
| openai | global (ChatGPT search, training) | none | OAI-SearchBot (GPTBot is training, separate) | not documented | skill `seo-engine-policies` › openai §8 row 18 |
| perplexity | global | none | PerplexityBot (Perplexity-User generally ignores robots.txt) | not documented | skill `seo-engine-policies` › perplexity §8 row 18 |
| anthropic | global | none | Claude-SearchBot, Claude-User (ClaudeBot is training) | not documented | skill `seo-engine-policies` › anthropic §8 row 17 |
| other-ai-crawlers (Apple and others) | global AI features and datasets | none | Applebot (falls back to Googlebot rules) | not documented | skill `seo-engine-policies` › other-ai-crawlers §8 row 17 |
| brave | low for PT; default in Brave browser for some users | none (re-fetch form) | no own token: follows Googlebot access | not documented | skill `seo-engine-policies` › brave §4; skill `seo-engine-policies` › brave §8 row 17 |
| seznam | Czech Republic | Add Page form or API | SeznamBot | not documented | skill `seo-engine-policies` › seznam §4; skill `seo-engine-policies` › seznam §8 row 17 |
| yandex | not stated in docs; marginal for PT | Yandex Webmaster | Yandex robots | not captured on the page; do not claim | skill `seo-engine-policies` › yandex §4; skill `seo-engine-policies` › yandex §8 row 17 |
| naver | South Korea | Search Advisor ownership check | Yeti | documented | skill `seo-engine-policies` › naver §4; skill `seo-engine-policies` › naver §8 row 17 |
| baidu | mainland China | 搜索资源平台 | Baiduspider | not documented | skill `seo-engine-policies` › baidu §4; skill `seo-engine-policies` › baidu §8 row 17 |

For a Portuguese site: Google, Google AI features and Bing (with Copilot and the Bing-fed engines behind it) carry the work; allow the AI search bots you want cited; Seznam, Yandex, Naver and Baidu matter only when you target their markets.

This table answers "which engines, and what does each need" on its own (with the engine matrix); open an engine page only to quote one engine's rule text.

## Sources

- research/REPORT.md §7 (ideas 2, 9, 10, 11, 16), checked 2026-10-11; PLAN §3 (playbook list) and §3.1.
- Lanes and gate order: skill `seo-optimizer` › audit-output-and-templates.
- Ledger counts: skill `seo-evidence` › evidence-and-tactics-1 (#56, #60, #118, #119, #19 sample counts); skill `seo-evidence` › titles-and-serp-tests (#2, #76, #155); skill `seo-authority` › authority-links-and-pr (#15); skill `seo-authority` › authority-trust-and-distribution (#62); skill `seo-evidence` › evidence-and-tactics-2 (#101 mark).
- Practitioner counts: skill `seo-evidence` › practitioner-professional; skill `seo-evidence` › practitioner-technical-1; skill `seo-evidence` › practitioner-agentic; skill `seo-evidence` › practitioner-general.
- Engine pages: skill `seo-engine-policies` (14 pages, last_verified 2026-10-11).
- https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a — Bing Webmaster Guidelines, fetched 2026-10-11.
- https://support.google.com/webmasters/answer/16908024?hl=en — GSC generative AI control, fetched 2026-10-11.
- https://searchadvisor.naver.com/guide/indexnow-about — Naver IndexNow, fetched 2026-10-11.
