# SEO drift monitoring — baseline, diff, and the deploy gate

## Contents

- Why this gate exists
- Baseline field spec
- URL normalisation
- The 17 comparison rules
- Security floor for whatever runs this
- Applying it to a Next.js deploy `[practitioner]`
- Deploy gates
- Crawler-facing drills and the WAF-drift alert
- Cross-references
- Sources

## Why this gate exists

Most SEO regressions are not decisions. They are a refactor that dropped a `canonical`, a staging config that shipped `noindex`, a component rename that emptied an `<h1>`, a CMS migration that stripped Open Graph tags, or a dependency bump that moved LCP. None of them appear in a ranking tool until traffic has already moved, by which point the change is buried under a week of other commits. A byte-level snapshot taken *before* the deploy turns a two-week forensic exercise into a diff.

`[practitioner]` This pairs directly with the project's existing rule to diff a branch against the live running baseline before a tar/rsync deploy. That rule protects the *code*; this protects the *rendered SEO surface*, which is what the code was for.

## Baseline field spec

Thirteen fields per URL. Everything here is cheap to capture and expensive to lose. `[practitioner]`

| Field | Type | Notes |
|---|---|---|
| `title` | string | Trimmed, whitespace-normalised |
| `meta_description` | string | Trimmed |
| `canonical` | string \| null | Store normalised (see below) *and* raw |
| `meta_robots` | string | Full directive string, not a parsed boolean |
| `h1` | array | Order preserved — Rule 6 compares the first |
| `h2` | array | Order preserved |
| `h3` | array | Order preserved |
| `schema` | array | Parsed JSON-LD blocks |
| `open_graph` | dict | Tag → content |
| `cwv` | dict \| null | p75 LCP / INP / CLS + Lighthouse performance score |
| `status_code` | int | Captured even on 4xx/5xx — the status **is** a tracked field |
| `html_hash` | SHA-256 | Body content, catch-all |
| `schema_hash` | SHA-256 | JSON-LD only, so a schema edit is separable from a copy edit |

Two hashes rather than one is the design decision worth keeping: it lets Rule 14 ("schema modified") fire independently of Rule 17 ("something changed"), which is the difference between an actionable alert and a diff nobody reads.

## URL normalisation

Baselines only match if the key is canonicalised the same way every time `[practitioner]`:

1. Lowercase the scheme and host (leave the path alone — paths are case-sensitive).
2. Strip default ports (`:80` on http, `:443` on https).
3. Sort query parameters.
4. Remove UTM parameters.
5. Strip the trailing slash.

⚠️ `[practitioner]` Steps 3–5 are lossy on purpose, and on some sites they are wrong. If `/guia/` and `/guia` serve different responses, or if a query parameter is load-bearing for the rendered page (a filter that changes the `<title>`), normalisation will silently collapse two distinct pages into one baseline and every diff after that is nonsense. Check that the normalisation is a no-op on your route set before trusting a single comparison.

## The 17 comparison rules

Three severity tiers, each with a response time `[practitioner]`:

| Tier | Meaning | Response time |
|---|---|---|
| **CRITICAL** | SEO-breaking, likely traffic loss within days | Immediate |
| **WARNING** | Potential impact, needs investigation | Within one week |
| **INFO** | Awareness only, may be intentional | Review at convenience |

### CRITICAL — rules 1–8

| # | Compare | Threshold | Action |
|---|---|---|---|
| 1 | `schema` array | Had items, now empty | Restore. Eligible rich results (Product, Review, LocalBusiness and similar supported types) can drop quickly. **Retired types — FAQ, HowTo — are not rich-result losses**; do not raise them as such |
| 2 | `canonical` | Different non-null values after normalisation | Confirm intentional. A wrong canonical routes ranking signals to another page |
| 3 | `canonical` | Had a value, now `null` | Restore. Google will guess, and guesses badly on parameterised URLs |
| 4 | `meta_robots` | `noindex` absent before, present now (case-insensitive) | If unintentional, fix immediately — the page drops from the index within days. The single highest-value rule in the set |
| 5 | `h1` | Had entries, now zero | Restore. Primary topic signal |
| 6 | First `h1`, `SequenceMatcher` ratio | Similarity below 0.5 against the baseline H1 string | Confirm the change is deliberate and still matches the target query |
| 7 | `title` | Had a value, now `null` or empty | Restore. Google auto-generates one, usually worse |
| 8 | `status_code` | 2xx before, 4xx or 5xx now | Investigate immediately. Rankings drop within days |

