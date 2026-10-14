# AI Search (GEO) & Conversion SEO — Reference
<!-- split-header-2: part 1 of 2 of ai-retrieval-and-citation.md (original lines 1–151; boundary start) -->
<!-- /split-header-2 -->

## Contents

- Why GEO (Generative Engine Optimization) matters
- How AI answer engines actually retrieve (RAG / query fan-out)
- How AI answer engines pick sources
- Citation deltas — rules the generic GEO advice misses
- Google's AI optimisation guide — the myth list
- Differentiation over redundancy — and the GIST hypothesis behind it
- Unverified

Other parts of the same original file: [ai-retrieval-and-citation-2.md](ai-retrieval-and-citation-2.md).

## Why GEO (Generative Engine Optimization) matters

Modern search includes:
- Google AI Overviews
- Bing Copilot
- ChatGPT search/browsing
- Perplexity-style answer engines
- Voice search (Google Assistant, Siri, Alexa)
- Featured snippets
- Knowledge panels
- People Also Ask blocks

Many of these are **zero-click** — the user gets the answer without visiting your site. The win condition shifts from "rank #1" to "be the cited source" + "earn the trust to be navigated to anyway."

## How AI answer engines actually retrieve (RAG / query fan-out)

On a real-time question, AI answer engines run **retrieval-augmented generation (RAG)** via a **query fan-out**: rewrite the prompt into *many* search queries, hit a conventional engine or the engine's own index, and synthesize the answer from what comes back `[hypothesis]` — which backend each engine queries is not documented in any saved source. Two things the naive version of this model gets wrong:

- **Retrieval keys on the fan-out's rewrites, not your head term.** A page ranked #40 for the user's original question can be #3 for one of the rewritten sub-queries — and get cited. This is also why vendor studies showing "AI citations increasingly come from outside the head-term top 10" don't refute the mechanism: they score rank against the *original* query, understating pool membership. (Their specific percentages disagree with each other and lump engines that don't share a backend — take the direction, never quote the numbers.)
- **Live SERPs are not the only door.** *Reasoning, not a measurement — flagged as such:* the denominator artifact above cannot by itself explain a **change over time**, because fan-out was already in use during the periods when head-term overlap was reported as high. That points to engines also drawing more on retrieval *outside* live SERPs — their own indices and passage stores, their own crawlers, multi-hop browsing, licensed/partner corpora, hard-weighted reference and UGC domains. **Treat this as the most plausible reading of noisy vendor data, not as an established finding**: nobody outside the engines can currently measure how the weight splits, and it is moving.

Three consequences govern everything else in this file:

1. **No pure-GEO bypass of discoverability.** A page no engine can retrieve by *any* path cannot be cited — GEO is an *overlay* on SEO, not an alternative. But the bar is **retrievable by that engine**, not "head-term top 10." "Can't be cited without a classical ranking" is too strong; "can't be cited without being discoverable" survives.
2. **Rank + own the cited passage for the queries the fan-out actually issues, with original data** — long-tail, conversational, problem-framed queries, not just the head term. And work the non-SERP doors: reference-grade pages, entity presence, crawlability by the engines' own bots.
3. **Bing may matter more than its market share suggests.** That ChatGPT search leans on Bing, and that DuckDuckGo/Ecosia ride it, is `[memory]` — no saved OpenAI page says so; verify before putting it in a report. Copilot is Microsoft's own surface.

### Bing as a first-class AI-retrieval surface

- Verify in **Bing Webmaster Tools**, submit the sitemap, and track Bing rank separately — Bing clusters and weights signals differently from Google.
- Bing is widely held to reward **literal on-page optimization** (exact terms in title/H1/body) and **structured data** more than modern Google `[hypothesis]`. Treat reported "2-day FAQ → GPT lift" stories as *test-it* hypotheses, not laws; measure before scaling.
- Do not treat "Bing = ChatGPT's index" as established `[memory]`. What OpenAI documents is its own search crawler: OAI-SearchBot «is used to surface websites in search results in ChatGPT's search features», and sites opted out of it «will not be shown in ChatGPT search answers, though can still appear as navigational links» `[documented: https://developers.openai.com/api/docs/bots, 2026-10-14]`. Allow OAI-SearchBot first; measure ChatGPT citations directly rather than inferring them from Bing rank.

