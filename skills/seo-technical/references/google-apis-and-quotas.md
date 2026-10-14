# Google APIs and quotas
<!-- split-header: part 1 of 2 of google-apis-and-quotas.md (step-3 original lines 1–118; boundary start) -->
<!-- /split-header -->

## Contents

- GSC Search Analytics — query shape
- URL Inspection API — verdict vocabulary
- Indexing API — narrower than everyone thinks
- GA4 Data API — token quotas, not request quotas
- DMA and Consent Mode v2 — the EU measurement boundary
- CrUX and PageSpeed Insights — field fields and nulls
- Unverified

Other parts of the same original file: [google-apis-and-quotas-2.md](google-apis-and-quotas-2.md).

## GSC Search Analytics — query shape

`POST https://www.googleapis.com/webmasters/v3/sites/{siteUrl}/searchAnalytics/query` `[documented: https://developers.google.com/webmaster-tools/v1/searchanalytics/query, 2026-10-12]`.

| Field | Values that matter |
|---|---|
| `dimensions` | `query`, `page`, `country`, `device`, `date`, `searchAppearance` |
| `type` | `web` (default), `image`, `video`, `news`, `discover`, `googleNews` |
| `aggregationType` | `auto` (default), `byPage`, `byProperty`, `byNewsShowcasePanel` |
| `rowLimit` | 1–25,000 (default 1,000) |
| `startRow` | pagination offset (default 0) |
| `dataState` | `final` (default), `all`, `hourly_all` |

`[documented: https://developers.google.com/webmaster-tools/v1/searchanalytics/query, 2026-10-12]` (the page also lists `hour` as a groupable dimension)

Three things that bite in practice:

- **`searchAppearance` works as a dimension and as a filter** — you can filter by it «even if you are not grouping by that dimension» `[documented: https://developers.google.com/webmaster-tools/v1/searchanalytics/query, 2026-10-14]`. It separates rich-result impressions from plain blue links; a CTR "collapse" is often a surface-mix change visible only once you split on it.
- **`dataState: "final"` is the default, so recent days are missing rather than low**. Use `all` for fresh-but-unsettled rows, `hourly_all` for hourly data grouped by `hour` `[documented: https://developers.google.com/webmaster-tools/v1/searchanalytics/query, 2026-10-12]`. Comparing a `final` window against an `all` window manufactures a fake decline.
- **`aggregationType: byPage` changes the denominator.** The response echoes `responseAggregationType`; read it back rather than assuming your request was honoured `[documented: https://developers.google.com/webmaster-tools/v1/searchanalytics/query, 2026-10-12]`.

### Dimension filters and the regex ceiling

`dimensionFilterGroups` takes groups of `{dimension, operator, expression}`. Operators: `contains`, `equals`, `notContains`, `notEquals`, `includingRegex`, `excludingRegex`. Regex is **RE2 syntax**; a filter is max 4,096 characters `[documented: https://developers.google.com/webmaster-tools/v1/searchanalytics/query, 2026-10-12]`.

Two consequences `[practitioner]`: RE2 has no backreferences and no lookaround, so a Perl-style brand-exclusion pattern is rejected rather than silently mis-matching; and a generated alternation (one term per brand variant) hits 4,096 characters faster than expected — split into several `excludingRegex` filters in one group. skill `seo-content` › keyword-research-1 owns the mining workflow this syntax serves.

## URL Inspection API — verdict vocabulary

`POST https://searchconsole.googleapis.com/v1/urlInspection/index:inspect` `[documented: https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect, 2026-10-12]`.

- `indexStatusResult.verdict`: `PASS` (Valid), `FAIL` (Error/Invalid), `NEUTRAL` (Excluded), `VERDICT_UNSPECIFIED`; `PARTIAL` is reserved and no longer in use
- `robotsTxtState`: `ALLOWED`, `DISALLOWED`
- `indexingState`: `INDEXING_ALLOWED`, `BLOCKED_BY_META_TAG`, `BLOCKED_BY_HTTP_HEADER`
- `pageFetchState`: `SUCCESSFUL`, `SOFT_404`, `BLOCKED_ROBOTS_TXT`, `NOT_FOUND`, `ACCESS_DENIED`, `SERVER_ERROR`, `REDIRECT_ERROR`, `ACCESS_FORBIDDEN`, `BLOCKED_4XX`, `INTERNAL_CRAWL_ERROR`, `INVALID_URL`
- `googleCanonical` vs `userCanonical` — the pair that proves a canonical override; `crawledAs`: `DESKTOP` / `MOBILE`

`[documented: https://developers.google.com/webmaster-tools/v1/urlInspection.index/UrlInspectionResult, 2026-10-12]`

