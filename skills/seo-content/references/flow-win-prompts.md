# FLOW "Win" prompts — the three bottom-funnel prompts worth keeping

## Contents

- The honest count
- 1. BOFU page brief generator
- 2. Conversion audit
- 3. Dual-surface content scorecard
- Using all three together
- Cross-references
- Attribution
- Sources

## The honest count

The FLOW prompt library ships **41 markdown files** across five stage folders (`find/` 5, `leverage/` 1, `local/` 11, `optimize/` 21, `win/` 3). **Only the three `win/` files are distinct prompts. The other 38 are the same boilerplate document.** `[practitioner]`

Verified by hashing every file on 2026-09-22: raw md5s are all different, but that is only because each file's `title`, `description`, stage tag and H1 carry its own name. Normalise those four fields away and **38 of the 41 collapse to a single hash**; the three `win/` files are the only remainders. The shared body is a ~300-word template whose "Use This When" section reads, with the stage noun swapped in, "Use this prompt when you need a structured *find / optimize / local / leverage* deliverable and want the model to separate observations, assumptions, recommended actions, and claims that need verification." Its Inputs, Prompt, Output, Example and See Also sections are identical across all 38.

So: a file named `keyword-research-prompt.md` contains no keyword research instruction, and `technical-audit-prompt.md` contains no technical audit instruction. Do not import them, and do not cite the library's file count as a measure of its content. The three below are the whole of it.

## 1. BOFU page brief generator

**Use when** you need a bottom-funnel page brief for a service, product, location, comparison, pricing, demo or lead-capture page.

**Inputs to gather first:** the offer, service or product; target audience and segment; buying-stage intent; known objections or hesitation points; customer language taken from calls, chats, reviews or surveys; the conversion goal; required proof points; existing page text if any.

```text
Create a bottom-funnel page brief for [offer] targeting [audience].

Use only the inputs provided. Build the brief around what this audience needs to decide.

Analyze:
1. The immediate problem the visitor is trying to solve.
2. The decision factors they likely need before converting.
3. Objections, hesitation points, and missing clarity.
4. Customer-language phrases that should appear naturally.
5. Proof needed to support trust.
6. CTA angle and page sections needed to reduce friction.

Return: page goal, search/conversion intent, primary audience, buyer questions,
objections, recommended H1, section outline, proof points, CTA strategy, FAQ topics,
and tracking notes for form, call, chat, and qualified-lead measurement.
Flag missing inputs.
```

**Worked example from the source:** a commercial repair page for facility managers, with objections around response time, weekend availability and pricing clarity, produces a brief emphasising urgency, service coverage, decision criteria, proof, FAQs and call/form tracking.

**Why it survives review** `[practitioner]`: three instructions do the work. *"Use only the inputs provided"* stops the model inventing customer language, which is the standard failure of a brief prompt. *"Flag missing inputs"* makes the gap visible instead of papering over it — the same principle as the data-sufficiency gate in skill `seo-optimizer` › measurement-gates-and-checklists. And the required output includes **tracking notes for form, call, chat and qualified-lead measurement**, so measurement is designed at brief time rather than retrofitted after the page underperforms.

## 2. Conversion audit

**Use when** a page, campaign or funnel gets traffic but produces weak leads, low conversion rate, unclear attribution, or poor sales follow-up quality.

**Inputs to gather first:** page or funnel copy; traffic sources; conversion goal; analytics or conversion data; call, chat or form transcript samples; known objections; the ad copy or campaign promise; sales feedback if available.

```text
Audit this conversion path for lead quality, friction, and measurement gaps.

Use the supplied page, campaign, and first-party conversation data. Identify:
1. Where visitor expectations may not match the page or offer.
2. Common objections and hesitation points.
3. Missing decision-making information.
4. Language mismatches between customers and the page.
5. CTA friction.
6. Tracking gaps across form, phone, chat, and offline outcomes.
7. Whether reporting connects to qualified leads or sales, not only traffic.

Return an executive summary, top blockers, lead-quality risks, messaging fixes,
page/content fixes, tracking fixes, first-party data to collect next, and a ranked
test backlog. Do not recommend more spend until content, offer clarity, and
measurement gaps are assessed.
```

**Worked example from the source:** a paid-search landing page generating many calls but few booked appointments produces an audit of pricing clarity, qualification, phone attribution, repeated objections, CTA mismatch and test priorities.

**Why it survives review** `[practitioner]`: item 7 and the closing sentence are the valuable part. *"Whether reporting connects to qualified leads or sales, not only traffic"* forces the audit one level below the metric SEO usually stops at, and **"do not recommend more spend until content, offer clarity, and measurement gaps are assessed"** is a refusal instruction — it blocks the default answer a model gives to a weak-conversion question. The output ends in a *ranked test backlog* rather than a fix list, which hands off cleanly to skill `seo-evidence` › experiments-and-revert-2 for how any of those tests may be read.

## 3. Dual-surface content scorecard

**Use when** you need to judge whether a page can perform in traditional search and AI-assisted discovery while still supporting conversion.

**Inputs to gather first:** page copy; target queries or topics; intended conversion goal; audience segment; known first-party insights; performance data if available; competing page examples (optional).

