<!-- split-header: part 2 of 2 of titles-and-serp-tests.md (step-3 original lines 81–127; boundary H2) -->
# Metadata at scale — per-template tests, running a title test, SERP features

## Contents

- Metadata change lifecycle
- Swap Test
- Templated metadata at site scale
- Per-template tests, not rules
- How to run a title test
- Answer formatting and SERP features
- CTR — optimise qualified clicks
- What supersedes content-and-intent.md's title formula
- Sources

Other parts of the same original file: [titles-and-serp-tests.md](titles-and-serp-tests.md).

<!-- /split-header -->
## Metadata change lifecycle

Run this whenever a title or description changes on more than one URL. It comes before the per-template test further down: the lifecycle makes sure the right field is changed in the right place; the test then tells you whether the change helped.

**Evidence rules** `[unvalidated house heuristic]`

- Read production metadata from the server-returned HTML of the live URL; never infer it from source code. Layout inheritance, CMS fallbacks, route precedence and template interpolation can make code and production disagree in either direction.
- A sitemap alone is only one piece of evidence and never the full inventory. Gather URLs from six places: navigation, footer, hubs, the sitemap, the route table and production URLs. When a generated family is large, look at its template and a set of representative samples, not each URL.
- Edit the source of truth (metadata API, layout, CMS field), never the generated output.

**Steps** `[unvalidated house heuristic]`

