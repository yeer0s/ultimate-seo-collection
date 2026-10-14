<!-- split-header-2: part 2 of 2 of rendering-and-sitemaps.md (original lines 222–405; boundary H2) -->
# Sitemaps, IndexNow, JS rendering and the audit checklist (technical audit, rendering part 2)
## Contents

- Sitemap.xml
- IndexNow
- JS rendering — *working ≠ visible*
- Audit checklist (run on every audit)
- Sources

Other parts of the same original file: [rendering-and-sitemaps.md](rendering-and-sitemaps.md).

<!-- /split-header-2 -->
## Sitemap.xml

### Rules

- Only include canonical URLs.
- Exclude noindex'd, redirected, 4xx and non-canonical URLs. A parameter URL is excluded when it duplicates a canonical, and included when it is itself the canonical of distinct content — URL syntax does not decide it.
- Include `<lastmod>` for each URL — accurate dates only (lying about freshness can hurt).
- For multilingual sites, use `<xhtml:link rel="alternate" hreflang="..."/>` inside each `<url>` entry.
- Split into multiple sitemaps if >50,000 URLs or >50MB. Index sitemap references the children.
- Submit to Google Search Console + Bing Webmaster Tools.
- Reference in `robots.txt`: `Sitemap: https://example.com/sitemap.xml`

### Next.js App Router example