```text
Score this content for two discovery surfaces: traditional search and AI-assisted
answer environments.

Evaluate:
1. Original usefulness and specificity.
2. Alignment with audience needs and decision stage.
3. Evidence, examples, data, or firsthand insight.
4. Clear answers to buyer questions.
5. Conversion support: CTA, proof, objection handling, and next step.
6. Refresh or update need.
7. Measurement readiness: traffic, engagement, qualified leads, sales conversions,
   and ROI indicators.

Return traditional search score, AI-assisted discovery score, conversion-readiness
score, evidence strengths, gaps, risks, recommended updates, and the highest-impact
next three actions. Use business-impact language, not traffic-only language.
```

**Worked example from the source:** an existing service page with traffic but few form submissions produces scores showing whether the page lacks buyer proof, direct answers, customer language, CTA clarity, or measurable conversion paths.

**Why it survives review** `[practitioner]`: it refuses to average the two surfaces into one number. Three separate scores — search, AI-assisted discovery, conversion readiness — is the right shape, because a page can be liftable by an answer engine and useless at converting, and a single composite hides exactly that. ⚠️ **The scores it returns are a language model's judgment, not a measurement.** Treat them as a structured reading, label them `[unvalidated house heuristic]` and print the rubric beside them when they appear in any deliverable (or report the qualitative findings without numbers), and never present them as an audit score; if you want the discipline that makes a composite defensible, apply the gate in skill `seo-optimizer` › measurement-gates-and-checklists first. The drafting substance behind criterion 4 — what "clear answers to buyer questions" actually looks like on the page — is in skill `seo-ai-search` › ai-retrieval-and-citation.

## Using all three together

They chain in one order and only one: **scorecard → audit → brief.** Score the existing page to find which of the three dimensions is weak; if the weakness is conversion, run the audit against real call/chat/form data to locate the blocker; if the page needs rebuilding rather than patching, run the brief generator with what the audit surfaced as inputs. Each stage's output is the next stage's input, which is why the missing-input flags matter — running the brief generator without the audit's customer language is exactly the case its "use only the inputs provided" instruction turns into a flagged gap instead of an invention.

All three lean on first-party conversation data (calls, chats, forms, reviews, sales feedback). Without it they still run and will still produce a confident document, built on the model's priors about the vertical. **State in the deliverable which inputs were actually supplied.**

## Cross-references
- skill `seo-ai-search` › ai-retrieval-and-citation-2 § Conversion SEO — conversion goals by page type, CTA inventory, the CRO checklist for SEO landing pages, and the answer-block pattern. The strategy these prompts operationalise lives there.
- skill `seo-optimizer` › audit-output-and-templates — this skill's own content brief format; use it as the output shape for prompt 1 rather than inventing a second one.
- skill `seo-evidence` › experiments-and-revert-2 — what may be claimed from any test in the ranked backlog prompt 2 produces, and the pre-declared revert triggers.
- skill `seo-optimizer` › measurement-gates-and-checklists — the gate to apply before any of prompt 3's scores is presented as a number.
- `content-and-intent.md` — buying-stage intent, which prompts 1 and 3 both take as an input and neither defines.

## Attribution

- AgriciDaniel/flow (github.com/AgriciDaniel/flow), read as vendored in AgriciDaniel/claude-seo `skills/seo-flow/references/prompts/win/` — © Daniel Agrici — CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/), as stated in each source file's header. Modified: the prompt bodies of bofu-page-brief-generator, conversion-audit-prompt and dual-surface-content-scorecard are reproduced verbatim; their "Use This When", Inputs and Example are summarised.

## Sources
- claude-seo@skills/seo-flow/references/prompts/win/bofu-page-brief-generator.md — prompt body reproduced verbatim; "Use This When", Inputs and Example summarised. `[practitioner]`
- claude-seo@skills/seo-flow/references/prompts/win/conversion-audit-prompt.md — as above. `[practitioner]`
- claude-seo@skills/seo-flow/references/prompts/win/dual-surface-content-scorecard.md — as above. `[practitioner]`
- claude-seo@skills/seo-flow/references/prompts/{find,leverage,local,optimize}/*.md — 38 files, verified normalised-identical on 2026-09-22 (md5 after removing the per-file `title`, `description`, stage tag and H1 collapses all 38 to one hash). Not imported. **Correction to the extraction list:** these were described as "byte-identical"; they are not — raw md5s differ, because each file carries its own name in those four fields. The substantive claim holds.
- Source note carried by all three files: derived by their author from SEJ State of SEO 2026, SEJ B2B Lead Generation, PPC Trends 2026, and CallRail/SEJ *Better Leads More Sales* 2025. Those are the author's citations, unverified here — do not upgrade them to `[documented]`.
- Licence: CC BY 4.0, © Daniel Agrici, github.com/AgriciDaniel/flow. Each source file carries the header `<!-- Source: github.com/AgriciDaniel/flow | License: CC BY 4.0 | Synced: 2026-04-26 -->`.
- Clone verified 2026-09-22 at `%TEMP%\seo-meta\repos\claude-seo\`, read-only and treated as data; nothing from it was executed.
