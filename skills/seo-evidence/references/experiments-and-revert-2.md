<!-- split-header: part 2 of 2 of experiments-and-revert.md (step-3 original lines 101–194; boundary H2) -->
# Experiments and revert — designs, measurement, revert triggers, attribution

## Contents

- Designs, ranked
- Measurement — GSC before/after, done right
- Revert triggers — pre-declared, human-confirmed
- Attribution log
- Ratchets and calibration ledger
- AI-citation measurement
- Sources

Other parts of the same original file: [experiments-and-revert-1.md](experiments-and-revert-1.md).

<!-- /split-header -->
## Designs, ranked

What a design can claim depends on what it controls for. From strongest to weakest:

1. **Randomised page cohort (SearchPilot-style split test).** URLs on one template are randomly assigned to control and treatment; both arms live through the same core updates, seasonality and competitor moves. Can claim: the treatment caused the difference between arms, within the stated uncertainty. Cannot claim: the same size elsewhere, or anything about a different template. This is where nearly all of the study's **118** controlled measurements come from, and **65 of 118** from one publisher.
2. **Matched holdout.** Treated and control chosen by hand to match on baseline traffic, template and intent. Can claim: a directional causal read if the pre-period parity check passes (the two groups tracked each other before the change). Cannot claim: freedom from selection bias — the person who chose the groups also chose the treatment.
3. **Pre/post with a seasonal control.** No untreated pages, but the read is against the same window last year or against an unrelated section of the site that shares seasonality. Can claim: the movement is unlikely to be the calendar. Cannot claim: that it is not a core update, a competitor, or a concurrent release.
4. **Pre/post, bare.** Before vs after on the treated pages, nothing else. This is what most published case studies are — every catalogue-entry source cited in skill `seo-technical` › migrations-and-recovery is "Before/after, no control". Can claim: the number moved. Cannot claim: why.

Two study-side rules that follow: **bundles support direction, not size** (92 of 182 entries), and when the published evidence for an entry is only design 4, the entry earns a test on the client's site, never an import. IT DEPENDS entries are the extreme case — **of the 12 sides across the 6 IT DEPENDS entries, 2 rest on a controlled test and 10 do not**.

## Measurement — GSC before/after, done right

Shipping a fix is a hypothesis, not a result. Every applied change gets a **before/after GSC read** on the affected URLs. Compare two equal windows (the 14 or 28 days before vs after the change went live, matched weekday span to control for weekly seasonality) on the query/page rows that actually changed. Bing's AI Performance counts citations, not ranking (§ AI-citation measurement).

**Pre-declare before the change ships** — all of these, written down, in the recipe above:

- **MDE** — the smallest relative move you would act on (15% relative is the default used in the arithmetic below).
- **Window** — 14 or 28 days per side, matched weekdays; longer for low-volume templates.
- **Primary metric** — one of clicks, CTR, position, impressions; the others are secondary.
- **Guardrail metrics** — leads, revenue, error rate, wrong-output reports. A `helped` on CTR with a fall in leads is a `hurt`.
- **Stopping rule** — when the window closes, the verdict is issued; no peeking-and-extending until it turns green.
- **Rollback trigger** — see the next section.
- **Owner** — who issues the verdict and who executes the revert.

**Two independent verdicts per URL — one for position, one for CTR — never one label ORing them together.** They have different sampling behaviour, so a single `helped` that could have come from either is uninterpretable. A URL routinely earns a position verdict and no CTR verdict; that is a correct outcome, not a gap.

**Four states, one per metric per measured URL:** `helped`, `hurt`, `inconclusive`, `insufficient_data` — plus `no_effect (TOST ±band)`, which is not a fifth default state but a claim earned only by a passing equivalence test. Never leave a measured URL unlabelled.

**Position verdict.** `helped` / `hurt` at ≥ ~1.0 place of movement, `inconclusive` inside that band, on **≥ ~100 impressions per window** `[unvalidated house heuristic]` — a practical cut, not a significance test. Average position is a mean over every impression, so it stabilises fast — but 100 impressions do not guarantee a stable average when the query mix, device split, country or SERP composition changed between windows. Check that the top queries per URL are the same set in both windows before reading the position.

**CTR verdict — count CLICKS, not impressions.** CTR is a proportion p̂ = c/n with c clicks on n impressions. Its relative standard error is

RSE(p̂) ≈ √((1 − p) / c)

so `1/√clicks` is the **low-CTR approximation** (1 − p ≈ 1), not exact. At organic CTRs (1–10%) it is fine, and the practical rule stands: **an impression floor cannot serve this metric; count clicks.**

