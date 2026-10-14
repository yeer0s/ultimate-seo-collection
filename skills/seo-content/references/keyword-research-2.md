<!-- split-header: part 2 of 2 of keyword-research.md (step-3 original lines 307–477; boundary H2) -->
# Keyword research (2 of 2) — categorise, validate, prioritise, map, Mowei playbook, validation stack
## Contents

- Step 4 — Categorize into the keyword universe
- Step 5 — Validate with paid tools (optional)
- Step 6 — Prioritize the keyword universe
- Step 7 — Map to page types
- Mowei-specific keyword research playbook
- Cadence
- Output: keyword universe spreadsheet
- Validation stack — operational details

Other parts of the same original file: [keyword-research-1.md](keyword-research-1.md).

<!-- /split-header -->
## Step 4 — Categorize into the keyword universe

Take your raw discoveries and slot each into the intent matrix from [content-and-intent.md](content-and-intent.md):

| Type | Example | Page that captures it |
|------|---------|----------------------|
| Head term | "comparar luz" | Pillar |
| Long-tail | "melhor tarifa luz bi-horária 200kwh" | Cluster article |
| Pain-point | "porque é a fatura da luz tão alta" | Problem-aware article |
| Comparison | "edp vs galp" | Versus page |
| Alternative | "alternativa à edp" | Alternative page |
| Local | "fornecedor luz algarve" | Local landing |
| Regulatory | "tarifa erse 2026" | Glossary/explainer |
| Transactional | "mudar fornecedor luz online" | Lead/conversion page |
| Calculator | "simulador conta luz" | Tool page |
| Review | "goldenergy opiniões" | Review/reputation page |
| Objection | "é seguro mudar fornecedor luz" | Trust/FAQ page |

A keyword without a slot is either irrelevant or you're missing a page type.

## Step 5 — Validate with paid tools (optional)

If first-party + free signals give you 80% of what you need, skip paid tools. Most pre-launch sites overpay for keyword tools that don't change the recommendations.

Validate paid only when:
- You need volume confirmation for a 50+ keyword shortlist
- You need backlink/competitor gap data (only paid tools have this)
- You're optimizing an established site and need difficulty scores

### Ahrefs (gold standard for backlinks)

- **Site Explorer** — competitor's organic pages, keywords, backlinks
- **Keyword Explorer** — volume, difficulty, parent topic, traffic potential
- **Content Gap** — find keywords competitors rank for that you don't
- **Site Audit** — technical issues across 170+ checks

Cost: Lite tier ~$129/month (verify current pricing before quoting it). **There is no trial** — Ahrefs discontinued paid trials. Free **Ahrefs Webmaster Tools** covers your own verified domains only, not competitors'.

### Semrush (gold standard for keyword research)

- **Keyword Magic Tool** — broader Portuguese-market data than Ahrefs typically
- **Position Tracking** — daily rank tracking
- **Topic Research** — cluster suggestions
- **Domain Overview** — competitor organic + paid traffic estimates

Cost: ~€120/month. Free tier limited (10 queries/day).

### DataForSEO (programmatic, cheaper at scale)

API access to keyword volume, SERP data, PAA, autocomplete, backlinks.

Cost: pay-per-call, typically €30-50/month for moderate use. Best for backend integration.

```python
# DataForSEO keyword volume + difficulty
import requests, base64
auth = base64.b64encode(b'login:password').decode()
r = requests.post(
    'https://api.dataforseo.com/v3/keywords_data/google/search_volume/live',
    headers={'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'},
    json=[{
        'keywords': ['comparar luz', 'edp vs galp', 'simulador conta luz'],
        'location_code': 2620,  # Portugal
        'language_code': 'pt'
    }]
)
```

### Getting competitor data without a subscription

**Do not recommend trial-cycling** — signing up for a trial intending to cancel before billing, then repeating it each cycle. It is ToS-hostile, it is the same *low-effort + systematized + scaled* shape the Shortcut Trap rule in SKILL.md tells you to refuse, and advising it in a skill that carries a Hard-Refusals section is incoherent. (It is also moot: Ahrefs no longer offers a paid trial at all — verify current terms before quoting any trial.)

