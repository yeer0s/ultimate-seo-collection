<!-- split-header-2: part 2 of 2 of comparison-pages.md (original lines 126–195; boundary H2) -->
# Comparison pages (2 of 2) — rollout gates, comparison-site practice, unverified items
## Contents

- Rollout gates
- Comparison-site practice (the Mowei class)
- Unverified
- Cross-references
- Sources

Other parts of the same original file: [comparison-pages.md](comparison-pages.md).

<!-- /split-header-2 -->
## Rollout gates

Comparison and location templates fail the same way: a set grows past the point where anyone has read a sample of it. The numeric gates below are `[unvalidated house heuristic]` — nobody measured that 500 is the cliff and 499 is safe — but they exist to force a human decision at a defensible frequency, and they are worth adopting for that reason alone.

**Set-size gates** `[unvalidated house heuristic]`:

| Condition | Gate |
|---|---|
| 100+ pages published without content review | ⚠️ **WARNING** — audit a sample before publishing more |
| 500+ pages without written justification | 🛑 **HARD STOP** — explicit approval plus a thin-content audit |
| Unique content below 40% | ❌ flag as thin; the source recommends considering a hard stop below 30% |
| Fewer than 300 words per page | ⚠️ flag for review |

**Location pages are gated harder** `[unvalidated house heuristic]`: WARNING at **30+** pages with 60%+ uniqueness enforced, HARD STOP at **50+** requiring demonstrated legitimate presence in each location, a per-page content strategy, and real local signals. Google's doorway-page treatment is the specific risk; the tell is a set where only the city name changes.

**Rollout procedure** `[practitioner]`: publish in batches of **50–100**, monitor indexation and rankings for **2–4 weeks** before expanding, never publish 500+ programmatic pages at once, and human-review a **5–10% sample** of every batch before it ships.

**Uniqueness formula** `[unvalidated house heuristic]`:

```
unique % = words unique to this page / total words on page × 100
```

measured against every other page in the set, **excluding** shared header, footer and navigation, **including** template boilerplate. Two things make this weaker than it looks: the thresholds are invented, and **metadata is scored separately** — a set can pass on body copy while every URL in it carries one generated title/description shape. Score titles and descriptions as their own set, and treat a high-similarity metadata verdict as a gate failure regardless of body uniqueness.

**Safe at scale vs penalty risk** `[practitioner]` overlaps with `programmatic-seo.md`'s own examples — the additions are: user-profile pages (user-generated unique content) on the safe side, and on the risk side, **"[Competitor] alternative" pages without real comparison data**, which is precisely the failure mode of a comparison programme run as a keyword play.

Enforcement context: Google's scaled content abuse policy dates from March 2024 [documented: https://developers.google.com/search/blog/2024/03/core-update-spam-policies, 2026-10-11].

