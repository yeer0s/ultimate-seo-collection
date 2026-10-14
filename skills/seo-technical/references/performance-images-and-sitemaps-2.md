<!-- split-header: part 2 of 2 of performance-images-and-sitemaps.md (step-3 original lines 121–172; boundary H2) -->
# Sitemap extension rules, agent-friendly pages (performance, images and sitemaps 2 of 2)
## Contents

- Sitemap extension rules
- Agent-friendly pages
- Cross-references
- Unverified
- Sources

Other parts of the same original file: [performance-images-and-sitemaps-1.md](performance-images-and-sitemaps-1.md).

<!-- /split-header -->
## Sitemap extension rules

Three subtypes carry rules **on top of** the general guidance in [rendering-and-sitemaps-2.md](rendering-and-sitemaps-2.md#sitemapxml). Validate per subtype `[practitioner]`.

**Image** (`http://www.google.com/schemas/sitemap-image/1.1`): the required tags are `<image:image>` and `<image:loc>`, with **up to 1,000 `<image:image>` per `<url>`**; Google removed `<image:caption>`, `<image:geo_location>`, `<image:title>` and `<image:license>` from its documentation `[documented: https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps, 2026-10-12]`. Flag those four as info-level removable, not errors `[practitioner]`.

**Video**: `<video:video>` required, carrying `<video:thumbnail_loc>`, `<video:title>`, `<video:description>`, plus **either** `<video:content_loc>` **or** `<video:player_loc>`; mRSS also supported. Video tags flagged as deprecated: unverified [unverified: Google's video sitemap page was not saved]; see ## Unverified.

**News**: **up to 1,000 `<news:news>` tags per sitemap** — split the file beyond that; one `<news:news>` per `<url>`; news sitemaps «are based on generic sitemaps», so the general rules also apply; a news extension may sit in an ordinary sitemap; articles older than two days are either removed or kept with their `<news:news>` metadata removed `[documented: https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap, 2026-10-12]`. Required: `<news:publication>`, `<news:name>`, `<news:language>`, `<news:publication_date>`, `<news:title>`. Submit/discover via Search Console or robots.txt / a sitemap index; Publisher Center is publication management only.

🔴 **Validator rule** `[practitioner]`: when the `news:` namespace is detected, check **both** limits independently — the generic 50,000-URL limit on `<url>` entries and the 1,000 cap on `<news:news>` tags. A sitemap with 5,000 ordinary URLs and 500 news entries is valid. A generic linter misses the news-tag cap, and flags the deprecated image tags as errors when they are merely removable. Subtype detection comes before validation.

## Agent-friendly pages

Whether an AI agent — not a crawler, an *operator* — can actually use a page. web.dev's agent-friendly guide backs the ghost-overlay, semantic-HTML (`role` and `tabindex` as fallback), `<label for>`, `cursor: pointer`, 8-square-pixel and stable-layout points below `[documented: https://web.dev/articles/ai-agent-site-ux, 2026-10-12]`; the WCAG/HIG sizes, the overlay offenders and item 7 come from the source repo `[practitioner]`.

1. **Real interactive elements.** `<button>` for actions, `<a href>` for navigation, real `<input>`/`<select>`/`<textarea>` — not `<div onclick>`, not custom `contenteditable` widgets. Where a real tag is impossible: `role="button"`/`role="link"`, `tabindex="0"`, `Enter`/`Space` handlers. *Why*: the accessibility tree exposes real elements with their roles; custom div widgets often appear with **no role at all**, and agents skip them.
2. **Label associations.** Every input needs `<label for>`, or `aria-label` / `aria-labelledby`. Without it the input is a void to an agent reading the tree.
3. **Interactive target size.** Visual-analysis pipelines filter out interactive elements below roughly **8 square pixels** of unobscured area. WCAG AA's **24×24** and Apple HIG's 44×44 are stricter and clear the gate by default — audit anything under 24×24 as both a WCAG failure and a candidate for agent invisibility.
4. **No transparent overlays on interactive nodes.** Vision models discard covered nodes. Offenders: full-card click handlers overlaying child links, cookie layers persisting past consent, modal portals left at `pointer-events: auto`, tracking pixels at `inset: 0`.
5. **Layout stability across templates.** "Add to cart" in different positions per category makes a screenshot-driven agent relearn the page. **Overlaps CLS but is broader** — CLS is within-page shift; this is page-to-page consistency, which no Core Web Vital measures.
6. **`cursor: pointer` is a legitimate signal.** Vision models read it as "actionable". Don't strip it from real controls; don't apply it to non-interactive elements, which makes agents click things that do nothing.
7. **Stable, meaningful selectors.** Semantic tags, stable `id`s on layout containers, `data-*` attributes describing **purpose, not implementation**. An auto-generated class like `__sc_a4b7d9e2` as the only handle on a critical control is targetable but unreadable.

Most of this is accessibility work with a second payoff `[practitioner]` — the honest way to fund it. Items 1–3 are WCAG obligations already and 5 is a design-system argument; the new asks are 4, 6 and 7.

Lighthouse's Agentic Browsing category: see skill `seo-ai-search` › agent-readiness (moved there in phase 2; the description that stood here was stale).

## Cross-references

- `rendering-and-sitemaps.md#core-web-vitals` — the three metrics, targets, supporting diagnostics, field-vs-lab, common fixes. This file only decomposes LCP; that file owns the bar.
- `rendering-and-sitemaps-2.md#sitemapxml` — canonical-only inclusion, `lastmod` honesty, the 50,000-URL / 50 MB split, submission. The extension rules above add to it per subtype.
- `rendering-and-sitemaps.md#structured-data-json-ld` — `ImageObject` markup for the Licensable badge.
- `google-apis-and-quotas.md#crux-and-pagespeed-insights--field-fields-and-nulls` — CrUX field names for the LCP subparts, `"NaN"`/`null` handling, update cadence.
- skill `seo-optimizer` › audit-output-and-templates — lab-as-proxy rules for a URL with no CrUX eligibility yet (TBT as the INP stand-in, the diarised four-week field re-read).

## Unverified

- Video tags flagged as deprecated: the source repo flags `<video:category>`, `<video:gallery_loc>`, `<video:price>`, `<video:tvshow>` and the player `autoplay` / `allow_embed` attributes as info-level removable, with its own caveat to recheck Google's docs before citing a removal date [unverified: Google's video sitemap page was not saved]

## Sources

All `claude-seo` paths below are relative to `skills/`. These entries are provenance only and carry no evidence label: a repo transcription is not a primary read. Each claim keeps its own label in the body or in ## Unverified.

- `seo/references/cwv-thresholds.md:21-34` — LCP subpart table, TTFB < 800 ms target, additive total.
- `seo/references/cwv-thresholds.md:102-108` — the whole tooling changelog above; perishable. The Soft Navigations item at `:38` was read and **excluded** as uncited Chrome-version speculation.
- `seo-images/SKILL.md:35-49` — alt-text failure modes; tiered file-size thresholds, carried in the body as a house heuristic (no measurement published behind them).
- `seo-images/SKILL.md:100-122` — `fetchpriority="high"` for LCP images; the five-value `lazy_method` taxonomy and the explicit instruction not to treat a missing native attribute as a regression under a JS loader.
- `seo-images/SKILL.md:236-320, 401-410` — tool order and availability check, conversion commands, IPTC+XMP injection, the WebP-no-native-IPTC constraint, six-step pipeline, "IPTC display is not a ranking factor".
- `seo-images/SKILL.md:309-388` — Merchant Center `DigitalSourceType` requirement and disapproval risk, the five-value vocabulary with the `digitalCapture` caveat, the URI form, the audit one-liner, SynthID/C2PA scope, Licensable either/or, feed-text labelling, visual-search fan-out; primary source cited by the repo: https://support.google.com/merchants/answer/14743464
- `seo-images/SKILL.md:411-421` — ranked-impact table.
- `seo-sitemap/SKILL.md:64-81` — image / video / news extension rules, the 1,000-per-`<url>` image cap, 2022 image-tag deprecations, video required and deprecated tags with the repo's own recheck caveat, news 1,000-item cap and last-2-days rule, namespace override of the generic 50k check.
- `seo-technical/references/agent-friendly-pages.md:24-104` — seven-item checklist, ~8-square-pixel filter, 24×24 WCAG AA and 44×44 Apple HIG figures, overlay offenders, CLS-overlap note, selector guidance.
- `seo-technical/references/agent-friendly-pages.md:105-156` — the former Lighthouse agent-audit section (moved to skill `seo-ai-search` in phase 2), including the explicit "fractional pass-ratio, not a weighted score" instruction, the three WebMCP audit ids, run paths, and "CrUX never provides these lab audits".
