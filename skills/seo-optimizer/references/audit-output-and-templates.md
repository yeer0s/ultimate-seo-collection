# Tools & Output Templates — Reference
<!-- split-header-2: part 1 of 2 of audit-output-and-templates.md (original lines 1–417; boundary start) -->
<!-- /split-header-2 -->

## Contents

- Tool stack — by purpose
- Output templates
- Prioritisation

Other parts of the same original file: [audit-output-and-templates-2.md](audit-output-and-templates-2.md).

## Tool stack — by purpose

Open-source tools (crawlers, Lighthouse and Lighthouse CI, robots/sitemap parsers, link checkers, schema typing, framework SEO packages) are no longer listed here; see skill `seo-strategy` › resources-catalogue-2 (tools by job, with licence, method and trap per row). The rows below are hosted, free-of-charge platform tools and commercial products.

### Free / essential

| Tool | Purpose |
|------|---------|
| Google Search Console | Queries, clicks, impressions, indexing, technical issues — **day-zero install** |
| Bing Webmaster Tools | Bing/Copilot visibility, crawl/index diagnostics |
| PageSpeed Insights (pagespeed.web.dev) | Performance + Core Web Vitals (lab + field) |
| CrUX (Chrome UX Report) | Real-user performance data |
| Google Rich Results Test | Validate structured data eligibility for rich results |
| Schema Markup Validator (validator.schema.org) | Generic schema syntax validation |
| Google Analytics 4 | User behavior, conversions, traffic sources |
| Looker Studio | Custom SEO dashboards (free, integrates with GSC + GA4) |
| Chrome DevTools | Technical debugging, rendered HTML inspection |
| robots.txt report (Search Console) | Crawl rule validation. *The old standalone "robots.txt Tester" is retired — the report is its replacement* |
| XML sitemap validators | Sitemap correctness |
| Google Trends | Demand seasonality and trends |
| Google Business Profile | Local SEO base |
| Google URL Inspection (in GSC) | See what Googlebot rendered |

### Professional (paid)

| Tool | Best use |
|------|----------|
| Ahrefs | Backlinks, competitor research, content gaps, keyword volume + difficulty |
| Semrush | Keyword research, competitor analysis, PPC/SEO overlap, position tracking |
| Screaming Frog SEO Spider | Technical crawling and page-level audits (free up to 500 URLs) |
| Sitebulb | Visual technical SEO audits with prioritization |
| Lumar / Deepcrawl | Enterprise crawling at scale |
| Botify | Enterprise crawl + log-file analysis |
| Oncrawl | Log + crawl analysis, JS rendering at scale |
| SurferSEO / Clearscope / Frase | Content optimization scoring against top-ranking pages |
| AlsoAsked | People Also Ask mapping (visualizes question chains) |
| AnswerThePublic | Question discovery from autocomplete data |
| SEOTesting.com | SEO experiments (test changes against control) |
| AccuRanker / SE Ranking | Daily rank tracking |
| Little Warden / Conductor Website Monitoring | Real-time SEO monitoring (alerts on critical changes). *ContentKing was acquired by Conductor and no longer sells standalone* |
| Sitechecker / Screpy | Lightweight ongoing audits |

### Performance / technical

| Tool | Purpose |
|------|---------|
| WebPageTest | Deep speed diagnostics, waterfalls, video |
| GTmetrix | Performance summaries (less Google-aligned than PSI) |
| Cloudflare Analytics | CDN + performance data |
| New Relic / Datadog | Server/app performance monitoring |
| Log file analyzers (Screaming Frog, Botify, Oncrawl) | Bot crawl behavior |

### AI / search visibility

| Tool type | Examples |
|-----------|----------|
| LLM citation tracking | Profound, Otterly, Peec AI, AthenaHQ (category churns fast — verify the vendor still trades before quoting it) |
| Brand mention monitoring | Brand24, Mention |
| Entity audit | Kalicube, Wordlift |
| SERP feature trackers | Semrush sensor, AccuRanker SERP features |
| Vector / RAG retrievability | Custom (test your content with embedding queries) |