```ts
// app/sitemap.ts
import { MetadataRoute } from 'next'

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const [home, products] = await Promise.all([getHomePage(), getAllProducts()])
  return [
    { url: 'https://example.com/', lastModified: home.updatedAt },
    // One entry per locale URL; every entry lists all locales, itself included.
    ...products.flatMap(p => {
      const languages = { 'en': `https://example.com/en/products/${p.slug}/`, 'pt-PT': `https://example.com/pt/products/${p.slug}/` }
      return Object.values(languages).map(url => ({ url, lastModified: p.updatedAt, alternates: { languages } }))
    })
  ]
}
```

Google wants an entry for each version, each listing «every alternate version of the page, including itself» `[documented: https://developers.google.com/search/docs/specialty/international/localized-versions, 2026-10-14]`.

`lastModified` is the page's real last content change, never the build time. Change frequency and priority are left out: "Google ignores <priority> and <changefreq> values" `[documented: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap, 2026-10-11]`.

### One URL source for sitemap, IndexNow and feeds `[practitioner]`

Build the list of public URLs once — for example a `getAllPublicUrls(baseUrl)` function that returns each URL with its real `modifiedDate` — and import it from the sitemap route, the IndexNow submitter and any RSS feed. Parallel hand-kept lists drift: a page sits in the sitemap but is never pinged, or two locale lists stop matching.

### `next-sitemap`: the `autoLastmod` trap

When the sitemap comes from `iamvishnusankar/next-sitemap` instead of native `sitemap.ts` `[documented: https://raw.githubusercontent.com/iamvishnusankar/next-sitemap/master/README.md, 2026-10-12]`:

- `autoLastmod` defaults to `true` and writes the generation time (`new Date()`) — i.e. the **build time** — into every URL's `lastmod`, which teaches Google that the site's `lastmod` carries no information `[practitioner]`. Set it to `false` and pass real content dates through `transform`.
- Its defaults, `changefreq: daily` and `priority: 0.7`, are values Google ignores `[documented: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap, 2026-10-11]`.
- Put only the index sitemap in robots.txt (`includeNonIndexSitemaps: false`), `exclude` noindexed routes, and use server-side sitemaps for dynamic URLs.
- On the App Router, native `sitemap.ts` / `robots.ts` remove the dependency entirely.

### Sitemap served as HTML — worse than a 404 `[practitioner]`

**Symptom:** `/sitemap.xml` answers **200** with `Content-Type: text/html`, and the body is the home page or an i18n redirect target. The status line shows nothing wrong; GSC lists the sitemap as an HTML page or "couldn't fetch". None of its URLs are read.

**Causes:** a catch-all page route or i18n middleware matching before the sitemap handler; a geo or locale redirect that catches `/sitemap*`; a CDN rule that rewrites or strips `Content-Type`.

**Check after every deploy** (it is one of the rows in [seo-drift-monitoring.md](seo-drift-monitoring.md#deploy-gates)):

```
curl -sI https://example.com/sitemap.xml            # expect 200 + application/xml or text/xml
curl -sI -A "Googlebot" https://example.com/sitemap.xml
curl -s  https://example.com/sitemap.xml | head -3  # first bytes must be <?xml / <urlset / <sitemapindex
```

**Fix:** keep `sitemap*` (and `robots.txt`) out of the i18n/middleware matcher, e.g. Next.js `matcher: '/((?!api|_next|sitemap|robots|.*\\..*).*)'`; then resubmit the sitemap in GSC and in Bing Webmaster Tools.

### robots.txt lines that touch sitemaps and parameters `[documented: https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec, 2026-10-11]`

| Directive | Format | Wrong |
|---|---|---|
| `Disallow` / `Allow` | Root-relative path starting with `/`; case-sensitive; the longest (most specific) match wins | `Disallow: https://example.com/admin/` |
| `Sitemap` | Absolute URL; with several sitemaps, list the index | `Sitemap: /sitemap.xml` |

`Clean-param: utm_source&utm_medium&utm_campaign&gclid&fbclid` is a Yandex directive that lets its robot fold tracking-parameter duplicates into the main URL `[documented: https://yandex.com/support/webmaster/en/robot-workings/clean-param, 2026-10-11]`. Google supports only `user-agent`, `allow`, `disallow` and `sitemap` in robots.txt `[documented: https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec, 2026-10-11]`; for Google, `rel="canonical"` consolidates parameter duplicates such as `?gclid=` `[documented: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls, 2026-10-12]`.

robots.txt does not canonicalise: Google says not to use it for canonicalization, because disallowed URLs may still be indexed without their content `[documented: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls, 2026-10-12]`. A duplicate you block is never fetched, so its canonical tag cannot be read `[practitioner]`.

### Removing a URL — the status follows what replaces it `[practitioner]`

| Situation | Response |
|---|---|
| A close replacement exists, or the content was merged | 301 to that URL (not the home page by default) |
| Gone for good, no alternative | 410 |
| Gone, may return | 404 |
| Must stay reachable but out of search | `noindex`, left crawlable |
| Urgent hide while the real fix ships | GSC Removals tool — temporary only |

Before removing a page, check what it earns: clicks, backlinks, internal links and conversions. Merging it into another page often works better than deleting it. Afterwards: drop it from the sitemap, point internal links directly at the final URL rather than leaning on the redirect, make sure each redirect target is itself in the sitemap, and avoid chains. 404 vs 410 evidence (#80) and consolidation rules: [migrations-and-recovery.md](migrations-and-recovery.md#canonicals-and-indexation-repair).

## IndexNow

URL submission protocol supported by Bing, Yandex, and others. Lets you ping engines when a URL is created/updated/deleted.

```
POST https://api.indexnow.org/indexnow
Content-Type: application/json

{
  "host": "example.com",
  "key": "<your-key>",
  "keyLocation": "https://example.com/<your-key>.txt",
  "urlList": ["https://example.com/new-page/"]
}
```

Wire into your CMS or deployment pipeline. Place the key file at the documented `keyLocation` to prove ownership.

What to send and to whom:

- Send only **canonical** URLs, and send them once for each deploy; the triggers are new pages, substantive updates and deletions; minor edits do not qualify `[practitioner]`. Take them from the same URL source as the sitemap (see Sitemap.xml above).
- One submission reaches every participating engine (Bing, Yandex, Seznam, Naver and others) — check the current participant list before naming engines `[documented: https://www.indexnow.org/faq, 2026-10-11]`. Google does not take part; for Google, the sitemap and internal links are the signals.
- Up to 10,000 URLs per POST `[documented: https://www.indexnow.org/documentation, 2026-10-11]`. Make relative paths absolute before submitting `[practitioner]`.

## JS rendering — *working ≠ visible*

A site that looks perfect to a human can be an empty shell to a crawler. Googlebot queues every 200-status page for rendering «unless a robots meta tag or header tells Google not to index the page» — "The page may stay on this queue for a few seconds, but it can take longer than that"; on a `noindex` it «may skip rendering and JavaScript execution», so removing an initial `noindex` with JavaScript is not a dependable fix `[documented: https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics, 2026-10-14]` — and **most AI answer-engine crawlers don't execute JavaScript at all** — so client-rendered content is *invisible* to the very surfaces you want citations from.

Verify:
- **GSC URL Inspection** — the index check of record. `site:` is a quick check only: a site-wide `site:` search shows "a sample of pages from your site that Google knows about" `[documented: https://support.google.com/webmasters/answer/7440203, 2026-10-12]`; see [incident-triage.md](incident-triage.md#classify-the-incident-first).
- **GSC URL Inspection → Test Live URL → "Rendered HTML"** — is your content actually there? (Locally: View-Source / `curl` = first-pass HTML; DevTools Inspect = hydrated DOM. Content only in the latter may never be seen by crawlers.)
- **Critical content, `<title>`, and meta are in the server HTML**, not injected after JS.
- **Internal links are real `<a href>`**, not JS click handlers.
- **Render resources aren't blocked** — never `Disallow` your CSS/JS bundles (`/_next/`, `/static/`) in robots.txt; Googlebot must fetch them to render.

Prefer SSR / ISR / SSG over pure CSR for any page that must rank or be cited.

### Rendering is chosen per route `[practitioner]`

Whatever has to rank or be cited ships its content in the HTML.

| Route type | Strategy |
|---|---|
| Marketing, methodology, guides, static comparisons | SSG / ISR |
| Data with a known cadence (tariffs, rates) | ISR (60 s–1 h) or on-demand revalidation when the data changes |
| Personalised / geo-priced | SSR + streaming: static shell first, slow holes streamed in |
| Static page with one live widget | Partial prerender / islands — hydrate only the widget |
| Post-login workspaces | CSR acceptable; **never** on public or citation-target pages |

On money paths, links must navigate and forms must submit with JavaScript off; JS only enhances them. Each hydrated island needs a stated reason and an INP budget. Test: walk the money path with JS disabled — it completes, or the audit records FAIL.

### Caching that changes what a crawler receives `[practitioner]`

- Public HTML: `Cache-Control: public, s-maxage=60–300, stale-while-revalidate=86400, stale-if-error=86400`. ⚠️ Cloudflare standard caching ignores `stale-while-revalidate`, so prove the behaviour — stop the origin and expect a stale 200 — instead of trusting the header.
- Cache key: path plus an explicit allowlist of query parameters (plus country only if prices differ by country). **Do not vary HTML on the session cookie, `User-Agent` or an A/B cookie** — the hit ratio collapses and crawlers get a different document from users.
- **Bots and users receive the same HTML.** A different body for crawlers is what Google's spam policies call cloaking — presenting different content to users and search engines with the intent to manipulate rankings `[documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]`. Personalised parts live in private holes (streamed or fetched client-side), never inside the cached document.
- **Dynamic rendering** (a pre-rendered page for bots) is, in Google's words, «a workaround and not a recommended solution, because it creates additional complexities and resource requirements»; «As long as your dynamic rendering produces similar content, Googlebot won't view dynamic rendering as cloaking», but «completely different content to users and crawlers can be considered cloaking» `[documented: https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering, 2026-10-11]`. Serve one page to both instead.
- Content-hashed immutable assets, and **purge HTML on every deploy**: stale HTML that references deleted chunks renders a broken shell (the stale-chunk 404 class).
- `curl -I` public HTML twice: expect MISS, then HIT. No `public` on documents that vary by cookie; no `Vary: User-Agent` on HTML, except for m-dot setups that use dynamic serving (see [crawl-and-index.md](crawl-and-index.md#canonical-rules)).

### Degrade, do not blank `[practitioner]`

When a data API fails, render the last good snapshot with an age stamp ("dados das HH:MM"), not an empty `<main>`; during the outage, crawlers fetch and index precisely that empty shell. Probe: route `/api/**` → 500 and measure the text length of `main`. The dated drills and the WAF-drift alert: [seo-drift-monitoring.md](seo-drift-monitoring.md#crawler-facing-drills-and-the-waf-drift-alert).

### Raw vs rendered crawl diff `[practitioner]`

Crawl the site twice — raw HTML, then rendered — and diff title, canonical, robots meta and links. `PhialsBasement/LibreCrawl` renders with Playwright and has a PSI hook; `advertools.crawl` covers the raw side. Any field present only in the rendered DOM is invisible to crawlers that do not execute JavaScript.

### Rejected as architecture theatre `[practitioner]`

Lighthouse 100 as a gate (budgets yes, score no); a CSR single-page app for a comparison portal; SSR everything on pages that could be cached; in 2026, AMP or a separate `m.` site; HTML rendered at the edge yet cacheable for only 60 s.

## Audit checklist (run on every audit)

- [ ] Crawl with Screaming Frog / Sitebulb / equivalent
- [ ] Export all URLs; classify by type (page / asset / redirect / 4xx / 5xx)
- [ ] Check indexability per URL (robots.txt, meta robots, canonical)
- [ ] Check status codes — list all non-200s
- [ ] Map all redirects — find chains, loops, wrong destinations
- [ ] Validate canonicals — are they correct? self-referencing where appropriate?
- [ ] Check titles, meta descriptions, H1s — uniqueness, length, keyword presence
- [ ] Measure internal link depth — find orphans
- [ ] Compare sitemap vs crawl — what's in sitemap but not findable? findable but not in sitemap?
- [ ] Validate robots.txt — anything blocking that shouldn't?
- [ ] Validate structured data: syntax in a schema testing tool such as Schema Markup Validator; Rich Results Test only for features it supports ("Site names aren't supported in the Rich Results Test") `[documented: https://developers.google.com/search/docs/appearance/site-names, 2026-10-12]`
- [ ] Run Core Web Vitals (PageSpeed Insights, CrUX)
- [ ] Pull Search Console data — top queries, ranking pages, decaying pages, high-impression-low-CTR
- [ ] Identify ranking pages losing clicks (decay)
- [ ] Identify position 4-10 (improvement opportunities) and 11-20 (push to page 1)
- [ ] Compare against top competitors for target keywords
- [ ] Prioritize by impact × business value × confidence ÷ implementation difficulty

## Sources

- https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering — Dynamic rendering as a workaround, fetched 2026-10-11, saved as phase-2 sources/google/g-dynamic-rendering.raw
- installed/site-improvement@references/architecture-and-build.md, installed/site-improvement@references/execution-and-resilience.md (phase-2 adapted file research/adapted/installed__site-improvement/rendering-caching-and-crawler-parity.md) — per-route rendering table, HTML-first money paths, crawler-facing caching rules, degrade-without-blanking, architecture-theatre list (drills and WAF-drift in seo-drift-monitoring.md). INTEGRATE, in-house (no third-party licence found).
- kostja94/marketing-skills@skills/seo/technical/sitemap/SKILL.md, kostja94/marketing-skills@skills/seo/technical/indexnow/SKILL.md, kostja94/marketing-skills@skills/seo/technical/robots/SKILL.md, kostja94/marketing-skills@skills/seo/technical/indexing/SKILL.md (phase-2 adapted file research/adapted/kostja94__marketing-skills/sitemap-indexnow-ssot-and-sitemap-served-as-html.md) — one URL source, IndexNow submission rules, sitemap-served-as-HTML diagnosis, robots path-format traps, the Yandex Clean-param sentence, URL-removal table. INTEGRATE, MIT.
- iamvishnusankar/next-sitemap@README.md (phase-2 adapted file research/adapted/group-E__readme-tool-repos/tool-stack-by-job.md) — `autoLastmod` build-time trap, ignored defaults, index-only robots entry. INTEGRATE, MIT.
- PhialsBasement/LibreCrawl@README.md and eliasdabbas/advertools@README.md (phase-2 adapted file research/adapted/group-E__readme-tool-repos/tool-stack-by-job.md) — raw vs rendered crawl diff. INTEGRATE, MIT.
- coreyhaines31/marketingskills@skills/seo-audit/references/international-seo.md (phase-2 adapted file research/adapted/coreyhaines31__marketingskills/international-hreflang-delta.md) — Next.js `sitemap.ts` self-alternate and next-intl `localePrefix` caveats. INTEGRATE, MIT.
