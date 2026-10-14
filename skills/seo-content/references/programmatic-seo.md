# Programmatic SEO — Reference
<!-- split-header-2: part 1 of 2 of programmatic-seo.md (original lines 1–197; boundary start) -->
<!-- /split-header-2 -->

## Contents

- The core distinction
- Quality checklist (pass on every programmatic page)
- Data defensibility tiers
- Boilerplate audit
- Common programmatic patterns
- Playbook catalogue

Other parts of the same original file: [programmatic-seo-2.md](programmatic-seo-2.md).

## The core distinction

| Good programmatic SEO | Bad programmatic SEO (doorway pages) |
|----------------------|--------------------------------------|
| Each page satisfies a distinct intent | Pages target slight keyword variants of the same intent |
| Each page has unique value (data, calc, comparison, decision support) | Templates with location/keyword swap and nothing else |
| Useful comparison tables, calculators, or local data | Boilerplate text + city name |
| Pages are internally linked | Pages exist only to capture queries, not to be navigated |
| Pages are kept updated | Stale, never refreshed |
| Human QA on samples | No human ever looks at outputs |
| Distinct titles, metas, H1s, body content | Identical structure, only the entity name changes |

If your "1000 city pages" are 95% the same text with the city name swapped, treat that as a review signal, not a verdict. Google's doorway test is about function: pages "targeted at specific regions or cities that funnel users to one page", or "substantially similar pages that are closer to search results than a clearly defined, browseable hierarchy" `[documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]`. If the pages fail that test, Google's spam policies say they may rank lower or not appear in results at all.

## Quality checklist (pass on every programmatic page)

Run this before publishing a programmatic template at scale:

- [ ] **Unique search intent** — what specific query does this page satisfy that other pages don't?
- [ ] **Unique data** — is there a number, fact, comparison, or piece of info that only this page has?
- [ ] **Unique recommendation** — does the page give a specific, page-aware recommendation (not boilerplate)?
- [ ] **Useful elements** — table, calculator, list, decision tree, map — something interactive or comparative?
- [ ] **Clear update logic** — when does this page get refreshed? from what data source?
- [ ] **Internal links** — does this page link out to ≥3 related pages with descriptive anchors?
- [ ] **Indexation rules** — should ALL pages be indexed, or only those above a quality threshold (e.g. ≥20 listings, ≥10 reviews, ≥3 data points)?
- [ ] **Human QA on a sample** — pull 5-10 random pages and read them. Are they actually useful?
- [ ] **Conversion path** — what does the user do after reading this page? Is the CTA clear and matched to intent?
- [ ] **Doorway test** — if you swapped the entity (city, product, brand), would the page change in any way other than name? If no, that is a review signal: check the page's function against Google's doorway definition (does it only funnel visitors to one shared page, or is it closer to a search result than a browsable hierarchy?) `[documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]`. If it fails that check, redesign the template or remove the pages; if visitors can complete the real task for that entity on the page, it is a destination.

## Data defensibility tiers

`[practitioner]` Whether each URL in a set can carry unique value depends on the data underneath it, so grade the data source before anyone builds a template.

| Tier | Source | Duplicate / thin risk | What the page still needs |
|---|---|---|---|
| 1 Product-generated | Artefacts the product itself renders: templates, exports, generated previews, calculator outputs | Lowest, provided each URL shows distinct output | Proof the artefact is real (embed, download, ID) |
| 2 Product-derived | Own aggregates: cohorts, benchmarks, adoption, prices observed in the funnel | Low, when aggregated | Minimum cell size, no individual identifiable, "as of [date]" label, the window covered |
| 3 UGC / customer | Reviews, submissions, showcase items | Medium | Moderation, consent for names/logos, `Review` markup only when accurate, a cap or quality score on submissions |
| 4 Licensed / partner | Partner price lists, licensed feeds | Medium — competitors receive the same feed | Contract scope per field, attribution line, refresh tied to the partner SLA; uniqueness has to come from our framing, comparison logic or calculator, never the raw feed |
| 5 Public / scraped | Open data, directories, enrichment | Highest — everyone holds the same facts | Synthesis, an editorial angle or a unique tool on top; date-stamp volatile facts; plan pruning or `noindex` for URLs that stay thin |