### WARNING — rules 9–14

| # | Compare | Threshold | Action |
|---|---|---|---|
| 9 | `title` | Strings differ (whitespace-normalised) | Verify keyword coverage; monitor CTR in GSC over two weeks — see skill `seo-evidence` › metadata-at-scale § How to run a title test |
| 10 | `meta_description` | Strings differ (trimmed) | Verify; monitor CTR |
| 11 | `cwv` p75 LCP / INP / CLS | Current value more than 20% worse than the baseline value for that metric | Investigate the regression: recent code, new third-party scripts |
| 12 | Lighthouse performance score | Drop of 10 or more points on the 0–100 scale (e.g. 85 → 74) | Run a full PageSpeed analysis |
| 13 | `open_graph` | Had entries, now empty | Restore. Social previews go generic |
| 14 | `schema_hash` | Hash differs **and** schema still exists (removal is Rule 1) | Re-validate: type changes, dropped properties, new validation errors |

### INFO — rules 15–17

| # | Compare | Threshold | Action |
|---|---|---|---|
| 15 | `schema` array | Was empty, now has items | Positive. Validate the new markup |
| 16 | `h2` array | Different count or different text | Review hierarchy against target topics |
| 17 | `html_hash` | Hash differs | Catch-all. Read it only when no other rule fired |

### Where this rule set is weak `[practitioner]`

- **Rule 17 is close to useless on a JS framework.** A Next.js document carries build IDs, RSC payloads and hydration data that change on every build regardless of content. Expect it to fire on 100% of pages in a deploy diff — meaning it distinguishes nothing. Either hash extracted main content rather than raw HTML, or demote it to a field you log and never alert on.
- **Rule 11 cannot gate a deploy.** CrUX p75 is field data over a rolling 28-day window; it physically cannot respond to a release that shipped an hour ago. Use Rule 12 (lab, Lighthouse) at the gate and Rule 11 as a weekly trailing check. Treating a field metric as a deploy signal produces an alert that arrives a month late and blames the wrong commit.
- **Rules 9 and 10 fire on every intentional copy edit.** Without an expected-changes list per release they train the team to ignore WARNING. Pre-declare which URLs are *supposed* to change and suppress those two rules for them — and only those two.
- **Rule 12 watches the 0–100 score; a CI gate should not.** Lighthouse CI practice is to assert metric values and budgets, because the score's weights change between Lighthouse versions — see Deploy gates below. Keep Rule 12 as a trailing hint, and gate on the metrics.
- **The set is single-page and single-snapshot.** It has no field for hreflang, no internal-link or orphan detection, no redirect-chain check, no `robots.txt` diff, no sitemap diff, and no indexation status from GSC. Those live in `crawl-and-index.md`, `rendering-and-sitemaps-2.md` (sitemaps) and the hreflang files, and must be run separately; a green drift report is not a clean technical audit.

## Security floor for whatever runs this

`[practitioner]` Any crawler you point at arbitrary URLs is an SSRF primitive. The source tool's floor is the right minimum and is worth stating as a requirement rather than a feature:

- **All fetching through one validated path** that rejects private IPs, loopback, reserved ranges and cloud metadata endpoints. Never bypass the validator "just for this one internal URL".
- **No `curl`, no subprocess HTTP.** One code path means one place to fix.
- **Parameterised SQL everywhere** (`?` placeholders, never string interpolation) — baselines are stored locally in SQLite and the URL is attacker-influenced input.
- **TLS always verified.** No `verify=False` anywhere in the pipeline.

Baselines are stored under a local cache directory keyed by normalised URL, with two tables: snapshots, and comparison results carrying the triggered rules and severities.

## Applying it to a Next.js deploy `[practitioner]`

The gate, in the order it runs:

**1. Pre-deploy baseline of the representative route set.** Do not baseline every URL — baseline one URL per *route template*, plus every commercially critical page. On mowei.pt the representative set already exists: a route-walk smoke test covers 288 representative URLs across the App Router's ~300 `page.tsx` files, and that list is the right input. Capture the baseline against **production, immediately before the deploy** — not against local dev, whose `<head>` differs.

**2. Deploy.** For the frontend this is the off-box build path; nothing about the gate changes that.

