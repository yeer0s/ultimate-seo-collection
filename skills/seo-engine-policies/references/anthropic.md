# Anthropic — policies, enforcement, controls
> last_verified: 2026-10-11 · market relevance: global (Claude model training, Claude search and user fetches); no market split documented · doc languages: en · coverage: ABSENT-SEARCHED · scope_exception: none

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

- Anthropic is an AI company, not a search engine with a spam policy. Its crawler article (dated «April 7, 2026» {an-crawler}) governs three robots: ClaudeBot (training), Claude-User (fetches at a user's request) and Claude-SearchBot (search quality). [documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11]
- What this page can answer: crawler access and opt-outs (§3, §8). What it cannot: "what gets a site penalised by Anthropic" — no such policy was found (§6).

## 2. Primary documents

| Document | URL | Language | Fetched | Governs |
|---|---|---|---|---|
| Does Anthropic crawl data from the web, and how can site owners block the crawler? (article 8896518, dated 2026-04-07) | https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler | en | 2026-10-11 | the three robots, robots.txt, Crawl-delay, opt-out |

## 3. Crawlers and verification

| Token | Purpose | Effect of disallowing it |
|---|---|---|
| ClaudeBot | collects content that could contribute to model training | future materials excluded from training datasets |
| Claude-User | fetches pages when a user asks Claude a question | no retrieval for user queries; may reduce visibility in user-directed search |
| Claude-SearchBot | indexes content to improve search results | no indexing for search; may reduce visibility in search results |

- The article gives tokens only, not full UA strings. robots.txt blocks are per host: «Please do this for every subdomain that you wish to opt out from.» {an-crawler} [documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11]
- Verification by IP: the article says «If a crawler has a source IP address on this list, it indicates that the crawler is coming from Anthropic.» {an-crawler}, but our saved text holds no list (§11). No reverse-DNS method is documented. [documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11]

## 4. Webmaster tools and submission

- No webmaster console, sitemap or URL submission is described; the controls are robots.txt (Disallow, Crawl-delay) and an email contact for malfunctioning bots. [documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11]

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

- No site-level prohibitions, demotion, de-indexing or ban were found in the documents searched (ABSENT-SEARCHED; absence not established); the read article covers crawler controls only: «Below is information on the three robots that Anthropic uses and how to set your site preferences» {an-crawler} [documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11]

## 7. Detection and recovery

- Report path for misbehaving bots: «believe that our Bots may be malfunctioning, please reach out to» {an-crawler} the address on the page (obfuscated in our saved copy). [documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11]
- Write from the site's domain: «Please reach out from an email that includes the domain you are contacting us about» {an-crawler} [documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11]
- IP blocking is not a reliable opt-out: «Alternate methods like blocking IP address(es) from which Anthropic Bots operates may not work correctly or persistently guarantee an opt-out» {an-crawler} [documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11]
- No timeline for a robots.txt change to take effect and no appeal path are stated. [documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11]

## 8. AI-use controls

| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 17 | ClaudeBot, Claude-User, Claude-SearchBot (robots.txt; Crawl-delay) | «Anthropic’s Bots respect “do not crawl” signals by honoring industry standard directives in robots.txt.» {an-crawler} | principles list | [documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11] |
| 18 | ClaudeBot (training opt-out) | «When a site restricts ClaudeBot access, it signals that the site's future materials should be excluded from our AI model training datasets.» {an-crawler} | bot table › ClaudeBot | [documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11] |

- Claude-User is covered by robots.txt: «Claude-User allows site owners to control which sites can be accessed through these user-initiated requests.» {an-crawler} [documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11]
- Its cost: «Disabling Claude-User on your site prevents our system from retrieving your content in response to a user query» {an-crawler} [documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11]
- Search opt-out: «Disabling Claude-SearchBot on your site prevents our system from indexing your content for search optimization» {an-crawler} [documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11]
- Crawl rate: «we support the non-standard Crawl-delay extension to robots.txt» {an-crawler}, example `User-agent: ClaudeBot` / `Crawl-delay: 1`. [documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11]
- Anti-bot measures: «we will not attempt to bypass CAPTCHAs for the sites we crawl.» {an-crawler} [documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11]
- The opt-out mechanism: «Opting out of being crawled by Anthropic Bots requires modifying the robots.txt file» {an-crawler} [documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11]

## 9. Delta from Google

- No spam policy, manual actions or reconsideration found in the documents searched (Google has all three, see google.md); the article governs crawler access only. [documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11]
- Crawl-delay: Anthropic supports the «non-standard Crawl-delay extension» {an-crawler} [documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11]; Google: «other fields such as crawl-delay aren't supported» {g-robots-spec} [documented: https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec, 2026-10-11]
- User-triggered fetches: Claude-User is under robots.txt control (§8) [documented: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler, 2026-10-11]; Google's user-triggered fetchers «generally ignore robots.txt rules» {g-user-fetchers} [documented: https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers, 2026-10-11]

## 10. Practitioner layer

- None in the corpora (engine-corpus-items.md: anthropic 0).

## 11. Unverified

- Anthropic crawler IP list: [unverified: the article refers to "this list" of source IPs, but the saved text holds no list or link to one]

## Sources

- https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler — Does Anthropic crawl data from the web, and how can site owners block the crawler? (Claude Help Center, dated 2026-04-07), fetched 2026-10-11, saved as phase-2 sources/anthropic/an-crawler.raw
- https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec — robots.txt specification (Google; §9 comparison only), fetched 2026-10-11, saved as phase-2 sources/google/g-robots-spec.raw
- https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers — Google user-triggered fetchers (§9 comparison only), fetched 2026-10-11, saved as phase-2 sources/google/g-user-fetchers.raw
