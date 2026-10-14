# Local and Maps SEO

## Contents

- Choosing the subtype
- Required vs recommended properties
- Industry patterns worth carrying
- Multi-location pattern
- What moves the local pack — all vendor evidence
- Citations and NAP
- GBP feature status
- Measuring Maps visibility: the geo-grid
- Free data sources
- The 50-point GBP rubric
- Cross-references
- Unverified
- Sources

## Choosing the subtype

Pick the most specific Google-supported `LocalBusiness` subtype; fall back to the generic parent only when no subtype fits `[practitioner]`.

| Vertical | Use | Avoid |
|---|---|---|
| Food | `Restaurant`, `CafeOrCoffeeShop`, `BarOrPub`, `Bakery`, `FastFoodRestaurant`, `IceCreamShop` | `FoodEstablishment` when a subtype exists |
| Healthcare | `MedicalClinic`, `Hospital`, `Dentist` (all three rich-result eligible), `Physician` (with `Person`), `Optician`, `Pharmacy` | `MedicalBusiness` when a subtype exists |
| Legal | `LegalService` + `Person` | `Attorney` — **deprecated by Schema.org** |
| Home services | `Plumber`, `Electrician`, `HVACBusiness`, `RoofingContractor`, `GeneralContractor`, `HousePainter`, `Locksmith`, `MovingCompany` | `HomeAndConstructionBusiness` when a subtype exists |
| Real estate | `RealEstateAgent` for agents **and** brokerages | `RealEstateBrokerage` — no such type exists on Schema.org |
| Automotive | `AutoDealer` (sales), `AutoRepair` (service), `AutoPartsStore` (parts) | one blended listing for all three |

Google asks for the most specific `LocalBusiness` subtype possible and names `Restaurant`, `DaySpa` and `HealthClub` as examples `[documented: https://developers.google.com/search/docs/appearance/structured-data/local-business, 2026-10-12]`. Other Schema.org subtypes the source lists: `BeautySalon`, `ChildCare`, `FinancialService`, `Hotel`, `InsuranceAgency`, `PetStore`, `Store`, `TravelAgency`, `VeterinaryCare` `[practitioner]`.

## Required vs recommended properties

Per Google's LocalBusiness structured-data page `[documented: https://developers.google.com/search/docs/appearance/structured-data/local-business, 2026-10-12]`:

- **Required:** `name` and `address` as a `PostalAddress` (its example fills `streetAddress`, `addressLocality`, `addressRegion`, `postalCode`, `addressCountry`; include as many as possible).
- **Recommended:** `aggregateRating` and `review` (only for sites that capture reviews about other local businesses), `geo` (**at least 5 decimal places**), `openingHoursSpecification` (late-night, 24 h and seasonal closures are covered), `telephone`, `url`, `priceRange` (under 100 characters, or Google shows no price range), `department` for nested departments, plus `menu` and `servesCuisine` for food establishments.
- Keep `name` identical to the Google Business Profile, and `telephone` matching GBP and on-page NAP `[practitioner]`.
- **Service-area businesses:** `areaServed` is **not** among the properties on Google's LocalBusiness page `[documented: https://developers.google.com/search/docs/appearance/structured-data/local-business, 2026-10-12]`; it is a Schema.org property (`Place`/`GeoShape`) and the industry convention — use named cities with `sameAs` links to Wikipedia/Wikidata `[practitioner]`.

## Industry patterns worth carrying

- **Healthcare:** `MedicalClinic`/`Hospital`/`Dentist` at the location level; `Person` + `medicalSpecialty` + `hospitalAffiliation` + `hasCredential` on physician pages; `sameAs` to the NPI Registry and the medical board entry `[practitioner]`. HIPAA review-response rule: unverified [unverified: HHS enforcement page not readable by curl on 2026-10-12 (HTTP 403)]; see ## Unverified. In the EU the constraint to check is GDPR Art. 9 health data, not HIPAA `[practitioner]`.
- **Legal:** `LegalService`, never `Attorney`; `makesOffer > Service`, one per practice area. Reviews follow the practitioner listing when an attorney changes firms `[practitioner]`.
- **Automotive:** **`VehicleListing` rich results are retired** — phase-out announced 12 June 2025, documentation removed 9 September 2025 because the type is "no longer shown in Google Search results" `[documented: https://developers.google.com/search/updates, 2026-10-11]` — use `Car` + `Offer`.
  Merchant Center vehicle feeds: unverified [unverified: no Merchant Center vehicle-listings page saved on 2026-10-12]; see ## Unverified.
  The full deprecated-type timeline lives in skill `seo-technical` › schema-reference.