1. **Classify.** Map each URL to its page type. Flag metadata that is missing, duplicate, stale, inherited, fallback or cross-locale; old brand names; claims carried over from a sibling page.
2. **Find the template suffix first.** If the layout already appends `| Brand`, a title written with the brand in it ships with the brand twice. Check before writing any title.
3. **Name the page's job.** What can this page, and only this page, promise and prove? Use verified product facts only; never invent a differentiator.
4. **Run the [Swap Test](#swap-test).**
5. **Write.**
   - Title: lead with the primary concept where it reads naturally. A title *body* of roughly 60 Latin characters is a warning rather than a gate; the brand suffix is not counted in it, and Google may cut or replace that suffix. With CJK or RTL scripts, judge the rendered width instead of any translated character count. Title and H1 serve one intent; they need not match word for word. Never add a year, number or superlative just for click appeal (superlatives also pass your claims-review gate).
   - Description: open with what separates this page from its siblings. Google sets no limit on meta description length; the snippet is truncated as needed, typically to fit the device width `[documented: https://developers.google.com/search/docs/appearance/snippet, 2026-10-12]`. Add a price, date, author or availability only if the page displays it and it is current (price-staleness guard: skill `seo-content` › comparison-pages). A CTA only where the page has a task.
   - For the title link Google can draw on `<title>`, the page's main visible title, headings, anchor text or `og:title` `[documented: https://developers.google.com/search/docs/appearance/title-link, 2026-10-12]`; snippets come primarily from page content and can differ per search `[documented: https://developers.google.com/search/docs/appearance/snippet, 2026-10-12]`. Aim for a consistent page identity; control over the displayed string is not on offer. The body must substantiate what the description promises.
6. **Localise from target-market queries**, not by translating and truncating. Each locale's URL, canonical, hreflang set and `og:locale` must agree.
7. **Report cannibalisation; do not fix it inside this job.** List the URLs and the evidence, and name the intent they overlap on. Whether to merge or re-target is a separate decision (skill `seo-content` › content-and-intent-2 § Cannibalization).

**Release checks — first the built app, then production** `[unvalidated house heuristic]`. Take representative URLs for each page type and locale and read the initial server response rather than a browser DOM snapshot:

- exactly one effective `<title>` and one intended description;
- no empty, placeholder, duplicate or doubly suffixed output;
- title and H1 share the intent; H2s and body support the promise;
- every canonical, robots, hreflang, OG and Twitter tag points at the absolute URL it is meant to;
- status codes, image URLs, locale output and HTML escaping are right.

Once deployed, check those same URLs again in the raw production HTML. Once Google has recrawled, read query mix, rewrite rate and CTR in GSC with the two-window method in [experiments-and-revert-2.md](experiments-and-revert-2.md). Never promise a ranking or CTR lift.

## Swap Test

`[unvalidated house heuristic]` For every title and description, ask: could it move, unchanged, onto a sibling page? If it could, it carries no page-specific information — add a verified fact about this page or sharpen the task it names. This is the per-URL version of the doorway test in skill `seo-content` › programmatic-seo, and it is step 4 of the lifecycle above.

## Templated metadata at site scale

Bulk metadata jobs — a CSV column poured into a template, or a model asked for "a description for each title" — stamp one shape onto every URL. Reviewing page by page misses it; it only shows up across the whole **site**. Four deterministic string comparisons, no model; the title-prefix comparison runs only when the title is long enough that a sentence would not naturally begin with it `[unvalidated house heuristic]`:

| Rule | Signature | Severity |
|---|---|---|
| templated_metadata | description **opens with the exact title** and **ends in a stock CTA** ("Try it free now.", "Start free!", "Learn more now!") | high |
| description_echoes_title | opens with the title, then adds real information | medium |
| description_duplicates_title | description == title | medium |
| brand_suffix_in_description | the title's `\| Brand` suffix concatenated into the description body | low (generation artefact) |

Per-site report: pages checked, templated count and ratio, and the shared CTA phrases with their counts (e.g. one phrase on 26 URLs). Flag the site as a whole when the ratio is high `[unvalidated house heuristic]` — the source sets no published threshold we can cite.

Evidence position: templated or duplicated metadata is a quality problem `[unvalidated house heuristic]`; the source tool itself does not claim that any Google update targeted it. Google generates title links automatically and may show text other than the `<title>` `[documented: https://developers.google.com/search/docs/appearance/title-link, 2026-10-12]`, and builds snippets primarily from page content rather than the meta description `[documented: https://developers.google.com/search/docs/appearance/snippet, 2026-10-12]`, which is why the remedy is page-specific copy (the [Swap Test](#swap-test)), not a new template. A rewrite is still a change with a revert rule — run it as in [How to run a title test](#how-to-run-a-title-test).

Mowei application `[unvalidated house heuristic]`: the template echo turns up first on programmatic comparison pages (`/comparar/x-vs-y`) and municipality pages. Before each programmatic release, pull every title/description pair from the sitemap URLs and run all four rules.

## Per-template tests, not rules

Every entry is a hypothesis for *one* template on *your* site.

- **Brand suffix.** #162 (prepend brand, +15% organic sessions, 1 controlled, searchpilot 2024) and #163 (remove brand + pipes, +63.5% *impressions*, 1 before/after with control, 23 blog pages, confounded with keyword insertion) — both EXPERIMENTAL, opposite directions, different metrics. The formula's flat "unknown brand — drop the suffix" is one side of an untested pair. Test per template: intent vs navigational, listings vs articles.
- **All caps.** #159 (+17.5% organic sessions, 2 samples, retail) and #170 (+14%, 1 sample, travel) — both searchpilot, EXPERIMENTAL. On a YMYL comparison brand a tone cost is likely and unmeasured `[hypothesis]`; one non-money template first, if at all.
- **Question titles.** #169 (+5% organic sessions, 1 controlled). Informational routes whose query is a question.
- **"Updated Daily".** #166 (+11% organic sessions, 1 controlled, search-results pages). Only where the page is regenerated daily from a live source; a title claim is a date claim — Google's helpful-content questions warn against changing a page's date to make it seem fresh when the content has not substantially changed `[documented: https://developers.google.com/search/docs/fundamentals/creating-helpful-content, 2026-10-12]`.
- **Remove "Compare".** #164 (+24% organic sessions, 1 controlled, searchpilot 2025). For a site whose every listing route begins "Comparar", the most direct question in the index. One sample: run it on one `/comparar` template with a holdout.
- **Remove extra keywords** (#172, +11%), **redundant location qualifier** (#171, +5%, median +8%, 2 controlled), **CTA at the start** (#167, +18%, replacing a price phrase), **"best" on listings** (#161, +11% — superlative gate first), **remove long meta descriptions** (#126, +4.2%) — all EXPERIMENTAL, all searchpilot, all "shorten toward what the query carries", each a template test with a control.
- **The one MAINSTREAM rewrite** — #168, +14.2 ranking positions, 6 samples, 0 controlled, bundled with schema, links and alt text — and **the bundle** #160 (+52% conversions, 15 samples, 1 controlled) support only "sites that rewrote titles among other things reported gains". Neither measures a title.

## How to run a title test

The six-part recipe filled in for a title template. The statistics — MDE, power, the two-proportion test, the `inconclusive` rule — live in `experiments-and-revert-2.md`; cross-reference, do not restate.

1. **When it applies.** One template (e.g. `/comparar/energia/*`), ≥ 40 URLs `[unvalidated house heuristic]` with stable impressions over the prior 28 days, no other change scheduled on those URLs in the window. URL count is not power: the click thresholds in `experiments-and-revert-2.md` decide whether the test can read.
2. **Before you start.** Export 28 days of GSC clicks, impressions, CTR, position per URL. Sample the displayed title for ≥ 10 URLs per arm `[unvalidated house heuristic]` and log it. Stratified random assignment on impressions; check pre-period parity before touching anything.
3. **What to change.** The one title variable under test — suffix, "Comparar" prefix, price segment. Nothing else in `<head>`, `<h1>` or body.
4. **What to keep.** Control titles untouched. Meta descriptions, headings, schema, internal links, URLs identical across arms.
5. **What to measure.** Re-sample the displayed title after indexing and log the rewrite rate per arm. Keep every assigned URL in the primary read (intention-to-treat): a rewrite is something the treatment can cause, so dropping rewritten URLs keeps only the treated pages where it took and fakes a win. Then clicks (not CTR alone — impressions move too), treatment vs control, at the click thresholds in `experiments-and-revert-2.md`. A read restricted to URLs showing the intended title, if wanted, is secondary and reported as such.
6. **When to revert.** Pre-declared: clicks or sessions below control past the declared bound; a rewrite rate above the control's; or, for any price or date claim, a single stale value seen in the SERP. Revert the template, keep the log.

## Answer formatting and SERP features

**Answer-format entries (#1–#7).** #7 (structure page text for answer box placements, MAINSTREAM, +98.6% organic sessions, 7 samples, 0 controlled, bundle) is the best-supported direction: answer the query in the opening paragraph, convert key points into ordered lists or tables. #5 (question headings + schema, MAINSTREAM, +65% impressions, 4 / 0), #4 (simplify copy, MAINSTREAM, +344% citation rate, 3 / 0), #2 (+280% AI citations) and #3 (5x AI citations) — EXPERIMENTAL, one controlled test each, same author — and #6 (EXPERIMENTAL, +187% AI citations headline, controlled sample +3%) all point the same way and none isolates a variable. #25 (explanatory block for featured snippets, EXPERIMENTAL, +25% organic sessions, 1 of 2 controlled) is the featured-snippet version. Carry #7 as `[measured: MAINSTREAM, n=7, c=0]` and #4 as `[measured: MAINSTREAM, n=3, c=0]` — bundles, direction only; "engines lift well-structured answers" is `[hypothesis]`. Google's AI guidance says no new markup or file format is required to appear in its generative features `[documented: https://developers.google.com/search/docs/appearance/ai-features, 2026-10-11]`.

**Rich-result eligibility register** — verify against Search Central before promising any SERP appearance; retirements are frequent:

| Feature | Status | Label |
|---|---|---|
| FAQ rich results | Gone 7 May 2026 (gov/health only since Aug 2023) | `[documented: https://developers.google.com/search/updates, 2026-10-11]` (7 May 2026) `[documented: https://developers.google.com/search/blog/2023/08/howto-faq-changes, 2026-10-11]` (gov/health, Aug 2023) — supersedes the rich-result mechanism behind #1, #135 and the FAQ part of #141 |
| HowTo rich results | Gone Sept 2023 | `[documented: https://developers.google.com/search/blog/2023/08/howto-faq-changes, 2026-10-11]` |
| Sitelinks search box (`SearchAction`) | Removal from results began 21 Nov 2024 (announced 21 Oct 2024) | `[documented: https://developers.google.com/search/blog/2024/10/sitelinks-search-box, 2026-10-12]` |
| Product / Review snippets | Documented as current; product rich results support only pages focused on a single product (or its variants), not listing or category pages | `[documented: https://developers.google.com/search/docs/appearance/structured-data/product-snippet, 2026-10-12]` |
| EEA aggregator units | Only for hotel, flight, long-distance train or bus, product and local-business queries; the aggregator must be approved as a Vertical Search Service and supply data by feed or API. Energy, insurance and banking queries are not on the list, so "comparison platform" alone establishes nothing | `[documented: https://developers.google.com/search/docs/appearance/aggregator-unit, 2026-10-12]` |

Existing `FAQPage`/`HowTo` markup is harmless; stop counting it as a win.

## CTR — optimise qualified clicks

A title that stops attracting the wrong click lowers CTR and improves the business. Removing a static price (#157/#158) or a misleading superlative cuts clicks from users who would have bounced; the study's sessions metric never sees downstream quality. Measure what the page exists for — completed comparisons, leads, applications — alongside clicks, and accept a CTR fall when the lost clicks were unqualified `[unvalidated house heuristic]`. skill `seo-content` › gsc-page2-audit §2 gives the bands: a "Snippet problem" URL (ranking, never clicked) is where a title test earns most; an "Opportunity" URL (position 8–20) is where answer-format work earns more.

## What supersedes content-and-intent.md's title formula

The formula in skill `seo-content` › content-and-intent ("Primary Keyword + Differentiator | Brand", ≤60 characters, one intent, important term early, match the page) stands as a **drafting aid**. Two of its rules are superseded by the ledger. The flat **"unknown brand — drop the `| Brand` suffix"** is one side of an untested pair (#162 vs #163, both EXPERIMENTAL, opposite directions) and becomes a per-template test. Any reading of **"one clear intent — avoid stuffing" as "strip synonyms and secondary terms"** is contradicted by #165 (AVOID, −27% organic sessions) and #173 (AVOID, −20%): prune boilerplate (#172), keep the descriptive variants the query carries. The 60/160-character limits are display heuristics, not requirements — Google sets no length limit on either, truncates the displayed text as needed to fit the device width, and generates title links automatically `[documented: https://developers.google.com/search/docs/appearance/title-link, 2026-10-12]` `[documented: https://developers.google.com/search/docs/appearance/snippet, 2026-10-12]`.

## Sources

- AgriciDaniel/claude-seo@scripts/metadata_template.py:1-74 (phase-2 adapted file research/adapted/AgriciDaniel__claude-seo/templated-metadata-and-section-risk-checks.md) — section 1 only: the four templated title/description rules, the per-site report, the evidence position and the Mowei application. INTEGRATE, MIT.
- kostja94/marketing-skills@skills/seo/on-page/metadata/SKILL.md, kostja94/marketing-skills@skills/seo/on-page/title/SKILL.md, kostja94/marketing-skills@skills/seo/on-page/description/SKILL.md (phase-2 adapted file research/adapted/kostja94__marketing-skills/metadata-lifecycle-and-swap-test.md) — evidence rules, the seven-step change lifecycle, the Swap Test and the release checks. INTEGRATE, MIT.
