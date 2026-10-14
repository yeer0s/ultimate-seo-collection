<!-- split-header-2: part 2 of 2 of briefs-and-personas.md (original lines 131–213; boundary H2) -->
# Briefs and personas (2 of 2) — competitor filtering, output shape, personas, wireframes
## Contents

- Competitor filtering before any gap analysis
- Brief and outline output shape
- Personas: derive from signals, never invent
- Wireframes: IST/SOLL and the concrete-placeholder rule
- Cross-references
- Sources

Other parts of the same original file: [briefs-and-personas.md](briefs-and-personas.md).

<!-- /split-header-2 -->
## Competitor filtering before any gap analysis

`[practitioner]`. Score gaps only against **real business competitors**. First decide what the client's business is: a domain that sells or compares the same thing the client does is a competitor and stays, whatever bucket below it falls in (for a comparison platform such as Mowei, other comparison aggregators — `comparaja.pt`, `kuantokusta.pt` — are the core competitor set, as in [keyword-research-2.md](keyword-research-2.md#mowei-specific-keyword-research-playbook)). Then filter the rest of the SERP by category: encyclopedias and health references; social platforms (including Reddit, Quora, YouTube, LinkedIn); content platforms (Medium, Substack, site builders); search engines; marketplaces; forums and Q&A; news and media; data platforms (Statista, IBISWorld, SimilarWeb); directories and review sites; comparison aggregators; job boards; SEO-tool blogs; AI platforms; any `.gov*` domain; any `.edu`/`.ac.*` domain.

Also drop URLs on otherwise valid domains matching `/tag/`, `/tags/`, `/author/`, `/category/`, `/archive/`, `/feed/`, `/rss/`, `/wp-json/`, `/wp-admin/`, `/login`, `/signup`, `/register`, `/cart`, `/checkout`, `/terms`, `/privacy`, `/cookie-policy`, `/disclaimer`, `/sitemap`, `/robots.txt`.

Then: if fewer than 3 real competitors remain, **say so** — a thin competitive landscape is a finding, not a reason to pad the table with Wikipedia. Never count a filtered domain in the competitor analysis.

Two corrections on import. (1) The source has a typo — `screaming frog.co.uk` at `excluded-domains.md:40` should be `screamingfrog.co.uk`; the space makes the entry unmatchable, so that domain was never actually filtered. (2) The list is US/AU-centric and **incomplete for Portugal** `[practitioner]`: a pt-PT run also needs the local news and portal domains (`publico.pt`, `eco.sapo.pt`), the `.pt` comparison aggregators (filtered only when the client is not itself a comparison business), and the regulators (`erse.pt`, `anacom.pt`, `bportugal.pt`, `asf.com.pt`) — regulators belong in the `.gov` bucket: cite them, never score them as competitors. When the client is a comparison platform, the comparison-aggregator bucket is not filtered: those sites are its direct competitors.

## Brief and outline output shape

`[practitioner]`. The section list is substantially the generic template at `content-and-intent.md#content-brief-template`; three additions are worth carrying.

**The annotated outline.** Every H2/H3 carries a per-section word count, a format note (table, definition box, bullet list), a snippet target where one is winnable, and its own keyword guidance. That is what separates a brief from a list of headings.

**The competitor table.** URL, key H2s, estimated words, score, main gap. The 4 axes of 1-10 (depth, formatting, SEO, UX) and the gap priority `Impact × Competitive Advantage ÷ Effort` are both `[unvalidated house heuristic]` — equal weighting by assumption, and a formula multiplying three unmeasured estimates. Publish the inputs beside any priority number.

**Outline-only mode.** Drop the competitor table, gaps, information-gain and E-E-A-T sections; keep H1, slug, word-count target and the annotated heading tree with a writing note per section.

Word-count targets stay **production estimates for costing, never ranking targets** — the framing `content-and-intent.md` already uses. Quote the competitor average beside your number so its origin is visible.

