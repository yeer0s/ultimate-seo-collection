<!-- split-header-2: part 2 of 2 of gsc-page2-audit.md (original lines 199–324; boundary H2) -->
# GSC page-2 audit (2 of 2) — page audit, the three above you, AI queries, output contract
## Contents

- 4. Page audit — what actually turns up
- Diagnose against the three above you
- 5. AI-assistant queries are visible in GSC
- 6. Output contract
- Sources

Other parts of the same original file: [gsc-page2-audit.md](gsc-page2-audit.md).

<!-- /split-header-2 -->
## 4. Page audit — what actually turns up

Fetch each ranking page's title/meta/canonical/H1/H2 verbatim (raw HTML regex on the
SSR output; a markdown-converting fetcher can drop head tags). On a site whose
metadata hygiene is already good, the naive "keyword missing from title" fix is rare.
What recurs instead — the working diagnosis taxonomy (one chip per row):

- **Metadata/snippet** — title/meta present but *generic or verdict-free* while the
  SERP is brand-dominated. Fix = concrete numbers (live price, count, date) and a
  verdict in the meta. Dynamic figures must come from the live data layer, never
  hardcoded into a template.
- **Word-form/spelling** — page says "Contas Bancárias", demand says "comparar
  bancos"; page says "Q2", searchers type "2.º trimestre"; "novobanco" vs "novo
  banco". Cheapest fixes on the list.
- **Intent mismatch** — measured demand for a *neighbouring* question hitting the
  wrong page (e.g. "reembolso X" queries landing on a "cancelar X" page at pos 40).
  Fix = a dedicated page for the measured intent, not tweaks to the wrong page.
- **Cannibalization** — see §3.
- **Content depth / authority** — on-page already done; ranking gap is domain-level.
  Say that plainly instead of inventing a tweak. Head terms at pos 70+ belong here.
- **Wrong language/geo** — impressions in another language (e.g. FR/EN queries on a
  PT-only site) inflate a page's "opportunity". Not a win unless a locale strategy
  exists; label and move on.
- **Zero-click query class** — date/deadline queries ("prazo X 2026") resolve in the
  SERP. Answer-first titles win the snippet + brand impression; the click was never
  coming. Score these accordingly.

**Claim-safety gate on every proposed title/meta:** superlatives ("mais barato",
"melhor") only where the site's data layer substantiates them live, and only within
the project's approved-claims rules. A CTR fix that ships an unprovable claim is a
regression, not a win.

## Diagnose against the three above you

`[practitioner]` For a striking-distance page, take the three results ranking directly
above it and write down, for each, the concrete reason it wins. It is usually one of:

- **Intent match** — it answers the question asked; ours answers a neighbouring one (a
  price query met by a features page loses).
- **Missing section** — a sub-question we skip; PAA and the top results' subheads
  reveal it.
- **Freshness** — their figures, year or screenshots are current.
- **Format** — they carry the table, steps or calculator the query wants.
- **Links** — more and stronger internal and external links point at them.

**No nameable reason → no rewrite.** The gap is then more likely authority than
on-page, and the work is internal links from strong pages plus earned links, not copy.

**Cannibalisation comes first.** If two of our URLs alternate on the query, run the
class check in [gsc-page2-audit.md](gsc-page2-audit.md) §3 first. Consolidate only when
both serve the same intent and the class is a real split (not owned SERP slots, a
parameter or dated-series split); then choose one owner, fold in the useful parts of the other, 301 it
(skill `seo-technical` › migrations-and-recovery), and only then push. A comparison page
and a how-to guide sharing a query serve different tasks: keep both and sharpen each.

**Make the smallest change that closes the named gap.** Add the missing section
instead of rewriting a page that already ranks; answer the query in the opening two
sentences; add descriptive in-body links from our strongest related pages (often the
biggest and most neglected lever); update stale facts. When the problem is CTR only,
change **title and description and nothing else**, so the effect can be attributed.
One change set per URL per measurement window, read with skill `seo-evidence` ›
experiments-and-revert-2.

**Stop rule** `[practitioner]`: after two rounds of changes with no movement in
position, stop editing. The limit is either intent mismatch (the SERP wants a
different page type — see [page-types-and-serp-clustering.md](page-types-and-serp-clustering.md))
or authority, and neither yields to more on-page work. Put the page on the report's
honesty list.

