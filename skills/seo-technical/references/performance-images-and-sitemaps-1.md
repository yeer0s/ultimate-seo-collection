# Performance subparts, images and sitemap extensions
<!-- split-header: part 1 of 2 of performance-images-and-sitemaps.md (step-3 original lines 1–120; boundary start) -->
## Contents

- LCP subparts
- Performance tooling changelog (2025–2026)
- Image size tiers and lazy-load detection
- The exiftool / cwebp / ImageMagick pipeline
- Unverified
- Sources

Other parts of the same original file: [performance-images-and-sitemaps-2.md](performance-images-and-sitemaps-2.md).

<!-- /split-header -->

Answers three operational questions the main references keep short: *which phase of LCP is actually slow*, *what to do to an image file and what is a waste of time*, and *what rules apply to an image / video / news sitemap that do not apply to a normal one*. It closes with the agent-friendly-page checklist. Load it when diagnosing a missed LCP target, running an image pass, validating an extension sitemap, or auditing a page for AI-agent usability. The CWV bar (three metrics, targets, field-vs-lab) lives in `rendering-and-sitemaps.md#core-web-vitals`; the general sitemap rules (canonicals only, 50,000-URL split, `lastmod` honesty) in `rendering-and-sitemaps-2.md#sitemapxml`. Neither is restated here.

## LCP subparts

Every LCP value breaks down into four subparts with no overlap or gap, which add up to the full LCP time `[documented: https://web.dev/articles/optimize-lcp, 2026-10-12]`. LCP image subparts were added to the CrUX API in January 2025 `[documented: https://developer.chrome.com/docs/crux/release-notes, 2026-10-12]`.

| Subpart | What it measures | Target |
|---|---|---|
| **TTFB** | Time to First Byte (server response) | ≤ 0.8 s good, > 1.8 s poor `[documented: https://web.dev/articles/ttfb, 2026-10-12]` |
| **Resource load delay** | TTFB → LCP resource request starts | Minimize |
| **Resource load duration** | Downloading the LCP resource | Depends on size |
| **Element render delay** | Resource loaded → rendered | Minimize |

**Total LCP = TTFB + resource load delay + resource load duration + element render delay.** Only TTFB carries a published numeric target here; the other three are "minimize", so a tool that prints a pass/fail per subpart is inventing thresholds `[practitioner]`.

Why this beats a single LCP number `[practitioner]`: each subpart has a disjoint remedy set. High **TTFB** is server/CDN/origin work — image compression cannot touch it. High **resource load delay** means the browser learned about the LCP resource late; fix with `fetchpriority="high"`, `<link rel="preload">`, or getting the image out of a lazy-loader or client-rendered component. High **resource load time** is file size — the only phase the image pipeline below improves. High **element render delay** is render-blocking CSS/JS or a font swap. "LCP 4.1 s, compress your hero" without the split is a coin flip.

Verdict rules, the field/lab reconciliation table, INP phases and CLS causes: [cwv-field-lab-diagnosis.md](cwv-field-lab-diagnosis.md).

The source repo dated the CrUX subpart addition both February and January 2025; the CrUX release notes settle it as January 2025 (above). API field names: `google-apis-and-quotas.md#crux-and-pagespeed-insights--field-fields-and-nulls`.

## Performance tooling changelog (2025–2026)

Each item is perishable: re-read the Lighthouse changelog and the CrUX release notes before quoting a version number to a client `[practitioner]`.

- **Lighthouse 13.5.0** (2026-09-17) is the newest release in the changelog read on 2026-10-12. **13.0.0 (2025-10-10) removed the performance audits replaced by performance insights**, plus `font-size`, `third-party-facades` and the empty `first-meaningful-paint` audit `[documented: https://raw.githubusercontent.com/GoogleChrome/lighthouse/main/changelog.md, 2026-10-12]`. A missing audit id across 13.0 is a removal, not a failure `[practitioner]`.
- **The PWA category was removed in Lighthouse 12.0.0** (2024-04-22) `[documented: https://raw.githubusercontent.com/GoogleChrome/lighthouse/main/changelog.md, 2026-10-12]`. Code parsing a `pwa` category reads it as absent, not failing.
- **PageSpeed Insights' CPU throttling factor changed in Lighthouse 12.2.3 (2024-12-02).** The changelog says TBT times for all sites should **improve** in PSI, and that the CLI, Node API and DevTools are unaffected `[documented: https://raw.githubusercontent.com/GoogleChrome/lighthouse/main/changelog.md, 2026-10-12]`. (The source repo said mobile TBT rose; the changelog says the opposite.) **Do not compare PSI lab TBT across that boundary** — the same kind of measurement-change check as the DMA date in `google-apis-and-quotas.md`.
- **The CrUX Dashboard** (Looker Studio) was deprecated at the end of November 2025; the October 2025 dataset was the last fed to its connector, and CrUX Vis left experimental status in March 2025 `[documented: https://developer.chrome.com/docs/crux/release-notes, 2026-10-12]`. An earlier Looker Studio CWV dashboard is now a frozen picture, not a monitor `[practitioner]`.
- Search Console and mobile-first items from the source repo: unverified [unverified: no saved Google page states them]; see ## Unverified.

