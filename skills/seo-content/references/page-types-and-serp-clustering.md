# Page types and SERP clustering

## Contents

- The eight page types and their structural signals
- SERP consensus and page-type mismatch
- SERP-overlap clustering
- Hub-and-spoke build specs
- Cluster scorecard and completion gate
- Cross-references
- Sources

## The eight page types and their structural signals

`[practitioner]` — a classification scheme with no measurement behind it. Its value is consistency: the same taxonomy is applied to the target page AND to each of the top 10 SERP results, so "mismatch" is a comparison of like with like rather than an opinion.

| Type | On-page signals that identify it | SERP indicators | Schema expected | Default structure |
|---|---|---|---|---|
| Landing | Hero with one value prop, prominent CTA, pricing section/link, testimonials, reduced nav | Branded queries, high ad density, sitelinks to /pricing or /features | WebSite or SoftwareApplication | Hero → social proof → 3-5 features → how it works → pricing → CTA repeat → FAQ |
| Blog post | Author byline, publish date, body over 800 words, share buttons, `/blog/` breadcrumb, related posts | Paragraph/list featured snippets, PAA with 4+ questions, diverse domains, dates in snippets, low ad density | Article or BlogPosting + author entity + datePublished + dateModified | Title → author+date → intro → H2 sections → images → conclusion → author bio |
| Product | Price displayed, add-to-cart, multiple product images, spec list, star reviews, SKU | Shopping carousel, price/availability/rating rich snippets, merchant names in titles | Product (name, price, availability, review) | Title → images → price+CTA → description → specs → reviews → related |
| Hybrid (service + content) | Educational sections interleaved with CTAs, "learn more" beside "get started", both /blog/ and /product/ in nav | Mixed branded and informational results, mixed Product and SoftwareApplication schema | Product or SoftwareApplication | Problem → solution → how it works → feature deep-dives → proof → CTA → FAQ |
| Service | Methodology/process description, case studies, "how we work", team credentials, consultation CTA | Local pack present, "near me" related searches, agency/firm domains, PAA about process and cost | Service or ProfessionalService | Overview → benefits → process → case studies → team → packages → contact CTA |
| Comparison | "vs"/"versus" in title or URL, feature matrix, pros/cons, side-by-side layout, "best X for Y" framing | "vs" in related searches, PAA about alternatives, review-site domains (G2/Capterra/TrustRadius), listicle titles, affiliate disclosures | ItemList or Table | Intro → criteria → matrix → individual reviews → verdict → FAQ |
| Local | Physical address, map embed, consistent NAP, service-area description, directions | Local pack (map + 3 listings), "near me" related, Business Profile cards, local directories | LocalBusiness (correct subtype) + geo + openingHoursSpecification | Name+location → services here → map → hours → reviews → local content → contact |
| Tool / interactive | Input fields, calculator or generator UI, sliders/dropdowns, results area, utility-first design, "free [tool]" in title | Calculator/generator/checker in related searches, tool-first domains, **minimal PAA** (users want to DO, not READ) | WebApplication or SoftwareApplication | Tool above fold → brief instructions → output → supporting content → FAQ → related tools |

**The minimal-PAA signal on tool SERPs is the most useful single row in that table** `[practitioner]`: a thin PAA block on a commercial-sounding query usually means Google has decided the query wants an instrument, not an essay. Mowei's ferramentas surface competes almost entirely in this cell.

### Classification tiebreak order

When a page shows signals for several types, take the first match `[practitioner]`:

1. Functional interactive tool present → **Tool**
2. Physical address + map → **Local** (unless a tool is primary)
3. Comparison table + "vs" framing → **Comparison**
4. Price + buy button → **Product**
5. CTA-heavy with minimal navigation → **Landing**
6. Service process + case studies → **Service**
7. Educational + CTA mix → **Hybrid**
8. Default → **Blog post**

A fixed order matters more than the order being right: two auditors classifying the same page must land in the same cell, or the mismatch matrix below is noise.

## SERP consensus and page-type mismatch

`[practitioner]`. Classify each of the top 10 organic results, then read the consensus:

- **Strong consensus** — more than 6 of the 10 results share one type.
- **Mixed** — 4 to 6 of 10.
- **Fragmented** — fewer than 4 of 10. Google has not decided; this is a differentiation opportunity, not a template to copy.

Mismatch severities, as inherited `[practitioner]` — the severity words are editorial judgment, not measured impact:

