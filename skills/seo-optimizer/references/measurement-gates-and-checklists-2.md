<!-- split-header: part 2 of 2 of measurement-gates-and-checklists.md (step-3 original lines 118–182; boundary H2) -->
# Measurement gates (2 of 2) — metered-API budget presets, field allowlists, prompt-file tests
## Contents

- Metered-API budget presets
- Field-allowlist pattern for verbose APIs
- Tests that lint the prompt files themselves
- Cross-references
- Sources

Other parts of the same original file: [measurement-gates-and-checklists.md](measurement-gates-and-checklists.md).

<!-- /split-header -->
## Metered-API budget presets

A spend guard for any paid SEO data API (DataForSEO, Ahrefs, Semrush, SERP or backlink providers, an MCP server that wraps one): **price each call before it runs, hold it when it crosses a limit, and fail closed.** The guard is a gate in the sense of the data-sufficiency section: it lives in code next to the client, not only in this text.

**The guard, step by step** `[unvalidated house heuristic]`:

1. **Estimate before calling.** Look up the endpoint in a local price table (unit price × items in the request, e.g. keywords in a batch or rows requested) and write the estimate down before the request leaves.
2. **Check three limits:** the per-call hold threshold (above it, ask the user and wait), the per-run ceiling (the sum of estimates for the whole planned job), and the daily ceiling (today's logged spend + this estimate).
3. **Fail closed.** If the endpoint is missing from the price table, the table is older than 30 days, the spend ledger cannot be read or written, or no preset is selected, the call does not run — the run reports the blocker as an environment fact, never as a finding about the site.
4. **Log the real cost.** After each call, record the estimate, the provider-reported cost (when the response carries one) and the endpoint in the ledger. An actual cost above the estimate makes the next call of that endpoint hold until the price table is corrected.
5. **Say the preset in the report** next to the tier (see the tiered-capability section above), so the reader knows the sample was bounded by money as well as by credentials.

**House presets** — ship named presets instead of asking for a number. No preset is unlimited: a pipeline that needs more chooses the largest preset and raises it explicitly, in writing, for that run. Amounts are in the provider's billing currency `[unvalidated house heuristic]`:

| Preset | Per-call hold above | Per-run ceiling | Daily ceiling | For |
|---|---|---|---|---|
| Trial (default) | 0.10 | 1.00 | 2.00 | Learning, testing a new endpoint |
| Standard | 0.50 | 5.00 | 10.00 | One site audit |
| Bulk | 2.00 | 25.00 | 50.00 | Multi-site or agency batch work |

**One published instance.** The claude-seo DataForSEO extension ships named presets that gate on a per-call threshold as well as a daily ceiling `[vendor]`:

| Preset | Daily limit | Per-call approval threshold | Mode | For |
|---|---|---|---|---|
| Conservative | $2.00 | $0.10 | threshold | Learning, testing |
| Standard | $10.00 | $0.50 | threshold | Regular audits |
| Aggressive | $50.00 | $2.00 | threshold | Agency bulk work |
| Unlimited | $999.00 | — | none | Trusted pipelines |

The same reference prices endpoint families (roughly $0.001–$0.002 per SERP call, $0.05 per keyword-volume batch or business-listings call, $0.01–$0.02 for on-page and backlink sub-calls) and lists cost-reduction levers: prefer the lightweight SERP variant, batch keywords into one volume call, use the queued task type instead of live for non-urgent work, avoid operator-bearing image queries that carry a cost multiplier, and cache within a session `[vendor]`. The savings are the source's own figures; no independent measurement is published. Its "Unlimited" preset (no per-call threshold) is the one row this skill does not adopt, because a guard with no ceiling cannot fail closed.

## Field-allowlist pattern for verbose APIs

Point a tool-response filter at an allowlist of fields keyed by module, so only SEO-relevant keys survive into context — for SERP items: type, rank group, rank absolute, position, title, description, url, domain, breadcrumb, featured-snippet flags, rating, timestamp, and the SERP-feature blocks (local pack, AI overview, people-also-ask, related searches, knowledge graph), with nested allowlists for video and image items `[practitioner]`. The config's own header claims roughly a three-quarters reduction in token usage across 9 modules and 79 tools `[vendor, no measurement published — treat the reduction as directional]`.

Generalise it: **for any chatty API or MCP server, define the allowlist once, next to the client, and make it the default path.** Beyond tokens, the allowlist is a written record of which fields the analysis depends on, and a field that disappears upstream fails loudly instead of quietly widening the response.

## Tests that lint the prompt files themselves

A repo-level practice worth naming `[practitioner]`: **write tests whose subject is the instruction text, not the code.** The imported repo does this in at least two shapes `[practitioner]`:

- **Assert a superseded claim cannot come back.** A test reads the skill markdown and asserts the corrected claim is present — with whitespace normalised to a single space first, because prose gets re-wrapped whenever a nearby line changes, and asserting on the literally wrapped string breaks on every unrelated reflow while matching at sentence level over normalised whitespace survives it.
- **Assert the rule names its own enforcement.** The gate test asserts the skill text contains `MUST NOT`, the validator's filename, and the failure token `status: FAIL` — then separately exercises the validator to prove the forbidden combination really does fail.

Both are cheap and both target the failure this skill keeps hitting: a rule that is true in the document and absent from the run. Apply the same to this library — a claim that loses its label, a primary-source URL that vanishes, or a threshold that reappears after being retired is a test case, not a proofreading task.

## Cross-references
- skill `seo-evidence` › experiments-and-revert-2 — verdict states (`insufficient_data` / `inconclusive` / `helped` / `hurt` / `no_effect (TOST)`), the click-count thresholds behind them, and pre-declared revert triggers. This file does not restate any of them; when a gate here says "not enough data", that file says what you may then claim.
- skill `seo-technical` › cwv-field-lab-diagnosis — the Core Web Vitals thresholds the CWV skeleton above formats.
- `audit-output-and-templates.md` — the skill's own output templates (audit table, recommendation, reporting dashboard, Search Console opportunity report) and the prioritisation formula; use those first and treat the skeletons above as section orders to fold in.
- skill `seo-content` › gsc-page2-audit — the Search Console workflow the performance skeleton reports on.
- skill `seo-ai-search` › geo-audit-and-citability — a worked example of what happens when these gates are absent from an audit tool.

## Sources
- claude-seo@skills/seo-backlinks/SKILL.md:160, 170-179, 181-190, 192-236, 254-263, 265-292 — data-sufficiency gate, MUST-NOT-score rule, `Not Assessed` literal, validator gate, confidence-weighted cascade, pre-delivery checklist. Carried as `[practitioner]`; all weights and confidence multipliers carried as `[unvalidated house heuristic]`.
- claude-seo@skills/seo-audit/SKILL.md:55-100 — structured audit-data envelope. `[practitioner]`
- claude-seo@skills/seo-google/assets/templates/cwv-audit-report.md, gsc-performance-report.md, indexation-status-report.md — three report skeletons, taken as section orders and disclosure footers. `[practitioner]`
- claude-seo@skills/seo-maps/SKILL.md:47-66 and skills/seo-google/SKILL.md:47-56 — tiered capability detection with mandatory tier disclosure. `[practitioner]`
- claude-seo@skills/seo-dataforseo/references/cost-tiers.md:1-45 — endpoint pricing and budget presets. `[vendor]`
- Phase-2 research report research/REPORT.md §7 idea 15 — the spend-guard idea (price each paid call, hold it before it runs, fail closed); the guard steps, house presets and the 30-day price-table limit are our own `[unvalidated house heuristic]`.
- coreyhaines31/marketingskills@skills/seo-audit/SKILL.md:40-51 (phase-2 adapted file research/adapted/coreyhaines31__marketingskills/striking-distance-push-and-launch-checklist.md) — fetch caveat only: non-rendering fetches miss client-injected JSON-LD, so "no schema" needs a rendered check or `unverifiable_js`. INTEGRATE, MIT.
- claude-seo@extensions/dataforseo/field-config.json:1-40 — field-allowlist pattern; its token-reduction claim carried as `[vendor, no measurement published]`.
- claude-seo@tests/test_ai_crawler_claims.py:1-30 and tests/test_backlink_score_gate.py:1-40 — tests that lint the prompt files themselves. `[practitioner]`
- Clone verified 2026-09-22: every line range above was read in the read-only clone at `%TEMP%\seo-meta\repos\claude-seo\` before being written here. The clones were treated as data; nothing in them was executed.