- **Restaurants:** `ReserveAction` and `OrderAction` are machine-readable data only, not Google-supported rich results; Google Food Ordering direct checkout was discontinued in June 2024 `[practitioner — no primary URL in source]`.

## Multi-location pattern

One `Organization` on the homepage with a stable `@id`; one `LocalBusiness` subtype per location page, each with its own `@id`, and `branchOf` pointing at the organization's `@id` `[practitioner]`:

```json
{ "@context":"https://schema.org", "@type":"Organization",
  "@id":"https://example.com/#org", "name":"Brand", "url":"https://example.com" }

{ "@context":"https://schema.org", "@type":"Dentist",
  "@id":"https://example.com/locations/downtown/#location",
  "name":"Brand — Downtown",
  "branchOf":{"@id":"https://example.com/#org"},
  "address":{ "...": "..." },
  "geo":{"latitude":"40.71234","longitude":"-74.00567"},
  "telephone":"+1-555-123-4567" }
```

Subdirectory URLs (`domain.com/locations/city-name/`) over subdomains `[practitioner]`. The source attaches a "50%+ traffic lift" to a Bruce Clay study with no sample size — **do not quote that figure** `[vendor, no denominator published]`.

## What moves the local pack — all vendor evidence

No engine documentation ranks local factors. Everything below is survey or model output; publish the source beside the number or do not publish the number.

- **Whitespark 2026 Local Search Ranking Factors**, published 6 Nov 2025, **47 experts surveyed across 187 factors** `[vendor]`: GBP signals 32% of local-pack factor weight; review signals ~20% (up from ~16% in 2023); on-page ~15–19%; link signals declining; behavioural/engagement rising; social signals and AI-search signals measured for the first time. The individual factors are expert-assigned scores, not measurements: primary GBP category (193), keywords in the GBP business title (181), proximity of address to the search point (176). **Top negative factor: an incorrect primary category (176)** — the single worst listing mistake — followed by duplicate profiles at the same address (142).
- **Search Atlas ML study, August 2025** `[vendor]`: an XGBoost regression explaining 92–93% of observed ranking variance attributes 55.2% of that variance to proximity, 19.2% to review count, 5.9% to domain power, 5.3% to semantic relevance in review text, everything else under 5% each. Read it as: **most of what a client can control sits inside the ~45% that is not proximity.**
- **Sterling Sky review findings, 2025** `[vendor]`: a "Magic 10" threshold — a noticeable lift moving from 9 to 10 reviews, none from 10 to 11 — and an "18-day rule", rankings falling sharply after ~3 weeks with no new review. Velocity over volume. Neither has a published sample size.
- **BrightLocal LCRS 2026 (Feb 2026)** `[vendor — respondent count not published in the source file; verify before quoting]`: 74% of surveyed consumers say only reviews from the last 3 months matter; 41% "always" read reviews (29% in 2025); 68% use only 4+ star businesses (55% in 2025); Google's share of review-platform usage 71% (83% in 2025) while Apple Maps rose to 27% (14% in 2025). The same survey is the source of the "45% use AI for local recommendations, up from 6%" figure quoted at `skills/seo-local/SKILL.md:31` — **survey self-report, not measured behaviour.**

## Citations and NAP

Citations are declining as a local-pack factor but the Whitespark 2026 panel places **3 of the top 5 AI-visibility factors in the citation group** `[vendor]`. Google's local-ranking help page now describes prominence through how many websites link to the business and its reviews and ratings, and does not mention directories `[documented: https://support.google.com/business/answer/7091, 2026-10-12]`.
Directories removal date: unverified [unverified: no saved page dates the change to July 2025]; see ## Unverified.

Practical check `[practitioner]`: extract NAP from three places — visible page HTML, the `LocalBusiness` JSON-LD, and any visible GBP data — and flag every discrepancy between them. Probe presence with `site:` absence checks (`site:yelp.com "Business Name"`, `site:bbb.org "Business Name"`); **an empty `site:` result is weak evidence of absence, not proof** — confirm on the directory's own search before reporting a missing citation.

