-- GSC bulk-export analysis queries (BigQuery).
--
-- WHY THIS IS A FILE AND NOT A SNIPPET. The prose version carried three schema
-- bugs that all looked fine on the page:
--   1. `page`     -> the column is `url`.
--   2. `position` -> no such column. The export ships `sum_position`.
--   3. `AVG(sum_position)` -> meaningless. `sum_position` is already a SUM over
--      the row's impressions, and it is ZERO-BASED. Average position is
--      SUM(sum_position)/SUM(impressions) + 1.
-- Bug 3 is the dangerous one: it RUNS, returns plausible numbers, and silently
-- mis-ranks whatever you filter on.
--
-- Each row is a (data_date, url, query, device, country) slice, so anything you
-- want per-query MUST be aggregated. Selecting without GROUP BY reads one
-- country-device-day, not the total.
--
-- Schema confirmed against Google's own docs (Search Console Help 12917991 /
-- 12917174): the columns are `url` and `query`; `sum_position` is zero-based;
-- and Google's published sample computes average position as exactly
-- ((sum(sum_position) / sum(impressions)) + 1.0).
--
-- THE ALIAS TRAP — narrower than it looks, and fatal only with HAVING.
-- Google's own sample writes `sum(impressions) AS impressions`, which is fine
-- BECAUSE IT HAS NO HAVING CLAUSE. Add one, and `HAVING SUM(impressions) >
-- 1000` fails to compile: BigQuery resolves the bare name in HAVING to the
-- OUTPUT ALIAS, so you get "Aggregations of aggregations are not allowed".
-- Copying Google's sample and bolting a HAVING onto it is therefore a trap
-- with an impeccable pedigree. Simplest defence: never reuse the column name
-- as the alias — hence total_impressions / total_clicks below.
--
-- HOW TO VERIFY. `bq --dry_run` is a real check — verified 2026-08-19 on this
-- file: piping the whole file to `bq query --use_legacy_sql=false --dry_run`
-- caught BOTH an appended bogus column AND the alias collision above (exit 1,
-- "Aggregations of aggregations are not allowed"). Dry-run your edits.
--
-- Prefer ONE STATEMENT AT A TIME anyway, for a weaker but practical reason:
-- a whole-file run stops at the first error and does not tell you which
-- statement broke, so on a multi-query file you get one error and no address.
--   bq query --use_legacy_sql=false --dry_run \
--     --parameter=start:DATE:2026-04-10 --parameter=end:DATE:2026-05-10 \
--     'SELECT ...one statement...'
-- (Passing a multi-line query as a shell ARGUMENT truncates it at the first
-- newline on Windows — pipe via stdin, or collapse it to one line.)

-- ---------------------------------------------------------------------------
-- 1. High impressions, low CTR — demand you surface for but fail to capture.
-- ---------------------------------------------------------------------------
SELECT
  query,
  url,
  SUM(impressions)                                   AS total_impressions,
  SUM(clicks)                                        AS total_clicks,
  ROUND(SUM(clicks) * 100.0 / SUM(impressions), 2)   AS ctr_pct,
  ROUND(SUM(sum_position) / SUM(impressions) + 1, 1) AS avg_position
FROM `searchconsole.searchdata_url_impression`
WHERE data_date BETWEEN @start AND @end
GROUP BY query, url
HAVING SUM(impressions) > 1000
   AND SUM(clicks) * 1.0 / SUM(impressions) < 0.02
ORDER BY total_impressions DESC
LIMIT 100;

-- ---------------------------------------------------------------------------
-- 2. Page-2 opportunities — ranked 11-20 with real demand behind them.
-- ---------------------------------------------------------------------------
SELECT
  query,
  url,
  ROUND(SUM(sum_position) / SUM(impressions) + 1, 1) AS avg_position,
  SUM(impressions)                                   AS total_impressions,
  SUM(clicks)                                        AS total_clicks
FROM `searchconsole.searchdata_url_impression`
WHERE data_date BETWEEN @start AND @end
GROUP BY query, url
HAVING SUM(sum_position) / SUM(impressions) + 1 BETWEEN 11 AND 20
   AND SUM(impressions) > 500
ORDER BY total_impressions DESC
LIMIT 100;

-- ---------------------------------------------------------------------------
-- 3. Cannibalization — one query, several of your URLs splitting the signal.
--    The GSC UI cannot do this at scale: the Queries tab does not list URLs,
--    so by hand it is filter-one-query-then-open-Pages, repeated forever.
-- ---------------------------------------------------------------------------
SELECT
  query,
  COUNT(DISTINCT url)                                 AS competing_urls,
  SUM(impressions)                                    AS total_impressions,
  ROUND(SUM(sum_position) / SUM(impressions) + 1, 1)  AS avg_position,
  STRING_AGG(DISTINCT url, ', ' ORDER BY url LIMIT 5) AS sample_urls
FROM `searchconsole.searchdata_url_impression`
WHERE data_date BETWEEN @start AND @end
GROUP BY query
HAVING COUNT(DISTINCT url) >= 2
   AND SUM(impressions) > 500
ORDER BY total_impressions DESC
LIMIT 50;
