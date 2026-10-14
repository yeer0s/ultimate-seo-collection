# Migrations and recovery — URL changes, domain moves, consolidation, incidents, rollback
<!-- split-header: part 1 of 2 of migrations-and-recovery.md (step-3 original lines 1–37; boundary start) -->
<!-- /split-header -->

## Contents

- Classify the incident first
- Sources

Other parts of the same original file: [migrations-and-recovery.md](migrations-and-recovery.md).

## Classify the incident first

Treatment before classification is how disavow files get uploaded against a deploy bug. Run the checks in this order and stop at the first that explains the loss; several can be true at once, so finish the list before choosing a treatment.

| Class | The check that distinguishes it | What it looks like |
|---|---|---|
| **Manual action** | GSC → Security & Manual Actions → Manual actions. Non-empty = this class. | Named section or "site-wide", a policy cited, a reconsideration path. |
| **Core / ranking update** | Google's ranking-updates history against the break date; compare an untreated section and a competitor set over the same days. | Site- or template-wide step change within days of a listed update; control sections move too. |
| **Site-reputation action** | Same report; note the audience. From **30 Aug 2026** («Following discussion with the European Commission»), a site reputation abuse manual action is still issued and notified in Search Console, but **its impact does not apply for searchers in the EEA**; the affected section may instead be separated to rank independently; outside the EEA the action still affects the affected portion `[documented: https://developers.google.com/search/blog/2026/08/update-site-reputation-policy, 2026-10-14]`. Portugal is in the EEA. | A third-party or off-topic section loses visibility while the core holds. This does **not** make parasite sections advisable: policy risk outside the EEA, reputational and YMYL-correctness risk everywhere. |
| **Deployment or rendering failure** | Deploy log for the break date; URL Inspection → Test Live URL → *Rendered HTML* on three URLs; `curl` the first-pass HTML; robots, `noindex`, canonical and status headers as served. | Loss coincides with a release; shell HTML, canonical elsewhere, accidental `noindex`/`Disallow`, redirect loop. Immediate-revert class. |
| **Indexing change** | GSC page indexing report by reason and template; indexed counts before/after. | "Crawled – currently not indexed", "Duplicate, Google chose different canonical", soft-404s rising on one template. |
| **Demand shift or seasonality** | Trends for head queries; GSC impressions YoY on the same weeks; if impressions and clicks fell together and position held, it is demand. | Position flat, impressions and clicks down, same dip last year. |
| **Security incident** | GSC → Security issues; crawl as Googlebot for injected content; server logs. | Hacked-content warnings, spam URLs in coverage, snippets in the wrong language. |
| **CTR loss with rank held (AI Overview class)** | Run only after the deploy, indexing and manual-action checks are clear. GSC query filter and a dated SERP check per query (subsection below). | Average position held, impressions flat or rising, clicks falling — an AI Overview now answers above the result. |

Slow, page-by-page loss on pages that used to perform is a refresh question, not an incident: decay triage is in skill `seo-content` › content-and-intent-2 § Content refresh workflow (Step 0).

Two corrections this skill used to get wrong:

- **"Crawled – currently not indexed" establishes crawling without indexing and does not name the cause.** Google's help says only that the page was crawled but not indexed, may or may not be indexed in future, and need not be resubmitted `[documented: https://support.google.com/webmasters/answer/7440203, 2026-10-12]`. It does not certify that robots, noindex and rendering are clear, and does not by itself justify an "authority triage" story. Read the rendered HTML, the served canonical and any near-duplicates before reaching for value or authority explanations. Republishing under a fresh slug is not a routine recovery step (next section) `[practitioner]`.
- **`site:` is a quick check, not the status of record.** Google's page indexing help suggests `site:` searches, including `site:<exact-url>`, as a quick check for sites under 500 pages, and the URL Inspection tool to find the index status of a specific page and why it is not indexed `[documented: https://support.google.com/webmasters/answer/7440203, 2026-10-12]`. This skill is stricter (`SKILL.md` rule 1): a `site:` result is a lead to confirm, never the reported index status; report from URL Inspection for a URL and from the page indexing report for a template `[unvalidated house heuristic]`.

### CTR loss with rank held — the AI Overview class

Pattern: **position held, impressions flat or up, clicks down.** Treat it as its own class only once the deploy, indexing and manual-action rows above have come back clean.

**1. Isolate the queries.** In GSC compare the last 28 days with the 28 before, weekdays matched. Keep queries whose **CTR fell by 20% or more while impressions changed by no worse than −10%**, with average position roughly unchanged; take the 20 that lost the most clicks `[unvalidated house heuristic]`. Before trusting the comparison, check the data-reliability windows in skill `seo-engine-policies` › google-updates-timeline.

**2. Confirm the SERP for each query.** Logged out, with location and language matched (pt-PT / Portugal for Mowei), record: is an AI Overview shown; are we cited in it (visible, or behind "show more"); who else is cited; how many organic results sit above the fold. Keep a dated screenshot — the SERP changes while you work.

**3. Segment** `[practitioner]`

| Segment | Pattern | Priority |
|---|---|---|
| A | AI Overview present, cites us | Low — the lost clicks come from the format; work on the snippet and on brand impression |
| B | AI Overview present, does not cite us | High — a retrievability / answer-passage gap |
| C | AI Overview present, cites a competitor | High — read the cited passage: which fact, table or source do they have that we lack? |
| D | No AI Overview; the intent moved | Not this class — go back to SERP and intent analysis |

**4. Diagnose segments B and C** `[practitioner]`

- Answer passage: the direct answer within the opening lines, the query restated as a heading, sentences that stand alone and carry a specific figure, a date and a source.
- Freshness with substance: a visible updated date, current-year figures, sources revised within the last 12 months. Changing only the date does not count.
- Trust: a named author or reviewer, primary sources, consistent entity details.
- Access: the answer is in the server HTML; Googlebot is allowed — Google-Extended has no bearing on AI Overviews `[documented: https://developers.google.com/search/docs/appearance/ai-features, 2026-10-11]`; the answer sits behind no paywall; use structured data only when it agrees with what the page visibly shows `[documented: https://developers.google.com/search/docs/appearance/ai-features, 2026-10-11]`.

**5. Re-read and stop.** Re-check at T+7, T+14 and T+28 using the verdict rules in skill `seo-evidence` › experiments-and-revert-2, reading citation and CTR separately. The source suggests "CTR back to >50% of pre-drop baseline by T+28" as the bar for success — an `[unvalidated house heuristic]`; declare your own bar in advance. If segment B does not recover, the query is probably being answered from the model or the index without needing our page: move effort to adjacent long-tail and comparison intents. For queries the business should not be chasing, stop — that traffic was not worth defending.

## Sources

- aaron-he-zhu/aaron-marketing-skills@seo-geo/implement/geo-content-optimizer/references/ai-overview-recovery.md (phase-2 adapted file research/adapted/aaron-he-zhu__aaron-marketing-skills/ai-overview-ctr-loss-triage.md) — the CTR-loss-with-rank-held class: query filter, SERP check, A–D segments, B/C diagnosis, re-read and stop rules (FAQ/HowTo schema steps and the DR<30 gate were cut upstream and stay out). INTEGRATE, Apache-2.0.