`richResultsResult` returns a verdict plus `detectedItems` grouped by `richResultType` `[documented: https://developers.google.com/webmaster-tools/v1/urlInspection.index/UrlInspectionResult, 2026-10-12]`. **Do not expect FAQPage or HowTo** — FAQ rich results stopped appearing on 2026-05-07 `[documented: https://support.google.com/webmasters/answer/6211453, 2026-10-12]`; How-to rich results stopped showing in 2023 `[documented: https://developers.google.com/search/blog/2023/08/howto-faq-changes, 2026-10-11]`.

Rate limits: **2,000 QPD / 600 QPM per site**, 10,000,000 QPD / 15,000 QPM per project `[documented: https://developers.google.com/webmaster-tools/limits, 2026-10-12]`. The per-site day cap binds first on a real audit — inspect a sample and let the sitemap/coverage report carry the rest `[practitioner]`.

## Indexing API — narrower than everyone thinks

**The Indexing API is scoped to URLs carrying `JobPosting` or `BroadcastEvent` embedded in `VideoObject` structured data, and nothing else** `[documented: https://developers.google.com/search/apis/indexing-api/v3/quickstart, 2026-10-12]`. The page says it «can only be used to crawl pages with» those types; it documents nothing for ordinary pages, so do not submit them. For a handful of ordinary URLs use URL Inspection; for many, use sitemaps.

This corrects the commonest misconception in the "get my page indexed faster" genre: a tool selling "instant indexing" for a blog or catalogue via this API is using it outside its documented scope. The general-purpose equivalent for non-Google engines is IndexNow — `rendering-and-sitemaps-2.md#indexnow`.

Quotas `[documented: https://developers.google.com/search/apis/indexing-api/v3/quota-pricing, 2026-10-12]`:

| Limit | Value | Scope |
|---|---|---|
| Publish requests | 200/day (default) | Per project |
| Read-only requests | 180/min | Per project |
| Total requests | 380/min | Per project |

Auth: service account with scope `…/auth/indexing`, holding **Owner** on the GSC property `[documented: https://developers.google.com/search/apis/indexing-api/v3/prereqs, 2026-10-12]` — a higher bar than read-only pulls need, so do not reuse one service account across both unless you accept granting Owner for a read workload `[practitioner]`.

## GA4 Data API — token quotas, not request quotas

GA4 meters in **tokens**, so "how many calls can I make" has no fixed answer. Core quotas for a standard property (Analytics 360 limits are higher) `[documented: https://developers.google.com/analytics/devguides/reporting/data/v1/quotas, 2026-10-12]`:

| Quota | Limit | Scope |
|---|---|---|
| Core tokens per day | 200,000 | Per property |
| Core tokens per hour | 40,000 | Per property |
| Core tokens per hour | 14,000 | Per project per property |
| Concurrent requests | 10 | Per property |
| Server errors per hour | 10 | Per project per property |

Realtime and Funnel requests have their own quotas of the same size. Most requests charge 10 or fewer tokens; more complex ones charge more. Set `returnPropertyQuota: true` and read consumption back from the response rather than estimating. Each request charges both hourly quotas, so the per-project-per-property one (14,000) runs out first unless more than 3 projects share the property `[documented: https://developers.google.com/analytics/devguides/reporting/data/v1/quotas, 2026-10-12]`.

GA4 date ranges per request: unverified [unverified: the limit of 4 date ranges per request is not on the saved Data API quotas page]; see ## Unverified.

### The *AI Assistants* channel caveat

GA4's default channel group has an **AI Assistant** channel: sources like **ChatGPT, Gemini, Deepseek, Copilot or Grok**; the medium is set to `ai-assistant` when the referrer matches Google's list of AI assistants. It **excludes Google AI Overviews and AI Mode**, which count under Organic Search `[documented: https://support.google.com/analytics/answer/9756891, 2026-10-12]`.

GA4 AI Assistant channel launch: unverified [unverified: the ~2026-05-13 launch date, Claude as a listed source, and forward-only with no backfill are not on the saved channel-group page]; see ## Unverified.

