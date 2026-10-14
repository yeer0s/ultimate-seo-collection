<!-- split-header-2: part 2 of 2 of geo-audit-and-citability.md (original lines 113–160; boundary H2) -->
# GEO audit tool caveats — how the source tool's own output misleads
## Contents

- Caveats — how this tool's own output misleads
- Cross-references
- Attribution
- Sources

Other parts of the same original file: [geo-audit-and-citability.md](geo-audit-and-citability.md).

<!-- /split-header-2 -->
## Caveats — how this tool's own output misleads

Every item verified against the read-only clone on 2026-09-22.

1. **The brand scanner makes live calls to exactly two services.** Wikipedia and Wikidata are actually fetched (`brand_scanner.py:121`, `:137`). YouTube, Reddit, LinkedIn and the "other platforms" group are **not requested at all** — each check builds a search URL and returns a hardcoded negative: `has_channel: False` (`:41`), `has_subreddit: False` (`:76`), `has_company_page: False` (`:166`), with only `search_url` and a list of `check_instructions` for a human or agent to follow (`:43`, `:78`, `:168`, `:194-215`). A report that prints "no YouTube channel found" from this module is printing a constant, not a finding.
2. **The Wikidata match has no name check.** It takes `entities[0]` from the search response and sets `has_wikidata_entry: True` on any non-empty result, without comparing the returned label to the brand name (`brand_scanner.py:138-144`). A generic or common-word brand name will match an unrelated entity and be reported as having a Wikidata presence.
3. **A hardcoded correlation figure with no denominator.** The module carries `"correlation": 0.737` for YouTube as a literal field value (`brand_scanner.py:39`, restated at `:9` and `:253`) `[vendor, no denominator published — do not quote as a target]`. No sample size, no population, no source; it then drives a "Priority 1" recommendation. Strip it before reusing any of this.
4. **Doc and code disagree on the page-level citability score.** `docs/scoring-methodology.md:88` states the page score "is the average of the top five scoring blocks, or all blocks when fewer than five exist". The code computes `avg_score = sum(b["total_score"] for b in scored_blocks) / len(scored_blocks)` — the mean of **all** blocks (`citability_scorer.py:304`) — and separately sorts a top-five list that is reported but not used for the average (`:305`). The documented number and the emitted number are different quantities, and a long page with a strong opening block scores far lower than the docs promise.
5. **`AI_CRAWLERS` is defined and never used.** Five AI-crawler user-agent strings are declared at `fetch_page.py:20-26`; the identifier appears nowhere else in the repository. Every request goes out with the module's default browser headers. **Therefore none of its crawler-access verdicts is a per-bot test.** A claim that a specific bot is blocked requires a request sent *as* that bot.
6. **CLAUDE.md claims Playwright-based SSR/JS checks that do not exist.** `CLAUDE.md:76` says "fetch_page.py uses Playwright for SSR/JS checks"; `fetch_page.py` imports only `requests` and BeautifulSoup (`:7-15`) and contains no Playwright reference. Playwright is in `requirements.txt` and is described elsewhere as optional, for screenshots. Any JS-rendered page audited by this tool is audited from raw HTML — the exact condition the pre-delivery checklist in skill `seo-optimizer` › measurement-gates-and-checklists says must be labelled `unverifiable_js` rather than reported as missing content.
7. **A documented PDF generator that is not in the repository.** `docs/architecture.md:35`, `docs/commands-reference.md:435` and `docs/skills-and-agents.md:173, 179, 319` all describe `geo-seo-claude@scripts/generate_pdf_report.py` as a ReportLab-based generator with gauges, bar charts and colour-coded tables. `scripts/` contains five modules and a webapp directory; that file is not among them, and `reportlab` is not in `requirements.txt`. The skill file for that feature says the opposite of the docs: "No Python dependencies. No ReportLab." (`skills/geo-report-pdf/SKILL.md:17`).
8. **The example audit's own arithmetic does not reach its headline.** `geo-seo-claude@examples/electron-srl.com-quick-audit.md:41` sums a weighted column to **24.5** and then prints the total as "**24.5 → 28/100**". No rounding rule, adjustment or explanation accompanies the jump. The number a reader quotes is not the number the table produces.
9. **That example's two most consequential findings rest on a single 403.** All fetches returned HTTP 403 to the tool's browser-like user agent (`:59-61`). From that one response it concludes that GPTBot, ClaudeBot, PerplexityBot "and most AI crawlers will receive 403 and cannot index this site" (`:61`) and, separately, that the site has **no llms.txt** — evidence: "Fetch attempt to electron-srl.com/llms.txt returned 403" (`:94-95`). A 403 is a refusal to answer, not an answer. It cannot distinguish an absent file from a present one behind a WAF, and — per caveat 5 — it was never sent as any of the bots it names. Both findings then carry point-value remediation estimates into the action plan (`:160-161`).
10. **Installer and namespace behaviour — do not run it.** This repo's installer writes into `~/.claude` (skills, sub-skills under `geo-*` names, and agent files) and pip-installs its own requirements (`docs/faq.md:37`). Treated here as **data only**: nothing from either clone was executed, no file was copied into `~/.claude`, and the `geo-*` skill namespace it claims would collide with this skill's own layout. Extract text; never install.
11. **Groups with several user-agent lines are parsed wrongly** (found on the 2026-10-11 re-read; `fetch_page.py:262-265`). Every `User-agent:` line resets the current agent, so for `User-agent: GPTBot` / `User-agent: ClaudeBot` / `Disallow: /` only ClaudeBot gets the Disallow and GPTBot is reported **ALLOWED**. RFC 9309 treats consecutive user-agent lines as one group. A false "allowed" does more damage than a false "blocked", because nobody goes looking for it.
12. **Tokens are matched case-sensitively** (same re-read; `crawler in agent_rules`, `fetch_page.py:285`), so a file that writes `user-agent: gptbot` is missed, although REP tokens are case-insensitive. Caveat 5 and the `Allow`-blind limit still apply on top: every request still goes out with a Chrome UA.