### Implementation

| Tool | Purpose |
|------|---------|
| Rank Math / Yoast / SEOPress | WordPress SEO (metadata, schema, sitemaps) |
| Headless CMS (Sanity, Contentful, Strapi, Payload) | Structured SEO fields |
| GitHub | Version control, code review |
| Cloudflare | CDN, redirects, page rules, edge caching |
| Vercel / Netlify | Modern deploy with SSR/ISR |
| Google Tag Manager | Tracking deployment without code |
| BigQuery | GSC + GA4 data warehouse for advanced analysis |
| n8n / Zapier / Make | Workflow automation (sitemap pings, alert routing) |
| IndexNow | Fast URL submission to Bing + participating engines |

## Output templates

### 1. SEO recommendation template

```
**Recommendation:** [What to do, in one sentence]
**Priority:** P0 / P1 / P2 / P3
**Impact:** High / Medium / Low — [why]
**Effort:** Hours / Days / Weeks
**Affected URLs:** [list or pattern]
**Reason:** [why this matters, in 2-3 sentences]
**Implementation steps:**
1.
2.
3.
**Validation:** [how to confirm it worked — e.g. "Rich Results Test passes; GSC shows enhancement type X"]
**Risks:** [what could go wrong]
**Owner:** [who]
```

### 2. SEO audit table

| Issue | URL(s) | Impact | Effort | Priority | Fix | Validation |
|-------|--------|--------|--------|----------|-----|------------|

A pre-launch audit of one route opens at most 3 subskill rows, picked from: TE1 crawl/index, TE2 rendering/sitemaps, TE3 schema, CO2 intent, CO4 comparison and EU legal gates, CO7 publishing gates, AI2 AI crawlers, google-ai (point 7b). Live-site inspection and deploy-drift gates are post-launch work.

**The audit's output format: verdict line, then the 8-point scorecard, always all 8 rows** (points as in the router's 8-point table):

| # | Point | Status | Evidence | Label |
|---|---|---|---|---|
| 1–8 | one row per point | PRESENT / PARTIAL / MISSING, or NOT INSPECTED | `file:line` (or URL + what it returned); NOT INSPECTED names the file or URL to open | one of the 9 labels |

- With no repo or URL access every row is NOT INSPECTED and the total is `INSUFFICIENT DATA (0/8)`; the scorecard is still printed, so the reader sees the eight checks and where each one is read. `[unvalidated house heuristic]`
- Point 7b row: the GSC "Search generative AI" control is effectively include — set on the property, or "Inherit control from parent" (the default for a child property) with the parent on include — a per-property control over Google's Search generative AI features (AI Overviews, AI Mode, generative AI features in Discover), not a ranking or inclusion signal for other parts of Search, not a training control `[documented: https://support.google.com/webmasters/answer/16908024, 2026-10-14]`.
- Every action bullet under the scorecard carries its own label; an unlabelled tactic is a defect in the report.

### 3. Content brief table

| Field | Recommendation |
|-------|----------------|
| Primary keyword | |
| Search volume | |
| Difficulty | |
| Intent | |
| Page type | |
| Funnel stage | |
| SERP format Google rewards | |
| AI Overview present? | |
| Required sections (H2s) | |
| Unique angle | |
| Internal links (source → target → anchor) | |
| External sources | |
| Schema type | |
| CTA | |
| Word count | |
| Author / reviewer | |

### 4. Title + meta rewrite table

| URL | Current title | New title | Current meta | New meta | Reason |
|-----|---------------|-----------|--------------|----------|--------|

### 5. Internal linking map

| Source page | Target page | Anchor text | Placement (paragraph) | Reason |
|-------------|-------------|-------------|----------------------|--------|

### 6. Redirect map (for migrations)

| Old URL | New URL | Status | Type (301/302) | Reason |
|---------|---------|--------|----------------|--------|

