# Other AI crawler owners (Apple, Common Crawl, Meta, ByteDance, Amazon) — policies, enforcement, controls
> last_verified: 2026-10-11 · market relevance: global AI features and datasets · doc languages: en · coverage: Apple: COMPLETE, Common Crawl: COMPLETE, Meta: COMPLETE, ByteDance: ABSENT-SEARCHED, Amazon: COMPLETE · scope_exception: none

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

### Apple
- Applebot powers Spotlight, Siri and Safari; data may train Apple foundation models. [documented: https://support.apple.com/en-us/119829, 2026-10-14]

### Common Crawl
- A non-profit «open repository of web crawl data» {cc-ccbot}. [documented: https://commoncrawl.org/ccbot, 2026-10-14]

### Meta
- Link previews (Facebook, Instagram, Messenger), Meta AI search, ads, AI model training. [documented: https://developers.facebook.com/docs/sharing/webmasters/web-crawlers, 2026-10-14]

### ByteDance
- Bytespider: no official document found (search logged); see §11.

### Amazon
- Amazon search experiences such as Alexa; Amazonbot «may be used to train Amazon AI models» {amzn-amazonbot}. [documented: https://developer.amazon.com/amazonbot, 2026-10-14]

## 2. Primary documents

| Document | URL | Language | Fetched | Governs |
|---|---|---|---|---|
| About Applebot (2026-09-04) | https://support.apple.com/en-us/119829 | en | 2026-10-11 | Applebot, Applebot-Extended |
| CCBot | https://commoncrawl.org/ccbot | en | 2026-10-11 | CCBot |
| Meta Web Crawlers | https://developers.facebook.com/docs/sharing/webmasters/web-crawlers | en | 2026-10-11 | Meta UAs, robots.txt |
| About Amazonbot | https://developer.amazon.com/amazonbot | en | 2026-10-11 | Amazonbot, Amzn-SearchBot, Amzn-User |

## 3. Crawlers and verification

### Apple
- UA contains `Applebot`; verify by reverse DNS `*.applebot.apple.com` or the IP CIDRs JSON. `iTMS` (Podcasts) «does not follow robots.txt» {ap-applebot}. `isAccessibleForFree: false` pages are not used as AI context. [documented: https://support.apple.com/en-us/119829, 2026-10-14]

### Common Crawl
- UA `CCBot/2.0`; dedicated IPs with reverse DNS `*.crawl.commoncrawl.org` (not IPv6); IP JSON published. [documented: https://commoncrawl.org/ccbot, 2026-10-14]

### Meta
- `facebookexternalhit` (shared links), `meta-webindexer` (Meta AI search), `meta-externalads`, `meta-externalagent` (AI training), `meta-externalfetcher` (user fetches). [documented: https://developers.facebook.com/docs/sharing/webmasters/web-crawlers, 2026-10-14]

### ByteDance
- None found; see §11.

### Amazon
- `Amazonbot`, `Amzn-SearchBot`, `Amzn-User`, each with a published IP list; settings independent. The last two «does not crawl content for generative AI model training»; Amzn-User is user-initiated and «may not follow all robots.txt directives» {amzn-amazonbot}. [documented: https://developer.amazon.com/amazonbot, 2026-10-14]

## 4. Webmaster tools and submission

- Meta: Sharing Debugger / Sharing API force a re-crawl [documented: https://developers.facebook.com/docs/sharing/webmasters/web-crawlers, 2026-10-14]. Apple, Common Crawl, Amazon: no console or URL submission in the saved pages. ByteDance: none found.

## 5. What is prohibited

### Apple
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

### Common Crawl
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

### Meta
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

### ByteDance
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

### Amazon
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

### Apple
- «Site rules for Applebot-Extended are not considered in ranking for Search.» {ap-applebot} [documented: https://support.apple.com/en-us/119829, 2026-10-11]
| — | Spam penalties | not addressed |

### Common Crawl
| — | Spam penalties | not addressed |

### Meta
- FacebookExternalHit «might bypass robots.txt when performing security or integrity checks» {meta-crawlers} [documented: https://developers.facebook.com/docs/sharing/webmasters/web-crawlers, 2026-10-11]

### ByteDance
| — | Enforcement | not addressed |

### Amazon
| — | Spam penalties | not addressed |

## 7. Detection and recovery

### Apple
- «Applebot’s crawl rate adjusts automatically when a site slows down or returns errors.» {ap-applebot} [documented: https://support.apple.com/en-us/119829, 2026-10-11]

### Common Crawl
- «we are aware of crawlers falsely identifying themselves as CCBot» {cc-ccbot}; reverse DNS lets webmasters «verify whether a logged request stems from the real CCBot» {cc-ccbot} [documented: https://commoncrawl.org/ccbot, 2026-10-11]

### Meta
- «crawlers may cache the contents of `robots.txt` for up to 24 hours» {meta-crawlers} [documented: https://developers.facebook.com/docs/sharing/webmasters/web-crawlers, 2026-10-11]

### ByteDance
| — | Detection and recovery | not addressed |

### Amazon
- Changes «may take ~24 hours for our systems to reflect» {amzn-amazonbot}; robots.txt may be «a cached copy from the last 30 days» {amzn-amazonbot} [documented: https://developer.amazon.com/amazonbot, 2026-10-11]

## 8. AI-use controls

### Apple
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 17 | Applebot; robots.txt | «If robots instructions don't mention Applebot but mention Googlebot, the Apple robot will follow Googlebot instructions.» {ap-applebot} | Customizing robot.txt rules | [documented: https://support.apple.com/en-us/119829, 2026-10-11] |
| 18 | Applebot-Extended; nosnippet | «opt-out from having their content used to train generative foundation models by disallowing Applebot-Extended» «opt out of their content being used in these broad world knowledge answers by applying the nosnippet meta tag» {ap-applebot} | Intro; Applebot-Extended | [documented: https://support.apple.com/en-us/119829, 2026-10-11] |

### Common Crawl
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 17 | CCBot; robots.txt | To block it, «include the following in your robots.txt:» (`User-agent: CCBot` / `Disallow: /`) {cc-ccbot} | CCBot | [documented: https://commoncrawl.org/ccbot, 2026-10-11] |
| 18 | — | not addressed | — | — |

### Meta
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 17 | robots.txt | «add a disallow for the relevant crawler to robots.txt» «The Meta-ExternalFetcher crawler may bypass robots.txt because it performs fetches that were requested by the user.» {meta-crawlers} | The robots.txt file | [documented: https://developers.facebook.com/docs/sharing/webmasters/web-crawlers, 2026-10-11] |
| 18 | Meta-ExternalAgent | It «crawls the web for use cases such as training foundation AI models» «robots.txt rather than non-standard formats like NoAI tags» {meta-crawlers} | Meta-ExternalAgent; intro | [documented: https://developers.facebook.com/docs/sharing/webmasters/web-crawlers, 2026-10-11] |

### ByteDance
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 17 | — | not addressed | — | — |
| 18 | — | not addressed | — | — |

### Amazon
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 17 | Robots Exclusion Protocol (not Amzn-User, see §3) | «Automated crawling from these listed user agents respects the Robots Exclusion Protocol» {amzn-amazonbot} | Our Approach to Robots.txt | [documented: https://developer.amazon.com/amazonbot, 2026-10-11] |
| 18 | Amazonbot; noarchive | «may be used to train Amazon AI models» «noarchive (do not use the page for model training)» {amzn-amazonbot} | Amazonbot; robots meta | [documented: https://developer.amazon.com/amazonbot, 2026-10-11] |

## 9. Delta from Google

- Apple: Googlebot rules govern an unnamed Applebot; no crawl-delay. [documented: https://support.apple.com/en-us/119829, 2026-10-11]
- Amazon: Amzn-SearchBot, if unnamed, follows rules for other search bots; `noarchive` = no model training; no crawl-delay. [documented: https://developer.amazon.com/amazonbot, 2026-10-11]

## 10. Practitioner layer

- None in the corpora.

## 11. Unverified

- ByteDance Bytespider: no official page; bytespider.bytedance.com had no DNS on 2026-10-11; UA, robots and AI use unknown [unverified: no primary document to read].
- Common Crawl Opt-out Registry and FAQ: linked, not read [unverified: not saved].

## Sources

- https://support.apple.com/en-us/119829 — About Applebot, fetched 2026-10-11, saved as sources/other-ai/ap-applebot.raw
- https://commoncrawl.org/ccbot — CCBot, fetched 2026-10-11, saved as sources/other-ai/cc-ccbot.raw
- https://developers.facebook.com/docs/sharing/webmasters/web-crawlers — Meta Web Crawlers, fetched 2026-10-11, saved as sources/other-ai/meta-crawlers.raw
- https://developer.amazon.com/amazonbot — About Amazonbot, fetched 2026-10-11, saved as sources/other-ai/amzn-amazonbot.raw
