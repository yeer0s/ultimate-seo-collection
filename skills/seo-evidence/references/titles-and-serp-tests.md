# Titles, snippets and SERP tests — the study's title family as a ledger
<!-- split-header: part 1 of 2 of titles-and-serp-tests.md (step-3 original lines 1–80; boundary start) -->
<!-- /split-header -->

## Contents

- Titles are the study's most-tested and most-contradictory family
- Entry-by-entry ledger
- Guardrails (AVOID and IT DEPENDS)

Other parts of the same original file: [metadata-at-scale.md](metadata-at-scale.md).

## Titles are the study's most-tested and most-contradictory family

The index lists **20 title-tag entries** (#154–#173), more than any other family. Of the study's **9 AVOID entries, 5 are titles or meta** — #157, #158, #165, #173 (titles) and #127 (meta descriptions). A sixth, #67 (keyword-stuffed passages, −10% impressions), sits in the GEO family but fails the same way: keyword pressure on copy a human was meant to read. The remaining three AVOIDs (#98 breadcrumbs, #123 maps, #179 search widget) are layout questions.

Three facts govern the rest of this file:

1. **Most title results are EXPERIMENTAL or single-publisher controlled tests.** Eleven of the 20 title entries are EXPERIMENTAL (≤2 independent samples); three of the four title AVOIDs rest on one sample; #154 is one academic paper. Only #155, #160 and #168 reach MAINSTREAM. And **searchpilot.com supplies the controlled test in 21 of the 33 ledger entries below** — one testing platform, one client base (retail, travel, listings). Real split tests, the strongest design the study scores, but they describe one publisher's clients, not the web.
2. **The MAINSTREAM title entries are MAINSTREAM by count, not by design.** #168 (rewrite titles + metas, +14.2 ranking positions) has 6 samples and **0 controlled**; #160 (rewrite titles + restructure + update posts, +52% conversions) has 15 samples and **1 controlled** — the same arxiv paper that is #154 on its own. Neither isolates the title.
3. **Google rewrites titles.** The title link may be generated from the `<title>`, the main heading, anchor text or other on-page text when the `<title>` is judged unsuitable `[documented: https://developers.google.com/search/docs/appearance/title-link, 2026-10-12]`. **Before reading any title test — the study's or yours — confirm the treatment is what the SERP displayed.** A −6% or a +24% measured where Google showed another title measures the deployment, not the wording. Search Console does not report a rewrite rate; sample the live SERP for a stratified set of URLs in each arm and log displayed vs deployed `[unvalidated house heuristic]`.

## Entry-by-entry ledger

Marks, effects, metrics and sample counts as printed. "Controlled" is counted from Evidence Appendix designs (Controlled A/B test, Before/after with control, Quasi-experiment). The catalogue's "on N of M samples" is the number of samples measured in the headline metric, **not** the controlled count — #168 prints "on 2 of 6 samples" while all six sources are before/after, no control.

| # | Tactic (as printed) | Mark | Effect + metric (as printed) | Samples / controlled | Publisher lineage | How to carry it |
|---|---|---|---|---|---|---|
| #154 | Add AI-generated title tags and meta descriptions | ACADEMIC | +10.26% click-through rate | 1 / 1 (arxiv 2025, size not reported); bundle | Same arxiv source is #160's only controlled sample | Machine drafts under human review; one paper. |
| #155 | Add dynamic lowest price details to title tags | MAINSTREAM | +12% organic sessions; range +10% to +17% | 3 / 2 (searchpilot 2023 +12%, 2024 +10%; 1 design unclear +17%) | All searchpilot.com | Testable only with a live price and a staleness guard. |
| #156 | Add emojis to title tags | IT DEPENDS | −6% organic sessions (1 controlled) vs +1,851 impressions (0 controlled) | 3 / 2 (searchpilot 2023 A/B −6%; delante.co 2025 before/after +1,851; searchpilot 2025 A/B direction only) | Positive side is one agency's redesign bundle | Never import; if pressed, run the study's recipe, revert on a sessions fall. |
| #157 | Add product prices to title tags | AVOID | −15% organic sessions | 1 / 1 (searchpilot 2023) | searchpilot.com | Static price tokens out of title templates. |
| #158 | Append static rental prices to location title tags | AVOID | −7% organic sessions | 1 / 1 (searchpilot 2025, 1 page) | searchpilot.com | Same. |
| #159 | Capitalize all text in page title tags | EXPERIMENTAL | +17.5% organic sessions; median +16.5%, range +14% to +18.9% | 2 / 2 (searchpilot 2026 A/B; 2025 quasi-experiment) | searchpilot.com, retail product pages | Retail hypothesis; brand/YMYL tone risk `[hypothesis]`. |
| #160 | Rewrite titles, restructure site, and update posts | MAINSTREAM | +52% conversions; range +20% to +741.5% | 15 / 1 (arxiv +10.26%); 14 before/after | 13 publishers, agency case studies | A direction for a site overhaul; never a title number. |
| #161 | Add best to title tags on product listing pages | EXPERIMENTAL | +11% organic sessions | 1 / 1 (searchpilot 2025, 1 page) | searchpilot.com | "Melhor" is a superlative — your claims review decides first. |
| #162 | Prepend brand name to title tags | EXPERIMENTAL | +15% organic sessions | 1 / 1 (searchpilot 2024, 1 page) | searchpilot.com | Per-template test; opposite of #163. |
| #163 | Remove brand names and pipes from title tags | EXPERIMENTAL | +63.5% impressions | 1 / 1 (hurrdatmarketing 2025, before/after with control, 23 blog pages, 1 month); bundle — keywords inserted at the same time | One agency | Impressions, not clicks; brand removal confounded with keyword insertion. |
| #164 | Remove 'Compare' keyword from title tags | EXPERIMENTAL | +24% organic sessions | 1 / 1 (searchpilot 2025, 1 page) | searchpilot.com | The direct question for every `/comparar` route — test, do not assume. |
| #165 | Remove synonym keywords from listing title tags | AVOID | −27% organic sessions; reported −27% to −20%, one source, 4 values | 1 / 1 (searchpilot 2025) | searchpilot.com | Keep secondary terms and synonyms in listing templates. |
| #166 | Replace month and year with Updated Daily in titles | EXPERIMENTAL | +11% organic sessions | 1 / 1 (searchpilot 2023, search-results pages) | searchpilot.com | Only where the page genuinely refreshes daily. |
| #167 | Put booking call to action at start of titles | EXPERIMENTAL | +18% organic sessions | 1 / 1 (searchpilot 2023, location pages; replaced a leading price phrase) | searchpilot.com | Travel template; the control was itself a price phrase. |
| #168 | Rewrite title tags and meta descriptions | MAINSTREAM | +14.2 ranking positions; median +10.3 positions on 2 of 6 samples, range +5.4 to +15.2 | 6 / 0 — all before/after; bundle with structured data, internal links, alt text; 2018–2026 | 6 agencies | MAINSTREAM by count only; the ranking figure is two uncontrolled agency reports. |
| #169 | Rewrite title tags into questions | EXPERIMENTAL | +5% organic sessions | 1 / 1 (searchpilot 2026, 1 page) | searchpilot.com | Informational templates, small effect, one test. |
| #170 | Rewrite title tags in all uppercase letters | EXPERIMENTAL | +14% organic sessions | 1 / 1 (searchpilot 2025, travel listings) | searchpilot.com | As #159. |
| #171 | Remove airport location word from page title tags | EXPERIMENTAL | +5% organic sessions; median +8%, range +5% to +11% | 2 / 2 (searchpilot 2023) | searchpilot.com | "Remove what the query does not carry", per template. |
| #172 | Remove extra keywords from title tags | EXPERIMENTAL | +11% organic sessions | 1 / 1 (searchpilot 2025, 1 page) | searchpilot.com | Pruning boilerplate is not pruning synonyms (#165). |
| #173 | Target high volume keyword variants in title tags | AVOID | −20% organic sessions; reported −27% to +9%, crosses zero, no median | 4 / 2 (moz 2021 A/B −20%, 1 page; searchpilot 2025 A/B −11%; moz 2021 before/after +9%, 200 URLs; searchpilot 2026 design unclear −27%); bundle with metas | moz.com + searchpilot.com | Both controlled samples negative; keep the specific label. |
| #126 | Remove long meta descriptions from listing pages | EXPERIMENTAL | +4.2% organic sessions | 1 / 1 (searchpilot 2025, 1 page) | searchpilot.com | Letting Google extract the snippet is a legitimate template test. |
| #127 | Swap numbers for emoji digits in meta descriptions | AVOID | −5% organic sessions; reported −9% to −4%, one source, 4 values | 1 / 1 (searchpilot 2023) | searchpilot.com | Plain numerals. |
| #76 | Update article title markup to primary heading tags | EXPERIMENTAL | +6.2% organic sessions | 1 / 1 (moz 2023 A/B, 8 weeks) | moz.com | Visible article title as `<h1>`; cheap, one test. |
| #1 | Add FAQ content and FAQ schema to category pages | MAINSTREAM | +9% organic sessions; median +112% across 6 samples, range +9% to +350% | 15 / 2 (searchpilot 2023 A/B +9%; socialanimal 2026 with control +11); 13 before/after; bundle | 13 publishers; headline from searchpilot | Rich result retired 7 May 2026; the FAQ *content* half remains testable. |
| #2 | Place direct answers in opening paragraphs | EXPERIMENTAL | +280% citation rate (AI citations) | 1 / 1 (guptadeepak 2026 A/B, 30 URLs, 60 days) | One author | Cheap on informational pages; one test. |
| #3 | Format content as discrete factual statements | EXPERIMENTAL | 5x citation rate (AI citations) | 1 / 1 (guptadeepak 2026 A/B, 30 URLs) | Same author as #2 | One lineage with #2. |
| #4 | Simplify copy and align intent on key articles | MAINSTREAM | +344% citation rate; reported +49% to +344%, one source, 4 values | 3 / 0 (seerinteractive 2025, 11 pages; two direction-only); bundle | 3 publishers | Direction only. |
| #5 | Add question headings and schema markup | MAINSTREAM | +65% impressions; median +159%, range +65% to +253% | 4 / 0 — all before/after; bundle | 4 publishers | Question sub-headings + summary paragraphs; the schema half earns no rich result now. |
| #6 | Reformat main pages into questions and FAQ schema | EXPERIMENTAL | +187% citation rate (AI citations) | 2 / 1 (searchpilot 2023 A/B **+3%**; m8l 2025 before/after +187%); bundle | Headline from the uncontrolled side | Read the controlled +3%. |
| #7 | Structure page text for answer box placements | MAINSTREAM | +98.6% organic sessions; median +198.4%, range +25% to +500% | 7 / 0 (6 before/after, 1 design unclear — searchpilot 2024 +25%); bundle | 7 publishers | Best-supported answer-format direction — still zero controlled. |
| #25 | Add targeted explanatory text for featured snippets | EXPERIMENTAL | +25% organic sessions; median +28.2%, range +25% to +31.4% | 2 / 1 (searchpilot 2024 A/B +25%; seoworks 2026 before/after +31.4%) | searchpilot + one agency | Concise answer block under the H1; pages already ranking 2–8. |
| #67 | Add keyword-stuffed passages to web page content | AVOID | −10% impressions | 1 / 1 (arxiv A/B, 1,000 queries; GEO benchmark, "not a live search console") | Academic benchmark | Remove forced keyword lists; lab metric, direction transfers. |
| #79 | Replace screenshots with high-contrast visuals | EXPERIMENTAL | +20% click-through rate | 1 / 1 (splitmetrics 2025 A/B, "1 user") | SplitMetrics is an **app-store** listing test platform | Store-listing CTR, not Google SERP CTR — do not carry into a snippet plan. |

## Guardrails (AVOID and IT DEPENDS)

**Static prices in titles — AVOID.** #157 (−15% organic sessions, 1 controlled) and #158 (−7%, 1 controlled) each removed a fixed price string from a template and recovered. #155 (MAINSTREAM, +12% organic sessions, 3 samples, 2 controlled, all searchpilot) is a different treatment: a JavaScript-appended *current lowest active price* on category pages. The distinction is freshness. For mowei, tariffs move with ERSE decisions and provider repricing — **a cached title showing a stale "desde 0,14 €/kWh" is a YMYL trust defect**, not a CTR tweak. If #155 is tested: the price reads from the same live source as the comparison table; the title regenerates on every price change (no ISR or fetch-cache older than the feed); a staleness guard drops the price segment entirely when the source exceeds the guard window `[unvalidated house heuristic]`. Static is refused; dynamic-with-guard is testable.

**Emojis — IT DEPENDS (#156).** Of the 3 samples, 2 are controlled A/B tests, both searchpilot.com: the 2023 test reports **−6% organic sessions**, the 2025 test direction only. The +1,851 impressions side is one agency's redesign bundle, 0 controlled; the study prints "no pooled figure — averaging the two sides would describe neither". Ask the entry's question — emojis alone, or with a content and structural overhaul? — and if the client insists, run the study's recipe: randomised subset, control untouched, sessions vs control, revert to text-only if sessions fall. YMYL and brand tone are a separate objection `[hypothesis]`; keep it apart from the evidence.

**Emoji digits in meta — AVOID (#127, −5% organic sessions, reported −9% to −4%, 1 controlled).** Plain numerals.

**Removing synonyms — AVOID (#165, −27% organic sessions, 1 controlled).** #172 (+11%, remove boilerplate and repeated brand modifiers) is not the same operation: it removed noise, #165 removed meaning.

**Swapping to high-volume variants — AVOID (#173, −20% organic sessions).** Four samples; both controlled ones negative (−20%, −11%), the one positive uncontrolled. Keyword volume is a demand signal, not a title instruction.

**Keyword-stuffed passages — AVOID (#67, −10% impressions, 1 controlled, GEO benchmark).** Agrees with the keyword-stuffing refusal in skill `seo-optimizer` § Hard refusals.

