# Measuring AI citations

## Contents

- Scope
- Ladder, repeat runs, fan-out extraction
- Prompt families and source-type tally
- Measurement fields — framing and position of every mention
- Unverified
- Sources

## Scope

Open this file for "do ChatGPT, Perplexity or AI Overviews cite us", "why are we cited but never recommended", or "did the GEO work move anything". It assumes the bot can already read the page: proving access is in [ai-crawlers-and-bot-policy.md](ai-crawlers-and-bot-policy.md) (bot tokens) and [ai-crawlers-and-bot-policy-2.md](ai-crawlers-and-bot-policy-2.md#the-edge-gate-in-practice) (edge gate). What may be *claimed* from a before/after is governed by skill `seo-evidence` › experiments-and-revert-2.

## Ladder, repeat runs, fan-out extraction

### The visibility ladder — four rungs, never one "AI visibility" number `[practitioner]`

| Rung | Means | Governed by | Seen in |
|---|---|---|---|
| 1 Retrieved | Read while building the answer, not cited | Crawlability, parseable HTML, query relevance | Bot logs (hint only) |
| 2 Cited | Listed as a source | Usefulness of the passage: structure, sourced figures, freshness | Prompt tracking, AIO source list, Bing WMT AI Performance |
| 3 Mentioned | Brand named in the answer text | Entity recognition + what the web says | Prompt tracking |
| 4 Recommended | On the shortlist the buyer acts on | **Off-site consensus**: reviews, forums, analysts, press — largely independent of your own pages | Prompt tracking + the framing of the mention |

There is also a shadow rung, **recommended against**: on prompts heavy with requirements, engines list products to avoid and cite sources for it. That is why each mention's framing is logged (see the measurement fields below).

How to read it: when citations climb while the recommendation rate stays flat, the wider web is not yet backing up what your pages say. The fix is off-site, not another on-page edit.

**A self-ranked "best X" list can end up promoting rivals.** In one study of 100 B2B "best [category] software" queries, self-promotional listicles collected 323 AIO citations, and in 224 of them (69%) the answer recommended other brands `[vendor]` (Amsive/Lily Ray, spring 2026, 3 dates, observational, c=0). The suspected mechanism is that the engine treats your guide as a category source and then recommends from consensus `[hypothesis]`. The practitioner alternative: name the category leader first, state what it does well, then show where you differ `[practitioner]`. On a YMYL comparison platform this lines up with the fairness rules in skill `seo-content` › comparison-pages.

### Format volatility — a dated snapshot, not a rule

Share of ChatGPT citations by page type around the ChatGPT 5.6 release (Aug 2026) `[vendor]` (Peec AI via Rudzki/Ray, pre/post, c=0):

| Page type | Pre | Post | Change |
|---|---:|---:|---:|
| Listicles | 15.77% | 7.80% | −50.5% |
| Comparison / vs / alternatives | 9.08% | 6.17% | −32.1% |

In the same data, fan-out modifiers such as "vs / comparison / top / best / reviews" declined while `site:` and "official" grew. One reading is that retrieval shifted toward primary and owned sources once those formats had been mass-produced for GEO `[hypothesis]`. This was measured on ChatGPT alone; the absence of a reported demotion on other engines does not mean they are stable. In the same month practitioners reported Reddit almost disappearing as a ChatGPT citation source and owned sites making up roughly 60% of Gemini citations `[practitioner]` (counts unsourced).

What follows from it:

1. Never justify mass-producing listicles or comparison pages on the grounds that they win AI citations. Build comparison pages for human buyers and for Google, and count any AI citation as a by-product.
2. Owned "official" pages — methodology, pricing, product, original data — are the hedge that no retrieval change takes away.
3. Re-date any citation-share figure before quoting it; a surface at 2% can drop to 0% after a single update.

### Repeat runs — answers are non-deterministic `[practitioner]`

- Treat one run as an anecdote. For every prompt, do **3–5 runs on each engine, each in a fresh session**, and record a rate with its n ("cited 3/5, n=5").
- Fold wording variants of one intent into a single core prompt and spend the budget on repeats rather than on variants.
- Compare rates over time: 4/5 falling to 3/5 is noise; 4/5 falling to 0/5 and staying there for a month is signal. Treat that as a monitoring heuristic, not a significance test; any "it worked" claim stays under the verdict states in skill `seo-evidence` › experiments-and-revert-2 still govern any "it worked" claim.
- Restrict the prompt list to prompts that move revenue; a glossary citation rarely sells anything.
- Before fixing a "not cited" result, sort its cause into one of three: **technical** (the engine cannot fetch or parse the page), **comprehension** (the engine describes you wrongly or vaguely, meaning the fact is never stated plainly on the page that ought to carry it), or **trust** (the engine understands you and still does not pick you, which points to off-site consensus).

### Fan-out extraction (ChatGPT) `[practitioner]`

Method circulated in Aug 2026; it depends on the current UI, so re-verify before relying on it. Run the prompt with search on, open DevTools → Network, reload the conversation, and search the response payload for `queries`. Use what you find to build the test list from the real background queries, and to see which domains the fan-out runs `site:` searches against — those profiles become the priority list. **Never** use it to mass-produce a page per fan-out query: creating separate content for fan-out variations "primarily to manipulate rankings or generative AI responses in Google Search violates Google's scaled content abuse spam policy" `[documented: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide, 2026-10-14]`, and the policy covers many pages made "for the primary purpose of manipulating search rankings and not helping users", typically with "little to no value to users" `[documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-14]`. A fan-out query that reveals a genuinely distinct problem can still earn its own substantive page.

### Attribution triad — AI influence hides in branded and direct traffic `[vendor]`

Two observational panels: a genuine recommendation produced about twice the downstream search and visit behaviour of a passing mention (Scrunch, opt-in panel, compared against its own baseline); recommended brands saw about 2.5× new visitors in the following week, yet only about 9% of them arrived as visible AI referrals (SimilarWeb). Neither is controlled, so never forecast from them. Measure three signals together:

1. Prompt tracking (ladder rungs plus framing).
2. Self-reported attribution: a "how did you hear about us?" question with an AI option and a follow-up "what did you type?" — buyers hand over real prompts.
3. Branded-search volume in GSC: when it lifts and stays up with no campaign running, treat it as a candidate AI effect `[hypothesis]`.

### Shaping consensus (rung 4) — slow and anecdotal `[practitioner]`

- **Profile parity:** every third-party profile (Wikidata where legitimate, LinkedIn, partner listings, directories, review sites) should state the same segment, category and differentiators as the About page. It is the cheapest change on offer.
- **Cons written by others:** look up which con the aggregators list about you. Should it repeat a weakness that engines already echo, ask the publisher to swap in a different con that is also **true**. Never ask for removal, and never ask for a false claim.
- **Repairing a repeated weakness:** address it publicly, with specifics and a named person. One anecdote: one and a half to two years of founder posts plus a concrete "4–8 weeks" on the implementation page changed how engines described the product.
- **Repositioning or merger:** take a baseline for both old-segment and new-segment prompts and expect a dip (one client). Move the off-site signals first, stage the on-site rewrite after, and keep pages that win old-segment prompts until tracking shows the new association has formed.
- Refused, as in SKILL.md: invented awards, brand-run "independent" review sites, bulk seeding of Reddit or Wikipedia.

### Markdown representation for agents `[practitioner]`

No confirmed citation signal. Two optional implementations: serve Markdown at the **same canonical URL** on `Accept: text/markdown` with `Vary: Accept`, or send an HTTP `Link` header pointing at a parallel Markdown version. A Markdown version on a separate indexable URL is a duplicate, so keep it non-indexable or canonicalised to the HTML. Fuller rules in [agent-readiness.md](agent-readiness.md#markdown-and-discovery-files).

## Prompt families and source-type tally

The prompt panel reveals **which sources engines cite** when asked the questions that a page exists to answer. It never produces a single "AI visibility %".

### Build the panel from six prompt families `[practitioner]`

| Family | Shape (pt-PT example for a comparison site) | Why it matters |
|---|---|---|
| Recommendation | "melhor tarifa de eletricidade para 2 pessoas" | Triggers web retrieval and source lists most often `[hypothesis]` |
| Comparison | "EDP vs Goldenergy", "qual é melhor para …" | Maps to versus pages |
| Feature | "tarifa bi-horária com …", "conta sem comissões que …" | Maps to filter / attribute pages |
| Use case | "seguro auto para jovem condutor" | Maps to persona / segment pages |
| Price / value | "tarifa mais barata", "vale a pena …" | Claim-safety gate applies to anything we write back |
| Switching | "como mudar de operadora", "alternativa a …" | Maps to how-to and alternative pages |

Add modifiers (audience, constraint, locale) only where real demand shows up in GSC queries, People Also Ask or autocomplete. Group the prompts into 5–10 clusters according to which decision the user is making. Choose a panel size you can genuinely re-run on a schedule: a small panel run monthly beats a large one run once.

### Per run, record one row per prompt × engine

date · locale · engine · model/version if shown · logged-in state · competitors named (position) · our domain cited (Y/N, position in answer) · **every cited URL** · for each cited URL, its **source type**, one of forum-UGC (Reddit etc.) / video / regulator-government / news / directory / comparison or review site / brand site · plus the two fields in the next section.

### Read-outs

- **Citations per tested answer opportunity**, per engine and per cluster ("cited in 7 of 40, pt-PT, Copilot, 2026-10") — the same reporting unit as skill `seo-evidence` › experiments-and-revert-2.
- **Source-type tally per cluster** — the dominant type decides the work. If brand and comparison pages dominate, the gap is on-page (answer-first passage, table, original data). If directories and review sites dominate, the work is the presence and accuracy of our listing there. If forums dominate, only genuine, disclosed participation is allowed.
- **Most-cited domains** across the panel form the off-page target list. Give every target an owner and a concrete action: secure a listing, correct a stale one, or pitch an article author a genuinely useful update.
- **Format gaps:** competitors cited for a comparison table, a methodology or data that we lack.

### Guardrails

- No live runs means saying so; never "project" what an engine would cite.
- Off-page actions stay within the hard refusals in SKILL.md: no fake or incentivised reviews, no link exchanges, and no undisclosed employee or brand accounts posing as customers. UCPD Annex I consumer-impersonation ban: unverified [unverified: EUR-Lex text not readable by curl on 2026-10-12]; see ## Unverified.
- Re-run on a fixed cadence (quarterly at minimum for core clusters) with the same prompts; changing the prompt set breaks the time series.

## Measurement fields — framing and position of every mention

Two fields go on every row of the panel, next to cited Y/N `[practitioner]`:

| Field | Values | Why |
|---|---|---|
| `framing` | favourable / neutral / hedged / negative / recommended against | Separates rung 3 (mentioned) from rung 4 (recommended) and catches the shadow rung |
| `position` | first sentence / first paragraph / body / sources only | A source quoted in the lead and a source listed only in the footer are different outcomes |

Report trends in these fields alongside the citation count, never instead of it.

## Unverified

- UCPD Annex I consumer-impersonation ban: Annex I of the EU Unfair Commercial Practices Directive (Dir. 2005/29/EC) bans falsely presenting oneself as a consumer [unverified: EUR-Lex text not readable by curl on 2026-10-12].

## Sources

- coreyhaines31/marketingskills@skills/ai-seo/references/citations-vs-recommendations.md, format-volatility.md, positioning-and-consensus.md, agent-readiness.md (§Citation-source volatility, §Markdown representation) (phase-2 adapted file research/adapted/coreyhaines31__marketingskills/ai-citation-ladder-and-measurement.md) — the ladder, the ChatGPT 5.6 format snapshot (kept `[vendor]`), repeat-run rules, fan-out extraction, attribution triad, consensus moves, Markdown note. INTEGRATE, MIT.
- TheCraigHewitt/seomachine@.claude/commands/research-ai-citations.md, context/ai-citation-targets.md (phase-2 adapted file research/adapted/TheCraigHewitt__seomachine/ai-citation-prompt-audit.md) — six prompt families, per-run record, source-type tally, guardrails; the undisclosed-Reddit persona advice stays cut. INTEGRATE, MIT.
- Research REPORT §7 idea 13 — log the framing of AI mentions and the position of our passage inside the answer as measurement fields.
