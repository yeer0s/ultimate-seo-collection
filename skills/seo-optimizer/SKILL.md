---
name: seo-optimizer
description: >-
  Routes search-visibility work to the right SEO subskill and runs full SEO audits. Use for a full or pre-launch SEO audit of a site, page or route, or when no seo- subskill clearly fits; a question led by one area (engine policies, evidence, technical, content, authority, AI search, strategy), even one that touches a second, loads those subskills directly instead. Triggers: "audit/review our SEO", "pre-launch SEO", "SEO health check", "why isn't this ranking". Answers partial questions and names adjacent gaps. Holds the full evidence grammar; each seo- subskill carries its short form. Not for paid-ads tracking, legal review, or brand work with no search component.
---

# seo-optimizer

Organic visibility, AI answer-engine citations, trust, conversion — in that order. This skill routes and audits; seven `seo-` subskills hold the depth.

## Load rule (every seo- skill)

Descriptions always; a SKILL.md body on trigger; then **one reference per load-when row the question touches** — another only if the question spans another row or a file's `Next:` line points there. Never open files "to be thorough". Ledger parts, practitioner parts, engine pages and the crawler registry are lookup-only.

## Philosophy

1. **People-first, search-aware.** Satisfy a real user, then make it crawlable and trustworthy.
2. **Intent before keywords:** the job decides the page.
3. **Clusters over isolated articles.**
4. **Durable assets, not hacks:** crawlability, trust, links, original data.
5. **Conversion is the point.** Ask once: **would this page deserve to exist if Google did not exist?** If no, rethink the page.

### The Shortcut Trap

Legitimate SEO is high-friction. Shortcuts that skip it at scale — mass low-value pages, link drops, PBNs, service-for-link swaps, duplicate-filter evasion — match spam policies. **Self-check:** *low-effort + systematised + scaled + no value per URL* → refuse; value per URL decides, not the production method. The refusal is a **policy and YMYL-correctness refusal, not an evidence claim**: unedited AI articles show +17 pp positions `[measured: MAINSTREAM, #50, n=4, c=1 — uncontrolled before/after; the one A/B reports direction only]`. Agent pipelines run the fail-closed gates in skill `seo-content` › publishing-gates.

**Owned-property links** are judged by purpose and footprint, not ownership: a link a reader would expect is navigation; a network built to pass rank is refused below.

**EEA `[documented: https://developers.google.com/search/blog/2026/08/update-site-reputation-policy, 2026-10-11]`:** from 30 Aug 2026 a site-reputation-abuse manual action is still issued and notified, but it no longer affects rankings for EEA searchers (Google may instead separate the section so it ranks on its own merits); outside the EEA it still demotes the affected section. Policy risk differs by searcher location; the refusal stands on correctness and reputation.

### Hard refusals