### New-page launch checklist

`[practitioner]`

- [ ] In-body links from at least 3 relevant existing pages, descriptive anchors (a
      floor against orphaning, not a quota)
- [ ] A unique title and description for the target query; one H1 aligned with the title
- [ ] Self-referencing canonical; listed in the XML sitemap; indexable (no stray
      noindex, not disallowed)
- [ ] Main content present in the server-rendered HTML
- [ ] Structured data only where the type is supported (skill `seo-technical` › schema-reference)
- [ ] Linked into the conversion path
- [ ] Request indexing once in GSC (repeating the request does nothing); submit via
      IndexNow for Bing. Still not indexed after a few weeks → run the indexation
      diagnosis instead of resubmitting.

## 5. AI-assistant queries are visible in GSC

Long conversational queries — including literal leaked prompt fragments like
`context: location: portugal … question: qual é o melhor pacote…` — show up in the
query report. AI Overviews and AI Mode may use a query fan-out technique (several related searches per response)
`[documented: https://developers.google.com/search/docs/appearance/ai-features, 2026-10-11]`.
Reading a given prompt-shaped row as that fan-out retrieving the site is a
`[hypothesis]`: a human can paste the same prompt into Search, and GSC does not say
which happened. Report such rows as "prompt-shaped queries", not as AI retrievals, unless other
evidence corroborates it. Treat multi-brand comparison questions as a
structural signal: a pairwise X-vs-Y page can't serve a 4-brand question — route
those to a roundup/"best" page via internal links.

## 6. Output contract

Dashboard/report rows: query (or page), ranking page, impressions, clicks, position,
est. gain (labeled as planning number), diagnosis chip. A small position scale with a
page-1 threshold marker reads faster than a number. Then fixes ordered by return,
each with the **exact before/after** (title tag, meta, H1, the H2 to add, which URL
301s where) — "improve the title" is not a deliverable. Close with the honesty list:
pages where on-page is done and the real constraint is depth/authority, so the reader
gets five real fixes instead of ten padded ones.

Wire the follow-up: re-measure the touched URLs after 14–28 matched days using the
post-change impact rules in the main skill (separate position and CTR verdicts;
CTR needs clicks, not impressions).

Additions to the contract `[practitioner]`:

- **Cap priority actions at 3–5**, each with its URL, the metric evidence and the exact
  fix. Any impact figure is a planning number derived from this site's own impressions (§2);
  a generic CTR curve must never be passed off as a forecast.
- **Audit history table** on every repeat audit: each previously flagged item →
  `resolved` / `improved` / `still present` / `worsened`, with its current metric.
  After every audit, store the top issues with date, page, metric and type so the
  next run can fill this table.
- **"What we saw and deliberately ignored"**: two or three one-liners, so the reader
  knows a signal was noticed and consciously deprioritised.
- **Segment split** in the totals: branded vs non-branded (§3a), and any segment flag
  raised in §3b.

## Sources

- AminForou/mcp-gsc@gsc_server.py (lines 85-104, 252-305, 463-530, 1027-1190, 1192-1335), skills/{cannibalization-check,content-opportunities,indexing-audit,seo-weekly-report}/SKILL.md, CLAUDE.md (phase-2 adapted file research/adapted/AminForou__mcp-gsc/gsc-mcp-tool-surface-and-recipe-guards.md) — Agent / MCP access: tool contract, data-state trap, four recipe guards, keep-list. INTEGRATE, MIT.
- nowork-studio/notfair-plugin@seo/seo-analysis/WORKFLOW.md (Phases 3, 3.5, 3.6, 4, 4.5, 6) (phase-2 adapted file research/adapted/nowork-studio__notfair-plugin/gsc-audit-segments-and-inspection.md) — §§ 3a–3e, the owned-SERP-slots exception in §3, output-contract additions. INTEGRATE, MIT.
- coreyhaines31/marketingskills@skills/seo-audit/references/rankings-push.md (phase-2 adapted file research/adapted/coreyhaines31__marketingskills/striking-distance-push-and-launch-checklist.md) — Diagnose against the three above you, smallest change, stop rule, new-page launch checklist; the fetch caveat goes to another skill. INTEGRATE, MIT.
- research/REPORT.md §7 idea 5 — audit any connector before trusting it.
