# International SEO, locale formats and translation quality
<!-- split-header-2: part 1 of 2 of international-and-hreflang.md (original lines 1–123; boundary start) -->
<!-- /split-header-2 -->

## Contents

- Machine translation and scaled content abuse
- Geo-signal hierarchy, and what is not a lever
- Region-specific Search result units (EEA, South Africa, Türkiye)
- Locale formats
- Detecting a translation that was never really done
- Not imported: cultural-profile tables
- Unverified
- Sources

Other parts of the same original file: [international-and-hreflang-2.md](international-and-hreflang-2.md).

## Machine translation and scaled content abuse

The enforceable, webmaster-facing rule is the spam policy: its scaled-content-abuse examples include generating many pages "through automated transformations like synonymizing, translating, or other obfuscation techniques), where little value is provided to users" `[documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]`.

Rater-guidelines machine-translation clause: unverified [unverified: the saved Quality Rater Guidelines copy yields only its cover and contents]; see ## Unverified.

The policy test is **purpose and value, not creation method**: scaled content abuse is «many pages … generated for the primary purpose of manipulating search rankings and not helping users», «no matter how it's created» `[documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]`. Human review is a quality-assurance step, not a policy boundary: reviewed low-value pages at scale are not cleared by it, and an unreviewed translation is not a violation by that fact alone. As QA `[unvalidated house heuristic]`, have a native speaker review MT, because "lightly post-edited" output still carries hallucinated terms, wrong gender or number agreement, or untranslated proper nouns. For Portuguese this matters more than for most target languages: gender and number agreement errors are the exact failure mode of cheap MT, and pt-BR output shipped on a pt-PT page reads as machine-made to any Portuguese reader even when it is grammatical.

Signals worth surfacing in an audit, with the source's severities `[practitioner]`:

| Signal | Severity | What it means |
|---|---|---|
| Several hreflang alternates point to pages identical except for header chrome | Critical | The body was never translated — only the template was wrapped |
| `<html lang="xx">` does not match the body language | High | Translation pipeline ran with no final QA step |
| Auto-translated meta description left over the house length target (160 characters `[unvalidated house heuristic]`), untrimmed | Medium | No human edited the translation. Google sets no meta description length limit; the snippet is truncated as needed `[documented: https://developers.google.com/search/docs/appearance/snippet, 2026-10-12]` |
| `lang` is `auto` or absent | Medium | Undeclared language confuses hreflang and AI crawlers alike |
| Untranslated proper nouns or product names scattered in the body | Low (heuristic) | Classic MT failure, hard to detect automatically |
| Schema.org `inLanguage` missing or wrong | Medium | Cross-check `inLanguage` against the body language in any multilingual audit |

**What NOT to flag** — imported verbatim because an audit that flags these destroys its own credibility, exactly the failure the skill's own "an imprecise gate blames the product" discipline warns about:

- Sites with a few MT pages **clearly labelled as MT** (the human-translation-fallback pattern); the source repo's QRG basis for this is unread (## Unverified).
- Machine-translated **UI strings** — that is i18n, not "content".
- Pages with `lang="auto"` when no fallback signal can be fetched. Be conservative; do not claim what cannot be verified.

**No per-mechanism exemption exists.** On 2025-06-11 Google removed from its multilingual documentation the section «about using robots.txt to block all automatically translated pages», to align with its March 2024 spam policy update — «a docs-only change, no change in behavior» `[documented: https://developers.google.com/search/updates, 2026-10-14]`. Judge auto- and AI-translated pages case-by-case on user value; the remedy for a low-value translated page is page-level `noindex`, not a sitewide block `[unvalidated house heuristic]`. Google's own translate widget is detectable by the `.goog-te-banner-frame` iframe `[practitioner]`, and its output also produces poor passage citability for answer engines `[hypothesis]` (skill `seo-ai-search` › ai-retrieval-and-citation).

## Geo-signal hierarchy, and what is not a lever

`[practitioner]`. Practical locale-signal ordering: **ccTLD > hreflang annotations > server location/IP > on-page signals (addresses, language, currency, Business Profile)**. Present it as a working heuristic — it is **not** a confirmed Google ranking order. Google's multi-regional guide lists those signals without ranking them, and says Google **ignores** locational meta tags (like `geo.position` or `distribution`) and geotargeting HTML attributes `[documented: https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites, 2026-10-12]`, so any recommendation built on `geo.region` or similar markup is dead weight.

Google calls the Search Console **International Targeting report deprecated**; it removed the report from its documentation on 2022-08-24 and said its multi-regional and localized-versions guidance remains relevant `[documented: https://developers.google.com/search/updates, 2026-10-11]`. Do not recommend a GSC country-targeting setting. hreflang is the remaining lever, and a ccTLD decision is a one-way door made at domain level.

