# GEO audit and citability — drafting heuristics, llms.txt validation, and how the source tool misleads
<!-- split-header-2: part 1 of 2 of geo-audit-and-citability.md (original lines 1–112; boundary start) -->
<!-- /split-header-2 -->

## Contents

- Citability heuristics — drafting guidance, not a score
- Drafting a liftable passage
- llms.txt — format validation rules
- Brand-presence checklist
- The honest part of the source tool
- Sources

Other parts of the same original file: [geo-audit-and-citability-2.md](geo-audit-and-citability-2.md).

## Citability heuristics — drafting guidance, not a score

A passage scorer defines eleven textual signals across five dimensions `[practitioner]`. **The signals are useful as a drafting checklist. The point values attached to them are `[unvalidated house heuristic]` — invented by the tool's authors, derived from no study, and not reproduced here as targets.**

**Answer quality**
- Open with a definition pattern — "X is a…", "X refers to…", "X means…", "X is defined as…", "in simple terms,…". The scorer matches these as regexes; for drafting, the point is that the first sentence should assert what the thing *is*, not set the scene.
- Put the answer inside the first 60 words. The scorer looks for a copula, a percentage, a currency amount or a magnitude word in that window.
- Phrase the heading as the question the passage answers (the scorer rewards a heading ending in `?`).
- Keep sentences between 5 and 25 words; the scorer computes the share of sentences in that band.
- Attribute claims explicitly — "according to…", "research shows…", "studies found…", "data indicates…".

**Self-containment**
- Keep pronoun density low: the scorer counts it/they/them/their/this/that/these/those/he/she/his/her and rewards a pronoun-to-word ratio below 0.02. The drafting rule is plainer — **a passage lifted out of the page must still name its subject**, so repeat the noun rather than referring back.
- Carry at least three proper nouns (named entities, brands, specific products or standards).
- The scorer also bands passages by word count and gives its highest band to a narrow range `[vendor, no denominator published — do not quote as a target]`. Write to completeness, not to a word count.

**Structure**
- Average sentence length in the 10–20 word range.
- Include ordinal/transition markers (first, second, third, finally, additionally, moreover, furthermore).
- Include numbered items or explicit step references.
- Break paragraphs — a single undifferentiated block scores nothing structurally and reads worse.

**Specificity**
- Carry figures with units and context (counts of users, customers, pages, companies), currency amounts, and a year reference for timeliness.
- Name sources inline; the scorer matches "according to / per / from / by" followed by a capitalised name, a parenthetical citation, and a short list of well-known research houses and vendors.

**Uniqueness**
- Signal original work — "our research / our study / we found / we measured / we surveyed".
- Include a case study or worked example.
- Name the specific tools or products used, which is what a practitioner does and a summariser does not.

Read as a whole, these are a restatement of one idea: **write the passage so it survives being cut out of the page.** This skill's own answer-block pattern and AI-friendly page skeleton in `ai-retrieval-and-citation-2.md` are the canonical drafting instruction; the list above is the finer-grained sentence-level version of the same thing, and adds nothing about *ranking*.

## Drafting a liftable passage