| Target type | SERP expects | Severity | Remedy |
|---|---|---|---|
| Blog post | Product pages | CRITICAL | Build a dedicated product/offer page |
| Blog post | Comparison | HIGH | Restructure around an explicit criteria matrix |
| Product | Informational | HIGH | Add an educational layer above the commercial block |
| Landing | Tool / calculator | HIGH | Build the interactive component |
| Service | Local results | MEDIUM | Add location signals and local schema |
| Blog post | "[service] in [city]" | CRITICAL | Build a real location page |
| Type matches | — | ALIGNED | Compete on depth and UX, not structure |

Record schema types present from **currently supported** SERP features only — exclude FAQ and HowTo, both retired (skill `seo-evidence` › titles-and-serp-tests holds the rich-result register and the retirement dates).

### The SXO gap score is a house heuristic

`[unvalidated house heuristic]` — seven dimensions, six worth 0-15 and Freshness worth 0-10, totalling 0-100 (page type, content depth, UX signals, schema, media richness, authority signals, freshness). **The weights were invented; no study derives them, and a 68 does not mean anything against a 72.** Use the dimension list as a checklist of what to look at, and publish the per-dimension breakdown rather than the composite. (The topic list placed this table at `SKILL.md:51-62`; it is actually at `:122-134` — `:51-62` is the SERP-collection step.)

## SERP-overlap clustering

`[practitioner]`. The principle is sound and cheap to state: **two keywords that return the same results should be served by the same page; two that return different results need different pages.** It substitutes Google's own ranking decisions for your intuitions about text similarity.

Method:

1. For each candidate keyword, retrieve the top 10 **organic** URLs — ignore ads, snippets, PAA and panels.
2. Normalise: strip protocol, trailing slash and non-meaningful query parameters. Store as a set.
3. For each pair, score `overlap = |urls_A ∩ urls_B|`, a count out of 10.
4. Apply the thresholds below.

| Overlap (of 10 URLs) | Relationship | Action |
|---|---|---|
| 7-10 | Same page | Merge; primary keyword = the higher-volume one |
| 4-6 | Same cluster | Same spoke cluster; one or two posts depending on the volume gap |
| 2-3 | Interlink | Adjacent clusters, connected by cross-links |
| 0-1 | Separate | Different clusters, or outside this pillar entirely |

The cut points are `[unvalidated house heuristic]` — nothing establishes 7 rather than 6 as the merge line. Treat them as a consistent convention for one project, not a law, and record which cut point you used so a later audit can re-derive the same clusters.

**Ambiguous 3-4 scores** break in this order: shared domains but different pages (closer), same intent category (lean same cluster), volume ratio above 10:1 (the big one earns its own page), else keep in the same cluster as separate posts.

**Cost control.** N keywords need **N SERP fetches** (one stored set per keyword, step 1) and N(N−1)/2 **local set comparisons** — 40 keywords is 40 fetches and 780 comparisons, and the comparisons are cheap once the sets are cached. Fetches are the cost, and they grow linearly. To cut the pairs a human must review, pre-group on intent and head term, comparing only within groups, then cross-checking the highest-volume keyword of each group against the others. Skip rules: two long-tail variants of the same head term with the same intent can be assumed 4-6 without a fetch; keywords in different intent categories can be assumed 0-2 unless they share a head term. Spot-check a sample of the skipped pairs rather than trusting the assumption blind. Cache every SERP within a session so no keyword is fetched twice.

**Five anti-patterns** `[practitioner]`:

1. Never cluster by text similarity alone — "dog training tips" and "dog training classes" can have disjoint SERPs.
2. Never group by stemming alone — "run" and "running" can be different intents.
3. Never assume related searches belong in the same cluster; verify with SERP data.
4. Never ignore SERP-feature differences — a local-pack keyword and a featured-snippet keyword need different page types even at moderate URL overlap.
5. Never treat all domains equally — Wikipedia and Reddit appear everywhere and inflate every overlap score. Filter the most ubiquitous domains before scoring, or weight the rest higher.

Anti-pattern 5 is the one that silently ruins a run: with Wikipedia, Reddit and one dominant publisher in every set, a floor of 3 shared URLs appears between unrelated keywords, and the 2-3 "interlink" band fills with junk.

## Hub-and-spoke build specs

`[practitioner]`. `content-and-intent.md#topical-authority--build-clusters-not-random-posts` owns the pillar/cluster concept and a worked Portuguese energy example; what follows is the build contract only.