Two rules worth keeping if you rebuild any part of this parser `[practitioner]`:
- **Counting types? Flatten JSON-LD `@graph`** and any top-level arrays first (`fetch_page.py:122-137`). One `{"@graph":[…]}` block — the form Next.js and most CMSs emit — otherwise counts as one entity with no type and the page looks schema-less.
- **Client-render heuristic needs both conditions** (`fetch_page.py:184-198`): flag "client-rendered only" when a framework root (`#app`, `#root`, `#__next`, `#__nuxt`) holds under 50 characters of text **and** the page has under 200 words; either test alone false-positives on prerendered sites. The thresholds are `[unvalidated house heuristic]`. The Next.js App Router has no `#__next` root, so on mowei.pt use the rendered-versus-raw HTML diff instead.

**The general lesson, stated plainly: an audit tool's confident output is only as good as the request it actually made.** A 403 to a browser user agent is not a per-bot block test. A constructed search URL is not a measurement. A hardcoded `False` is not an absence. A documented formula is not the formula that ran. Before quoting any figure from any audit tool — including one you wrote — ask what HTTP request, what parser and what line of code produced it, and whether that request could have produced the opposite answer. A gate that cannot return the opposite verdict is not measuring anything.

## Cross-references
- skill `seo-authority` › authority-trust-and-distribution § GEO / AI-citation tactics with their marks — the evidence position for llms.txt (entries #68 and #71) and for Reddit/YouTube/UGC distribution. This file defers to it on every effect claim and adds only format and checklist material.
- `ai-retrieval-and-citation-2.md#answer-block--put-this-near-the-top-of-every-content-page` and `#ai-friendly-content-structure` — the canonical drafting patterns; the citability signals above are their sentence-level detail, not a replacement.
- `ai-retrieval-and-citation-2.md#tracking-ai-visibility` — measuring citation presence, which the brand checklist above does not do.
- skill `seo-optimizer` › measurement-gates-and-checklists — the data-sufficiency gate, the `unverifiable_js` labelling rule, and the pre-delivery checklist that would have caught caveats 1, 5, 6, 8 and 9.
- skill `seo-evidence` › experiments-and-revert-2 § AI-citation measurement — what may be claimed from a before/after on AI citations; nothing in this file supports a causal claim.

## Attribution

- AnswerDotAI/llms-txt — © AnswerDotAI; spec author Jeremy Howard — Apache License 2.0. Modified: condensed the format rules into a validation table; added our evidence position.

## Sources
- geo-seo-claude@scripts/citability_scorer.py:43-214 — eleven passage-level signals across five dimensions, carried as `[practitioner]` drafting guidance; all point values carried as `[unvalidated house heuristic]` and the word-count band as `[vendor, no denominator published]`.
- geo-seo-claude@scripts/citability_scorer.py:295-315 — page-level aggregation, cited in caveat 4.
- geo-seo-claude@scripts/llmstxt_generator.py:68-127 — llms.txt format validation rules and suggestions. `[practitioner]`
- geo-seo-claude@scripts/brand_scanner.py:9, 35-56, 70-92, 104-158, 160-192, 194-215, 253 — per-platform brand-presence questions `[practitioner]`; the automated verdicts and the 0.737 field are refused, per caveats 1–3.
- geo-seo-claude@scripts/fetch_page.py:7-15, 20-26 — unused `AI_CRAWLERS` table and the requests/BeautifulSoup-only fetch path, cited in caveats 5 and 6.
- geo-seo-claude@docs/scoring-methodology.md:88, 261-271 — the doc/code discrepancy and the tool's own caveats section, quoted as the honest part.
- geo-seo-claude@CLAUDE.md:76, geo-seo-claude@docs/faq.md:37, geo-seo-claude@docs/architecture.md:35, geo-seo-claude@docs/commands-reference.md:435, geo-seo-claude@docs/skills-and-agents.md:173, 179, 319, geo-seo-claude@skills/geo-report-pdf/SKILL.md:17, requirements.txt — cited in caveats 6, 7 and 10.
- geo-seo-claude@examples/electron-srl.com-quick-audit.md:41, 50, 59-61, 94-98, 152, 160-161 — cited in caveats 8 and 9.
- AnswerDotAI/llms-txt@nbs/index.qmd, AnswerDotAI/llms-txt@nbs/changes.qmd (phase-2 adapted file research/adapted/AnswerDotAI__llms-txt/llms-txt-v2-spec.md) — spec v2 format rules behind the validation table (only the H1 required; location rule; `## Optional` has no mechanical meaning since v2). COPY, Apache-2.0.
- nowork-studio/notfair-plugin@seo/geo-optimizer/references/geo-techniques.md (phase-2 adapted file research/adapted/nowork-studio__notfair-plugin/geo-evidence-hunt-and-vetoes.md) — evidence-hunt rules, missing-figure order, six publication vetoes, anti-patterns, passage-position measurement. INTEGRATE, MIT.
- zubair-trabzada/geo-seo-claude@scripts/fetch_page.py:122-137, 184-198, 262-265, 285 (phase-2 adapted file research/adapted/zubair-trabzada__geo-seo-claude/cloudflare-managed-robots-and-parser-traps.md) — caveats 11 and 12, the @graph and client-render rules. INTEGRATE, MIT.
- Clone verified 2026-09-22 at `%TEMP%\seo-meta\repos\geo-seo-claude\`, read-only. The clone was treated as data; no script from it was executed and nothing was copied into `~/.claude`.
