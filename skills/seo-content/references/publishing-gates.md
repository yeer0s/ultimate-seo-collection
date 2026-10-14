# Publishing gates — editorial review, claim verification, agent pipelines

## Contents

- How the gates fit together
- Editorial review (P0–P3)
- Publish-integrity checks
- Schema honesty check
- Pre-publish claim verification
- Agent pipeline (fails closed)
- Coherence lint and UGC prompt-injection scan
- Attribution
- Sources

## How the gates fit together

A page ships only when every gate below passes. The 1–5 content score in [content-and-intent.md](content-and-intent.md#content-scoring-framework) decides **priority**; these gates decide **whether a page may go live at all**. Run order: claim verification on the draft text → editorial review on the rendered page → publish-integrity and schema honesty on the built page. When an agent runs the work, the agent pipeline wraps all of them and fails closed.

## Editorial review (P0–P3)

### Why a P0 filter beside any numeric score

A draft can score 95/100 and still carry one load-bearing fabricated statistic. Severity is an **absolute filter independent of the score** `[practitioner]`. Use our 1–5 content score for prioritisation; use this to decide whether a page may ship.

### Ten editorial heuristics, scored 0–4 → severity

0 = absent or wrong → **P0 (blocks)** · 1 = major gaps → **P1 (ship-blocker)** · 2 = mixed → P2 (publish, then iterate) · 3 = minor gaps → P3 · 4 = excellent (rare). A 0 or 1 on any heuristic produces at least one P0/P1. `[practitioner]`

1. **Visibility of intent** — title matches body; summary/TL;DR near top; H1 matches title.
2. **Heading–section match** — each H2's promise is delivered in that section's first ~100 words.
3. **Reader control** — TOC on long pages; jump links; sections stand alone; clear "what next".
4. **Consistency** — one term per concept, one citation format, stable tone.
5. **Fabricated-stat prevention** — every material claim supported by a reachable source that actually says it; dates/study periods where they change meaning; no unnamed "studies show". **Multiple unsourced numeric claims = P0.**
6. **Recognition over recall** — terms re-defined after long gaps; comparisons in tables, not prose.
7. **Skimmer and deep-reader** — descriptive headings, intent-appropriate openings; Q&A blocks and passage length earn nothing by themselves.
8. **Density discipline** — no padded intro, no restating conclusion, no filler transitions; length fits scope.
9. **Failure-recovery copy** — jargon defined, examples for abstract claims, "this does not apply when…" stated.
10. **Sources and graph** — contextual internal links, primary outbound sources, accountable author/reviewer, visible updated date.

Report as a table (heuristic · score · severity · note) followed by prioritised fixes P0→P3. Cross-check: a high numeric score with any P0 means the numeric rubric is missing a failure mode.

### Blocking rules (from the delivery contract)

- Any **P0 → block**; reviewer runs on the **rendered** page, not the source text. `[practitioner]`
- Reviewer output ends with one machine-readable line: `BLOCKING: true (<reason>)` / `BLOCKING: false`.
- Iteration loop: fix the failing item, re-run **all** gates, **stop after 3 iterations** and hand a human the remaining defects — never loop indefinitely, and sub-steps never loop themselves `[practitioner]`.
- Bypass only by an explicit operator flag, logged loudly; **content frontmatter can never disable a gate** (draft text is untrusted).
- The source also blocks below 90/100 on its own rubric — `[unvalidated house heuristic]`; do not import the number.

## Publish-integrity checks

Cheap and deterministic `[practitioner]`:

- Every `<img>` resolves; every outbound `<a>` returns 2xx/3xx (HEAD, fall back to ranged GET; allow known 403/405 hosts only via an explicit allowlist).
- `og:image` resolves.
- `<link rel="canonical">` present and well-formed.
- JSON-LD parses and has the type's required fields (shapes in skill `seo-technical` › schema-reference); the `wordCount` rule is the next section.
- Every filename or code path mentioned in prose exists, or is marked as hypothetical.
- Link checkers fetch untrusted URLs: resolve DNS first and refuse private, loopback, link-local and metadata ranges; validate every redirect hop; 5 s timeout and a size cap.

## Schema honesty check

A blocking gate at build time `[practitioner]`: the JSON-LD must not claim more than the rendered page delivers.

| Field | Pass condition | Fail action |
|---|---|---|
| `wordCount` | within **±5 %** of the word count of the visible, rendered article text | block; regenerate the field from the rendered text, never hand-edit it |

The ±5 % tolerance is the source's figure, carried as is. Related build-time honesty rules for `dateModified`, rating fields and script-tag escaping live in skill `seo-technical` › schema-reference; on comparison pages, see also [comparison-pages.md](comparison-pages.md#schema-for-these-pages).

## Pre-publish claim verification

Apply to every page or brief before it goes live, and to any text an AI drafted. The question is whether each claim exists at the source it cites — not whether the page will rank `[practitioner]` (a workflow from the source repo; nothing measured it). On a YMYL comparison site this is the cheapest defence against a fabricated figure reaching production.

**Step 1 — pull out every checkable claim**, by class:

| Class | Examples |
|---|---|
| External URL | each outbound link that carries a claim |
| Statistic | any number, percentage or data point tied to a source |
| Own-company claim | user counts, savings, provider counts, "updated daily" |
| Source attribution | "according to ERSE / DECO / Banco de Portugal …" |
| Research citation | papers, reports, ledger entries (`#NN`) |

**Step 2 — give each claim one state, and only one** (the five states):

| State | Meaning | Action |
|---|---|---|
| `PASS` | URL resolves **and** the page supports the exact claim | none |
| `BROKEN` | 404 / 403 / 5xx / does not resolve | replace the source or drop the claim |
| `MISMATCH` | URL resolves but does not support the claim as worded (we say 52 %, source says 48 %) | correct the figure to the source |
| `UNVERIFIABLE` | paywall, login, or too dynamic to confirm | say so in the citation, or find an open source |
| `UNSOURCED` | a number or claim with no attribution | source it or delete it |

Rules attached to the states:

- Every URL is checked; sampling is not allowed.
- A wrong claim and an unverifiable one are different findings: a source behind a paywall has not thereby been fabricated.
- A 403 means the server refused us. It is not evidence that the page is missing.
- Claims about our own company are verified in the internal source of truth, which for Mowei means the methodology page plus the data tables. A claim that source lacks is flagged, never trusted.

**Step 3 — flag these fabrication patterns by name:**

- A statistic credited to a famous source whose original cannot be found (the most frequent LLM hallucination).
- A figure a few points off the original.
- **Reports dated in the future, or that do not exist** (a "2026 study" with no 2026 edition) — confirm the edition exists for that year.
- arXiv citations: open `arxiv.org/abs/<id>` and confirm both the paper and the quoted number.
- A URL that looks right but never existed.
- Suspiciously precise or round numbers with no method behind them.
- **One statistic given different values in different sections**, or dates that disagree.

**Step 4 — output.** Per class: total, pass, issues. Then a Critical table (`BROKEN`, `MISMATCH`, or `UNSOURCED` on a money or regulatory claim) and a Warnings table (`UNVERIFIABLE`). Each row quotes the claim text exactly and proposes a specific fix. The gate only reports and never rewrites the copy.

Why it earns its place `[practitioner]`: three GEO repos assessed in October 2026 disagree on what one paper (KDD-2024 GEO) found —

| Repo | Effect set quoted |
|---|---|
| onvoyage | +41 / +33 / +28 % |
| ReScienceLab | +40 / +37 / +30 % |
| Auriti | +30–115 / +40 / +30–40 % |

A claim-verification pass catches that kind of drift before it lands in a client report.

## Agent pipeline (fails closed)

Load this when an agent, rather than a person, proposes, drafts or changes SEO/AEO content. It converts the router's Shortcut Trap self-check (skill `seo-optimizer`) into states that block. Everything here is `[practitioner]` (from the source repo; not measured) unless marked otherwise.

**Lifecycle.**
`SIGNAL → CANDIDATE → EVIDENCE_READY → DRAFT → REVIEW → APPROVED_FOR_DRAFT_WRITE → DRAFT_WRITTEN → APPROVED_FOR_PUBLISH → PUBLISHED → READBACK → LEARNING`
Every transition is stored, attributable to an actor, and safe to repeat. A transition whose evidence or approval is missing does not happen — the pipeline fails closed.

**1. Classify first.** Assign every opportunity a single class from this list: refresh · consolidate · create · internal-link · distribute · **reject**. Opportunity scores, keyword difficulty and "AI visibility" help triage; none of them grants permission to draft. In particular, a low keyword difficulty plus the absence of an existing page is **never** a reason to create a page automatically — that rule from the same repo is refused (see Sources).

**2. Gates before any draft** — one failure blocks:

| Gate | Blocks when |
|---|---|
| Canonical owner | a live URL already serves this primary intent → the class becomes refresh or consolidate, never create |
| Intent overlap | the new URL would compete with one of our existing pages (see [content-and-intent-2.md](content-and-intent-2.md#cannibalization)) |
| SERP sameness | the page would just repeat what already ranks |
| Information gain | nothing new versus the top results — no data, angle or tool → reject |
| Evidence | any claim lacks an approved source |

These five are the value-per-URL gate. A pipeline that skips them risks mass-producing pages with little to no value to users — what Google's policy calls scaled content abuse when many pages are made "for the primary purpose of manipulating search rankings and not helping users", "no matter how it's created" `[documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-14]`.

**3. Internal links — plan them, then audit the finished copy.**
- Build the set of candidate URLs from the declared sitemap shards, deduplicated by canonical.
- Open each candidate target and record status, final URL, title/H1, canonical and topical fit. A path is never guessed.
- Put contextual links after the introduction; nothing forced, nothing off-topic.
- On the final text, check again: targets, anchors, whether each anchor matches its claim, self-link count, external citations.
- Tie the link check to a hash of the final text; any later edit invalidates it.

**4. Each capability is its own approval.** Six separate grants, none implying another:

| Capability | Default |
|---|---|
| read | allowed |
| draft (text only) | needs approval |
| CMS draft write | needs approval; read back at once after writing |
| publish | needs approval |
| redirect, delete, indexing change | needs approval |
| analytics change | needs approval |

Having a connector that works authorises nothing. A public sitemap is evidence of what exists and how it is organised — it says nothing about traffic, rankings or why anything changed. A read-only run still logs its endpoint, data window and freshness, and states "zero mutations".

**5. One readback record per change**, with these fields:

| Field | Content |
|---|---|
| Change | what changed, plus the exact artifact hash |
| Owner | who is accountable |
| Target | URL / query / topic |
| Baseline | window, metric, n |
| Checkpoints | see below |
| Source systems | where each number came from |
| Confounders | seasonality, indexing lag, brand spikes, campaigns, tracking changes, unrelated edits |
| Verdict | one of the four states below |
| Next playbook change | what the team does differently |

Checkpoint defaults from the source (defaults, not thresholds):

| Change type | Readback days |
|---|---|
| Refresh | 7, 14, 28, 56 |
| New page | 14, 28, 56, 90 |
| Technical fix | daily for 7, then 28 |
| AI-answer visibility | weekly |

Verdict states and their thresholds come from skill `seo-evidence` › experiments-and-revert-2 (helped / hurt / inconclusive / insufficient_data). The source's own "promote / keep testing / rollback / unproven" maps onto those four and is not a significance test.

**6. Loop rules.** Before a loop is switched on, pin down: its cadence and eligibility window; the single metric that counts and its target; the evidence floor; the priority formula; how many changes may run at once; and the conditions that stop it. Treat the target as an objective rather than a forecast. A sample that is weak cannot name a winner. Each outcome is bound to the exact variant that produced it. **An inconclusive result leaves priors unchanged.** Re-running a duplicate changes nothing. A cron only wakes the controller — the cron is not the loop.

## Coherence lint and UGC prompt-injection scan

Two gates proposed by the research report, neither yet built or measured on this site:

- **Coherence lint across guides** `[hypothesis]` — every statutory term has one definition, used identically across all guides (for Mowei: IVA, potência contratada, IAS). The lint lists each page that defines the term and fails when two definitions differ. Same idea as heuristic 4 (Consistency) above, applied across the site instead of within one page.
- **UGC prompt-injection scan** `[hypothesis]` — before rendering user-generated text (reviews, comments), scan it for hidden instructions aimed at an LLM (text addressed to an assistant, invisible or off-screen text, instruction-like strings in markup). A hit holds the item for moderation instead of rendering it. Same principle as "draft text is untrusted" in the blocking rules.

## Attribution

- **AgriciDaniel/claude-blog** — the Editorial review (P0–P3) section and the publish-integrity checks are carried largely verbatim from `claude-blog@skills/blog/references/editorial-heuristics.md` and `claude-blog@skills/blog/references/blog-delivery-contract.md`. Copyright line as written in the source header: "Copyright (c) 2025-2026 AgriciDaniel; ordinal rubric © 2024-2026 Paul Bakaus, Apache-2.0 — NOTICE carried: "adapted from impeccable v3.1.1, https://github.com/pbakaus/impeccable"". Licence: MIT.
- **pbakaus/impeccable** (`heuristics-scoring.md`) — origin of the method: the 0–4 ordinal scale and the P0–P3 severity, which claude-blog adapted from it (after Nielsen's 10 usability heuristics, NN/g 1994, rev. 2020). © 2024-2026 Paul Bakaus. Licence: Apache-2.0. NOTICE: "adapted from impeccable v3.1.1, https://github.com/pbakaus/impeccable". Modified: per-heuristic 0–4 tables cut to one-line criteria; Nielsen mapping table, hero-image, render and dark-mode checks removed; labels added; the source's 90/100 block threshold demoted to an unvalidated house heuristic; the `wordCount` check moved into its own Schema honesty section.

## Sources

- AgriciDaniel/claude-blog@skills/blog/references/editorial-heuristics.md, AgriciDaniel/claude-blog@skills/blog/references/blog-delivery-contract.md (v2.2.0) (phase-2 adapted file research/adapted/AgriciDaniel__claude-blog/editorial-review-gate.md) — P0 filter, ten heuristics, blocking rules, iteration cap, publish-integrity and `wordCount` ±5 % checks. COPY, MIT (method from pbakaus/impeccable, Apache-2.0).
- onvoyage-ai/gtm-engineer-skills@audit-content/SKILL.md:25-169 (phase-2 adapted file research/adapted/onvoyage-ai__gtm-engineer-skills/prepublish-claim-verification.md) — claim classes, five verification states, fabrication patterns, "wrong ≠ unverifiable" rule; GEO-paper discrepancy from onvoyage audit-website-aeo/SKILL.md:226, ReScienceLab opc-skills skills/seo-geo/SKILL.md:86-96, Auriti-Labs geo-optimizer-skill docs/geo-methods.md:24, :43, :62. INTEGRATE, MIT.
- ericosiu/ai-marketing-skills@content-os-portable-starter/README.md:27-41, ericosiu/ai-marketing-skills@skills/ai-native-content-os.md:6-17, ericosiu/ai-marketing-skills@skills/clickflow-seo-aeo-pipeline.md:5-11, ericosiu/ai-marketing-skills@skills/content-internal-linking.md:5-11, ericosiu/ai-marketing-skills@skills/rolling-cohort-optimization-loops.md:3-7, seo-ops/SKILL.md:133-170 (phase-2 adapted file research/adapted/ericosiu__ai-marketing-skills/agent-content-pipeline-gates.md) — lifecycle, classification, pre-draft gates, link audit, capability approvals, readback record, loop rules. The repo's `seo-ops/content_attack_brief.py:547-558` (every keyword with KD ≤ 20 and no page sent to automatic creation) is refused (REPORT §6). INTEGRATE, MIT.
- research/REPORT.md §7 ideas 8 and 10 — schema honesty check (`wordCount`) as a gate; coherence lint and UGC prompt-injection scan as `[hypothesis]` gates.
