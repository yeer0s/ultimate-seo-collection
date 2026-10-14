<!-- split-header-2: part 2 of 2 of resources-catalogue.md (original lines 112–169; boundary H2) -->
# Resources catalogue (2 of 2) — tools by job, not recommended, datasets, communities
## Contents

- Tools by job
- Not recommended
- Datasets
- Communities
- Unverified
- Sources

Other parts of the same original file: [resources-catalogue.md](resources-catalogue.md).

<!-- /split-header-2 -->
## Tools by job

Each row starts from the job to be done. A tool earns its place for the method it encodes and keeps its trap beside it; the name on its own recommends nothing. When a tool's README disagrees with Google documentation, the row stays and the disagreement is written into it. Before suggesting any tool, say the job, the method and the trap.

| Job | Tool | Licence | What it is good for | Caveat |
|---|---|---|---|---|
| Decide whether bot Y may fetch URL X | `google/robotstxt` | Apache-2.0 | Google's production robots.txt parser and matcher (RFC 9309). The binary exits 0 for ALLOWED and 1 for DISALLOWED `[documented: https://raw.githubusercontent.com/google/robotstxt/master/README.md, 2026-10-12]`; reach for it whenever a file mixes `Allow` overrides and wildcards `[practitioner]` | You must hand it a URI already in RFC 3986 format; the library does not fully normalise it. It does **not** apply crawler fallbacks: with no group of its own, `Googlebot-Image` follows the `Googlebot` group, and the binary will not model that `[documented: https://raw.githubusercontent.com/google/robotstxt/master/README.md, 2026-10-12]`. Used in skill `seo-ai-search` › ai-crawlers-and-bot-policy |
| Spot robots.txt or sitemap changes between deploys; read bot hits from logs | `eliasdabbas/advertools` (`robotstxt_to_df`, `sitemap_to_df` for a robots.txt, an index or a sitemap; `crawl` + `crawlytics`; `logs_to_df`) | MIT | Take a snapshot of robots.txt and every sitemap at each deploy and diff the two; turn server logs into bot hits per path and status code `[practitioner]` | User-agent strings can be spoofed `[documented: https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers, 2026-10-11]`, so log work needs bot verification by reverse DNS or Web Bot Auth; Google publishes reverse-DNS masks for its fetchers and is experimenting with Web Bot Auth `[documented: https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers, 2026-10-11]`. Used in skill `seo-technical` › seo-drift-monitoring (deploy gates) |
| Bot gate at the edge (risk row) | `TecharoHQ/anubis` | MIT | Puts a proof-of-work JavaScript challenge in front of the origin. Its own README calls this "a bit of a nuclear response" that "may inhibit 'good bots'" unless they are allowlisted (README:98) | Most AI crawlers do not execute JavaScript, so a challenged bot reads nothing, and the challenge page answers 200. Wherever Anubis or any PoW/JS gate sits in front of the site, prove access by fetching as each bot; allowlist only verified Googlebot and Bingbot plus the AI bots you want citing you. Used in skill `seo-ai-search` › ai-crawlers-and-bot-policy |
| Broken links, redirects and fragments in CI | `JustinBeckwith/linkinator` | MIT | `--recurse --check-fragments --redirects error --require-https error` breaks the build on any internal redirect, which turns the migration rule "no internal redirects" into a gate. `--retry` respects a 429 `retry-after` | Fragment checks only see server-rendered HTML (README:121). Used in skill `seo-technical` › migrations-and-recovery and skill `seo-technical` › seo-drift-monitoring (deploy gates) |
| Lab performance and SEO hygiene for one URL | `GoogleChrome/lighthouse` (`--only-categories=performance,seo`) | Apache-2.0 | Run it several times and judge the median, not one run `[documented: https://raw.githubusercontent.com/GoogleChrome/lighthouse/main/docs/variability.md, 2026-10-12]`; throttling is simulated by default `[documented: https://raw.githubusercontent.com/GoogleChrome/lighthouse/main/docs/throttling.md, 2026-10-12]` | The SEO category is a hygiene checklist and says nothing about ranking. Lab numbers are not field Core Web Vitals. Used in skill `seo-technical` › cwv-field-lab-diagnosis; pre-publish checklist in skill `seo-optimizer` › audit-output-and-templates |
| Performance regression gate per PR | `GoogleChrome/lighthouse-ci` (`lhci autorun`) | Apache-2.0 | Assertions on any Lighthouse audit or category plus a budgets file, for each PR, with several runs per URL (`numberOfRuns`, default 3) `[documented: https://raw.githubusercontent.com/GoogleChrome/lighthouse-ci/main/docs/configuration.md, 2026-10-12]` | Assert on the metrics, never on the 0–100 score: its weights move between Lighthouse versions. Used in skill `seo-technical` › seo-drift-monitoring (deploy gates) |
| Lighthouse over a whole site | `harlan-zw/unlighthouse` | MIT | Scans an entire site with Lighthouse, using what its README calls "smart sampling" `[documented: https://raw.githubusercontent.com/harlan-zw/unlighthouse/main/README.md, 2026-10-12]` | Lab data only. Read results template by template, never as one site-wide average. Used in skill `seo-technical` › site-inspection-method |
| Author JSON-LD in TypeScript | `google/schema-dts`; vocabulary from `schemaorg/schemaorg` (monthly releases, with a "pending" area) | Apache-2.0 (both) | Type-checks JSON-LD at build time; `@graph` ties Organization, WebSite and page entities together. **Escape at least `<` as `\u003c` before injecting into `<script type="application/ld+json">`**: `JSON.stringify` does not sanitise strings used in XSS `[documented: https://nextjs.org/docs/app/guides/json-ld, 2026-10-12]`; escaping `>`, `&` and `'` too (`\u003e`, `\u0026`, `\u0027`) is the stricter house rule `[practitioner]`. | Passing the type check does not make a page eligible for a Google rich result: the types still include `FAQPage` and `HowTo`, which have none. Check eligibility in skill `seo-technical` › schema-reference |
| Next.js metadata and JSON-LD components | `garmeeh/next-seo` | MIT | Ready-made components for types that are live: Product, MerchantReturnPolicy, MemberProgram (loyalty), DiscussionForumPosting, ProfilePage, VacationRental, Event, JobPosting | Four stale README claims: `HowToJsonLd` "can help … appear as rich results" (README:670), but HowTo was retired Sept 2023; `FAQJsonLd` says government/health only (README:2573), but FAQ rich results are gone for every site since 7 May 2026; `ClaimReviewJsonLd` (README:228) was retired 12 June 2025; the course-list carousel (README:2281, 2412) was retired 12 June 2025, while the single Course card remains live. Used in skill `seo-technical` › schema-reference |
| Crawl the site for SEO elements, raw and rendered | `PhialsBasement/LibreCrawl` (Playwright JS rendering, PSI hook); `advertools.crawl` (Scrapy) as the raw pass | MIT | Crawl once without rendering and once rendered, then diff title, canonical, robots meta and links; anything present only in the rendered DOM is invisible to crawlers that do not execute JavaScript `[practitioner]` | Do not swap in `python-seo-analyzer` (LEARN only, no text taken): it counts words and adds an LLM "expertise" pass on a retired model (`claude-3-sonnet-20240229`, README:200), so its scores are `[unvalidated house heuristic]`. Used in skill `seo-technical` › rendering-and-sitemaps-2 (Raw vs rendered crawl diff) |
| Next.js sitemap and robots | `iamvishnusankar/next-sitemap` | MIT | Lists only the index sitemap in robots.txt (`includeNonIndexSitemaps: false`); server-side sitemaps for dynamic URLs | Default `changefreq: daily` and `priority: 0.7` are ignored by Google `[documented: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap, 2026-10-11]`. **`autoLastmod: true` writes the build time onto every URL** (README:116, 159), teaching Google that your `lastmod` carries no signal: turn it off and pass real content dates through `transform`. `exclude` noindexed routes. On the App Router, the native `sitemap.ts` / `robots.ts` remove the dependency. Used in skill `seo-technical` › rendering-and-sitemaps-2 (`autoLastmod` trap) and skill `seo-technical` › seo-drift-monitoring (build-time `lastmod` flag) |
| Nuxt technical SEO | `harlan-zw/nuxt-seo` | MIT | One config for robots, `X-Robots-Tag`, sitemap and link checker. Its skew protection keeps old asset chunks alive during a deploy, so a crawler fetching mid-deploy avoids chunk 404s `[hypothesis]` | Its README:27 calls JSON-LD "the single biggest lever for rich results, AI Overviews" — wrong: Google says structured data is not required for AI features `[documented: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide, 2026-10-11]`. Catalogue row only (framework-specific) |
| Keyword, backlink and SERP data for an agent | `every-app/open-seo` | MIT | Lets an agent read real data through an MCP with your own DataForSEO key, so it does not make up search volumes | The hosted plan puts a 28 % surcharge on every DataForSEO request (README:61) `[vendor]`. Catalogue row only |