### 7. Developer ticket (for technical fixes)

```
**Title:** [Short imperative — "Fix canonical tags on provider comparison pages"]

**Problem:**
[1-2 paragraphs on what's wrong, with file:line evidence]

**SEO impact:**
[Why this matters for rankings/crawl/user experience]

**Implementation:**
- [Specific change 1]
- [Specific change 2]
- [Specific change 3]

**Acceptance criteria:**
- [ ] [Verifiable change 1]
- [ ] [Verifiable change 2]
- [ ] [Verifiable change 3]

**Validation:**
- [How to test — e.g. "Rich Results Test passes for /pricing/"]

**Out of scope:**
- [What this ticket explicitly does NOT cover]
```

### 8. Pillar + cluster map

```
Pillar: [Topic]
URL: /[pillar-slug]/
Primary keyword:
Supporting clusters:

| Cluster topic | URL | Primary keyword | Intent | Status |
|---------------|-----|-----------------|--------|--------|
| | | | | new / draft / live / refresh-needed |

Lateral links between clusters:
- [Cluster A] ↔ [Cluster B] — [why]
- [Cluster C] ↔ [Comparison page X] — [why]
```

### 9. Programmatic SEO template spec

```
Template name:
URL pattern: /[segment-1]/[segment-2]/
Data source:
Quality threshold (minimum data required to publish):
Page sections:
1. [Section] — generated from [data field]
2. ...
Title template (with rotation):
Meta description template:
Schema type:
Internal linking rules:
- Link from this page to: [related templates]
- Pages that should link to this template:
Sitemap inclusion criteria:
Update cadence:
Human QA cadence:
Sample URLs (5-10 to spot-check before scaling):
```

### 10. SEO reporting dashboard structure

Build dashboards at multiple levels:

**Visibility tier:**
- Total impressions (GSC) — trend, by query group
- Average position — trend, by page group
- SERP features captured — featured snippets, PAA, AI Overview citations

**Traffic tier:**
- Organic clicks — trend, by page group, by query group
- Organic sessions (GA4) — trend, source/medium = google/organic
- Click-through rate — by query, by page

**Quality tier:**
- Engagement rate (GA4)
- Average engagement time
- Pages per session
- Scroll depth (custom event)

**Conversion tier:**
- Conversions by source (GA4 events)
- Lead value by page (if attributable)
- Conversion rate by intent type

**Technical tier:**
- Indexed pages (GSC Coverage report)
- Crawl errors / warnings
- Core Web Vitals — LCP / INP / CLS distribution

**Authority tier:**
- Referring domains (Ahrefs/Semrush) — net new per month
- Brand mentions — branded vs unbranded queries trend

**Local tier (if applicable):**
- Google Business Profile actions (calls, directions, website clicks)
- Local pack appearances

**AI visibility tier:**
- Manual checks of target queries on AI Overviews / Perplexity / Copilot — citation rate

### 11. Search Console opportunity report

Run weekly. Every Logic number is an `[unvalidated house heuristic]` trigger for **diagnosis**, not action: compare CTR with this site's CTR at the same position, check the click floor (skill `seo-evidence` › experiments-and-revert-2), and never noindex or remove on a threshold alone.

| Opportunity | Logic | Action |
|-------------|-------|--------|
| High impressions, low CTR | CTR <2% on query with >1000 impressions/month | Rewrite title + meta |
| Average position 4-10 | Rankings just below page 1 fold | Improve content depth + internal links |
| Average position 11-20 | Page 2 — close to breakthrough | Add missing sections, schema, links |
| Declining clicks | -20% week-over-week sustained | Refresh workflow |
| Queries without dedicated page | Query traffic to a partial-match page | Create dedicated page |
| Pages with many queries | One page ranks for 50+ queries | Expand into a cluster |
| Cannibalization | 2+ pages ranking for same query | Merge or differentiate |
| Indexed but no traffic | Pages with 0 impressions for 3+ months | Confirm it is indexed (URL Inspection), then decide: improve, noindex, or remove |

