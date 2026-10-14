# Bing — policies, enforcement, controls
> last_verified: 2026-10-11 · market relevance: global; index also feeds Copilot · doc languages: en · coverage: COMPLETE · scope_exception: none

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
- One rulebook for Bing search, Copilot and grounding API results [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]. Copilot: `microsoft-copilot.md`; Bing-fed engines: `bing-syndication.md`.
- §5: Bing's duplicate-content item sits in class 2 (nearest; no doorway term). Prompt injection fits no class: extra Bing class in §6.

## 2. Primary documents
| Document | URL | Language | Fetched | Governs |
|---|---|---|---|---|
| Webmaster Guidelines | https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a | en | 2026-10-11 | rules, abuse |
| Crawlers | https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0 | en | 2026-10-11 | user agents |
| Verify Bingbot | https://www.bing.com/webmasters/help/how-to-verify-bingbot-3905dc26 | en | 2026-10-11 | rDNS |
| Robots meta tags | https://www.bing.com/webmasters/help/robots-meta-tags-and-attributes-that-bing-supports-5198d240 | en | 2026-10-11 | directives |
| Bing Chat controls 2023-09-22 | https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat | en | 2026-10-11 | AI use |
| Webmaster support | https://www.bing.com/webmasters/help/webmaster-support-24ab5ebf | en | 2026-10-11 | support |
| How Bing delivers results | https://support.microsoft.com/en-us/topic/how-bing-delivers-search-results-d18fc815-ac37-4723-bc67-9229ce3eb6a3 | en | 2026-10-11 | spam, appeals |

