# Technical SEO — Deep Audit Reference
<!-- split-header: part 1 of 2 of technical-audit.md (step-3 original lines 1–204; boundary start) -->
<!-- /split-header -->

## Contents

- Crawlability
- Indexability
- Site architecture
- URL conventions
- Sources

Other parts of the same original file: [rendering-and-sitemaps.md](rendering-and-sitemaps.md).

## Crawlability

### What to check

- Important pages are linked internally (no orphans).
- Important pages are not blocked by `robots.txt`.
- XML sitemap includes only canonical, indexable URLs (no 4xx, no noindex, no parameter URLs).
- No broken internal links.
- No redirect chains (A → B → C). Each redirect should be a single hop.
- Crawl traps controlled — filters, parameters, calendars, internal search, infinite URLs.

### robots.txt template

```
User-agent: *
Disallow: /api/
Disallow: /admin/
Disallow: /dashboard/
Disallow: /login
Disallow: /search?
Disallow: /*?utm_
Disallow: /*?sort=
Disallow: /*?filter=
Allow: /

Sitemap: https://example.com/sitemap.xml
```

⚠️ **`Allow: /` goes LAST, not first.** Google and RFC 9309 resolve conflicts by *longest match*, so order is irrelevant to them — but not every consumer implements that. Python's stdlib `urllib.robotparser`, and other first-match parsers still shipped in crawlers and audit tools, take the **first** matching rule: with `Allow: /` at the top, `/admin/` and `/login` read as ALLOWED. Two parsers genuinely disagree on the same file. Putting the broad `Allow` last costs nothing under longest-match and removes the ambiguity everywhere else.

Be careful with `Disallow: /*?` — it can block legitimate URLs. Prefer specific parameter blocks.

### AI crawlers — the access decision behind every GEO tactic

**Check this before recommending a single GEO tactic.** Wanting citations in ChatGPT, Perplexity or AI Overviews while blocking the agents that fetch your pages is the most expensive contradiction in modern SEO, and it is invisible in every ranking tool. Audit the live `robots.txt` first — a `Disallow` written years ago by someone worried about scraping routinely turns out to be the whole reason a client is absent from AI answers.

**The axis that matters is training vs retrieval, and most robots.txt files confuse them:**

