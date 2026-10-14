---
name: seo-authority
description: >-
  Builds and audits authority and off-site trust: what the evidence says about links, the link-spam line, linkable assets and digital PR, E-E-A-T and YMYL trust, entity and brand signals, Reddit/YouTube/forum distribution, disavow, site-reputation abuse. Use for "backlinks", "digital PR", "toxic links", "E-E-A-T", "brand mentions". Refuses link schemes, PBNs, link swaps and astroturfing. Not for per-engine penalty rules (seo-engine-policies).
---

# seo-authority

Earned links, trust and brand signals — what the record supports, where the spam line is, and what we refuse.

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
| AU1 | links, the link-spam line, linkable assets, digital PR | [authority-links-and-pr.md](references/authority-links-and-pr.md) |
| AU2 | E-E-A-T, entity, brand, community distribution, site reputation | [authority-trust-and-distribution.md](references/authority-trust-and-distribution.md) |

## Not mine

| Question | Skill |
|---|---|
| a manual action, reconsideration, an engine's link policy text | `seo-engine-policies` |
| study figures for a link tactic | `seo-evidence` |
| AI-citation tactics and measurement | `seo-ai-search` |
| roadmap and creative ideas | `seo-strategy` |

## Rules

1. Refused: link buying, PBNs and domain pools, link swaps and service-for-link exchanges, portfolio cross-linking beyond what a reader expects, undisclosed or astroturfed community posting.
2. Editorial outreach is "alive by count" in the published record, with zero controlled tests — never promise a lift.
3. Disavow only when both hold: a considerable number of spammy, artificial or low-quality links point to the site, and they have caused, or likely will cause, a manual action for unnatural links; try removal first; misuse can harm `[documented: https://support.google.com/webmasters/answer/2648487, 2026-10-11]`. Never on a third-party "toxic score" alone `[unvalidated house heuristic]`.
4. Third-party sections that ride the host's signals are a owner-level decision; the refusal stands on correctness and reputation.
5. Mechanism stories about authority are `[hypothesis]`.
