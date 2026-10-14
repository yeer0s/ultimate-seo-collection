# AI crawler registry — a list to test against, never a block list

## Contents

- What the registry is
- Why the generated block files are dangerous for SEO
- Classified tokens for a PT/EU site
- Conflicts with vendor documentation
- Matching rule
- How to use
- Attribution
- Sources

## What the registry is

**A list to test against, never a block list.** `ai-robots-txt/ai.robots.txt` keeps the largest public list of AI user-agent tokens: **181 entries** in `robots.json` (counted 2026-10-11, last push 2026-10-09). Each row has `operator`, `respect` (does it honour robots.txt), `function`, `frequency`, `description`. The repo *generates block files* from it (robots.txt, .htaccess, nginx, Caddy, HAProxy, lighttpd). **Use the data; do not deploy the generated files on a site that wants search or AI visibility.**

## Why the generated block files are dangerous for SEO

`[practitioner]` The list is "AI-related crawlers of all types, regardless of purpose" (README.md:5). It therefore blocks retrieval and search crawlers together with training crawlers. The shipped `robots.txt` and `nginx-block-ai-bots.conf` (returns 403) include, among others:

- **Search-engine crawlers:** `Applebot` (Siri/Spotlight/Safari; robots.json:135), `Bravebot` (Brave Search index; :198), `PetalBot` (Huawei Petal Search; :976), `YouBot` (:1256).
- **AI-answer retrieval bots:** `OAI-SearchBot` (:899), `Claude-SearchBot` (:275), `PerplexityBot` (:969), `DuckAssistBot` (:423), `meta-webindexer` (Meta AI citations; :808), `MistralAI-Index` (:815), `Kimi-SearchBot` (:689).
- **Link previews:** `facebookexternalhit` (:472) — blocking it kills Open Graph previews on Meta apps and Apple Messages (the repo says so itself).
- **Generic words matched as tokens:** `Spider` (:1109), `Code` (:324), `Operator` (:934), `Cursor` (:374), `LCC` (:738), `Trae` (:1165), `YaK` (:1228). The server configs match case-insensitively on word boundaries (nginx-block-ai-bots.conf:3), so any UA containing the standalone word "spider" or "code" gets a 403 — collateral on unrelated crawlers.

