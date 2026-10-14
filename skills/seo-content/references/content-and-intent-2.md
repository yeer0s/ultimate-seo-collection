<!-- split-header-2: part 2 of 2 of content-and-intent.md (original lines 305–407; boundary H2) -->
# Content and intent (2 of 2) — refresh and decay triage, new content, cannibalisation
## Contents

- Content refresh workflow
- New content workflow
- What to deprioritize (vanity SEO)
- Cannibalization
- Sources

Other parts of the same original file: [content-and-intent.md](content-and-intent.md).

<!-- /split-header-2 -->
## Content refresh workflow

For pages with declining clicks (use Search Console):

### Step 0 — detect, validate and classify the decay

Do this before step 1; it decides whether the page needs a refresh at all.

**Detect.** Pull two Search Console **page** exports covering the same length of time — back-to-back periods for a short-term read, or the matching period one year earlier when seasonality may be at play (look back as far as 16 months before diagnosing). Hold property, search type, device, country and filters identical on both sides. Clicks are the default metric; before acting, also read impressions, CTR, position, the query×page pairs and search-appearance deltas.

| Fall versus the comparison period | Band |
|---|---|
| 20–39.9 % | warning |
| 40–59.9 % | high |
| ≥ 60 % | critical |

The bands are an `[unvalidated house heuristic]` and only order pages for review. Whether a later change worked is judged by skill `seo-evidence` › experiments-and-revert-2 (four verdict states, click floors, no `neutral`).

**Validate before saying "dropped".** If a page appeared in the earlier export and is missing from the current one, its state is `needs_validation` — not `dropped_out` — until four things are confirmed: the filters match, the row limit was high enough to include it, the dimensions match, and URL Inspection has been run `[practitioner]`. A truncated export is the usual cause of a false "drop".

**Attribute, in this order:**

