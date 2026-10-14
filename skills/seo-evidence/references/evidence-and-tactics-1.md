# Evidence and tactics — the SEO Meta Study layer
<!-- split-header: part 1 of 3 of evidence-and-tactics.md (step-3 original lines 1–96; boundary start) -->
<!-- /split-header -->

## Contents

- How to read an evidence mark
- The six-part replication recipe
- The shortlist — 17 tactics worth the next sprint

Other parts of the same original file: [evidence-and-tactics-2.md](evidence-and-tactics-2.md), [evidence-and-tactics-3.md](evidence-and-tactics-3.md).

## How to read an evidence mark

The study puts one of five marks on each of its 182 entries. Each mark carries a shape and a word, never colour alone.

| Mark | What it means | Count in the index |
|---|---|---|
| MAINSTREAM | three or more independent samples, or two if both are controlled tests | 107 |
| EXPERIMENTAL | at most two independent samples; no evidence score is reported, because an agreement figure on one or two observations describes the observations, not a rate. "Read them as hypotheses with a method attached." | 54 |
| IT DEPENDS | controlled tests (or published sources) point opposite ways and the context that decides is named | 6 |
| AVOID | the evidence argues against the tactic | 9 |
| ACADEMIC | peer-reviewed or preprint work measured on benchmark datasets and simulated engines; reported separately because its effect sizes are not interchangeable with a live site's | 6 |

Rules that govern how a mark may be used:

- **Independence is counted by sample.** One published study is one sample. Eight teams that ran the same test contribute eight; the same figure repeated across eight blogs contributes one, because there is one measurement behind it.
- **E and A are two scores, never one.** E is how strong the evidence is; A is how much the tactic is worth doing. A tactic can be well evidenced and not worth your week, and the reverse. Never merge them, never invent a missing one, and never read either as a probability of success. The score colour is a band within this edition (green from 59.6 up, grey from 56.1, brown below), not an absolute grade.
- **The bundle caveat.** 92 of 182 entries (51%) rest on at least one source that changed something else at the same time and measured one outcome. The figure on such an entry belongs to the whole package, so it supports no single tactic: take the direction, not the size.
- **Publication bias.** Of 1,700 published outcomes, 81.9% were positive and 3.8% negative (1,392 improvements, 196 mixed, 65 declines, 46 no effect). In the 90-document hand-verified subset the split was 64% positive, 8% negative. Null and mixed results are underrepresented, not rare, so directional agreement across studies overstates confidence. (The four published categories sum to 1,699 against the stated 1,700; keep that one-document discrepancy visible rather than smoothing it.)
- **The controlled-test gap.** 602 of 769 tactics that passed the evidence gates have no controlled test behind them; 138 rest on exactly one; 23 on two; 6 on three or more (5 on three, 1 on four). The author's phrase: roughly four out of five scored tactics rest on somebody watching a graph move.
- **Single-publisher concentration.** 55% of all controlled measurements (65 of 118) come from one publisher, which is roughly one source in eleven. Most of what the field calls controlled evidence is one testing team's programme. Ask whether a conclusion survives excluding that publisher.
- **Recency is scored, not filtered.** Every tactic carries a recency term that decays with the age of its sources, and the half-life differs by area: a title-tag result from four years ago still means something; an AI-search result from four years ago does not. 523 of 793 sources are dated 2025–2026; 604 are dated 2024 or later.
- **"Mechanism unconfirmed"** is a flag the study prints when the measured change has no established route to the metric. It appears on both llms.txt entries (#68, #71). Google states that Google Search itself doesn't use these files and that they "will neither harm nor help" visibility in Google Search `[documented: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide, 2026-10-11]`; for other engines and model providers we hold no official statement either way. A MAINSTREAM mark with this flag means "measured several times" and nothing about *why*. This is the reconciliation with the llms.txt row of [works-vs-doesnt.md](works-vs-doesnt.md): the two agree on mechanism and differ only on what a repeated measurement is allowed to be called.
- **ACADEMIC = benchmark, not live site.** Most are preprints; peer-review status was not verified per source. Never a forecast for a production site.
- **Effects are grouped by what was measured.** Percentages, percentage points and ranking positions are never averaged together; a percentage on a ranking line means whatever that publisher meant, not positions gained.
- **Typical published gains are what publishers chose to publish.** Organic sessions median +36% (87 entries; 80 gains, 7 declines; a quarter above +110%); conversions median +55.5% (24 entries); AI citations median +67% (15 entries). Of 160 entries reporting a relative percentage change, 70 are above +50%, 36 above +100%, only 9 report declines. Do not budget for them.

### The rule for speaking to a client

Every tactic you name carries, in one sentence: **the mark · the sample count as printed · the design (controlled / before-after) · the bundle flag if any · and the words "a published result, not a forecast for your site".** The shortlist's samples column reads "N of M": N samples measured the headline metric, out of M independent samples behind the entry (entry #1: 6 of 15 samples measured organic sessions; 2 of the 15 were controlled).

Correct: *"Adding author bylines is MAINSTREAM in the study — 7 independent samples, 1 controlled A/B test, and the +113% AI-citations headline rests on 1 of the 7. That is a published result, not a forecast for your site; we would test it on 20 posts against 20 matched controls."*

Incorrect: *"Author bylines lift AI citations by 113% — the meta study proves it."* (Drops the sample count, hides that the headline figure is one sample, presents a published number as a forecast, and uses "proves" of a before-after corpus.)

## The six-part replication recipe

Every entry's "how to replicate it" has six parts, and the study's authors wrote them from the method the source describes — they are not the source's own recommendation. Use it for every rollout, not just weak marks: it turns a published result into a local measurement.

1. **When it applies** — the page type, template or situation the source actually tested. If the site does not match, the entry is a hypothesis, not evidence.
2. **Before you start** — the baseline to record and the matched control group to set aside. No baseline, no reading.
3. **What to change** — the intervention, scoped to a test group, with the bundle called out if the source changed several things together.
4. **What to keep** — everything held identical across test and control during the window. Movement in a "kept" element voids the read.
5. **What to measure** — the metric, the comparison (test vs control), the window. Apply the position and CTR verdict thresholds in [experiments-and-revert-2.md](experiments-and-revert-2.md) (Measurement — GSC before/after, done right) — they are not restated here.
6. **When to revert** — the pre-declared condition under which the change comes out. The study's own sentence: without a rule for when to revert, every outcome reads as confirmation.

Filled in for shortlist #1, entry #1 (Add FAQ content and FAQ schema to category pages), from the study's own recipe:

- *When it applies:* e-commerce or listing sites with category pages that lack direct FAQ content or schema markup.
- *Before you start:* identify brand queries related to category products and map matched pairs of category URLs for split testing.
- *What to change:* on a randomized variant set of category pages, add a question and answer addressing top brand choices at the top of the content area, and matching FAQ JSON-LD in the head; leave a matched set untouched as holdout. The source changed text and schema together, so the combined implementation is what gets tested.
- *What to keep:* category layouts, internal link architecture, product listings and title tags unchanged across both groups.
- *What to measure:* organic sessions, variant vs control, over 28 days, using a causal impact model.
- *When to revert:* keep the FAQ section and schema only if organic sessions rise in the test group relative to the holdout — and note the study's own gap here: the primary source did not report page sample size or timeframe, which limits statistical verification.

`[unvalidated house heuristic]` One addition for a comparison site: the revert rule also fires on any incorrect price, rate or eligibility statement inside the added content, regardless of traffic.

## The shortlist — 17 tactics worth the next sprint

Entry requires E ≥ 60 and a mainstream lane (three or more independent samples, or two if both controlled). Within that, rank weights actionability 0.65 against evidence 0.35, and no more than three entries share a metric family. 61 entries met the entry condition; these 17 ranked highest under the cap. **Order is not evidence strength.** "Samples" is printed as the study prints it (N on the headline metric of M independent).

| Rank | Score (0.65 A + 0.35 E — rank order, not evidence) | # | Tactic | E / A | Samples | Median effect · metric | Bundle | What to change (one line) | Caveat |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 75.9 | 1 | Add FAQ content and FAQ schema to category pages | 93.1 / 66.7 | 6 of 15 | +9% organic sessions | yes | Top-brand Q&A at top of content + matching FAQ JSON-LD on a randomized variant set | The +9% headline is the controlled test; the before-after median across the 6 samples is +112% (range +9% to +350%). FAQ rich results discontinued May 2026 |
| 2 | 75.2 | 56 | Update facts and expand sections on blog posts | 88.1 / 68.2 | 3 of 5 | +55% organic sessions | yes | Replace outdated stats with current figures, add sections on missing subtopics; controls untouched | Two interventions in one measurement |
| 3 | 73.9 | 160 | Rewrite titles, restructure site, and update posts | 91.4 / 64.4 | 5 of 15 | +52% conversions | yes | Rewrite titles + metas, flatten navigation, update posts, disavow toxic links; matched sections as control | Four interventions — direction only |
| 4 | 70.7 | 60 | Add author bylines to blog articles | 86.5 / 62.2 | 1 of 7 | +113% AI citations | no | Visible byline under H1 linking to an author page on 20 posts; 20 matched controls | Headline metric rests on one sample; 1 controlled test among the 7 |
| 5 | 69.9 | 139 | Add schema markup to product and blog pages | 94.6 / 56.5 | 4 of 13 | +40% organic sessions | yes | Product + Article JSON-LD on 100 + 100 pages, plus business-profile updates; matched control | Schema and profile edits bundled |
| 6 | 67.1 | 30 | Add FAQs, tables, and schema to product pages | 77.2 / 61.7 | 1 of 4 | +56% AI citations | yes | Q&A section, direct-topic headlines, features as tables, structured markup | Headline on one sample |
| 7 | 66.1 | 84 | Cross-link pillar pages and supporting articles | 73.4 / 62.2 | 2 of 5 | +94% ranking positions | no | Body anchor links from each cluster article to its pillar | A percentage on a ranking line means what the publisher meant, not positions gained |
| 8 | 65.1 | 19 | Consolidate repetitive pages into detailed hubs | 62.1 / 66.7 | 2 of 6 | +74% conversions | yes | Merge package pages into procedure hubs, rewrite regional pages with distinct local detail, 301 retired URLs | Merge + rewrite + redirects bundled |
| 9 | 65.1 | 109 | Replace keyword repetition with semantic variations | 70.6 / 62.2 | 1 of 3 | +180% AI citations | no | On 30 matched URLs, replace repeated instances of the main keyword | Headline on one sample |
| 10 | 64.9 | 57 | Update blog post content and publication date | 70.0 / 62.2 | 2 of 6 | +57% impressions | yes | Update title, meta, headings, body, internal links and timestamp together | Date change is bundled with real edits — for date-only see #58/#59 (EXPERIMENTAL) |
| 11 | 63.8 | 136 | Add JSON-LD schema markup to blog posts | 63.6 / 63.9 | 1 of 4 | +31.78% ranking positions | no | Article-type JSON-LD in the head; control unchanged | Percentage on a ranking line; one sample |
| 12 | 62.9 | 66 | Add citations to authoritative sources | 65.5 / 61.5 | 1 of 2 | +31.4% impressions | yes | Inline citations with links + summary blocks + revised headings; matched control | Two independent samples; bundle |
| 13 | 60.7 | 32 | Create and optimize product category pages | 70.2 / 55.6 | 2 of 5 | +18% revenue | yes | Rewrite headings, expand copy, publish subcategory pages for unaddressed queries | Bundle |
| 14 | 60.7 | 118 | Sync local directory listings across platforms | 73.0 / 54.1 | 3 of 7 | +38% organic clicks | no | Name, address, phone, hours and URL made identical to official location pages | Requires real venues |
| 15 | 60.0 | 83 | Add brand-icon CTAs with internal links | 65.2 / 57.3 | 2 | +80% conversions | no | CTA block with brand icons linking to brand category pages, below the product description | Two samples, both on conversions |
| 16 | 59.8 | 119 | Update local profile, schema, and review prompts | 77.0 / 50.5 | 3 of 8 | +10 ranking positions | yes | Primary category, menu details, name alignment, LocalBusiness schema, review requests | Five interventions bundled |
| 17 | 59.5 | 141 | Add Product, Review, and FAQ schema to SKU pages | 60.4 / 59.0 | 3 of 6 | +40% click-through rate | yes | Product + AggregateRating + FAQPage JSON-LD on 100 product pages | Partly discontinued: Product and Review markup still produce rich results; the FAQ part does not (Google stopped FAQ rich results May 2026) |

