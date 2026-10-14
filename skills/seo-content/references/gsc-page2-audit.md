# GSC page-2 / CTR-recovery audit — runnable procedure
<!-- split-header-2: part 1 of 2 of gsc-page2-audit.md (original lines 1–198; boundary start) -->
<!-- /split-header-2 -->

## Contents

- 0. Access — API first, browser UI as fallback
- Agent / MCP access
- 1. The anonymization trap decides the audit's shape
- 2. Bands and scoring
- 3. Cannibalization — verify class before prescribing
- 3a. Branded vs non-branded split
- 3b. Segment flags
- 3c. URL Inspection flags
- 3d. Keyword orphans
- 3e. Inventory cross-check

Other parts of the same original file: [gsc-page2-audit-2.md](gsc-page2-audit-2.md).

## 0. Access — API first, browser UI as fallback

**Prefer the Search Console API over the browser UI.** No 500-row UI cap, exact CTR/position
floats, and `dimensions:['query','page']` gives the query↔page map without a per-query UI
loop. The map is not complete: each response returns at most 25,000 rows (page with
`startRow`), rows come sorted by clicks, and the API "does not guarantee to return all
data rows but rather top ones" `[documented: https://developers.google.com/webmaster-tools/v1/searchanalytics/query, 2026-10-12]`.
Low-click query×page rows are the ones lost, and the query dimension can also miss most
impressions (§1). Report extraction coverage (query×page impressions ÷ page-only
impressions) next to any cannibalization finding. Auth pattern:
Desktop-app OAuth client, `searchconsole v1`, scope `webmasters`, cached refresh token
(survives access-token expiry; no browser flow needed on re-run). Window: end at
`today − 3d` (GSC lags 2–3 days), matched weekday span. On Windows set `PYTHONUTF8=1`
before printing query strings.

Browser-UI gotchas (when the API isn't wired):
- `search.google.com/search-console/welcome` shows "add a property" **even when
  properties exist** — never conclude "no properties" from that page. Probe a direct
  property URL instead: `https://search.google.com/u/N/search-console?resource_id=sc-domain%3Aexample.com`
  (or the URL-encoded https prefix for URL-prefix properties), sweeping the account
  index `N` from 0.
- The performance table's "Rows per page" dropdown often eats the first click (open
  animation) — click via an element ref, wait, then **verify the parsed row count**
  before trusting the extraction. If you parsed 10 rows, the dropdown didn't take.
- Domain (`sc-domain:`) and URL-prefix properties are separate permission grants; an
  account can hold one and 403 on the other.

## Agent / MCP access

**Rule: audit any connector before trusting it.** Before an agent's numbers go into a
report, read how the connector sorts rows, where it caps them, and what it puts in a
row that is missing from one window. Every defect below was found that way.

`mcp-gsc` (AminForou) is the GSC connector practitioners recommend `[practitioner]`.
Treat it as a data pipe only; its bundled recipes are unsafe as shipped — three of the
four pick the wrong rows.