1. **Is it a data anomaly?** Read Google's "Data anomalies in Search Console" page first. A logging defect is not a ranking change, and an anomaly that began before an update cannot show that the update caused the fall. Example: a logging error cut impressions in the Generative AI performance report in Search for 13–17 Aug 2026; the missing data was restored on 21 Aug `[documented: https://support.google.com/webmasters/answer/6211453, 2026-10-12]`. Check whether a restoration note exists before reading such a dip. Our standing window also applies: GSC impressions, CTR and position unreliable 2025-05-13 → 2026-04-27 (skill `seo-engine-policies` › google-updates-timeline).
2. **Is it a named update?** Take its start and end from the Search Status Dashboard; **let at least one full week pass after completion**; compare one week after the update with one week before rollout; read Web, Images, Video and News separately. Dates alone do not tell you what an update "rewarded", and smaller core updates are not announced [documented: https://developers.google.com/search/docs/appearance/core-updates, 2026-10-12]. Do not respond with mass deletion.
3. **Did we change something?** After a fix Google might hold pages in a duplicate cluster for **up to two weeks** `[documented: https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting, 2026-10-12]`: mark it `PENDING_REEVALUATION` and do not fix it again `[practitioner]`.
4. Only then look at indexation, canonicals, internal links, backlinks, seasonality and business value.

**Pick the action:**

| Action | Choose it when |
|---|---|
| Refresh / update | demand is still there; the page needs freshness, sections, a better title or internal links → continue with step 1 below |
| Investigate query shift | clicks fell but impressions held → look at CTR, rank, SERP features or query mix |
| Consolidate / 301 | the page fell out, or the loss is severe and a stronger sibling covers the intent (this is a URL change — skill `seo-technical` › migrations-and-recovery) |
| Prune | prior demand was very low, the page has no business value, and a rewrite is not justified |

Mowei note `[practitioner]`: on regulated figures, any change from ERSE, the IRS tables or IAS (a regulatory event) forces a refresh regardless of what traffic does. Decay triage is only the second trigger, not the first.

**Review markup at refresh time.** Before adding or keeping `Review` / `AggregateRating`, confirm: the reviews rest on genuine experience; any incentive is disclosed clearly and prominently; the review content is readily available on the marked-up page; reviews and ratings are not aggregated from other websites `[documented: https://developers.google.com/search/docs/appearance/structured-data/review-snippet, 2026-10-12]`. A markup that parses proves nothing about authenticity — when you cannot verify, mark it unverified and emit no rating `[practitioner]`.

### Steps 1–12 — refresh

1. Confirm the decline — is it ranking drop or CTR drop?
2. Re-analyze SERP intent — has Google's preferred format changed?
3. Compare to current top 3-5 ranking pages — what do they have that you don't?
4. Add missing sections / data / examples / tools.
5. Update prices, laws, regulations, screenshots — anything dated.
6. Improve title + meta for CTR (test with Google's PAA / featured snippet patterns).
7. Add internal links from newer pages.
8. Add or update schema.
9. Strengthen trust — author bio, sources, methodology.
10. Republish with visible update date.
11. Request re-indexing if appropriate.
12. Monitor 2-8 weeks — Google takes time to recrawl + reweight.

## New content workflow

1. Choose topic from keyword universe (commercially relevant + realistic ranking path).
2. Confirm business relevance — does it lead to revenue eventually?
3. Analyze SERP — what format does Google reward?
4. Classify intent.
5. Choose page type.
6. Create content brief.
7. Draft content with unique insight/data.
8. Add internal links + external citations.
9. Add schema.
10. Optimize title / meta / H1.
11. Add CTA matched to funnel stage.
12. QA for originality, usefulness, factual accuracy.
13. Publish.
14. Update sitemap; ping IndexNow (**Bing + participating engines — Google does not consume IndexNow**, so this is not a Google indexing step; for Google, the sitemap update and internal links are the signal).
15. Monitor performance.
16. Refresh based on data.

## What to deprioritize (vanity SEO)

Skip keywords with:
- High volume but low commercial relevance ("what is electricity")
- No realistic ranking path (Wikipedia-dominated SERPs)
- Wrong geography for your business
- Wrong user intent for your funnel
- No conversion path
- Regulatory or legal risk

Volume isn't the goal — *qualified visits that convert* is the goal.

## Cannibalization

Two of your URLs on one query is not harm by itself (sitelinks, brand queries, a compare page and a how-to page serving different intents, owned top-5 slots). `[hypothesis]` Same-intent pages can split signals when Google alternates between them. Detect candidates by:
- Same query ranks two of your URLs in different weeks
- **GSC method (the Queries tab does not list URLs — this is the step people get wrong):** Performance → filter to the one query → switch to the **Pages** tab. That shows every URL that served it. Two or more URLs with meaningful impressions on the same query is the signal. At scale, use the BigQuery cannibalization query in [keyword-research.md](keyword-research-1.md#gsc-analysis-sql-templates-bigquery) rather than clicking query by query
- Both pages are mid-ranked (positions 8-30) and neither breaks through

Before any fix, run the class check in [gsc-page2-audit.md § 3](gsc-page2-audit.md#3-cannibalization--verify-class-before-prescribing). Act only where the intent is the same **and** Google alternates between the URLs over time with neither holding a stable slot. If both sit in the top 5 within ~2 positions, monitor; do not consolidate. Then fix by:
- Merging into one canonical page
- Differentiating intent (split into different angles)
- 301 the weaker → stronger

## Sources

- AgriciDaniel/claude-blog@skills/blog-decay/SKILL.md, AgriciDaniel/claude-blog@skills/blog-google/references/search-currentness.md:34-75,131-144 (v2.2.0) (phase-2 adapted file research/adapted/AgriciDaniel__claude-blog/content-decay-triage.md) — Content refresh step 0: decay bands, the needs_validation rule, attribution order, action table, PENDING_REEVALUATION, review-markup check. INTEGRATE, MIT.
- AgriciDaniel/claude-blog@skills/blog/references/editorial-heuristics.md (phase-2 adapted file research/adapted/AgriciDaniel__claude-blog/editorial-review-gate.md) — the one-line P0 filter note beside the content score (full gate and attribution in publishing-gates.md). COPY source, written here in our own words; MIT.