Site-reputation-abuse handling diverged by audience on **2026-08-28** (effective 2026-08-30), "Following discussion with the European Commission" [documented: https://developers.google.com/search/blog/2026/08/update-site-reputation-policy, 2026-10-14]: a manual action still affects search results for users outside the EEA; for users inside the EEA "the impact of the manual action won't apply", and the affected section "may be separated in our systems so that, over time, it ranks independently from the rest of the site". The action itself is still issued and notified (below). **Portugal is in the EEA** — report the risk for both audiences, and do not tell a Portuguese client the policy is inert for them.

Read "apply" above as the search-result effect only. Issuance and notice are unchanged: "it's possible that any given page might have a manual action taken on it", and "Site owners will continue to be notified within Search Console" `[documented: https://developers.google.com/search/blog/2026/08/update-site-reputation-policy, 2026-10-11]`. A Portuguese section can still receive one.

## Comparison-site practice (the Mowei class)

A consumer comparison portal is a comparison site by construction: every results page is a comparison page, and the ethics layer above is not decoration on it. All `[practitioner]`:

- **Compare total cost, not the headline rate.** An offer with an introductory period is two numbers — the promotional cost and the post-promotional cost — plus the horizon over which they combine. A page that ranks on month-one price and hides month-thirteen price is misleading even when every figure on it is accurate.
- **Disclose coverage explicitly.** "We compare N of the M providers operating in this market", with the excluded set nameable on request. A comparison that reads as exhaustive and is not is the single most damaging trust failure available to this page type.
- **Disclose commercial relationships and placement.** Commissions, sponsored positions, and the fact that a ranked position may be paid must be visible on the page carrying the ranking — not only in a policy page.
- **Publish the ranking logic, and answer "why does this offer rank here?" per row.** The per-row answer is also the most liftable passage on the page for an answer engine, which is a side benefit, not the reason.
- **Keep personalised calculator and wizard states out of the crawl.** A results URL parameterised by a user's consumption, household size or salary generates an unbounded URL space of near-identical pages — a crawl trap and a thin-content set at the same time. Canonicalise to the unparameterised comparison page, and index only the curated, stable comparison routes.
- **Guard price staleness wherever a scraped price reaches a title, a meta description or a snippet.** A cached title quoting a tariff the provider no longer offers is a trust defect on a YMYL surface, not a CTR experiment. The guard drops the price segment entirely when the source feed exceeds the freshness window. See skill `seo-evidence` › titles-and-serp-tests for the #155 conditions.
- **Every provider-facing number carries its as-of date and its source**, on the page, in the same visual unit as the number.

## Unverified

- June 2025 wave of scaled-content manual actions: community-reported [unverified: no Google page states the wave dates].
- Whether a comparison portal is an "online platform" under DSA Arts. 25 and 27 [unverified: no ruling or Commission guidance on comparison portals was checked].
- Portuguese vertical-regulator regime details in the EU legal gates table (DL 81-C/2017, IDD/ASF, ERSE comparator conduct, EECC Art. 103 / ANACOM certification, MiFID II boundary) [unverified: the source skill flagged these regime details as not checked against the instruments].
- Portuguese transposition of CCD2 Dir. (EU) 2023/2225 and of Dir. (EU) 2024/825 [unverified: no Diário da República text was checked].

## Cross-references

- `programmatic-seo.md` — the programmatic quality checklist, doorway test, template patterns, indexation rules, failure modes. Not restated here.
- skill `seo-evidence` › titles-and-serp-tests — price-in-title evidence (#155 vs #157/#158), title testing method, CTR-vs-qualified-clicks.
- skill `seo-technical` › schema-reference — `ItemList`, `Product`, `SoftwareApplication` shapes and required fields; the `FAQPage` retirement.
- skill `seo-technical` › crawl-and-index — canonical and indexability.
- skill `seo-technical` › rendering-and-sitemaps — the JSON-LD baseline.
- skill `seo-evidence` › evidence-and-tactics-1 — how to weigh a vendor survey like Intergrowth's against a controlled test.

## Sources

- claude-seo@skills/seo-competitor-pages/SKILL.md:24-45, 72-121, 125-140, 173-182 — page subtypes, comparison schema, title formulas, fairness guidelines; carried `[practitioner]`.
- claude-seo@skills/seo-plan/assets/saas.md:96-118 — nominative fair use guardrails `[practitioner]`; the 4–7% vs 0.5–1.8% conversion figure carried as `[vendor, Intergrowth Nov 2025]` with its missing denominator stated, explicitly not a target.
- claude-seo@skills/seo-programmatic/SKILL.md:74-98, 114-119 — rollout gates, scaled-content-abuse enforcement context, uniqueness formula and the separate metadata scoring; thresholds `[unvalidated house heuristic]`.
- claude-seo@skills/seo/references/quality-gates.md:20-45, 48-66 — location-page thresholds `[unvalidated house heuristic]` and the safe-vs-risky page-type table.
- Mowei-class practices — `[practitioner]`, from this project's standing rules on coverage, disclosure and price freshness; no external source.
- coreyhaines31/marketingskills@skills/competitors/SKILL.md:17, 67-73, 183-231 (phase-2 adapted file research/adapted/coreyhaines31__marketingskills/comparison-claim-audit.md) — evidence rules under Fairness, four-state Claim audit. INTEGRATE, MIT.
- installed/site-improvement@references/legal-gates.md, SKILL.md:57-83 (phase-2 adapted file research/adapted/installed__site-improvement/eu-legal-gates-comparison-pages.md) — EU legal gates table, audit gate; replaces reliance on US nominative fair use for EU sites. Application dates re-checked against EUR-Lex texts saved at phase2/sources/eu-law/eu-2024-825.txt (Art. 4(1)) and eu-2023-2225.txt (Arts. 47, 48(1)). INTEGRATE, in-house (no third-party licence).
- installed/site-improvement@references/aeo-citation.md (phase-2 adapted file research/adapted/installed__site-improvement/aeo-citation-deltas.md) — the comparison-portal schema mapping only (delta 3), plus delta 1 as the precise-number legal gate. INTEGRATE, in-house (no third-party licence).
- research/REPORT.md §7 idea 11 — legal gate before a precise number on credit, insurance or investment pages; methodology page as the P2B Art. 5 artefact.