**Tool contract** `[documented: https://raw.githubusercontent.com/AminForou/mcp-gsc/main/gsc_server.py, 2026-10-12]` (read from the repo's `gsc_server.py`; nothing executed; line numbers are those of the saved copy):

| Tool | Returns | Limit that matters |
|---|---|---|
| `get_search_analytics` | rows by dimension list (query, page, device, country, date) | `row_limit` ≤ 500; **no sort or filter argument** |
| `get_advanced_search_analytics` | the same, plus `filters` (AND across dimensions), `search_type` (WEB/IMAGE/VIDEO/NEWS/DISCOVER), `start_row`, `data_state` | ≤ 25,000 rows per call; paginate with `start_row`. **`sort_by` runs client-side over rows the API already returned — the top rows by clicks** (lines 1001-1006) |
| `get_search_by_page_query` | queries for one page | ≤ 500 rows |
| `compare_search_periods` | per-key deltas between two windows | top 1,000 rows per window (lines 1065, 1072) |
| `inspect_url_enhanced`, `batch_url_inspection`, `check_indexing_issues` | URL Inspection verdict, coverage, fetch, robots, Google-selected canonical, rich results | ≤ 10 URLs per call, run concurrently; API quota 600/min and 2,000/day per site (skill `seo-technical` › google-apis-and-quotas) |
| `list_sitemaps_enhanced`, `get_sitemap_details`, `submit_sitemap` | sitemap state | a GSC "Success" can be months old `[practitioner]` |
| `add_site`, `delete_site`, `delete_sitemap` | account writes | **disabled unless `GSC_ALLOW_DESTRUCTIVE=true`** — leave it disabled for agents |

- **Data state.** The server defaults to `GSC_DATA_STATE=all` (line 82), while the API
  default is `final`. Under `all` the most recent 2–3 days are preliminary, so a window
  ending today compared against one ending 28 days ago manufactures a decline. Use
  `final`, or end both windows 3 days back.
- **Domain properties.** Pass `sc-domain:` and filter on `page` to isolate a subdomain
  (tool docstrings, e.g. lines 409-410).

**Recipe guards** — each bundled recipe, its defect, and the rule to follow instead:

| Recipe | Defect (file:line) | Use instead |
|---|---|---|
| **content-opportunities** — query×page, `sort_by=impressions`, `row_limit=1000`, keep position 11–20, impressions > 100, CTR < 3 %, score `impressions × (0.05 − ctr)` | Rows come back as the top 1,000 **by clicks**, so the very rows wanted — page 2, many impressions, no clicks — are dropped before the filter sees them (gsc_server.py:1057; SKILL.md:14-23). `end_date = today` adds an empty preliminary tail. The 5 % CTR target is an `[unvalidated house heuristic]`; page-2 CTR is low because of position, so filtering on CTR adds little. | Page-led pull: `dimensions=page`, then `get_search_by_page_query` per page, or the BigQuery bulk export (`scripts/gsc_bigquery.sql`). Paginate to the end with `start_row`. Band by position as in §2. Never report "clicks gained if CTR reaches X". |
| **indexing-audit** — inspect the 20 pages with the most impressions | A page with impressions is indexed by definition, so the sample leaves out exactly the pages the audit exists for (SKILL.md:14). The step also passes `sort_by` to a tool that has no such argument. | Sample from the sitemap and the money-page list, within the 2,000/day quota. Report `coverageState`, `robotsTxtState`, `pageFetchState`, and Google-selected vs user-declared canonical. |
| **compare_search_periods** / **seo-weekly-report** (">20 % click drop" alert) | A key absent from one window is filled with `position: 0` (gsc_server.py:1265-1266), so a query that vanished from the current window shows a **positive** `position_diff` and reads as "improved". A query absent only because it fell under the 1,000-row cut looks lost or new. The 20 % alert has no volume floor (seo-weekly-report SKILL.md:16). | An absent row means "not in top N", never zero. Give a position verdict only where both windows have ≥ ~100 impressions, and read clicks by the click table in skill `seo-evidence` › experiments-and-revert-2: below ~100 clicks per side the state is `insufficient_data`; ~100–~355 is `inconclusive` unless the two-proportion test on the actual counts gives p < 0.05 (a −15 % fall can reach it from ≈305); ≈355 per side is where a +15 % relative CTR move can reach p < 0.05. Use 28-day windows ending on the same weekday, `final` data. |
| **cannibalization-check** — ≥ 2 pages on one query in the top 1,000 query×page rows → consolidate to the better page | Two URLs on one query is often right: sitelinks, brand queries, a compare page and a how-to page serving different intents. The row cap also skews the check toward head queries. | Use the class check in §3 (and skill `seo-technical` › migrations-and-recovery). Act only where the intent is the same and Google alternates between the URLs over time. Pull all rows (BigQuery or paginated). |

**Worth keeping from the repo** `[practitioner]`:
- Data tools return JSON, not prose, so the model quotes numbers instead of
  paraphrasing them.
- Account writes sit behind a flag that is off by default — the same allowlist idea as
  skill `seo-optimizer` › measurement-gates-and-checklists.
- Inspections run concurrently in batches of at most 10, so a 20-URL check finishes
  inside the MCP timeout.

## 1. The anonymization trap decides the audit's shape

🔴 **On low/mid-traffic sites the query dimension can carry as little as 15% of total
impressions** (mowei.pt: 3,131 of 20,500; the same site earlier measured a 96% click
drop by query vs date). Consequences, in order:

1. **Run the audit page-led.** Bands over `dimensions:['page']` (full coverage);
   query rows are the *labeling layer* that explains a page's demand, not the universe.
2. **Never sum query rows into a totals metric** — totals come from the no-dimension
   or date-dimension call.
3. **State visibility per page**: "known queries: 275i of 507i visible" tells the
   reader how much of the diagnosis is grounded. A page with 1,459 impressions and
   0% query visibility gets a snippet-level fix, not invented query targets.
4. **Thresholds scale to the site.** A "40+ impressions per query" floor built for a
   big site returns an empty band here. Set floors from the observed distribution
   (e.g. top-decile query impressions), and say which floor was used.

## 2. Bands and scoring

Pull 28d, then bucket (page-led; positions are averages, so bands blur at edges):

| Band | Definition | Meaning |
|---|---|---|
| **Opportunity** | pos 8–20.99, impressions ≥ floor, CTR < 2% | Below/at the fold; on-page + snippet work moves it |
| **Snippet problem** | pos < 8, impressions ≥ floor, CTR ≈ 0 | Already ranking, never clicked — title/meta, not ranking, work. Often the *biggest* bucket |
| **Too far back** | pos ≥ 21, impressions ≥ floor | Not an on-page tweak; list honestly as authority/content-depth or wrong-audience |

**Ordering score: `est monthly clicks = impressions × (0.06 − CTR)`.** 0.06 is an
`[unvalidated house heuristic]` stand-in for CTR around position 5 — a *planning number
for ordering, not a forecast*, and say so in the output. The formula has no position
term: score only rows already in the Opportunity or Snippet bands, so a pos-28 row is
filtered out (Too far back) before it is scored, never outranked by the score. Within
a band the score orders by impressions and CTR shortfall. On SERPs dominated by AI Overviews/big brands the
realistic ceiling may sit below 0.06 — keep the label "planning number" honest.

## 3. Cannibalization — verify class before prescribing

From the `['query','page']` map, flag any query where >1 URL earned impressions. Then
**diagnose the class before recommending a 301**:

- **Real split** (two content pages, comparable positions): consolidate — the URL
  already ranking best usually wins, not the one that "should" win by topic.
- **Parameter/filter split** (`/x` vs `/x?type=y`): **check the live canonical first.**
  If the param URL already canonicals to the clean URL, Google is *choosing* to show
  both — that's a soft split; the fix is editorial (make the clean page target the
  query), not another canonical/301.
