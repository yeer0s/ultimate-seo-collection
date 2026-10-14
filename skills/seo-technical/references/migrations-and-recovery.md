<!-- split-header: part 2 of 2 of migrations-and-recovery.md (step-3 original lines 38–143; boundary H2) -->
# Migrations and recovery — URL changes, migrations, consolidation, canonical repair, links, rollback
## Contents

- URL and slug changes
- Domain and platform migrations
- Consolidation
- Canonicals and indexation repair
- Links: disavow and recovery
- Core-update and HCU-class recoveries
- Rollback playbook
- Sources

Other parts of the same original file: [incident-triage.md](incident-triage.md).

<!-- /split-header -->
## URL and slug changes

**Entry #174 — Include target keywords in page URLs — IT DEPENDS** `[measured: IT DEPENDS, n=2 samples, c=0 controlled]`. The two sides: **−38% organic sessions** where pages changed their addresses to target broad high-volume terms (moz.com 2021, before/after, no control, 200 URLs) versus **direction only** where specific service pages added targeted role terms (daveashworth.co 2026, before/after, no control, 27 URLs). The study's moderator question: *are you adding specific role modifiers or broad high-volume keywords to your URLs?* Its own "what this evidence cannot tell you": the uncontrolled observation does not rule out seasonality, concurrent changes, or loss of equity during redirect processing. Evidence score 35.5.

How to carry it:

- **Descriptive slugs on NEW pages** `[practitioner]` — fine, cheap, a usability choice; there is no measured ranking claim to attach to it.
- **Renaming EXISTING URLs to insert keywords — refuse without a matched control.** The only sized side of #174 is a loss. If the client insists, run the study's own recipe: map old→new, implement 301s, treat a sample, keep a matched control at the old paths, hold titles/headings/body/internal links identical across both, compare organic sessions for 60 days, revert if the treated set drops relative to control.
- **"Fresh slug + 301 to trigger re-evaluation" is a URL change and inherits this mark.** It is not a fix for "Crawled – currently not indexed"; it moves whatever the page had to a new address and adds redirect processing on top. Fix value and internal discovery first; if a URL change is still wanted, it is an experiment under #174's conditions, never a routine step.

## Domain and platform migrations

**Entry #133 — Migrate domain extension using server redirects — MAINSTREAM** `[measured: MAINSTREAM, n=6 samples across 6 publishers, c=0 controlled]`. Headline **+60% organic sessions** (hooshmand.net 2023, 1 site — a traffic-drop-*recovery* write-up); the study notes the **reported values run from −90% to +65% and cross zero, so no median is printed**. Other sized sources: seoprofy.com 2025 (+65%, 1 site), sistrix.com 2025 (+61.7%, 1 domain); three are direction only, including salt.agency 2026 on **1,052 domains**, whose own title says 27% of migrations recover within 90 days. All six before/after, no control. Evidence 64.6, actionability 39.7.

Read it as **support for careful execution, not a promise that changing TLD or platform raises traffic.** Nobody publishes the migration that lost 40% and stayed there `[practitioner]`; the −90% in this entry is the drop that preceded a published recovery.

The procedure `[practitioner]`:

1. **URL inventory** — every URL with GSC impressions over 16 months, in the sitemap, with external links, or referenced by internal links or redirects. Union, deduplicate, freeze.
2. **1:1 map** — old path → new path, exact equivalent, one hop. Anything without an equivalent gets an explicit decision (nearest parent, 410, or keep) — never a default to the home page.
3. **Redirect tests** — run the whole map against staging before cutover: exactly one 301 per row, final status 200, final URL equals the mapped target; fail on chains, loops, 302s and 200s at the old path.
4. **Parity checks** on a template sample: title, meta, canonical (self-referential on the new host), hreflang pairs, JSON-LD, internal links resolving directly to new-host URLs, robots/noindex identical, rendered HTML identical in content.
5. **Keep the old property in GSC**, add the new one, submit the **change of address** for host-to-host moves; submit the new sitemap and keep the old one listing old URLs until they drop out.
6. **Monitor by template**, not site-wide: clicks, impressions, position, indexed count and coverage reasons per template — daily for two weeks, weekly to 90 days. A site-wide line hides the template that did not redirect.
7. **Pre-declared rollback conditions** — metric, band, window, decider — written before cutover (skill `seo-evidence` › experiments-and-revert-2 § Revert triggers). Keep the old host serving 301s for at least a year; rolling back a migration is itself a migration.

