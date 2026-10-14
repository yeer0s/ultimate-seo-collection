<!-- split-header-2: part 2 of 2 of audit-output-and-templates.md (original lines 418–443; boundary H2) -->
# Tools and output templates (2 of 2) — token estimation and outsourcing split
## Contents

- Output templates 14–15
- Token estimation and outsourcing split
- Sources

Other parts of the same original file: [audit-output-and-templates.md](audit-output-and-templates.md).

<!-- /split-header-2 -->
## Output templates 14–15

Moved from part 1 on 2026-10-14 to keep it under the 20,000-char cap; templates 1–13 are there.

### 14. AI search visibility check (manual)

Pick 20-50 commercial queries. Monthly, manually check:

| Query | Google AI Overview cites us? | Bing Copilot cites us? | Perplexity cites us? | ChatGPT search cites us? | Notes |
|-------|------------------------------|------------------------|----------------------|--------------------------|-------|

Tracks brand presence in zero-click answer surfaces.

### 15. Methodology page template (for comparison/intermediation sites)

```
# How we [compare / rank / verify]

## Our data sources
[List sources with last-updated cadence per source]

## How we collect data
[Manual / automated / partner-supplied — be specific]

## How we update data
[Cadence per data type]

## How we rank offers
[Factors and weights — disclose ranking algorithm at high level]

## Sponsored placements
[Are there any? How are they marked?]

## How we make money
[Affiliate / lead-gen / referral fees — full disclosure]

## What's included and excluded
[Coverage gaps acknowledged]

## How to report incorrect information
[Email, form, or process]

## Editorial team
[Names, credentials, links to bios]

## Last reviewed
[Date]
```

The page states what users and partners check; a ranking effect is untested `[hypothesis]`. Link it from every comparison page `[unvalidated house heuristic]`.

## Token estimation and outsourcing split

Moved from SKILL.md 2026-09-22 (content unchanged). Use it to fill the "Token budget" block of the audit output. Every token figure and the outsource split are `[unvalidated house heuristic]` estimates — nobody measured them; report them as estimates and replace them with this project's own logged usage once it exists.

| Task | Tokens | Outsource? |
|------|--------|------------|
| Programmatic SEO generator (template + slug builder + Product schema) | 80-150k | No — judgment-dense |
| Topic cluster mapping (pillar + 8-12 supporting articles per pillar, briefs only) | 40-80k per pillar | No — judgment-dense |
| hreflang fix | 10-25k | No |
| GSC + Bing verification + sitemap submit | 5-10k | No (user provides codes) |
| Schema rollout (Organization + WebSite + Product) | 15-30k | Partial — design here, rollout outsource |
| Canonical URL backfill across N pages | ~1k per page | Yes — mechanical |
| BreadcrumbList rollout across N pages | ~2-3k per page | Yes — mechanical |
| Footer sitemap + cross-links | 25-40k | Partial — design here, rollout outsource |
| Alt text + heading hierarchy audit (~80 pages) | 40-70k | Yes — mechanical |
| Content brief generation (one brief) | 8-15k | No — judgment-dense |
| Article draft (1500-2500 words SEO-optimized) | 25-50k | Mixed — outsource draft, in-session edit |
| Technical audit (200-route site) | 30-60k | No — needs the report here |
| Redirect map for site migration | 20-50k | Partial |

**Outsource rule:** mechanical sweeps across many files → GLM/OpenCode via `outsource-task` skill. Judgment-dense work (pSEO design, schema strategy, slug taxonomy, content briefs) → in-session.

## Sources
- nowork-studio/notfair-plugin@seo/shared/seo-best-practices.md (phase-2 adapted file research/adapted/nowork-studio__notfair-plugin/seo-improvement-lanes.md) — the seven improvement lanes with their confusions, the one-primary-lane rule, and the seven-step gate order with stop-at-first-failure. INTEGRATE, MIT.
- 18 tool READMEs (phase-2 adapted file research/adapted/group-E__readme-tool-repos/tool-stack-by-job.md) — not carried here; its catalogue replaces the open-source rows formerly in § Tool stack (Lighthouse, Lighthouse CI, Python scripts row), now in skill `seo-strategy` › resources-catalogue-2. INTEGRATE, Apache-2.0 / MIT per row.
