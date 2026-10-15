# Source-specific methods (what worked, what failed)

## Regulator registers and company registries
- Licence registers (credit intermediaries, insurance distributors, payment/e-money institutions) usually
  return 403 or a CAPTCHA to scripts but load in a real browser. Search by number, then by name; record
  number, legal name, category (tied / untied / ancillary; agent / broker), lender/insurer count, status,
  liability-insurance expiry. Self-declared numbers in site footers are often mistyped — the register wins.
- Company registries: free tiers often expose legal form, constitution date, activity code, former names,
  and **size bands** (turnover / headcount) through search facets. Some show a sales chart whose values are
  shares of a multi-year total, not euros — divide consecutive years for growth. Paid reports: do not buy
  without the owner's approval.
- Domain WHOIS (national registry port-43 service) reveals the registrant for some ccTLDs; hidden owner →
  write "operator not disclosed".

## Traffic triangulation (grade every figure A–D)
Sources, from strongest: audited audience measurement / first-party disclosures → real-user rank buckets
(public browser-telemetry top lists per country) → research rank lists → panel estimates (public site
pages) → clickstream estimates → organic-only crawl models → aggregator copies.
- Calibrate rank → visits using domains where an A-grade figure exists; report best estimate + range.
- The panel's public headline is one month; check the ratio against a second estimator (a geometric mean
  near 1 confirms it; near 3 would mean a quarterly total).
- The subject's own analytics beat every panel for its own row.

## Backlinks / authority
- Public web-graph releases (domain-level ranks, vertices, edges) can be streamed and filtered to the
  target domains plus their referrers — reproducible, but sampled and domain-level only.
- Public "top websites" pages of commercial SEO tools give a rating + linking domains; a 404 means "not in
  the public list", not zero.
- Check the subject's robots policy: blocking a crawler also removes the subject from that crawler's graph.

## Search visibility and AI answers
- One browser session per engine; ≤35 queries; 20–30 s pacing; record engine, locale params, local time.
- Capture per query: ads (order), organic top-10 (domain + title), AI-answer presence + cited domains,
  "people also ask", subject position. Store raw rows in CSV; compute share of voice with a script that
  is validated by reproducing an earlier table before adding new rows.
- Run brand queries first (brand, domain, `site:` count) — confusion with similar brands is a finding.
- A second engine and its AI assistant surface different small sites; label results per engine.

## Paid media
- Ad transparency centers (region filter, domain search → advertiser accounts with verified legal names →
  per-ad first/last shown, format, impressions range, payer). Note published data lags.
- Social ad libraries (country filter, keyword search, sort by impressions; "ad details" shows reach,
  targeting, payer). Anonymous lead-gen pages and white-label "comparators" paid by a supplier show up here.
- Automated sessions may be shown fewer ads; daytime differs from night.

## Gated-flow observation
- Walk public simulators step by step; record what is asked before any result (contact data, ID numbers,
  postcode, documents). If a step requires input to proceed, use obviously fictional non-personal values
  (amounts, ages), never names/emails/phones/IDs. Stop before any submit button.

## Fact-check grading
- CONFIRMED / CORRECTED / UNVERIFIABLE, with the decisive quote. Official-journal pages that render empty:
  read a faithful reproduction and mark "confirmed via reproduction — read the official text before acting".
- Distinguish counts of operations vs people, shares of a sub-market vs the whole market, income vs turnover.

## Known blocks
- Large forums and some social platforms refuse automated fetches and browser-tool use — record as a gap.
- Some regulator sites time out from certain networks — try another day before concluding.
