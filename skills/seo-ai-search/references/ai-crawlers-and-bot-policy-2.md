<!-- split-header-2: part 2 of 2 of ai-crawlers-and-bot-policy.md (original lines 100–177; boundary H2) -->
# AI crawlers and bot policy (2 of 2) — non-Google controls, the edge gate in practice
## Contents

- Non-Google surfaces: documented controls
- The edge gate, in practice
- Cross-references
- Unverified
- Attribution
- Sources

Other parts of the same original file: [ai-crawlers-and-bot-policy.md](ai-crawlers-and-bot-policy.md).

<!-- /split-header-2 -->
## Non-Google surfaces: documented controls

Only provider-documented behaviour; upstream re-verified 2026-07-30, not re-fetched here except where a 2026-10-11 read is cited. Eligibility never guarantees selection.

| Surface | Documented control | Site-owner action |
|---|---|---|
| ChatGPT Search | `OAI-SearchBot` governs search eligibility; `GPTBot` = model-improvement crawling; `ChatGPT-User` = user-triggered visits, not a search control. Separate published IP ranges. `[documented: https://developers.openai.com/api/docs/bots, 2026-10-11]` | Allow `OAI-SearchBot` + its IPs at the edge if citation is wanted; decide `GPTBot` on training policy alone. |
| Perplexity | `PerplexityBot` surfaces and links sites in results; `Perplexity-User` performs user-requested fetches and **generally ignores robots.txt**; IP ranges and WAF guidance published for both. `[documented: https://docs.perplexity.ai/guides/bots, 2026-10-11]` | robots for `PerplexityBot`; verify WAF against both UAs and current IP lists. |
| Claude | `Claude-SearchBot` = search indexing; `Claude-User` = user-directed retrieval; `ClaudeBot` = possible model development. `[documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11]` | Allowing `ClaudeBot` is not a search-visibility control. |
| Gemini API + Google Search grounding | Gemini google_search citation behaviour: unverified [unverified: ai.google.dev grounding page not readable by curl on 2026-10-12 (HTTP 302)]; see ## Unverified. | Never report Gemini API citation fields as Google Search signals. |
| Microsoft Copilot Studio (public-web grounding) | Uses **Bing Custom Search** restricted to the configured domains, then grounding and provenance checks; Microsoft recommends sitemaps, Bingbot crawlability and IndexNow. Scoped to Copilot Studio, not every consumer Copilot. `[documented: https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/generative-ai-public-websites, 2026-10-12]` | Keep Bing indexation fresh; name the exact Copilot product in any finding. |
| Brave Search | Independent index; crawler has **no distinct user-agent**; if a page is not crawlable by Googlebot, Brave's crawler will not crawl it; delisting via `noindex` after re-fetch. `[documented: https://search.brave.com/help/brave-search-crawler, 2026-10-11]` | Brave access follows your Googlebot rules; verify in Brave itself. Do not assume Brave is any assistant's fixed backend. |
| Bing + Copilot | `noarchive` — "NOARCHIVE prevents content from being used in Copilot responses and grounding results"; `nocache` — "NOCACHE limits Copilot to using only the URL, title, and snippet" (both quotes: Bing Webmaster Guidelines, https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, read 2026-10-11). Content with either tag still appears in Bing's ordinary results; a page carrying both is treated as `nocache` (Bing blog, 2023-09-22, https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat). `[documented: https://www.bing.com/webmasters/help/robots-meta-tags-and-attributes-that-bing-supports-5198d240, 2026-10-11]` | These are Bing's controls, not Google's. Do not ship `noarchive` on a site that wants Copilot citations. |

No published crawler/index contract for a provider → record the gap; never derive a durable rule from one answer or one referral.