Invalid-code errors that fail silently. Google supports ISO 639-1 language codes, optionally followed by an ISO 3166-1 Alpha 2 region code; other codes (its example is `es-419`) are not supported, and a region alone is not valid. A script may also be given explicitly in ISO 15924 form — `zh-Hant`, `zh-Hans`, and with a region `zh-Hans-US` `[documented: https://developers.google.com/search/docs/specialty/international/localized-versions, 2026-10-12]`. Accept `language`, `language-REGION`, `language-Script` and `language-Script-REGION`. The last three bullets apply that rule `[practitioner]`:

- **A country code alone is invalid** — a region cannot be specified without a language. Google's own counter-example is `be`, which is the Belarusian *language* code, not Belgium.
- `en-uk` for the UK — `UK` is not a valid ISO 3166-1 region; the code is `en-GB`.
- `EU` or `UN` as a region — not ISO 3166-1 values.
- `es-LA` — Latin America is not a country; name specific ones.

For a Portuguese site the choice runs the other way: `pt` alone is valid and means Portuguese in general `[documented: https://developers.google.com/search/docs/specialty/international/localized-versions, 2026-10-14]`. Use it when one version serves all Portuguese speakers; use `pt-PT` (and `pt-BR`) when you publish separate regional versions `[unvalidated house heuristic]`. See `rendering-and-sitemaps.md#hreflang`.

## Region-specific Search result units (EEA, South Africa, Türkiye)

Google's regional-differences page (added 2026-09-08) lists Search features that exist **only in certain regions**: in the EEA, aggregator and supplier units for hotels, flights, ground transportation, local businesses and products, plus an ecosystem carousel and job-sites features; in Türkiye, places-sites features; in South Africa, a badge and refinement chip `[documented: https://developers.google.com/search/docs/appearance/aggregator-features, 2026-10-12]`. Eligibility and participation are documented per feature. Read them as result features with their own entry rules, not as ranking signals `[hypothesis]`.

**Portugal is in the EEA, so this applies directly to Mowei and to any Portuguese client** `[practitioner]`. Two consequences. First, the result layout a Portuguese user sees for a travel, transport or product query differs from what a US-based tool or a VPN check reports — a rank or layout claim taken from the wrong locale is an environment fact, not a finding. Second, the aggregator/supplier distinction is a positioning question before it is an SEO one: a comparison platform is an **aggregator**, and which unit it can appear in follows from that. State in any report which side of the line the business sits on and link the regional documentation, so nobody is surprised by a different layout in those markets.

## Locale formats

`[practitioner]` (source credits Chris Muller, Pro Hub Challenge). Mismatched formats — a US date on a German page, a dollar figure on a euro page — signal poor localisation and cost reader trust before any ranking effect. The source table covers en-US, en-GB, de-DE, de-AT, de-CH, fr-FR, fr-CA, es-ES, es-MX, it-IT, nl-NL, ja-JP, ko-KR, zh-CN and **pt-BR — but has no pt-PT row at all.** That gap is the one this file exists to close.

### pt-PT `[practitioner]`

