# Measurement gates and delivery checklists
<!-- split-header: part 1 of 2 of measurement-gates-and-checklists.md (step-3 original lines 1–117; boundary start) -->
<!-- /split-header -->

## Contents

- The data-sufficiency gate — a rule this skill adopts
- Confidence-weighted source cascades
- Pre-delivery review checklist
- Structured audit envelope
- Report skeletons
- Tiered capability detection, disclosed before the run
- Sources

Other parts of the same original file: [measurement-gates-and-checklists-2.md](measurement-gates-and-checklists-2.md).

## The data-sufficiency gate — a rule this skill adopts

**No composite score unless N of M inputs carry real data. Otherwise print `INSUFFICIENT DATA (X/M)` and name every missing input.** `[practitioner]`

The pattern is imported from a backlink-health scorer, where it is stated concretely: seven weighted factors, and a numeric 0–100 score is produced only when **four or more of the seven** have at least one data source; below that the output is the literal string `Backlink Health Score: INSUFFICIENT DATA (X/7 factors scored)`, followed by the individual factor scores that *are* available with their source and confidence, plus a pointer to the setup command that would raise the count `[practitioner]`.

Generalised for this skill, the gate has four parts, all of which must be present or the gate is decorative:

1. **Declare M before you run.** The denominator is the set of inputs the composite claims to summarise, fixed in advance. A denominator chosen after the fetches is a denominator chosen to pass.
2. **Declare N as a floor, not a target.** The imported instance uses 4/7 — a hair over half. Whatever floor you pick, it belongs in the output next to the score, because the reader cannot otherwise tell a 62/100 built on seven inputs from a 62/100 built on four.
3. **Below the floor there is no number — not an approximate one.** The source repo states this as a MUST NOT and explains why: "A numeric score with fewer than 4 data sources is **misleading**: it implies poor health when the reality is that we simply lack data" `[practitioner]`. It goes further for its weakest source — when a bulk crawl corpus is the only thing available it forbids *any* number, per-factor or otherwise, and requires the literal token `Not Assessed` in place of every figure `[practitioner]`.
4. **Redistribute the surviving weights proportionally** when you are above the floor and some inputs are missing, and say that you did `[practitioner]`.

**Make the gate machine-checkable, because prose alone did not hold.** The same repo records that this exact rule "has been stated in this skill before and was violated anyway, so it is now checkable", and routes every report through a validator whose `source_score_consistency` check returns `status: FAIL` when a numeric score is present but no scoreable source supplied data, or when any finding marked `source: not-assessed` carries a numeric `score`, `value` or `health_score`; on FAIL the report is not presented `[practitioner]`. That is the transferable idea: **a gate that only lives in an instruction file is an instruction, not a gate.** The equivalent here is a small validator over the JSON envelope below, run before any report reaches a human.

Two failure modes to watch for, both of which this skill has seen elsewhere: a gate whose all-clear is unreachable (test that it can *pass*, not only that it fires), and a gate that reports an environment fact — an unconfigured API, a JS-rendered page — as a product defect. The pre-delivery checklist below exists to catch the second.

## Confidence-weighted source cascades

When several sources can fill the same slot, rank them and attach a confidence multiplier per source, so the composite degrades visibly rather than silently. The imported instance pairs each factor with a preference order and a confidence per source `[practitioner]`:

| Factor | Weight | Sources, preference order | Confidence |
|---|---|---|---|
| Referring domain count | 0.20 | DataForSEO > Moz | 1.0 / 0.85 |
| Domain quality distribution | 0.20 | DataForSEO > Moz DA distribution | 1.0 / 0.85 |
| Anchor text naturalness | 0.15 | DataForSEO > Moz > Bing anchors | 1.0 / 0.85 / 0.70 |
| Toxic link ratio | 0.20 | DataForSEO > Moz spam score | 1.0 / 0.85 |
| Link velocity trend | 0.10 | DataForSEO only | 1.0 |
| Follow/nofollow ratio | 0.05 | DataForSEO > Bing details | 1.0 / 0.70 |
| Geographic relevance | 0.10 | DataForSEO > Bing country | 1.0 / 0.70 |

Its global fallback ladder runs: primary paid API (1.0) → Moz (0.85) → Bing, registered properties only (0.70) → a rank-only single-metric fallback (0.60) → bulk crawl corpus, domain-level only (0.50); with a direct verification crawler at 0.95 for checking a *known* link, and "run setup" when nothing is configured `[unvalidated house heuristic]`.

🔴 **The weights and the confidence multipliers are invented.** No study produced 0.20 for toxic-link ratio or 0.85 for Moz; they are one author's ordering `[unvalidated house heuristic]`. The rule this skill adopts is therefore: **publish the weights beside the score, in the same table, every time.** A reader who can see 0.20/0.15/0.10 can disagree with them; a reader shown only "62/100" cannot. Reuse the *shape* (ranked sources, explicit confidence, visible weights) and re-derive the numbers for whatever you are actually scoring — or state plainly that they are house judgment.

The cascade also distinguishes what a source *can* answer from what it is *best* at: a point-in-time crawl corpus cannot produce a velocity trend at all, and the skill says so rather than interpolating one `[practitioner]`.

## Pre-delivery review checklist

Run before any analysis reaches a human; fix findings rather than footnote them. Adapted from claude-seo's backlink skill `[practitioner]`:

**Fact-check every claim**
- Schema claims: did the parser actually return `@type` for each block? A missing `@type` may mean a `@graph` wrapper — valid JSON-LD, not malformed markup.
- "Removed / missing" findings: is the page JS-rendered? If the fetch could not execute JS, label it `unverifiable_js`. **Never report a JS-rendered page as "link removed" or "content missing"** — that is a false negative dressed as a defect.
- "No schema" findings: a fetch that does not render (curl, WebFetch-style tools) may never see JSON-LD that client-side code injects, and some fetch tools drop every `<script>` block while converting HTML to text. A non-rendering fetch can therefore never support "no structured data". Confirm against a rendered DOM (`document.querySelectorAll('script[type="application/ld+json"]')`), the rendered HTML in GSC URL Inspection, or the Rich Results Test; if none of these is available, the finding is `unverifiable_js` `[practitioner]`.
- Heading findings: check whether flagged H1s are counters, stats or hero numerals rather than semantic headings.
- Reciprocal patterns: cross-check outbound links against verified inbound sources before calling a link natural.
- Composite score: are N of M inputs scored? If not, `INSUFFICIENT DATA`, never a number.

**Verify data-source labels**
- Every metric carries a source label *and* its confidence, e.g. `Parsed (0.95)`, `CC (0.50)`.
- Every "not found" distinguishes **not crawled** vs **below threshold** vs **error**. These are three different facts and only one of them is about the site.
- Pages that could not be verified are marked unverifiable, not failed.

**Cross-check consistency**
- Platform/stack detection matches the actual signals found, not the guess.
- Counts in the summary match the underlying verified list.
- No claim appears without a source backing it. Never present inferred data as fact.

## Structured audit envelope

One JSON file per audit, written before any rendering, so a report can be produced even when a live API is unavailable. Shape, from claude-seo's audit skill `[practitioner]`:

```json
{
  "summary": { "health_score": 0, "business_type": "", "top_findings": [], "quick_wins": [] },
  "categories": [
    { "name": "Technical SEO", "score": 0, "what_works": [],
      "findings": [ { "title": "", "severity": "Critical|High|Medium|Low|Info",
                      "description": "Evidence-backed detail", "recommendation": "Specific fix" } ] }
  ],
  "action_plan": { "phases": [
      { "name": "Phase 1: Critical Fixes", "timeframe": "Week 1", "items": [] },
      { "name": "Phase 2: High-Impact Improvements", "timeframe": "Weeks 2-3", "items": [] },
      { "name": "Phase 3: Content & Authority", "timeframe": "Month 2", "items": [] },
      { "name": "Phase 4: Monitoring & Iteration", "timeframe": "Ongoing", "items": [] } ] },
  "artifacts": { "findings_dir": "findings/", "screenshots_dir": "screenshots/" }
}
```

Two properties make it worth copying: `what_works` per category (a findings-only report reads as a hit piece and gets dismissed), and a fixed severity vocabulary. Add one field this skill needs and the envelope lacks: **`inputs_scored: {n, m, missing: []}` alongside `health_score`**, so the gate above is expressible in the artifact rather than only in the prose.

## Report skeletons

Three templates worth keeping as section orders rather than as literal files `[practitioner]`:

- **Core Web Vitals audit** (`cwv-audit-report.md`) — field data first (p75 value, rating, good-threshold, and the good/needs-improvement/poor split per metric for LCP, INP, CLS, FCP, TTFB), with the collection window printed; then lab scores; then a multi-week trend table with direction and earliest→latest; then opportunities with estimated savings; then recommendations. The ordering is the lesson: **field data leads, lab data supports.** Thresholds themselves live in skill `seo-technical` › cwv-field-lab-diagnosis.
- **Search Console performance** (`gsc-performance-report.md`) — summary totals, top queries, top pages, a "quick wins" block scoped to positions 4–10 with high impressions, device breakdown. Its footer carries two disclosures worth imitating: the 2–3 day data lag with a ~16-month window, and a named data-quality caveat for a known logging error period with the affected metrics listed and the unaffected one (clicks) called out.
- **Indexation status** (`indexation-status-report.md`) — verdict counts, per-URL verdict/coverage-state/fetch-state/Google-canonical/last-crawl, a dedicated **canonical mismatch** table (declared vs Google-selected), common issues with priority and action, rich results. Footer states the API's own quota so the reader knows the sample ceiling.

**Adopt the footer habit generally:** every generated report ends with the data's freshness, its window, its known defects, and the quota that bounded the sample.

## Tiered capability detection, disclosed before the run

Detect what credentials and tools are actually present, map that to a tier, and **tell the user the tier before producing anything** — both imported skills state this as a standing instruction `[practitioner]`.

- Local/maps example: Tier 0 free (open POI and geocoding APIs, static checklist, schema generation), Tier 1 adds a paid listings API (geo-grid rank tracking, live profile audit, review intelligence), Tier 2 adds a maps platform key (place details, real-time status) — with a licensing note that the platform's terms restrict storage to the place identifier and cap coordinate caching at 30 days.
- Google-APIs example: Tier 0 API key (PageSpeed, CrUX, CrUX history), Tier 1 adds OAuth or a service account (Search Console, URL inspection, sitemaps, indexing), Tier 2 adds an analytics property, Tier 3 adds ads credentials for volume data.

The value is not the specific ladders, it is the contract: **a report's ceiling is set by the tier, so the tier is part of the report.** An unconfigured credential is an environment fact — it must never surface as a finding about the site.

## Sources
- claude-seo@skills/seo-backlinks/SKILL.md:160, 170-190, 192-236, 254-263, 265-292 — data-sufficiency gate, `Not Assessed` literal, validator gate, confidence-weighted cascade and fallback ladder, pre-delivery checklist (full list in part 2).
- claude-seo@skills/seo-audit/SKILL.md:60-100 — structured audit envelope.
- claude-seo@skills/seo-google/assets/templates/ — three report skeletons.
- claude-seo@skills/seo-maps/SKILL.md:47-66 and skills/seo-google/SKILL.md:47-56 — tiered capability detection.