### 12. Pre-publish QA checklist (every new page)

- [ ] **Intent** — page format matches what the SERP rewards for the target query
- [ ] **Title** — concise and descriptive, primary keyword early, includes differentiator. ~60 chars is an optional `[unvalidated house heuristic]` target, not a fail line: Google sets no title length limit and truncates "as needed, typically to fit the device width" `[documented: https://developers.google.com/search/docs/appearance/title-link, 2026-10-12]`
- [ ] **Meta description** — short, value + specifics, no clickbait. ~160 chars is an optional `[unvalidated house heuristic]` target: "There's no limit on how long a meta description can be" `[documented: https://developers.google.com/search/docs/appearance/snippet, 2026-10-12]`
- [ ] **H1** — single, page-topic
- [ ] **H2/H3** — hierarchical, descriptive, keyword-aware without stuffing
- [ ] **Quick answer block** near top of page
- [ ] **Original insight or data** present
- [ ] **Internal links** — ≥3 to related pages with descriptive anchors (a floor against orphaning, `[unvalidated house heuristic]`)
- [ ] **External citations** — to authoritative sources where claims are made
- [ ] **Schema** — appropriate type; no syntax errors in a schema testing tool such as Schema Markup Validator; Rich Results Test only for features it supports (e.g. "Site names aren't supported in the Rich Results Test") `[documented: https://developers.google.com/search/docs/appearance/site-names, 2026-10-12]`
- [ ] **Canonical** — self-referencing or correctly pointing to canonical
- [ ] **Hreflang** (if multilingual) — reciprocal alternates
- [ ] **Image alt text** — descriptive, not "image1.jpg"
- [ ] **Sitemap** — included only if it is an indexable canonical URL: "All pages listed in a sitemap are suggested as canonicals" `[documented: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls, 2026-10-14]`, and a sitemap listing `noindex` URLs is a named cause of error spikes `[documented: https://support.google.com/webmasters/answer/7440203, 2026-10-14]`
- [ ] **CTA** — matched to funnel stage
- [ ] **Author** — byline + bio for E-E-A-T
- [ ] **Last updated date** visible
- [ ] **CWV proxy (lab)** — Lighthouse LCP ≤2.5s, CLS ≤0.1, and **TBT ≤200ms** as the stand-in for INP. A Lighthouse *navigation* run never interacts with the page, so it cannot measure INP at all; TBT is the accepted lab proxy. (For a real INP number you need a timespan/user-flow run or field data.) Before launch a URL has no field data, so lab is the only thing tickable pre-publish. Smoke test, not a verdict. After launch, check CrUX rather than assume absence: the 28-day `collectionPeriod` is the aggregation window, and a page launched less than 28 days ago can already have data `[documented: https://developer.chrome.com/docs/crux/api, 2026-10-12]`.
- [ ] **Diarise the real CWV read** — re-check against **CrUX field data** ~4 weeks post-launch. That, not the lab run, is what Google acts on. **If the URL never gains URL-level CrUX eligibility** (a page needs "a minimum number of visitors", not disclosed `[documented: https://developer.chrome.com/docs/crux/methodology, 2026-10-14]`), fall back in this order: **origin-level CrUX** for the site as a whole, then your own RUM (`web-vitals` in the browser, reporting real user values). A URL that will never have field data should be marked `no_field_data` and judged at origin level — don't leave the item permanently unticked
- [ ] **Mobile** — renders correctly, no horizontal scroll
- [ ] **Indexability** — `index,follow` (or `noindex` deliberately)
- [ ] **Submit indexing** — GSC URL Inspection for Google; IndexNow ping for **Bing** and participating engines (Google does not consume IndexNow — these are two separate submissions, not one step)

### 13. Migration QA checklist (URL changes)