## 3. Crawlers and verification
- Bingbot (main), AdIdxBot (Ads), BingPreview, MicrosoftPreview, BingVideoPreview [documented: https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0, 2026-10-11].
- Verify: reverse DNS ends in `search.msn.com`, forward DNS returns the same IP; or Verify Bingbot tool [documented: https://www.bing.com/webmasters/help/how-to-verify-bingbot-3905dc26, 2026-10-11].

## 4. Webmaster tools and submission
- Bing Webmaster Tools: Site Explorer, URL Inspection, URL submission, Block URLs (90 days), Crawl Control, sitemaps, support request [documented: https://www.bing.com/webmasters/help/webmaster-support-24ab5ebf, 2026-10-11].
- Canonical-only sitemaps with lastmod; IndexNow on add/update/delete; 302 only under 2 days; 404 for deleted URLs [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11].

## 5. What is prohibited
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 1 | Cloaking | «Showing different content to search crawlers than to users» {b-guidelines} | Abuse list | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |
| 2 | Duplicate Content Across Multiple URLs | «Publishing the same or substantially similar content across multiple URLs» {b-guidelines} | Abuse list | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |
| 3 | — | not addressed | — | — |
| 4 | Keyword Stuffing and Artificially Engineered Language | «loading pages with irrelevant keywords can reduce visibility or lead to removal» {b-guidelines} | Abuse list | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |
| 5 | Link Schemes and Artificial Promotion | «link buying, link spamming, private networks, and artificial social promotion schemes» {b-guidelines} | Abuse list | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |
| 6 | Automatically Generated Content at Scale | «content generated without oversight, quality control, or editorial review» {b-guidelines} | Abuse list | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |
| 7 | Scraped or Republished Content Without Added Value | «lightly rewriting existing content without new insight or perspective is considered scraping» {b-guidelines} | Abuse list | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |
| 8 | — | not addressed | — | — |
| 9 | Malicious Behavior | «phishing, malware distribution, or other harmful activities risk demotion or removal» {b-guidelines} | Abuse list | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |
| 10 | — | not addressed | — | — |
| 11 | — | not addressed | — | — |
| 12 | — | not addressed | — | — |
| 13 | — | not addressed | — | — |
| 14 | Affiliate Programs Without Sufficient Value | «primarily redirect users to retailers without providing original value» {b-guidelines} | Abuse list | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |
| 15 | Misleading Structured Data | «Markup that is irrelevant, inaccurate, or misleading may be ignored» {b-guidelines} | Abuse list | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |
| 16 | — | not addressed | — | — |

## 6. Enforcement
- «reduced rankings, suppressed grounding visibility, loss of grounding eligibility, ignored structured data, or removal from the Bing index» {b-guidelines} [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]
- Extra Bing class, Prompt Injection and AI Manipulation: «content designed to manipulate or interfere with language models used by Bing or Copilot» {b-guidelines} [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]
- Spam: «Bing might remove such search results, or adjust Bing algorithms» {b-how-bing-delivers} [documented: https://support.microsoft.com/en-us/topic/how-bing-delivers-search-results-d18fc815-ac37-4723-bc67-9229ce3eb6a3, 2026-10-11]
- Site-owner notification of an action: unverified [unverified: no channel in the read docs]; see §11.

## 7. Detection and recovery
- «Site owners can contact support through Bing Webmaster Tools if action was taken in error» {b-guidelines} [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]
- Route: «contact us through our Support channel» {b-support} ("Raise support request"); check URL Inspection first [documented: https://www.bing.com/webmasters/help/webmaster-support-24ab5ebf, 2026-10-11]
- After a fix: «you can appeal using the Bing webmaster tools» {b-how-bing-delivers} [documented: https://support.microsoft.com/en-us/topic/how-bing-delivers-search-results-d18fc815-ac37-4723-bc67-9229ce3eb6a3, 2026-10-11]
- Appeal review timeline: unverified [unverified: none in the read docs]; see §11.

## 8. AI-use controls
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 17 | robots.txt; NOINDEX | «robots.txt controls crawl access, not indexing.» {b-guidelines} | Guidelines §10 | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |
| 18 | NOARCHIVE; NOCACHE | «NOARCHIVE prevents content from being used in Copilot responses and grounding results.» «NOCACHE limits Copilot to using only the URL, title, and snippet» {b-guidelines} | Guidelines §10 | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |

- noarchive: «Do not use the content for training Microsoft's generative AI foundation models.» Both tags: «we will treat it as NOCACHE.» {b-robots-meta} [documented: https://www.bing.com/webmasters/help/robots-meta-tags-and-attributes-that-bing-supports-5198d240, 2026-10-11]
- «content with the NOCACHE tag or NOARCHIVE tag will still appear in our search results.» {b-blog-2023-09-chat} [documented: https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat, 2026-10-11]

## 9. Delta from Google
- No doorway, hidden-text, sneaky-redirect, hacked, UGC, site-reputation or expired-domain item; adds duplicate content and prompt injection (compare google.md §5) [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11].
- Recovery is a support request in Bing Webmaster Tools; no manual-actions report named (compare google.md §7) [documented: https://www.bing.com/webmasters/help/webmaster-support-24ab5ebf, 2026-10-11].
- NOCACHE/NOARCHIVE govern Copilot and training (compare google.md §8) [documented: https://www.bing.com/webmasters/help/robots-meta-tags-and-attributes-that-bing-supports-5198d240, 2026-10-11].

## 10. Practitioner layer
- For retrieval-time answers, rank in the index the model actually searches — Bing named [practitioner: practitioner-technical-1.md:47 · consensus · 2 thr / 236 · newest 2026-05].

## 11. Unverified
- Site-owner notification of an action [unverified: no notification report for webspam actions in the read docs].
- Appeal review timeline [unverified: no timeline for support requests or appeals in the read docs].

## Sources
- https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a — Webmaster Guidelines, fetched 2026-10-11, saved as phase-2 sources/bing/b-guidelines.raw
- https://www.bing.com/webmasters/help/which-crawlers-does-bing-use-8c184ec0 — Crawlers, fetched 2026-10-11, saved as phase-2 sources/bing/b-crawlers.raw
- https://www.bing.com/webmasters/help/how-to-verify-bingbot-3905dc26 — Verify Bingbot, fetched 2026-10-11, saved as phase-2 sources/bing/b-verify-bingbot.raw
- https://www.bing.com/webmasters/help/robots-meta-tags-and-attributes-that-bing-supports-5198d240 — Robots meta tags, fetched 2026-10-11, saved as phase-2 sources/bing/b-robots-meta.raw
- https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat — Bing Chat controls, fetched 2026-10-11, saved as phase-2 sources/bing/b-blog-2023-09-chat.raw
- https://www.bing.com/webmasters/help/webmaster-support-24ab5ebf — Webmaster support, fetched 2026-10-11, saved as phase-2 sources/bing/b-support.raw
- https://support.microsoft.com/en-us/topic/how-bing-delivers-search-results-d18fc815-ac37-4723-bc67-9229ce3eb6a3 — How Bing delivers search results, fetched 2026-10-11, saved as phase-2 sources/bing/b-how-bing-delivers.raw