**Training-reservation is not only robots.txt** (upstream legal note; verify for the client's jurisdiction). DSM Art. 4 and AI Act Art. 53: unverified [unverified: EUR-Lex texts not readable by curl on 2026-10-12]; see ## Unverified. robots.txt signals intent but is not a complete training opt-out or licence; pair it with terms, access control and a machine-readable rights reservation where adopted.

**Observation record (every platform check):** query · locale · date · account / logged-in state · device · surfaced URL · cited passage · repeat count. Separate official requirements, measured observations and hypotheses in the write-up. The full measurement protocol is in [ai-citation-measurement.md](ai-citation-measurement.md).

## The edge gate, in practice

`SKILL.md` and skill `seo-authority` › authority-trust-and-distribution already state the rule: confirm the target engine's bot is allowed at the edge before recommending any GEO tactic. The operational form `[practitioner]`:

1. Enumerate the CDN/WAF bot policy's allowed and challenged agents (on mowei.pt this is the Cloudflare AI-crawler policy) and write the list down with a date.
2. For each engine you intend to be cited by, send a request with that bot's documented UA and record status + body length against the Chrome baseline.
3. Re-run step 2 **after every Cloudflare rule edit** — a managed-ruleset update can change bot verdicts without anyone touching `robots.txt`, and the failure is silent.
4. Only then propose page-level changes. A tactic aimed at a bot that receives a 403 is dead on arrival, and no ranking tool will ever show you that.

⚠️ A JS-challenge page returns **200** with a body. Length-compare against the browser baseline and look for challenge markers; status alone will not catch it.

**Proof-of-work and JS challenges** `[practitioner]`: tools such as `TecharoHQ/anubis` put a proof-of-work JS challenge in front of the origin; its own README calls this "a bit of a nuclear response" that "may inhibit 'good bots'" unless they are allowlisted. Most AI crawlers do not execute JavaScript, so a challenged bot reads nothing, and the challenge page still answers 200. Whenever Anubis or any PoW/JS gate sits in front of the site, run step 2 above as **each** bot you want citing you, and allowlist only verified Googlebot and Bingbot plus the verified AI bots you intend to be cited by.

### Cloudflare managed robots

Cloudflare can **prepend** a managed block of its own at the top of the robots.txt that the edge returns; that block disallows GPTBot, ClaudeBot, Google-Extended and other tokens `[practitioner]`. The block exists only in the response the edge sends, so anyone reading the file in the repository or on the origin never sees it. To detect it, fetch `https://<host>/robots.txt` through the edge and search, case-insensitively, for the comment `# BEGIN Cloudflare Managed content`; the block closes at `# END Cloudflare Managed Content`.

Rule for mowei.pt, which sits behind Cloudflare `[practitioner]`: the edge-gate procedure gets a **step 0** — after any change in the Cloudflare dashboard, diff the robots.txt the edge actually serves against the deployed file. A managed block that disallows `OAI-SearchBot` or `Claude-SearchBot` blocks citations, and no code review will ever surface it. The same managed block writes `Content-Signal` into the `*` group only, which named groups never read — see the group-selection trap in [agent-readiness.md](agent-readiness.md#robotstxt-traps-that-change-the-verdict). One more trap when auditing Content-Signal with third-party tools: geo-seo-claude's agent step validates the wrong keys (`ai-train, search, ai-personalization, ai-retrieval`) and flags `ai-input` as unknown, while Cloudflare's published policy uses `search`, `ai-input`, `ai-train`; the IETF individual draft it cites expired on 2026-04-04.

On each ai.robots.txt release, re-test the retrieval-class tokens through this gate ([ai-crawler-registry.md](ai-crawler-registry.md#how-to-use)).

## Cross-references

- skill `seo-technical` › crawl-and-index § AI crawlers — the access decision behind every GEO tactic — the crawler policy table, training vs retrieval, the named-group-does-not-inherit-`*` trap, the robots.txt stanza, `nosnippet`/`max-snippet`/`data-nosnippet`. The policy lives there; only the evidence discipline lives here.
- skill `seo-technical` › crawl-and-index § Crawlability — `Allow: /` ordering and first-match vs longest-match parser disagreement.
- `ai-retrieval-and-citation.md#how-ai-answer-engines-actually-retrieve-rag--query-fan-out` and `#llmstxt--not-a-searchvisibility-lever` — retrieval mechanics and the llms.txt evidence position.
- skill `seo-evidence` › experiments-and-revert-2 § AI-citation measurement — measuring citations once access is proven.
- skill `seo-authority` › authority-trust-and-distribution — the edge-gate rule in its distribution context.
- [agent-readiness.md](agent-readiness.md) — what agents can reach and act on, Content-Signal, Lighthouse Agentic Browsing.
- [ai-crawler-registry.md](ai-crawler-registry.md) — the classified ai.robots.txt token list and the whole-word matching rule.

## Unverified

- Gemini google_search citation behaviour: the Gemini API `google_search` tool returns inline citation annotations; this is developer-API behaviour, distinct from eligibility in Google Search AI features — never report Gemini API citation fields as Google Search signals [unverified: ai.google.dev grounding page not readable by curl on 2026-10-12 (HTTP 302)].
- DSM Art. 4 and AI Act Art. 53: EU DSM Directive (Dir. (EU) 2019/790) TDM reservations under Art. 4 and the EU AI Act (Reg. (EU) 2024/1689) Art. 53 copyright-policy obligation on general-purpose AI providers can matter for rights-reserved content [unverified: EUR-Lex texts not readable by curl on 2026-10-12].

## Attribution

- AgriciDaniel/claude-seo — Copyright (c) 2026 agricidaniel — MIT License. The crawler-table corrections in "Audit the right bot list" are carried from its google-ledger delta (phase-2 adapted file).
- aaron-he-zhu/aaron-marketing-skills — Copyright 2024 Aaron He Zhu; modified — rows already in our library removed, wording condensed — Apache License 2.0. Modified: carried the "Documented discovery and retrieval controls" table, the training-reservation note and the observation record into "Non-Google surfaces: documented controls"; converted its labels to our label set; merged our existing Bing `noarchive`/`nocache` paragraph into the table as one row.

## Sources

- `geo-seo-claude@scripts/fetch_page.py:20-26, 28-30` — `AI_CRAWLERS` UA map defined and never used; Chrome UA in `DEFAULT_HEADERS`. Carried as the caution above, `[practitioner]`. Verified by repo-wide grep: one hit, the definition.
- `geo-seo-claude@scripts/fetch_page.py:215-228` — the 14-token check list (topic list cited `:215-230`; the list itself ends at `:228`). Carried with two corrections, `[practitioner]`.
- `geo-seo-claude@scripts/fetch_page.py:277-302` — the seven status labels (topic list cited `:276-306`). Vocabulary carried; the `Allow`-blind implementation noted.
- `claude-seo@skills/seo-geo/SKILL.md:150-223` — crawler table, claim→bot pairing, user-triggered fetchers, Web Bot Auth. Policy table deliberately NOT carried (lives in skill `seo-technical` › crawl-and-index); the reporting rule carried; provenance only, the body labels it.
- `claude-seo@skills/seo-geo/SKILL.md:303-320` — 2026 AI citation surfaces and controls; provenance only, the body labels each claim from the Google page read.
- `claude-seo@skills/seo-technical/SKILL.md:30, 93` — Googlebot fetch limits, crawl-rate control removal, user-triggered fetchers, Web Bot Auth, `developers.google.com/crawling` migration; provenance only (repo transcription, not a primary read).
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide — no AI files/markup required; structured data not required for generative AI search. Checked 2026-09-22.
- https://developers.google.com/search/docs/appearance/ai-features — AI-feature appearance governed by standard preview/index directives. Checked via source repo 2026-09-22.
- https://developers.google.com/search/docs/appearance/preferred-sources — Preferred Sources is a per-user preference. Checked via source repo 2026-09-22.
- https://developers.openai.com/api/docs/bots · https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers · https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers · https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler · https://docs.perplexity.ai/guides/bots · https://support.apple.com/en-us/119829 — vendor crawler documentation, all read raw 2026-10-11 (phase-2 sources index); re-verify token names on every AI-visibility audit rather than trusting any table, this one included.
- https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a — Bing Webmaster Guidelines (2026 rewrite), read 2026-10-11 through Bing's help endpoint; NOARCHIVE / NOCACHE wording.
- https://www.bing.com/webmasters/help/robots-meta-tags-and-attributes-that-bing-supports-5198d240 · https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat — Bing robots meta tags and the 2023-09-22 Bing Chat controls.
- https://support.google.com/webmasters/answer/16908024 — Search generative AI control, read 2026-10-11.
- AgriciDaniel/claude-seo@skills/seo-agentic/SKILL.md and AgriciDaniel/claude-seo@skills/seo-agentic/references/access-policy.md (phase-2 adapted file research/adapted/AgriciDaniel__claude-seo/agent-readiness-and-access-policy.md) — access-policy corrections: RFC 9309 group selection, 5xx/4xx robots.txt, IP-block trap, spoofed-UA probe limits, Web Bot Auth dictionary form, verified-identity allowlisting. INTEGRATE, MIT.
- AgriciDaniel/claude-seo@data/google-updates.json, AgriciDaniel/claude-seo@skills/seo-geo/SKILL.md:140-330 (phase-2 adapted file research/adapted/AgriciDaniel__claude-seo/google-ledger-and-ai-guide-delta-2026-10.md) — crawler-table corrections only (Google-CloudVertexBot, Applebot-Extended, Anthropic IP file); Claude-User and Google-GeminiNotebook were already corrected here. COPY, MIT.
- aaron-he-zhu/aaron-marketing-skills@seo-geo/implement/geo-content-optimizer/references/ai-citation-patterns.md, seo-geo/tune/technical-seo-checker/references/llm-crawler-handling.md (phase-2 adapted file research/adapted/aaron-he-zhu__aaron-marketing-skills/ai-surface-retrieval-controls.md) — non-Google surface controls table, training-reservation note, observation record. COPY, Apache-2.0.
- zubair-trabzada/geo-seo-claude@scripts/fetch_page.py:248-253, tests/test_fetch_robots_cloudflare.py:18-29, agents/geo-ai-visibility.md:81, tests/agent-readiness-test-results.md:34 (phase-2 adapted file research/adapted/zubair-trabzada__geo-seo-claude/cloudflare-managed-robots-and-parser-traps.md) — Cloudflare managed-block detection, mowei.pt step 0, Content-Signal key defect. INTEGRATE, MIT.
- google/robotstxt@README.md (phase-2 adapted file research/adapted/group-E__readme-tool-repos/tool-stack-by-job.md, row A23-a) — the named REP parser, its exit codes and its two limits. INTEGRATE, Apache-2.0.
- TecharoHQ/anubis@README.md:98 (phase-2 adapted file research/adapted/group-E__readme-tool-repos/tool-stack-by-job.md, row A23-c) — PoW/JS challenge as an edge-gate risk; test as each bot. INTEGRATE, MIT.