- **Dated-series split** (monthly deadline pages, `…-jul` vs `…-ago`): expected
  ranking hand-off, usually 1-impression noise. No 301 — that would destroy the
  archive pattern.
- **Brand-navigational scatter** (brand query hitting 15 URLs): normal, ignore.
- **Owned SERP slots** `[practitioner]`: when every competing URL sits in the top 5,
  within ~2 positions of each other, the site holds several slots on that SERP.
  Monitor it; do not consolidate.

## 3a. Branded vs non-branded split

`[practitioner]` (this and §§ 3b–3e). Split every totals table by brand terms — ask for
them once, and include misspellings and the domain. Every opportunity and every
forecast uses the **non-branded** rows as its baseline, because branded CTR inflates
both. A branded query ranking below position 3 is a reputation or entity problem;
report it on its own.

## 3b. Segment flags

Each flag needs at least the site's impression floor (§1, point 4).

| Segment | Flag when | Usual reading |
|---|---|---|
| Section (`/energia/`, `/credito/`…) | section CTR well below the site average | a **template** title/meta problem — one template fix moves every page in the section |
| Section | high impressions, low clicks | intent mismatch, or a snippet problem across the template |
| Section | an expected section is missing | its pages are not ranking or not indexed — check the indexing report by template |
| Device | one device's CTR more than 30 % below the site average | mobile snippet truncation or mobile UX |
| Country | impressions with near-zero clicks in one market | hreflang / geo-targeting problem, or demand from the wrong market (see §4 "Wrong language/geo") |
| Search type | `discover` / `news` / `image` / `video` present | separate levers; report apart from web |

## 3c. URL Inspection flags

Inspect the top pages by clicks plus every declining page, then flag and explain:

- A top-traffic page that is `NOT_INDEXED` / `CRAWLED_CURRENTLY_NOT_INDEXED` →
  critical; find the cause actually served (noindex, canonical, robots, soft-404)
  before telling any value story.
- `DUPLICATE_WITHOUT_CANONICAL`, or Google chose a different canonical → set or fix
  the canonical.
- An important URL with no referring sitemap → add it to the sitemap.
- Last crawl more than 60 days ago on a page with traffic → a discovery /
  internal-link problem.
- Rich-result errors where schema exists → hand to the schema audit.

The URL Inspection API quota is per site: 2,000 queries a day and 600 a minute `[documented: https://developers.google.com/webmaster-tools/limits, 2026-10-12]` (skill
`seo-technical` › google-apis-and-quotas), so sample; never sweep.

## 3d. Keyword orphans

Look for a query sitting at position 4–20 where the URL that ranks is **unrelated to what was searched** (the homepage,
a sibling topic) and no page has the query in its title, H1 or slug. The fix is
a dedicated page for the measured intent — but only once you have confirmed it is a
distinct intent rather than a variant of an existing page (see
[content-and-intent.md](content-and-intent.md#intent-classification)). Three or more
related orphans form a cluster: check whether a pillar exists.

## 3e. Inventory cross-check

When a CMS export or the sitemap list is available:

- A published URL with zero GSC impressions → run the indexing check first; never
  assume "indexed but not ranking".
- Last modified more than 6 months ago **and** clicks declining → refresh candidate
  (see the decay step 0 in [content-and-intent-2.md](content-and-intent-2.md#content-refresh-workflow)).
  Age on its own is not a signal.

