# Google — policies, enforcement, controls
> last_verified: 2026-10-11 · market relevance: global · doc languages: en · coverage: COMPLETE · scope_exception: none

## Contents
- §1 Users · §2 Documents · §3 Crawlers · §4 Tools · §5 Prohibited · §6 Enforcement · §7 Recovery · §8 AI controls · §9 Delta · §10 Practitioner · §11 Unverified · Sources

## 1. Who uses this index
- Google web search, incl. Google's own properties, plus Discover/News notes (§6). Gemini, AI Overviews, AI Mode, Google-Extended: skill `seo-engine-policies` › google-ai.

## 2. Primary documents
| Document | URL | Language | Fetched | Governs |
|---|---|---|---|---|
| Spam policies | https://developers.google.com/search/docs/essentials/spam-policies | en | 2026-10-11 | §5 |
| Manual actions report | https://support.google.com/webmasters/answer/9044175 | en | 2026-10-11 | §6–§7 |
| Reconsideration requests | https://support.google.com/webmasters/answer/35843 | en | 2026-10-11 | §7 |
| Site reputation update (2026-08-28) | https://developers.google.com/search/blog/2026/08/update-site-reputation-policy | en | 2026-10-11 | §6 |
| Site reputation abuse (2024-11-19) | https://developers.google.com/search/blog/2024/11/site-reputation-abuse | en | 2026-10-11 | §6 |
| Back button hijacking (2026-04-13) | https://developers.google.com/search/blog/2026/04/back-button-hijacking | en | 2026-10-11 | §6 |
| Quality Rater Guidelines, version 2025-09-11 | https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf | en | 2026-10-11 | raters |
| Crawlers overview | https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers | en | 2026-10-11 | §3 |
| robots.txt spec | https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec | en | 2026-10-11 | §3, §8 |
| Robots meta tag | https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag | en | 2026-10-11 | §8 |
| Disavow links | https://support.google.com/webmasters/answer/2648487 | en | 2026-10-11 | §7 |

- QRG: a claimed June 2026 edition is not real; the live PDF still shows «September 11, 2025» {g-qrg} [documented: https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf, 2026-10-11]

## 3. Crawlers and verification
- Common crawlers «always respect robots.txt rules for automatic crawls»; verify by user agent, source IP and reverse DNS {g-crawlers-overview} [documented: https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers, 2026-10-11]
- robots.txt: no crawl-delay; 500 KiB cap; generally cached ≤24 h, longer if refresh fails; 4xx (not 429) = no limits; 5xx = crawl stops 12 h, then last good copy ≤30 days {g-robots-spec} [documented: https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec, 2026-10-11]

## 4. Webmaster tools and submission
- Search Console: Manual actions, Security issues and Links reports; disavow tool (§7). IndexNow: not documented.

## 5. What is prohibited
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 1 | Cloaking | «presenting different content to users and search engines with the intent to manipulate search rankings and mislead users» {g-spam}; paywall exempt only if Google sees the full content **and** Flexible Sampling guidance is followed | Cloaking | [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11] |
| 2 | Doorway abuse | «created to rank for specific, similar search queries. They lead users to intermediate pages that aren't as useful as the final destination» {g-spam} | Doorway abuse | [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11] |
| 3 | Hidden text and link abuse | «not to be easily viewable by human visitors» {g-spam} | Hidden text | [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11] |
| 4 | Keyword stuffing | «filling a web page with keywords or numbers» {g-spam} | Keyword stuffing | [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11] |
| 5 | Link spam | «creating links to or from a site primarily for the purpose of manipulating search rankings» {g-spam} | Link spam | [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11] |
| 6 | Scaled content abuse | «little to no value to users, no matter how it's created» {g-spam} | Scaled content abuse | [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11] |
| 7 | Scraping | «taking content from other sites, often through automated means, and hosting it with the purpose of manipulating search rankings» {g-spam} | Scraping | [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11] |
| 8 | Sneaky redirects | «show users and search engines different content or show users unexpected content» {g-spam} | Sneaky redirects | [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11] |
| 9 | Malicious practices (malware) | «software or mobile application specifically designed to harm a computer» {g-spam} | Malicious practices | [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11] |
| 10 | Hacked content | «any content placed on a site without permission» {g-spam} | Hacked content | [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11] |
| 11 | User-generated spam | «spammy content added to a site by users» {g-spam} | User-generated spam | [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11] |
| 12 | Site reputation policy | «published on a host site mainly because of that host's already-established ranking signals» {g-spam} | Site reputation policy | [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11] |
| 13 | Expired domain abuse | «repurposed primarily to manipulate search rankings by hosting content that provides little to no value to users» {g-spam} | Expired domain abuse | [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11] |
| 14 | Thin affiliation | «copied directly from the original merchant without any original content» {g-spam} | Thin affiliation | [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11] |
| 15 | Structured data issue | «irrelevant or misleading content»; «Reviews must not be written or provided by the business or content provider unless they are customer, independent, and unpaid editorial reviews» {g-manual-actions} | Structured data issue | [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11] |
| 16 | Back button hijacking | «interferes with user browser navigation by manipulating the browser history» {g-spam} | Malicious practices | [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11] |

