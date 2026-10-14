# Schema reference — what is dead, what is new, what to ship

## Contents

- Deprecated types — timeline
- Replacement decision table
- Additions, 2023–2026
- Live types and library traps (next-seo)
- Shapes: required fields by type
- JSON-LD escaping
- A static check worth running (not a hook to install)
- Cross-references
- Sources

## Deprecated types — timeline

Retirement dates, from Google's 2023 HowTo/FAQ post `[documented: https://developers.google.com/search/blog/2023/08/howto-faq-changes, 2026-10-11]`, its 2025-06-12 "Simplifying the search results page" post `[documented: https://developers.google.com/search/blog/2025/06/simplifying-search-results, 2026-10-12]` and its documentation-updates log `[documented: https://developers.google.com/search/updates, 2026-10-11]`. The 2025 post says the change does not affect ranking. Row notes marked "repo" come from the source repo and are not in those pages:

| Type | Status date | What happened |
|---|---|---|
| `HowTo` | **September 2023** | Rich result removed, desktop and mobile. Vocabulary survives, produces no Google effect. |
| `FAQPage` | **August 2023** restricted to gov/health; **7 May 2026** fully retired | Rich results retired for all sites, superseding the 2023 restriction. FAQ docs removed 2026-06-15. |
| `VehicleListing` | **12 June 2025** (phase-out announced) | Docs removed 2025-09-09. Repo: dealer-inventory rich cards no longer render. |
| `ClaimReview` | **12 June 2025** | Phased out of Search results; Google says use outside Google Search is not affected. |
| `EstimatedSalary` | **12 June 2025** | Docs removed 2025-09-09. Repo: `JobPosting` is unaffected. |
| `LearningVideo` | **12 June 2025** | Docs removed 2025-09-09. Repo: generic `VideoObject` rich result still renders. |
| `Course Info` | **12 June 2025** | Docs removed 2025-09-09. Repo: only the carousel died and the single-result `Course` card is live — ask which one the user means. |
| `Book Actions` | listed **12 June 2025**; banner removed **5 Nov 2025** | Google removed the deprecation banner because a feature still uses the markup. |
| `SpecialAnnouncement` | **31 July 2025** | Deprecated from that date; docs removed 2025-09-09. No replacement. |
| `PracticeProblem` | deprecation notice **5 Nov 2025**; tooling removed from **January 2026** | Rich Results Test, Search Console reporting and appearance filters dropped; docs removed January 2026. |

All five June-2025 retirements are announced at `developers.google.com/search/blog/2025/06/simplifying-search-results`; `HowTo`/`FAQ` at `.../2023/08/howto-faq-changes`; the FAQ retirement at `.../docs/appearance/structured-data/faqpage`.

**Tooling-removal timeline — do not send anyone to a dead validator.** For Course Info, Claim Review, Estimated Salary, Learning Video, Special Announcement and Vehicle Listing, Google removed support from Search Console rich-result reporting, the Rich Results Test and the Search appearance filters starting **9 September 2025**; the Search Console API kept them through December 2025 `[documented: https://developers.google.com/search/blog/2025/06/simplifying-search-results, 2026-10-12]`. (The source repo dated this removal January 2026, which is the PracticeProblem date.) An audit that tells a client to "validate this in the Rich Results Test" for one of these is telling them to check a surface that no longer exists.

**`Dataset` is the counter-example: not discontinued.** On 2025-11-05 Google clarified that Dataset markup is only used by Dataset Search, not Google Search, while phasing the type out of Google Search results `[documented: https://developers.google.com/search/updates, 2026-10-11]`; its Dataset page still describes how datasets appear in Dataset Search `[documented: https://developers.google.com/search/docs/appearance/structured-data/dataset, 2026-10-12]`. Keep it for Dataset Search; promise nothing for web Search.

## Replacement decision table

When a user asks for a dead type, answer with the substitute rather than the refusal `[practitioner]`:

| Asked for | Ship instead |
|---|---|
| `ClaimReview` | Nothing equivalent. `Article` with `dateline` if the context is news. |
| `EstimatedSalary` | `JobPosting` with `baseSalary` for a specific role. |
| `LearningVideo` | `VideoObject` (live). |
| `Course Info` carousel | Single `Course` rich card (live). |
| `SpecialAnnouncement` | `Event` if time-bounded, otherwise `Article` / `WebPage`. |
| `VehicleListing` | `Product` with vehicle-specific properties (`Car` + `Offer` for a dealer listing). |
| `HowTo` for SERP benefit | Nothing. If the goal is comprehension, use clear `<h2>` step headings — the ranking benefit was never schema-driven. |
| `FAQPage` for SERP benefit | Nothing. Keep existing markup only where it accurately describes visible FAQ content; use `QAPage` for genuine user-submitted Q&A. |