| Element | Portugal (pt-PT) | Example |
|---|---|---|
| Decimal separator | Comma | `1234,56` |
| Thousands separator | **Non-breaking space** is current practice — see note below | `1 234 567,89` |
| Date | `dd/mm/aaaa` (note: the Portuguese year placeholder is `aaaa`, from *ano*, not `yyyy` — it appears in form hints and placeholder text) | `14/04/2026` |
| Currency | `€` **after** the number, separated by a non-breaking space | `1 234,56 €` |
| Phone | `+351` followed by 9 digits, conventionally grouped 3-3-3 | `+351 210 000 000` |
| Postal code | `dddd-ddd` — four digits, hyphen, three digits; the three-digit suffix is mandatory and is not optional detail | `1000-001 Lisboa` |
| Address order | Street and number, then postal code and locality on the next line | `Rua Augusta 100`<br>`1100-053 Lisboa` |
| NIF (tax number) | Exactly 9 digits, no separators, no country prefix in display | `123456789` |
| Text expansion vs English | +15-25% (the source's Portuguese row; applies to both variants) | Longer buttons and nav labels |

**Which thousands separator is current practice.** Both the space and the dot are seen in Portuguese commercial writing, so this needs deciding once rather than per page. The grouping separator in ICU/CLDR for `pt-PT` is **U+00A0, a non-breaking space** — verified directly: `Intl.NumberFormat('pt-PT').format(1234567.89)` returns `1 234 567,89`, and `formatToParts` reports the group character as `a0` (checked 2026-09-22, Node/ICU). This matters operationally because **it is what a Next.js app already emits** whenever a figure passes through `Intl.NumberFormat` or `toLocaleString('pt-PT')`. Recommendation `[practitioner]`: take the CLDR space as house style so runtime-formatted and hand-written figures agree, never mix the two conventions on one page, and **never use a plain space** — a normal space lets a currency figure break across lines mid-number.

`Intl` with the same locale also yields `1 234 567,89 €` for EUR (symbol after, NBSP separator) and `14/04/2026` for a date, so a page that formats through the platform and a page hand-written to this table will match.

### Validation rules for any locale

`[practitioner]`

1. Scan the page for number patterns — prices, statistics, measurements.
2. Compare each against the expected format for the page's **declared** language.
3. Flag US-format numbers on non-US pages (`$1,234.56` on a de-DE or pt-PT page).
4. Check dates in posts, copyright lines and update timestamps — stale-looking US dates are a common leftover.
5. Verify the currency symbol and its placement match the target market.
6. Verify phone numbers use international format with the right country code.

Text-expansion ratios vs English, for layout budgeting `[practitioner]`: German +25-35%; French, Spanish, Italian and Portuguese +15-25%; Dutch +10-20%; Japanese −10-25%; Korean −10-20%; Chinese −20-30%. The practical consequence is that a button or nav label designed at English width breaks in Portuguese at roughly one word in five — test the longest string, not the average.

## Detecting a translation that was never really done

`[practitioner]`. Word-count ratio against the English source is a cheap, surprisingly sharp instrument. Expected ratios: German 1.25-1.35× (acceptable 1.10-1.50×), French 1.15-1.25× (1.00-1.40×), Spanish 1.15-1.25× (1.00-1.40×), Japanese 0.75-0.90× (0.60-1.00×), Chinese 0.70-0.80× (0.55-0.95×). The source has no Portuguese row; its expansion table puts Portuguese with French and Spanish, so **1.15-1.25× expected, 1.00-1.40× acceptable** is the consistent extrapolation `[practitioner]`.

The reading: **a translation materially shorter than expected has missing content; one materially longer has padding.** A German page shorter than its English source did not get fully translated. Apply the same logic in reverse for the contracting languages.

Freshness deltas against the source page `[practitioner]`: within 7 days = fresh; 8-30 days = aging, low priority; 31-90 days = stale, medium; over 90 days = outdated, high priority. On a site whose numbers change (tariffs, rates, brackets), the freshness delta is not a tidiness metric — a stale locale variant is publishing wrong figures.

Cultural-adaptation checks worth running, with the source's severities `[practitioner]`:

| Check | Look for | Severity |
|---|---|---|
| Legal references | Wrong jurisdiction cited (CCPA on a German page instead of DSGVO; on a Portuguese page, US or UK regulators instead of ERSE / ANACOM / Banco de Portugal / ASF) | High |
| Currency and unit mismatch | USD prices on a EUR page, imperial units on a metric page | High |
| Foreign brand references | US-only brands on a non-US page | Medium |
| Foreign statistics | US-only data cited on a localised page ("80% of Americans") | Medium |
| Untranslated elements | English left in navigation, buttons, alt text or schema | Medium |
| CTA register | Aggressive imperative CTAs on formal-register pages | Low |

The legal-reference row is the one that carries real risk for a Portuguese financial or utilities site: a translated page citing the wrong regulator is both a trust failure and, in regulated copy, a compliance exposure.

**The parity score is a house heuristic** `[unvalidated house heuristic]` — 100 points split 30 page-existence / 30 SEO-element / 25 content-structure / 15 freshness, with bands at 90-100, 70-89, 50-69 and below 50. Nothing derives those weights. The four *components* are the useful part: report existence, element, structure and freshness parity separately, each with its own count, rather than collapsing them into one number that hides which locale is actually broken.

## Not imported: cultural-profile tables

The source repo (claude-seo) carries a `claude-seo@references/cultural-profiles.md` of per-country behavioural generalisations. **It is deliberately excluded from this library.** Country-level stereotypes about how "German users" or "Japanese users" behave are unfalsifiable at page level, cannot be verified against any source, and would be applied to real users of a Portuguese financial site. Everything actionable that such a table gestures at is already covered above by observable, checkable signals: format conventions, legal jurisdiction, currency, register, and the expansion ratio that actually breaks layouts.

## Unverified

- Rater-guidelines machine-translation clause: the source repo reports that the Quality Rater Guidelines update of 23 January 2025 added language treating machine-translated content with no human review as scaled content abuse (§4.6.5) [unverified: the saved Quality Rater Guidelines copy yields only its cover and contents]
- Hreflang as a hint: the source repo says hreflang is a hint, not a directive [unverified: neither saved Google international page uses that wording]

## Sources
- claude-seo@skills/seo-hreflang/references/locale-formats.md:9-100 — locale format tables and validation rules (full list in part 2).
- claude-seo@skills/seo-hreflang/references/content-parity.md:37-50, 65-78 — word-count ratios, freshness deltas, 100-point parity score.

