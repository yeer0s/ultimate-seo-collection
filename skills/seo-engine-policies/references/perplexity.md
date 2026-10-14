# Perplexity — policies, enforcement, controls
> last_verified: 2026-10-11 · market relevance: global (Perplexity answer engine); no market split documented · doc languages: en · coverage: ABSENT-SEARCHED · scope_exception: none

## Contents

- 1. Who uses this index
- 2. Primary documents
- 3. Crawlers and verification
- 4. Webmaster tools and submission
- 5. What is prohibited
- 6. Enforcement
- 7. Detection and recovery
- 8. AI-use controls
- 9. Delta from Google
- 10. Practitioner layer
- 11. Unverified
- Sources

## 1. Who uses this index

- Perplexity is an AI answer engine, not a search engine with a spam policy. Its crawler document governs two agents: PerplexityBot (search results on Perplexity) and Perplexity-User (fetches made when a user asks a question). [documented: https://docs.perplexity.ai/guides/bots, 2026-10-11]
- What this page can answer: crawler access, WAF allow-listing and training statements (§3, §8). What it cannot: "what gets a site penalised by Perplexity" — no such policy was found (§6).

## 2. Primary documents

| Document | URL | Language | Fetched | Governs |
|---|---|---|---|---|
| Perplexity Crawlers | https://docs.perplexity.ai/guides/bots | en | 2026-10-11 | the two user agents, robots.txt tags, IP files, WAF setup |

## 3. Crawlers and verification

| Token | Purpose | robots.txt | IP file |
|---|---|---|---|
| PerplexityBot | surfaces and links sites in Perplexity search results; not for AI foundation models | honoured (robots.txt tag) | `perplexity.com/perplexitybot.json` |
| Perplexity-User | visits a page to answer a user's question and link it | "generally ignores robots.txt rules" | `perplexity.com/perplexity-user.json` |

- Full UA strings: «compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot» and «compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user» {px-bots}. [documented: https://docs.perplexity.ai/guides/bots, 2026-10-11]
- Verification = UA plus IP: «combine both User-Agent string matching and IP address verification» {px-bots}; the JSON endpoints are «the source of truth for your WAF configurations» {px-bots}. No reverse-DNS method is documented. [documented: https://docs.perplexity.ai/guides/bots, 2026-10-11]
- The page gives step-by-step allow rules for Cloudflare WAF and AWS WAF (UA contains the token AND source IP in the published ranges, action Allow). [documented: https://docs.perplexity.ai/guides/bots, 2026-10-11]

## 4. Webmaster tools and submission

- No webmaster console, sitemap submission, URL submission or IndexNow support is described; the controls are robots.txt tags and WAF rules. [documented: https://docs.perplexity.ai/guides/bots, 2026-10-11]

## 5. What is prohibited

| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 1 | — | not addressed | — | — |
| 2 | — | not addressed | — | — |
| 3 | — | not addressed | — | — |
| 4 | — | not addressed | — | — |
| 5 | — | not addressed | — | — |
| 6 | — | not addressed | — | — |
| 7 | — | not addressed | — | — |
| 8 | — | not addressed | — | — |
| 9 | — | not addressed | — | — |
| 10 | — | not addressed | — | — |
| 11 | — | not addressed | — | — |
| 12 | — | not addressed | — | — |
| 13 | — | not addressed | — | — |
| 14 | — | not addressed | — | — |
| 15 | — | not addressed | — | — |
| 16 | — | not addressed | — | — |

## 6. Enforcement

- No site-level prohibitions, demotion, de-indexing or ban were found in the documents searched (ABSENT-SEARCHED; absence not established); the read document covers crawler controls only: «Webmasters can use the following robots.txt tags to manage how their sites and content interact with Perplexity.» {px-bots} [documented: https://docs.perplexity.ai/guides/bots, 2026-10-11]

## 7. Detection and recovery

- Timeline after a robots.txt change: «Each setting works independently, and it may take up to 24 hours for our systems to reflect changes.» {px-bots} [documented: https://docs.perplexity.ai/guides/bots, 2026-10-11]
- Checking access: «Monitor your logs to ensure the rules are working as expected» {px-bots}; no reconsideration or appeal path is named. [documented: https://docs.perplexity.ai/guides/bots, 2026-10-11]

## 8. AI-use controls

| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 17 | PerplexityBot, Perplexity-User (robots.txt tags) | «Since a user requested the fetch, this fetcher generally ignores robots.txt rules.» {px-bots} | Perplexity Crawlers › Perplexity‑User | [documented: https://docs.perplexity.ai/guides/bots, 2026-10-11] |
| 18 | PerplexityBot (search, not training) | «It is not used to crawl content for AI foundation models.» {px-bots} | Perplexity Crawlers › PerplexityBot | [documented: https://docs.perplexity.ai/guides/bots, 2026-10-11] |

- PerplexityBot's job: «PerplexityBot is designed to surface and link websites in search results on Perplexity.» {px-bots} [documented: https://docs.perplexity.ai/guides/bots, 2026-10-11]
- Perplexity-User and training: «It is not used for web crawling or to collect content for training AI foundation models.» {px-bots} [documented: https://docs.perplexity.ai/guides/bots, 2026-10-11]
- The same page also says «Perplexity-User controls which sites these user requests can access.» {px-bots} — read together with row 17, robots.txt is not a dependable block for user fetches. [documented: https://docs.perplexity.ai/guides/bots, 2026-10-11]

## 9. Delta from Google

- No spam policy, manual actions or reconsideration found in the documents searched (Google has all three, see google.md); the read document governs crawler access only. [documented: https://docs.perplexity.ai/guides/bots, 2026-10-11]
- The user-triggered fetcher «generally ignores robots.txt rules» {px-bots}, so robots.txt is not a dependable block for it. [documented: https://docs.perplexity.ai/guides/bots, 2026-10-11]
- Blocking it with a WAF rule on UA + published IP ranges is our inference, not Perplexity's instruction (its WAF steps set the action to Allow); confirm in server logs that the blocked requests stop. [hypothesis]
- The page asks sites to allow-list its bots in WAFs, with IP ranges «updated regularly» {px-bots}. [documented: https://docs.perplexity.ai/guides/bots, 2026-10-11]

## 10. Practitioner layer

- Track AI visibility by running a fixed prompt set across ChatGPT, Perplexity, Gemini and AI Overviews and logging citations and brand mentions; technical practitioners prefer crawler logs over prompt dashboards. [practitioner: anonymised sources · consensus · 5 thr / 54 · newest 2026-08] (skill `seo-evidence`, practitioner-agentic)

## 11. Unverified

- None: every claim above is on the read crawler page; nothing else was located for Perplexity in this run.

## Sources

- https://docs.perplexity.ai/guides/bots — Perplexity Crawlers, fetched 2026-10-11, saved as phase-2 sources/perplexity/px-bots.raw