Two disciplines from the source worth keeping `[practitioner]`: flag an existing `FAQPage` as **Info, not Critical** — unsupported types do not cause errors, so stripping them is busywork; and treat "but AI engines still read it" as **unconfirmed** for both `HowTo` and `FAQPage`. No published measurement supports it.

## Additions, 2023–2026

Dates as recorded in the source repo's schema-types file `[practitioner]`; the rows for `DiscussionForumPosting`, `ProductGroup`, `ProfilePage`, Product Certification, organization-level shipping policies, comment-thread properties, `hasAdultConsideration`, `Product.category` and sale duration match Google's documentation-updates log `[documented: https://developers.google.com/search/updates, 2026-10-14]`. Dates are when Google documented support, not when schema.org added the vocabulary:

| Type / feature | Added | Note |
|---|---|---|
| `DiscussionForumPosting` | November 2023 | Forum and community content. |
| `Speakable` | updated 2024 | Voice surfaces. |
| **Product Certification** (`hasCertification`) | **April 2025** | Energy ratings, safety marks. Replaced `EnergyConsumptionDetails`. |
| **`ProductGroup`** | February 2024 | Product-variant documentation; variant grouping via `variesBy` / `hasVariant`. |
| **`ProfilePage`** | November 2023 | Author/creator pages, `mainEntity` a `Person`; the structured half of an E-E-A-T author signal. |
| `LoyaltyProgram` | June 2025 | Member pricing. |
| Organization-level shipping/return policies | November 2025 | Configured in Search Console, no Merchant Center needed. |
| `ConferenceEvent`, `PerformingArtsEvent` | December 2025 | Schema.org v29.4. |
| QAPage / DiscussionForumPosting comment-thread properties | 2026-03-24 | Comment-thread structure. |
| `hasAdultConsideration` | **2026-05-20** | Required for adult-oriented products; Google Search supports only `https://schema.org/SexualContentConsideration`. |
| `Product.category` multi-type | **2026-07-07** | Accepts `Text`, `CategoryCode`, or arrays mixing both; use Google's taxonomy URL with `codeValue`. |
| Offer sale duration | **2026-07-07** | `validFrom` plus `validThrough` or `priceValidUntil`, ISO 8601. |
| Education Q&A (`Quiz`, `eduQuestionType=Flashcard`) | 2026 | Live rich result; carousel expanded to more languages. |

