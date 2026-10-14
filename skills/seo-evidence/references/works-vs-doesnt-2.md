<!-- split-header-2: part 2 of 2 of works-vs-doesnt.md (original lines 86–122; boundary H2) -->
# What works and what doesn't (2 of 2) — field errors from popular SEO skills, unverified, sources
## Contents

- Field errors
- Unverified
- Sources

Other parts of the same original file: [works-vs-doesnt.md](works-vs-doesnt.md).

<!-- /split-header-2 -->
## Field errors

REPORT §6: errors repeated across the most-starred SEO skills (the repos are named there), kept as a red-team set. Each row negates the error; none is advice.

| Field error | Correction | Verdict |
|---|---|---|
| FAQPage and HowTo shown as rich-result wins (retired) | FAQ retired 7 May 2026 for all sites; HowTo retired September 2023: skill `seo-technical` › schema-reference | evidence argues against (AVOID) |
| SearchAction and ClaimReview shown as wins (retired) | Sitelinks search box removed 2024-11-21; ClaimReview 2025-06-12: skill `seo-technical` › schema-reference | evidence argues against (AVOID) |
| Keyword density, LSI keywords and word-count targets — folklore | Stuffing is spam: skill `seo-engine-policies` › google §5 row 4; no ideal page length (joined table, word count); #67 AVOID | evidence argues against (AVOID) |
| Made-up 0–100 scores sold as measurements | At most `[unvalidated house heuristic]`; "No third-party tool has access to our internal ranking or AI systems" [documented: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide, 2026-10-11] | no evidence either way |
| "Google-Extended controls AI Overviews" — folklore | Google-Extended governs Gemini/Vertex use, not Search inclusion: skill `seo-engine-policies` › google-ai §8 row 17 | evidence argues against (AVOID) |
| "Allow ClaudeBot / anthropic-ai for AI search" | Search tokens are Claude-SearchBot and OAI-SearchBot; anthropic-ai is not a listed token: skill `seo-engine-policies` › anthropic §8 row 17; skill `seo-engine-policies` › openai §8 row 17 | evidence argues against (AVOID) |
| "Claude uses Brave Search" | Anthropic's article names three robots and no Brave: skill `seo-engine-policies` › anthropic §8 row 17 | no evidence either way |
| "IndexNow reaches DuckDuckGo" | DuckDuckGo is not on the IndexNow endpoint list [documented: https://www.indexnow.org/faq, 2026-10-11] | evidence argues against (AVOID) |
| One GEO paper, three sets of numbers (KDD-2024) | A simulated-engine benchmark (ACADEMIC); #74 is benchmark-measured, never a live-site lift | measured, size transfers nowhere |
| Parasite SEO as a strategy | skill `seo-engine-policies` › google §5 row 12 | policy-forbidden (any evidence is moot) |
| Synonym cycling to evade duplicate filters; 100,000-title AI libraries; a page for every low-difficulty keyword — when made mainly to rank, with little to no value per page | skill `seo-engine-policies` › google §5 row 6 | policy-forbidden (any evidence is moot) |
| ~300 directory submissions; reciprocal link-exchange deliverables | skill `seo-engine-policies` › google §5 row 5 | policy-forbidden (any evidence is moot) |
| Undisclosed Reddit posting from personal accounts | Link spam when posts carry links: skill `seo-engine-policies` › google §5 row 5; legal angle (UCPD): see ## Unverified | policy-forbidden (any evidence is moot) |
| FID as the responsiveness metric (retired) | INP replaced it in 2024: skill `seo-technical` › rendering-and-sitemaps | evidence argues against (AVOID) |
| rel=next/prev as an indexing signal (retired); paginated pages canonicalised to page 1 | Each page self-canonicals: skill `seo-technical` › crawl-and-index | evidence argues against (AVOID) |
| changefreq/priority; Mobile-Friendly Test (retired Dec 2023) | "Google ignores <priority> and <changefreq> values" [documented: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap, 2026-10-11] | evidence argues against (AVOID) |
| Lighthouse score as a ranking penalty; `site:` as an index check | A 100 does not rank a page: [practitioner: anonymised sources · consensus · 6 thr / 378 · newest 2025-09]; URL Inspection is the index check: skill `seo-technical` › incident-triage | evidence argues against (AVOID) |
| ai.robots.txt block lists used blindly | They block Applebot, Bravebot, OAI-SearchBot, Claude-SearchBot, PerplexityBot, DuckAssistBot, meta-webindexer and match "Spider", "Code", "Cursor" (collateral 403s): skill `seo-ai-search` › ai-crawler-registry | evidence argues against (AVOID) |

## Unverified

- UCPD Annex I conflict [unverified: REPORT §6 says undisclosed posting conflicts with EU UCPD Annex I; the Annex text was not among the saved sources]

## Sources

- Ledger parts named under How to read. n, c not printed there were copied from: skill `seo-authority` › authority-trust-and-distribution (#68 n=4 c=0, #71 n=3 c=0); [experiments-and-revert-1](experiments-and-revert-1.md) (#88 n=3 c=0); the step-3 router, old SKILL.md line 114 (#90 n=3 c=1).
- Practitioner parts technical-1, technical-2, general, professional, agentic, secondary-digest-1; corpus PLAYBOOK-technical (word-count thread) and PLAYBOOK-professional (social-signals myth).
- Engine pages: skill `seo-engine-policies` › google, google-ai, anthropic, openai.
- Official pages, read raw 2026-10-11 (phase-2 source index): https://developers.google.com/search/docs/fundamentals/ai-optimization-guide · https://developers.google.com/search/docs/appearance/ai-features · https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap · https://developers.google.com/search/docs/crawling-indexing/links-crawlable · https://support.google.com/webmasters/answer/2648487 · https://www.indexnow.org/faq
- research/REPORT.md §6 (field errors and the repos that repeat them); PLAN §3, §6.2, §6.3; the step-3 router's "What does not move rankings" table.