| Agent | What it's for | Blocking it costs you |
|---|---|---|
| `GPTBot` | OpenAI **training** | No *retrieval* visibility (see caveat below) |
| `OAI-SearchBot` | OpenAI **retrieval** for ChatGPT Search | **Your ChatGPT Search citations** |
| `ChatGPT-User` | User-initiated fetch (someone pasted your link) | Possibly nothing: OpenAI says «robots.txt rules may not apply» to it `[documented: https://developers.openai.com/api/docs/bots, 2026-10-14]`; only an edge/WAF block reliably stops it |
| `ClaudeBot` | Anthropic **training** | No *retrieval* visibility (see caveat below) |
| `Claude-User` / `Claude-SearchBot` | Anthropic user-initiated / **retrieval** | Citations in Claude |
| `PerplexityBot` | Perplexity **indexing for citation** | **Your Perplexity citations** |
| `Perplexity-User` | User-initiated fetch | Not reliably anything: it «generally ignores robots.txt rules» `[documented: https://docs.perplexity.ai/guides/bots, 2026-10-14]`; only an edge/WAF block stops it |
| `CCBot` | Common Crawl — feeds many training sets | Training inclusion, not visibility |
| `Applebot-Extended` | Apple **AI-training** opt-out token | Nothing in Siri/Spotlight (that's `Applebot`) |
| `Google-Extended` | **Not a crawler** — see below | Gemini/Vertex grounding, **not** Search |
| `Bytespider`, `meta-externalagent` | ByteDance / Meta AI | Training inclusion |

**The single most-confused control: `Google-Extended`.** It is a robots.txt token, not a user-agent that fetches anything. It governs whether content Googlebot *already* crawled may be used for Gemini app grounding and model training. **It does not affect Google Search ranking, indexing, or AI Overviews** — those run on ordinary Googlebot. So "we blocked Google-Extended to stay out of AI" both fails (AI Overviews still use you) and costs nothing in Search. Decide it on training policy, not on visibility.

⚠️ **Caveat on "training costs no visibility."** It costs no *retrieval* visibility — blocking `GPTBot` cannot remove you from ChatGPT Search, because that is `OAI-SearchBot`'s job. What it may cost is **parametric presence**: whether a model can name your brand unprompted, with no retrieval step at all. That effect is real in principle and, as far as any published measurement goes, **unquantified** — so don't assert it in either direction. Say the retrieval half with confidence and label the rest as unknown.

**The default recommendation for a business that wants AI visibility:** allow every *retrieval* and *user-initiated* agent; decide *training* agents on policy and legal appetite, not SEO. Publishers with a licensing strategy invert the training half deliberately — that's a business call, and it belongs to the client, not to you.

**Policy rows from the public AI-bot registry** `[practitioner]` — the registry is a list of leads to verify against each vendor's own page, never a block list. The full classified list lives in skill `seo-ai-search` › ai-crawler-registry.

- **Never deploy a generated "block AI bots" robots.txt or server config, or a CDN toggle built on such a list, on a site that wants visibility.** Those lists cover AI-related crawlers of every purpose, so they block search engines (`Applebot`, `Bravebot`, `PetalBot`), retrieval bots (`OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot`, `DuckAssistBot`, `meta-webindexer`, `MistralAI-Index`) and link previews (`facebookexternalhit`) along with the training crawlers.
- **The training/retrieval split runs inside one vendor**, so decide per token: Meta `meta-webindexer` (AI citations) vs `meta-externalagent` (training); Apple `Applebot` (Siri/Spotlight/Safari) vs `Applebot-Extended` (training token); Mistral `MistralAI-Index` / `MistralAI-User` vs `MistralAI-Training`; Amazon `Amzn-SearchBot` / `Amzn-User` vs `Amazonbot`.
- **Default policy per class:** allow retrieval, user-triggered fetchers and search engines; decide training on policy; block nothing by default from rows whose purpose or robots.txt compliance the registry marks "Unclear" (106 of 181 rows for compliance when counted on 2026-10-11).
- **A robots.txt group binds only bots that honour robots.txt.** The registry marks `Perplexity-User`, `Meta-ExternalFetcher`, `Bytespider` and `DeepSeekBot` as not respecting it; for those, a `Disallow` states intent and enforcement happens at the edge, if at all.
- **Declared check for each intended-allow token:** parse the live robots.txt with a REP parser for the exact token and confirm whether it lands in its own group or falls through to `*` — combined with the group rule below, that is where an allow stanza opens or closes the wrong paths.
- ⚠️ The registry marks `ChatGPT-User`, `Claude-User` and `Google-Agent` as honouring robots.txt. The vendors' own pages differ: for `ChatGPT-User` OpenAI says «robots.txt rules may not apply» `[documented: https://developers.openai.com/api/docs/bots, 2026-10-14]`; Anthropic says disabling `Claude-User` «prevents our system from retrieving your content in response to a user query» `[documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-14]`. Google lists `Google-Agent` among its user-triggered fetchers, which «generally ignore robots.txt rules» `[documented: https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers, 2026-10-14]`. Where the vendor says robots.txt may not bind, only an edge/WAF rule enforces a block.

🛑 **A named group does not inherit `*` — this is where a well-meant AI stanza opens your admin panel.** RFC 9309: if more than one group matches the user-agent, «the matching groups' rules MUST be combined into one group»; only «If no matching group exists» does the crawler obey the `*` group `[documented: https://www.rfc-editor.org/rfc/rfc9309, 2026-10-12]`. Google: «User agent specific groups and global groups (*) are not combined» `[documented: https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec, 2026-10-11]`. So two `OAI-SearchBot` groups merge with each other, but once any group names the bot, the `User-agent: *` rules stop applying to it. A group containing only `Allow: /` exempts those bots from *every* `Disallow` you wrote under `*` — `/admin/`, `/login`, `/api/`, and the `/search?` crawl trap included. **Every rule you want an AI crawler to respect must be repeated in a group that names it** — and audit every group naming the bot, not just the first.

```
# Retrieval + user-initiated: allow, but repeat the site's own exclusions —
# these bots do NOT inherit anything from the User-agent: * group.
User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: PerplexityBot
User-agent: Perplexity-User
User-agent: Claude-User
User-agent: Claude-SearchBot
Disallow: /api/
Disallow: /admin/
Disallow: /dashboard/
Disallow: /login
Disallow: /search?
Disallow: /*?utm_
Disallow: /*?sort=
Disallow: /*?filter=
Allow: /

# Training: a policy decision, not an SEO one.
User-agent: GPTBot
User-agent: ClaudeBot
User-agent: CCBot
User-agent: Bytespider
User-agent: meta-externalagent
Disallow: /

# Training opt-out TOKENS (not crawlers — they gate use of already-crawled
# content). Omit these and you have opted out of OpenAI/Anthropic training
# while leaving Gemini and Apple training on, which is rarely what was meant.
# BUT SEE THE CAVEAT BELOW — Google-Extended is not purely a training switch.
User-agent: Google-Extended
Disallow: /

User-agent: Applebot-Extended
Disallow: /
```

⚠️ **Don't paste the `Google-Extended` block blind.** It is in the training group above for *consistency* — opting out of OpenAI and Anthropic training while leaving Gemini's on is rarely what anyone meant. But it is not a pure training switch: it also gates **Gemini grounding**, which is a retrieval-shaped surface. Blocking it costs you nothing in Google Search or AI Overviews, and it does cost you presence in Gemini's grounded answers. For a business whose goal is AI visibility, that is a real trade — decide it deliberately, and drop these two lines if grounded-answer presence matters more than training opt-out.

⚠️ **Diff the groups before shipping.** After writing any AI stanza, check each new group against `User-agent: *` and confirm nothing sensitive became reachable. Google's robots.txt report and any REP-compliant parser will show you the effective rules per user-agent — test the actual bot names, not `*`.

⚠️ **These tokens change.** Vendors add, rename and split agents (the OpenAI and Anthropic sets both gained a separate retrieval bot *after* their training bot shipped, which is exactly how sites ended up blocking retrieval by accident). Verify current names against each vendor's own published docs before shipping a stanza — and re-verify on any AI-visibility audit rather than trusting a table, this one included.

**Excerpt controls are separate from access — and they do not live in robots.txt.** `nosnippet` and `max-snippet:[n]` are **robots `meta` tags or `X-Robots-Tag` headers**; `data-nosnippet` is an **HTML attribute** on the element you want withheld. None of them is a robots.txt directive, and putting them there does nothing.

They limit the preview without blocking the crawl, and Google documents an AI-input effect for two of them: `nosnippet` applies to AI Overviews and AI Mode and «will also prevent the content from being used as a direct input for AI Overviews and AI Mode»; `max-snippet` «will also limit how much of the content may be used as a direct input for AI Overviews and AI Mode», except where the publisher separately granted use (in-page structured data, a licence agreement) `[documented: https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag, 2026-10-11]`. The same page documents `data-nosnippet` only for search-result snippets. The cost: a supporting link in AI Overviews or AI Mode requires a page «eligible to be shown in Google Search with a snippet» `[documented: https://developers.google.com/search/docs/appearance/ai-features, 2026-10-11]`, so `nosnippet` likely trades the citation for the exclusion `[hypothesis]`. A change takes effect only after recrawl, which «can take anywhere from several days to several months» `[documented: https://developers.google.com/search/docs/appearance/ai-features, 2026-10-11]`. Reach for `max-snippet` / `data-nosnippet` before blocking a crawler when the worry is answer-cannibalisation rather than access — blocking is far blunter.

## Indexability

### Per-page meta robots + canonical

```html
<meta name="robots" content="index,follow">
<link rel="canonical" href="https://example.com/final-url/" />
```

### What to noindex

| Page type | Action |
|-----------|--------|
| Internal search result pages | `noindex` |
| Thin tag/category pages | `noindex` or improve with unique content |
| Faceted filter URLs that duplicate the clean URL | `canonical` to clean URL or `noindex` (a facet that is a distinct, wanted collection stays indexable) |
| Cart / checkout / account pages | `noindex` |
| Staging / dev URLs | **HTTP auth** — that alone is sufficient and is the only reliable control. Don't pair `noindex` with a robots `Disallow`: a blocked URL is never fetched, so the `noindex` is never read, and an already-indexed URL can persist. Pick one — auth, or `noindex` on a *crawlable* URL |
| AI-generated thin content | remove, noindex, or merge |
| Old date-based archives with no traffic | noindex or 410 |
| Print versions / amp duplicates | canonical to canonical version |

### Canonical rules

- Self-referencing canonical on every page you want indexed under its own URL (points to itself).
- Decide by content, not URL syntax. Canonicalisation is for «duplicate or very similar pages» `[documented: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls, 2026-10-14]`: a sort, tracking or view parameter that repeats the base page canonicals to it; a filter URL that is a distinct collection you want indexed self-canonicals.
- Pagination: each page self-canonicals (`rel=next/prev` is retired as a Google signal; leaving it in place does no harm).
- Locale variants in different languages do NOT canonical to each other — they're alternates, not duplicates. Use hreflang. Exception: same-language regional duplicates (`example.de/` and `example.com/de/`) — Google says «pick a preferred version» and use `rel="canonical"` with hreflang `[documented: https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites, 2026-10-14]`; see [international-and-hreflang-2.md](international-and-hreflang-2.md).
- Mobile/desktop separate URLs (m.example.com): canonical desktop ← from mobile, with `Vary: User-Agent`.

### "Crawled — currently not indexed" (GSC)

The status says only that the page «was crawled by Google but not indexed. It may or may not be indexed in the future; no need to resubmit this URL for crawling» `[documented: https://support.google.com/webmasters/answer/7440203, 2026-10-12]`. It does not certify that robots, noindex or rendering are clear, and it names no cause. Sequence:

1. **Rule out the technical causes first** — read the rendered HTML in URL Inspection, the served canonical and any near-duplicates (the corrected diagnosis is in [incident-triage.md](incident-triage.md)).
2. **Then give each URL a distinct intent, consolidate thin or duplicate pages, and add contextual links from indexed pages** `[practitioner: anonymised sources · consensus · 3 thr / 16 · newest 2026-05]`.
3. Any "authority threshold" behind the status is a story Google does not document `[hypothesis]`.
4. **Do not republish under a fresh slug as a fix.** A URL change inherits entry #174's IT DEPENDS mark and is an experiment, never a routine step — see [migrations-and-recovery.md](migrations-and-recovery.md).

## Site architecture

```
Homepage
 ├── Pillar / category page
 │    ├── Subtopic page
 │    ├── Comparison page
 │    ├── FAQ page
 │    └── Tool/calculator
 └── Pillar / category page
      ├── Subtopic page
      └── Local page
```

Click depth targets `[unvalidated house heuristic]`:

| Page type | Max clicks from homepage |
|-----------|-------------------------|
| Core money pages | 1-2 |
| Pillar pages | 1-2 |
| Important cluster pages | 2-3 |
| Long-tail articles | 3-4 |

Deep pages are harder to discover and are linked less; how much depth costs is unmeasured here `[hypothesis]`. Use the table as a planning target, not a defect threshold.

## URL conventions

| Rule | Good | Bad |
|------|------|-----|
| Short | `/electricity/compare/` | `/best-cheap-top-electricity-provider-portugal-save-now/` |
| Descriptive | `/mortgage/taeg-vs-tan/` | `/page?id=92384` |
| Stable | `/electricity/compare/` | `/blog/2026/05/10/electricity-compare/` |
| Lowercase | `/car-insurance/` | `/Car-Insurance/` |
| Hyphenated | `/best-internet-provider/` | `/best_internet_provider/` |
| Localized | `/pt/seguro-auto/` | `/pt/auto-insurance/` |
| No filler | `/electricity/edp-vs-galp/` | `/articles/the-best-electricity-comparison-edp-and-galp-2026/` |

The table is usability and stability advice `[unvalidated house heuristic]`. Keywords in the URL carry no established ranking effect: entry #174 is IT DEPENDS, and its only sized side is a loss after renaming existing URLs — see [migrations-and-recovery.md](migrations-and-recovery.md) before changing a live slug.

## Sources

- ai-robots-txt/ai.robots.txt@main robots.json, README.md, FAQ.md (phase-2 adapted file research/adapted/ai-robots-txt__ai.robots.txt/ai-bot-registry-for-edge-gate.md) — policy rows only: why generated block files are unsafe for visibility, per-vendor training/retrieval splits, default policy per class, robots.txt-compliance flags, declared check, user-fetcher conflict. Rewritten in our own words; no verbatim text carried, so no Attribution section. COPY-tagged input used as INTEGRATE, MIT.

