# Keyword Research — Reference
<!-- split-header: part 1 of 2 of keyword-research.md (step-3 original lines 1–306; boundary start) -->
<!-- /split-header -->

## Contents

- Order of operations
- Step 1 — Google Search Console mining (your highest-ROI source)
- Step 2 — Bing Webmaster Tools
- Step 3 — Free public sources

Other parts of the same original file: [keyword-research-2.md](keyword-research-2.md).

## Order of operations

Always work this sequence. Skipping steps wastes effort.

1. **Define the business job** — what does the business sell, who buys, what's the conversion goal? Without this, every keyword recommendation is guesswork.
2. **Mine first-party data** — Google Search Console + Bing Webmaster Tools. Free, highest signal, you already own it.
3. **Mine free public sources** — autocomplete, PAA, Reddit, forums, competitor sitemaps, Google Trends.
4. **Categorize into intent universe** — apply the intent matrix from `content-and-intent.md`.
5. **Validate with paid tools (only if needed)** — see *Getting competitor data without a subscription* below. No usable Ahrefs trial exists; the sanctioned paths are the free tiers, DataForSEO pay-as-you-go, or one paid month used properly.
6. **Prioritize** — by `(volume × commercial value × ranking probability) ÷ effort`.
7. **Map to page types** — comparison, alternative, local, tool, cluster, etc.

## Step 1 — Google Search Console mining (your highest-ROI source)

GSC shows what queries people *already* find your site for. After 30-60 days of data, it's better than any third-party tool because it's your actual reality.

### Setup

1. Verify property in Search Console.
2. Submit sitemap (audit point 7).
3. Wait 30-60 days for data to accumulate.
4. Export Performance report (Queries tab) for last 28-90 days.

### The four GSC mining reports

Run all four every month. Every filter value below (impression floors, CTR < 2%, position bands) is an `[unvalidated house heuristic]`: scale floors to the site (gsc-page2-audit.md §1), and compare CTR with this site's CTR at the same position before calling it low.

#### 1. CTR opportunity report

```
Filter: Impressions > 1000 AND Clicks/Impressions < 2%
Sort by: Impressions descending
```

These are queries you rank for but no one clicks. Diagnosis:
- Position 1-3 with low CTR → title/meta is weak. Rewrite for click-worthiness.
- Position 4-10 with low CTR → title/meta + position both weak. Push position AND improve copy.

Action: rewrite title + meta. Test with PAA-style or featured-snippet-shaped phrasing.

#### 2. Page 2 push report

```
Filter: Average position 11-20 AND Impressions > 500
Sort by: Impressions descending
```

Page 2 is the cheapest win. These pages are close to breaking through. Add missing sections, refresh content, build internal links to them.

#### 3. Striking distance report

```
Filter: Average position 4-10 AND Impressions > 1000
Sort by: Impressions descending
```

Position 4-10 has volume, but the top 3 usually take most of the clicks `[hypothesis]` — no measured CTR curve backs a percentage here, so read the share from this site's own GSC CTR by position before quoting one. Push to position 1-3 with content depth, schema, and internal linking.

#### 4. Orphan opportunity report

```
NOT a GSC filter — GSC cannot express "has no dedicated page". Derive it:
1. Export Performance → Queries (90d, sorted by impressions).
2. Export your URL inventory (sitemap.xml, or the Pages tab).
3. Join query → best-serving URL (Performance → filter query → Pages tab, or the
   BigQuery export for bulk).
4. Flag rows where the best-serving URL is a hub/listing/blog index rather than a
   page that targets that query specifically.
```

These are queries you accidentally rank for but don't have a dedicated page. Each is a potential new pSEO/cluster page.

### Pulling GSC data programmatically

For sites with significant query volume, the GSC web UI caps at 1000 rows. Use the API.

```python
# Python — google-api-python-client + service account auth
from googleapiclient.discovery import build
from google.oauth2 import service_account

creds = service_account.Credentials.from_service_account_file(
    'sa.json',
    scopes=['https://www.googleapis.com/auth/webmasters.readonly']
)
service = build('searchconsole', 'v1', credentials=creds)

response = service.searchanalytics().query(
    siteUrl='sc-domain:example.com',
    body={
        'startDate': '2026-04-10',
        'endDate': '2026-05-10',
        'dimensions': ['query', 'page'],
        'rowLimit': 25000,
        'startRow': 0
    }
).execute()
```

