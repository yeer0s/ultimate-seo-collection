# Yandex — policies, enforcement, controls
> last_verified: 2026-10-11 · market relevance: not stated in docs; marginal for PT · doc languages: en (RU original) · coverage: PARTIAL · scope_exception: none

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
- Yandex Search: «deliver the most suitable and useful response» {y-advice} [documented: https://yandex.com/support/webmaster/en/yandex-indexing/webmaster-advice, 2026-10-11]
- PARTIAL: 13 docs read raw; §7.4 row "AI-use opt-out" is ❓ (none found) and INDEX row y-robots-list (duplicate URL) is NOT READ.

## 2. Primary documents
| Document | URL | Language | Fetched | Governs |
|---|---|---|---|---|
| High- vs low-quality websites | https://yandex.com/support/webmaster/en/yandex-indexing/webmaster-advice | en | 2026-10-11 | violation list |
| Use of SEO texts | https://yandex.com/support/webmaster/en/threat/seo-text | en | 2026-10-11 | stuffing, hidden text |
| Unexpected redirects | https://yandex.com/support/webmaster/en/threat/unexpected-redirection | en | 2026-10-11 | redirects |
| Mimicry | https://yandex.com/support/webmaster/en/threat/mimicry | en | 2026-10-11 | impersonation |
| Cloaking | https://yandex.com/support/webmaster/en/threat/cloaking | en | 2026-10-11 | cloaking |
| Unwanted software | https://yandex.com/support/webmaster/en/threat/undesirable | en | 2026-10-11 | malware |
| Social engineering | https://yandex.com/support/webmaster/en/threat/social-engineering | en | 2026-10-11 | phishing |
| Fraudulent activity | https://yandex.com/support/webmaster/en/threat/unfair-actions | en | 2026-10-11 | fraud |
| Useless content | https://yandex.com/support/webmaster/en/threat/useless-content | en | 2026-10-11 | copied / AI text |
| Imitation of user actions | https://yandex.com/support/webmaster/en/threat/user-actions-imitation | en | 2026-10-11 | behaviour bots |
| Using robots.txt | https://yandex.com/support/webmaster/en/controlling-robot/robots-txt | en | 2026-10-11 | robots.txt |
| Clean-param | https://yandex.com/support/webmaster/en/robot-workings/clean-param | en | 2026-10-11 | URL parameters |
| Check a Yandex robot | https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots | en | 2026-10-11 | rDNS |

## 3. Crawlers and verification
- rDNS then forward DNS: «All Yandex robots have names ending in yandex.ru, yandex.net or yandex.com.» {y-check-robots} [documented: https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots, 2026-10-11]
- Non-indexing robots «may ignore the file's restrictive directives» for `*` {y-check-robots}; name them (e.g. YandexCalendar). [documented: https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots, 2026-10-11]

## 4. Webmaster tools and submission
- Yandex Webmaster; violation pages sit under «Site security and violations» {y-threat-seo-text} [documented: https://yandex.com/support/webmaster/en/threat/seo-text, 2026-10-11]

## 5. What is prohibited
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 1 | Cloaking | «content shown to users is different from the content shown to indexing bots» {y-threat-cloaking} | Cloaking | [documented: https://yandex.com/support/webmaster/en/threat/cloaking, 2026-10-11] |
| 2 | doorway pages | «Unexpected redirects often involve the use of doorway pages» {y-threat-unexpected-redirection} | Unexpected redirects | [documented: https://yandex.com/support/webmaster/en/threat/unexpected-redirection, 2026-10-11] |
| 3 | Hidden texts (SEO texts) | «Texts with keywords or phrases that are invisible to users, but visible to indexing bots.» {y-threat-seo-text} | SEO texts | [documented: https://yandex.com/support/webmaster/en/threat/seo-text, 2026-10-11] |
| 4 | Keyword stuffing (SEO texts) | «Long lists of search queries or meaningless, incoherent texts loaded with keywords.» {y-threat-seo-text} | SEO texts | [documented: https://yandex.com/support/webmaster/en/threat/seo-text, 2026-10-11] |
| 5 | deceptive external links | «external links» … «with the goal of deceiving the search engine» {y-advice} | Markers | [documented: https://yandex.com/support/webmaster/en/yandex-indexing/webmaster-advice, 2026-10-11] |
| 6 | Useless content (AI-generated) | «created using neural networks, machine translation, or template methods» {y-threat-useless-content} | Useless content | [documented: https://yandex.com/support/webmaster/en/threat/useless-content, 2026-10-11] |
| 7 | Copied or rewritten content | «The content is fully or partially copied from other resources.» {y-threat-useless-content} | Useless content | [documented: https://yandex.com/support/webmaster/en/threat/useless-content, 2026-10-11] |
| 8 | Unexpected redirection | «created to automatically redirect users to another resource without their consent» {y-advice} | Markers | [documented: https://yandex.com/support/webmaster/en/yandex-indexing/webmaster-advice, 2026-10-11] |
| 9 | Unwanted software; Social engineering | «programs and applications that can cause serious harm to the user or their device» {y-threat-undesirable} | Unwanted software | [documented: https://yandex.com/support/webmaster/en/threat/undesirable, 2026-10-11] |
| 10 | targeted by attackers | «it may have been targeted by attackers» {y-threat-social-engineering} | Social engineering | [documented: https://yandex.com/support/webmaster/en/threat/social-engineering, 2026-10-11] |
| 11 | — | not addressed | — | — |
| 12 | — | not addressed | — | — |
| 13 | — | not addressed | — | — |
| 14 | affiliate programs, no added value | «through affiliate programs, but don't provide any additional value for the user» {y-advice} | Markers | [documented: https://yandex.com/support/webmaster/en/yandex-indexing/webmaster-advice, 2026-10-11] |
| 15 | fake positive reviews | «Post fake positive reviews or inaccurate information.» {y-threat-social-engineering} | Social engineering | [documented: https://yandex.com/support/webmaster/en/threat/social-engineering, 2026-10-11] |
| 16 | Imitation of user actions | «special software or services that automatically imitate user traffic from search engines» {y-threat-user-actions-imitation} | Imitation | [documented: https://yandex.com/support/webmaster/en/threat/user-actions-imitation, 2026-10-11] |

### Outside the 16 classes
- Mimicry: «copies the look or features of a well-known or official site» {y-threat-mimicry} [documented: https://yandex.com/support/webmaster/en/threat/mimicry, 2026-10-11]
- Fraudulent activity: «takes payment but doesn't deliver the goods or services» {y-threat-unfair-actions} [documented: https://yandex.com/support/webmaster/en/threat/unfair-actions, 2026-10-11]
- Site groups, pop-unders: «Created to occupy multiple positions in search results» {y-advice} [documented: https://yandex.com/support/webmaster/en/yandex-indexing/webmaster-advice, 2026-10-11]

## 6. Enforcement
- Algorithmic: «search algorithms may apply certain restrictions» … «the ranking of the entire site or some of its sections» {y-advice} [documented: https://yandex.com/support/webmaster/en/yandex-indexing/webmaster-advice, 2026-10-11]
- Fraud: «analyze a whole range of factors, including user reports» {y-threat-unfair-actions} [documented: https://yandex.com/support/webmaster/en/threat/unfair-actions, 2026-10-11]
- Malware: «it will flag a threat of distributing unwanted software» {y-threat-undesirable} [documented: https://yandex.com/support/webmaster/en/threat/undesirable, 2026-10-11]

## 7. Detection and recovery
- «The restriction will be lifted when the violation is fixed and the algorithms verify that it's not happening again.» {y-threat-user-actions-imitation} [documented: https://yandex.com/support/webmaster/en/threat/user-actions-imitation, 2026-10-11]
- Contact support: «Specify the violation you want to ask about» {y-threat-cloaking} [documented: https://yandex.com/support/webmaster/en/threat/cloaking, 2026-10-11]

## 8. AI-use controls
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 17 | robots.txt | «Yandex supports the Robots Exclusion Protocol with advanced features.» {y-robots} | Using robots.txt | [documented: https://yandex.com/support/webmaster/en/controlling-robot/robots-txt, 2026-10-11] |
| 18 | — | not addressed | — | — |
- «Pages restricted in robots.txt can participate in Yandex search.» Use noindex instead. {y-robots} [documented: https://yandex.com/support/webmaster/en/controlling-robot/robots-txt, 2026-10-11]
- Clean-param (strip e.g. UTM parameters): «We recommend using Clean-param» over Disallow {y-clean-param} [documented: https://yandex.com/support/webmaster/en/robot-workings/clean-param, 2026-10-11]
- Crawl-delay handling: unverified [unverified: directive page listed in the help navigation but its body was not saved]; see §11.

## 9. Delta from Google
- Mimicry and business fraud («according to Yandex data and user reports») are restriction grounds. {y-advice} [documented: https://yandex.com/support/webmaster/en/yandex-indexing/webmaster-advice, 2026-10-11]
- Clean-param directive (§8); no AI-use control found (class 18; search logged in sources/INDEX.md).

## 10. Practitioner layer
- None in the corpora (engine-corpus-items.md: yandex 0).

## 11. Unverified
- AGS, Minusinsk, Baden-Baden filter names: blogs only [unverified: no current Yandex page names them]
- Crawl-delay handling: page listed, not saved [unverified: body not fetched]
- Robot user-agent list and IndexNow page [unverified: not captured]

## Sources
- https://yandex.com/support/webmaster/en/yandex-indexing/webmaster-advice — High- vs low-quality websites, fetched 2026-10-11, saved as phase-2 sources/yandex/y-advice.raw
- https://yandex.com/support/webmaster/en/threat/seo-text — Use of SEO texts, fetched 2026-10-11, saved as phase-2 sources/yandex/y-threat-seo-text.raw
- https://yandex.com/support/webmaster/en/threat/unexpected-redirection — Unexpected redirects, fetched 2026-10-11, saved as phase-2 sources/yandex/y-threat-unexpected-redirection.raw
- https://yandex.com/support/webmaster/en/threat/mimicry — Mimicry, fetched 2026-10-11, saved as phase-2 sources/yandex/y-threat-mimicry.raw
- https://yandex.com/support/webmaster/en/threat/cloaking — Cloaking, fetched 2026-10-11, saved as phase-2 sources/yandex/y-threat-cloaking.raw
- https://yandex.com/support/webmaster/en/threat/undesirable — Unwanted software, fetched 2026-10-11, saved as phase-2 sources/yandex/y-threat-undesirable.raw
- https://yandex.com/support/webmaster/en/threat/social-engineering — Social engineering, fetched 2026-10-11, saved as phase-2 sources/yandex/y-threat-social-engineering.raw
- https://yandex.com/support/webmaster/en/threat/unfair-actions — Fraudulent activity, fetched 2026-10-11, saved as phase-2 sources/yandex/y-threat-unfair-actions.raw
- https://yandex.com/support/webmaster/en/threat/useless-content — Useless content, fetched 2026-10-11, saved as phase-2 sources/yandex/y-threat-useless-content.raw
- https://yandex.com/support/webmaster/en/threat/user-actions-imitation — Imitation of user actions, fetched 2026-10-11, saved as phase-2 sources/yandex/y-threat-user-actions-imitation.raw
- https://yandex.com/support/webmaster/en/controlling-robot/robots-txt — Using robots.txt, fetched 2026-10-11, saved as phase-2 sources/yandex/y-robots.raw
- https://yandex.com/support/webmaster/en/robot-workings/clean-param — Clean-param, fetched 2026-10-11, saved as phase-2 sources/yandex/y-clean-param.raw
- https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots — Check a Yandex robot, fetched 2026-10-11, saved as phase-2 sources/yandex/y-check-robots.raw