The channel **undercounts AI traffic structurally**, three ways `[practitioner]`: unsupported sources (Perplexity among them) may stay in Referral and need separate verification; most AI sessions arrive referrer-less and land in **Direct**; and AI Overviews/AI Mode — the largest AI surface for a Google-dependent site — is excluded by definition. A rising *AI Assistants* line is evidence of AI referral; a flat or absent one is **not** evidence of its absence. Never use this channel as the denominator in an "AI traffic share" claim. Before a before/after that might straddle the channel's start, find the first date the property's own data shows AI Assistant sessions; the launch date and backfill are unverified (see ## Unverified) `[unvalidated house heuristic]`. skill `seo-evidence` › experiments-and-revert-2 owns what a legitimate before/after looks like.

## DMA and Consent Mode v2 — the EU measurement boundary

Consent mode was updated in November 2023 with two more parameters, `ad_user_data` and `ad_personalization`; Google tells existing users to upgrade to consent mode v2 as it strengthens enforcement of its EU user consent policy `[documented: https://developers.google.com/tag-platform/security/guides/consent, 2026-10-12]`.

DMA boundary date: unverified [unverified: the Digital Markets Act date 2024-03-07 and its limits on Google's use of behavioural data are not on any saved page; EUR-Lex not readable by curl on 2026-10-12]; see ## Unverified. Operationally:

- **EU before/after across 2024-03-07 (DMA) or a consent-mode change: check before comparing.** Compare Search Console CTR only if the consent setup and measurement were the same in both windows; otherwise compare clicks, or keep both windows on one side of the change `[unvalidated house heuristic]`. No saved primary source states a CTR effect at that date. For a Portuguese property the check applies to essentially all the traffic.
- **GA4 organic reports under-report EU users who decline analytics cookies**: Analytics is missing data for them. Behavioral modeling estimates them only once the property is eligible (at least 1,000 events per day with `analytics_storage='denied'` for at least 7 days), and reports that include modeled data show higher user counts than observed-only ones `[documented: https://support.google.com/analytics/answer/11161109, 2026-10-12]`.

What to do `[practitioner, per the repo's own instruction]`: attach the diagnostic note to any EU GSC pull; surface the consent configuration when pulling GA4 organic, and if the property denies `ad_storage` by default note that counts are conservative and modelled uplift may apply; check Consent Mode v2 is wired before any pageview (`gtag('consent', 'default', …)`) and that `ads_data_redaction` is set on EU traffic. Do **not** turn this into cookie-consent UX advice — legal/engineering, outside the SEO perimeter.

**Combined effect, worth stating once to a stakeholder** `[unvalidated house heuristic]`: on an EU property, check two dates before reading a trend line — 2024-03-07 (DMA; a break only if consent setup or measurement changed across it, per the check above) and the first date the property's own data shows the GA4 AI Assistant channel (its launch date is unverified; see the section above). A trend line crossing either date is not comparable until that check is done.

## CrUX and PageSpeed Insights — field fields and nulls

CrUX record metrics worth knowing by name `[documented: https://developer.chrome.com/docs/crux/api, 2026-10-12]`:

- `largest_contentful_paint` (ms), `interaction_to_next_paint` (ms), `cumulative_layout_shift` — **CLS is a double encoded as a string**, parse it, don't assume a float.
- LCP subparts: `largest_contentful_paint_resource_type` (fractions), `..._image_time_to_first_byte`, `..._image_resource_load_delay`, `..._image_resource_load_duration`, `..._image_element_render_delay`. They were added to the CrUX API in the January 2025 release, published 2025-02-11 — which is why sources date them both January and February 2025 `[documented: https://developer.chrome.com/docs/crux/release-notes, 2026-10-12]`. What the subparts mean is in `performance-images-and-sitemaps-1.md#lcp-subparts`.
- `first_contentful_paint`, `experimental_time_to_first_byte`, `round_trip_time`, `navigation_types` (fractions), `form_factors` (fractions). The same January 2025 release added RTT to the API and retired the ECT dimension from BigQuery, with RTT as its replacement `[documented: https://developer.chrome.com/docs/crux/release-notes, 2026-10-12]`.

CrUX null handling: unverified [unverified: the string "NaN" for densities and null for percentiles in ineligible periods are not on the saved CrUX API page]; see ## Unverified. A naive cast turns `"NaN"` into a real NaN that propagates through an average, or into `0` under a permissive parser — which reads as a perfect score; check for both before any numeric operation `[practitioner]`.

CrUX API data is a **28-day rolling average**, updated **daily around 04:00 UTC** on a best-effort basis `[documented: https://developer.chrome.com/docs/crux/api, 2026-10-12]`. A fix shipped today cannot fully appear for about four weeks, and a partial improvement at week two is a mixed window, not a plateau `[practitioner]`. skill `seo-optimizer` › audit-output-and-templates owns the fallback ladder for URLs with no CrUX eligibility at all.

## Unverified

- GSC hourly data launch: `dataState: "hourly_all"` shipped in April 2025 [unverified: the saved Search Analytics query page documents the value but gives no launch date]
- GA4 date ranges per request: a Data API request accepts up to 4 date ranges [unverified: the limit of 4 date ranges per request is not on the saved Data API quotas page]
- GA4 AI Assistant channel launch: the channel went live around 2026-05-13, recognises Claude, and is forward-only with no backfill [unverified: the ~2026-05-13 launch date, Claude as a listed source, and forward-only with no backfill are not on the saved channel-group page]
- DMA boundary date: EU traffic through Google Search has been subject to the Digital Markets Act since 2024-03-07, which limits Google's use of behavioural data and drives Consent Mode v2 for GA4 and Ads in the EU [unverified: the Digital Markets Act date 2024-03-07 and its limits on Google's use of behavioural data are not on any saved page; EUR-Lex not readable by curl on 2026-10-12]
- CrUX null handling: in ineligible periods CrUX returns the string "NaN" for densities and null for percentiles [unverified: the string "NaN" for densities and null for percentiles in ineligible periods are not on the saved CrUX API page]