Never recommend or implement: keyword stuffing, doorway pages, **scaled content abuse** (many pages made primarily to manipulate rankings, little to no value, «no matter how it's created»), fake reviews, link farms/PBNs/domain pools, cloaking, parasite SEO, comment/forum spam, hidden links, expired-domain tricks, **service-for-link exchanges, cross-linking a portfolio of sites you control beyond links a reader would expect (reciprocal, sitewide, footer), and duplicate-filter evasion** (identical bodies, changed URL/H1/title). Spam-policy violations.

## Evidence marks — how every recommendation is labelled

Every tactic you recommend carries one label next to it:
`[documented]` engine documentation · `[measured: MARK, n=S samples, c=C controlled]` a published measurement · `[practitioner]` operating judgment · `[hypothesis]` mechanism story.

**Numbers keep their denominator.** "+113% AI citations (entry 60: 7 independent samples — 1 controlled A/B reporting direction only, 1 before/after with control at +113% on 123 pages, 4 uncontrolled, 1 design unclear; the 20-vs-20 pages is the study's replication recipe, not the measurement)" — never "+113%". The study's "N of M samples" column means N samples measured the headline metric out of M independent samples — it is NOT a controlled-test count; read controlled counts from each entry's study-design line. If the sample or control count is not reported, write "not reported" and do not headline the gain.

**Marks are counts, not verdicts.** MAINSTREAM = ≥3 independent samples (or 2 if both controlled): how many published, not whether it works. MAINSTREAM with 0 controlled tests and a range crossing zero = "published, direction unresolved". IT DEPENDS = ask the named moderator question, then test — 10 of 12 IT DEPENDS sides have no controlled test. EXPERIMENTAL = ≤2 samples, no E score; never quote one as evidence of size. ACADEMIC = benchmark sizes, not live-site.

**E and A never merge.** Quote evidence and actionability separately; shortlist rank weights A 0.65 and is not evidence.

**Bundles support direction, not size.** 92 of 182 entries changed several things, measured one outcome. Credit the bundle.

**Discount the record.** 81.9% of 1,700 published outcomes are positive; the hand-verified 90 ran 64%. 602 of 769 tactics have no controlled test. 65 of 118 controlled measurements come from one publisher — say when a claim's controlled evidence is single-publisher.

**Never forecast a published number onto a client site.** Medians (+36% sessions, 87 entries) are what publishers chose to publish. The only forecast allowed is built from the client's own GSC demand and funnel.

**No rollout without a revert rule.** Before any change: applicability, holdout, what stays fixed, primary metric + window, and the pre-declared trigger that reverts it. Without one, every outcome reads as confirmation.

Full ledger, six-part replication recipe, 182-entry catalogue: load skill `seo-evidence` (Evidence ledger).

**Closed set of 9 labels.** `[documented: <URL>, <YYYY-MM-DD>]` — a page we read, with its check date. `[documented-secondary: <source>, <date>]` — official page unread, named secondary used (only in `## Unverified` or an engine page §5/§8). `[unverified: <what is missing>]` — only in `## Unverified` or as a pointer `<topic>: unverified [unverified: …]; see <pointer>.` `[practitioner: anonymised sources · <label> · N thr / S · newest YYYY-MM · G/C]`. `[vendor]`, `[memory]` (verify before use), `[unvalidated house heuristic]`. One label per claim; only a dated fetch upgrades one.

## Operating sequence (run every time)

1. **Business understanding** — offer, buyer, geography, conversion goal, competitors, proprietary data; pick the scope and name the points it covers.
2. **SERP & intent** — match the page type to what the SERP rewards.
3. **Keyword universe** — by intent and by type.
4. **Architecture** — keywords → page types; depth budget ≤2 clicks money pages, ≤3 clusters.
5. **Audit** — detect the framework, run the 8 points (Explore subagent above 200 routes), score PRESENT / PARTIAL / MISSING with file:line.
6. **Prioritise** by `impact × business value × confidence ÷ difficulty`; file each action under **one primary lane** (eligibility · intent · content · on-page · experience · authority · measurement) and stop at the first failing gate `[practitioner]`. Lanes: OP1.
7. **Report**, verdict first. 8. **Ask** which gap to start with.

## The 8-point audit (one line each; depth in the owning skill)

| # | Point | Owner |
|---|---|---|
| 1 | Per-page meta: own title, description, OG, canonical per route and locale | `seo-evidence` (titles), `seo-technical` |
| 2 | Structured data matching visible content; no FAQ/HowTo rich-result promise | `seo-technical` |
| 3 | Breadcrumbs: `BreadcrumbList` + visible trail | `seo-technical` |
| 4 | Programmatic pages: one URL per distinct intent, value per URL | `seo-content` |
| 5 | Internal linking: topic links, no orphan money page | `seo-content` |
| 6 | Technical hygiene: robots, sitemap, canonicals, redirects, rendering, CWV, hreflang | `seo-technical` |
| 7 | GSC + Bing Webmaster Tools day one; IndexNow; 7b: GSC "Search generative AI" control on include (set or inherited) | `seo-technical`, `seo-engine-policies` |
| 8 | One editorial link from an owned property a reader expects | `seo-authority` |

## Decision rules

1. Name what the SERP rewards; every recommendation is an action (page, targets, anchors); every page has a job.
2. Refresh or consolidate — diagnose first; date-only bumps are anecdotes.
3. YMYL trust signals are a requirement `[practitioner]`: bylines, primary sources, dates, legal entity, methodology page.
4. **Audit any connector before trusting it** (GSC/MCP servers, crawlers, SEO APIs): check what it requested and returned.
5. **Policy gate first**: a tactic an engine forbids is not graded or built. Label every tactic.

## Route the question

| User asks about… | Load skill | Open first (load-when rows) |
|---|---|---|
| penalties, de-indexing, bans, manual action, "is X allowed on Bing", AI opt-outs | `seo-engine-policies` | EP1 (one engine) · EP2 (≥2, "which engines") · EP3 (dated Google update) |
| "does X work", studies, practitioners, myths, A/B, revert | `seo-evidence` | EV1 (does it work) · EV2 (named entry) · EV3 (practitioners) · EV4 (test, revert) · EV5 (titles) |
| crawl, index, render, schema, CWV, hreflang, migrations, traffic loss | `seo-technical` | TE1–TE11 |
| keywords, intent, briefs, programmatic, comparison, local, GSC page-2 | `seo-content` | CO1–CO10 |
| links, PR, E-E-A-T, brand, Reddit/YouTube, disavow | `seo-authority` | AU1–AU2 |
| AI answer engines, AI crawler access, llms.txt, AI-citation tracking | `seo-ai-search` | AI1–AI7 |
| strategy, roadmap, ideas, resources | `seo-strategy` | ST1–ST5 |

**Multi-part order:** policy gate → evidence → implementation (500 city pages: `seo-engine-policies` → `seo-evidence` → `seo-content`), each stage opening only its own rows. A full audit is OP1 plus ≤3 subskill rows.

## Audit delivery

| ID | Question shape | Open |
|---|---|---|
| OP1 | full audit, report template, lanes, delivery gates | [audit-output](references/audit-output-and-templates.md) (+ [part 2](references/audit-output-and-templates-2.md)) + [measurement-gates](references/measurement-gates-and-checklists.md) |
| OP2 | paid-API spend guard, field allowlists, prompt-file tests | [measurement-gates part 2](references/measurement-gates-and-checklists-2.md) |

## Final notes

- Each dated claim names its check date; engine pages are re-fetched after 180 days `[unvalidated house heuristic]`.
- Never fabricate a score; say when a check is uncertain.
