<!-- split-header-2: part 2 of 2 of programmatic-seo.md (original lines 198–328; boundary H2) -->
# Programmatic SEO (2 of 2) — implementation, failure modes, section-level risk check, when not to
## Contents

- Programmatic page generation — implementation
- Failure modes (and fixes)
- Section-level risk check (site reputation pre-check)
- When NOT to do programmatic SEO
- Examples — when programmatic SEO is the right move
- Examples — when it's the wrong move
- Unverified
- Sources

Other parts of the same original file: [programmatic-seo.md](programmatic-seo.md).

<!-- /split-header-2 -->
## Programmatic page generation — implementation

### Architecture

1. **Data source** — structured DB / spreadsheet / API
2. **Quality threshold** — minimum data quality to publish (e.g. ≥10 reviews, ≥3 features, ≥1 image)
3. **Template** — page component that consumes data
4. **Slug builder** — deterministic, keyword-rich URLs
5. **Metadata generator** — unique title/description per page from data
6. **Schema generator** — appropriate JSON-LD per page
7. **Sitemap inclusion** — only published pages above threshold
8. **Index regeneration** — on data update, regenerate affected pages and ping IndexNow (**Bing + participating engines; Google does not participate** — for Google, rely on the updated sitemap `lastmod` and internal linking)

### Slug taxonomy rules

- Lowercase, hyphenated.
- Include the keyword, not the ID.
- Stable — don't change slugs once published (each change is a 301 + ranking risk).
- Localized per locale.

Good:
- `/compare/edp-vs-galp/`
- `/best-electricity-provider-algarve/`
- `/alternative-to-edp/`

Bad:
- `/compare/123/`
- `/best/listing-456/`
- `/p/abc-def-ghi/`

### Titles + metas at scale

Generate from a template with data variables, but vary structure to avoid identical-looking SERPs:

```
Templates (rotate):
- "{ProviderA} vs {ProviderB}: {Vertical} Compared ({Year}) | {Brand}"
- "{ProviderA} or {ProviderB}? Side-by-Side {Vertical} Comparison | {Brand}"
- "{ProviderA} vs {ProviderB} {Year}: Price, Features, Reviews | {Brand}"
```

**Never hardcode the year.** `{Year}` is a variable in every template or none — a literal `(2026)` bakes a rollover bug into every generated page and quietly dates the whole set each January. Whatever renders the year needs a rebuild trigger; a template that cannot be re-rendered is a template that goes stale silently.

Validate: no duplicates, ≤60 chars (`[unvalidated house heuristic]`; Google sets no title length limit, see content-and-intent.md), keyword present. ⚠️ **That validator cannot catch the failure the warning below describes** — it inspects titles, and the doorway test is about *bodies*. Add a body-level near-duplicate check (shingle/similarity across the generated set, flag pairs above ~90%) or the title validator will pass a set of doorways with perfect titles.

> ⚠️ **Vary titles, never *only* titles.** Rotating title/H1 templates across pages that are *genuinely different* (different provider, different data) is good. Keeping **identical body content** and changing only the title/H1/slug to slip past duplicate detection is the doorway/scaled-content anti-pattern — Google evaluates body text (near-duplicate detection), not just the URL, H1, and title. If two pages would read identically with the entity name swapped, treat that as a doorway warning sign and check function: a page that only funnels visitors to one shared page fits Google's doorway definition `[documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]`; a page where visitors complete the real task for that entity is a destination, though its copy is still worth differentiating.

### Schema at scale

Generate appropriate JSON-LD per page type:
- Comparison page → `Article` + `BreadcrumbList` (no comparison-specific schema exists)
- Product variant → `Product` + variant attributes
- Local service → `LocalBusiness` or service-specific subtype + `BreadcrumbList`
- "Best X" list → `Article` with `ItemList`

### Indexation strategy

Don't blindly index everything. Tier:

- **Tier 1 (index, sitemap, internal links):** Pages above quality threshold, with strong unique data.
- **Tier 2 (index but not in sitemap, lighter internal linking):** Mid-quality pages — let Google find them but don't push.
- **Tier 3 (noindex):** Below threshold — exists for users who land via direct link or filter, but not eligible to rank.

Monitor Search Console. A page with no impressions after 3 months is a candidate for review, not an automatic tier 3: first check that it is indexed and indexable (URL Inspection), that its query has demand in that period (seasonality, Keyword Planner or GSC history of sibling pages), and that it is reachable through internal links. Zero impressions only triggers this investigation; it never decides the tier. Move a page to tier 3 only when the review also finds a value problem — thin or near-duplicate content, no unique data, or no reason a visitor would choose it over its siblings — not merely low visibility `[unvalidated house heuristic]`.

## Failure modes (and fixes)

Each symptom has several possible causes; run the check before the fix.

