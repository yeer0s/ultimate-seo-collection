<!-- split-header: part 2 of 2 of technical-audit.md (step-3 original lines 205–486; boundary H2) -->
<!-- split-header-2: part 1 of 2 of rendering-and-sitemaps.md (original lines 1–221; boundary start) -->
<!-- /split-header-2 -->
# Structured data, Core Web Vitals and hreflang tags — technical audit (2 of 3; sitemaps, IndexNow and JS rendering are in part 3)
## Contents

- Structured data (JSON-LD)
- Core Web Vitals
- Hreflang
- Unverified

Other parts of the same original file: [crawl-and-index.md](crawl-and-index.md), [rendering-and-sitemaps-2.md](rendering-and-sitemaps-2.md).

<!-- /split-header -->
## Structured data (JSON-LD)

Use Google Search Central as the source of truth for which schemas actually change SERP appearance — schema.org has many types but only a subset trigger rich results.

### Organization (root layout)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Example Brand",
  "url": "https://www.example.com/",
  "logo": "https://www.example.com/logo.png",
  "sameAs": [
    "https://www.linkedin.com/company/example",
    "https://twitter.com/example"
  ]
}
```

### WebSite (root layout)

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "url": "https://www.example.com/",
  "name": "Example",
  "alternateName": "Example.com"
}
```

**`SearchAction` / `potentialAction` is obsolete — don't ship it in new markup.** Google began removing the sitelinks search box on **21 Nov 2024**, «globally across all search results», and said it would then remove the Search Console rich results report for it and stop highlighting the markup in the Rich Results Test; unsupported structured data like this «won't cause issues in Search» `[documented: https://developers.google.com/search/blog/2024/10/sitelinks-search-box, 2026-10-14]`. So there's no urgency to strip it — just stop adding it.

`WebSite` itself **is** still supported and still worth shipping: site names use «a variation of WebSite structured data, which continues to be supported» `[documented: https://developers.google.com/search/blog/2024/10/sitelinks-search-box, 2026-10-14]` — a real, visible win.

⚠️ **The collision this used to cause.** The robots.txt template in [crawl-and-index.md](crawl-and-index.md#robotstxt-template) blocks `Disallow: /search?`, while the old `SearchAction` example declared `target: /search?q={search_term_string}` — the same file told you to block the exact path it told you to advertise. Blocking internal search results is *correct* (they're an infinite crawl trap and thin by nature); the `SearchAction` was the wrong half. Keep the robots rule.

### BreadcrumbList (every nested route)

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type":"ListItem","position":1,"name":"Home","item":"https://example.com/"},
    {"@type":"ListItem","position":2,"name":"Electricity","item":"https://example.com/electricity/"},
    {"@type":"ListItem","position":3,"name":"Compare Providers","item":"https://example.com/electricity/compare/"}
  ]
}
```

### Product (product/listing pages)

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "[Provider] [Tariff name]",
  "description": "[Tariff description from the provider's dated tariff sheet]",
  "image": ["https://www.example.com/img/tariff-example.png"],
  "brand": {"@type":"Brand","name":"[Provider]"},
  "offers": {
    "@type": "Offer",
    "priceCurrency": "EUR",
    "price": "[€/kWh from the dated, verified tariff sheet]",
    "priceSpecification": {"@type":"UnitPriceSpecification","unitCode":"KWH"}
  }
}
```

🛑 **`aggregateRating` is deliberately absent from this template — do not paste one in.** A hardcoded rating in a boilerplate is how fabricated review markup ships. Google requires `aggregateRating` to reflect ratings you genuinely collected *and* display to users on that same page; inventing one, or copying a plausible-looking `3.8` / `127`, is the **fake reviews** violation on the Hard Refusals list in SKILL.md. Emit it only from real, user-visible, first-party review data — and if the page has none, ship the Product block without it.

Two more traps in this block:

- **Product snippets need `name` plus one of `review`, `aggregateRating` or `offers`** — `image` is not on that list, and `priceCurrency` is «recommended for product snippets» but «required for merchant listing experiences» `[documented: https://developers.google.com/search/docs/appearance/structured-data/product-snippet, 2026-10-14]`. Check merchant-listing requirements separately; ship `image` whenever you have one `[unvalidated house heuristic]`.
- **`availability` is deliberately absent above.** `InStock` asserts inventory state, which is meaningless for a tariff that can never sell out. Include it only when stock is a real, changing fact.