Edge and off-box gotchas seen on real deploys `[practitioner]`: a CDN serving cached old-host HTML or cached 301s after a rollback (purge by URL list); a staging `robots.txt Disallow: /` or `noindex` header riding into the production build; a sitemap prerendered at build time on a box with no database, listing zero product URLs (check `sitemap.xml` entry counts after every deploy); www/non-www or HTTPS canonicalisation adding a second hop; internal links still paying a redirect on every click.

**Make "no internal redirects" a CI gate** `[practitioner]`: `JustinBeckwith/linkinator` with `--recurse --check-fragments --redirects error --require-https error` fails the build on any internal redirect (its fragment checks see server-rendered HTML only); the deploy-gate row is in [seo-drift-monitoring.md](seo-drift-monitoring.md#deploy-gates).

## Consolidation

Two MAINSTREAM entries, both all before/after:

- **Entry #18 — Redirect duplicate landing pages to primary URLs** `[measured: MAINSTREAM, n=4 samples across 4 publishers, c=0 controlled]` — **+110% organic sessions** (median), range +60% to +200%; sample sizes 1 page to 512 pages (thestacc.com 2026, +18%). Several changes, one measurement — the primary pages were also rewritten to absorb the duplicates' content.
- **Entry #19 — Consolidate repetitive pages into detailed hubs** `[measured: MAINSTREAM, n=6 samples across 6 publishers, c=0 controlled]` — **+74% conversions** (median), range +50% to +82%; the figure is located in source on 2 of 6 samples; sample sizes 1 URL to 87 merged pages. Bundle: merge + rewrite + regional detail + redirects. Direction, not size.

**Diagnose before calling it cannibalisation** `[practitioner]` — skill `seo-content` › gsc-page2-audit § 3 carries the class check. Two pages sharing queries are cannibalising only if they target the *same intent* and Google alternates between them for the same query set; pages on one topic serving different intents (compare vs how-to, national vs município) are complementary and merging them loses one intent. Pull query overlap by page from GSC over 28 days and read the SERPs for the shared queries.

**Refresh or consolidate — the decision tree:**

1. Does the page have its own intent and its own query set? → **Refresh** (facts, sections; skill `seo-content` › content-and-intent-2 § Content refresh workflow); do not merge.
2. Same intent as a stronger page, and it still earns clicks? → **Consolidate into the stronger page**: move any unique content across, 301 the retired URL to the survivor, update internal links to point at the survivor directly.
3. Same intent, no clicks, no links, no unique content? → **Retire**: 301 to the closest parent that serves the intent, or 410 if there is none. Never redirect to the home page by default.
4. Many thin pages on one theme with no single strong survivor? → **Hub** (#19's shape): one detailed page, 301s from every retired URL, and real distinct detail on whatever stays separate.

**Retire with 301, and keep the redirect map versioned** `[practitioner]`: the map is code, lives in the repo, is reviewed like code, and every entry records date, reason and the ticket. A redirect map nobody can diff is a migration nobody can roll back.

## Canonicals and indexation repair

- **Entry #16 — Set canonical tags on duplicate product pages — MAINSTREAM** `[measured: MAINSTREAM, n=4 samples across 4 publishers, c=0 controlled]` — **+178% organic sessions** (median), range +150% to +210.5%; netpeak.us 2024 (1 site, +178%, a 7-month marketplace programme), loopexdigital.com and shopifyproservices.com 2026 (847 URLs) direction only. All before/after. Repairing self-inflicted duplication is the most defensible indexation work there is; the size still belongs to those sites.
- **Entry #17 — Point main product canonicals to variant URLs — EXPERIMENTAL** `[measured: EXPERIMENTAL, n=2 samples, c=2 controlled, both searchpilot.com (2024 +22% organic sessions; 2025 direction only)]`. The study: "nobody outside these 2 tests has replicated it, and both came from one publisher — a hypothesis worth your own test, not advice." Do not copy it blind; canonicals follow actual equivalence and where the demand lands, not a case study.
- **Entry #81 — Remove duplicate copy and resolve feed errors — MAINSTREAM** `[measured: MAINSTREAM, n=9 samples across 7 publishers, c=0 controlled]` — **+120.7% conversions** (median), range +24% to +365.4%; bundle (delete or canonicalise duplicates, fix merchant-feed validation, add body copy, publish reviews).
- **Entry #82 — Remove misplaced noindex tags and fix crawl errors — MAINSTREAM** `[measured: MAINSTREAM, n=4 samples across 4 publishers, c=0 controlled]` — **+24% conversions**, one sample carries the figure, 3 of 4 same direction; bundle (noindex removal + canonical rewrites + restoring error pages + broken links).
- **Entry #80 — Serve missing status headers instead of gone — EXPERIMENTAL** `[measured: EXPERIMENTAL, n=1 sample, c=1 controlled, rebootonline.com 2022, 119 pages]` — **+49.6% indexed pages** by serving 404 instead of 410 on removed test pages. One team, one test. Carry the mechanism question if you like; **never falsify a resource's status to inflate an indexed count** — an indexed page that no longer exists is a soft-404 waiting to be reclassified, and indexed count is not a business metric.
- **Entry #100 — Bypass internal link redirects and set canonicals — EXPERIMENTAL** `[measured: EXPERIMENTAL, n=2 samples across 2 publishers, c=1 controlled]` — **+31% revenue** (moz.com 2015, 1 site, before/after); the controlled test (searchpilot.com 2023, size not reported) is **direction only, and the two samples point in different directions (1 of 2 same direction, agreement 0.50)**. Pointing internal links at the final URL is still right hygiene `[practitioner]`; it is not a revenue lever with a number.

**Three different controls, three different jobs** — Google discourages `noindex` for canonical choice and robots.txt for canonicalization (disallowed URLs may still be indexed without their content) `[documented: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls, 2026-10-12]`; a disallowed URL's `noindex` is never read `[documented: https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag, 2026-10-11]`; `noindex` URLs are still requested, so they do not save crawl budget `[documented: https://developers.google.com/crawling/docs/crawl-budget, 2026-10-12]`:

| You want… | Control | Not this |
|---|---|---|
| Duplicates to consolidate signals into one preferred URL that stays indexable | `rel=canonical` (plus 301 where the duplicate need not exist) | `noindex` to force canonical selection — Google discourages it |
| A URL crawled but kept out of the index | `noindex` (meta or header), URL must remain crawlable | `Disallow` in robots.txt — a blocked URL cannot have its `noindex` read, and can still be indexed from links |
| Crawl budget kept off worthless URL spaces | robots `Disallow`, parameter handling, fewer generated links | `canonical` or `noindex` (the crawler still has to fetch them) |

**Never `Disallow` a URL you want noindexed.** And parameter syntax alone does not decide indexability: include the intended indexable canonical set in the sitemap whatever the URL looks like, and exclude the non-canonical set whatever it looks like.

## Links: disavow and recovery

**Entry #13 — Submit disavowal files for identified spam links — IT DEPENDS** `[measured: IT DEPENDS, n=3 samples, c=0 controlled on both sides]`. Sides: **+80% organic sessions** for a site recovering from an active manual link penalty (seoworks.com 2026, 1 site, before/after, no control — and a bundle: webmaster outreach + disavow + reconsideration request, so the study says "take the direction and not the size") versus **direction only** for sites disavowing proactively without a penalty (zyppy.com 2024 and 2016, 1 site each). Moderator: *does your website currently have an active manual link penalty?* Evidence 38.3. The study's own limit: an uncontrolled case on a penalised site cannot separate disavowal from penalty removal.

**Google's stated scope for disavow** `[documented: https://support.google.com/webmasters/answer/2648487, 2026-10-11]`: for sites with a considerable number of spammy, artificial or low-quality links *and* those links have caused, or are likely to cause, a manual action. That is the whole use case. Outside it, the tool's own help page says most sites do not need it.

Operating rules `[practitioner]`:

- **Vendor "toxicity" scores are not evidence.** They are a vendor's heuristic over a vendor's crawl; nothing in the study or in Google's documentation ties them to a ranking outcome. Uploading a disavow on the strength of one is an uncontrolled change to a signal you cannot measure back.
- Disavow only when both hold: a considerable number of spammy, artificial or low-quality links point to the site, *and* they have caused, or likely will cause, a manual action for unnatural links; try removal first `[documented: https://support.google.com/webmasters/answer/2648487, 2026-10-11]`. A paid or link-scheme campaign in the site's own history qualifies only when it meets both conditions.
- If a manual action exists: export links, remove what can be removed, disavow the remainder at domain level, file a reconsideration request that documents the work, keep everything else on the site fixed during review (the study's #13 recipe), and track sessions monthly against the 90-day pre-penalty baseline.
- Bundled recoveries (#14 in the catalogue, disavow + on-page, +65% sessions MAINSTREAM) do not isolate disavow; credit the bundle.

## Core-update and HCU-class recoveries

`[practitioner]` throughout — the published record has no controlled evidence on recovering from a core update, and the honest reading of the case studies is that they describe sites that did many things and then rose at a later update.

- **There is no single fix.** A core update re-weights quality judgments across the site; a template that lost is a template whose pages now compare worse against what ranks. Nothing in a disavow file, a schema block or a date bump addresses that.
- **Audit per template** for: does the page deliver the value its title promises; does it match the dominant intent of the queries it lost; on YMYL surfaces, is the trust surface present (who wrote it, who reviewed it, effective date, sources, a methodology page, a corrections log). Compare the losing template against the three URLs that now outrank it on its top ten lost queries.
- **Consolidate thin sections** rather than refreshing each thin page — this is where #19's shape applies, with the same "direction, not size" caveat.
- **Measure continuously; the next core update is one more checkpoint.** Google: «some changes can take effect in a few days», others take months, and «you don't necessarily have to wait for a major core update» `[documented: https://developers.google.com/search/docs/appearance/core-updates, 2026-10-14]`. Compare changed templates with unchanged controls; keep the baseline and change log so any movement can be attributed.
- **Document what changed and when** — the attribution log in skill `seo-evidence` › experiments-and-revert-2. A recovery you cannot describe is one you cannot repeat.

## Rollback playbook

| Change class | Rollback trigger (pre-declared) | Rollback action | What to keep |
|---|---|---|---|
| Deploy / rendering failure (shell HTML, accidental `noindex`/`Disallow`, off-site canonical, redirect loop, 5xx) | Immediate, any confirmed instance | Redeploy previous image; purge CDN by URL list; re-run URL Inspection live on three URLs | Incident note with the header/HTML seen; the check added to deploy pre-flight |
| Wrong financial / regulatory output (YMYL) | Immediate, any confirmed instance | Revert engine or copy; publish a correction; pause SEO measurement on that template | The public correction entry; the fixture proving the fix |
| Title / meta template test | Arm B below arm A past the band at p<0.05; or Google rewrites the treated title on >50% of sampled queries; or leads fall | Restore arm A pattern on arm B | Attribution row with verdict; arm list; SERP samples |
| Internal-link change | Treated clicks fall >15% vs control over 4 consecutive weeks, mechanism confirmed | Remove the added links; leave control untouched | Crawl-depth export before/after; donor-page read |
| URL / slug rename (#174) | Treated sessions fall vs matched control over 60 days | Restore original paths; 301 new → old; relink; resubmit sitemap | The versioned redirect map; why the rename was tried |
| Consolidation / retirement (#18, #19) | Survivor does not absorb the retired query set in the window; or a merged intent leaves the SERPs | Restore the retired page at its URL, remove the 301, relink | Redirect map with dates; the query-overlap analysis |
| Canonical repair (#16, #17) | Google-selected canonical diverges from declared; indexed count of the intended set falls | Restore prior canonicals; re-inspect a sample | Declared vs Google-selected list, before and after |
| Domain / platform migration (#133) | Template clicks below band beyond the window (default 8–12 weeks), not explained by a listed update or demand | Restore old host from the frozen inventory; reverse 301s; withdraw change of address | Both GSC properties; URL inventory; redirect-test and parity reports |
| Disavow upload (#13) | Sessions keep falling after penalty resolution (the study's own revert line) | Edit or remove the disavow file (removal is not instant) | Link export; reconsideration record |

Trigger, window and owner are written before the change ships (skill `seo-evidence` › experiments-and-revert-2 § Revert triggers); a human confirms mechanism before executing the performance rows, and executes the immediate rows first and diagnoses after.

Cross-references: skill `seo-evidence` › experiments-and-revert-2 (designs, MDE/power, verdict states, attribution log), skill `seo-evidence` › evidence-and-tactics-1 (marks and denominators for every entry cited), `crawl-and-index.md` (crawlability, indexability, canonicals), `rendering-and-sitemaps-2.md` (sitemap, JS rendering), skill `seo-content` › gsc-page2-audit § 3 (cannibalisation class check), skill `seo-authority` › authority-links-and-pr (link acquisition and the EEA site-reputation note), `SKILL.md` (hard refusals and decision rules).

## Sources

- JustinBeckwith/linkinator@README.md (phase-2 adapted file research/adapted/group-E__readme-tool-repos/tool-stack-by-job.md) — the no-internal-redirect gate flags and the server-rendered-only fragment limit. INTEGRATE, MIT.
