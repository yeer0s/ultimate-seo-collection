<!-- split-header: part 2 of 8 of practitioner-playbook.md (step-3 original lines 36–140; boundary H2) -->
# Practitioner layer — technical practitioners (1 of 2): arguments by year, verified practices
## Contents

- Technical practitioners — primary corpus layer

Other parts of the same original file: [practitioner-index.md](practitioner-index.md), [practitioner-technical-2.md](practitioner-technical-2.md), [practitioner-agentic.md](practitioner-agentic.md), [practitioner-professional.md](practitioner-professional.md), [practitioner-general.md](practitioner-general.md), [practitioner-secondary-digest-1.md](practitioner-secondary-digest-1.md), [practitioner-secondary-digest-2.md](practitioner-secondary-digest-2.md).

<!-- /split-header -->
## Technical practitioners — primary corpus layer

**The evidence tier.** A collected corpus of public practitioner discussions (anonymised sources): 18,577 threads and 65,180 comments — 100.1% of the comment count the platform itself reports — dated 2018-01-05 to 2026-09-21, collected credential-free, so scores are real and bodies complete. The 732 highest-signal threads were read in depth, chosen by score and comment volume with a recency quota plus an authority set: any thread a Google staffer answered, or any comment scoring ≥20. That produced 1,210 extracted claims. Every cited post and comment id was checked against the corpus: 0 fabricated post ids, 0 fabricated comment ids; cited scores were overwritten with corpus values (8 corrections); a comment cited under the wrong thread was dropped rather than downgraded. Merging left 1,169 distinct practices, which the extraction model labelled 595 `consensus`, 305 `single-voice`, 269 `contested` — claims superseded by the derived counts in the label grammar below. A peer hand-checked 10 random citations (10/10 genuine); this skill's maintainer re-checked 6 more (3 posts, 3 comments) against the corpus database, all 6 matching on score, author, date and comment-parent.

**What that buys.** Attribution, and only attribution. **A high score is evidence of agreement, not of truth** — a score records that readers liked a claim, never that anyone measured it. This layer stays `[practitioner]` and never becomes `[measured]`, however many threads repeat it. Where a practice touches a study entry the bridge is marked, and the study's own caveats govern the number.

**The label grammar — derived, not asserted.** Every label here is **derived from the evidence array** — thread count and summed comment score, computed over the corpus — and the extraction model's own asserted label is **discarded wherever the two disagree**. It over-claimed badly: of the 595 practices it called `consensus`, **538 had not earned it — 46% of all 1,169**; counting both directions, 600 labels changed. `consensus` = **≥2 independent threads by ≥2 distinct authors and ≥10 summed score** (the author rule, added later, changed 0 of the 60 — `practitioner-agentic.md`), and **only 60 of 1,169 practices clear that bar**, so "the practitioners agree" is almost always one thread agreeing with itself. `single-thread (score N)` = one thread, but the supporting comments earned N summed score — **this is not one person's opinion**; it is a room that scored it, inside a single discussion, so it carries weight but no independent replication. `single-voice` = one thread and thin score (<10), the weakest label here, closer to a hypothesis than a practice. `contested` = a named counter-argument exists; it is **never re-derived and never upgraded**, because a counter-argument is a fact about the thread, not a function of score. **A `contested` practice must be carried with its counter-argument attached, never repeated as a recommendation** — the counter-argument is the finding. A separate grounding pass scored all 1,169 practices for whether the cited comment or post body actually supports the practice text as written (median overlap 0.45), flagging 38 for human reading — 33 because the practice headline names a mechanism no cited body contains, 5 for low overlap alone. The calibration that set this rule was run on a *different* extraction of the same corpus — a free-tier model over one chunk, deliberately chosen as the weaker instrument — where hand-reading the three lowest-overlap items found two faithful paraphrases (301-vs-308, and a Blocked Resources answer from a Google staffer, both scoring under 0.10 only because the model wrote in its own vocabulary) and one invention: "include an x-default hreflang tag", citing a real comment that said only that hreflang belongs in the HTML rather than the sitemap, and never mentioned x-default. Real id, right topic, invented mechanism. So **a low score is a reading prompt, never an automatic cut** — on that sample an automatic threshold would have killed two good practices to catch one bad one. **The two failures are different and take different remedies:** a mislabelled practice was faithfully extracted but wrongly summarised, and relabelling fixes it; a ⚠ flagged practice may assert a mechanism its cited sources never named, and only reading the thread fixes that — never delete it on the flag alone.