E-commerce requirement worth singling out: `returnPolicyCountry` is **required** for `MerchantReturnPolicy` (Google's documentation changelog, March 2025) `[documented: https://developers.google.com/search/updates, 2026-10-11]`.

## Live types and library traps (next-seo)

**A type being in the schema.org vocabulary tells you nothing about whether Google does anything with it** `[practitioner]`. The vocabulary grows with each monthly release; Google's supported set is a separate, smaller list, so confirm each type on its Search Central page before promising an effect.

`garmeeh/next-seo` ships ready Next.js components for live types: `Product`, `MerchantReturnPolicy`, `MemberProgram` (loyalty), `DiscussionForumPosting`, `ProfilePage`, `VacationRental`, `Event`, `JobPosting`. Its README also carries four stale claims — treat each as a trap, not as guidance:

| next-seo claim | Status |
|---|---|
| `HowToJsonLd` "can help … appear as rich results" (README:670) | HowTo rich result retired September 2023 |
| `FAQJsonLd` limited to government/health sites (README:2573) | FAQ rich results gone for every site since 7 May 2026 |
| `ClaimReviewJsonLd` (README:228) | Retired 12 June 2025 |
| Course-list carousel (README:2281, 2412) | Carousel retired 12 June 2025; the single `Course` card is still live |

## Shapes: required fields by type

Eleven types carried from the source template library, reduced to their load-bearing fields. Anything marked *required* is required for the rich result, not merely conventional `[practitioner — the template file itself carries no per-field Google citation; verify required-field lists against the type's Search Central page before shipping]`.

| Type | Required | Commonly needed |
|---|---|---|
| `VideoObject` | `name`, `description`, `thumbnailUrl`, `uploadDate` | `duration` (ISO 8601), `contentUrl`, `embedUrl`, `publisher` |
| `BroadcastEvent` | a `VideoObject` carrying `publication` with `isLiveBroadcast: true`, `startDate` | `endDate` — drives the LIVE badge |
| `Clip` | `hasPart[]` on a `VideoObject`; each clip needs `name`, `startOffset`, `url` | `endOffset` — drives key-moments |
| `SeekToAction` | `potentialAction.target` with `{seek_to_second_number}`, plus `startOffset-input: "required name=seek_to_second_number"` | — |
| `SoftwareSourceCode` | `name`, `codeRepository` | `programmingLanguage`, `runtimePlatform`, `author`, `license`, `dateCreated`/`dateModified` |
| `ProductGroup` | `name`, `productGroupID`, `variesBy[]`, `hasVariant[]` | each variant: `sku`, the varying properties, `offers` |
| `ProfilePage` | `mainEntity` (`Person` or `Organization`) with `name` | `url`, `description`, `sameAs[]` |
| `Certification` | `hasCertification.certificationIdentification`, `issuedBy` | attach to the `Product` |
| `OfferShippingDetails` | `shippingRate` (`MonetaryAmount`), `deliveryTime` with `handlingTime` + `transitTime` (`QuantitativeValue`, `unitCode: "DAY"`) | — |
| `Product` (full) | Snippet: `name` plus one of `review`, `aggregateRating`, `offers`; if using `offers`, each `Offer` needs `price` or `priceSpecification.price`; `priceCurrency` is required only for merchant listings `[documented: https://developers.google.com/search/docs/appearance/structured-data/product-snippet, 2026-10-14]` | `image`, `offers` with `price`, `priceCurrency`, `availability`, `sku`, `brand`, `category`, `priceValidUntil`, `hasMerchantReturnPolicy` (incl. `returnPolicyCountry`), `shippingDetails`, `aggregateRating` |
| `ItemList` | `itemListElement[]` of `ListItem` with `position` and `url` | `name`, `description`, `numberOfItems`, `itemListOrder` |

### Worked example — `ItemList` (hub, pillar, roundup, top-N)

```json
{ "@context":"https://schema.org", "@type":"ItemList",
  "name":"Comparar tarifários de eletricidade",
  "numberOfItems": 3,
  "itemListElement":[
    {"@type":"ListItem","position":1,"name":"Tarifa A","url":"https://example.pt/a"},
    {"@type":"ListItem","position":2,"name":"Tarifa B","url":"https://example.pt/b"},
    {"@type":"ListItem","position":3,"name":"Tarifa C","url":"https://example.pt/c"}
  ] }
```

`numberOfItems` must equal the number of `itemListElement` entries and the number of items a user can see on the page. A list that markup claims has 30 entries and renders 10 is a mismatch, not an optimisation `[practitioner]`.

### Worked example — `ProductGroup`

```json
{ "@context":"https://schema.org", "@type":"ProductGroup",
  "name":"Product name", "productGroupID":"pg-001",
  "variesBy":["https://schema.org/size","https://schema.org/color"],
  "hasVariant":[
    { "@type":"Product","name":"Red, Large","sku":"SKU-001",
      "color":"Red","size":"Large","image":"https://example.com/red-l.jpg",
      "offers":{"@type":"Offer","price":"29.99","priceCurrency":"EUR",
                "availability":"https://schema.org/InStock"} }
  ] }
```

Every property named in `variesBy` must actually appear on each variant, or the group is self-contradicting.

### Worked example — `ProfilePage`

```json
{ "@context":"https://schema.org", "@type":"ProfilePage",
  "mainEntity":{ "@type":"Person", "name":"Author Name",
    "url":"https://example.pt/autores/author-name",
    "description":"Expertise summary in one or two sentences.",
    "sameAs":["https://www.linkedin.com/in/…","https://…"] } }
```

`sameAs` is only worth shipping for profiles that exist and are reachable; a dead link is a negative entity signal, not a neutral one `[practitioner]`.

### Worked example — `VideoObject`

```json
{ "@context":"https://schema.org", "@type":"VideoObject",
  "name":"Video title", "description":"What the video covers.",
  "thumbnailUrl":"https://example.com/thumb.jpg",
  "uploadDate":"2026-09-22",
  "duration":"PT1H30M",
  "contentUrl":"https://example.com/video.mp4",
  "embedUrl":"https://example.com/embed/video",
  "publisher":{"@type":"Organization","name":"Publisher",
    "logo":{"@type":"ImageObject","url":"https://example.com/logo.png"}} }
```

`duration` is ISO 8601 (`PT1H30M`), not seconds. `contentUrl` must be a fetchable media file and `thumbnailUrl` a crawlable image — a thumbnail blocked in robots.txt kills the video rich result silently.

## JSON-LD escaping

Next.js's JSON-LD guide warns that `JSON.stringify` does not sanitise strings used in XSS injection and shows replacing `<` with its unicode equivalent `\u003c` `[documented: https://nextjs.org/docs/app/guides/json-ld, 2026-10-12]`. Escaping `>`, `&` and `'` as well is the source repo's stricter rule `[practitioner]`.

Before a JSON object is written into `<script type="application/ld+json">`, escape the characters that let text break out of the tag: `<` as `\u003c`, `>` as `\u003e`, `&` as `\u0026` and `'` as `\u0027`. Skip it and a `</script>` arriving in user-supplied text closes the tag early and opens an XSS hole.

- Type-check JSON-LD at build time with `schema-dts` and use `@graph` to link `Organization`, `WebSite` and the page entities.
- A type-valid object is not a Google-eligible one: the vocabulary includes `FAQPage` and `HowTo`, which have no Google rich result. Check eligibility against the timeline above.

## A static check worth running (not a hook to install)

`claude-seo@hooks/validate-schema.py` implements a pattern worth copying as a repo test: scan every `<script type="application/ld+json">` block and **fail** when it contains (a) unreplaced placeholder text — `[Business Name]`, `[City]`, `[Your…`, `[INSERT`, `REPLACE_*` — or (b) invalid JSON-LD. A `@type` on the deprecated list above is an **Info** finding, not a failure: accurate `FAQPage` markup kept for another consumer is permitted (see the table above) — fail on it only where the project's own policy forbids the type. Placeholders and invalid markup ship silently in production and neither is caught by a rendering test.

Two implementation notes taken from that file `[practitioner]`: match `<script …>…</script>` generally and *then* filter on the `type` attribute — a pattern requiring `type` to be the first and only attribute skips any block carrying a CSP `nonce`, an `id` or a `data-*` attribute, i.e. exactly the blocks a real framework emits; and tokenise attribute values rather than scanning `[^>]*`, which ends the tag at the first `>` even inside a quoted value.

**Do not install this repository's hook**, do not copy it into `~/.claude`, and do not execute anything from the clone. Write the check into the project's own test suite where its failures are visible to CI.

## Cross-references

- `rendering-and-sitemaps.md#structured-data-json-ld` — `Organization`, `WebSite`, `BreadcrumbList`, the obsolete `SearchAction` / sitelinks search box (removed 21 Nov 2024), and the robots.txt collision it used to create.
- skill `seo-evidence` › titles-and-serp-tests — which rich results actually change the SERP line, and how to test a change rather than assume it.
- skill `seo-content` › comparison-pages — `Product` + `AggregateRating`, `SoftwareApplication` and `ItemList` as applied to comparison and roundup pages, with the fairness constraints that go with them.
- skill `seo-content` › local-and-maps-seo — `LocalBusiness` subtypes, required properties, multi-location `branchOf`.

## Sources

- claude-seo@skills/seo-schema/references/deprecated-types-2024-2026.md:8-49, 52-65, 67-74 — retirement timeline, replacement table, primary URLs; repo transcription (source's own "last verified 2026-05-25"), not a primary read — labels sit on the claims in the body.
- claude-seo@skills/seo/references/schema-types.md:80, 85-102, 104-110 — tooling-removal timeline, 2023–2026 additions, e-commerce requirements; repo transcription, not a primary read.
- claude-seo@schema/templates.json — 11 type shapes reduced to required/common fields plus four worked examples; `[practitioner]`, since the file carries no per-field citation.
- claude-seo@hooks/validate-schema.py:1-60 — the placeholder/deprecated-type check described as a pattern only; the hook itself is not imported or installed.
- google/schema-dts@README.md:311-321 (phase-2 adapted file research/adapted/group-E__readme-tool-repos/tool-stack-by-job.md) — JSON-LD escaping before injection, build-time typing, `@graph`, type-valid ≠ eligible. The adapted row had lost its escape sequences; restored as the `<`-style JSON escapes. INTEGRATE, Apache-2.0.
- garmeeh/next-seo@README.md (phase-2 adapted file research/adapted/group-E__readme-tool-repos/tool-stack-by-job.md) — live-type components and the four stale README claims listed as traps. INTEGRATE, MIT.
- schemaorg/schemaorg@README.md (phase-2 adapted file research/adapted/group-E__readme-tool-repos/tool-stack-by-job.md) — idea only, our own words: vocabulary ≠ Google support. LEARN (no text taken), Apache-2.0.
- https://developers.google.com/search/blog/2025/06/simplifying-search-results — June 2025 retirements.
- https://developers.google.com/search/blog/2023/08/howto-faq-changes — HowTo and FAQ changes.
- https://developers.google.com/search/docs/appearance/structured-data/faqpage — FAQ rich-result retirement, 7 May 2026.