*(The repo also carries a Soft Navigations API item with specific future Chrome version numbers — uncited speculation about an unshipped feature, deliberately not imported.)*

## Image size tiers and lazy-load detection

**Tiered file-size thresholds by image role** — the repo publishes these as targets with no measurement behind them; treat them as operating defaults, not a standard `[unvalidated house heuristic]`:

| Image category | Target | Warning | Critical |
|---|---|---|---|
| Thumbnails | < 50 KB | > 100 KB | > 200 KB |
| Content images | < 100 KB | > 200 KB | > 500 KB |
| Hero / banner | < 200 KB | > 300 KB | > 700 KB |

The tiering is the useful part `[practitioner]`: a flat "all images under 100 KB" rule fails every legitimate hero and passes every bloated thumbnail. Judge a file against its role. The **LCP resource's** own size moves LCP directly; other images move it indirectly when they download at the same time and compete for bandwidth («network contention») `[documented: https://web.dev/articles/optimize-lcp, 2026-10-14]`. So a 600 KB below-fold image loaded eagerly next to the hero can delay LCP; deferred, it is a bandwidth issue only.

### Lazy-load detection taxonomy — the false-flag guard

Auditing `loading="lazy"` alone **misreports every JS-lazy-loaded site as unoptimised**. Five mechanism values, from the repo's own `lazy_method` classifier `[practitioner]`:

| `lazy_method` | Signal | Common stack |
|---|---|---|
| `native` | `loading="lazy"` attribute | Modern browsers, plain HTML |
| `perfmatters` | `data-perfmatters-src`/`-srcset`, or class `perfmatters-lazy` | WordPress + Perfmatters |
| `ewww` | `data-ewww-src` / `data-eio`, or class `lazyload-eio` | WordPress + EWWW Image Optimizer |
| `js-generic` | `data-src` / `data-lazy-src` / `data-original` / `data-srcset`, or class `lazyload` / `lazyloaded` / `lazy` | lazysizes, vanilla-lazyload, jQuery plugins |
| `none` | Neither attribute nor class signal | Not lazy-loading this image |

🔴 **When a JS lazy-loader is in use, the absence of native `loading="lazy"` is intentional, not a regression** `[practitioner]`. Report the method alongside the attribute — flagging `js-generic` pages as "no lazy loading" produces findings against work that is already correct.

The inverse matters too `[practitioner]`: a lazy-loader on the **LCP image** actively harms LCP by inflating resource load delay. The correct pattern is `fetchpriority="high"` on the hero, lazy-loading strictly below the fold.

## The exiftool / cwebp / ImageMagick pipeline

Tool order, availability checked first via `which exiftool cwebp convert ffmpeg` `[practitioner]`: **exiftool** (EXIF/IPTC/XMP read-write), **cwebp** (WebP), **ImageMagick `convert`** (conversion and resizing), **FFmpeg** (AVIF / fallback).

Six-step pass `[practitioner]`: (1) audit current state, (2) inject IPTC/XMP metadata — Creator, Copyright, Description, (3) convert to WebP, (4) generate responsive variants at 400w / 800w / 1200w, (5) **verify metadata survived the conversion**, (6) emit `<picture>` with an AVIF → WebP → JPEG fallback chain.