### `llms.txt` — not a search/visibility lever

What is known, by source:
- **Google Search:** you don't need LLMS.txt files to appear in Google Search, including its generative AI features, "as Google Search itself doesn't use them"; creating one "will neither harm nor help your site's visibility or rankings in Google Search" `[documented: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide, 2026-10-14]`. This is scoped to Google Search only.
- **Fetch observation:** one vendor's logs showed 84 of 62,100 AI-bot requests (0.1%) hitting `/llms.txt` `[vendor]` (OtterlyAI, via research/adapted/AgriciDaniel__claude-seo/google-ledger-and-ai-guide-delta-2026-10.md). One log set, not a cross-provider measurement.
- **Other providers (Perplexity, OpenAI, Anthropic, Microsoft):** no official statement held; whether any uses the file for retrieval or citation is unknown (skill `seo-authority` › authority-trust-and-distribution, #68/#71: mechanism unconfirmed).

Its clear use is as a token-saving convenience for **AI coding/developer agents** parsing docs `[practitioner]`. **Prioritise it only if you host developer documentation read by coding agents;** for consumer/marketing/comparison sites expect no Google Search effect and treat any other-engine effect as unproven `[hypothesis]`. Don't sell it to a client as an AI-visibility play.

The llms.txt specification v2 (modified 2026-08-10) requires only the H1 and itself makes no ranking or citation claim `[documented: https://llmstxt.org/, 2026-10-11]`; format validation rules are in [geo-audit-and-citability.md](geo-audit-and-citability.md#llmstxt--format-validation-rules).

## How AI answer engines pick sources

A list of commonly cited features `[hypothesis]`, not engine documentation: Google lists only indexation and snippet eligibility for a supporting link in AI Overviews or AI Mode, with «no additional technical requirements» `[documented: https://developers.google.com/search/docs/appearance/ai-features, 2026-10-11]`. Commonly cited as favoured:

1. **Direct, factual answer near the top** of a page — concise enough to lift verbatim.
2. **Factual density** — claims that are verifiable and well-sourced.
3. **Entity clarity** — the page clearly defines the entities (people, brands, places, products) it discusses.
4. **Source authority** — citations to regulators, official data, primary sources.
5. **Structured data** — schema helps machines classify content.
6. **Tabular data** — comparisons in tables are extremely parseable.
7. **FAQ format** — long-tail questions matched to direct answers.
8. **Author identity** — expert author with verifiable credentials.
9. **Freshness** — visible update dates, current data.
10. **Original data** — engines prefer unique sources to cite over derivative summaries.

## Citation deltas — rules the generic GEO advice misses

1. **On a regulated page, a precise number is advertising** (Consumer Credit Directive 2008/48/EC; CCD2, Directive (EU) 2023/2225, applying from 2026-11-20; IDD for insurance). CCD2 requires credit advertising that indicates an interest rate or any cost figure to carry standard information, including the annual percentage rate of charge, specified by a representative example `[documented: https://eur-lex.europa.eu/eli/dir/2023/2225/oj/eng, 2026-10-11]`. Generic GEO advice asks for declarative, liftable fact sentences. On credit pages, a concrete rate or saving figure triggers the TAEG and representative-example duties; on insurance pages it falls inside the IDD perimeter; on investment pages it touches the MiFID II boundary. Either write the precise claim together with its mandatory disclosure, or leave it out — being precise never exempts copy from the legal gate. Do not illustrate this rule with a made-up figure, because models copy examples.
2. **When your number disagrees with the web's consensus** `[practitioner]`, place the method — inputs, date, scope — right beside it. An outlier with no explanation looks like a mistake to a reader and, plausibly, to an engine that cross-checks sources `[hypothesis]`.
3. **Sourcing is language-local** `[hypothesis]`: published source-mix figures (Reddit and YouTube shares of Perplexity citations, overlap between ChatGPT and the AIO top 10) describe the English-language web and do not transfer. For pt-PT finance and energy queries, expect regulators and consumer bodies (ERSE, BdP, ANACOM, ASF, DECO) to be cited first. Before putting effort into community distribution, log which domains really are cited by running the prompt panel **in Portuguese** ([ai-citation-measurement.md](ai-citation-measurement.md)).
4. **Audit LLM-drafted copy before it ships** `[practitioner]`:
   - remove filler idioms ("delve into", "navigate the nuances"), piled-up hedging modals, decorative emoji and a monotonous sentence rhythm;
   - **check that every citation exists** and supports the claim made (author, venue, topic) — language models invent studies and attach them to real authors;
   - match the register to the persona; copy too polished for the person supposedly speaking reads as fake. Length is not value.
5. **Accessibility doubles as the extraction layer.** That semantic HTML — real `<table>` elements, ordered headings, labelled controls, alt text — helps parsers as well as screen readers is `[hypothesis]` as a citation mechanism; scope the work once for both. European Accessibility Act legal floor: unverified [unverified: EUR-Lex text of Directive (EU) 2019/882 not readable by curl on 2026-10-12]; see ## Unverified. The engineering target is WCAG 2.2 AA `[practitioner]`. Do not repeat the circulating "+23% organic traffic / +27% keywords for accessible sites" claim — it has no source and is correlational `[vendor]`.
6. **Vendor percentages are never targets** `[vendor]`. "AI-referral visitors convert ~5×", "AIO cuts position-1 CTR up to 58%", "cited brands gain +35% clicks" and "AEO-referral conversion target >12%" are second-hand marketing figures with no n and no design. They can justify looking at AI citations at all; they must never become a KPI target or a client forecast (SKILL.md: never forecast from a published number).

## Google's AI optimisation guide — the myth list

Gate for any GEO advice. Carried from claude-seo (see `## Attribution`).

Published 2026-05-15, llms.txt note 2026-06-15, updated 2026-07-10 (https://developers.google.com/search/docs/fundamentals/ai-optimization-guide). "Optimizing for generative AI search is … still SEO." Eligibility floor: indexed + snippet-eligible + included via the gen-AI control; there is no separate AI index. Google says you do **not** need to `[documented: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide, 2026-10-11]`:

1. create llms.txt, AI text files, AI markup or Markdown ("Google Search ignores them"; neither helps nor harms);
2. **"chunk" content into small pieces for AI**;
3. **rewrite content with special phrasings or long-tail keyword variations for AI**;
4. chase inauthentic mentions across blogs, forums or videos;
5. over-invest in structured data specifically for AI features.

What it says matters: unique, non-commodity, first-hand content (its example: "Why We Waived the Inspection…" vs "7 Tips for First-Time Homebuyers"). Who/How/Why test from *Creating helpful content*; warning signs include writing to a word count, faking date freshness, mass churn for "freshness". Rule `[practitioner]`: when a third-party GEO recommendation contradicts this list, flag the contradiction and defer to Google for Google surfaces; it may still apply to non-Google engines — say which.

llms.txt evidence to cite alongside the ledger entries #68/#71 in skill `seo-authority` › authority-trust-and-distribution: Google guide text above `[documented: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide, 2026-10-11]`; SE Ranking 300k-domain study — 1 of the 50 most AI-cited domains had one `[vendor]`; OtterlyAI logs — 84 of 62,100 AI-bot requests (0.1%) hit `/llms.txt` `[vendor]`. Real use: AI **coding** agents loading developer docs. Lighthouse's `llms-txt` audit is a lab check, not a Search signal ([agent-readiness.md](agent-readiness.md#lighthouse-agentic-browsing--reading-xn)).

## Differentiation over redundancy — and the GIST hypothesis behind it

**The tactic first — it doesn't depend on GIST.** The 2015-2024 "**skyscraper**" playbook (find the top-ranking article, write a slightly longer/prettier version) is a weak bid for citation `[practitioner]`: a near-duplicate gives an answer engine no evident reason to cite you over the incumbent, and gives a link-earner no reason to link you. "Do not be a semantic duplicate" is ordinary practitioner advice `[practitioner]` — a page that adds what the winners lack can be citable *alongside* them. That ranking #4 with an orthogonal angle earns more citations than ranking #2 with a rewrite of #1 is `[hypothesis]` — untested; test it on your own queries before choosing a strategy on it. The drafting advice does not depend on the engines' selection code.

**The orthogonal-content playbook.**

1. **Map the consensus.** Read the top 3–5 ranking pages for the target query. List the entities, sub-topics, data points, and stances they cover. That is the "no-lift zone."
2. **Find the missing node.** Ask: what dimension is genuinely absent? Common vectors the winners neglect:
   - **Data / benchmarks** — original measurements, a survey, price observations, a dataset.
   - **Edge cases** — the scenarios the generalist guide skips (regional variants, regulated exceptions, unusual profiles).
   - **How, not what** — the operational detail (integration steps, compliance workflow, migration procedure).
   - **Constraints** — legal, regulatory, accessibility, procurement, sourcing.
   - **Failure modes** — what breaks, when, and how to recover.
   - **Adjacent decisions** — what the reader must decide *around* the main question.
3. **Complement, don't replace.** The goal is *addendum content* the incumbent didn't write — you're bidding to be the second or third source cited alongside them, not to unseat them.
4. **Signal distinctness structurally.** Distinct entities in `Product` / `ItemList` / `Dataset` schema; specific numbers; unique tables; named authors; primary-source citations. Anything that makes the machine parse you as *different information*, not a paraphrase.

**The hypothesis behind the name — GIST, clearly labelled.** Google Research presented **GIST (Greedy Independent Set Thresholding)** at NeurIPS 2025 (arXiv 2405.18754) — a subset-selection protocol that iteratively takes the highest-utility item and *excludes* every remaining item within a semantic-similarity radius of it, with a proven ≥½-optimal utility guarantee. Two leaps stand between the paper and "this is how AI answer engines pick sources," and **neither is verified**: (1) *deployment* — publication ≠ production; (2) *domain* — the paper's demonstrated territory is generic ML data-subset selection, not answer-engine source selection. What makes the transfer plausible is compute economics: every answer surface must pick a handful of sources from a larger retrieval pool, and paying for redundant tokens across five near-identical sources is expensive. **If** engines run anything GIST-shaped, a page semantically inside the current #1's radius gets excluded regardless of its authority — which would turn skyscraper content from a weak bid into an actively losing one. Treat GIST as a named, cited reason the differentiation tactic *may matter more now* — never as the tactic's foundation.

**Testing your semantic distance from the consensus.**

There's no official Google-side tool. A cheap proxy:

```
Prompt to an LLM (Claude / Gemini / GPT):

"Here is my draft: [paste content]

Here are the current top 3 ranking URLs for [query]:
1. [url + paste text]
2. [url + paste text]
3. [url + paste text]

Estimate the semantic overlap between my draft and each of the three, and list the sections that are near-duplicates in framing or content."
```

This gives a *qualitative* overlap read — enough to catch the obvious near-duplicate. For an actual similarity number, use an **embedding model** (embed your draft and each competitor page, compare the vectors); a chat model cannot compute cosine similarity, only judge resemblance. Third-party "GIST compliance checkers" (e.g. websiteaiscore.com's beta) exist but are unverified — directional signal, not a source of truth.

**What none of this changes.**

- You still need to be **retrievable** to be selectable — via the fan-out's queries or the engines' own indices (see [above](#how-ai-answer-engines-actually-retrieve-rag--query-fan-out)). Diversity-shaped selection, if real, governs *picking within the pool*, not who gets in. Classical discoverability remains the entry ticket.
- Utility still matters. Being orthogonal to the consensus but *low-utility* (thin, unsourced, off-topic) doesn't get you picked either. Semantic distance + high utility, both.
- Consensus content still ranks in classical blue-link SERPs. The suspected risk is to your AI-citation share, not your organic clicks `[hypothesis]`; we hold no measurement of that share falling for "me too" content.

**The same line holds for "information gain":** the *tactic* (original data, orthogonal angle) stands on its own; the *mechanism* stays unconfirmed `[hypothesis]`.

## Unverified

- European Accessibility Act legal floor: in the EU, the European Accessibility Act (Directive (EU) 2019/882) via EN 301 549 sets WCAG 2.1 AA, transposed in Portugal by DL 82/2022 [unverified: EUR-Lex text of Directive (EU) 2019/882 not readable by curl on 2026-10-12; DL 82/2022 not fetched]
- Illyes llms.txt remark: Gary Illyes said in July 2025 that Google has "no plans to support" llms.txt [unverified: a Googler's public remark, no official page; Google's own position is the guide text cited above]

