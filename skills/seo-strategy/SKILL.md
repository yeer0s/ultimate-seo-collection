---
name: seo-strategy
description: >-
  Builds SEO strategy and new angles: playbooks by site stage and type (new domain, comparison site, local, publisher, SaaS, YMYL, multi-locale), a register of out-of-the-box ideas each with mechanism, evidence label, per-engine policy check and test recipe, and a catalogue of official docs, tools and datasets. Use for "SEO roadmap", "where do we start", "creative SEO ideas", "best SEO tools". Not for auditing a page (seo-optimizer).
---

# seo-strategy

Where to start, in what order, which engines matter per market, and which new ideas are worth a test.

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
| ST1 | roadmap, strategy, "where do we start", which engines per market | [strategy-playbooks.md](references/strategy-playbooks.md) |
| ST2 | out-of-the-box ideas | [ideas-register.md](references/ideas-register.md) |
| ST3 | tools, docs, datasets | by H2: [part 1](references/resources-catalogue.md) (official engine documents) or [part 2](references/resources-catalogue-2.md) (tools by job, datasets, communities) |
| ST5 | which tactic for which job | [tactics-by-job.md](references/tactics-by-job.md) |

## Not mine

| Question | Skill |
|---|---|
| auditing a page or route | `seo-optimizer` |
| what an engine forbids | `seo-engine-policies` |
| does a tactic work | `seo-evidence` |
| implementing a step | the owning skill named in the playbook step |

## Rules

1. Every playbook step carries an evidence label and passes the policy gate before it is planned.
2. An idea row is a hypothesis with a test recipe and a kill condition, never a promise.
3. Banned tactics appear only under "Tempting, and banned", with the policy cite and its condition; a refusal stricter than the policy is marked as a house rule.
4. No traffic forecast from published numbers; only from the client's own demand data.
5. Market share and engine reach are stated only with a dated source.
