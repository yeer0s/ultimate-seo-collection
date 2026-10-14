# Live-site inspection method

## Contents

- When to load this
- Controls before verdicts
- Fetching: behave like a browser
- Sampling by route template
- Measuring the right quantity
- Text probes that do not false-positive
- Findings that diff across runs
- SEO passes the method must carry
- Known harness defects (D1–D8)
- Unverified
- Sources

## When to load this

Load it when an audit has to produce a **measured** baseline of a live site (status codes, canonicals, indexability, what actually renders, lab CWV values) instead of a narrated one. This file is about the instrument and its honesty. What counts as a regression after a release lives in [seo-drift-monitoring.md](seo-drift-monitoring.md); how to read lab against field CWV lives in [cwv-field-lab-diagnosis.md](cwv-field-lab-diagnosis.md); score gates live in skill `seo-optimizer` › measurement-gates-and-checklists.

## Controls before verdicts

`[practitioner]` — learned on mowei.pt on 2026-08-28.

- Each rule that can be planted gets two fixtures, both run at the start of the same run: a **positive fixture that must trigger it** and a **clean twin that must stay quiet**. Pair used for the i18n key-leak rule: `site.banca_page.hero_title` must fire; `www.example.site … app.min.js.map` must not.
- When the positive fixture fails to fire, the rule drops out of the `armed` set. Its findings can then reach `likely` at most, and the run metadata says which rule was dropped.
- Only an armed rule may write `confirmed`. **Deterministic HTTP facts** (a status code, whether a header is present, whether two titles are equal) need their own planted control — serve a known 404, 301 or `noindex` fixture — or an explicit exemption. Without one of the two, the confidence cap quietly demotes them (defect D1 below).
- Show that the all-clear can actually be reached: run the scanner on a clean page. A scanner that can never report "clean" is an alarm bell, not a measurement.

## Fetching: behave like a browser

`[practitioner]`

- Send HTTP checks through the browser's own request context, which decodes brotli and normalises header case. A plain urllib probe on a brotli site with lowercase headers produced a false "no CSP/HSTS" finding and an empty link list.
- Send the audience's `Accept-Language` (pt-PT for mowei.pt).
- **Switch redirect-following off for sitemap sweeps** (`max_redirects=0` or the equivalent). A followed 301 is recorded as 200, and "redirect listed in the sitemap" vanishes from the report (defect D2).

## Sampling by route template

`[practitioner]`

- Turn the sitemap into templates. Group URLs by (parent prefix, depth); a segment position holding **≥ 8 distinct values becomes `{slug}`**; numeric or UUID-like segments become `{id}`. The 8 is an `[unvalidated house heuristic]`.
- Representatives: for a literal template, the URL of median length; for a template with a variable, **two** — the shortest and the longest.
- Always add the money surfaces, found by path hint (`comparar`, `simulador`, `ferramentas`, …). A few tens of templates stand in for hundreds of URLs, and a new section is picked up on the next run with no list to maintain.
- Sampling applies to the browser pass alone; every sitemap URL still goes through the inexpensive HTTP sweep.
- Same principle at Lighthouse scale: `harlan-zw/unlighthouse` scans an entire site with Lighthouse using "smart sampling" `[documented: https://raw.githubusercontent.com/harlan-zw/unlighthouse/main/README.md, 2026-10-12]`.
  Unlighthouse sampling rule: unverified [unverified: the saved README does not say it samples one URL per route template]; see ## Unverified.
  It is lab only, so read its output per template, never as a site-wide average.

## Measuring the right quantity

- **CLS is the largest session window** (1 s gap, 5 s cap), not the sum of every shift over the page's life `[documented: https://web.dev/articles/cls, 2026-10-12]`. A lifetime sum cannot be compared with CrUX or with the 0.1 threshold `[practitioner]`.
- A resource with `transferSize==0 && decodedBodySize==0` is **opaque** (cross-origin, no `Timing-Allow-Origin`). Count those on their own line; never add them as zero bytes `[practitioner]`.
- **Ready means `h1`/`main` visible plus a short settle**, not `networkidle` — a page with chatty analytics may never go idle `[practitioner]`.
- Lab LCP is unthrottled unless you throttle it; put that in the label. Field P75 (CrUX or RUM) makes the call `[practitioner]`.
- INP needs a genuine **click, tap or key press**; scrolling and hovering are not observed for INP `[documented: https://web.dev/articles/inp, 2026-10-12]`. So a pass that only scrolls or moves the mouse has measured nothing (defect D4) `[practitioner]`.

## Text probes that do not false-positive

`[practitioner]`

- Tie every i18n key-leak regex to the **namespace prefixes the site is known to use**. An unanchored `a.b.c` pattern matches hostnames and file names.
- Case-insensitive by default, and the probe and the fix must apply the same case rule; if they differ, believe neither.
- Check a value only on the node that carries it: a negative number is a defect on the net-result node and perfectly normal on a deduction row.
- **Sitemap ground truth:** a URL you made up probes the 404 surface; it is no evidence that a real page is broken. Check sitemap membership and internal links first.