## Not recommended

| Tool | Licence | Why it is not recommended |
|---|---|---|
| `towfiqi/serpbear` (rank tracking) | MIT | It gets ranks by scraping Google through third-party SERP APIs or proxies, which breaks Google's terms, and this skill's hard refusals include ToS-breaking automation. Its own README marks 3 of the 10 listed providers "Doesn't work Anymore" (README:59-61). A scraped rank is one location at one moment, not the GSC average position. **Rule: GSC is the truth for your own rankings.** |

## Datasets

| Dataset | Use, as far as this tree supports | Label | Detail |
|---|---|---|---|
| Google Search Status Dashboard | Incidents per product (Crawling, Indexing, Ranking, Serving) with date and duration; Ranking history lists core and spam updates. Rule an update in or out before blaming a deploy | [documented: https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history, 2026-10-11] | skill `seo-engine-policies` › google-updates-timeline-2 |
| CrUX | Field Core Web Vitals: judge pass/fail there, not on lab scores | [practitioner: anonymised sources · consensus · 11 thr / 160 · newest 2026-04-30] | skill `seo-technical` › google-apis-and-quotas |
| Common Crawl | «open repository of web crawl data»; CCBot obeys robots.txt, verifiable by reverse DNS | [documented: https://commoncrawl.org/ccbot, 2026-10-11] | skill `seo-engine-policies` › other-ai-crawlers |
| ai.robots.txt releases (MIT) | AI-crawler token registry (181 rows): leads to verify per vendor. Re-run the edge gate each release; never import its block list | [practitioner] | skill `seo-ai-search` › ai-crawler-registry |
| HTTP Archive | nothing supportable here — see Unverified | — | — |

## Communities

Complete collections of each community's public discussions (anonymised sources), every cited id checked: quotes and scores are sound, the advice not thereby correct. Cite a practice with its own label from the part file.

| Community | Corpus (threads read) | Label | Part |
|---|---|---|---|
| Technical practitioners | 18,577 posts, 65,180 comments, 2018-01-05 to 2026-09-21 (732) | [practitioner] | skill `seo-evidence` › practitioner-technical-1 |
| Professional practitioners | 34,623 posts, 222,690 comments, 2013-04-26 to 2026-09-22 (989) | [practitioner] | skill `seo-evidence` › practitioner-professional |
| General practitioners | 448,424 posts, 1,346,395 comments, 2008-04-22 to 2026-10-01 (3,930) | [practitioner] | skill `seo-evidence` › practitioner-general |
| Agentic-SEO practitioners | 3,703 posts, 21,071 comments, 2025-08-15 to 2026-09-22 (500) | [practitioner] | skill `seo-evidence` › practitioner-agentic |

The secondary digest (third-party write-ups, scores unseen) is leads only: skill `seo-evidence` › practitioner-index.

## Unverified

- HTTP Archive: one second-hand llms.txt figure in skill `seo-evidence` › practitioner-secondary-digest-1 [unverified: no HTTP Archive source read].

## Sources

- google/robotstxt, eliasdabbas/advertools, TecharoHQ/anubis, JustinBeckwith/linkinator, GoogleChrome/lighthouse, GoogleChrome/lighthouse-ci, harlan-zw/unlighthouse, google/schema-dts, schemaorg/schemaorg, garmeeh/next-seo, PhialsBasement/LibreCrawl, iamvishnusankar/next-sitemap, harlan-zw/nuxt-seo, every-app/open-seo, towfiqi/serpbear @README.md, plus facts only from sethblack/python-seo-analyzer @README.md (LEARN, no text) (phase-2 adapted file research/adapted/group-E__readme-tool-repos/tool-stack-by-job.md) — one row per tool: method, limit, README claims that contradict Google documentation; JSON-LD escape sequences restored as `\u003c` etc.; serpbear moved to "Not recommended". INTEGRATE, Apache-2.0 (robotstxt, lighthouse, lighthouse-ci, schema-dts, schemaorg) / MIT (all others).
- phase-2 sources/INDEX.md matched to engine-page Sources lists; saved status-dashboard and CCBot texts; practitioner part files (corpus sizes).