Representative commands `[practitioner]` (cwebp's `-q` sets quality and `-metadata all` copies all metadata the input carries `[documented: https://developers.google.com/speed/webp/docs/cwebp, 2026-10-12]`):

- WebP with metadata preserved: `cwebp -q 82 -metadata all input.jpg -o output.webp`
- ImageMagick fallback: `convert input.jpg -quality 82 output.webp`
- AVIF via FFmpeg (slower encode, best compression): `ffmpeg -i input.jpg -c:v libaom-av1 -crf 30 -still-picture 1 output.avif`
- Responsive variant: `convert input.jpg -resize 800x -quality 82 image-800.webp`
- IPTC injection: `exiftool -IPTC:By-line="…" -IPTC:Credit="…" -IPTC:CopyrightNotice="…" -XMP:Creator="…" -XMP:Rights="…" image.jpg`

Two constraints causing silent data loss. **The WebP container defines optional EXIF and XMP chunks and no IPTC chunk** `[documented: https://developers.google.com/speed/webp/docs/riff_container, 2026-10-12]` — use the XMP fields, which exiftool maps automatically `[practitioner]`; and step 5 exists because cwebp's `-metadata` default is `none`, so a conversion without `-metadata all` strips everything step 2 injected `[documented: https://developers.google.com/speed/webp/docs/cwebp, 2026-10-12]`.

What the metadata buys: with structured data or IPTC photo metadata, Google Images can show who the creator is, how the image may be used and credit information `[documented: https://developers.google.com/search/docs/appearance/structured-data/image-license-metadata, 2026-10-12]`. That is **display and brand attribution, not a ranking factor** `[practitioner]`.

### IPTC `DigitalSourceType` — AI-image labelling

**Google Merchant Center requires every image created with generative AI to carry the IPTC `DigitalSourceType` `TrainedAlgorithmicMedia` metadata tag, and says not to strip embedded `DigitalSourceType` tags** `[documented: https://support.google.com/merchants/answer/14743464, 2026-10-12]` — an operational policy requirement, not a ranking factor `[practitioner]`.

The values Merchant Center says to preserve `[documented: https://support.google.com/merchants/answer/14743464, 2026-10-12]`:

| Value | Meaning |
|---|---|
| `TrainedAlgorithmicMedia` | Created with a model derived from sampled content — the value for diffusion-model product imagery |
| `CompositeSynthetic` | A composite that includes synthetic elements |
| `AlgorithmicMedia` | Created purely by an algorithm, **not** from sampled training data |

exiftool writes the tag as the XMP `iptcExt` string tag `DigitalSourceType` `[documented: https://exiftool.org/TagNames/XMP.html, 2026-10-12]`. The source repo writes the full IPTC controlled-vocabulary URI rather than the bare token — `exiftool -XMP-iptcExt:DigitalSourceType="https://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia" file.jpg` — and audits for absence with `exiftool -if 'not $XMP-iptcExt:DigitalSourceType' -filename -DigitalSourceType *.jpg *.webp *.png` `[practitioner]`.

Three adjacent facts, each with its own boundary:
- SynthID watermarks and C2PA Content Credentials: unverified [unverified: no saved Google page describes their status as Merchant fields]; see ## Unverified.
- **Licensable badge**: one form of photo metadata is enough — structured data on the page, or IPTC photo metadata in the image `[documented: https://developers.google.com/search/docs/appearance/structured-data/image-license-metadata, 2026-10-12]`. Markup side: `rendering-and-sitemaps.md#structured-data-json-ld`.
- **AI-generated product titles and descriptions** go in Merchant Center's `structured_title` / `structured_description` attributes with `digital_source_type` `trained_algorithmic_media` `[documented: https://support.google.com/merchants/answer/14743464, 2026-10-12]` — enforced at the feed layer, outside an on-page image audit.

### Ranked impact — what actually matters for Google Images

`[unvalidated house heuristic]`

| Factor | Impact | Where set |
|---|---|---|
| Alt text | **CRITICAL** (ranking) | HTML `<img alt="">` |
| Filename | **HIGH** (ranking) | Filesystem — descriptive, hyphenated |
| Page context | **HIGH** (ranking) | Surrounding HTML content |
| File size / speed | MEDIUM (indirect, via CWV) | Compression + format conversion |
| IPTC Creator / Copyright | LOW (display only) | Image file metadata |
| EXIF camera data | **NONE** | Irrelevant for SEO |
| IPTC Keywords | **NONE** | Google ignores these |

**Read this table before quoting the pipeline above** `[practitioner]`. The two highest-impact levers — alt text and filename — cost nothing and need no tooling, while the elaborate exiftool pass buys a LOW display benefit plus a Merchant Center compliance requirement. An image "optimisation" that ships metadata injection while leaving `IMG_4417.jpg` and empty alt attributes has inverted its own priority list. Alt-text failures the repo names: filename-as-alt-text, keyword stuffing, "Click here" `[practitioner]`.

Visual-search discovery: unverified [unverified: no saved Google page describes visual-search fan-out across Lens, AI Mode and Circle to Search]; see ## Unverified.

## Unverified

- Search Console and mobile-first items from the source repo: hourly data (`HOUR` / `HOURLY_ALL`) from April 2025; a branded vs non-branded filter from November 2025, expanded about March 2026; natural-language configuration from February 2026; removal of the standalone Page Experience report; mobile-first indexing completed in 2024, with a mobile version "very strongly recommended" [unverified: no saved Google page states them]
- Lighthouse 13 scoring and runtime: the source repo says the 13.0 performance score was not re-weighted and the CLI needs Node.js 22.19+ [unverified: the saved changelog does not state either]
- SynthID watermarks and C2PA Content Credentials: the source repo says they are detection/transparency signals, not an additional required Merchant feed field beyond IPTC `DigitalSourceType`, and that Merchant feeds missing the label can be disapproved [unverified: no saved Google page describes their status as Merchant fields or a disapproval rule]
- Extra DigitalSourceType values: the source repo adds `compositeWithTrainedAlgorithmicMedia` (trained media composited over other media) and `digitalCapture` (a captured photograph) to the values Google reads [unverified: the saved Merchant Center page lists only the three values above]
- Visual-search discovery: the source repo says images now surface through visual-search fan-out across Lens, AI Mode and Circle to Search, by scene, objects and materials rather than alt text alone [unverified: no saved Google page describes visual-search fan-out across Lens, AI Mode and Circle to Search]

## Sources
- claude-seo@skills/seo-images/SKILL.md:35-49, 100-122, 236-320, 401-421 — tiered size thresholds, `lazy_method` taxonomy, tool order and six-step pipeline, ranked-impact table, alt-text failure modes (full list in part 2).