## Findings that diff across runs

Each finding is a record: `{rule, route, template, severity P0–P3, confidence confirmed|likely|needs-repro, evidence{kind,value}, fingerprint}` `[practitioner]`.

- Fingerprint = hash(rule | template | evidence with digits normalised).
- **Bucket metrics** (for example CLS `<0.1 / <0.25 / <0.5`) so that run-to-run jitter does not mint a "new" finding.
- Merge on fingerprint: keep the highest severity and the best confidence, and union the routes (with a cap on the list).

Severity anchors for Mowei `[unvalidated house heuristic]`:

| Severity | Examples |
|---|---|
| P0 | Wrong money figure; hydration error on a money route |
| P1 | Sitemap URL not 200; CLS ≥ 0.25; uncaught error |
| P2 | Duplicate titles; broken images; serious axe finding |
| P3 | Hygiene, e.g. missing canonical |

An inspection finding is an anchored observation, not a priority. It still goes through prioritisation: merge inspection findings and judgement findings into **one** ranked plan.

## SEO passes the method must carry

These are gaps in the installed harness; each row names the defect it closes.

| Pass | Check | Why |
|---|---|---|
| Sitemap discovery | `Sitemap:` lines in `robots.txt`; recurse into sitemap **index** files | The harness reads `/sitemap.xml` only and would sweep child `.xml` files as if they were pages (D3) |
| Indexability | meta robots in **any attribute order or quote style**, `googlebot`/`bingbot` metas, the **`X-Robots-Tag` header** | One regex for `name="robots"…noindex` misses the rest (D5) |
| Canonical | Parse the element, then require **target == requested URL** (or a documented exception) | Presence alone is the weak test (D5) |
| Redirects | 3xx listed in the sitemap, chains, loops | D2 |
| Bot parity | Fetch the same URL as a browser UA and as each allowed crawler; compare status and body hash | In Aug 2026 Cloudflare silently returned 403 to verified Googlebot while curl got 200. Request-as-bot method: skill `seo-ai-search` › ai-crawlers-and-bot-policy |
| Duplicate titles | Group per locale; skip URLs canonicalised elsewhere or `noindex` | Avoids cross-locale and variant false positives |
| Error boundary | Route `**/api/**` → 500; `main` must not go near-empty | A blank SSR shell is what a crawler indexes |

## Known harness defects (D1–D8)

The installed `site-improvement` harness was read as data, not run. Do not copy its checks with these defects in them.

| ID | Location | Defect |
|---|---|---|
| D1 | `lib.py:68-73`, `controls.py:13-101` | Only 8 planted rules can ever be armed, so `cap_confidence` demotes every `confirmed` from `non-200`, `duplicate-title`, `noindex-in-sitemap`, `cold-ttfb-tail`, `axe-*`, `csp-violation`, `bad-response`, consent, keyboard and `blank-on-api-500` to `likely` — although the doc promises `confirmed` for them |
| D2 | `inspect_site.py:48` | `request.get` follows redirects by default; sitemap 301s are reported as 200 |
| D3 | `inspect_site.py:323-324` | Reads `/sitemap.xml` only; no index recursion, no discovery through robots.txt |
| D4 | `inspect_site.py:100-103,146-149` | Only mouse-move and wheel happen before Event Timing is read; `slow-interaction` effectively never fires and has no control; the "lab INP" claimed at SKILL.md:29 is not measured |
| D5 | `inspect_site.py:59,63` | Robots-meta and canonical regexes depend on quote style and attribute order; no `X-Robots-Tag`; no self-canonical check |
| D6 | `lib.py:220` | `HYDRATION_RE` includes a bare case-insensitive `hydration` — over-broad; its clean twin never exercises that branch |
| D7 | `inspect_site.py:8` | The docstring promises an offline pass; only the API-500 pass exists (`:274`) |
| D8 | — | No bot-UA pass, although the verification pack lists `bot_ua.txt` (site-improvement SKILL.md:39) |

## Unverified

- Unlighthouse sampling rule: `harlan-zw/unlighthouse` samples one URL per route template and scans those [unverified: the saved README does not say it samples one URL per route template]

## Sources

- installed/site-improvement@references/site-inspection.md, installed/site-improvement@inspection/inspect_site.py, installed/site-improvement@inspection/lib.py, installed/site-improvement@inspection/controls.py, installed/site-improvement@inspection/routes.py (phase-2 adapted file research/adapted/installed__site-improvement/site-inspection-method.md) — controls-first rules, browser-context fetching, template sampling, measurement rules, probe rules, finding shape and Mowei severity anchors, the SEO pass gaps, and harness defects D1–D8 (read, not run). INTEGRATE, in-house (no third-party licence found; the vendored axe.min.js, MPL-2.0, is not reproduced).
- harlan-zw/unlighthouse@README.md (phase-2 adapted file research/adapted/group-E__readme-tool-repos/tool-stack-by-job.md) — one URL per route template, lab only, read per template. INTEGRATE, MIT.