For very large sites, integrate GSC → BigQuery (Google's free integration) and run SQL.

### GSC analysis SQL templates (BigQuery)

▶ **Runnable version: [`scripts/gsc_bigquery.sql`](../scripts/gsc_bigquery.sql)** — parameterised (`@start`/`@end`), dry-runnable with `bq`. Prefer running that over retyping the blocks below; the four traps it documents were invisible for exactly as long as they lived in a markdown fence.

**Four things break naive queries here.** The first three are schema facts, confirmed against Google's own docs ([table reference](https://support.google.com/webmasters/answer/12917991), [query guidelines](https://support.google.com/webmasters/answer/12917174)):

1. **The column is `url`, not `page`.**
2. **There is no `position` column.** The export ships `sum_position`, a *sum over the row's impressions*, and it is **zero-based**. Average position is `SUM(sum_position)/SUM(impressions) + 1` — which is exactly what Google's own sample query computes. `AVG(sum_position)` is meaningless and, worse, it *runs*, returning plausible numbers that silently mis-rank everything you filter on.
3. **Each row is a (date, url, query, device, country) slice.** Anything you want per-query must be aggregated with `GROUP BY`, or you are reading one country-device-day, not the total.

The fourth is not a schema fact but an alias trap, and it has an impeccable pedigree:

4. **Don't reuse a column name as its own aggregate alias.** Google's published sample writes `sum(impressions) AS impressions`, which is legal **only because that sample has no `HAVING`**. Bolt one on and `HAVING SUM(impressions) > 1000` fails to compile — BigQuery resolves the bare name in `HAVING` to the *output alias*, giving "Aggregations of aggregations are not allowed". Copying the official sample and adding a filter is therefore a bug you inherit. Use `total_impressions`.

```sql
-- High impressions, low CTR
SELECT query, url,
       SUM(impressions) AS total_impressions,
       SUM(clicks)      AS total_clicks,
       ROUND(SUM(clicks) * 100.0 / SUM(impressions), 2)   AS ctr_pct,
       ROUND(SUM(sum_position) / SUM(impressions) + 1, 1) AS avg_pos
FROM `searchconsole.searchdata_url_impression`
WHERE data_date BETWEEN '2026-04-10' AND '2026-05-10'
GROUP BY query, url
HAVING SUM(impressions) > 1000
   AND SUM(clicks) * 1.0 / SUM(impressions) < 0.02
ORDER BY total_impressions DESC LIMIT 100;

-- Page 2 opportunities
SELECT query, url,
       ROUND(SUM(sum_position) / SUM(impressions) + 1, 1) AS avg_pos,
       SUM(impressions) AS total_impressions
FROM `searchconsole.searchdata_url_impression`
WHERE data_date BETWEEN '2026-04-10' AND '2026-05-10'
GROUP BY query, url
HAVING SUM(sum_position) / SUM(impressions) + 1 BETWEEN 11 AND 20
   AND SUM(impressions) > 500
ORDER BY total_impressions DESC LIMIT 100;

-- Cannibalization detection (multiple URLs ranking for the same query)
SELECT query,
       COUNT(DISTINCT url) AS competing_urls,
       SUM(impressions)    AS total_impressions,
       STRING_AGG(DISTINCT url, ', ' ORDER BY url LIMIT 5) AS sample_urls
FROM `searchconsole.searchdata_url_impression`
WHERE data_date BETWEEN '2026-04-10' AND '2026-05-10'
GROUP BY query
HAVING COUNT(DISTINCT url) >= 2 AND SUM(impressions) > 500
ORDER BY total_impressions DESC LIMIT 50;
```

## Step 2 — Bing Webmaster Tools

Most teams skip Bing. Don't.

- **Free keyword research tool** built in — returns volume, competition, related terms. Less data than Ahrefs but free.
- **Search performance** report = same shape as GSC.
- **Crawl stats + diagnostics** — Bing's index is independent and surfaces issues Google doesn't.
- **AI Performance** — citation metrics, not clicks: total citations, average cited pages, grounding queries, page-level citation counts and trends `[documented: https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview, 2026-10-14]`; Citation Share does not "represent traffic share" `[documented: https://blogs.bing.com/search/June-2026/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare, 2026-10-14]`. Neither post lists a click or CTR metric for citations; claim click effects only from separate referral/click data.

Set up alongside GSC. Sitemap submission and monitoring are 10 minutes total.

## Step 3 — Free public sources

### Google autocomplete (free, infinite, daily-fresh)

The autocomplete API returns suggestions for any seed query. These are real searches.

▶ **Runnable version: [`scripts/autocomplete_expand.py`](../scripts/autocomplete_expand.py)** — `python autocomplete_expand.py "comparar luz" --hl pt --gl pt --depth 2`. Handles geo params, throttling, dedup and failure-tolerance; use it instead of hand-rolling the loop below.

```bash
# JSON endpoint — hl= is LANGUAGE, gl= is COUNTRY. Send both.
curl "https://suggestqueries.google.com/complete/search?client=firefox&q=comparar+luz&hl=pt&gl=pt"
```

Returns: `["comparar luz", ["comparar luz e gas", "comparar luz portugal", "comparar luz edp galp", ...]]`

⚠️ **`hl` alone will hand you the wrong country's market.** `hl=pt` says *Portuguese*, not *Portugal* — omit `gl` and a PT-market build silently fills with Brazilian suggestions on Brazilian volume, which is the exact failure the geo/language reality check in SKILL.md warns about. Same trap for es (ES vs MX/AR) and en (US vs UK/IE).

Run programmatically with seed expansion: take each suggestion, add `a-z` to the end, query again. Each level multiplies coverage — two levels is usually enough for hundreds of long-tail variants per seed; go to three only when the vertical is genuinely deep, because cost is exponential in depth.

```python
import requests, string

def expand(seed, lang='pt', country='pt'):
    r = requests.get(
        'https://suggestqueries.google.com/complete/search',
        params={'client': 'firefox', 'q': seed, 'hl': lang, 'gl': country}
    )
    return r.json()[1]

def deep_expand(seed, depth=2, lang='pt', country='pt'):
    # thread lang/country through — a bare expand(s) here silently reverts to
    # the defaults and undoes the geo fix above
    found = set([seed])
    queue = [seed]
    while queue and depth > 0:
        next_queue = []
        for s in queue:
            for letter in '_' + string.ascii_lowercase:
                suffix = '' if letter == '_' else f' {letter}'
                for sug in expand(s + suffix, lang, country):
                    if sug not in found:
                        found.add(sug)
                        next_queue.append(sug)
        queue = next_queue
        depth -= 1
    return found
```

### People Also Ask (PAA)

PAA boxes contain real questions Google considers related. Capture them per target query.

- **AlsoAsked.com** — free tier 3 searches/day; visualizes PAA chains.
- **AnswerThePublic.com** — free tier limited; great for question-shape discovery.
- **Manual SERP scraping** — for 20-50 priority queries, manually capture PAA boxes monthly.
- **API options** — DataForSEO has a `serp/google/people_also_ask` endpoint at ~€0.0006 per query.

PAA chains often reveal entire content cluster blueprints.

### Reddit / Quora / forum mining

Real users articulate problems in their own words. Translate into pain-point keywords.

For Mowei (Portugal market):
- `r/portugal`, `r/Lisboa`, `r/Porto`, `r/financasportugal`, `r/Algarve`
- Forum: `forum.zwame.pt` (telecom), `bordadagua.com` (energy)

Search recipe:
```
site:reddit.com/r/portugal "fatura luz" OR "tarifa elétrica"
site:reddit.com/r/portugal "trocar de operador"
site:reddit.com/r/financasportugal "seguro automóvel"
```

Each thread is a content brief. Post titles often *are* keywords.

Speedrun: paste 30 thread URLs into ChatGPT/Claude with prompt "extract every distinct question or pain point users raise; one per line." Cluster the output.

### Google Trends

- Seasonality patterns (when does "seguro saúde" peak? "IRS portugal"?)
- Regional interest (Lisboa vs Algarve vs Porto query mix)
- Rising queries (catch trends early)
- Compare 2-5 terms at once for relative volume

Free, fast. Don't trust absolute numbers — use it for shape, not size.

### Competitor sitemap mining

Competitor sitemaps are a free roadmap to their organic strategy.

```bash
curl https://comparaja.pt/sitemap.xml
curl https://doutorfinancas.pt/sitemap.xml
curl https://kuantokusta.pt/sitemap.xml
```

URL slugs reveal targeted queries:
- `/luz/edp-vs-galp` → "EDP vs Galp"
- `/seguros/saude/medis-vs-multicare` → "Médis vs Multicare"
- `/credito/habitacao/spread-baixo` → "spread baixo crédito habitação"

Build a competitor-keyword matrix:

| URL slug | Inferred keyword | Mowei has equivalent? | Priority |
|----------|------------------|----------------------|----------|
| /luz/edp-vs-galp | edp vs galp | No | High |
| /credito/spread-baixo | spread crédito habitação baixo | No | Medium |

Pages competitors built but you haven't = direct keyword gap.

### Wikipedia / regulator entities

For YMYL niches (financial, legal, regulatory), Wikipedia categories and regulator websites reveal entity terminology you should cover:
- ERSE pages → energy term taxonomy
- Banco de Portugal glossary → banking terms
- ASF glossary → insurance terms
- Portal das Finanças → tax terms

Each entity is a glossary page candidate. Glossary pages also rank for "X meaning" / "X explicado" queries.

