# Templates

## Contents

- A. BRIEF
- B. PROFILE-TEMPLATE
- C. Matrix row schema
- D. FEATURES columns
- E. TRUST columns
- F. TRAFFIC columns
- G. README skeleton
- H. SNAPSHOT skeleton

Replace `<…>` placeholders. Keep the section numbers stable so files stay grep-able across runs.

---

## A. `_method/BRIEF.md` (shared by every research agent)

```markdown
# <Subject> competition database — research brief

Run started <YYYY-MM-DD>. Owner: <role, e.g. founder>.

## What <Subject> is (so you know what "competitor" means)
<2–4 lines: what it does, positioning (e.g. neutral / non-intermediary), business model>
Verticals: <list with one-line scope each>

A competitor = any firm/site/app that <market> users use INSTEAD of <Subject> for comparing, choosing or
switching any of these products, or for the tools/content <Subject> offers. Include: <archetype list>.
EXCLUDE: <exclusion rule> — unless they are big/national.

## Output rules (folder: `<output folder>`)
1. One profile per firm at `competitors/<slug>.md` following `_method/PROFILE-TEMPLATE.md`.
   Slug = lowercase, hyphens. Check whether it exists first (Glob). If another cluster owns it, write
   `_supplements/<slug>--<your-cluster>.md` instead.
2. One vertical landscape at `verticals/<cluster>.md`.
3. Matrix rows: `matrices/rows-<cluster>.jsonl` (schema in templates §C). Use null when unknown — never invent.
4. Sources: `sources/sources-<cluster>.md` (URL | what it supports | accessed date).
5. Gaps: `gaps/gaps-<cluster>.md` (seen-not-profiled + why, blocked pages + error, unfilled dimensions, open questions).

## Evidence rules
- Tag every non-obvious fact `[src: URL, accessed <date>]` and `[verified]` / `[reported]` / `[inferred]`.
- Prefer primary sources: the firm's legal pages, regulator registers, company registries, review sites,
  app stores; traffic panels are estimates.
- Do NOT submit forms, create accounts, solve CAPTCHAs, or enter personal data. You may open public
  simulators and record what they ask BEFORE showing a result (that is the "gated" dimension).
- Do NOT use browser tools (one designated agent does). If a page blocks you, log it in gaps.
- Do the work yourself — do NOT spawn subagents. WebSearch is shared: at most <N> calls; prefer WebFetch.
- No secrets or personal data of private individuals in any file.

## Final message
Files written, firms profiled, the 5 most important findings for <Subject>, top gaps not closed.
```

---

## B. `_method/PROFILE-TEMPLATE.md`

```markdown
# <Firm> — competitor profile
`slug: <slug>` · `url: <url>` · `cluster owner: <cluster>` · `last verified: <date>`

## 0. One-paragraph verdict      what it is, why users use it, threat 1–5 and why
## 1. Identity & ownership       legal entity, registry id, HQ, founded, parent/investors, funding, staff, revenue (year)
## 2. Regulatory status          licences/registrations + category; what the status means for neutrality
## 3. Business model & money     who pays (commission, CPL/CPA, affiliate, ads, subscription, B2B); claims vs reality
## 4. Coverage                   table vertical | covered? | depth (counts, providers, tools) | notes — vs subject's verticals
## 5. User journey & UX          what is asked before results; ranked list vs callback; switching done?; app; advisors
## 6. Data & methodology         price source, freshness, whole-market vs panel, ranking method & sponsored disclosure
## 7. Content, SEO & audience    traffic (graded), top sections, sitemap size, tools, newsletter/video/social, press
## 8. Trust & reputation         complaint index, review sites, store ratings, awards, controversies/sanctions
## 9. Marketing & partnerships   campaigns, sponsorships, partners, white-label, affiliate programmes
## 10. Product & tech            notable features, launches (last 24 months), AI features, APIs
## 11. Strengths / weaknesses vs subject   where they win, where subject wins, copy / avoid
## 12. Threat & opportunity      score + reason, trend, partnership option, true and defensible attack angles
## 13. Sources                   numbered: URL — what it supports — accessed date
```

International benchmarks: sections 0, 1, 3, 4, 5, 7, 10, 11, 12, 13 at minimum, written to `international/`.

---

## C. Matrix row schema (`matrices/rows-<cluster>.jsonl`, one JSON object per line)

```
slug, name, url, country, type, archetype, verticals[], regulatory[], business_model, monetization[],
owner_group, founded, employees, revenue_eur, revenue_year, traffic_monthly_est, traffic_source,
trustpilot, complaint_index, app_rating, gated_results (bool|null), threat_to_subject (1–5),
threat_reason, last_verified (YYYY-MM-DD)
```
Validate after every write: every line must `json.loads`.

## D. FEATURES matrix columns (Y / N / P / ? / –)

```
group, slug, name, results_before_contact, whole_market, rank_total_cost, post_promo_total_contract,
bill_upload_ocr, switch_done_for_user, auto_switch, account_wallet, renewal_reminders, alerts,
ai_assistant, app, rewards_loyalty, human_advisors, eligibility_engine, source_date_per_product,
sponsored_disclosure, b2b_api, llm_app, evidence_note
```
The subject's row comes from the baseline file, never from marketing copy. Adapt capability columns to
the market, but keep "results before contact", "whole market" and "sponsored disclosure".

## E. TRUST columns

```
slug, name, role, complaint_category, complaint_index, complaint_label, resolution_pct, category_rank,
badges, review_score, review_count, review_note, google_rating, app_ios, app_android, awards,
controversies_sanctions, complaint_themes, evidence_file, last_verified
```

## F. TRAFFIC columns (with grade)

```
threat_rank, firm, slug, domain, visits_mo_best, range_low, range_high, grade (A–D), sources_used,
national_rank, rank_bucket_real_users, mom_change, app ratings…, social…, notes
```
Grades: A = audited / first-party; B = two independent estimates agree within ~25 %; C = one panel
estimate or calibrated rank; D = rank only / conflicting.

---

## G. `00-README.md` skeleton

1. Read in this order (snapshot → dashboard → threat ranking → subject baseline)
2. Folders table (one line per folder)
3. How the research ran (rounds and what each added)
4. Evidence conventions ([verified]/[reported]/[inferred], `[corrected …]`, estimates, legal drafts)
5. Known limits (quotas, blocks, unsampled areas) + "no forms, accounts, CAPTCHAs, personal data"

## H. `01-LANDSCAPE-SNAPSHOT.md` skeleton

1. **The picture in ten lines** — structural truth, top threats, regulators/state tools, trust default,
   search & AI visibility (with traffic comparison), substitutes/bundles, likely consolidator/entrant,
   subject's unique ground, subject's self-inflicted problems.
2. **Top-15 threats** table (# | firm | threat | where | one-line why).
3. **Per vertical** table (leaders | open ground for the subject).
4. **Decisions for the owner** (numbered, yes/no phrasing) + register facts verified.
5. **Confidence and what is still open** + saturation line (per-round yield, verdict, monitoring cadence).
