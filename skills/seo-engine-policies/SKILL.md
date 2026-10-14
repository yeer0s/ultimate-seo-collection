---
name: seo-engine-policies
description: >-
  States what each search and AI answer engine prohibits, how it enforces, notifies and allows recovery, and which crawler and AI opt-out controls it honours: Google, Bing/Copilot, DuckDuckGo, Ecosia, Yahoo, Qwant, Yandex, Baidu, Naver, Seznam, Brave, OpenAI, Perplexity, Anthropic, Apple. Each rule is cited and dated. Use for "manual action", "is this allowed on Bing", "how do we appeal". Not for whether a tactic works (seo-evidence).
---

# seo-engine-policies

What each engine forbids, how it enforces and allows recovery, and which crawler and AI controls it honours, from its dated documents.

<!-- grammar-excerpt -->
Label every tactic with one of the 9 marks: `[documented: <URL>, <date>]` · `[documented-secondary: …]` · `[unverified: …]` · `[measured: MARK, n=S, c=C]` · `[practitioner: anonymised sources · …]` · `[hypothesis]` · `[vendor]` · `[memory]` · `[unvalidated house heuristic]`.
Numbers keep their denominator; marks are counts, not verdicts; bundles support direction, not size.
Never forecast a published number onto a client site; only the client's own GSC demand and funnel forecast.
No rollout without a pre-declared revert rule (applicability, holdout, what stays fixed, metric + window, trigger).
Repetition never proves; full grammar: skill `seo-optimizer` § Evidence marks.
<!-- /grammar-excerpt -->

## Load rule

Open one reference per load-when row the question touches (a "by H2" row: only the part holding that H2); never a file "to be thorough". A pointer into another seo- skill's file is a citation: quote it, or load that skill's SKILL.md and open the file through its load-when row. Engine pages, ledger and practitioner parts and the crawler registry are lookup-only.

## Load when

| ID | Question shape | Open |
|---|---|---|
| EP1 | one named engine, or that engine's own rules | one of: [google](references/google.md), [google-ai](references/google-ai.md), [bing](references/bing.md), [microsoft-copilot](references/microsoft-copilot.md), [bing-syndication](references/bing-syndication.md), [yandex](references/yandex.md), [baidu](references/baidu.md), [naver](references/naver.md), [seznam](references/seznam.md), [brave](references/brave.md), [openai](references/openai.md), [perplexity](references/perplexity.md), [anthropic](references/anthropic.md), [other-ai-crawlers](references/other-ai-crawlers.md); a dated or regional change ("the EEA change"): google §6, not EP3 |
| EP2 | the answer cites ≥2 engines, or "which engines" / "all engines" | [engine-matrix.md](references/engine-matrix.md), then EP1 per engine the answer quotes (≤3); "which engines matter in a market" is the matrix plus skill `seo-strategy` › strategy-playbooks, no engine page |
| EP3 | a dated Google update, "was it an update", timeline | by H2: [policy and documentation changes](references/google-updates-timeline.md) or [core/spam rollouts, data windows, unverified](references/google-updates-timeline-2.md) |
| EP4 | asked what a violation class means | [policy-taxonomy.md](references/policy-taxonomy.md) |
| EP5 | a spam play: run request, or seen in a rival, proposal, tool, offer | by H2: [1](references/spam-playbook.md), [2](references/spam-playbook-2.md), [3](references/spam-playbook-3.md), [4](references/spam-playbook-4.md), [5](references/spam-playbook-5.md), [6](references/spam-playbook-6.md), [7](references/spam-playbook-7.md), [8](references/spam-playbook-8.md), [9](references/spam-playbook-9.md) |

## Engine index

| Page | Covers | Market relevance |
|---|---|---|
| google | Search, Discover, News | global; baseline |
| google-ai | AI Overviews, AI Mode, Gemini, Google-Extended | global |
| bing | Bing Search | feeds Copilot, DDG, Yahoo, Ecosia (part) |
| microsoft-copilot | Copilot, Bing AI answers | global |
| bing-syndication | DuckDuckGo, Ecosia, Yahoo, Qwant | FR/DE (Qwant, Ecosia) |
| yandex | Yandex | RU, CIS, TR |
| baidu | Baidu | CN |
| naver | Naver | KR |
| seznam | Seznam | CZ |
| brave | Brave Search | global, small |
| openai | ChatGPT search, GPTBot | global AI |
| perplexity | Perplexity | global AI |
| anthropic | Claude | global AI |
| other-ai-crawlers | Apple, Common Crawl, Meta, ByteDance, Amazon | crawlers |

All 14 pages: `last_verified` 2026-10-11.

## How to read a page

13 sections: §1–§4 users, documents, crawlers, tools; §5 prohibited (classes 1–16); §6 enforcement; §7 recovery; §8 AI controls (17–18); §9 delta from Google; §10 practitioner; §11 unverified. A §5/§8 row: engine's term, ≤25-word quote, dated label; "not addressed" is an answer.

## Not mine

| Question | Skill |
|---|---|
| does a tactic work, studies, practitioners | `seo-evidence` |
| fixing robots.txt, canonicals, schema, migrations | `seo-technical` |
| getting cited by AI engines, edge-gate testing | `seo-ai-search` |
| link building, E-E-A-T, digital PR | `seo-authority` |

## Rules

1. One engine's policy never fills another engine's cell. "Bing probably also…" is `[hypothesis]`; "same as Google" needs a cite.
2. Say the page's `last_verified` date when quoting; re-fetch if older than 180 days `[unvalidated house heuristic]`.
3. An INCOMPLETE page says so, lists what is unverified, names the official channel and gives the safe default; it never invents rules.
4. Practitioner penalty reports stay in a page's §10, `[practitioner]`.
5. A forbidden tactic is not graded or built: policy gate before evidence before implementation. A spam play (EP5) is never run, tuned or priced: a run request gets a one-sentence refusal, then the play in entry order, mechanism only; rival, victim, audit: explain fully.
6. **Default engine set:** a rule every engine has (link spam, cloaking, doorways, scaled content) is answered for Google **and** Bing at least (EP2) when the question names one engine or none; say where others are silent. Site reputation abuse: google §6 only.
7. **Vanished from an engine:** technical causes first (skill `seo-technical` › crawl-and-index), then engine page §5–§7; a traffic drop starts at skill `seo-technical` › incident-triage.
8. **Route on:** link penalty: skill `seo-authority` › authority-links-and-pr; partner section on your domain: google §6, skill `seo-authority` › authority-trust-and-distribution, skill `seo-content` › programmatic-seo-2; lighter page for bots: skill `seo-technical` › rendering-and-sitemaps-2; mass city pages: skill `seo-evidence` › works-vs-doesnt, then skill `seo-content` › programmatic-seo.
