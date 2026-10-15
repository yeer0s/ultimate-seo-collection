# Agent prompt templates

Every prompt starts with the same three lines (the "preamble"), then the phase-specific job.

**Preamble (paste first):**
> You are a competitive-intelligence researcher building <Subject>'s competitor database. Cluster: `<name>`.
> Do the work yourself — do NOT spawn subagents or background tasks, and do not hand back until every file below is written.
> FIRST read completely: `<folder>/_method/BRIEF.md` (rules — follow exactly), `PROFILE-TEMPLATE.md`, `OWNERSHIP.md`, `PRIOR-KNOWLEDGE.md` (build on it, re-verify, don't copy). WebSearch cap: <N> calls; prefer WebFetch on known URLs, sitemaps, registers. No browser tools.

---

## P2 — Cluster discovery
> Job: identify every significant <market> player users use to compare/choose <cluster scope>. Candidate list to start from (search hard beyond it): <names>. Full-template profiles for the ones that matter (aim <n>). For each: legal entity + registry id + revenue/employees, licences, coverage depth (count product pages via sitemap.xml), gated or not, monetisation, reviews/complaint index, traffic, marketing, partners, launches in the last 24 months, AI features.
> Also `verticals/<cluster>.md`: market structure (regulator statistics), who leads, coverage table vs <Subject>'s <counts>, white space, threats, regulatory constraints that matter for <Subject>'s positioning.
> Write `matrices/rows-<cluster>.jsonl`, `sources/sources-<cluster>.md`, `gaps/gaps-<cluster>.md`. Final reply per brief.

Standard clusters: horizontal multi-vertical · one per regulated vertical group · content/tools/creators · state tools + consumer associations · mobility/home/other · platforms, bundles & AI substitutes · international benchmarks (split into 2–4 regional batches).

## P3 — Subject baseline (no web)
> Read the subject's live code/product (read-only) and internal notes. Write `dimensions/<subject>-baseline.md`: per vertical — what is live, product/provider counts (say which file and how counted), data source & freshness, gated?, switching?, lead/affiliate paths, account/alerts, AI. Answer these specific questions with file:line evidence: <questions raised by cluster agents>. End with a capability matrix (same columns as FEATURES). Tag `[verified-in-code path:line]` vs `[from-notes]`.

## P4a — Gap-close
> Read `gaps/gaps-<clusters>.md`. Close these items: <grouped list>. Profile only if real reach; otherwise a gaps line with the reason. Write `rows-r<k>-<name>.jsonl`, sources, gaps. Final reply per brief.

## P4b — Fact-check
> For each claim below: find the primary source, quote the decisive sentence (≤25 words), grade CONFIRMED / CORRECTED (give the right fact) / UNVERIFIABLE (say what blocked you). Claims: <numbered list of hot claims from agent reports>. Write `dimensions/fact-check-r<k>.md` (# | claim | verdict | URL | quote | note) and list every file:line that must change. Do not edit other files.

## P5 — Dimension analysts (two in parallel)
> A: regulation & business models (per-firm licence/who-pays/claims-vs-reality table; archetype map; legal perimeter for the subject, drafts for counsel; unit economics) + features/UX matrix (subject row from baseline) + `matrices/FEATURES-firm-x-capability.csv`.
> B: trust & reputation + `matrices/TRUST.csv`; ownership/M&A/entry (ownership map, deal multiples, entrants with labelled probabilities, partnership candidates); threat ranking top-30 resolving cluster disagreements, white-space map per vertical, 10 true & defensible positioning lines with conditions, 10 risks incl. self-inflicted ones.
> Mostly local files; web only to fill named holes (cap <N>).

## P6 — Browser verifier (the only agent with the browser)
> Load the browser tools; create your own tab and close it at the end. Never sign in, submit personal data, click ads, accept non-essential cookies, or solve CAPTCHAs. Typing a registration number or company name into a public register search box is allowed. Pace a few seconds per action.
> A. Regulator registers: verify number, name, category, status for <list>. B. Pages that blocked fetchers: <list> — record only what is asked before results. C. Brand visibility on a second search engine.
> Write `dimensions/browser-verification.md` (claimed | register value | verdict | URL | date) + list of files to fix; blocks → gaps.

## P6b — Database editor (no web)
> Apply the verified corrections from <files> surgically: `~~old~~ → new [corrected <date>: <source>]`; grep the whole folder for each wrong value; keep jsonl valid; write `_method/CHANGELOG-corrections.md` (file | old | new | source).

## P7a — Saturation sweep
> Prove nothing significant is missing. Sweep DIRECTORIES (industry associations, startup portfolios, app-store searches, "alternative to <leader>" queries, last-24-month press). For each new name: profile if real reach or funded; else a gaps line. Write `gaps/SATURATION-VERDICT.md`: directories swept, names checked/added/rejected, verdict + residual risk.

## P7b — SERP sweep (browser)
> Run ≤35 queries per session on <engine + locale params>, 20–30 s apart; stop for good on a CAPTCHA. Per query: ads, organic top-10, AI-answer presence + cited sites, subject position. Cross-check top-5 domains against known slugs; profile any unknown domain in top-5 for ≥2 queries or #1 once. Write `dimensions/search-visibility-r<k>.md` (method, per-query table, share of voice, AI-answer analysis, paid landscape, subject visibility, implications) + `matrices/serp-raw-r<k>.csv` (query, vertical, kind, position, domain, title).

## P9 — Synthesis (you)
Merge (`scripts/merge_rows.py <folder> [--subject <name>]`), build dashboard (`scripts/build_dashboard.py <folder> --title "<Subject> competition landscape"`), validate the dashboard JS (`node --check`), write README + snapshot, copy the clean pack to the output location.