Tier 1: Google Business Profile, Apple Business, Bing Places (overhauled Oct 2025; feeds Copilot and other assistants), Facebook, Yelp. Tier 2: BBB, YellowPages, Manta, Superpages, Foursquare, Nextdoor. Tier 3 aggregators that redistribute downstream: Data Axle, Foursquare, Neustar/TransUnion `[vendor]`. The source's Apple Business platform-relaunch claims are flagged inside the source itself as TechRadar-sourced and unverified against Apple — treat them the same way.

## GBP feature status

GBP feature removals: unverified [unverified: no Google Business Profile help page saved on 2026-10-12]; see ## Unverified. **Recheck the live primary source before advising redirects** `[practitioner]`.

Active: Q&A (category/region limited), Posts with scheduling, services menu, attributes, photos/video, Local Lists, AI "Suggest Description". Google Verified badge: unverified [unverified: the source file gives no citation and no Google page was saved]; see ## Unverified.

Two useful negatives `[vendor]`: GBP Posts have **no direct ranking impact** (WebFX empirical testing) though they can trigger Post Justifications; photo **geotagging has no impact**, and the benefit of photos appears to be "some vs none", not more vs many. A third `[vendor]`: do not point the GBP website link at the site's strongest page — Sterling Sky's Diversity Update work suggests it risks suppressing that page's organic ranking.

## Measuring Maps visibility: the geo-grid

Simulate Maps searches from a lattice of coordinates around the business and read the rank at each point `[practitioner]`. Grid generation, Haversine-flattened:

```
step_km = (2 * radius_km) / (grid_size - 1)
center_index = (grid_size - 1) / 2
dy = (i - center_index) * step_km ;  dx = (j - center_index) * step_km
lat = center_lat + dy / 111.32
lng = center_lng + dx / (111.32 * cos(center_lat * pi/180))
```

Grid sizing: 3×3 (9 points, ~2 km) for a snapshot; **7×7 (49 points, ~5 km) as the default**; 9×9 (81, ~8 km) for wide service areas; 13×13 (169, ~15 km) rural. Radius guidance: dense urban 2–5 km, suburban 5–10 km, rural 10–25 km. The per-keyword costs in the source ($0.018 at 3×3 up to $0.338 at 13×13) are DataForSEO live-mode prices as of the file's March 2026 date — **re-price before quoting a client** `[vendor]`.

Share of Local Voice = `points_in_top_3 / total_grid_points × 100`. The five interpretation bands (80–100 dominant, 60–79 strong, 40–59 moderate, 20–39 weak, 0–19 critical) are **`[unvalidated house heuristic]`** — invented cut-points with no study behind them; report the raw ratio (e.g. "28 of 49 grid points in the top 3") and let the band be commentary. The ASCII heatmap at `maps-geo-grid.md:96-140` is a fine terminal output format: rank digits per cell, `[1]` marking the centre, `-` for not ranked, with SoLV, average rank and weakest quadrant on the footer line.

## Free data sources

- **Overpass API** (`https://overpass-api.de/api/interpreter`) — competitor POI discovery by tag and radius. Usage guideline for the main instance: under 10,000 queries and 1 GB of data a day **and no more than 10 minutes of total processing time** for one-off use, a hundredth of those numbers for regular use, counted across all users of an app; a `User-Agent` or `Referer` that identifies the app; no parallel scripts; commercial use on self-hosted or paid servers; default query timeout 3 minutes `[documented: https://wiki.openstreetmap.org/wiki/Overpass_API, 2026-10-12]`. Set `[timeout:25]`; OSM data is ODbL, attribute OpenStreetMap; no reviews, ratings or GBP data; coverage is strong in Europe `[practitioner]`.
- **Geoapify Places** — free plan 3,000 credits/day, every 20 places cost 1 credit, API key required, results may be cached and stored with no limits, GeoJSON output, dot-separated categories `[documented: https://apidocs.geoapify.com/docs/places/, 2026-10-12]`; free plan up to 5 requests/second `[documented: https://www.geoapify.com/pricing/, 2026-10-12]`.
- **Nominatim** (public instance) — geocoding only: **1 request/second at most**, a `User-Agent` or `Referer` that identifies the application, auto-complete and systematic queries (including reverse queries in a grid) forbidden, bulk geocoding discouraged (small one-time jobs only, single thread, results cached), repeated identical queries may be blocked `[documented: https://operations.osmfoundation.org/policies/nominatim/, 2026-10-12]`. Use it to resolve the geo-grid centre point only, never to discover businesses `[practitioner]`.