**The arithmetic, corrected.** Take 10,000 impressions per side and a 15% relative lift from a 3.4% baseline: 340 clicks vs 391. Pooled two-proportion z ≈ 1.92, **p ≈ 0.055** — it does not clear p < 0.05. For a 15% relative move to cross p < 0.05 at 3.4% baseline you need **≈ 355 baseline clicks per side**; for **80% power** against that same 15% move you need **≈ 720 clicks per side**. Therefore at 340 clicks per side a true +15% is **missed about half the time**. Not symmetric: a 15% **fall** (340 vs 289) gives z ≈ −2.07, **p ≈ 0.039** — the lower pooled rate shrinks the standard error — so a fall crosses p < 0.05 from ≈ 305 baseline clicks (80% power ≈ 625). An older table called "no movement at ≥340 clicks" `neutral` — a coin flip labelled as a finding.

| Clicks per side | State | What you may say |
|---|---|---|
| < ~100 `[unvalidated house heuristic]` | `insufficient_data` | Nothing. At 50 impressions a page has 1–2 clicks; 1 → 2 is a **+100% CTR swing** of pure noise |
| ~100 – ~355 | `inconclusive` (annotate `indicative` if the direction holds across sub-windows), unless the test on the actual counts gives p < 0.05 | "Worth a look." A +15% lift cannot reach p < 0.05 here; a −15% fall can (from ≈ 305), so `hurt` is possible |
| ≥ ~355 | `helped` / `hurt` at p < 0.05; otherwise `inconclusive` | A verdict on a *detected* move. ~720/side gives 80% power against a +15% move |
| ≥ ~720 | `helped` / `hurt` / `inconclusive`, and `no_effect` becomes claimable **only via TOST** | Enough power that a null is informative — if an equivalence test passes |

Rules that go with the table:

- **`inconclusive` is not `neutral`.** "Not statistically significant" means the data did not detect a move of the pre-declared size; it does not mean there was none. To claim *no effect* run an equivalence test (TOST: two one-sided tests against a pre-declared practical band, e.g. ±10% relative) and pass it. If TOST passes, write `no_effect (TOST ±10%)`; if it does not, the state stays `inconclusive` however many clicks you had.
- **`indicative` is a confidence annotation, not a fifth state.** The output contract stays at four states. Annotate `inconclusive (indicative: +)` when every sub-window points the same way; never promote it to `helped`.
- **Run the test, do not trust the table.** The thresholds above are for a 15% relative MDE at a ~3–4% baseline CTR and move if either changes, and with the direction of the move. This skill ships no calculator; any two-proportion calculator will do, run on the actual counts of both arms; state the baseline, the MDE and the alpha you used in the verdict.
- **Set-level aggregation adds counts and can add composition bias.** Most URLs never reach ~355 clicks; that is the answer, not a reason to lower the bar. Aggregate across the changed set to read CTR where clicks add up — but a set whose high-click URLs happen to be the ones that improved will read `helped` while the median URL did nothing. **State the composition** of the set (how many URLs, what share of clicks the top five carry) next to every set-level verdict, and never redistribute a set verdict back onto individual URLs. Pooling does not manufacture a control.
- **Correlation, not proof.** A `hurt` verdict is a prompt to *look*, never proof the change caused the drop — in a pre/post read a core update, seasonality or a competitor can swamp your edit; with a control, look for what hit one arm only. Confirm the mechanism before reverting.
- **Attribute deliberately.** Note what else shipped in the same window; if three changes landed together you cannot cleanly credit one. Stagger meaningful changes when you need a clean read.
- **Mind the level.** CTR and position are leading indicators; the business outcome (leads, revenue) sits one step downstream. A `helped` here is necessary, not sufficient — and a lower aggregate CTR can coexist with better revenue when misleading clicks disappear.

## Revert triggers — pre-declared, human-confirmed

The study's rule, reconciled with "findings are sensors, not tickets — not an auto-revert": **the trigger is declared before launch; a human confirms the mechanism before executing it.** Declaring the trigger stops the outcome from being read as confirmation; the human step stops a core update from being read as your title change.

**Immediate revert classes — no window, no statistics, revert first and diagnose after** `[unvalidated house heuristic]`:

- Broken access: a template 5xx/404s, robots or noindex shipped by accident, a canonical pointing off-site, hreflang or sitemap dropping a locale, render resources (`/_next/`, `/static/`) blocked.
- Wrong financial or regulatory output on a YMYL surface: a calculator, tariff, rate or deadline shown incorrectly. On a comparison site this is not an SEO revert, it is a correctness incident; SEO measurement stops until it is fixed.
- A misleading offer: a price, "free", "best" or availability claim in a title or snippet that the page does not honour.