- **Pillar** — broadest keyword; comprehensive overview covering every cluster subtopic; a table of contents; links to **every** spoke; Article + BreadcrumbList + ItemList; refresh quarterly or when spokes are added.
- **Spoke** — one unique primary keyword; deeper than the pillar's treatment of the same subtopic; links to the pillar (mandatory) plus 2-3 siblings; Article + BreadcrumbList.
- **Shape** — 2-5 clusters per pillar, 2-4 posts per cluster, 5-21 posts including the pillar.
- Word-count figures in the source (2,500-4,000 pillar, 1,200-1,800 spoke) are **production estimates for costing, never ranking targets** — the same framing `content-and-intent.md` applies to its brief template. Do not repeat them to a client as thresholds.

Template by intent: informational-broad → ultimate guide; informational-how → how-to; informational-list → listicle; informational-concept → explainer; commercial-compare → comparison; commercial-evaluate → review; commercial-rank → best-of; transactional → landing page. Where several fit, match the format the top results actually use, and avoid two identical templates inside one cluster.

Link rules, in tiers: spoke → pillar and pillar → spoke are **mandatory** (a cluster missing either is structurally broken); 2-3 contextual spoke-to-spoke links inside a cluster are recommended, placed in body paragraphs rather than a "related posts" strip; 0-1 cross-cluster links, only where a genuine topical bridge exists. Floors: every post has at least 3 inbound internal links, no page sits more than 2 clicks from the pillar, and no single anchor text accounts for more than 40% of the inbound internal links to a given page.

**Cannibalisation prevention** — no two posts share a primary keyword, full stop; overlap of 7+ means merge; after clustering, list every primary keyword and hunt near-duplicates ("best CRM" vs "top CRM software"), then either merge or differentiate by intent. `content-and-intent-2.md#cannibalization` covers diagnosing it after the fact; this is the build-time guard.

## Cluster scorecard and completion gate

`[practitioner]`. Each metric carries its own denominator, which is why this scorecard survives contact with a real build where the SXO composite does not:

| Metric | Formula | Target |
|---|---|---|
| Coverage | written posts ÷ planned posts | all planned posts written |
| Link density | total internal links ÷ total posts | ≥ 3.0 per post |
| Orphan pages | count of posts with 0 inbound internal links | 0 |
| Pillar connectivity | spokes linking to the pillar ÷ total spokes | all |
| Reverse pillar links | spokes linked from the pillar ÷ total spokes | all |
| Cross-links | implemented ÷ recommended | ≥ 4 in 5 |
| Cannibalisation | count of posts sharing a primary keyword | 0 |
| Content gaps | planned posts not yet written | 0 |

Gate before calling a cluster done: both mandatory link directions present, no post under 3 inbound links, no shared primary keywords, no orphans. A failing gate is reported with remediation — **never silently passed**, which is the same discipline skill `seo-evidence` › experiments-and-revert-2 applies to verdict states.

## Cross-references

- `content-and-intent.md#page-types-and-their-jobs` — page type → business role and conversion goal. Not restated here.
- `content-and-intent.md#intent-diagnostic-from-serp` — query shape → intent → page type. This file is the inverse direction.
- `content-and-intent-2.md#cannibalization` — post-hoc diagnosis; above is the build-time guard.
- skill `seo-evidence` › titles-and-serp-tests — which rich results still exist, and the retirement dates behind "exclude FAQ/HowTo".
- `programmatic-seo.md` — scaling page types by template, and the gates on doing so.
- `./briefs-and-personas.md` — the per-page-type brief variants that turn a classification into a writing spec.

## Sources

- claude-seo@skills/seo-sxo/references/page-type-taxonomy.md:1-188 — the 8-type taxonomy, signals, SERP indicators, structures and tiebreak order. Carried as `[practitioner]`.
- claude-seo@skills/seo-sxo/SKILL.md:36-96 — SERP consensus bands and the mismatch severity matrix. Carried as `[practitioner]`.
- claude-seo@skills/seo-sxo/SKILL.md:122-134 — the 7-dimension 0-100 gap score. Carried as `[unvalidated house heuristic]`; topic-list line reference `:51-62` was wrong and is corrected above.
- claude-seo@skills/seo-cluster/references/serp-overlap-methodology.md:1-108 — clustering method, thresholds (`[unvalidated house heuristic]`), tiebreaks, cost control, 5 anti-patterns.
- claude-seo@skills/seo-cluster/references/hub-spoke-architecture.md:1-181 — pillar/spoke specs, cluster constraints, template-by-intent, link tiers, cannibalisation rules. Carried as `[practitioner]`; word counts reframed as production estimates.
- claude-seo@skills/seo-cluster/references/execution-workflow.md:125-180 — scorecard formulas and the completion gate. Carried as `[practitioner]`.