## The 50-point GBP rubric

`skills/seo/references/maps-gbp-checklist.md:16-118` scores a GBP on 50 points (2 = present and optimised, 1 = present, 0 = missing) across critical fields, then applies per-industry multipliers (×2 photos for real estate, ×2 products for automotive) and re-normalises to 0–100. **The point values, the multipliers and the 90-100/…/rating bands are all `[unvalidated house heuristic]`** — nobody measured that a missing `priceRange` costs 2 points or that photos are worth double in real estate. The *field inventory* is useful as a completeness checklist; the *score* is not a finding. If you emit it, print the weights next to the number.

## Cross-references

- skill `seo-technical` › rendering-and-sitemaps — the JSON-LD baseline (Organization, WebSite, BreadcrumbList) and the obsolete `SearchAction`; do not restate it here.
- skill `seo-technical` › schema-reference — the full deprecated-type timeline (`VehicleListing`, `HowTo`, `SpecialAnnouncement`, `FAQPage`) and the replacement decision table.
- [comparison-pages-2.md › rollout gates](comparison-pages-2.md#rollout-gates) — location-page rollout gates for programmatic local pages.
- skill `seo-evidence` › evidence-and-tactics-1 — how to weigh a vendor survey against a controlled test.

## Unverified

- HIPAA review-response rule: a US healthcare provider's review response cannot confirm or deny that the reviewer was a patient; the source cites a $30,000 settlement (Manasa Health Center, 2023) [unverified: HHS enforcement page not readable by curl on 2026-10-12 (HTTP 403)]
- Merchant Center vehicle feeds: feed-based Vehicle Listings via Merchant Center still function after the `VehicleListing` rich-result retirement [unverified: no Merchant Center vehicle-listings page saved on 2026-10-12]
- Directories removal date: Google's July 2025 documentation update removed "directories" from the prominence definition [unverified: no saved page dates the change to July 2025]
- GBP feature removals: GBP messaging/chat; call history/tracking (31 Jul 2024); school reviews/ratings (30 Apr 2025); GBP-hosted websites listed by the source as "historically reported; unverified in this run" [unverified: no Google Business Profile help page saved on 2026-10-12]
- Google Verified badge: the source says a Google Verified badge replaced Guaranteed/Screened in October 2025; confirm before telling a client to pursue it [unverified: the source file gives no citation and no Google page was saved]

## Sources

- claude-seo@skills/seo/references/local-schema-types.md:8-71, 75-107, 110-166, 193-219 — subtype table, property requirements, industry patterns, multi-location pattern; provenance only (a repo transcription is not a primary read) — the body labels each property list and convention.
- claude-seo@skills/seo/references/local-seo-signals.md:13-52, 55-67, 69-101, 104-129, 132-152 — Whitespark 2026, Search Atlas ML, review benchmarks, citation tiers, GBP feature status; all carried as `[vendor]`.
- claude-seo@skills/seo/references/maps-geo-grid.md:13-42, 68-93, 96-140 — grid maths and cost table `[practitioner]`/`[vendor]`; SoLV bands `[unvalidated house heuristic]`.
- claude-seo@skills/seo/references/maps-free-apis.md:11-67, 71-104, 107-143 — Overpass, Geoapify, Nominatim limits (provenance only; the body labels each limit from the provider's own page).
- claude-seo@skills/seo/references/maps-gbp-checklist.md:16-118 — field inventory kept, scoring carried as `[unvalidated house heuristic]`.
- claude-seo@skills/seo-local/SKILL.md:31, 92, 151-169 — BrightLocal AI-usage figure `[vendor]`, Google Verified badge `[unverified]`, NAP/citation check procedure `[practitioner]`.
- Not imported: the "43% CTR increase (Webstix case study)" and "50%+ traffic lift (Bruce Clay)" figures at `local-schema-types.md:4` and `:217` — no denominator published.