## 6. Enforcement
- Detection by «automated systems and, as needed, human review»; sites «may rank lower in results or not appear in results at all» {g-spam} [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]
- Algorithmic: «in most cases we automatically discover it and remove it»; manual: set by «a human reviewer», per URL pattern or whole site, notified «in the Manual actions report and in the Search Console message center»; News/Discover content policies too {g-manual-actions} [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11]
- Back button hijacking: «manual spam actions or automated demotions», «enforcement on June 15, 2026» {g-blog-2026-04-bbh} [documented: https://developers.google.com/search/blog/2026/04/back-button-hijacking, 2026-10-11]
- Site reputation policy in the EEA (from 2026-08-30): a manual action is still issued and site owners «will continue to be notified within Search Console»; for users inside the EEA «the impact of the manual action won't apply» and the affected section «may be separated in our systems»; outside the EEA the action applies to the affected portion; reconsideration continues, and eligible sites may go to mediation {g-blog-2026-08-srp} [documented: https://developers.google.com/search/blog/2026/08/update-site-reputation-policy, 2026-10-11].
- Sub-section measurement «doesn't mean that these sub-sections have somehow been demoted» {g-blog-2024-11-sra} [documented: https://developers.google.com/search/blog/2024/11/site-reputation-abuse, 2026-10-11]

## 7. Detection and recovery
- Report shows «patterns of affected pages»; fix all of them, keep them crawlable, then Request Review; reviews «can take several days or weeks», link cases longer {g-manual-actions} [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11]
- A request asks Google to «review your site after you fix problems identified in a manual action or security issues notification» {g-reconsideration} [documented: https://support.google.com/webmasters/answer/35843, 2026-10-11]
- Site-reputation requests from European Economic Area sites: «we commit to answer requests within a short timeframe» {g-spam} [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]
- Disavow: for actual or likely unnatural-link actions; «most sites will not need to use this tool»; per property plus child properties; no Domain properties or subpaths; 100,000 lines / 2MB; «a few weeks» {g-disavow} [documented: https://support.google.com/webmasters/answer/2648487, 2026-10-11]

## 8. AI-use controls
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 17 | robots.txt | «other fields such as crawl-delay aren't supported» {g-robots-spec} | Syntax | [documented: https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec, 2026-10-11] |
| 18 | nosnippet, data-nosnippet, max-snippet (Google-Extended: skill `seo-engine-policies` › google-ai) | nosnippet «will also prevent the content from being used as a direct input for AI Overviews and AI Mode» {gai-robots-meta} | nosnippet | [documented: https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag, 2026-10-11] |

## 9. Delta from Google
This is the baseline page.

## 10. Practitioner layer
- None in the corpora.

## 11. Unverified
- QRG body: g-qrg.pdf now holds body text; INDEX says TOC only [unverified: extraction not logged].
## Sources
- https://developers.google.com/search/docs/essentials/spam-policies — fetched 2026-10-11, saved as sources/google/g-spam.raw
- https://support.google.com/webmasters/answer/9044175 — fetched 2026-10-11, saved as sources/google/g-manual-actions.raw
- https://support.google.com/webmasters/answer/35843 — fetched 2026-10-11, saved as sources/google/g-reconsideration.raw
- https://developers.google.com/search/blog/2026/08/update-site-reputation-policy — fetched 2026-10-11, saved as sources/google/g-blog-2026-08-srp.raw
- https://developers.google.com/search/blog/2024/11/site-reputation-abuse — fetched 2026-10-11, saved as sources/google/g-blog-2024-11-sra.raw
- https://developers.google.com/search/blog/2026/04/back-button-hijacking — fetched 2026-10-11, saved as sources/google/g-blog-2026-04-bbh.raw
- https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf — fetched 2026-10-11, saved as sources/google/g-qrg.raw
- https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers — fetched 2026-10-11, saved as sources/google/g-crawlers-overview.raw
- https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec — fetched 2026-10-11, saved as sources/google/g-robots-spec.raw
- https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag — fetched 2026-10-11, saved as sources/google-ai/gai-robots-meta.raw
- https://support.google.com/webmasters/answer/2648487 — fetched 2026-10-11, saved as sources/google/g-disavow.raw