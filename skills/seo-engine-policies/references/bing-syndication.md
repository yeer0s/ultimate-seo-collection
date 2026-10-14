# Bing-fed engines (DuckDuckGo, Ecosia, Yahoo, Qwant) — policies, enforcement, controls
> last_verified: 2026-10-11 · market relevance: privacy-minded searchers in PT/EU; Ecosia EUSP in FR · doc languages: en, fr · coverage: DuckDuckGo: ABSENT-SEARCHED, Ecosia: ABSENT-SEARCHED, Yahoo: ABSENT-SEARCHED, Qwant: PARTIAL · scope_exception: none

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

None of the four publishes its own spam policy in the pages read; for Bing's rules see the `bing` page.

### DuckDuckGo
- «We also maintain our own crawler (DuckDuckBot)»; links and images «which we largely source from Bing» {ddg-sources} [documented: https://duckduckgo.com/duckduckgo-help-pages/results/sources, 2026-10-11]

### Ecosia
- Results «come from our partners Microsoft Bing, Google and EUSP»; «EUSP is currently only available in France.» {eco-providers} [documented: https://support.ecosia.org/article/579-search-results-providers, 2026-10-11]

### Yahoo
- «All algorithmic search results for Yahoo Search are provided by Microsoft Bing» {yahoo-ranked} [documented: https://en-maktoob.help.yahoo.com/kb/SLN35619.html, 2026-10-11]

### Qwant
- QwantBot builds «l'index qui alimente notre moteur de recherche» (“the index that powers our search engine”) {qwant-bot} [documented: https://help.qwant.com/bot/, 2026-10-11]

## 2. Primary documents

| Document | URL | Language | Fetched | Governs |
|---|---|---|---|---|
| DDG result sources | https://duckduckgo.com/duckduckgo-help-pages/results/sources | en | 2026-10-11 | sources |
| DuckDuckBot | https://duckduckgo.com/duckduckgo-help-pages/results/duckduckbot | en | 2026-10-11 | crawler |
| DuckAssistBot | https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot | en | 2026-10-11 | AI crawler |
| Ecosia providers | https://support.ecosia.org/article/579-search-results-providers | en | 2026-10-11 | sources |
| Ecosia EUSP launch | https://blog.ecosia.org/launching-our-european-search-index/ | en | 2026-10-11 | EUSP |
| QwantBot | https://help.qwant.com/bot/ | fr | 2026-10-11 | crawler |
| Yahoo ranking (mirror) | https://en-maktoob.help.yahoo.com/kb/SLN35619.html | en | 2026-10-11 | sources |

## 3. Crawlers and verification

### DuckDuckGo
- `DuckDuckBot/1.1`, IPs in `duckduckbot.json`. [documented: https://duckduckgo.com/duckduckgo-help-pages/results/duckduckbot, 2026-10-11]
- `DuckAssistBot/1.2`, IPs in `duckassistbot.json`. [documented: https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot, 2026-10-11]

### Ecosia
- No crawler documented; EUSP (joint venture with Qwant) runs the Staan index. [documented: https://blog.ecosia.org/launching-our-european-search-index/, 2026-10-11]

### Yahoo
- No crawler documented.

### Qwant
- UA contains `Qwantbot`; verify by reverse DNS ending `qwant.com` + forward DNS, or `qwantbot.json`; documents `Crawl-delay`, `noindex`. [documented: https://help.qwant.com/bot/, 2026-10-11]

## 4. Webmaster tools and submission

- DDG, Ecosia, Yahoo: no tool documented; Yahoo points to the Bing Webmaster Guidelines.
- Qwant: a current `sitemap.xml` and a fast server raise crawl frequency. [documented: https://help.qwant.com/bot/, 2026-10-11]
- IndexNow: no saved page mentions it for these four; do not claim it.

## 5. What is prohibited

### DuckDuckGo
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

### Ecosia
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

### Yahoo
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

### Qwant
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

### DuckDuckGo
- No own policy found in the documents searched; links «largely source from Bing» {ddg-sources} [documented: https://duckduckgo.com/duckduckgo-help-pages/results/sources, 2026-10-11]

### Ecosia
- No own policy found in the documents searched; «Ecosia does not manually reorder or override the organic results» {eco-providers} [documented: https://support.ecosia.org/article/579-search-results-providers, 2026-10-11]

### Yahoo
- No own policy found in the documents searched; results «provided by Microsoft Bing» {yahoo-ranked} [documented: https://en-maktoob.help.yahoo.com/kb/SLN35619.html, 2026-10-11]

### Qwant
- No own policy in the page read; results come from QwantBot's own index. [documented: https://help.qwant.com/bot/, 2026-10-11]

## 7. Detection and recovery

### DuckDuckGo
- No recovery process found in the documents searched; organic links come from Bing. [documented: https://duckduckgo.com/duckduckgo-help-pages/results/sources, 2026-10-11]
- DDG result removal: unverified [unverified: help article not saved]; see §11.

### Ecosia
- Removal requests go to a «separate guide on the Ecosia Help Center» {eco-providers} [documented: https://support.ecosia.org/article/579-search-results-providers, 2026-10-11]
- Ecosia removal guide: unverified [unverified: guide not saved]; see §11.

### Yahoo
- Delisting: «contact Microsoft Bing to find out the reason for a delisting» {yahoo-ranked} [documented: https://en-maktoob.help.yahoo.com/kb/SLN35619.html, 2026-10-11]

### Qwant
- Crawl problems: «Signalez-nous tout problème par e-mail» (“report any problem by e-mail”) {qwant-bot} [documented: https://help.qwant.com/bot/, 2026-10-11]
- Qwant missing-site article: unverified [unverified: article not saved]; see §11.

## 8. AI-use controls

### DuckDuckGo
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 17 | DuckDuckBot | «It respects WWW::RobotRules» {ddg-duckduckbot} | About DuckDuckBot | [documented: https://duckduckgo.com/duckduckgo-help-pages/results/duckduckbot, 2026-10-11] |
| 18 | DuckAssistBot | «This data is not used in any way to train AI models.»; robots.txt disallow, «the change will take effect after 72 hours» {ddg-duckassistbot} | About DuckAssistBot | [documented: https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot, 2026-10-11] |

### Ecosia
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 17 | — | not addressed | — | — |
| 18 | — | not addressed | — | — |

### Yahoo
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 17 | — | not addressed | — | — |
| 18 | — | not addressed | — | — |

### Qwant
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 17 | robots.txt | «QwantBot respecte le standard d'exclusion des robots» (“respects the robots exclusion standard”) {qwant-bot} | Contrôler QwantBot | [documented: https://help.qwant.com/bot/, 2026-10-11] |
| 18 | — | not addressed | — | — |

- Qwant AI training article: unverified [unverified: article not saved]; see §11.

## 9. Delta from Google

- Yahoo's algorithmic results all come from Bing. [documented: https://en-maktoob.help.yahoo.com/kb/SLN35619.html, 2026-10-11]
- Ecosia's provider (Bing, Google, EUSP) can change per search. [documented: https://support.ecosia.org/article/579-search-results-providers, 2026-10-11]
- «Opting out of DuckAssistBot does not impact organic search rankings» {ddg-duckassistbot} [documented: https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot, 2026-10-11]

## 10. Practitioner layer

- None in the corpora.

## 11. Unverified

- DDG result removal: help article listed, not fetched [unverified: help article not saved]
- Ecosia removal guide: not fetched [unverified: guide not saved]
- Qwant missing-site article: listed, not fetched [unverified: article not saved]
- Qwant AI training article: listed, not fetched; AI-use control unknown [unverified: article not saved]
- EUSP in Germany: blog headline 2026-07-30 vs providers page "France only" [unverified: post not fetched]
- Yahoo canonical URL: help.yahoo.com SLN35619 serves generic help [unverified: canonical not located]

## Sources

- https://duckduckgo.com/duckduckgo-help-pages/results/sources — DDG result sources, fetched 2026-10-11, saved as phase-2 sources/bing-syndication/ddg-sources.raw
- https://duckduckgo.com/duckduckgo-help-pages/results/duckduckbot — DuckDuckBot, fetched 2026-10-11, saved as phase-2 sources/bing-syndication/ddg-duckduckbot.raw
- https://duckduckgo.com/duckduckgo-help-pages/results/duckassistbot — DuckAssistBot, fetched 2026-10-11, saved as phase-2 sources/bing-syndication/ddg-duckassistbot.raw
- https://support.ecosia.org/article/579-search-results-providers — Search Result Providers, fetched 2026-10-11, saved as phase-2 sources/bing-syndication/eco-providers.raw
- https://blog.ecosia.org/launching-our-european-search-index/ — European search index goes live, fetched 2026-10-11, saved as phase-2 sources/bing-syndication/eco-eusp.raw
- https://help.qwant.com/bot/ — Le bot Qwant (QwantBot), fetched 2026-10-11, saved as phase-2 sources/bing-syndication/qwant-bot.raw
- https://en-maktoob.help.yahoo.com/kb/SLN35619.html — How your content is ranked, fetched 2026-10-11, saved as phase-2 sources/bing-syndication/yahoo-ranked.raw