**3. Post-deploy diff, same URL set, same normalisation.** Read CRITICAL first. Rules 4 (noindex added), 3 (canonical removed) and 8 (status became an error) are the three that justify an immediate rollback without further discussion — each is a known way a staging config reaches production. Rules 1, 2, 5 and 7 need a ten-second check against the release notes before anyone reverts.

**4. Sitemap and prerender check — treat as a CRITICAL rule, not an INFO one.** The 17 rules above have no sitemap field, and on this stack that is the exact hole a real incident fell through: an off-box build prerenders `sitemap.xml` without a live Django, and the route ships with an empty or truncated sitemap that no page-level diff can see. The check is a count, and it is binary:

```
curl -A Mozilla https://mowei.pt/sitemap.xml | grep -c /rendimento/acoes/
```

Expected: **32**. A `0` means the sitemap prerendered without the backend. The documented remedy is to touch the two `.next/server/app/sitemap.xml` artefacts to an older timestamp inside the `nextjs` container and restart it — a plain restart plus a CDN purge has failed to clear it. 🔴 **Never `rm` `.next/server/app/sitemap.xml`**: that path is the route's code directory, not a cache, and deleting it has caused roughly 90 seconds of 500s. Full procedure: the project `CLAUDE.md` deploy section.

Generalise the shape, not the number: for any route whose content is *generated at build time from a backend*, assert a **count** post-deploy. A count is the cheapest assertion that can tell "rendered correctly" apart from "rendered empty", and an empty sitemap returns HTTP 200.

**5. Pre-declare what is allowed to change, before you look at the diff.** Write the expected CRITICAL/WARNING rules into the release note *in advance*. A diff read after the fact gets rationalised; a diff read against a pre-declared list cannot be. This is the same discipline as the pre-declared revert triggers in skill `seo-evidence` › experiments-and-revert-2 — and the revert decision itself belongs there, not here.

⚠️ **Run the drift walk and the route smoke walk serially, not concurrently.** Two crawlers against one origin compete for the port and the CPU and manufacture failures that look like product defects.

## Deploy gates

Checks that cover the holes listed under "Where this rule set is weak" (robots, sitemap, redirects, metrics). Each row is a tool chosen for the method it encodes; the trap column is part of the gate.

| Gate | Tool and method | Fail when | Trap |
|---|---|---|---|
| robots.txt and sitemap diff | `eliasdabbas/advertools`: `robotstxt_to_df` and `sitemap_to_df` (accepts robots.txt, an index or a sitemap) snapshot both on every deploy; diff against the previous snapshot `[practitioner]` | A `Disallow` appears or disappears unannounced; sitemap URL count or set changes outside the release note | `logs_to_df` bot counts need bot verification (reverse DNS or Web Bot Auth) — user-agent strings are spoofed `[documented: https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers, 2026-10-11]` |
| `lastmod` honesty | Same sitemap snapshot: compare `lastmod` values between deploys `[practitioner]` | Every URL carries the same `lastmod`, equal to the build time — the `next-sitemap` `autoLastmod: true` signature (see [rendering-and-sitemaps-2.md](rendering-and-sitemaps-2.md) § `next-sitemap`: the `autoLastmod` trap) | Native `sitemap.ts` with `new Date()` produces the same failure |
| Sitemap served as HTML | `curl -sI` the sitemap as a browser and as Googlebot; read the first bytes `[practitioner]` | Not 200, `Content-Type` not XML, or body does not start with `<?xml` / `<urlset` / `<sitemapindex` | A 200 status alone proves nothing — procedure in [rendering-and-sitemaps-2.md](rendering-and-sitemaps-2.md) § Sitemap served as HTML |
| No internal redirects | `JustinBeckwith/linkinator` `--recurse --check-fragments --redirects error --require-https error`; `--retry` honours a 429 `retry-after` `[practitioner]` | Any internal link answers with a redirect, or any link is broken | Fragment checks only see server-rendered HTML (README:121) |
| Performance regression | `GoogleChrome/lighthouse-ci` `lhci autorun`: assertions on any audit's `numericValue` (LCP, CLS, TBT) and a `budgets.json` file per PR, 3 runs per URL by default `[documented: https://raw.githubusercontent.com/GoogleChrome/lighthouse-ci/main/docs/configuration.md, 2026-10-12]` | A metric or budget assertion fails | Assert metrics, **not** the 0–100 score — its weights change between Lighthouse versions. Lab only; field CWV is a trailing weekly read (Rule 11) |

The sitemap count check in step 4 above stays: these gates add to it, they do not replace it.

## Crawler-facing drills and the WAF-drift alert