## Personas: derive from signals, never invent

`[practitioner]`. The single rule worth importing from the persona material: **every persona must trace back to a specific signal cluster.** The validation checklist enforces it — no invented personas, 4 to 7 of them, each carrying the SERP evidence that generated it, scores citing page evidence rather than numbers alone, and the weakest persona addressed first.

| Signal source | What it reveals | Example persona |
|---|---|---|
| PAA question cluster | Knowledge gaps by audience | Beginner, Technical evaluator |
| Ad copy segments | Commercial targets and objections | Budget buyer, Enterprise buyer |
| Related-search themes | Journey-stage groups | Researcher, Comparison shopper |
| SERP result types | Consumption preference | Visual learner, Data-driven analyst |
| Featured-snippet format | Expected answer style | Quick-answer seeker |

`[practitioner]` — the same signals drive user stories in the form *"As a [persona], I want to [goal], because [emotional driver], but I'm blocked by [barrier]"*, each citing at least one observed signal. Signal → emotional state: "is X safe/legitimate/scam" in PAA → sceptical; many comparison queries → overwhelmed by choice; basic "how to" dominating PAA → confused; high ad density plus shopping results → ready to buy; "[X] not working" → frustrated with the current solution. Signal → barrier → what the page must carry: unanswered PAA → a complete answer in the first scroll; ads leaning on trust badges → social proof and credentials; many "vs"/"best" related searches → explicit differentiation or a recommendation; cost-and-free-alternative PAA → transparent pricing and value justification; setup-related "how to" → a step-by-step or a tool; "instant"/"today" ad copy → quick-win content.

Two SERP-format readings are worth keeping as hypotheses to test, not diagnoses: `[hypothesis]` **no featured snippet at all may mean no format has won yet** — possibly an opening; and `[hypothesis]` **if the AI Overview cites sources but not you, the content may not match what the answer synthesises**. Before prescribing a rewrite, check eligibility first (indexed, snippet-eligible) and repeat the observation over several days: AI Mode and AI Overviews may use different models, so the links shown vary, and a compliant page is not guaranteed to be served `[documented: https://developers.google.com/search/docs/appearance/ai-features, 2026-10-14]`.

### The persona scoring rubric is a house heuristic

`[unvalidated house heuristic]` — four dimensions (relevance, clarity, trust, action) at **25 points each for 100 per persona**, banded 80-100 / 60-79 / 40-59 / 0-39. Nothing establishes the equal weighting or the band edges. The *questions* survive without the arithmetic: does the page address this persona's specific need; can they find the answer in roughly ten seconds; are the trust signals the ones **this** persona needs; is there a next step matched to their journey stage. Report the four answers with evidence rather than a number; if a number is reported, print the rubric beside it.

The aggregation advice — weight personas by the intent mix visible in the SERP, then fix the weakest high-weight persona first plus any dimension weak across all personas — is sound prioritisation `[practitioner]` independent of the point values.

## Wireframes: IST/SOLL and the concrete-placeholder rule

`[practitioner]`. Express the recommendation as two structures — **IST** (the page now: above-fold elements with content quoted, sections with word counts, plus an explicit "missing from SERP expectations" list) and **SOLL** (what it should be: a semantic section outline per page type, mobile-first at 375px, the single most critical element inside the first ~600px). The eight SOLL skeletons match the eight types in `./page-types-and-serp-clustering.md`.

What makes the output actionable is the placeholder discipline: **a placeholder must be concrete enough to build without a follow-up question.**

| Vague | Concrete |
|---|---|
| "Add a CTA" | "Add a 'Simular agora' button below the hero, linking to /ferramentas/salario-liquido" |
| "Include social proof" | "Add 3 regulator marks (ERSE, ANACOM, Banco de Portugal) plus the methodology link" |
| "Add an FAQ section" | "Add 5 FAQs taken from PAA: 'Quanto custa mudar de fornecedor?', …" |
| "More content" | "Add a 400-word section under H2 'Como funciona o cálculo' with the worked example" |

