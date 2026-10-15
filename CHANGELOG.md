# Changelog

All notable changes to the Ultimate SEO Collection. Versions follow [Semantic Versioning](https://semver.org/).

## [1.1.0] — 2026-10-15

### Added
- **Competitive-landscape research protocol** in `seo-optimizer` (route row OP3). A repeatable,
  multi-agent study of every competitor in a market: pinned inputs, discovery by cluster,
  gap-closing and fact-check rounds at primary sources, real-browser checks of regulator registers,
  search / traffic / backlink / paid-media / AI-citation dimensions, and a saturation stop rule.
  Output contract: one profile per firm, vertical and dimension files, CSV matrices, sources, gaps,
  a two-page snapshot and a self-contained HTML dashboard.
  - `references/competitive-landscape-research.md` — the protocol (phases P0–P10, operating rules,
    output design, dimension checklist, safety rules, hand-offs to the seo- subskills).
  - `references/competitive-landscape-agent-prompts.md`, `-templates.md`, `-methods.md`,
    `-market-pack-example.md` — opened only for the phase that needs them.
  - `scripts/merge_rows.py` and `scripts/build_dashboard.py` + `scripts/dashboard_template.html`
    (Python standard library, no network calls).
- Eval case **E33** and routing probe **R17** for the new route.

### Changed
- `seo-optimizer` description and router: competitor and landscape questions now route to OP3.
- Research findings keep their own claim tags inside the study pack and take the collection's
  evidence labels when they become SEO recommendations; a competitor's traffic-panel figure is
  `[vendor]` and is never forecast onto your own site.

## [1.0.1] — 2026-10-14

### Changed
- Practitioner evidence now cites anonymised sources only.

## [1.0.0] — 2026-10

### Added
- First public release: eight skills (router + seven specialists), engine policy pages for
  11 search and AI engines, the 87-play spam-defence catalogue, and a 32-case eval set.
