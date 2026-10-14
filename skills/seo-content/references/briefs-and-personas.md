# Briefs and personas
<!-- split-header-2: part 1 of 2 of briefs-and-personas.md (original lines 1–130; boundary start) -->
<!-- /split-header-2 -->

## Contents

- Two modes, decided before anything else
- The two rules that keep a brief deliverable
- Information gain is the non-negotiable field
- Research before the brief
- Per-page-type brief variants
- Sources

Other parts of the same original file: [briefs-and-personas-2.md](briefs-and-personas-2.md).

## Two modes, decided before anything else

`[practitioner]`

- **Improve mode** (an existing URL). Fetch the page first. Name what is already strong and mark it *keep*; name what is thin, missing or outdated and mark it *add*. The outline must distinguish keep/strengthen from add-new. **Do not recommend a full rewrite when targeted additions will win** — a rewrite discards accumulated links, rankings and any editorial quality the page already has, and it is the default output of a brief writer who did not read the page.
- **New-page mode** (a keyword, no page). Use the site's homepage and sitemap for business context only, and build from the competitive gaps a new page can fill.

Confusing the two is the most common brief defect: an improve-mode request answered with a new-page brief reads as a demand to discard a working asset.

## The two rules that keep a brief deliverable

`[practitioner]` — both are anti-hallucination discipline, and they are the highest-value import in this file.

**Website Relevance Rule.** Every heading, subtopic, keyword and FAQ suggested must be something this site can credibly write about from its actual services or products. Read the homepage and sitemap first. Do not borrow a competitor's structure when those sections cover things this site does not offer. Before each suggestion ask: *can this website actually deliver on this content?* If no, delete it. A brief full of undeliverable sections is how a content programme ends up publishing pages about things the business does not do.

**Site Structure Coverage Rule.** When briefing a hub, category, overview or "types of" page, the outline must reference **every** relevant category or sub-page that exists on the site — none invented, none omitted — each as its own section with an internal-link suggestion. That is what makes the page a functioning hub rather than an essay. For non-hub pages, use the site structure to suggest real link targets without forcing every category into the outline.

Both rules are checkable afterwards: take every heading in the brief and find its supporting page or service. A heading with no referent is a defect.

**Output-language rule** `[practitioner]` — never name researchers, frameworks or tools in client-facing output ("the X method", "the Y formula", vendor tool names). They are internal thinking aids. Write for a business owner or a writer, not for an SEO audience.

## Information gain is the non-negotiable field

`[practitioner]`. Every brief must state **exactly** what new value the page adds that no currently ranking page provides: proprietary data or original research; a case study with real outcomes; expert quotes or first-hand experience; an original synthesis or framework. **"More detail" and "better formatting" are not answers.** If the field cannot be filled, the page probably should not be commissioned — that is the field's job.

The information-gain gate that decides whether an asset is worth commissioning at all lives in skill `seo-authority` › authority-links-and-pr.

## Research before the brief

Run this before a brief or article goes to a writer. The evidence labels judge **one claim**; this section judges **the set of research** the claims were drawn from.

### Echo clustering — five articles quoting one study count once

`[practitioner]` For each load-bearing claim:

1. Trace every retrieved source back to its **upstream** — the original statistic, quote or analysis.
2. Group the sources by upstream. Several paraphrases of one upstream form an **echo cluster and count as 1**. Several independent upstreams making compatible claims form a healthy cluster, counted as the number of upstreams.
3. Cite the upstream as the primary source; cite a secondary one only when it adds analysis.
4. Measure coverage by **number of clusters, not number of retrieved pages**.

Record it inline:

```
Claim: <claim with its number and date>
Upstream: <original source>
Echo sources: <paraphrases — not corroboration>
Independent corroboration: <different upstream, its own number>
Cluster health: <N defensible upstreams; anything quarantined and why>
```

This is our "65 of 118 controlled measurements come from one publisher" rule, applied to brief research.

### Five checks before research reaches a writer

`[practitioner]`

| Check | Passes when |
|---|---|
| Groundedness | every non-trivial claim is tied to evidence that substantiates it; no unnamed "studies show" |
| Specificity | named entities, exact numbers, dates |
| Coverage | ≥ 2 independent upstreams per load-bearing claim, and ≥ 2 perspectives (provider and consumer, regulator and practitioner) |
| Actionability | the reader can do something concrete with it |
| Format | inline citations; no invented titles |

A load-bearing claim resting on one source fails Coverage however good that source is. The source's 30/25/20/15/10 weights and its "< 70 = remediate" cut-off are an `[unvalidated house heuristic]` — use the checks, not the score.

### Pre-flight — reframe trap topics before searching

`[practitioner]`

| Trap | Example | Reframe |
|---|---|---|
| Demographic shopping phrasing | "gift for 40-year-old man" | ask hobby / relationship / budget; search those |
| A number that collides with unrelated content | "42 …" | drop the number unless it is the subject (a law number, a tariff year) |
| Tutorial phrasing | "how to use X" | search the way practitioners talk: "X setup", "X problems" |
| A single generic noun | "electricity" | ask for the angle first (tariff type, switching, bill) |