The legitimate no-subscription ladder, cheapest first:

1. **GSC + Bing Webmaster Tools** — free, first-party, and better than any third-party estimate for a site with history. Always exhaust these first.
2. **Competitor sitemap mining** (above) — free, and tells you what they *published*, which is often more useful than what they rank for.
3. **Ahrefs Webmaster Tools** — free for domains you can verify. Your own backlinks and keywords only, not competitors'.
4. **Semrush free tier** — ~10 queries/day. Enough to spot-check a handful of competitor terms, not to build a universe.
5. **DataForSEO** — pay-as-you-go, cents per query, no subscription. The honest way to buy absolute volumes and competitor SERP data at small scale.
6. **One paid month, used properly** — if you genuinely need Ahrefs/Semrush depth, buy a month, do the export, cancel. Paying for what you use is not trial-gaming; the distinction is whether you paid for the value you took.

Don't carry a monthly subscription until SEO is producing leads worth more than the tool cost.

## Step 6 — Prioritize the keyword universe

Score every keyword in your universe:

```
Priority = (search volume × commercial value × ranking probability) ÷ effort
```

| Factor | How to estimate |
|--------|-----------------|
| Search volume | GSC impressions (best), Bing keyword tool, paid tool |
| Commercial value | Maps to revenue: transactional > commercial > informational |
| Ranking probability | Domain authority vs SERP competitors; long-tail = higher probability |
| Effort | Content production cost: long-tail article < pillar page < interactive tool |

Skip keywords where:
- Volume × commercial value is low (vanity)
- Ranking probability is near zero (Wikipedia-dominated SERP)
- Wrong geography or wrong intent for your funnel
- Regulatory or legal risk

A 100-volume long-tail with high commercial intent and low competition beats a 10000-volume head term where you can't realistically rank.

## Step 7 — Map to page types

Each prioritized keyword maps to a page type. From the keyword universe → content production roadmap.

| Keyword | Intent | Page type | Status | Owner | Target date |
|---------|--------|-----------|--------|-------|-------------|
| comparar luz | Commercial | Pillar (existing) | Refresh | Claude | Wk 1 |
| edp vs galp | Comparison | Versus page | New | Claude | Wk 2 |
| melhor tarifa luz algarve | Local commercial | Local pSEO | New (template) | Claude | Wk 3 |
| simulador conta luz | Tool | Calculator | Existing | — | Done |
| porque é a fatura da luz tão alta | Pain-point | Problem-aware article | New | Editorial | Wk 4 |

This roadmap is the bridge from keyword research to content production.

## Mowei-specific keyword research playbook

For the Portugal-energy-comparison case, run this sequence:

1. **Verify GSC + Bing** for `mowei.pt` — first audit point 7. Wait 30-60 days for data.
2. **Mine competitor sitemaps:** `comparaja.pt`, `doutorfinancas.pt`, `kuantokusta.pt`, `selectra.pt`. Build competitor keyword gap matrix.
3. **Autocomplete expansion** for seeds: `comparar luz`, `tarifa luz`, `melhor seguro auto`, `crédito habitação`, `IRS 2026`, `apoio social`.
4. **Reddit mining:** r/portugal + r/financasportugal + r/Lisboa for recurring questions per vertical.
5. **Regulator entity sweep:** ERSE, Banco de Portugal, ASF, ANACOM, DGEG glossaries → glossary page candidates.
6. **Categorize** into the intent universe per vertical.
7. **Prioritize** by (volume × commercial value × probability) ÷ effort.
8. **Map to page types:** focus on versus pages (energy + insurance + telecom), local pages (Algarve / Lisboa / Porto / Norte), tool pages (calculators), problem-aware articles.

This produces the content production roadmap that feeds directly into the programmatic-SEO build — see [programmatic-seo.md](programmatic-seo.md).

## Cadence

| Activity | Frequency |
|----------|-----------|
| GSC mining (4 reports) | Monthly |
| Competitor sitemap diff | Quarterly |
| Autocomplete refresh | Quarterly |
| Reddit/forum mining | When entering new vertical |
| Regulator entity sweep | When entering new vertical |
| Paid-tool deep dive | Annually (one paid month, or DataForSEO per-query) |
| AI Overview / Copilot citation check | Monthly (manual, top 30 commercial queries) |

