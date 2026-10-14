# Data assets and charts — the text layer machines can cite

## Contents

- When to use this file
- The chart package — nine parts, every time
- Rules for data charts
- A data-page package per vertical
- Sources

## When to use this file

Use it whenever a page puts out **original data**, for instance a tariff comparison, a price index or a survey. People read the chart; crawlers, answer engines and image search read the text that surrounds it. Everything here is `[practitioner]`. The source's slogan that AI engines cite text rather than pixels is a story about mechanism, not a measurement, and no effect size is attached to any step.

## The chart package — nine parts, every time

1. **Takeaway heading** — an H2 on a dedicated data page, an H3 inside an article. State the finding as a sentence that includes its number ("Electricity tariff X is the cheapest for 3.45 kVA in 9 of 12 months"), not a label such as "Tariffs by month".
2. **Key-finding paragraph above the chart, at most 60 words.** It names its subject instead of using pronouns, carries at least one number together with the sample and the period, and still makes sense when read alone.
3. **The chart itself.** Prefer inline SVG whose labels are real `<text>` elements rather than text flattened into paths; give it `role="img"` plus `<title>` and `<desc>` referenced through `aria-labelledby`. Never let colour carry meaning by itself; keep text contrast at ≥ 4.5:1 and marks at ≥ 3:1. For palette and mark choices on Mowei, the dataviz skill applies.
4. **Source and method line under the chart**, always: `Source: [org], [year]. N=[n]. Method: [one sentence].`
5. **A "what this means" paragraph** of two or three sentences giving the interpretation and saying whom it applies to.
6. **An HTML data table placed in the server-rendered DOM**, and not lazy-loaded through JavaScript: `<caption>`, `<thead>`, `<th scope>`, units in the headers, and values that match the chart exactly.
7. **A download link** to the same data as CSV.
8. **`Dataset` JSON-LD** with `name`, `description` (the key-finding text), `temporalCoverage`, `variableMeasured` (`PropertyValue` + `unitText`), `creator`, `datePublished`, `license` and `distribution` (`DataDownload`, `text/csv`). `Dataset` markup is only used by **Google Dataset Search**, not Google Search `[documented: https://developers.google.com/search/updates, 2026-10-11]` (eligibility in skill `seo-technical` › schema-reference), so promise nothing for web Search.
9. **Image metadata:** a descriptive, hyphenated filename; alt text that states the conclusion in roughly 125 characters or fewer, with the table serving as the long description; a `<figure>` with `<figcaption>`; the first visible chart never lazy-loaded; and an entry in the image sitemap.

## Rules for data charts

- A chart earns its place only if it carries data, explains a process or proves a claim; decorative charts are out.
- Every number needs a source someone can check; run the pre-publish claim check in skill `seo-content` › publishing-gates over the whole package.
- Link the data page from every guide and comparison page that uses the number, using the finding itself as the anchor text.
- When the data refreshes, re-date the whole package. A table still saying "2025" and left on a live tariff page counts as a trust defect for a YMYL site.

## A data-page package per vertical

`[hypothesis]` Every Mowei comparison vertical already computes figures that nobody else publishes — monthly counts of which tariff is cheapest, fee spreads between banks, and similar. Turning one of these per vertical into a dated, downloadable dataset is the "original data" lever on this skill's practitioner list of source preferences (see [ai-retrieval-and-citation.md](ai-retrieval-and-citation.md#how-ai-answer-engines-pick-sources)).

What each vertical's package contains:

- dated one-line findings, each written as a takeaway heading plus key-finding paragraph;
- the HTML table in the DOM;
- the CSV download;
- `Dataset` JSON-LD as in step 8 above.

Pair the original data with a stat page, so that links and answer-engine lifts point at Mowei rather than at a site that re-reported the number. Measure the outcome with the prompt panel and ladder in [ai-citation-measurement.md](ai-citation-measurement.md) — never with a forecast. Any vertical-specific wording or figure goes through your own claims review before publication.

## Sources

- onvoyage-ai/gtm-engineer-skills@create-geo-charts/SKILL.md:10, :48-54, :128-134, :146-284, :374-398 (phase-2 adapted file research/adapted/onvoyage-ai__gtm-engineer-skills/chart-text-layer-package.md) — the nine-part text-layer package, table and Dataset rules, alt-text and figure rules, chart rules, the per-vertical idea. INTEGRATE, MIT.
- Research REPORT §7 idea 9 — a data-page package per vertical (dated findings, HTML table, CSV, Dataset JSON-LD, paired stat page).