On YMYL comparison copy, sourcing every figure is first a correctness rule and only second a GEO tactic. Statistics and quotations as citation levers already sit in the evidence ledger as ACADEMIC (#69, #70: benchmark lineage, effect sizes do not transfer) — see skill `seo-authority` › authority-trust-and-distribution.

**Evidence hunt — verify before the passage exists** `[practitioner]`
- Each statistic must trace back to a URL you fetched and read yourself; write its source, date, time window and denominator beside it.
- Each quotation must come from a named person in a named, citable publication, and each named expert must be a real person at a real organisation.
- Prefer sources in this order: primary data (regulator, statistics office, the law itself), then peer-reviewed work, then a named research firm's report, then trade press. In Portugal that means ERSE, ANACOM, Banco de Portugal, ASF, INE and the Diário da República ahead of any secondary source.
- First-party data is the strongest asset: before searching outside, check whether the site's own records already answer the claim — comparison logs, price histories, user counts.

**When the figure you want does not exist**, work down this list: (1) anchor to a related figure that does exist and state honestly how the two relate; (2) run the analysis on first-party data; (3) drop the claim. **Never** leave a vague directional placeholder ("studies show", "cada vez mais", "many companies") in its place — that is next door to fabrication and fails the claim-safety gate.

**Vetoes — these stop publication outright; they are not score deductions** `[practitioner]`
1. A statistic, quotation, citation or expert that is fabricated or cannot be verified.
2. An internal contradiction: the same fact given as two different figures, whether on one page or across the site.
3. A title that promises what the page does not deliver.
4. YMYL content with no identifiable author or reviewer.
5. The target engine's crawler blocked at robots.txt or at the edge (the edge gate in [ai-crawlers-and-bot-policy-2.md](ai-crawlers-and-bot-policy-2.md#the-edge-gate-in-practice)).
6. A YMYL claim missing its legal disclaimer or scope note.

**Effort-wasting anti-patterns** `[practitioner]`: generic AI-sounding introductions; unsupported superlatives (also a claims-policy problem); several H2s circling one sub-topic; filler paragraphs; repeating the keyword (ACADEMIC: it scored negative in the GEO benchmark).

**Measure the passage, not just the page** `[practitioner]`: for each page, record where our passage appears inside the AI answer — first sentence, first paragraph, body, or sources list only — next to cited Y/N. Being quoted as the lead source and being listed in a footer are different outcomes. Treat organic clicks to that page as the control series. The field definitions are in [ai-citation-measurement.md](ai-citation-measurement.md#measurement-fields--framing-and-position-of-every-mention).

## llms.txt — format validation rules

The format contract is the llms.txt specification v2 (modified 2026-08-10): "An H1 with the name of the project or site. This is the only required section" `[documented: https://llmstxt.org/, 2026-10-11]`. The other sections are optional, so their *absence* is never a failure. Sections that *are* supplied still follow the spec: they come «in the specific order» (BOM, H1, blockquote, detail sections without headings, then H2 file lists), and each file-list item contains «a required markdown hyperlink», then optional notes after a colon `[documented: https://llmstxt.org/, 2026-10-11]`. So fail a file on a missing H1, on supplied sections out of order, or on a file-list item without a Markdown link; the counts and extras below are suggestions. (Replaces the geo-seo-claude validator, which failed files with no description, no section or no link. Spec text and table adapted from AnswerDotAI/llms-txt, see `## Attribution`.)

| Check | Requirement | Status |
|---|---|---|
| Title | First non-BOM line is `# <site or project name>` | REQUIRED |
| Summary | A `> blockquote` with the key facts | optional (suggest) |
| Detail | Paragraphs or lists before the first `##` | optional |
| File lists | `## <section>` then `- [name](url)` with optional `: notes` | optional (suggest); if present, every item needs the link |
| `## Optional` | Skippable secondary links; no mechanical meaning since v2 | optional |
| Location | `/llms.txt` or any subpath (most specific wins); never `/.well-known/` | location rule |

Non-blocking suggestions worth keeping from the old tool: roughly 10–20 key page links rather than fewer than five, and at least two sections so content types are separated. It also probes for a companion `llms-full.txt` and records only whether it exists. A non-200 response is recorded as an issue with the status code — **note that it does not distinguish a 404 from a 403, which matters (see Caveats).**

**Carry these rules with this skill's existing evidence position, unchanged.** skill `seo-authority` › authority-trust-and-distribution holds it: entry #68 (llms.txt + schema) `[measured: MAINSTREAM, n=4 samples, c=0 controlled]` and entry #71 (llms.txt alone) `[measured: MAINSTREAM, n=3 samples, c=0 controlled]` — the latter with **no median, values running −19.7% to +81% and crossing zero** — both marked mechanism-unconfirmed, against Google's documented statement that Search does not use llms.txt and that it will neither harm nor help visibility `[documented: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide, 2026-10-11]`. The operating conclusion there stands: **ship it as a no-claim static file if the client wants one, or skip it.** The validator above tells you whether the file is well-formed. It tells you nothing about whether the file does anything. Do not let a green `format_valid` become an implied performance claim.

## Brand-presence checklist

The brand scanner's real contribution is its per-platform question list — a manual checklist for the surfaces AI answer engines draw from `[practitioner]`. Use it as a checklist a human or a browsing agent works through; do not use its automated verdicts (see Caveats).

- **Wikipedia / Wikidata** — Is there an article? Does a Wikidata entry exist with complete structured data? Is the brand cited as a source inside other articles? Are `sameAs` links in the site's schema pointing at both? Notability is the gate, and PR coverage alone does not clear it.
- **YouTube** — Is there an official channel? Is there content *from* the brand (tutorials, demos, explainers)? Is there content *about* the brand from others? What are the view counts on brand-related videos, and is the sentiment positive?
- **Reddit** — Does the brand have its own subreddit? Is it discussed in relevant industry subreddits? What is the sentiment? Does it appear in recommendation threads? Is there an official account? **Are the mentions recent (within six months)?**
- **LinkedIn** — Company page, follower count, posting recency, employee thought leadership, articles about the brand, engagement on posts.
- **Industry directories and review platforms** — presence, completeness, and recency of the listing.

skill `seo-authority` › authority-trust-and-distribution owns the evidence marks for the distribution tactics themselves (Reddit, YouTube, UGC) and should be consulted before any of these becomes a recommendation with an expected effect attached. The checklist establishes *presence*; it does not establish *causation*.

## The honest part of the source tool

Worth quoting because it is the section most GEO tools omit `[practitioner]`:

- **Deterministic vs LLM-judged.** Only two of its components — the citability scorer and the llms.txt validator — are deterministic and reproducible. The Brand Authority, Content E-E-A-T, Technical, Schema and Platform scores "are produced by LLM subagents following documented rubrics; they are guided evaluations rather than reproducible computations", and two runs on the same URL may differ. **Five of its six scored categories are a language model's opinion.**
- **Weights are opinionated.** Its category weight distribution "reflects the judgement of the tool's authors… These weights are not derived from a controlled study" `[unvalidated house heuristic]`.
- **Diagnostic, not a guarantee.** A high score "improves the structural conditions for AI citation but does not guarantee that any particular AI system will cite or recommend the site".
- **Schema validation is structural, not semantic** — it checks syntax, recognised types and required fields, not whether the values are true. A schema block that validates may still describe the wrong entity.
- **llms.txt is an emerging standard** whose presence "does not guarantee any specific crawler behaviour at this time".

If you build a scoring instrument for this skill, ship this section with it. The caveats below are what happens when a tool's marketing surface omits it.

## Sources

- geo-seo-claude@scripts/citability_scorer.py:43-214 — the eleven passage signals (point values not carried).
- geo-seo-claude@scripts/brand_scanner.py:35-234 — the per-platform brand-presence question list.
- geo-seo-claude@docs/scoring-methodology.md:261-271 — the tool's own limitations section, quoted.