| Symptom | Possible causes | Check that tells them apart | Fix once confirmed |
|---------|-----------------|------------------------------|--------------------|
| Pages indexed but no traffic | No demand for the query; out of season; thin/near-duplicate template (doorway risk) | Query demand and seasonality; compare page text against siblings | Thin template: add unique data per page or raise the threshold |
| Manual action: "Thin content with little or no added value" | Google's examples for this action are thin affiliate pages, content from other sources (scraped content, low-quality guest posts) and doorways `[documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11]`; the action is about added value, not about how the pages were produced | Read the example URLs in the Manual Actions report | Remove or rebuild the affected template, then request review |
| Sudden traffic drop after launch | Deployment error (accidental `noindex`, robots.txt, canonical, redirects); algorithmic update; manual action | URL Inspection on sample pages; check deploy diff; Manual Actions report; dates of confirmed Google updates | Deployment error: fix and re-request indexing. Update: audit the template and merge near-duplicates |
| Pages indexed inconsistently | Low perceived quality or duplication; weak internal linking; crawl capacity (rarely, below very large sites) | Coverage reasons in the Page indexing report; crawl stats; link depth | Improve and differentiate pages; link important ones; reduce indexable low-value variants |
| Cannibalization between pages | Templates target overlapping intents | GSC Performance: several of your URLs swapping positions for the same query | Differentiate the intents, or merge and redirect |
| Clicks fall while impressions hold, on informational queries | An AI Overview now answers the query (hypothesis); lower rank; seasonality; a SERP layout change | Check the live SERP for an AI Overview citing or summarising your page; compare position and impressions over the same period | If the overview answers the query: offer what a summary cannot (tools, calculators, current data) `[hypothesis]`; otherwise treat as a ranking or demand change |

## Section-level risk check (site reputation pre-check)

Unit of analysis is the **first path segment** (subfolder), because Google's site-reputation policy acts on sections, not domains [hypothesis]. Per sampled page, count three signal families and average per section:

- third-party authorship markers — "Partner Content", "Sponsored", "Brand Studio", "In Partnership With", "Advertorial", "Paid Post";
- commercial-intent markers — "Buy now", "Add to cart", "Promo code", "Coupon", "Affiliate disclosure";
- affiliate link parameters — `tag=`, `aff_id=`, `affid=`, `partnerid=`, `ref_=`.

Since 2026-08-30 Google's site-reputation manual actions have a different effect for searchers inside the EEA than outside it [documented: https://developers.google.com/search/blog/2026/08/update-site-reputation-policy, 2026-10-11]; see skill `seo-engine-policies` › google-updates-timeline.

Flag a section whose profile departs from the site's main body of content — for example an editorial site where one subfolder reads as nothing but commerce. The result is **advisory only**: no scanner can see the agreement between the site and whoever produced the content `[practitioner]`.

⚠️ Defects in the source method, fixed before reuse `[practitioner]`:

- The method treats `utm_source=` / `utm_campaign=` as affiliate signals too, yet they only tag campaigns and say nothing about affiliation — remove them from the count.
- It scores phrases such as "Compare prices" and "Best X deals" as commercial skew. By design a **comparison platform** is commercial throughout, so judge each section against the site's own corpus and never against a fixed absolute rate; with an absolute rate every Mowei vertical would flag. What Mowei actually has to watch for is a section written by a partner (a lender's "guide" hosted under `/guias/`, say).
- The source's cut-offs per section — affiliate hits ≥3, commerce hits ≥2, third-party hits ≥1, each counted per page — are an `[unvalidated house heuristic]`.

## When NOT to do programmatic SEO

- You don't have unique data per page.
- You can't human-QA at least a sample.
- You can't keep pages updated.
- The intent doesn't actually have search volume per variant.
- Your domain has any spam signals already (one bad programmatic launch can compound).

If any of these are true, stick to handcrafted pages until you have the data + processes.

## Examples — when programmatic SEO is the right move

- Comparison platform with structured provider data → comparison pages
- Marketplace with listings → "best X in Y" pages from listing aggregates
- SaaS with strong competitor → "alternative to X" pages
- Local service business with multiple cities → local service pages with real local data
- Job board → "[role] jobs in [city]" with active listings
- Real estate → "[property type] in [neighborhood]" with current listings
- E-commerce with variant taxonomy → variant pages where meaningfully different

## Examples — when it's the wrong move

- Blog with no structured data
- Personal portfolio
- B2B site selling one product
- Site that hasn't validated PMF (build a few pages first, see if they convert, then scale)

## Unverified

- Google 2024-11-19 clarification as quoted by claude-seo ("no amount of first-party involvement alters the third-party nature"): not verbatim [unverified: the quote is not found word for word in the saved 2024-11 Search Central post].

## Sources

- kostja94/marketing-skills@skills/seo/programmatic-seo/SKILL.md (lines 97-170, 235-261) (phase-2 adapted file research/adapted/kostja94__marketing-skills/programmatic-data-tiers-and-boilerplate-audit.md) — Data defensibility tiers, AI copy on a data spine, Boilerplate audit; the source's synonym-cycling remediation refused. INTEGRATE, MIT.
- coreyhaines31/marketingskills@skills/programmatic-seo/references/playbooks.md, coreyhaines31/marketingskills@skills/programmatic-seo/SKILL.md:36-66 (phase-2 adapted file research/adapted/coreyhaines31__marketingskills/programmatic-playbook-catalogue.md) — Playbook catalogue with value bars, defensibility order, layering rule; doorway-test column added by us. INTEGRATE, MIT.
- AgriciDaniel/claude-seo@scripts/parasite_risk.py:1-140 (v2.4.2) (phase-2 adapted file research/adapted/AgriciDaniel__claude-seo/templated-metadata-and-section-risk-checks.md, section 2 only) — Section-level risk check: unit of analysis, three signal families, advisory output, three defects fixed. INTEGRATE, MIT.