**Dates are load-bearing.** Google's behaviour changed repeatedly across this window, so each line carries the newest thread supporting it. An old newest-citation means possibly stale — common enough here to check every time.

### What these practitioners argue about, by year

Share of that year's posts mentioning the topic. Shares, not counts — the corpus tripled in volume after 2023, so raw counts rise for everything.

| topic | 2018-21 | 2025-26 | direction |
|---|---|---|---|
| AI search / LLM citation | 0.5% | 11.2% | rising |
| search console | 10.0% | 9.3% | flat |
| schema / structured data | 5.9% | 4.8% | flat |
| sitemaps | 5.5% | 3.7% | falling |
| internal linking | 1.6% | 3.6% | rising |
| robots / noindex | 5.3% | 3.2% | falling |
| indexing problems | 1.8% | 3.1% | rising |
| redirects | 7.5% | 3.0% | falling |
| canonical | 4.8% | 2.6% | falling |
| javascript rendering | 3.2% | 2.4% | flat |
| core web vitals | 1.5% | 1.9% | flat |
| migration | 2.1% | 1.8% | flat |

For audit time: the directive layer (redirects, canonicals, sitemaps, robots) is shrinking as a share of the argument because it is largely solved — budget it as a checklist. The growth is in AI search (22x its 2018-21 share), indexing and internal linking, where the practitioners' answer is consistently that it is a demand and quality problem rather than a technical one. Spend less time proving directives correct, more on whether the pages deserve crawling at all.

### The practices that survived verification

Format: practice · label · weight · newest citation. Weight `N thr / S` = N independent threads, S summed comment score.

