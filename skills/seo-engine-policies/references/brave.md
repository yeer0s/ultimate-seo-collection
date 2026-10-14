# Brave Search — policies, enforcement, controls
> last_verified: 2026-10-11 · market relevance: low for PT (results languages listed: US/UK English, French, German, Japanese); default in Brave browser for some users · doc languages: en · coverage: ABSENT-SEARCHED · scope_exception: none

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

- Brave Search runs its own index: «Brave delivers results from its own, built-from-scratch index.» {br-search} [documented: https://brave.com/search/, 2026-10-11]
- It is sold to others: «We also offer API access to Brave Search so it can power other search engines.» {br-search} [documented: https://brave.com/search/, 2026-10-11]
- Languages: «Brave Search is available in US and UK English, as well as French, German, and Japanese.» {br-search} — Portuguese is not listed. [documented: https://brave.com/search/, 2026-10-11]
- Its AI answers draw on the same results: «These summaries are based solely on Web search results» {br-search}. [documented: https://brave.com/search/, 2026-10-11]
- No spam policy or webmaster guidelines were found (sources/INDEX.md, "Not found (searched)"); see §6.

## 2. Primary documents

| Document | URL | Language | Fetched | Governs |
|---|---|---|---|---|
| Brave Search Crawler (help) | https://search.brave.com/help/brave-search-crawler | en | 2026-10-11 | crawler, robots.txt, noindex, delisting, re-fetch |
| What is Brave Search? | https://brave.com/search/ | en | 2026-10-11 | index, ranking/downranking stance, AI answers, fallback mixing |

The help index (search.brave.com/help, incl. the "AI in Brave Search" article it links) returned HTTP 429 and was not read (§11).

## 3. Crawlers and verification

- No own user-agent token: «The Brave Search crawler does not advertise a differentiated user agent» {br-crawler} — so it cannot be named in robots.txt or verified by UA. [documented: https://search.brave.com/help/brave-search-crawler, 2026-10-11]
- It follows Googlebot's access: «if a domain or page is not crawlable by Googlebot, then Brave Search’s bot will not crawl it either.» {br-crawler} [documented: https://search.brave.com/help/brave-search-crawler, 2026-10-11]
- No IP list or reverse-DNS method is documented.
- Discovery is partly from users: the crawler is «partially powered by information provided by users enrolled in the Web Discovery Project» {br-crawler} (opt-in, in Brave browser). [documented: https://search.brave.com/help/brave-search-crawler, 2026-10-11]

## 4. Webmaster tools and submission

- No webmaster console, sitemap submission or IndexNow support is described. Two URL forms exist: re-fetch («You can submit your page for re-fetching here.» {br-crawler}) and delisting a page that no longer exists. [documented: https://search.brave.com/help/brave-search-crawler, 2026-10-11]

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

- Stated policy: «No, Brave Search does not filter, downrank, or censor search results.» {br-search} [documented: https://brave.com/search/, 2026-10-11]
- The one exception is legal: «We do need to comply with laws governing search engines, including CSAM, copyright takedown (DMCA), right to be forgotten (GDPR), and nation-state orders.» {br-search} [documented: https://brave.com/search/, 2026-10-11]
- Google's actions can pass through when a user enables fallback mixing: «If you’ve enabled fallback mixing, and a result is censored, filtered, or re-ranked in Google, those changes would pass through to our results.» {br-search} [documented: https://brave.com/search/, 2026-10-11]

## 7. Detection and recovery

- Delisting your own page: «A site owner can delist a page by using the robots noindex directive.» {br-crawler} [documented: https://search.brave.com/help/brave-search-crawler, 2026-10-11]
- It takes effect only after a re-fetch: «Brave needs to re-fetch it in order to apply the changes» {br-crawler}; no timeline is given. [documented: https://search.brave.com/help/brave-search-crawler, 2026-10-11]
- Personal data: «you should follow the guidance and process of the Right To Be Forgotten.» {br-crawler} [documented: https://search.brave.com/help/brave-search-crawler, 2026-10-11]
- Dead pages still shown: «you can submit your URL here» {br-crawler} (or email the not-found address on the page). No reconsideration path or penalty system was found in the documents searched. [documented: https://search.brave.com/help/brave-search-crawler, 2026-10-11]

## 8. AI-use controls

| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 17 | Brave Search crawler (no own UA; follows Googlebot access; noindex) | «if a domain or page is not crawlable by Googlebot, then Brave Search’s bot will not crawl it either.» {br-crawler} | Brave Search Crawler | [documented: https://search.brave.com/help/brave-search-crawler, 2026-10-11] |
| 18 | — | not addressed | — | — |

- robots.txt does not keep a page out of the index: «Note that robots.txt is not used to prevent a page from being indexed.» {br-crawler} [documented: https://search.brave.com/help/brave-search-crawler, 2026-10-11]
- Why there is no token: «we must avoid discrimination from websites that allow only Google to crawl them» {br-crawler} [documented: https://search.brave.com/help/brave-search-crawler, 2026-10-11]
- AI-answers / training opt-out: unverified [unverified: none found in br-crawler or br-search; the help index was rate-limited]; see §11.

## 9. Delta from Google

- No own crawler token, so robots.txt rules aimed at Googlebot also govern Brave (§3). [documented: https://search.brave.com/help/brave-search-crawler, 2026-10-11]
- No spam policy found in the documents searched; Brave states it does not downrank, except for legal compliance (§6); no manual-action or reconsideration system is documented in them. [documented: https://brave.com/search/, 2026-10-11]
- Users can re-rank results with Goggles: «Goggles will act as a re-ranking option on top of the Brave Search index.» {br-search} [documented: https://brave.com/search/, 2026-10-11]

## 10. Practitioner layer

- None in the corpora (engine-corpus-items.md: brave 0).

## 11. Unverified

- AI-answers / training opt-out: [unverified: no Brave document read in this run offers an opt-out from AI answers or training; sources/INDEX.md logs the search as not found]
- Brave Search help index: [unverified: search.brave.com/help returned HTTP 429 on 2026-10-11; its linked articles (e.g. "AI in Brave Search") were not read]

## Sources

- https://search.brave.com/help/brave-search-crawler — Brave Search Crawler, fetched 2026-10-11, saved as phase-2 sources/brave/br-crawler.raw
- https://brave.com/search/ — What is Brave Search?, fetched 2026-10-11, saved as phase-2 sources/brave/br-search.raw