A wireframe full of "improve trust" is a to-do list nobody can action; the specificity is the deliverable.

## Cross-references

- `content-and-intent.md#content-brief-template` — the generic brief template. Fill it using the mode, rules and per-type variants above; not restated here.
- `content-and-intent.md#page-types-and-their-jobs` — page type → business role and conversion goal.
- `./page-types-and-serp-clustering.md` — classifying the page type a brief is written for, and the SERP-consensus read behind "what format Google rewards".
- skill `seo-evidence` › titles-and-serp-tests — title and meta formulas, and which rich results still exist (the FAQPage position above).
- `keyword-research-1.md` — sourcing candidate keywords; skill `seo-ai-search` › ai-retrieval-and-citation — why information gain matters to answer engines.
- Consumer-seat evaluation of a live surface is **not** in scope here — that is `consumer-lens` and `measured-journeys`, which test real people against a real page.

## Sources

- claude-seo@skills/seo-content-brief/SKILL.md:26-38 — improve vs new-page modes. `[practitioner]`
- claude-seo@skills/seo-content-brief/SKILL.md:72-94 — Website Relevance Rule, Site Structure Coverage Rule, output-language rule. `[practitioner]`, highest-value import in this file.
- claude-seo@skills/seo-content-brief/SKILL.md:145-152 — information-gain requirement. `[practitioner]`
- claude-seo@skills/seo-content-brief/SKILL.md:169-229 — brief and outline-only output structures; competitor 4×10 score and `Impact × Advantage ÷ Effort` as `[unvalidated house heuristic]`.
- claude-seo@skills/seo-content-brief/references/page-type-templates.md:1-153 (source dated 2026-04-17) — 10 per-page-type brief variants with schema and keyword placement. `[practitioner]`; the FAQ-rich-result retirement it cites is provenance only (dated labels: skill `seo-technical` › rendering-and-sitemaps).
- claude-seo@skills/seo-content-brief/references/keyword-density.md:1-30 — density as an internal readability heuristic, explicitly not a Google rule; framing preserved on import.
- claude-seo@skills/seo-content-brief/references/excluded-domains.md:1-64 — competitor exclusion categories and path patterns. `[practitioner]`; `screaming frog.co.uk` typo at `:40` corrected to `screamingfrog.co.uk`, and a Portugal-specific extension added as `[practitioner]`.
- claude-seo@skills/seo-sxo/references/persona-scoring.md:8-35, 163-170 — signal→persona table and the no-invented-personas validation rule. `[practitioner]`. Lines 39-116 (4×25-point rubric) carried as `[unvalidated house heuristic]`.
- claude-seo@skills/seo-sxo/references/user-story-framework.md:1-139 — story format, signal→emotional-state and signal→barrier mappings. `[practitioner]`
- claude-seo@skills/seo-sxo/references/wireframe-templates.md:1-170 — IST/SOLL structures and the concrete-placeholder rule. `[practitioner]`; examples re-written for a Portuguese comparison surface.
- AgriciDaniel/claude-blog@skills/blog/references/research-quality.md (v2.2.0; method itself adapted from mvanhorn/last30days-skill v3.2.1, MIT) (phase-2 adapted file research/adapted/AgriciDaniel__claude-blog/research-quality-and-echo-clustering.md) — Research before the brief: echo clustering, five checks, pre-flight traps, entity decomposition, freshness floor. INTEGRATE, MIT.
- coreyhaines31/marketingskills@skills/content-strategy/SKILL.md:56-58, 129-144 (phase-2 adapted file research/adapted/coreyhaines31__marketingskills/link-earning-formats-and-information-gain-gate.md) — pointer only to the information-gain gate integrated in skill `seo-authority` › authority-links-and-pr. INTEGRATE, MIT.
