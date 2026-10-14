---
name: seo-evidence
description: >-
  Grades whether an SEO, AEO or GEO tactic works, using the 182-entry Meta Study ledger and four practitioner layers from anonymised sources with consensus counts, and designs experiments with holdouts, revert triggers and title or snippet tests. Use for "does X work", "is this a myth", "the study says", "did our change work", "should we roll back". Never turns a published gain into a forecast. Not for engine rules (seo-engine-policies).
---

# seo-evidence

Whether a tactic works, how sure we are, and how to test it on this site before anyone calls it a win.

<!-- grammar-excerpt -->
Label every tactic with one of the 9 marks: `[documented: <URL>, <date>]` · `[documented-secondary: …]` · `[unverified: …]` · `[measured: MARK, n=S, c=C]` · `[practitioner: anonymised sources · …]` · `[hypothesis]` · `[vendor]` · `[memory]` · `[unvalidated house heuristic]`.
Numbers keep their denominator; marks are counts, not verdicts; bundles support direction, not size.
Never forecast a published number onto a client site; only the client's own GSC demand and funnel forecast.
No rollout without a pre-declared revert rule (applicability, holdout, what stays fixed, metric + window, trigger).
Repetition never proves; full grammar: skill `seo-optimizer` § Evidence marks.
<!-- /grammar-excerpt -->

## Load rule

Open one reference per load-when row the question touches (a "by H2" row: only the part holding that H2); never a file "to be thorough". A pointer into another seo- skill's file is a citation: quote it, or first load that skill's SKILL.md and open the file through its own load-when row. Engine pages, ledger and practitioner parts and the crawler registry are lookup-only.

## Load when

| ID | Question shape | Open |
|---|---|---|
| EV1 | "does X work", "is it a myth", "is it proven", folklore | by H2: [part 1](references/works-vs-doesnt.md) (the joined table, one row per claim) or [part 2](references/works-vs-doesnt-2.md) (field errors repeated in popular SEO skills) |
| EV2 | a named ledger entry or study figure, or a `Next:` pointer from EV1 | the part holding the entry: [part 1](references/evidence-and-tactics-1.md) (how to read marks, recipe, shortlist), [part 2](references/evidence-and-tactics-2.md) (catalogue #1–#182), [part 3](references/evidence-and-tactics-3.md) (AVOID, IT DEPENDS, untested) |
| EV3 | practitioners or forum consensus named in the question | [practitioner-index.md](references/practitioner-index.md), then one of: [technical-1](references/practitioner-technical-1.md), [technical-2](references/practitioner-technical-2.md), [agentic](references/practitioner-agentic.md), [professional](references/practitioner-professional.md), [general](references/practitioner-general.md), [digest-1](references/practitioner-secondary-digest-1.md), [digest-2](references/practitioner-secondary-digest-2.md) |
| EV4 | test design, holdouts, revert, "did our change work" | the part holding the H2: [part 1](references/experiments-and-revert-1.md) (why, recipe), [part 2](references/experiments-and-revert-2.md) (designs, measurement, revert triggers) |
| EV5 | titles, snippets, SERP-feature tests | [titles-and-serp-tests.md](references/titles-and-serp-tests.md) (title ledger #154–#173, guardrails) |
| EV6 | metadata at scale, templated titles, swap test (a single title A/B test is EV5 + EV4) | [metadata-at-scale.md](references/metadata-at-scale.md) |

## Not mine

| Question | Skill |
|---|---|
| what an engine forbids, manual actions, appeals | `seo-engine-policies` |
| implementing schema, canonicals, sitemaps | `seo-technical` |
| measuring AI citations | `seo-ai-search` |
| writing the brief or page | `seo-content` |

## Rules

1. Quote a ledger entry as mark + n + c + metric + design, never as a bare percentage.
2. MAINSTREAM means "published ≥3 times", never "proven". A range crossing zero is "direction unresolved".
3. `[practitioner]` claims carry their counts (threads, score, newest month) and stay `[practitioner]` until a measurement with n and c exists or an engine page says it. Consensus = ≥2 threads, ≥2 authors, ≥10 summed score; `contested` always prints its counter-argument.
4. A claim repeated across many GitHub skills or blogs is still one claim; star counts are not evidence.
5. Two verdicts per URL — position and CTR — never one label ORing them. "Not significant" is not "no effect".
6. Every test declares its revert trigger before launch; a human confirms the mechanism before reverting.
7. Echo clustering: many sources repeating one upstream origin count as one source, not corroboration; group by origin before counting (skill `seo-content` › briefs-and-personas).
