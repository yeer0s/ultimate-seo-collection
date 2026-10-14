# OpenAI — policies, enforcement, controls
> last_verified: 2026-10-11 · market relevance: global (ChatGPT search answers, GPT model training); no market split documented · doc languages: en · coverage: ABSENT-SEARCHED · scope_exception: none

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

- OpenAI is an AI company, not a search engine with a spam policy. Its one crawler document governs four agents: ChatGPT search (OAI-SearchBot), model training (GPTBot), user-triggered fetches in ChatGPT and Custom GPTs (ChatGPT-User) and ad landing-page checks (OAI-AdsBot). [documented: https://developers.openai.com/api/docs/bots, 2026-10-11]
- What this page can answer: crawler access and opt-outs (§3, §8). What it cannot: "what gets a site penalised by OpenAI" — no such policy was found (§6).

## 2. Primary documents

| Document | URL | Language | Fetched | Governs |
|---|---|---|---|---|
| Overview of OpenAI Crawlers | https://developers.openai.com/api/docs/bots | en | 2026-10-11 | the four user agents, robots.txt tags, IP files |

The §7.4 row "Publishers and developers FAQ" (help.openai.com article 12627856) was not used: that ID now serves an unrelated article (sources/INDEX.md, "Not found (searched)"). See §11.

## 3. Crawlers and verification

| Token | Purpose | robots.txt | IP file |
|---|---|---|---|
| OAI-SearchBot | surfaces sites in ChatGPT search | honoured; opt-out removes the site from search answers | `openai.com/searchbot.json` |
| GPTBot | crawls content that may be used for training | Disallow = do not train | `openai.com/gptbot.json` |
| ChatGPT-User | fetches a page when a user asks; not automatic crawling | "may not apply" | `openai.com/chatgpt-user.json` |
| OAI-AdsBot | visits only pages submitted as ads | not stated | `openai.com/adsbot.json` |

- User-agent strings carry the token plus a URL, e.g. «compatible; GPTBot/1.4; +https://openai.com/gptbot» {oa-bots}; version numbers may change. [documented: https://developers.openai.com/api/docs/bots, 2026-10-11]
- robots.txt fetches may carry a marker: «we may use a user-agent string with an additional robots.txt marker» {oa-bots}. [documented: https://developers.openai.com/api/docs/bots, 2026-10-11]
- Verification = UA token plus the published IP ranges (one JSON file per agent, table above): «allowing requests from our published IP ranges below» {oa-bots}. No reverse-DNS method is documented. [documented: https://developers.openai.com/api/docs/bots, 2026-10-11]

## 4. Webmaster tools and submission

- No webmaster console, sitemap submission, URL submission or IndexNow support is described on the crawler page. The only submission path mentioned is ads: OAI-AdsBot visits pages submitted as ads. [documented: https://developers.openai.com/api/docs/bots, 2026-10-11]

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

- No site-level prohibitions, demotion, de-indexing or ban were found in the documents searched (ABSENT-SEARCHED; absence not established); the read document covers crawler controls only: «OpenAI uses OAI-SearchBot and GPTBot robots.txt tags to enable webmasters to manage how their sites and content work with AI.» {oa-bots} [documented: https://developers.openai.com/api/docs/bots, 2026-10-11]
- The one policy check documented is on ads, not organic content: «When you submit an ad, OpenAI may visit the landing page to ensure it complies with our policies.» {oa-bots} [documented: https://developers.openai.com/api/docs/bots, 2026-10-11]

## 7. Detection and recovery

- No reconsideration or appeal path is named; the change channel is robots.txt: «Please use OAI-SearchBot in robots.txt for managing Search opt outs and automatic crawl.» {oa-bots} [documented: https://developers.openai.com/api/docs/bots, 2026-10-11]
- Timeline after a robots.txt change: «For search results, please note it can take ~24 hours from a site’s robots.txt update for our systems to adjust.» {oa-bots} [documented: https://developers.openai.com/api/docs/bots, 2026-10-11]
- Seeing the bots in logs: «The marker helps site owners more easily distinguish requests for the robots.txt file from requests for other resources» {oa-bots} [documented: https://developers.openai.com/api/docs/bots, 2026-10-11]

## 8. AI-use controls

| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 17 | OAI-SearchBot, GPTBot, ChatGPT-User, OAI-AdsBot (robots.txt tags) | «Because these actions are initiated by a user, robots.txt rules may not apply.» {oa-bots} | Overview › ChatGPT-User | [documented: https://developers.openai.com/api/docs/bots, 2026-10-11] |
| 18 | GPTBot (training opt-out); OAI-SearchBot (search-answer opt-out) | «Disallowing GPTBot indicates a site’s content should not be used in training generative AI foundation models.» {oa-bots} | Overview › GPTBot | [documented: https://developers.openai.com/api/docs/bots, 2026-10-11] |

- Search opt-out: «Sites that are opted out of OAI-SearchBot will not be shown in ChatGPT search answers, though can still appear as navigational links.» {oa-bots} [documented: https://developers.openai.com/api/docs/bots, 2026-10-11]
- Settings are separate: «Each setting is independent of the others» — «a webmaster can allow OAI-SearchBot in order to appear in search results while disallowing GPTBot» {oa-bots} [documented: https://developers.openai.com/api/docs/bots, 2026-10-11]
- Shared crawl: «If your site has allowed both bots, we may use the results from just one crawl for both use cases» {oa-bots} [documented: https://developers.openai.com/api/docs/bots, 2026-10-11]
- ChatGPT-User does not decide search inclusion: «ChatGPT-User is not used to determine whether content may appear in Search.» {oa-bots} [documented: https://developers.openai.com/api/docs/bots, 2026-10-11]
- OAI-AdsBot: «OAI-AdsBot only visits pages submitted as ads» and «the data collected by OAI-AdsBot is not used to train generative AI foundation models.» {oa-bots} [documented: https://developers.openai.com/api/docs/bots, 2026-10-11]

## 9. Delta from Google

- No spam policy, manual actions or reconsideration found in the documents searched (Google has all three, see google.md); OpenAI's read document governs crawler access only. [documented: https://developers.openai.com/api/docs/bots, 2026-10-11]
- The user-triggered agent may ignore robots.txt («robots.txt rules may not apply» {oa-bots}), so robots.txt is not a full block on ChatGPT reading a page. [documented: https://developers.openai.com/api/docs/bots, 2026-10-11]
- Opting out of search does not remove every mention: opted-out sites «can still appear as navigational links» {oa-bots}. [documented: https://developers.openai.com/api/docs/bots, 2026-10-11]

## 10. Practitioner layer

- Track AI visibility by running a fixed prompt set across ChatGPT, Perplexity, Gemini and AI Overviews and logging citations and brand mentions; technical practitioners prefer crawler logs over prompt dashboards. [practitioner: anonymised sources · consensus · 5 thr / 54 · newest 2026-08] (skill `seo-evidence`, practitioner-agentic)

## 11. Unverified

- OpenAI publishers FAQ: [unverified: help.openai.com article 12627856 serves an unrelated article on 2026-10-11; no publisher FAQ located, so any publisher-side rules it held are unread]

## Sources

- https://developers.openai.com/api/docs/bots — Overview of OpenAI Crawlers, fetched 2026-10-11, saved as phase-2 sources/openai/oa-bots.raw