- [ ] Old URLs 301 to their equivalent new URLs (no chains); no equivalent → explicit decision (nearest parent, 410 or keep)
- [ ] No 404s on previously indexed URLs
- [ ] Sitemap updated to new URLs
- [ ] Internal links updated to new URLs (no internal redirects)
- [ ] External backlinks audited — outreach to update high-value ones
- [ ] Canonical tags point to new URLs
- [ ] Hreflang updated to new URLs
- [ ] Search Console — submit new sitemap; verify property if domain changed
- [ ] Bing Webmaster — same
- [ ] Monitor for 30/60/90 days — rankings recovery, crawl errors, traffic restoration

Templates 14 (AI search visibility check) and 15 (methodology page): [audit-output-and-templates-2.md](audit-output-and-templates-2.md).

## Prioritisation

Three layers, applied in this order: run the gate order to find which lane is allowed to act, file each action under its one lane, then score the actions that survive with the formula.

### Gate order — run before proposing any edit `[practitioner]`

Check the gates top to bottom. The first gate that fails is where the work is; actions belonging to later lanes are parked until it passes.

| # | Gate | Question | If it fails |
|---|---|---|---|
| 1 | Eligibility | Can the engine fetch, render and index the URL? | Lane 1 work only |
| 2 | Intent | Is the query worth winning, and is this the page that should own it? | Settle query→page ownership first |
| 3 | Page fit | Does the page actually satisfy that intent? | Improve, merge or reroute the page; leave metadata alone until then |
| 4 | SERP fit | What does the live results page reward (format, AI Overview, local pack, zero-click)? | Stop here until answered |
| 5 | Business value | Which conversion does this move? | Stop here until answered |
| 6 | Risk | Does it touch redirects, canonicals, production templates or claims? | Human approval before shipping |
| 7 | Measurement | Are baseline, metric, window and a revert trigger declared in advance? | Do not ship yet — see skill `seo-evidence` › experiments-and-revert-2 |

### Improvement lanes — one primary lane per action `[practitioner]`

Every recommendation sits in exactly one primary lane. It may mention secondary lanes, but only the primary lane decides where it ranks.

| # | Lane | Covers | Commonly confused with |
|---|---|---|---|
| 1 | Eligibility & indexability | Crawl, render, canonical, index | Content quality — content work is premature while the page cannot be reliably fetched and indexed |
| 2 | Demand & intent | Which query is worth winning; which single page owns it | SERP packaging — choose the query/page pair first |
| 3 | Content usefulness & trust | Does the job the searcher came for; first-hand proof; sourced YMYL claims | Metadata — no title rescues a page that misses the intent |
| 4 | On-page relevance & SERP packaging | Title, H1, meta description, answer block, anchors, valid schema | Demand selection |
| 5 | Page experience | CWV field data, HTTPS, mobile, interstitials, correct images | Ranking magic — good CWV does not save weak intent or content |
| 6 | Authority & distribution | Earned links, mentions, internal link equity; local presence for local businesses | Manipulation — the SKILL.md hard refusals apply |
| 7 | Measurement & experiment | Baseline, holdout, revert rule | Dashboards — measurement exists to pick and validate actions |

### Scoring formula

```
Priority = (SEO impact × business value × confidence) / implementation difficulty
```

Examples:
| Issue | Impact | Business value | Confidence | Difficulty | Priority |
|-------|--------|----------------|------------|------------|----------|
| Money pages noindexed | 10 | 10 | 10 | 1 | 1000 (critical) |
| Broken canonical on top page | 8 | 9 | 9 | 2 | 324 (high) |
| Sitemap full of non-indexable URLs | 5 | 5 | 9 | 2 | 113 (high) |
| Slow LCP on top landing page | 7 | 8 | 7 | 5 | 78 (medium) |
| Missing meta on low-value page | 2 | 2 | 9 | 1 | 36 (low) |
| Duplicate H1 on minor blog post | 1 | 1 | 9 | 1 | 9 (defer) |

Don't ship recommendations without scoring them — it forces honest priority.

