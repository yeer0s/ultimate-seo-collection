# AI crawlers and bot policy — proving an access claim
<!-- split-header-2: part 1 of 2 of ai-crawlers-and-bot-policy.md (original lines 1–99; boundary start) -->
<!-- /split-header-2 -->

## Contents

- The rule the whole file exists for
- Status vocabulary for reporting declared access
- Audit the right bot list
- Bots robots.txt cannot block
- Fetch limits — the crawler that arrives and still misses your schema
- Google's AI citation surfaces and their controls (2026)
- Unverified
- Sources

Other parts of the same original file: [ai-crawlers-and-bot-policy-2.md](ai-crawlers-and-bot-policy-2.md).

## The rule the whole file exists for

**A bot-access claim requires a request sent AS that bot.** Reading `robots.txt` tells you what a site *declares*. It does not tell you what a bot *receives* — a CDN bot rule, a WAF challenge, a rate limiter or an origin ACL can refuse a crawler that `robots.txt` welcomes, and none of that is visible in the file.

This is not hypothetical. `[practitioner]` `geo-seo-claude@scripts/fetch_page.py:20-26` defines an `AI_CRAWLERS` dictionary of five user-agent strings (GPTBot, ClaudeBot, PerplexityBot, GoogleBot, BingBot) and **never references it anywhere else in the repository** — a repo-wide grep for `AI_CRAWLERS` returns exactly one hit, the definition itself. Every request the tool makes goes out with the Chrome UA in `DEFAULT_HEADERS` (`:28-30`). Its `BLOCKED` verdicts are therefore parses of a text file, not per-bot tests, and its example audit's "crawlers blocked" conclusion rests on a single 403 answered to a *browser* UA. `[practitioner]` Treat any audit tool's bot verdict as a `robots.txt` parse until you have seen the request it actually sent.

The two-tier procedure `[practitioner]`:

1. **Declared access** — parse `robots.txt` per user-agent, with a REP-compliant parser such as `google/robotstxt` (Google's production REP parser and matcher, RFC 9309; its binary exits 0 for ALLOWED and 1 for DISALLOWED) `[documented: https://raw.githubusercontent.com/google/robotstxt/master/README.md, 2026-10-12]`, testing the real token (`OAI-SearchBot`, not `*`). Two limits of that binary `[documented: https://raw.githubusercontent.com/google/robotstxt/master/README.md, 2026-10-12]`: you must hand it a URI already in RFC 3986 format (it does not fully normalise it), and it does not apply crawler fallbacks (a bot such as `Googlebot-Image` that lacks a group of its own falls back to the `Googlebot` group, which the binary will not infer). Remember RFC 9309 group selection: once a group matches the bot, `*` no longer applies to it at all (details in [agent-readiness.md](agent-readiness.md#robotstxt-traps-that-change-the-verdict)).
2. **Actual access** — issue a request with that bot's documented UA string and compare status, body length and rendered content against the browser baseline. A 200 to Chrome and a 403 to `PerplexityBot` is an edge rule, and it is invisible in step 1. Note the limit `[practitioner]`: a spoofed-UA probe shows how the edge treats *unverified* traffic carrying that UA — a WAF challenging it may be correctly refusing an impersonator. Confirm what the verified bot actually receives in the WAF logs, and send spoofed probes only with the site owner's authorisation.

Report the two separately. "Declared allowed, edge-blocked" is a common and expensive state. Two robots.txt states change the verdict before any parsing `[documented: https://www.rfc-editor.org/rfc/rfc9309, 2026-10-12]`: a 5xx on `robots.txt` means crawlers must assume complete disallow, while a 4xx means they may access any resource. And a crawler you IP-block cannot read the file at all `[practitioner]`.

## Status vocabulary for reporting declared access

A seven-label scheme worth adopting verbatim, because each label supports a *different* conclusion `[practitioner]`:

| Status | Derivation | What you may conclude |
|---|---|---|
| `BLOCKED` | Own group, `Disallow: /` | Site-wide refusal, declared and deliberate |
| `PARTIALLY_BLOCKED` | Own group, some non-empty `Disallow` path | Path-level refusal — name the paths, never generalise to the site |
| `ALLOWED` | Own group, no blocking `Disallow` | Declared allow, **specific to that bot** |
| `BLOCKED_BY_WILDCARD` | No own group; `*` has `Disallow: /` | Refusal by inheritance — fixable without touching the bot's name |
| `ALLOWED_BY_DEFAULT` | No own group; `*` does not block | Allowed, but *unintentionally* — nobody decided this |
| `NOT_MENTIONED` | No own group and no `*` group | Silence, which REP reads as allow |
| `NO_ROBOTS_TXT` | 404 | Allow by absence; also worth flagging on its own |

The value is the distinction between the three "yes" states: `ALLOWED` is a decision, `ALLOWED_BY_DEFAULT` and `NOT_MENTIONED` are accidents that survive only until someone edits the `*` group. ⚠️ The implementation behind this table has a real limitation: it treats a group as blocking on `Disallow` presence and ignores `Allow` overrides, so it cannot model longest-match resolution. For a report, use it as a vocabulary; for a verdict on a complex file, use a REP-compliant parser (`google/robotstxt`, which resolves `Allow` overrides and wildcards).

## Audit the right bot list

geo-seo-claude's token list (`geo-seo-claude@scripts/fetch_page.py:215-228`) checks fourteen tokens `[practitioner]`: GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, `anthropic-ai`, PerplexityBot, CCBot, Bytespider, cohere-ai, Google-Extended, GoogleOther, Applebot-Extended, FacebookBot, Amazonbot.

Two defects to fix before reusing it `[practitioner]`:

- **It omits `Claude-SearchBot`** — the only token that governs citability in Claude's search features. A report built on this list cannot make a Claude-citability claim at all, while appearing to cover Anthropic.
- **It includes `anthropic-ai`**, which Anthropic's current crawler support article does not document. claude-seo (`skills/seo-geo/SKILL.md:190-192`) records removing that row "rather than kept as a guess" `[practitioner]`. A token nobody publishes produces a `NOT_MENTIONED` that means nothing.

Also missing and worth adding: `Perplexity-User`, `meta-externalagent`, `Google-CloudVertexBot`. The longer classified list (retrieval, engines, user-fetch, agents, training, special purpose) is in [ai-crawler-registry.md](ai-crawler-registry.md) — a list to test against, never a block list.

Crawler-table corrections (carried from claude-seo, see `## Attribution`) — Google-CloudVertexBot `[documented: https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers, 2026-10-11]`; Applebot-Extended `[documented: https://support.apple.com/en-us/119829, 2026-10-11]`; verification files `[documented: https://developers.openai.com/api/docs/bots, 2026-10-11]` `[documented: https://docs.perplexity.ai/guides/bots, 2026-10-11]` `[documented: https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers, 2026-10-11]` `[documented: https://claude.com/crawling/bots.json, 2026-10-12]`:

- **Google-CloudVertexBot** = site-owner-requested Vertex AI Agent crawls (honours robots.txt).
- Applebot-Extended does not crawl; it labels content Applebot already fetched — blocking it does not remove a site from Siri/Spotlight/Safari.
- Anthropic publishes IP prefixes at `claude.com/crawling/bots.json` (file `creationTime` 2026-10-07 when read). Other verification files: `openai.com/{gptbot,searchbot,chatgpt-user}.json`, `perplexity.com/perplexitybot.json`, Google `…/crawling/ipranges/user-triggered-agents.json`.
- (Claude-User honouring robots.txt and Google-GeminiNotebook replacing Google-NotebookLM (the old name) are already reflected in the next section.)

**Name the user-agent you checked and the capability it governs, in the report prose** `[practitioner]`. The pairings that get conflated most: ChatGPT Search citability is `OAI-SearchBot` (never `GPTBot`); Claude search citability is `Claude-SearchBot` (never `ClaudeBot`); Google Search and AI Overview eligibility is `Googlebot` (never `Google-Extended`); Siri/Spotlight/Safari discoverability is `Applebot` (never `Applebot-Extended`). The full policy table and the Google-Extended explanation are in skill `seo-technical` › crawl-and-index.

**A named group does not inherit `*`.** Google's spec: groups declared for the same specific user agent are «combined internally into a single group», but «User agent specific groups and global groups (*) are not combined» `[documented: https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec, 2026-10-11]`; RFC 9309 likewise merges all groups matching a product token and falls back to `*` only «If no matching group exists» `[documented: https://www.rfc-editor.org/rfc/rfc9309, 2026-10-12]`. Read every group naming the bot. A named group such as `User-agent: GPTBot` therefore drops every `*` rule it does not repeat; write each vendor group complete and test it as that bot, since other vendors' parsers are not documented here `[unvalidated house heuristic]`.

## Bots robots.txt cannot block

`[documented: https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers, 2026-10-11]` Google's user-triggered fetchers "generally ignore robots.txt rules", because a user requested the fetch. Google documents **Google-Agent** (agents hosted on Google infrastructure), **Google-GeminiNotebook** (fetches individual URLs that Gemini Notebook users add as sources) and **Google Messages** (link previews) as user-triggered. `Google-NotebookLM` is the old name, listed as a former agent supported until August 2026: update allowlists.

Other vendors differ, so never group them. OpenAI: for `ChatGPT-User`, "robots.txt rules may not apply" `[documented: https://developers.openai.com/api/docs/bots, 2026-10-11]`. Perplexity: `Perplexity-User` "generally ignores robots.txt rules" `[documented: https://docs.perplexity.ai/guides/bots, 2026-10-11]`. Anthropic: its bots, `Claude-User` included, "respect “do not crawl” signals by honoring industry standard directives in robots.txt" `[documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11]`. Blocking a fetcher that ignores robots.txt requires server-side access control, not a robots directive — and blocking it breaks a live fetch for a real person who pasted your link.

**Web Bot Auth** lets a bot authenticate cryptographically with HTTP Message Signatures (RFC 9421) `[documented: https://www.rfc-editor.org/rfc/rfc9421, 2026-10-12]` via a `Signature-Agent` header plus a key directory; Google is experimenting with it using the `https://agent.bot.goog` identity, and publishes reverse-DNS masks for its user-triggered fetchers `[documented: https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers, 2026-10-11]`. Correction from the current draft (`draft-ietf-webbotauth-httpsig-protocol-00`, 2026-09-01) `[documented: https://datatracker.ietf.org/doc/draft-ietf-webbotauth-httpsig-protocol/, 2026-10-12]`: `Signature-Agent` is now a **Dictionary** structured header (`sig1="https://signer.example"`); earlier versions used a bare string — test that your verifier accepts the new form; keys (RSA, EC or Ed25519) are published at `/.well-known/http-message-signatures-directory` and signatures carry `tag="web-bot-auth"`. Allowlist verified identity (IP ranges or signatures), never UA strings `[practitioner]`. This matters for the edge tier: once a bot can prove identity, "allow the real Googlebot, challenge the impersonators" becomes a WAF rule rather than a UA-string guess.

Google's crawling documentation **moved to `developers.google.com/crawling`** (migrated 2025-11-20) `[documented: https://developers.google.com/search/updates, 2026-10-11]`. Google's IP-range files are `common-crawlers.json`, `special-crawlers.json`, `user-triggered-fetchers.json`, `user-triggered-fetchers-google.json` and `user-triggered-agents.json` `[documented: https://developers.google.com/crawling/docs/crawlers-fetchers/verify-google-requests, 2026-10-12]`.
Google IP-range path and rename: unverified [unverified: the saved verify-google-requests text names the files but not their path or the googlebot.json rename]; see ## Unverified.
Update any allowlist automation that pins old file names `[practitioner]`.

## Fetch limits — the crawler that arrives and still misses your schema

When crawling for Google Search, Googlebot fetches the **first 2 MB of a supported file type** (HTML included) and the **first 64 MB of a PDF**, measured on the uncompressed data `[documented: https://developers.google.com/search/docs/crawling-indexing/googlebot, 2026-10-12]`; 15 MB is the default for Google's crawlers and fetchers in general `[documented: https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers, 2026-10-11]`. Inline base64 images, oversized inline CSS/JS and bloated navigation can push body content or a JSON-LD block past the cap, where it is simply not indexed. On a large Next.js route this is a live risk: inlined RSC payloads and hydration data sit in the document. Keep the primary content and every structured-data block inside the first 2 MB. Measure the **uncompressed HTTP response** (the cap applies to downloaded data, not the rendered DOM) and the byte offset of the essential content and JSON-LD in it; each referenced CSS/JS resource is fetched separately under the same limit, so check those individually `[documented: https://developers.google.com/search/docs/crawling-indexing/googlebot, 2026-10-14]`.

Crawl rate auto-adjusts: Googlebot slows down automatically on 500-range responses and slow response times, and the Search Console crawl rate limiter tool was deprecated on 8 January 2024 `[documented: https://developers.google.com/search/blog/2023/11/sc-crawl-limiter-byebye, 2026-10-12]`. Influence crawling through sitemaps, server responsiveness and robots controls.

## Google's AI citation surfaces and their controls (2026)

`[documented: https://developers.google.com/search/docs/appearance/ai-features, 2026-10-11]` **There is no AI-specific opt-out file.** Appearance in AI Overviews and AI Mode is governed by the ordinary preview and index directives — `nosnippet`, `data-nosnippet`, `max-snippet`, `noindex` — which are meta-robots tags, `X-Robots-Tag` headers or an HTML attribute, never `robots.txt` lines. Source: developers.google.com/search/docs/appearance/ai-features. Their AI reach is documented per directive: `nosnippet` «will also prevent the content from being used as a direct input for AI Overviews and AI Mode»; `max-snippet` «will also limit how much of the content may be used as a direct input», except where use was separately granted (structured data, a licence) `[documented: https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag, 2026-10-11]`. A supporting link needs a page «eligible to be shown in Google Search with a snippet», and a change waits for recrawl, «several days to several months» `[documented: https://developers.google.com/search/docs/appearance/ai-features, 2026-10-11]`. Trade-offs: skill `seo-technical` › crawl-and-index.
There is, since 2026-08-31, a **Search Console setting**: the **Search generative AI** control (Settings → include / exclude / inherit) decides whether a site's content can appear in AI Overviews, AI Mode and Discover's generative AI features; it "isn't used as a ranking or inclusion signal affecting other parts of Search" and "doesn't affect AI training" (training is Google-Extended) `[documented: https://support.google.com/webmasters/answer/16908024, 2026-10-11]`. Check it is on include before any GEO work.

Bing and Copilot controls (`noarchive`, `nocache`) are in the next section.

`[documented: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide, 2026-10-11]` **You do not need new machine-readable files, AI text files, markup or Markdown to appear in Google Search, including its generative AI capabilities**, and "structured data isn't required for generative AI search". Any recommendation that starts "first, add an AI file" is contradicted by the engine's own documentation.

Surfaces across AI Overviews and AI Mode:

- **Preferred Sources** — when a user selects an eligible domain or subdomain (not a subdirectory) as a preferred source, its content is more likely in that user's Top Stories and can carry a "preferred" badge, including in AI Mode and AI Overviews; there it needs the site to be included in Search generative AI features in Search Console. Publishers may offer Google's interactive button or a deeplink `[documented: https://developers.google.com/search/docs/appearance/preferred-sources, 2026-10-12]`. It is a per-user preference; do not promise a ranking lift from it `[practitioner]`.
- Other 2026 AI-surface features: unverified [unverified: no saved Google page describes them]; see ## Unverified.

`[documented: https://developers.google.com/search/docs/appearance/ai-features, 2026-10-11]` AI Overviews and AI Mode "may use different models and techniques, so the set of responses and links they show will vary" — score both rather than assuming one result transfers.

## Unverified

- Google IP-range path and rename: the source repo says the IP-range files live under `/crawling/ipranges/` and that `googlebot.json` was renamed `common-crawlers.json` [unverified: the saved verify-google-requests text names the files but not their path or the googlebot.json rename]
- Other 2026 AI-surface features: the source repo lists "Highly Cited" badges (earned by original reporting that other articles cite, not a markup), Community Perspectives (forum and firsthand content) and inline links, desktop hover Link Previews and link carousels, all served from the `Googlebot` index [unverified: no saved Google page describes them]

## Sources

- https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec — robots.txt specification, fetched 2026-10-11, saved as phase-2 sources/google/g-robots-spec.raw (group precedence).
- geo-seo-claude@scripts/fetch_page.py:20-26, 28-30, 215-228, 277-302 — the unused `AI_CRAWLERS` map and Chrome UA, the 14-token check list, the seven status labels.
- claude-seo@skills/seo-geo/SKILL.md:190-192, 206-223 — removal of the undocumented `anthropic-ai` row; the user-agent → capability reporting rule.