## Output: keyword universe spreadsheet

The deliverable from a keyword research session:

Every volume cell carries **its tool, its date and its geo** — a bare number in a spreadsheet gets copied forward for years and nobody can tell whether it was measured, estimated, or invented. Leave it blank rather than guess; `—` is information, a made-up `~2400` is not.

| Keyword | Source | Volume (tool · date · geo) | Intent type | Page type | Existing page? | Priority | Notes |
|---------|--------|---------------|-------------|-----------|----------------|----------|-------|
| edp vs galp | Competitor sitemap + autocomplete | *[e.g. DataForSEO · 2026-08 · PT]* | Comparison | Versus | No | P0 | Main competitor has it; high commercial intent |
| simulador luz | GSC + autocomplete | *[GSC impressions · trailing 90d · PT]* | Tool | Calculator | Yes (`/ferramentas/simulador-luz`) | Refresh | Update with 2026 ERSE data |

Hand this to the content team or feed into the pSEO generator template.

## Validation stack — operational details

Moved from SKILL.md 2026-09-22 (content unchanged); the core keeps the four-tier order and the two traps, this section keeps the runnable specifics.

- **GSC tooling pattern:** a small OAuth script (`searchconsole v1`, `searchanalytics.query`, dims `query`/`page`, 90-day window). The query dimension can expose only a small share of impressions — on one site query rows carried ~15% (3,131 of 20,500); the rest were simply not returned as query rows — so check coverage per extraction and run the analysis page-led. Ordering heuristic for buried-but-shown rows: `impressions × (0.06 − CTR)` `[unvalidated house heuristic]` (site-specific; estimate attainable CTR by position, device and SERP layout before trusting it). Full procedure: [gsc-page2-audit.md](gsc-page2-audit.md). If an SEO/analytics MCP is connected (Ahrefs, Similarweb, Supermetrics, Amplitude), pull rank/traffic context from it after GSC, not instead of it.
- **Bing Webmaster Tools API:** `ssl.bing.com/webmaster/api.svc/json/GetQueryStats|GetPageStats|GetRankAndTrafficStats?apikey=`. Bing routinely surfaces a *different* winning cluster than Google (seen in the wild: fiscal/deadline + reference pages ranking Bing p1 while ~invisible on Google). Treat cross-engine divergence as signal, not noise.
- **Google Trends via `pytrends`:** geo-targeted, 12-month window, max 5 terms per query normalised within a batch → include one stable **anchor term in every batch and rescale** for cross-batch comparability. Gives *relative* demand plus **seasonality** (publish ahead of the peak). Gotchas: don't pass `retries=`/`backoff_factor=` to `TrendReq` (urllib3 `method_whitelist` crash); Google 429-throttles aggressive runs — space batches and write results incrementally so a mid-run throttle doesn't lose everything. Trends can read zero on genuinely low-volume terms (material in Portugal) — zero is not proof of no demand.
- **Head-term aggregation trap:** a head term showing decent cumulative GSC impressions can measure ~0 in Trends because the impressions came from many micro-variants at page 4-5, not head-term demand. Distinguish exact-query rows from page aggregates and cross-check the head term in Trends before building a head-term page.
- **Geo/language example:** `como ficar rico` is a Brazilian SERP owned by BR financial giants on BR volume; near-zero in Portugal. Ranking there is both unwinnable (domain authority) and useless (wrong-country traffic). Verify the term has demand *in the target geo* before committing.
- **Absolute volume:** Google Keyword Planner — account creation without a campaign is documented; card-on-file friction may still apply, so verify at signup and flag it up front. Alternative without a Google Ads account: **DataForSEO** (needs its own DataForSEO account and API login/password — see the Basic-auth example above; pay-as-you-go cents/query, numbers it says come from Keyword Planner `[vendor]`). Reserve Ahrefs/Semrush for backlink/SERP-difficulty depth, not basic volume.
