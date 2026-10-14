# Experiments and revert — holdouts, power, verdicts, rollback
<!-- split-header: part 1 of 2 of experiments-and-revert.md (step-3 original lines 1–100; boundary start) -->
<!-- /split-header -->

## Contents

- Why every rollout is an experiment
- The six-part replication recipe

Other parts of the same original file: [experiments-and-revert-2.md](experiments-and-revert-2.md).

## Why every rollout is an experiment

The Ovisy SEO Meta Study (Ćorluka, Sept 2026) puts it in one sentence: *without a rule for when to revert, every outcome reads as confirmation.* A change shipped with no revert rule cannot lose — a rise is credited, a fall is blamed on a core update, a flat line is "still bedding in". That is not measurement; it is a story with a graph attached.

The published record shows what that habit produces at scale:

- **602 of 769** scored tactics have no controlled test behind them; 138 rest on exactly one; 23 on two; 6 on three or more. Roughly four out of five rest on somebody watching a graph move.
- **81.9% of 1,700** published outcomes are positive (1,392 improvements, 196 mixed, 65 declines, 46 no effect — 1,699 of the stated 1,700; keep the gap visible). The **90 hand-checked** documents ran **64%** positive, 8% negative — coding inflation sits on top of publication bias.
- **65 of 118** controlled measurements come from one publisher. When a claim's controlled evidence is single-publisher, say so.
- **92 of 182** entries changed several things and measured one outcome. A bundle supports direction, never size.

The consequence for this skill: a published lift is evidence that a direction is worth testing on the client's site. It is never a forecast for that site. The only forecast allowed is built from the client's own GSC demand and funnel, and the only proof that a change worked is a read against a control the client owns.

## The six-part replication recipe

The study attaches the same six parts to every entry. Fill all six before the change ships; an empty "when to revert" means the rollout is not ready.

```
Tactic / entry #:
Mark and denominator:   [measured: MARK, n=S, c=C] — printed effect, metric, design(s)

When it applies       — the site/template condition that has to be true first
Before you start      — baselines captured (metric, window, per-URL and set-level), holdout chosen
What to change        — the ONE treatment, on the named cohort only
What to keep          — everything held fixed on treated AND control during the window
What to measure       — primary metric + window + MDE; guardrail metrics (leads/revenue/errors)
When to revert        — the pre-declared trigger; who confirms mechanism; who executes
Owner / date / ticket:
```

### Filled example 1 — internal links to reduce click depth (entry #88)

```
Tactic / entry #:       Add internal links to reduce page click depth — #88
Mark and denominator:   [measured: MAINSTREAM, n=3 samples across 2 publishers, c=0 controlled]
                        +87% organic sessions (median), range +87% to +113%; all three sources
                        before/after with no control (linkvector.io 2024, 1 page; botify.com 2025,
                        1 site ×2). Direction only; the size belongs to those sites.

When it applies       — money pages (e.g. /comparar/* result templates) sit ≥3 clicks from the
                        home page in the crawl graph AND already have impressions in GSC.
Before you start      — export crawl depth per URL; capture 28 days of GSC clicks/impressions/
                        position per URL; split the deep money pages into treated and control
                        halves matched on baseline clicks and template.
What to change        — from 2–3 already-trafficked hub/guide pages, add in-body contextual
                        links with descriptive anchors to each TREATED page only.
What to keep          — titles, body copy, canonicals, schema, nav and footer unchanged on both
                        halves; no other release touching those templates in the window.
What to measure       — primary: organic clicks treated vs control, 28 days post vs 28 pre,
                        matched weekday span; secondary: average position; guardrail: lead
                        submissions from treated pages must not fall.
When to revert        — if treated clicks fall >15% relative to control over 4 consecutive weeks,
                        confirm mechanism (core update? seasonality? donor pages lost traffic?),
                        then remove the added links. Log the null or harm either way.
```

### Filled example 2 — title-tag test on a template

```
Tactic / entry #:       Rewrite title tag on the energy tariff result template
Mark and denominator:   see titles-and-serp-tests.md for the title family; the relevant AVOIDs
                        (#165 strip synonyms −27% sessions; #173 swap in high-volume variants
                        −20% sessions) rule out two of the obvious rewrites before you start.

When it applies       — the template has ≥ ~355 clicks per side per window when pooled
                        (power arithmetic: experiments-and-revert-2.md); Google shows OUR title on the
                        majority of sampled SERPs (check before, not after).
Before you start      — 28 days of GSC clicks, impressions, CTR, position per URL; randomise
                        URLs on the template into A (control) and B (treatment); record which
                        title Google actually shows for a sample of 20 queries per arm.
What to change        — the title pattern on arm B only; meta description untouched so the
                        read is about the title.
What to keep          — H1, body, schema, internal links, prices shown, canonical; no other
                        template release in the window.
What to measure       — primary: CTR at the arm level (clicks/impressions pooled per arm),
                        MDE 15% relative, 28-day window, two-proportion z-test; secondary:
                        position per arm (a title change can move position, not just CTR);
                        guardrail: lead rate per session on arm B.
When to revert        — arm B CTR below arm A past the pre-declared band with p<0.05, OR
                        Google rewrites the treated title on >50% of sampled queries (the test
                        is not being shown), OR the guardrail falls — confirm, then restore A.
```