A site that pastes these files, or a CDN "block AI bots" toggle built on a similar list, silently removes itself from ChatGPT search answers (OpenAI: opted-out sites "can still appear as navigational links"), Claude, Perplexity, Meta AI and Apple surfaces. That is exactly the "declared allowed, edge-blocked" failure the edge gate in [ai-crawlers-and-bot-policy-2.md](ai-crawlers-and-bot-policy-2.md#the-edge-gate-in-practice) exists to catch.

## Classified tokens for a PT/EU site

Respect values are as the registry states them; where the registry and a vendor doc disagree, trust the vendor doc and re-verify (see the next section). `[practitioner]` for the classification; a row counts as documented only where a dated documented label citing a saved vendor page sits on it.

| Class | Tokens (robots.json line) | Blocking costs |
|---|---|---|
| **Retrieval / AI search index** | `OAI-SearchBot` :899 · `Claude-SearchBot` :275 · `PerplexityBot` :969 · `meta-webindexer` :808 · `MistralAI-Index` :815 (Mistral: not used for training) · `DuckAssistBot` :423 · `Kimi-SearchBot` :689 · `YandexAdditional`/`YandexAdditionalBot` :1235 (YandexGPT quick answers) | Citations in that product |
| **Search engines with AI surfaces** | `Applebot` :135 · `Bravebot` :198 · `PetalBot` :976 · (`Googlebot`, `Bingbot` are not in the list — keep them that way) | Organic + AI answers in that engine |
| **User-triggered fetch** | `ChatGPT-User` :261 · `Claude-User` :282 · `Perplexity-User` :962 (respect: **No**) · `MistralAI-User` :829/:836 · `Meta-ExternalFetcher` :801 (respect: **No**) · `Kimi-User` :696 · `Amzn-User` :93 (Amazon: «may not follow all robots.txt directives» `[documented: https://developer.amazon.com/amazonbot, 2026-10-14]`) · `kagi-fetcher` :661 · `Google-NotebookLM` :549 (old name of Google-GeminiNotebook) · `GoogleAgent-URLContext` :563 · `Diffbot-User` :409 | A live fetch for a person who pasted your link |
| **Browser agents** | `ChatGPT Agent` :254 · `Operator` :934 · `Google-Agent` :514 · `GoogleAgent-Mariner` :556 · `NovaAct` :885 · `AmazonBuyForMe` :79 · `Manus-User` :773 · `Kimi-Agent` :682 | Agents completing tasks (compare, sign up) on the site |
| **Training** | `GPTBot` :591 · `ClaudeBot` :296 · `Google-Extended` :528 (token, not a crawler) · `Applebot-Extended` :142 · `CCBot` :233 · `meta-externalagent` :780 · `FacebookBot` :465 · `MistralAI-Training` :822 · `KimiBot` :703 · `cohere-training-data-crawler` :339 · `Bytespider` :226 (respect: **No**) · `TikTokSpider` :1144 · `DeepSeekBot` :388 (respect: **No**) · `ERNIEBot` :444 · `QwenBot` :1046 · `PanguBot` :941 · `AI2Bot`/`Ai2Bot-Dolma` :23/:37 | Training inclusion — a policy call, not SEO |
| **Special purpose** | `OAI-AdsBot` :892 (checks landing pages submitted as ChatGPT ads; not training) · `GoogleOther` :570 · `Google-CloudVertexBot` :521 (crawls on the owner's request) · `facebookexternalhit` :472 (previews) | Ads review / R&D crawls / link previews |
| **AI search APIs (data providers)** | `ExaSearchBot` :458 · `TavilyBot` :1116 · `LinkupBot` :766 · `AIWebIndex` :51 · `ShapBot` :1095 | Presence in third-party agent search APIs — unmeasured value `[hypothesis]` |

Tokens this adds to the short list in [ai-crawlers-and-bot-policy.md](ai-crawlers-and-bot-policy.md#audit-the-right-bot-list): `meta-webindexer` (the Meta AI *citation* bot, distinct from training `meta-externalagent`), `MistralAI-Index`/`-User`, `DuckAssistBot`, `Bravebot`, `Applebot` as a block-list casualty, `OAI-AdsBot`, the agent class, and the Amazon split (`Amzn-SearchBot`/`Amzn-User` vs `Amazonbot`). Which of these to allow or refuse on a given site is a policy decision held in skill `seo-technical` › crawl-and-index.

## Conflicts with vendor documentation

`[practitioner]` Resolve against vendor docs before each audit; the vendor page wins.

- `ChatGPT-User` is marked respect "Yes" (:262). OpenAI's bots page says robots.txt rules "may not apply" to it — carry the OpenAI wording (quoted in [ai-crawlers-and-bot-policy.md](ai-crawlers-and-bot-policy.md#bots-robotstxt-cannot-block)).
- `Google-Agent` is marked "Yes" (:516). Google documents its user-triggered fetchers as generally ignoring robots.txt — carry Google's wording.
- `Claude-User` is marked "Yes", linking Anthropic's support article (:284). This agrees with Anthropic's page, and [ai-crawlers-and-bot-policy.md](ai-crawlers-and-bot-policy.md#bots-robotstxt-cannot-block) already lists Claude-User as honouring robots.txt.
- `Google-NotebookLM` (:549) is the old name (old name kept only for testing); Google now documents `Google-GeminiNotebook`, with the old token supported until August 2026. Test both until the registry catches up.
- Data quality: 106 of 181 rows say respect "Unclear", 53 say operator "Unclear"; many rows are scraped from knownagents.com summaries. Treat a row as a **lead to verify**, not a fact.

## Matching rule

Verbatim from the registry: "Agent names should be matched as whole words rather than substrings … Without word boundaries, agent names match inside unrelated strings" (FAQ.md:53-59). Any log grep or edge rule built from this list must use word boundaries — and must still accept that generic tokens (`Spider`, `Code`) over-match.

## How to use

The rule `[practitioner]`: **test the edge gate against every ai.robots.txt release; never import the block list.** Add each new retrieval-class token to the per-bot test list, and assert that no CDN or robots rule has imported the block list. On mowei.pt, check the Cloudflare managed block (see [ai-crawlers-and-bot-policy-2.md](ai-crawlers-and-bot-policy-2.md#cloudflare-managed-robots)) for `Applebot`, `Bravebot`, `DuckAssistBot` and `meta-webindexer`.

Operational form, extending the two-tier procedure in [ai-crawlers-and-bot-policy.md](ai-crawlers-and-bot-policy.md#the-rule-the-whole-file-exists-for):

1. **Pin a release** of `robots.json` (tag `v1.n`; subscribe to `releases.atom`, README.md:97-100). Read it as data; never execute the repo's scripts.
2. **Write the intended policy per token** using the class table above: allow retrieval + user-fetch + engines; decide training on policy; block nothing by default from the "unclear" rows.
3. **Declared check:** REP-parse the live robots.txt for each intended-allow token (exact token, own group vs `*`).
4. **Actual check:** request a representative URL with that bot's documented UA string (robots.json has tokens, not full UA strings — take the string from the vendor page) and compare status + body length with a browser baseline; a JS challenge returns 200.
5. **Observed check** (idea from `Auriti-Labs/geo-optimizer-skill@docs/geo-logs.md`, `@docs/ai-bots-reference.md:266-284`): count hits per token in 28 days of access logs, word-boundary matched, and verify identity (published IP ranges, reverse DNS, or Web Bot Auth) because UA strings are spoofed. An intended-allow retrieval bot with zero verified hits is a lead, not a verdict.
6. **On each new release:** diff the token set; any new token in a retrieval/search/user-fetch class goes into the test list. Never auto-import the release into a block rule.

The registry's Bing page (noarchive as the only Bing control) is not carried here: Bing's current documented `noarchive`/`nocache` wording is in [ai-crawlers-and-bot-policy-2.md](ai-crawlers-and-bot-policy-2.md#non-google-surfaces-documented-controls).

## Attribution

- ai-robots-txt/ai.robots.txt — Copyright (c) 2024 ai.robots.txt — MIT License. Classified token table, the "Why the generated block files are dangerous" list, the matching rule and the edge-gate steps are carried verbatim or near-verbatim from the phase-2 adapted file; conflict notes and the "How to use" rule are ours.

## Sources

- ai-robots-txt/ai.robots.txt@robots.json, README.md, FAQ.md, ai-robots-txt/ai.robots.txt@docs/additional-steps/bing.md, nginx-block-ai-bots.conf (phase-2 adapted file research/adapted/ai-robots-txt__ai.robots.txt/ai-bot-registry-for-edge-gate.md) — 181-entry registry (line numbers above), README.md:5, :22, :97-100, FAQ.md:35-59, nginx-block-ai-bots.conf:1-13. COPY, MIT. Counts (181 rows, 106 respect-unclear, 53 operator-unclear) made with Grep on the clone, 2026-10-11.
- Auriti-Labs/geo-optimizer-skill@docs/geo-logs.md, Auriti-Labs/geo-optimizer-skill@docs/ai-bots-reference.md:266-284 (MIT) — log-tier idea only, no text copied.
- Research REPORT §7 idea 1 — run the edge gate against every ai.robots.txt release; never import the block list.
