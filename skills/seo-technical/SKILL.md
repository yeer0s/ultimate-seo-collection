---
name: seo-technical
description: >-
  Audits and fixes technical search visibility: robots.txt, indexing, canonicals, redirects, JavaScript rendering, structured data, Core Web Vitals, sitemaps and IndexNow, hreflang, migrations and traffic-loss triage, deploy-drift gates, live-site inspection, Search Console and CrUX APIs. Use for "not indexed", "wrong canonical", "add schema", "fix hreflang", "traffic dropped". Not for what content to write (seo-content).
---

# seo-technical

Can every engine fetch, render, index and correctly attribute the page — and does it stay that way after each deploy?

<!-- grammar-excerpt -->
Label every tactic with one of the 9 marks: `[documented: <URL>, <date>]` · `[documented-secondary: …]` · `[unverified: …]` · `[measured: MARK, n=S, c=C]` · `[practitioner: anonymised sources · …]` · `[hypothesis]` · `[vendor]` · `[memory]` · `[unvalidated house heuristic]`.
Numbers keep their denominator; marks are counts, not verdicts; bundles support direction, not size.
Never forecast a published number onto a client site; only the client's own GSC demand and funnel forecast.
No rollout without a pre-declared revert rule (applicability, holdout, what stays fixed, metric + window, trigger).
Repetition never proves; full grammar: skill `seo-optimizer` § Evidence marks.
<!-- /grammar-excerpt -->

## Load rule

Open one reference per load-when row the question touches (a "by H2" row: only the part holding that H2); never a file "to be thorough". A pointer into another seo- skill's file is a citation: quote it, or first load that skill's SKILL.md and open the file through its own load-when row. Engine pages, ledger and practitioner parts and the crawler registry are lookup-only.

## Load when

| ID | Question shape | Open |
|---|---|---|
| TE1 | crawl, index, robots.txt, canonicals, redirects | [crawl-and-index.md](references/crawl-and-index.md) |
| TE2 | JS rendering, sitemaps, IndexNow, bot/user parity | by H2: [part 2](references/rendering-and-sitemaps-2.md) (sitemaps, IndexNow, JS rendering, audit checklist) or [part 1](references/rendering-and-sitemaps.md) (JSON-LD, CWV bar, hreflang tags) |
| TE3 | structured data | [schema-reference.md](references/schema-reference.md) |
| TE4 | Core Web Vitals diagnosis | [cwv-field-lab-diagnosis.md](references/cwv-field-lab-diagnosis.md) |
| TE5 | LCP subparts, images, sitemap extensions | by H2: [part 1](references/performance-images-and-sitemaps-1.md) (LCP, images) or [part 2](references/performance-images-and-sitemaps-2.md) (sitemap extensions, agent-friendly pages) |
| TE6 | traffic loss, incident classification | [incident-triage.md](references/incident-triage.md); then skill `seo-engine-policies` › google-updates-timeline-2 (core/spam rollout dates) and, to rule decay in or out, skill `seo-content` › content-and-intent-2 (decay triage) |
| TE7 | migrations, URL changes, consolidation, rollback | [migrations-and-recovery.md](references/migrations-and-recovery.md) |
| TE8 | hreflang, locales | by H2: [part 1](references/international-and-hreflang.md) (MT and scaled content, geo signals, formats) or [part 2](references/international-and-hreflang-2.md) (scale, frameworks, Bing/Yandex, locale release gates) |
| TE9 | deploy drift, CI gates | [seo-drift-monitoring.md](references/seo-drift-monitoring.md) |
| TE10 | Search Console / CrUX APIs, quotas | by H2: [part 1](references/google-apis-and-quotas.md) (query shapes, URL Inspection, Indexing, GA4, Consent Mode, CrUX) or [part 2](references/google-apis-and-quotas-2.md) (quota table, Keyword Planner, auth) |
| TE11 | live-site inspection | [site-inspection-method.md](references/site-inspection-method.md) |

## Not mine

| Question | Skill |
|---|---|
| is a tactic allowed by an engine | `seo-engine-policies` |
| does schema or a title change work | `seo-evidence` |
| AI crawler access as a citation strategy | `seo-ai-search` |
| what pages to build | `seo-content` |

## Rules

1. Index status comes from Search Console URL Inspection, never from `site:`.
2. Never `Disallow` a URL you want noindexed — the crawler must fetch it to read the tag.
3. Classify an incident (deploy, core update, manual action, demand, tracking) before treating it.
4. Server HTML must carry everything that must rank or be cited.
5. Every redirect, canonical or template change ships with a revert rule and a re-crawl check.
6. A schema request that also promises AI citations or a ranking tactic stays here (TE3) plus skill `seo-evidence` › works-vs-doesnt for the claim; it does not need `seo-ai-search`.