Fill each page's evidence block from tiers 1–2 first and reach for tier 5 last. A set resting only on tier 5 should be presumed a doorway candidate until it passes the doorway test above.

**Mowei mapping** `[practitioner]`: tariffs and offers taken from ERSE, ANACOM or partner feeds sit at tiers 4–5. What makes one comparison URL defensible is tiers 1–2 — our calculator output for that profile, the price history we observed, our methodology. Those belong on the page, not just the feed row.

### AI-written copy on a data spine

`[practitioner]`

- The data layer holds the facts (one row per page in JSON/CSV, with a source and date on every field); the model is limited to phrasing, shortening and ordering them. The system prompt forbids invented numbers, and publishing is blocked whenever a required field or citation is empty.
- Expose a machine-readable table of the page's facts, on the page or in an appendix, so any number can be audited.
- Record provenance per field and set a freshness window per field type, e.g. prices 30 days, ratings 90 days `[unvalidated house heuristic]` (the windows are the source's, not measured).
- Remove rows that would duplicate an intent before generation, not afterwards.
- An optional disclosure ("summary drafted with AI; figures from [source, date]") builds trust; it does not move rankings.

Shuffling section order or adjectives between URLs creates no value: Google's spam policy defines scaled content abuse as many pages generated "for the primary purpose of manipulating search rankings and not helping users", typically unoriginal content "that provides little to no value to users, no matter how it's created" `[documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-14]` — see the scaled-content refusal in the router skill `seo-optimizer`.

## Boilerplate audit

`[practitioner]` For a set that is already live and whose template pages have started to read as interchangeable — the same closing line, the same value statement on every URL, identical FAQ endings.

1. **Scan the rendered HTML**, not the template source, at three levels: inside a single page (sections that all close on the same formula), inside one category, and site-wide. Flag any sentence or n-gram found on more than ~30 % of a category's pages `[unvalidated house heuristic]`. Leave header, footer and navigation out; keep template body text in.
2. **Sort each flagged pattern** into one of three kinds:
   - *Information-free filler* — would be equally true on every page.
   - *Accurate but generic* — true, yet nothing in it is specific to this entity.
   - *Ordinary words at high frequency* — normal vocabulary; usually fine.
3. **Decide URL by URL, not sentence by sentence:**
   - Page-specific data exists → swap the filler for that data, stated functionally (which constraint this option solves, for whom, at what figure). Never replace one template sentence with a rotation of synonyms.
   - No page-specific data → merge into a parent (301) or `noindex` until the data exists. Rewording is not a fix.
   - Ordinary high-frequency words → leave them alone.
4. **Re-scan** after every round, one category at a time, and check no new shared pattern has appeared.
5. **Prevent recurrence:** make the same n-gram / near-duplicate check (the body-level shingle check under "Titles + metas at scale" below) a publish gate for every new batch.

⚠️ The source also recommends preparing 8–15 synonym variants and cycling them across neighbouring pages, or replacing 30–40 % of the instances. **Refused:** both make pages look different to a similarity check while adding no value, which is duplicate-filter evasion.

## Common programmatic patterns

### Comparison: provider × provider

```
URL: /compare/[provider-a]-vs-[provider-b]/
Title: [Provider A] vs [Provider B]: [Vertical] Compared (2026) | [Brand]
```

Page elements:
- Quick verdict (1-2 sentences)
- Side-by-side comparison table (price, features, terms, support, reviews)
- Pros/cons of each
- Who each is best for (specific scenarios)
- How they compare on common pain points
- Real customer review aggregate
- Switching guide (A → B and B → A)
- FAQ
- Internal links to: each provider's individual page, the vertical pillar, related comparisons
- CTA: lead form / quote

Generate from data: provider table, review aggregate, pricing API.

### Best X in Y

```
URL: /best/[category]-in-[location]/
Title: Best [Category] in [Location] (2026) | [Brand]
```

Page elements:
- Quick top-3 recommendation with reasons
- Full ranked list with criteria explanation
- Comparison table of top 5
- Local pricing reality (if applicable)
- Common local pain points / regulations
- FAQ specific to the location
- CTA

### Alternative to X

```
URL: /alternative-to-[competitor]/
Title: [N] [Product] Alternatives to [Competitor] ({Year}) | [YourBrand]
```

⚠️ **Two different brands live in this template.** `[Competitor]` is the product being replaced; `[YourBrand]` is the publisher. Using one token for both — as an earlier version of this file did — renders *"Alternatives to Salesforce | Salesforce"*, which reads as the competitor's own page and will be treated as such.

Page elements:
- Why people leave [brand]
- Top alternatives with comparison
- "Best alternative for [scenario]" sections
- Migration guide
- FAQ
- CTA

### Local service pages

```
URL: /[service]/[city]/
Title: [Service] in [City] | [Brand]
```

Quality requirement: each city page must include at least one piece of city-specific content:
- Local pricing data
- Local provider/coverage info
- Local regulations or tax implications
- City-specific testimonial or case study
- Local FAQ
- Map / directions if physical service

A city page with no city-specific content is a doorway risk. Check its function: if it lets visitors do the real task for that city (check availability, book, see local prices), it is a destination; if it only funnels them to one shared page, it matches Google's doorway definition, and such pages may be demoted or removed `[documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]`.

### Product variants (e-commerce)

```
URL: /products/[product]/[variant]/
```

Use canonical to the canonical product if variants have minor differences. Use unique pages with unique content if variants are meaningfully different (size, edition, region).

## Playbook catalogue

The patterns above (comparison, best-X, alternative, local, product variants) are the common ones. These are the other recurring playbooks, each with the bar that separates a real page from a doorway `[practitioner]`. The last column applies this file's doorway test to that playbook: swap the entity and name what must still differ.

| Playbook | Query shape | URL | Value bar (fails → do not build) | Doorway test — after swapping the entity, what must differ |
|---|---|---|---|---|
| Converter / calculator | "[X] to [Y]", "[thing] calculator" | `/converter/x-to-y` | A working tool, current data and a correct result on every URL; related conversions linked. Restating the pair fails. | The computed result and the inputs it uses |
| Templates | "[type] template" | `/templates/[type]` | A usable artefact (download or interactive), several variants, quality comparable to paid ones. Previews alone fail. | The artefact itself and its variants |
| Examples | "[type] examples" | `/examples/[type]` | Real examples, each with an analysis of why it works; filtering. Scraped screenshots fail. | The examples and their analyses |
| Personas / segments | "[product] for [audience]" | `/for/[segment]` | Features, cases, objections and proof specific to the segment. The same body with the segment name swapped fails. | Features, cases, objections and proof — not just the segment name |
| Integrations | "[A] [B] integration" | `/integrations/[b]` | The integration exists; setup steps; use cases. Vaporware fails. | Setup steps and use cases for that integration |
| Glossary | "what is [term]" | `/glossario/[term]` | One term per page, deeper than a dictionary entry, with examples and linked related terms. | Definition, examples and related-term links |
| Directory | "[category] providers" | `/[category]` | Every listing carries details and data, filtering, update dates. Names only fails. | The listings, their data and update dates |
| Profiles | "[entity]" / "[entity] + attribute" | `/[entity]` | Sourced, maintained facts that add something beyond Wikipedia. A rehash fails. | The sourced facts about that entity |
| Translations | same intent, other language | `/[lang]/…` | Human-reviewed translation of all the main content, plus hreflang (skill `seo-technical` › international-and-hreflang). House rule: no unreviewed machine translation. (Google treats auto-translated pages as scaled content abuse when they are produced mainly to manipulate rankings and add little value `[documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]`; translation as such is not a violation.) | Language of the whole main content, human-reviewed |

**Defensibility order** `[practitioner]`, strongest first: proprietary (we created it) → product-derived (from our users) → user-generated → licensed → public. Public data alone gives the weakest claim to unique value per URL; state that in the plan and put computation, comparison or decision support on top. (Tier detail: Data defensibility tiers above.)

**Stacking playbooks** (segment × location, best-X × location) multiplies the URL count. Every added layer has to bring distinct data per URL; otherwise it is over-generation — pages with neither distinct demand nor distinct data (see "When NOT to do programmatic SEO").

**On a comparison/calculator platform** the natural fits are the converter/calculator, glossary, directory and segment rows; templates, examples and integrations seldom apply.

