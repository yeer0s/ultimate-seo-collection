<!-- split-header-2: part 2 of 2 of international-and-hreflang.md (original lines 124–220; boundary H2) -->
# International SEO (2 of 2) — scale, frameworks, Bing/Yandex; locale coverage states and release gates
## Contents

- Delta: scale, frameworks, Bing/Yandex
- Locale coverage states and release gates
- Cross-references
- Unverified
- Sources

Other parts of the same original file: [international-and-hreflang.md](international-and-hreflang.md).

<!-- /split-header-2 -->
## Delta: scale, frameworks, Bing/Yandex

What the hreflang basics in [rendering-and-sitemaps.md](rendering-and-sitemaps.md#hreflang) do not yet say.

**Same-language regional pages may share one canonical.** Translations self-canonicalise. For similar or duplicate content in the *same* language on different regional URLs (say `example.de/` and `example.com/de/`), Google's multi-regional guidance says to pick a preferred version and use `rel="canonical"` plus hreflang so the right regional URL is served `[documented: https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites, 2026-10-12]` — not every regional URL has to point at itself. The source repo's SKILL.md:184 claims the opposite ("each locale page must self-canonical"); its own reference file is the better source and is followed here. This does not relax the rule for translations: locale variants in different languages never canonicalise to each other.

**Placement methods are equivalent; pick one.** HTML `<link>`, the HTTP `Link` header and sitemap `<xhtml:link>` are equivalent for Google; using all three at once brings no Search benefit and is harder to manage `[documented: https://developers.google.com/search/docs/specialty/international/localized-versions, 2026-10-12]`. Use one method per site.

**Scale.** A sitemap is limited to 50 MB uncompressed or 50,000 URLs `[documented: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap, 2026-10-11]`. With about 20 alternates per URL, plan on 2,000–5,000 URLs per sitemap file `[practitioner]`. Divide sitemaps along content-type lines rather than by locale; files split by locale all have to cross-reference one another `[practitioner]`.

**Next.js / next-intl.** Two framework caveats (self-alternate missing from `sitemap.ts`, `localePrefix: 'never'`) are recorded with the implementation in [rendering-and-sitemaps.md](rendering-and-sitemaps.md#hreflang).

**Bing and Yandex** `[practitioner]` — from third-party sources; the source repo cites no Bing document. Reports say Bing gives hreflang only weak weight, leaning more on `<html lang>`, `<meta http-equiv="content-language">`, the ccTLD and server location; Yandex is reported to support hreflang the way Google does. Inexpensive insurance: a correct `<html lang>` on every page and the content-language meta on locale pages. Check Bing Webmaster Guidelines before presenting any of this as Bing policy.

**Paginated locale pages.** Give every page of every locale its own canonical URL; never use page 1 as the canonical for page 2 and beyond. Google says it no longer uses `rel="next"`/`rel="prev"` (retired for Google; other engines may still use them) `[documented: https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading, 2026-10-12]`.

**noindex vs not building the page.** For thin locale pages the source prefers not creating what cannot be made helpful. Google's crawl-budget guide says Google still requests a `noindex` page before dropping it, and that the guide is aimed mainly at sites with 1 million+ pages changing weekly or 10,000+ pages changing daily `[documented: https://developers.google.com/crawling/docs/crawl-budget, 2026-10-12]`. Below that, page-level `noindex` remains a valid remedy, as Machine translation above says. A cross-language canonical is never the way to hide a thin translation.

**Site-wide quality drag.** Google says its core ranking systems work mainly at page level but also consider some site-wide signals, and that the March 2024 core update folded the identification of helpful content into several core systems `[documented: https://developers.google.com/search/blog/2024/03/core-update-spam-policies, 2026-10-11]`. Its core-updates guide adds that deleting unhelpful content can help the good content on a site perform better `[documented: https://developers.google.com/search/docs/appearance/core-updates, 2026-10-12]`. A set of low-value locales is the usual way a multilingual site builds up that drag `[practitioner]`.

## Locale coverage states and release gates

Every rule in this section is `[practitioner]`.

### Three decisions, kept apart

1. **Language support** — content or interface exists in the language.
2. **Locale support** — spelling, formats, currency, terminology or product behaviour differ.
3. **Market entry** — the geography has working pricing, payments, support, proof and compliance.

Countries differing is not by itself a reason for country copies; a locale needs a distinction someone will maintain. Order candidate locales on five inputs: demand that already exists, the search opportunity, likely conversion, how deep the competition is, and whether the team can keep the locale up to date.

### One coverage state per page type per locale

| State | Meaning | Public behaviour |
|---|---|---|
| `source-current` | The source-language page is current | Source URL public |
| `translation-draft` | Work exists but is not approved | Preview or `noindex` only |
| `localized-ready` | Content, terminology, facts and metadata passed review | The locale URL may be indexed and may join hreflang |
| `outdated` | The source changed after approval | Stays live; queued for review by risk. On a site whose numbers change, an outdated locale publishes wrong figures — high risk |
| `not-applicable` | The product or content does not apply in that market | No alternate is manufactured |

Gates differ by page type: support pages and UGC can pass a lighter gate than pricing, checkout, legal and high-intent pages. Anything regulated or legal goes to a subject-matter reviewer, who checks that the parties, numbers, obligations, rights, jurisdiction and version precedence all survive translation.

**A localized URL never carries source-language body text.** Translated chrome (nav, footer, title) around untranslated content is a mixed-language page, not a locale; if it also carries hreflang, it tells Google an equivalent page exists when none does.

### URL invariants

- Each indexable locale page has exactly one stable public URL. User preference (cookie, `Accept-Language`) may help returning visitors but never stands in for public locale URLs.
- The URL, the rendered language, `<html lang>`, navigation, metadata and structured data all describe the same locale.
- The language switcher uses crawlable links and keeps the page context when an equivalent exists; when none exists, it says so.
- Canonical, hreflang, sitemap, internal links and redirects agree on one URL form.
- Subdirectories are often the simplest choice. A subdomain or ccTLD is justified when hosting, ownership, regulation or operations call for it. No structure wins everywhere.

### Migrating locale URLs (query parameter, cookie, prefix or domain change)

1. Inventory current URLs and their behaviour, including indexed and externally linked variants.
2. Freeze the target URL policy and the locale mapping.
3. Map each old URL to its closest new locale URL with a permanent redirect, keeping path and query state where that is safe.
4. Update internal links, the switcher, canonicals, hreflang, sitemaps, structured data and analytics segments.
5. Keep compatibility redirects until logs and search data show nobody uses them — there is no fixed retention period.
6. Declare rollback triggers in advance, and confirm a rollback would not bring back conflicting index signals ([migrations-and-recovery.md](migrations-and-recovery.md)).

### Production checks per page type × locale

- The intended status code; the initial HTML carries the right language, title, description, canonical and locale-aware structured data.
- hreflang is reciprocal only among published, genuinely equivalent (`localized-ready`) pages.
- No mixed-language or fallback rendering under a locale URL.
- Sitemaps list only canonical, indexable, published locale URLs.
- Redirects terminate; internal links stay inside the current locale whenever an equivalent exists.

Look at each locale separately instead of relying on global totals alone: index coverage, impressions, clicks, conversions and stale-content rate. Open the next locale only once the first has shown it can keep pace with source changes.

## Cross-references

- `rendering-and-sitemaps.md#hreflang` — tag implementation, reciprocity, `x-default`, ISO code rules, canonical alignment, ccTLD vs subdirectory vs subdomain, and the "all alternates point to `/`" duplicate-content failure. The technical layer; not restated here.
- `crawl-and-index.md#indexability` — page-level `noindex`, the remedy for a low-value translated page.
- skill `seo-ai-search` › ai-retrieval-and-citation — passage citability, which translated-widget output degrades.
- skill `seo-content` › content-and-intent — "translate intent, not just words" as a content position.
- skill `seo-content` › briefs-and-personas — the Website Relevance Rule, which is the same discipline applied to a brief: do not import structure the site cannot actually deliver.
- skill `seo-evidence` › experiments-and-revert-2 — before/after comparability, which region-specific result units and consent-mode effects both undermine in EEA markets.

## Unverified

- Hreflang cluster canonical rules: the source says the canonical must sit inside the hreflang cluster, that hreflang on a URL canonicalised elsewhere is ignored, and cites a 2023 Mueller remark on folding regional pages [unverified: the saved multi-regional and localized-versions pages say none of this]
- Hreflang method conflicts: the source says a pair is dropped when two placement methods conflict [unverified: the saved localized-versions page does not say so]
- Hreflang sitemap scale: the source says `<xhtml:link>` children do not count toward the 50,000-URL limit, so the 50 MB limit is reached first, and that Mueller advises annotating only pages that get wrong-language traffic [unverified: the saved sitemap and localized-versions pages do not say so]

## Sources

- claude-seo@skills/seo-hreflang/references/machine-translation-qa.md:1-60 (source last verified 2026-07-09) — QRG §4.6.5 MT position, the spam-policy anchor, the signals table and the "what NOT to flag" list. Policy statements are repo transcriptions, not a primary read (labels sit on the claims in the body); severities `[practitioner]`.
- claude-seo@skills/seo-hreflang/SKILL.md:55-62 — invalid hreflang code patterns (repo transcription; not a primary read).
- claude-seo@skills/seo-hreflang/SKILL.md:64-72 — geo-signal hierarchy (`[practitioner]`), hreflang-as-hint and the 2022 removal of GSC International Targeting (repo transcription; not a primary read).
- claude-seo@skills/seo-hreflang/SKILL.md:74-83 — EEA / South Africa / Türkiye aggregator and supplier units, documentation dated 2026-09-08 (repo transcription; not a primary read); the Portugal-is-EEA consequence is `[practitioner]`.
- claude-seo@skills/seo-hreflang/references/locale-formats.md:9-100 — number, date, currency, address, phone tables, expansion ratios and validation rules. `[practitioner]`. **No pt-PT row exists in the source**; the pt-PT row above is added here as `[practitioner]`.
- claude-seo@skills/seo-hreflang/references/content-parity.md:37-50 — word-count ratio table and freshness deltas. `[practitioner]`; the Portuguese row is extrapolated from the expansion table and labelled as such.
- claude-seo@skills/seo-hreflang/references/content-parity.md:65-78 — 100-point parity score. `[unvalidated house heuristic]`.
- <https://developers.google.com/search/docs/essentials/spam-policies> — scaled content abuse, naming translation as an automated transformation. Source records the policy as updated 2026-05-15; re-check before citing the date.
- ICU/CLDR via `Intl.NumberFormat('pt-PT')` and `Intl.DateTimeFormat('pt-PT')` — group separator U+00A0, decimal comma, `€` after the number, `dd/mm/aaaa`. Checked 2026-09-22 on Node.
- claude-seo@skills/seo-hreflang/references/cultural-profiles.md — **deliberately not imported** (stereotype tables); exclusion reasoned above.
- coreyhaines31/marketingskills@skills/seo-audit/references/international-seo.md, coreyhaines31/marketingskills@skills/seo-audit/SKILL.md:162-233 (phase-2 adapted file research/adapted/coreyhaines31__marketingskills/international-hreflang-delta.md) — same-language regional canonicals, placement-method conflicts, sitemap scale, Bing/Yandex signals, paginated locale pages, noindex vs not building, site-wide quality drag. INTEGRATE, MIT.
- kostja94/marketing-skills@skills/strategies/commercial/localization/SKILL.md (phase-2 adapted file research/adapted/kostja94__marketing-skills/locale-coverage-states-and-release-gates.md) — launch decision split, five coverage states, URL invariants, locale URL migration steps, production checks. INTEGRATE, MIT.
