---
name: seo-ai-search
description: >-
  Makes content retrievable and citable by ChatGPT search, Perplexity, AI Overviews, AI Mode, Gemini, Copilot and Claude: query fan-out, the CDN/WAF edge gate per bot, training vs retrieval crawlers, agent readiness, citable passages, llms.txt position, and measuring AI citations. Use for "GEO", "AEO", "structure this so AI engines cite it", "AI visibility", "are AI bots blocked", "llms.txt". Not for AI companies' policy text (seo-engine-policies).
---

# seo-ai-search

Be fetched by each AI engine's retrieval bot, own a liftable passage, and measure citations honestly.

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
| AI1 | how AI engines pick and cite sources, GEO/AEO | by H2: [part 1](references/ai-retrieval-and-citation.md) (retrieval, source choice, citation deltas, myth list, differentiation) or [part 2](references/ai-retrieval-and-citation-2.md) (answer block, structure, entities, conversion, tracking) |
| AI2 | AI crawler access, blocking, Google's and Bing's AI controls | by H2: [part 1](references/ai-crawlers-and-bot-policy.md) (proof rule, bot list, fetchers, Google's AI controls) or [part 2](references/ai-crawlers-and-bot-policy-2.md) (Bing and other non-Google controls, the edge gate) |
| AI3 | an unfamiliar bot token, a block list to vet (ai.robots.txt), edge-gate tests; vendor bots named in the question use AI2 + their engine pages | [ai-crawler-registry.md](references/ai-crawler-registry.md) |
| AI4 | llms.txt, citability audit | [geo-audit-and-citability.md](references/geo-audit-and-citability.md) (its tool caveats: [part 2](references/geo-audit-and-citability-2.md)) |
| AI5 | measuring AI citations | [ai-citation-measurement.md](references/ai-citation-measurement.md) |
| AI6 | agent readiness, agentic browsing | [agent-readiness.md](references/agent-readiness.md) |
| AI7 | data pages, charts | [data-assets-and-charts.md](references/data-assets-and-charts.md) |

## Not mine

| Question | Skill |
|---|---|
| an AI company's crawler policy or opt-out text | `seo-engine-policies` |
| does llms.txt or a GEO tactic work (ledger) | `seo-evidence` |
| robots.txt syntax, rendering, schema | `seo-technical` |
| UX and conversion of the page | `site-improvement` |

## Rules

1. **Edge gate first:** a bot-access claim needs a request sent as that bot; `robots.txt` shows only what is declared.
2. Training and retrieval bots are separate decisions: blocking GPTBot does not remove a site from ChatGPT search answers (blocking OAI-SearchBot does, though the site "can still appear as navigational links"); blocking Google-Extended does not remove it from AI Overviews (Googlebot does).
3. Never import a block list wholesale; test against it.
4. llms.txt is a no-claim file at most; no ranking or citation promise.
5. AI-citation counts are sampled and volatile: repeat runs, log framing and position, never forecast.
6. When the user names specific vendors' bots to allow or block, also open skill `seo-engine-policies` EP2: the engine-matrix and each named vendor's page, so every training vs retrieval claim cites the vendor's own dated document. A block list or registry question is AI3 + AI2 only.