**AI search, GEO and LLM citation**
- llms.txt is not an AI-visibility or bot-control lever and is rarely fetched; bot control is robots.txt · `consensus` · 5 thr / 123 · 2026-07-27. **Bridge — contradicts the headline of `[measured: MAINSTREAM #68]` and `[measured: MAINSTREAM #71]` while agreeing with their "mechanism unconfirmed" flag.** #71 spans −19.7% to +81% with no median: unexplained variance, not a reason to ship the file.
- Google's generative AI features still require a crawled, indexed, snippet-eligible page · `consensus` · 2 thr / 236 · 2026-05-25. For retrieval-time answers, rank in the index the model actually searches — Bing named.
- Heavy schema plus green CWV does not put a new site in Google, nor prove an AI ranking · `consensus` · 4 thr / 42 · 2026-05-08.
- Keep rich-result structured data; Google's AI guide adds no special AI schema · `contested` · 2 thr / 179 · 2026-05-25. **Counter:** the OP and a score-8 reply reduce it to schema not mattering at all; a score-2 reply treats entity/schema tuning as how LLMs retrieve.
- Measure AI crawlers from logs and CDN data, not prompt dashboards · `consensus` · 3 thr / 33 · 2026-07-09.
- Front-loaded answers and topical coverage are what these practitioners credit for citation · `consensus` · 2026-05. **Bridge:** direction matches `[measured: EXPERIMENTAL #2]` (+280% AI citations, ≤2 samples). No study entry measures AI citations of orphan pages (#89 measured ranking positions after linking orphan posts).

**Crawling and indexing**
- "Discovered – currently not indexed" on a technically clean URL is a crawl/quality decision, not a defect · `consensus` · **14 thr / 324 — heaviest in the corpus** · 2026-08-27. Sitemaps and internal links cannot create demand; a Google staffer's reply is that the problem is not technical.
- robots.txt Disallow does not noindex: the URL can still be listed, and Google never sees the noindex it cannot fetch · `consensus` · 3 thr / 39 · 2026-03-22. To remove a URL: unblock, noindex, confirm the drop, then disallow.
- 404 and 410 are correct for a gone URL and are not a penalty · `consensus` · 2 thr / 56 · 2020-03-28. The real defect is usually the internal link or sitemap entry pointing at it.
- Do not noindex internally-linked category or structural URLs — it blocks PageRank and eventually crawling · `consensus` · 34 · 2023-06-21. **Bridge:** `[measured: MAINSTREAM #82]`, the reverse direction (removing misplaced noindex, +24% conversions).
- IndexNow does not rank URLs; the 2MB Googlebot cap is uncompressed per-file size · `single-thread (score 34 / 170)` · 34 / 170 · 2026-02-05.
- Googlebot 403 while Screaming Frog gets 200 is a user-agent-specific WAF or nginx block · `single-thread (score 24)` · 24 · 2026-05-29.

**JavaScript rendering**
- JS SEO work is diagnosis plus developer translation, not a ticket saying "Google renders JS" · `consensus` · 3 thr / 26 · 2026-06-23.
- CSR-only React/Vite is indexed as an empty shell; ship SSR or SSG HTML · `consensus` · 2 thr / 31 · 2026-06-05.
- LLM crawlers still fail JS-heavy sites Google already renders · `consensus` · 3 thr / 13 · 2026-03-11. The operative reason to server-render in 2026 — and not a Google reason.
- Never disallow CSS or JavaScript in robots.txt · `single-thread (score 30)` · 30 · 2026-04-01.
- Dynamic rendering is rejected: it doubles the stack and the versions drift — serve one hybrid page · `consensus` · a practitioner · 2020.

**Search Console**
- The URL removal tool hides a URL; it does not deindex it, and it expires · `consensus` · 3 thr / 23 · 2026-05-26.
- The late-2025 GSC impression crash was Google removing `num=100` — rebaseline before calling it a ranking loss · `single-thread (score 42)` · 42 · 2025-10-14.
- Split indexed URLs into click-active, impression-active and inactive; do not use `site:` counts as index size · `single-thread (score 80)` · 80 · 2023-01-29.
- Read index coverage on "All submitted pages", expecting variant URLs to stay out · `contested` · 2 thr / 53 · 2026-05-26. **Counter:** one commenter says ignoring ~15k crawled-not-indexed URLs hides real problems; the other says they are mostly garbage. ⚠ grounding-flagged — verify against the cited thread before acting

**Structured data**
- Rich results require structured data; the blanket claim that schema is useless for SERP features is wrong · `contested` · 2 thr / 70 · 2026-05-06. **Counter:** one member's PSA that schema is unnecessary except as a publishing requirement for flights, ecommerce and jobs — posted at score 0 and rebutted by the higher-scored replies. The one place a single thread is the evidence.
- FAQ rich results were limited to authoritative government and health sites, then removed · `single-thread (score 61)` · 61 · 2025-12-09. **Bridge:** the same discontinuation already flagged on `[measured: MAINSTREAM #1]` and `[measured: MAINSTREAM #135]` — both figures are now historical.
- Structured data does not make a URL rank (Mueller, April 2025); misuse removes rich results, not rankings · `consensus` · 2025-04. JSON-LD retains non-citation uses: rich results, voice, knowledge graph, entity recognition.

**Redirects and migrations**
- Google treats a 308 like a 301; choose 308 only to preserve the HTTP method · `consensus` · 2 thr / 14 · 2026-01-25.
- Do not mass-redirect 404s to the homepage — that is the canonical soft-404 · `single-thread (score 44)` · 44 · 2025-09-08. A host or IP move does not change rankings if the new IP is clean and the config survives.
- Internal 301s do not leak equity, but fix nav and footer templates and break chains · `single-thread (score 24)` · 24 · 2025-05-08. **Bridge:** `[measured: EXPERIMENTAL #100]`, +31% revenue for bypassing internal link redirects and setting canonicals; and `[measured: MAINSTREAM #133]`, +60% organic sessions for a domain-extension migration — keep a sitemap of legacy URLs so the 301s get found.

**Internal linking**
- For crawled-not-indexed URLs, send equity from pages that already have traffic; do not invent links · `consensus` · 2 thr / 51 · 2026-07-15. **Bridge:** `[measured: MAINSTREAM #88]` (+87% organic sessions for reducing click depth) agrees on direction.
- Internal linking and topic structure are where commenters say they actually saw movement · `consensus` · 3 thr / 27 · 2026-06-26. Links must be `<a href>`; an onclick handler is not crawlable.
- More links is not the goal: sitewide widget links into tag and archive templates were the defect, contextual links to category URLs the fix · `consensus` · 2026. Embedding-based linking at a 60% similarity cutoff is `contested`.

**Sitemaps and robots**
- Treat XML sitemaps as an optional discovery and GSC-filtering aid; Google says many small sites can skip them · `consensus` · 2 thr / 47 · 2026-01-15. They still earn their place on large sites, JS-heavy sites and migrations.
- Do not robots.txt-block URLs you need Google to see as noindex or canonicalized · `consensus` · 2 thr · 2026-03-12. Block unintended `.md` and `.atom` URLs, then check whether the crawled-not-indexed count actually falls.

**Canonicalisation**
- Self-reference the preferred URL, and do not reshuffle canonicals during a migration · `consensus` · 2 thr / 15 · 2025-03-05. **Bridge:** `[measured: MAINSTREAM #16]`, +178% organic sessions for canonical tags on duplicate product pages.
- Parameter duplicates: canonical to the clean URL and strip params from internal links — do not robots-block them, which discards any links those URLs earned · `single-thread (score 17)` · 17 · 2026-01-28.
- Pagination: self-canonical when page 2+ must be crawled · `single-thread (score 28)` · 28 · 2019-11-16. A canonical is a hint, not a 301, and Google must crawl the URL to read it — so it saves no crawl budget.

**Core Web Vitals**
- Judge CWV on CrUX field pass/fail, then stop · `consensus` · **11 thr / 160 — second-heaviest in the corpus** · 2026-04-30. **Bridge:** `[measured: MAINSTREAM #132]` bundles a CWV fix *with* revamped content for its +30% organic sessions, so by the study's own bundle caveat it supports no CWV-only claim.
- In 2026 CWV is a floor, not an additive ranking project · `contested` · 4 thr / 56 · 2026-06-28. **Counter:** two score-2 replies say Google has stated CWV signals are used in ranking; a score-7 reply argues load time still moves bounce rate enough to waste SEO gains.
- Fix failing field CWV; do not buy a Lighthouse 92-to-98 bump · `contested` · 3 thr / 69 · 2026-01-30. The threads say Lighthouse omits INP (thread-dated; web.dev: a lab load "without a user cannot measure INP", TBT is the proxy `[documented: https://web.dev/articles/vitals, 2026-10-14]`); the field bar is CrUX at ≥75% of users "good" on LCP, INP and CLS. ⚠ grounding-flagged — verify against the cited thread before acting
- Zero Ahrefs/Screaming Frog errors and PSI 100 do not move rankings · `single-thread (score 63)` · 63 · 2026-06-29.
- Lab weight and TBT cuts are credited for conversion even where rankings did not move · `single-thread (score 56)` · 56 · 2026-07-09. **Bridge:** consistent with `[measured: MAINSTREAM #147]` (+111.8% conversions), itself a bundle — conversion is the honest metric to claim.

**International**
- Use reciprocal hreflang, not `html lang` and not a switcher plugin · `single-thread (score 24)` · 24 · 2026-03-06. Keeping a ccTLD live means canonicals and country targeting, not 301s to the .com.
- hreflang swaps the locale URL into the stronger page's existing slot; it is not a rank boost · `single-thread (score 39)` · 39 · 2019-02-07. Wrong hreflang can drop pages — validate before launch.

**Tooling**
- Screaming Frog at roughly $259/year is the audit crawler these practitioners defend · `single-thread (score 126)` · 126 · 2025-11-18. Botify was quoted at $150,000/year for ~1.06M URLs, Oncrawl at about $1,650/month for the same basket.
- Fix crawl, index and intent issues; ignore perfect audit scores — audit scores and DR thresholds are tool constructs · `consensus` · 2 thr / 40 · 2026-01-15.
- GSC API plus the repo, with a human approving every edit, is the automation shape these practitioners endorse · `single-thread (score 73)` · 73 · 2026-03-30. Crawl with Screaming Frog or Sitebulb, then hand the export to the model.
- Bing Webmaster Tools as a differential: if Bing fetches and Google does not, suspect Google; if neither fetches, suspect your server · `consensus` · 17 thr.