**On `Product` vs `Service` for a tariff** `[unvalidated house heuristic]`: `Product` fits *here* — the tariff is a priced offer a user can actually sign up for, which is what `Offer` models. Whether it earns any rich-result or comparison-surface treatment for a tariff is not documented here `[hypothesis]`. Reach for `Service` instead when there is **no priced, purchasable offer** on the page (an advisory page, a "contact us for a quote" page). The distinction is whether a concrete price attaches, not whether the noun feels physical.

### FAQPage

⛔ **Dead for Google rich results as of 7 May 2026.** «As of May 7, 2026, FAQ rich results are no longer appearing in Google Search» `[documented: https://support.google.com/webmasters/answer/6211453, 2026-10-14]`, and Google removed the FAQ rich result documentation on 2026-06-15 `[documented: https://developers.google.com/search/updates, 2026-10-14]`. In Aug 2023 it had been narrowed to «well-known, authoritative government and health websites» `[documented: https://developers.google.com/search/blog/2023/08/howto-faq-changes, 2026-10-14]`.
FAQ report, Rich Results Test and API removal dates: unverified [unverified: no saved page dates them]; see ## Unverified.
**Do not promise a client FAQ rich results, and do not count FAQPage markup as a rich-result win.**

The remaining case for shipping it is **machine legibility**: clean Q&A pairs may be easier for non-Google consumers to parse `[hypothesis]`. For Google's AI features it buys nothing documented — «There's also no special schema.org structured data that you need to add» `[documented: https://developers.google.com/search/docs/appearance/ai-features, 2026-10-11]`. File it under machine-liftability, never under rich-result eligibility.

Only use on pages with genuine Q&A content that is visible to users on that page. Don't fake it.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How long does switching electricity provider take in Portugal?",
      "acceptedAnswer": {"@type":"Answer","text":"3 weeks on average. The new provider handles the switch — you don't need to contact the old one."}
    }
  ]
}
```

### Article / BlogPosting (content pages)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Switch Electricity Provider in Portugal",
  "datePublished": "2026-05-10",
  "dateModified": "2026-05-10",
  "author": {"@type":"Person","name":"Maria Silva","url":"https://example.com/authors/maria-silva"},
  "publisher": {"@type":"Organization","name":"Example","logo":{"@type":"ImageObject","url":"https://example.com/logo.png"}},
  "image": "https://example.com/images/switch-electricity.jpg"
}
```

### Other schemas worth knowing

| Type | Use for |
|------|---------|
| `SoftwareApplication` | Apps, tools, calculators, browser extensions |
| `LocalBusiness` (and subtypes: Restaurant, RealEstateAgent, etc.) | Physical-location businesses |
| `HowTo` | ⛔ **Dead for Google rich results.** Removed from desktop and mobile and the docs retired (Sept 2023). Markup is harmless but buys nothing on Google; keep only if a non-Google consumer needs it |
| `Review` | Genuine reviews only — never fake |
| `VideoObject` | Embedded videos |
| `JobPosting` | Job listings |
| `Event` | Events with date/location |
| `Recipe` | Cooking recipes |
| `Person` | Author/expert pages — describes who wrote it; any E-E-A-T effect is `[hypothesis]` |
| `Course` | Educational courses |

Validate every schema before shipping — **but pick the right validator.** Google's **Rich Results Test** only checks types Google still renders a rich result for, so do not expect it to validate `FAQPage` or `HowTo` (the RRT removal dates are unverified; see ## Unverified). For anything outside Google's live rich-result set — including markup you ship purely for machine-liftability — use **validator.schema.org**, which validates against the vocabulary rather than against Google's feature list. Using RRT alone will read "no items detected" on markup that is perfectly valid.

## Core Web Vitals

Core Web Vitals are **exactly three** metrics. Grading a site on five and calling the result "CWV" is how a passing site gets reported as failing.

| Metric | Target | What it measures |
|--------|--------|------------------|
| LCP (Largest Contentful Paint) | ≤ 2.5s | Main content load speed |
| INP (Interaction to Next Paint) | ≤ 200ms | Interaction responsiveness — replaced FID (retired) in 2024 |
| CLS (Cumulative Layout Shift) | ≤ 0.1 | Visual stability during load |

**Supporting diagnostics — *not* Core Web Vitals.** Use these to find *why* a CWV target is missed; never report them as CWV pass/fail:

| Metric | Target | What it measures |
|--------|--------|------------------|
| TTFB (Time to First Byte) | ≤ 0.8s | Server response speed (precondition for good LCP) |
| FCP (First Contentful Paint) | ≤ 1.8s | First paint of any content |

**Grade from field data, not lab data.** CWV assessment uses CrUX (real Chrome users, 28-day rolling); Lighthouse/PageSpeed lab scores are a debugging tool and routinely disagree with it. A verdict sourced from a lab run is not a CWV verdict.

### Common fixes

| Problem | Fix |
|---------|-----|
| Slow LCP image | Compress, preload via `<link rel="preload" as="image">`, use WebP/AVIF, set explicit `width`/`height` |
| Render-blocking CSS | Inline critical CSS; defer the rest with `media="print"` swap or `<link rel="preload">` |
| Render-blocking JS | `defer` or `async` on script tags; remove unused JS |
| Heavy third-party scripts | Audit Tag Manager bloat; delay non-critical scripts; consider Partytown |
| Slow server / TTFB | CDN, edge caching, better hosting, reduce DB query time |
| Layout shift (CLS) | Set `width`/`height` on images and embeds; reserve space for ads/iframes; preload fonts |
| Font flash (FOUT/FOIT) | `font-display: swap`; preload key fonts; use system fonts where possible |
| Too much client-side JS | Move to SSR/ISR; use React Server Components or framework equivalent |
| Bad mobile speed | Mobile-first design; reduce payload; lazy-load below-fold |

Tools: PageSpeed Insights (field + lab), CrUX (real-user Chrome data), WebPageTest (deep diagnostics), Lighthouse CI (automated regression).

## Hreflang

### Implementation

```html
<link rel="alternate" hreflang="pt-PT" href="https://example.com/pt/energia/" />
<link rel="alternate" hreflang="en" href="https://example.com/en/electricity/" />
<link rel="alternate" hreflang="de" href="https://example.com/de/strom/" />
<link rel="alternate" hreflang="x-default" href="https://example.com/" />
```

### Rules

| Rule | Why |
|------|-----|
| Reciprocal | Each variant must link to all others including itself |
| Use ISO codes | A language alone (`pt`, `de`) is valid; add a region (`pt-PT`, `en-GB` vs `en-US`) when you serve regional variants `[documented: https://developers.google.com/search/docs/specialty/international/localized-versions, 2026-10-14]` |
| `x-default` recommended | Google recommends it as the fallback for unmatched languages; not required `[documented: https://developers.google.com/search/docs/specialty/international/localized-versions, 2026-10-14]` |
| Translate intent, not just words | German users may search differently |
| Localize examples | Prices, regulators, providers, currency |
| Use European Portuguese, not Brazilian | If targeting Portugal |
| Don't auto-translate | Low-quality translations damage trust |
| Clean URL prefixes | `/pt/`, `/en/`, `/de/` — not query params |

### Common failures

- One layout declares multiple langs but they all point to `/`. **This is duplicate content signaling, not internationalization.** Either build the locale variants or remove the alternates.
- ccTLDs vs subdirectories vs subdomains decision should be deliberate; ccTLDs (`.pt`) carry strongest geo-signal but require separate domains.

### Next.js and next-intl caveats

- App Router `sitemap.ts`: `alternates.languages` does **not** emit a self-referencing `<xhtml:link>` for the `<loc>` URL — the documented output lists only the alternates you pass `[documented: https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap, 2026-10-12]`. Put the page's own locale in the list explicitly. (The example in [rendering-and-sitemaps-2.md](rendering-and-sitemaps-2.md#sitemapxml) emits one entry per locale URL and passes the full language map, so each entry's own locale is in its list.)
- next-intl localePrefix never: unverified [unverified: the saved next-intl routing page (2026-10-12) holds no text on localePrefix or alternate links]; see ## Unverified. Use `'always'`, or any setting that keeps one URL per language `[practitioner]`.

Scale, placement-method conflicts, same-language regional canonicals and Bing/Yandex: [international-and-hreflang-2.md](international-and-hreflang-2.md#delta-scale-frameworks-bingyandex).

## Unverified

- next-intl localePrefix never: next-intl `localePrefix: 'never'` takes the locale out of the URL and switches alternate links off [unverified: the saved next-intl routing page (2026-10-12) holds no text on localePrefix or alternate links]
- FAQ report, Rich Results Test and API removal dates: the FAQ search-appearance report and Rich Results Test support were dropped in June 2026 and Search Console API support in August 2026 [unverified: no saved page dates them]