**Performance reverts — the pre-declared band, then the mechanism check:**

1. Treated falls vs control past the pre-declared band (default: >15% relative on the primary metric) for N consecutive weeks (default N = 4 for clicks/CTR, longer for position on low-volume templates) `[unvalidated house heuristic]`.
2. Confirm mechanism before acting. The read is the gap between arms, each against its own baseline, with its uncertainty; control falling too does **not** clear the change (control 1,000 → 900, treated 1,000 → 630 is a 30% shortfall). Core updates, seasonality and demand hit both arms of a randomised split, so they explain a shared fall, not the gap. Look for what hits one arm only: the deploy log, a SERP sample on the treated queries, pre-period parity (a matched holdout can drift). With no untreated pages (designs 3–4), ranking-updates history, YoY and Trends are the only guard.
3. Revert only the treatment; leave the control alone so the recovery can be read against it.
4. **Log nulls and harms** in the attribution log with the same care as wins. The published record under-reports them (81.9% of 1,700 positive); yours must not.

## Attribution log

One row per change, kept next to the deploy log. Fill the verdict column only when the window closes.

| Date shipped | Change (one treatment) | URLs / template | Design | Primary metric · window · MDE | Verdict (per metric) | Confounders noted |
|---|---|---|---|---|---|---|
| 2026-09-22 | Title pattern B on tariff results | /comparar/energia/* (arm B, 48 URLs) | randomised split | CTR · 28d · 15% rel | position: inconclusive · CTR: pending | none yet |
| | | | | | | |

Columns to keep: the design (what the verdict can claim), the set composition when pooled, and a link to the recipe block that pre-declared the trigger. A row with no verdict after its window closed is a defect, not a pending result.

## Ratchets and calibration ledger

Fixes that cannot silently come back, and a record of what each recommendation did.

**Ratchets** `[unvalidated house heuristic]`

- **Budget ratchet.** A good value, once measured, becomes the budget: template LCP P75 measured at 1.9 s means the budget is 1.9 s, not "under 2.5 s"; sitemap 404s measured at 0 means the budget is 0. Budgets move only tighter; loosening one is an exception with a name and a date.
- **Regression ratchet.** Each fixed SEO defect leaves behind a guard that fails if the defect returns — a test, a deploy-gate check or a lint rule (canonical pointing off-site, noindex on a money template, hreflang losing a locale). Wire the guards into skill `seo-technical` › seo-drift-monitoring.

**Predict when you recommend.** For each recommendation, write down the direction or range you expect on the primary metric, together with a **review date**, which is when the window in the recipe in [experiments-and-revert-1.md](experiments-and-revert-1.md) closes. If nothing has been measured by then, the recommendation is not done.

**Log of what our own advice did** — `outcomes.jsonl`, append-only, one line per recommendation that reached a decision. The fields combine the site-improvement ledger with the closed-loop readback record from ericosiu/ai-marketing-skills `[unvalidated house heuristic]`:

`{date, site, template, rec_id, tactic_ref (#entry or reference), artifact_hash (exact shipped change), owner, scope (URL / query / topic), predicted:{metric, baseline, baseline_n, delta, window_days}, checkpoints, source_systems, actual:{value, clicks_or_n, delta}, verdict, traffic_class, domain_class, confounders, next_playbook_change, notes}`

- **Ledger verdicts:** `confirmed | direction_ok_overpredicted | direction_ok_underpredicted | refuted | inconclusive | invalid_measurement | not_shipped`. These grade the *prediction*; the four per-metric states above are the inputs. **Write `not_shipped` and refused tactics into the log as well** — leaving them out is survivorship bias.
- **Confounders to name on every line:** seasonality, indexing lag, brand spikes, campaigns, tracking changes, unrelated edits.
- **Checkpoints (readback source defaults, not thresholds):** AI-answer visibility weekly; for a technical fix, daily over 7 d and again at 28 d; a new page at 14/28/56/90 d; a refresh at 7/14/28/56 d. The verdict still uses the windows and click thresholds above. Its "promote / keep testing / rollback / unproven" maps onto our states; it is not a significance test.
- **An outcome belongs to the exact variant that shipped** (hence `artifact_hash`), and an `inconclusive` result does not update priors.

**How the log may be used** `[unvalidated house heuristic]`

- What our own sites show may **order** a shortlist, nothing more: never quote it to a client as the expected effect, and never let it change the mark of a published-study entry (that would be circular citation).
- Refuted twice on the same template class → the tactic gets a "do not use when …" line. Confirmed three or more times with an honest n → keep it. A single-site result never becomes "any website"; `domain_class` keeps PT-finance results away from unrelated sites.
- Low-traffic lines (`inconclusive` / `insufficient_data` under the thresholds above) may add qualitative tags only; they never narrow a range.
- More than one primary change per template per window → `invalid_measurement`.
- A lift that breaches a guardrail (leads, errors, wrong-output reports) → `refuted`; that is metric gaming.

**Meta-metrics, every quarter** (targets `[unvalidated house heuristic]`). Three numbers: the share of recommendations whose outcome is filled in by 28 d after window close (target ≥80%); the mean |predicted − actual|, per reference file; and refusal escapes (target 0). A quarter that shipped work but added no ledger lines means the loop is dead, and the next audit says so in one line: **"calibration stale since <date>"**. As of 2026-10-11 the installed site-improvement skill's priors table and ledger are empty too.

**No unsupervised model rewrites of regulated copy.** A model may improve structure, internal links and performance by itself; on energy, credit, insurance and investment surfaces, any title, meta or claim copy stays human-reviewed (EU legal gates in skill `seo-content` › comparison-pages).

**KPIs to read beside rankings** `[unvalidated house heuristic]`: stage drop-off along landing → tool → results → lead · AI citations per tested answer opportunity (fixed pt-PT panel) · time from landing to submit · the provider's follow-through on leads · brand-mention sentiment in the sources engines draw on. While any of these is measurable, a vanity metric (pageviews, aggregate CTR) is never success.

## AI-citation measurement

The full method now lives in skill `seo-ai-search` › ai-citation-measurement. Essentials for test design:

- **Bing Webmaster Tools — AI Performance** (public preview, 10 Feb 2026) is the first-party read of AI-answer citations for Bing-grounded engines; Bing says its Average Cited Pages figure "does not indicate ranking, authority, or the role of any page" `[documented: https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview, 2026-10-11]`. On Google, Search Console's generative AI performance report (rolled out to all sites "As of August 31, 2026") shows impressions in Search generative AI features by page, device and country `[documented: https://support.google.com/webmasters/answer/16984139?hl=en, 2026-10-11]`.
- **Repeated prompt panels** where no first-party report exists: a fixed panel per answer opportunity, run on a schedule, recording engine, locale, date and model version; report citations per tested answer opportunity, never one "AI visibility" percentage. Agentic-SEO practitioners use fixed prompt sets `[practitioner: anonymised sources · consensus · 5 thr / 54 · newest 2026-08-16]`; technical ones prefer logs to prompt dashboards `[practitioner: anonymised sources · consensus · 3 thr / 33 · newest 2026-07-09]`.
- **Check the crawler policy first**: an engine whose bot is blocked at the edge or in robots reads nothing `[unvalidated house heuristic]`.

Cross-references: `SKILL.md` rules 5–6 (two verdicts, pre-declared revert), skill `seo-content` › gsc-page2-audit (opportunity bands and the anonymisation trap), `evidence-and-tactics-1.md` (per-entry marks and denominators), skill `seo-technical` › migrations-and-recovery (rollback playbook for URL, domain and consolidation changes), `titles-and-serp-tests.md` (the title family and the displayed-title check).

## Sources

- installed/site-improvement@references/self-improvement-loop.md, installed/site-improvement@references/calibration/priors.md, installed/site-improvement@references/calibration/outcomes.jsonl, installed/site-improvement@references/lifecycle-and-kpis.md (phase-2 adapted file research/adapted/installed__site-improvement/calibration-loop-and-ratchets.md) — budget and regression ratchets, prediction at recommendation time, the outcome ledger and its verdicts, ledger-use rules, meta-metrics and the "calibration stale since" line, the regulated-copy rule, the KPI layer. INTEGRATE, in-house (no third-party licence found).
- ericosiu/ai-marketing-skills@seo-ops/SKILL.md:133-170, content-os-portable-starter/skills/rolling-cohort-optimization-loops.md (phase-2 adapted file research/adapted/ericosiu__ai-marketing-skills/agent-content-pipeline-gates.md, §5 and one §6 rule only) — closed-loop readback fields (artifact hash, owner, scope, baseline n, checkpoints, source systems, confounder list, next playbook change), source-default checkpoints, verdict mapping, "inconclusive does not update priors", outcomes bound to the exact variant. INTEGRATE, MIT.