Log it as `Pre-flight: matched <trap>. Reframed to "<query>".`

### Decompose named entities

`[practitioner]` When the subject is a named provider, product, law or regulator, plan five searches. Start with the **time anchor**, then cover the **discourse** (Reddit, forums, and Portal da Queixa for Portugal), the **tangential entities** (parent group, related products), the **counter-perspective** (complaints, competitors, consumer bodies) and, last, the **primary entity** (its official site, a filing with the regulator). Place this plan at the top of the research notes so a reviewer sees what was searched.

### Freshness floor

| Topic type | Floor for load-bearing sources |
|---|---|
| News, trend, product release | ≥ 2 sources within 30 days (≥ 1 for a release) |
| Practitioner workflow, evergreen explainer | ≥ 2 within 90 days |
| Historical / definitional | none |

Older sources can supply context but never carry the claim. The 30- and 90-day values are an `[unvalidated house heuristic]`. Portuguese regulated figures (ERSE tariffs, IRS tables, IAS) are different: there the floor is the **current regulatory period**, not a count of days — an effective date outranks a publication date `[practitioner]`.

## Per-page-type brief variants

`[practitioner]` (source dated 2026-04-17). These are the section-level variants of the generic template in `content-and-intent.md`; adapt, do not apply mechanically — not every section fits every business.

| Page type | Goal | Mandatory sections | Schema | Primary-keyword placement |
|---|---|---|---|---|
| Service | Convert to enquiry/booking | What it is (definition box, 80-120 words) · Who needs it · How it works (numbered) · Costs (table or range) · Outcomes · Why choose us · FAQ · CTA | Service (+ LocalBusiness if location-specific) | H1, first 100 words, one H2, slug, title |
| Blog post | Rank informational, feed service pages | Direct answer first (40-60 words, snippet target) · Context · 3-5 H2 subtopics from PAA and gaps · Common mistakes · FAQ · contextual CTA | Article | H1, first 100 words, slug, title, one image alt |
| Case study | Trust via real outcomes | Outcome first (bold stat in line one) · Client situation · Challenge · Approach · Result with figures · Takeaways · related-service CTA | Article | Outcome or matter type in H1 and title |
| Category | Rank broad terms, funnel to children | Scope · **one section per real sub-page, linked** · Who we help · Process · FAQ · CTA | Service + BreadcrumbList | Category name in H1, title, URL, first paragraph |
| Landing | One conversion action | Hero (offer + CTA) · Problem · Benefits · Social proof · How it works (3 steps) · Objections/FAQ · final CTA | WebPage | Offer or outcome in H1, title, hero subhead |
| FAQ page | Long-tail and snippet capture | 8-15 questions grouped by subtopic, each answered in 40-60 words · CTA after the last | WebPage (see below) | "[Topic]: Perguntas frequentes" style H1, and the first answer |
| Location | Rank [service] + [city] | What we do in [city] · Local areas served · Service areas · Why local matters · Local team · Local reviews · FAQ · local CTA | Service + LocalBusiness (address, phone, geo) | [Service] [City] in H1, title, URL, first paragraph, schema |
| About | Site-wide trust | Who we are · Story with founding date · Team bios with credentials · Values · Awards with dates · Media mentions · CTA | Organization + Person per member | Brand name or "[Brand] [industry]" |
| Homepage | Brand authority, funnel outward | Hero · Services overview linked out · Differentiators · Social proof · Service area · broad FAQ · CTA | Organization + WebSite + Service | Primary service (+ city) in H1, title, first paragraph |
| Hub / pillar | Topical authority | See `./page-types-and-serp-clustering.md#hub-and-spoke-build-specs` | Article + BreadcrumbList + ItemList | Broadest keyword |

**Schema caveat carried from the source, and it is the reason to read this table rather than an older one**: Google retired FAQ rich results for all sites on 7 May 2026 `[documented: https://developers.google.com/search/updates, 2026-10-11]`, so the templates specify plain `WebPage` and warn against adding `FAQPage` for visibility — no ranking or AI benefit is confirmed. `QAPage` applies only where users can submit answers to a single question. The register of what still produces a rich result lives in skill `seo-evidence` › titles-and-serp-tests; do not re-derive it here.

**Keyword placement** `[practitioner]`. Density is framed in the source, correctly, as **an internal readability and stuffing heuristic — not a Google percentage rule**, and is imported only with that framing intact. There is no quota. The hard requirement is placement, not frequency: title and H1 (near the front), slug, meta description, first 100 words, and one image alt where relevant.

## Sources

- claude-seo@skills/seo-content-brief/SKILL.md:26-38 — improve vs new-page modes.
- claude-seo@skills/seo-content-brief/SKILL.md:72-94 — Website Relevance Rule, Site Structure Coverage Rule, output-language rule.
- claude-seo@skills/seo-content-brief/SKILL.md:145-152 — information-gain requirement.
- claude-seo@skills/seo-content-brief/references/page-type-templates.md:1-153 — per-page-type brief variants.
- claude-seo@skills/seo-content-brief/references/keyword-density.md:1-30 — keyword placement, density as a readability heuristic only.