`[practitioner]` Run each drill, and write down the date it last passed.

| Fault injected | Required behaviour |
|---|---|
| Origin killed | The CDN serves a stale 200 with a visible age stamp |
| Data API returns 500, or hangs for 3 s | Fallback content renders within 3 s; `main` is not blank |
| Requests carrying a verified bot UA receive 403 | **The WAF-drift alert fires** |

**WAF-drift alert:** page a human when the share of 403s or challenges served to verified crawlers (Googlebot, Bingbot, GPTBot, …) moves away from its baseline. Never let automation relax the WAF without a rule diff. Why it exists: in the Aug-2026 incident Cloudflare hard-blocked verified Googlebot and Bingbot while every curl check returned 200. How to verify a bot's identity: skill `seo-ai-search` › ai-crawlers-and-bot-policy. The degrade-without-blanking rule these drills test lives in [rendering-and-sitemaps-2.md](rendering-and-sitemaps-2.md) § Degrade, do not blank.

## Cross-references

- skill `seo-evidence` › experiments-and-revert-2 — owns revert conditions and verdict states. Drift detection feeds it; it does not duplicate it.
- skill `seo-evidence` › experiments-and-revert-2 — what to do once a drift alert needs a traffic answer.
- `incident-triage.md#classify-the-incident-first` — deploy vs core update vs indexing vs demand. A clean drift diff is the strongest available evidence that a traffic move was *not* the deploy.
- `crawl-and-index.md#indexability`, `rendering-and-sitemaps-2.md#sitemapxml` and `international-and-hreflang-2.md` — the checks this rule set structurally cannot make (hreflang, orphans, redirect chains, robots, sitemap validity).
- `rendering-and-sitemaps.md#core-web-vitals` — the CWV bar itself; rules 11 and 12 only detect movement against your own baseline.
- skill `seo-engine-policies` › google-updates-timeline-2 § Data-reliability windows — check these before any before/after — before attributing a drift alert to a traffic change.

## Sources

- `claude-seo@skills/seo-drift/SKILL.md:35-54` — the 13-field baseline spec, carried whole as a specification.
- `claude-seo@skills/seo-drift/SKILL.md:63-70` — severity tiers and response times, carried verbatim.
- `claude-seo@skills/seo-drift/SKILL.md:86-88` — URL normalisation steps, carried with a `[practitioner]` caution about lossy collapse.
- `claude-seo@skills/seo-drift/SKILL.md:188-195` — the security floor, restated as a requirement.
- `claude-seo@skills/seo-drift/references/comparison-rules.md:1-124` — all 17 rules with compare/threshold/action; cross-refs rewritten from the source tool's slash commands to this skill's reference paths. The "where this rule set is weak" section is `[practitioner]` and is not in the source.
- installed/site-improvement@references/architecture-and-build.md, installed/site-improvement@references/execution-and-resilience.md (phase-2 adapted file research/adapted/installed__site-improvement/rendering-caching-and-crawler-parity.md) — crawler-facing drills table and the WAF-drift alert with its Aug-2026 origin. INTEGRATE, in-house (no third-party licence found).
- eliasdabbas/advertools@README.md (phase-2 adapted file research/adapted/group-E__readme-tool-repos/tool-stack-by-job.md) — robots.txt and sitemap snapshot-and-diff gate; bot verification caveat for log parsing. INTEGRATE, MIT.
- iamvishnusankar/next-sitemap@README.md (phase-2 adapted file research/adapted/group-E__readme-tool-repos/tool-stack-by-job.md) — `autoLastmod` build-time stamp as a gate condition. INTEGRATE, MIT.
- JustinBeckwith/linkinator@README.md (phase-2 adapted file research/adapted/group-E__readme-tool-repos/tool-stack-by-job.md) — no-internal-redirect gate flags, `--retry`, fragment-check limit. INTEGRATE, MIT.
- GoogleChrome/lighthouse-ci@README.md (phase-2 adapted file research/adapted/group-E__readme-tool-repos/tool-stack-by-job.md) — assert metrics and budgets, several runs, not the score. INTEGRATE, Apache-2.0.
- kostja94/marketing-skills@skills/seo/technical/sitemap/SKILL.md (phase-2 adapted file research/adapted/kostja94__marketing-skills/sitemap-indexnow-ssot-and-sitemap-served-as-html.md) — sitemap-served-as-HTML post-deploy check. INTEGRATE, MIT.
