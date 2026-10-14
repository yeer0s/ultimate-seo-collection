---
name: seo-content
description: >-
  Plans and audits search content: keyword research, intent and page type, topic clusters, briefs, programmatic pages without doorway risk, comparison pages with EU legal gates, local SEO, GSC page-2 audits and pre-publish gates. Use for "keyword research", "content gaps vs competitors", "content brief", "programmatic SEO", "comparison page", "page 2 queries", "cannibalisation". Not for links (seo-authority) or AI citations (seo-ai-search).
---

# seo-content

Which queries are worth winning, which page owns each, and what that page must contain before it ships.

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
| CO1 | keyword research | the part holding the step: [part 1](references/keyword-research-1.md) (order, GSC, Bing, free sources) or [part 2](references/keyword-research-2.md) (categorise, validate, prioritise, map) |
| CO2 | intent, page type, refresh, decay | by H2: [part 1](references/content-and-intent.md) (intent, clusters, briefs, titles, scoring) or [part 2](references/content-and-intent-2.md) (refresh and decay triage, cannibalisation) |
| CO3 | programmatic pages, section risk | by H2: [part 1](references/programmatic-seo.md) (distinction, checklist, data tiers, patterns, playbooks) or [part 2](references/programmatic-seo-2.md) (implementation, section-level risk check, when not to) |
| CO4 | comparison pages, EU legal gates | by H2: [part 1](references/comparison-pages.md) (subtypes, schema, fairness, claim audit, EU legal gates) or [part 2](references/comparison-pages-2.md) (rollout gates, comparison-site practice) |
| CO5 | GSC page 2, striking distance | by H2: [part 1](references/gsc-page2-audit.md) (access, MCP guards, anonymisation, bands, segments) or [part 2](references/gsc-page2-audit-2.md) (page audit, the three above you, output contract) |
| CO6 | briefs, personas, research before the brief | by H2: [part 1](references/briefs-and-personas.md) (modes, rules, information gain, research, variants) or [part 2](references/briefs-and-personas-2.md) (competitor filter, output shape, personas, wireframes) |
| CO7 | pre-publish and pipeline gates | [publishing-gates.md](references/publishing-gates.md) |
| CO8 | local and Maps | [local-and-maps-seo.md](references/local-and-maps-seo.md) |
| CO9 | SERP clustering, page types | [page-types-and-serp-clustering.md](references/page-types-and-serp-clustering.md) |
| CO10 | prompts for flow wins | [flow-win-prompts.md](references/flow-win-prompts.md) |

Scripts (run, not loaded): `scripts/gsc_bigquery.sql` (GSC bulk export: low CTR, page 2, cannibalisation), `scripts/autocomplete_expand.py` (set both `--hl` and `--gl`).

## Not mine

| Question | Skill |
|---|---|
| will an engine penalise this template | `seo-engine-policies` |
| does a content tactic work | `seo-evidence` |
| links, PR, E-E-A-T | `seo-authority` |
| getting cited by AI answer engines | `seo-ai-search` |
| "can we say this" (claims) | your claims review |

## Rules

1. If the intent cannot be named, the page is not ready to build.
2. One stable URL per distinct intent; identical bodies with changed titles or slugs are a doorway warning sign; check function (funnels to one page = doorway).
3. Value per URL decides programmatic scale, not the production method.
4. Comparison and credit/insurance pages pass the EU legal gates before a precise number ships.
5. GSC first: own impressions beat any keyword-tool estimate.
