# Tactics by job — which tactic for which job, with its label and owner

## Contents

- How to read
- Get crawled and indexed
- Diagnose a traffic drop
- Content: write, refresh, scale
- Titles, snippets and structured data
- AI search: access, citation, measurement
- Authority and links
- Measure, test and ship
- Banned shortcuts
- Sources

## How to read

An index, not a source: every row points at the file that owns the tactic, and the label is copied from that file (no new claims here). The verdict uses the fixed vocabulary; where the owner gives several labels, the row shows the one behind the tactic. Engine rules are never restated: the owner file carries the engine-page pointer. No row is a forecast; a tactic is planned only after its policy gate passes ([strategy-playbooks.md](strategy-playbooks.md)).

## Get crawled and indexed

| Job | Tactic | Label | Verdict | Owner |
|---|---|---|---|---|
| A new site is invisible | Verify GSC and Bing Webmaster Tools on day 1, submit sitemaps, IndexNow pings for add / update / delete | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] | supported by engine docs | [strategy-playbooks.md](strategy-playbooks.md) § New domain |
| Pages are not indexed | Read the page indexing report by reason and template; "Discovered – currently not indexed" read as a quality decision first | [practitioner: anonymised sources · consensus · 14 thr / 324 · newest 2026-08-27] | practitioner agreement, untested | skill `seo-technical` › crawl-and-index |
| Keep a URL out of the index | `noindex`, not robots.txt Disallow (Disallow blocks crawling, not indexing) | [practitioner: anonymised sources · consensus · 3 thr / 39 · newest 2026-03-22] | practitioner agreement, untested | skill `seo-technical` › crawl-and-index |
| Sitemaps get ignored | Sitemaps as a discovery hint with real `lastmod`; no ranking expected | [documented: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap, 2026-10-11] | supported by engine docs | skill `seo-technical` › rendering-and-sitemaps-2 (Sitemap.xml) |
| Faster pickup on Bing and IndexNow engines | IndexNow on publish; it requests a crawl, each engine still decides | [documented: https://www.indexnow.org/faq, 2026-10-11] | supported by engine docs | skill `seo-technical` › rendering-and-sitemaps-2 § IndexNow |
| Links are not followed or crawled | Internal links as `<a href>` elements | [documented: https://developers.google.com/search/docs/crawling-indexing/links-crawlable, 2026-10-11] | supported by engine docs | skill `seo-technical` › crawl-and-index |
| Duplicate URLs split signals | Canonicals on duplicates, remove misplaced `noindex`, in a migration 301 each old URL to its equivalent and decide explicitly for URLs without one (nearest parent, 410 or keep) | [measured: MAINSTREAM, n=?, c=?] (#16, #82, #133) | measured, direction only | skill `seo-technical` › migrations-and-recovery |
| Bots see a different page from users | Bot parity pass: fetch as a browser and as each allowed crawler, compare status and body hash | [practitioner] | practitioner agreement, untested | skill `seo-technical` › site-inspection-method |

## Diagnose a traffic drop

| Job | Tactic | Label | Verdict | Owner |
|---|---|---|---|---|
| "Was it a penalty?" | Classify before treating: manual action → update → site-reputation → deploy/render → indexing → demand → security → AI-Overview CTR loss | [practitioner] | practitioner agreement, untested | skill `seo-technical` › incident-triage |
| Did an update cause it? | Look up the rollout window on the Search Status Dashboard; for a core update, wait a full week after it completes, then compare that week with a week before the rollout started | Dashboard: [documented: https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history, 2026-10-11]; comparison window: [documented: https://developers.google.com/search/docs/appearance/core-updates, 2026-10-14] | supported by engine docs | skill `seo-engine-policies` › google-updates-timeline |
| Clicks fall while rank holds | AI-Overview CTR-loss triage (query filter, dated SERP check), run after deploy, indexing and manual-action checks | [practitioner] | practitioner agreement, untested | skill `seo-technical` › incident-triage |
| A page decays slowly | Decay triage: same-length GSC page exports, validate before calling it "dropped", attribute in order | [practitioner] | practitioner agreement, untested | skill `seo-content` › content-and-intent-2 |
| Rank decay alerts | Fall bands (20 / 40 / 60 %) only to order pages for review | [unvalidated house heuristic] | no evidence either way | skill `seo-content` › content-and-intent-2 |
| A manual action for links | Remove what you can first; disavow only with «a considerable number of spammy, artificial, or low-quality links» that caused or «likely will cause a manual action» [documented: https://support.google.com/webmasters/answer/2648487, 2026-10-11]; reconsideration per the engine's doc | [measured: IT DEPENDS, n=3, c=0] (#13) | depends on an actual or likely manual link action | skill `seo-authority` › authority-links-and-pr |

## Content: write, refresh, scale

| Job | Tactic | Label | Verdict | Owner |
|---|---|---|---|---|
| Pick what to write first | One narrow cluster, one owner page per query intent, long tail before head terms | [practitioner: anonymised sources · consensus · 2 thr / 39 · newest 2022] | practitioner agreement, untested | skill `seo-content` › keyword-research-1 |
| Old posts lose clicks | Refresh facts and sections, not just the date | [measured: MAINSTREAM, n=5, c=?] (#56, bundle) | measured, direction only | skill `seo-content` › content-and-intent-2 |
| Thin or overlapping pages | Consolidate into hubs and 301 the rest | [measured: MAINSTREAM, n=6, c=?] (#19, bundle) | measured, direction only | skill `seo-technical` › migrations-and-recovery |
| Programmatic pages at scale | Grade the data source first (data defensibility tiers 1–5); a tier-5-only set is a doorway candidate | [practitioner] | practitioner agreement, untested | skill `seo-content` › programmatic-seo |
| Template pages look alike | ≥3 differentiators beyond the swapped variable | [practitioner: anonymised sources · consensus · 6 thr / 50 · newest 2026-06-14] | practitioner agreement, untested | skill `seo-content` › programmatic-seo |
| A hosted or partner section | Section-level risk check per first path segment, advisory only | [hypothesis] | no evidence either way | skill `seo-content` › programmatic-seo-2 |
| AI drafts | A human reviews every AI draft; never fully automated publishing | [practitioner: anonymised sources · consensus · 4 thr / 24 · newest 2026-05-23] | depends on human review and added value | skill `seo-content` › publishing-gates |
| A draft scores well but may be wrong | P0–P3 editorial severity as a filter beside any score; claim verification before publish | [practitioner] | practitioner agreement, untested | skill `seo-content` › publishing-gates |
| Comparison pages | Original value per page: live data, date, method, exclusions; fair competitor framing | [practitioner: anonymised sources · consensus · 6 thr / 50 · newest 2026-06-14] | practitioner agreement, untested | skill `seo-content` › comparison-pages |
| Several locales | One locale per URL, hreflang with return links, localise rather than machine-translate | [practitioner: anonymised sources · consensus · 8 thr / 47 · newest 2026-05] | practitioner agreement, untested | skill `seo-technical` › international-and-hreflang |
| Local pages | One page per real location; NAP identical everywhere | [measured: MAINSTREAM, n=7, c=?] (#118) | measured, direction only | skill `seo-content` › local-and-maps-seo |

## Titles, snippets and structured data

| Job | Tactic | Label | Verdict | Owner |
|---|---|---|---|---|
| Titles at scale | Swap test: a title or description that could move unchanged to a sibling page carries nothing page-specific | [practitioner] | practitioner agreement, untested | skill `seo-evidence` › metadata-at-scale |
| Price in titles | A dynamic lowest price only with a staleness guard; static price strings are AVOID (#157, #158) | [measured: MAINSTREAM, n=3, c=2] (#155, one publisher) | measured, size transfers nowhere | skill `seo-evidence` › titles-and-serp-tests |
| Low CTR at a good position | Rewrite title and meta where CTR trails position; test, then keep or revert | [practitioner: anonymised sources · consensus · 2 thr / 18 · newest 2026-06-17] | practitioner agreement, untested | skill `seo-evidence` › metadata-at-scale |
| Rich results | Structured data only for what is visible and eligible | [documented: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide, 2026-10-11] | supported by engine docs | skill `seo-technical` › schema-reference |
| Retired rich results | No FAQ rich result in Google Search from 2026-05-07; HowTo docs removed as «no longer shown in search results» | [documented: https://developers.google.com/search/updates, 2026-10-11] | supported by engine docs | skill `seo-technical` › schema-reference |
| JSON-LD that lies | Schema honesty check at build: wordCount, dateModified and ratings match the page; escape `<>&'` | [hypothesis] | no evidence either way | [ideas-register.md](ideas-register.md) |

## AI search: access, citation, measurement

| Job | Tactic | Label | Verdict | Owner |
|---|---|---|---|---|
| Be cited in ChatGPT search | Allow OAI-SearchBot; block GPTBot (training) separately if wanted; test the edge as each bot | [documented: https://developers.openai.com/api/docs/bots, 2026-10-11] | supported by engine docs | skill `seo-ai-search` › ai-crawlers-and-bot-policy |
| Be cited in Claude | Allow Claude-SearchBot; block ClaudeBot (training) separately if wanted; test the edge as each bot | [documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11] | supported by engine docs | skill `seo-ai-search` › ai-crawlers-and-bot-policy |
| Be cited in Perplexity | Allow PerplexityBot (search; «not used to crawl content for AI foundation models»); test the edge as the bot | [documented: https://docs.perplexity.ai/guides/bots, 2026-10-11] | supported by engine docs | skill `seo-ai-search` › ai-crawlers-and-bot-policy |
| Stop AI scraping without losing AI search | Training-only blocks; never paste a full block list (it catches retrieval bots) | [practitioner] | practitioner agreement, untested | skill `seo-ai-search` › ai-crawler-registry |
| Appear in AI Overviews | An indexed, snippet-eligible page; no special AI markup | [documented: https://developers.google.com/search/docs/appearance/ai-features, 2026-10-11] | supported by engine docs | skill `seo-ai-search` › ai-retrieval-and-citation |
| Google's AI inclusion setting | Confirm GSC "Search generative AI" reads include before any GEO work | [documented: https://support.google.com/webmasters/answer/16908024?hl=en, 2026-10-11] | supported by engine docs | skill `seo-engine-policies` › google-ai |
| Agents must use the site | Agent-readiness fix order: P0 accessibility, CLS, content without JavaScript, deliberate robots groups, WAF passing verified bots | [practitioner] | practitioner agreement, untested | skill `seo-ai-search` › agent-readiness |
| Measure AI visibility | Four-rung ladder (retrieved, cited, mentioned, recommended), never one number; log the framing of each mention | [practitioner] | practitioner agreement, untested | skill `seo-ai-search` › ai-citation-measurement |
| Count AI crawler visits | Server and CDN logs per verified token, not prompt dashboards | [practitioner: anonymised sources · consensus · 3 thr / 33 · newest 2026-07-09] | contested | skill `seo-ai-search` › ai-citation-measurement |
| A citable data asset | Data page per vertical: dated findings, HTML table, CSV, Dataset JSON-LD | [measured: MAINSTREAM, n=8, c=0] (#15, bundle) | measured, direction only | skill `seo-ai-search` › data-assets-and-charts |
| llms.txt | A no-claim file at most; Google Search does not use it | [documented: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide, 2026-10-11] | contested | skill `seo-ai-search` › geo-audit-and-citability |

## Authority and links

| Job | Tactic | Label | Verdict | Owner |
|---|---|---|---|---|
| Earn links with no history | One linkable asset (dataset, calculator, study) pitched to the few writers who cover the topic | [measured: MAINSTREAM, n=8, c=0] (#15, bundle) | measured, direction only | skill `seo-authority` › authority-links-and-pr |
| Press and trade coverage | Trade publications, not post farms | [practitioner: anonymised sources · consensus · 2 thr / 18 · newest 2025-04] | practitioner agreement, untested | skill `seo-authority` › authority-links-and-pr |
| Spread equity to new pages | Contextual internal links from the strongest pages | [measured: MAINSTREAM, n=3, c=1] (#90) | measured, direction only | skill `seo-evidence` › works-vs-doesnt |
| YMYL trust: bylines | Author bylines linking to a profile page | [measured: MAINSTREAM, n=7, c=1] (#60) | measured, direction only | skill `seo-authority` › authority-trust-and-distribution |
| YMYL trust: reviewers, method | Named reviewers; methodology page with a published "what we don't do" block (not tested by #60) | [unvalidated house heuristic] | no evidence either way | [strategy-playbooks.md](strategy-playbooks.md) § YMYL |

## Measure, test and ship

| Job | Tactic | Label | Verdict | Owner |
|---|---|---|---|---|
| Prove a change helped | Pre-declared baseline, window, holdout and revert trigger; four verdict states | [unvalidated house heuristic] | no evidence either way | skill `seo-evidence` › experiments-and-revert-2 |
| Core Web Vitals verdicts | Field data at p75; no CrUX record = unavailable, not passing; lab: ≥3 runs, median and range | [practitioner] | practitioner agreement, untested | skill `seo-technical` › cwv-field-lab-diagnosis |
| CWV as a ranking project | Pass on CrUX, then stop | [practitioner: anonymised sources · consensus · 11 thr / 160 · newest 2026-04-30] | contested | skill `seo-technical` › cwv-field-lab-diagnosis |
| Deploys break SEO | CI gates: robots/sitemap diff, redirect errors, Content-Type, fail on build-time `lastmod` for unchanged URLs, edge vs deployed robots | [practitioner: anonymised sources · consensus · 13 thr / 481 · newest 2026-01] | practitioner agreement, untested | skill `seo-technical` › seo-drift-monitoring |
| Trust a connector or API | Same 28 days via the connector and the GSC export: row count, top queries, positions | [unvalidated house heuristic] | no evidence either way | skill `seo-optimizer` › measurement-gates-and-checklists |
| Know if our advice helped | Log every recommendation with baseline and window, `not_shipped` too | [hypothesis] | no evidence either way | [ideas-register.md](ideas-register.md) |

## Banned shortcuts

PBNs, link swaps, scaled AI pages, parasite sections, cloaking, prompt injection, fake review stars, CTR bots and the rest are listed with their engine cites and the policy condition each meets in [ideas-register.md](ideas-register.md) § Tempting, and banned; refusals stricter than the policy are marked there as house rules. They have no row here.

## Sources

- Owner files named in each row (all in this tree, read 2026-10-11/12); labels copied from them, or from the step-11 layers that copy them: skill `seo-evidence` › works-vs-doesnt, [strategy-playbooks.md](strategy-playbooks.md), [ideas-register.md](ideas-register.md).
- PLAN §3 (Tactics row: job → tactic → label → owning file; no new claims).
- Official pages read raw 2026-10-11 (phase-2 source index): https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a · https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap · https://www.indexnow.org/faq · https://developers.google.com/search/docs/crawling-indexing/links-crawlable · https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history · https://developers.google.com/search/docs/fundamentals/ai-optimization-guide · https://developers.openai.com/api/docs/bots · https://developers.google.com/search/docs/appearance/ai-features · https://support.google.com/webmasters/answer/16908024?hl=en
- https://developers.google.com/search/docs/appearance/core-updates — saved 2026-10-12 (sources/google/s12-037), re-read 2026-10-14: the core-update comparison window.
