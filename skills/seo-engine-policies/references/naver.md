# Naver — policies, enforcement, controls
> last_verified: 2026-10-11 · market relevance: South Korea (Korean-language search) · doc languages: ko · coverage: COMPLETE · scope_exception: none

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
- Naver web search, from its own crawler: «웹 수집 로봇이 자동으로 수집한 사이트 정보를 반영하여 노출하고 있습니다» {nv-faq-start-register} (“shows site data its crawler collected”). [documented: https://searchadvisor.naver.com/guide/faq-start-register, 2026-10-11]
- IndexNow pings are «다른 검색사들에게도 공유됩니다» {nv-indexnow-about} (“shared with other engines”). [documented: https://searchadvisor.naver.com/guide/indexnow-about, 2026-10-11]

## 2. Primary documents
| Document | URL | Language | Fetched | Governs |
|---|---|---|---|---|
| 웹 콘텐츠 스팸사례 | https://searchadvisor.naver.com/guide/content-abusing | ko | 2026-10-11 | spam, sanctions, reinstatement |
| 콘텐츠 작성시 권장 사항 | https://searchadvisor.naver.com/guide/content-basic | ko | 2026-10-11 | content, AI use |
| 검색엔진 최적화의 목적 | https://searchadvisor.naver.com/guide/seo-basic-intro | ko | 2026-10-11 | SEO basics |
| robots.txt 설정하기 | https://searchadvisor.naver.com/guide/seo-basic-robots | ko | 2026-10-11 | robots |
| 검색로봇 확인 방법 | https://searchadvisor.naver.com/guide/seo-basic-firewall | ko | 2026-10-11 | Yeti check |
| 수집요청 및 검색제외 | https://searchadvisor.naver.com/guide/request-crawl | ko | 2026-10-11 | recrawl, removal |
| RSS 및 사이트맵 제출 | https://searchadvisor.naver.com/guide/request-feed | ko | 2026-10-11 | feeds |
| 웹 검색 제외 | https://searchadvisor.naver.com/guide/faq-serpremove | ko | 2026-10-11 | removal policy |
| 사이트 등록 및 소유확인 | https://searchadvisor.naver.com/guide/faq-start-register | ko | 2026-10-11 | registration |
| IndexNow 소개 | https://searchadvisor.naver.com/guide/indexnow-about | ko | 2026-10-11 | IndexNow |
| 선호 URL 및 로봇 메타 태그 | https://searchadvisor.naver.com/guide/markup-structure | ko | 2026-10-11 | robots meta |

## 3. Crawlers and verification
- Crawler Yeti (UA token Yeti/1.1, plain or Chrome-style); also Ads-Naver and Blueno (previews). Verify: rDNS ends in .naver.com and resolves back to the IP, or match naverbot.json. [documented: https://searchadvisor.naver.com/guide/seo-basic-firewall, 2026-10-11]
- «IP 기반으로 차단하지 마세요» {nv-seo-basic-intro} (“do not block by IP”); use robots.txt. [documented: https://searchadvisor.naver.com/guide/seo-basic-intro, 2026-10-11]
- robots: ≤5 redirects then allow-all; 4xx allow-all; 5xx disallow-all; per host/protocol/port; ads and preview robots may not follow it. [documented: https://searchadvisor.naver.com/guide/seo-basic-robots, 2026-10-11]

## 4. Webmaster tools and submission
- «검색 등록 절차는 존재하지 않습니다» {nv-faq-start-register} (“no registration procedure”); registering + 소유확인 (ownership) gives crawl/index reports. [documented: https://searchadvisor.naver.com/guide/faq-start-register, 2026-10-11]
- Register per host; ownership by meta tag or HTML file; content shows «최대 1주일 이내» {nv-seo-basic-intro} (“within a week”) of Yeti's visit. [documented: https://searchadvisor.naver.com/guide/seo-basic-intro, 2026-10-11]
- Sitemap/RSS: verified domain only, ≤10 MB, sitemap ≤50,000 URLs, RSS full body; sitemap preferred. [documented: https://searchadvisor.naver.com/guide/request-feed, 2026-10-11]
- Crawl request: limited per site, «최소 1일에서 몇 주간» {nv-request-crawl} (“1 day to weeks”); no exposure guarantee. [documented: https://searchadvisor.naver.com/guide/request-crawl, 2026-10-11]
- IndexNow (API key): «색인을 보장하지는 않습니다» {nv-indexnow-about} (“no index guarantee”). [documented: https://searchadvisor.naver.com/guide/indexnow-about, 2026-10-11]

## 5. What is prohibited
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 1 | 클로킹 (cloaking) | «검색 사용자에게 보여주는 내용과 검색엔진에 전달하는 내용을 의도적으로 다르게 구성하는 경우» (“users and engine see different content”) {nv-content-abusing} | 스팸사례 | [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11] |
| 2 | 중복된 콘텐츠 (duplicate sites) | «동일한 콘텐츠로 구성된 여러 개의 사이트를 개설하는 경우» (“several sites with the same content”) {nv-seo-basic-intro} | §4 | [documented: https://searchadvisor.naver.com/guide/seo-basic-intro, 2026-10-11] |
| 3 | 숨겨진 텍스트 (hidden text) | «글자색을 배경색과 동일하게 설정하거나» (“text colour = background”) {nv-content-abusing} | 스팸사례 | [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11] |
| 4 | 키워드 반복·남용 (keyword abuse) | «제목이나 본문에 동일 키워드를 의도적으로 반복하거나» (“repeating a keyword on purpose”) {nv-content-abusing} | 스팸사례 | [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11] |
| 5 | 링크 스팸; 백링크 악용 (backlink abuse) | «외부 링크를 인위적으로 대량 생성하여» (“mass-creating external links”) {nv-content-abusing} | 스팸사례 | [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11] |
| 6 | 저품질 콘텐츠 대량 생성 (mass low-quality) | «동일·유사한 템플릿을 활용하여 콘텐츠를 무의미하게 대량으로 발행» (“template mass publishing”); AI: «특정 기술의 활용 여부만으로는 판단하지 않습니다» (“not judged by tool alone”) {nv-content-abusing} | 스팸사례 | [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11] |
| 7 | 스크래핑 (scraping) | «자동화 프로그램을 통해 복사 또는 기계적으로 변형해서 거의 그대로 게시» (“auto-copied nearly as is”) {nv-content-abusing} | 스팸사례 | [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11] |
| 8 | 부적절한 리다이렉트 (improper redirect) | «사용자를 강제로 이동시키는 경우» (“forcibly moving users”) {nv-content-abusing} | 스팸사례 | [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11] |
| 9 | 악성코드 배포; 피싱 (malware; phishing) | «사용자의 동의 없이 악성코드·바이러스 등 유해한 소프트웨어를 설치하거나 배포» (“malware without consent”) {nv-content-abusing} | 스팸사례 | [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11] |
| 10 | 해킹된 콘텐츠 (hacked) | «보안 취약점으로 인해 무단으로 설치된 콘텐츠» (“installed via a security hole”) {nv-content-abusing} | 스팸사례 | [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11] |
| 11 | 게시판 (boards, under 링크 스팸) | «관리가 소홀한 경로나 게시판이 주요 표적이 되며» (“neglected boards are targets”) {nv-content-abusing} | 스팸사례 | [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11] |
| 12 | — | not addressed | — | — |
| 13 | 만료 도메인 악용 (expired domains) | «공신력 있는 기관이나 단체가 사용하던 만료 도메인을 구매한 뒤» (“buying trusted bodies' expired domains”) {nv-content-abusing} | 스팸사례 | [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11] |
| 14 | 짜깁기 (patchwork) | «타 사이트의 글을 복사하거나 짜깁기하지 마세요.» (“don't copy or patch others' posts”) {nv-content-basic} | ③ | [documented: https://searchadvisor.naver.com/guide/content-basic, 2026-10-11] |
| 15 | — | not addressed | — | — |
| 16 | 매크로 및 조작 행위 (macros) | «자동화된 프로그램으로 트래픽을 인위적으로 부풀려» (“bot-inflated traffic”) {nv-content-abusing} | 스팸사례 | [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11] |

## 6. Enforcement
- Algorithmic: «스팸 탐지 알고리즘을 지속적으로 업데이트» {nv-content-abusing}; sanction «노출 제외 또는 순위 하락» {nv-content-abusing} (“exclusion or rank drop”), also for formerly clean sites. [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11]
- Link spam can hit «사이트 전체» {nv-content-abusing} (“the whole site”); backlink abuse hits sold and forwarded sites; equivalent acts count as spam. [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11]
- Spam sites' crawl requests are limited. [documented: https://searchadvisor.naver.com/guide/request-crawl, 2026-10-11]
- Naver deletes on its own only «정책위반의 경우에만» {nv-faq-serpremove} (“only for policy breaches”: law, copyright). [documented: https://searchadvisor.naver.com/guide/faq-serpremove, 2026-10-11]
- Site notification of a spam sanction: unverified [unverified: no saved Naver post says]; see §11.

## 7. Detection and recovery
- Hacked check via 웹마스터 도구 > 검증 > URL 검사: «실제 검색로봇에 수집되는 HTML을 점검해보세요» {nv-content-abusing}. [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11]
- Appeal or after fixing: «검색 노출 정상화를 요청할 수 있습니다» {nv-content-abusing} via the 검색 노출 제보하기 form,; reviewed «합리적인 기간 내에» {nv-content-abusing} (“within a reasonable period”). [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11]
- Recrawl: 수집요청, prioritised, not real-time. Removal: delete, confirm 404, then 웹 페이지 검색 제외; «실시간으로 반영되지 않습니다» {nv-request-crawl}. [documented: https://searchadvisor.naver.com/guide/request-crawl, 2026-10-11]
- Setting «robots.txt를 먼저 설정하거나» {nv-faq-serpremove} (“robots.txt first”) blocks the removal check. [documented: https://searchadvisor.naver.com/guide/faq-serpremove, 2026-10-11]

## 8. AI-use controls
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 17 | robots.txt; noindex, nofollow | «네이버 검색로봇은 robots.txt에 작성된 규칙을 준수하며» (“follows robots.txt”) {nv-seo-basic-robots} | robots.txt 설정하기 | [documented: https://searchadvisor.naver.com/guide/seo-basic-robots, 2026-10-11] |
| 18 | nosourceinfo | «AI로 자동 생성된 출처설명이 제공되지 않습니다» (“no AI-generated source description”) {nv-markup-structure} | 로봇 메타 태그 | [documented: https://searchadvisor.naver.com/guide/markup-structure, 2026-10-11] |

## 9. Delta from Google
Only Naver-documented points; Google's side is on the google page.
- Extra spam classes: «낚시성» {nv-content-abusing} (clickbait), «유사 공공사이트» {nv-content-abusing} (fake agencies), «사용자 혼동 및 피해 유발 콘텐츠» {nv-content-abusing} (false numbers, synthetic images), «서비스 안정성 저해» {nv-content-abusing}. [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11]
- «AI 생성 콘텐츠를 그대로 게시하지 않고» {nv-content-basic} (“don't post AI output as is”); over half the content on the core topic. [documented: https://searchadvisor.naver.com/guide/content-basic, 2026-10-11]

## 10. Practitioner layer
- None in the corpora (engine-corpus-items.md: naver 0).

## 11. Unverified
- Site notification of a spam sanction [unverified: no saved Naver post says].
- Naver rules from the 2013 The Egg summary [unverified: secondary, outdated; not used].
- Structured-data spam and parasite pages [unverified: not in the saved posts].

## Sources
- https://searchadvisor.naver.com/guide/content-abusing — 웹 콘텐츠 스팸사례, fetched 2026-10-11, saved as phase-2 sources/naver/nv-content-abusing.raw
- https://searchadvisor.naver.com/guide/content-basic — 콘텐츠 작성시 권장 사항, fetched 2026-10-11, saved as phase-2 sources/naver/nv-content-basic.raw
- https://searchadvisor.naver.com/guide/seo-basic-intro — 검색엔진 최적화의 목적, fetched 2026-10-11, saved as phase-2 sources/naver/nv-seo-basic-intro.raw
- https://searchadvisor.naver.com/guide/seo-basic-robots — robots.txt 설정하기, fetched 2026-10-11, saved as phase-2 sources/naver/nv-seo-basic-robots.raw
- https://searchadvisor.naver.com/guide/seo-basic-firewall — 검색로봇 확인 방법, fetched 2026-10-11, saved as phase-2 sources/naver/nv-seo-basic-firewall.raw
- https://searchadvisor.naver.com/guide/request-crawl — 수집요청 및 검색제외, fetched 2026-10-11, saved as phase-2 sources/naver/nv-request-crawl.raw
- https://searchadvisor.naver.com/guide/request-feed — RSS 및 사이트맵 제출, fetched 2026-10-11, saved as phase-2 sources/naver/nv-request-feed.raw
- https://searchadvisor.naver.com/guide/faq-serpremove — 웹 검색 제외, fetched 2026-10-11, saved as phase-2 sources/naver/nv-faq-serpremove.raw
- https://searchadvisor.naver.com/guide/faq-start-register — 사이트 등록 및 소유확인, fetched 2026-10-11, saved as phase-2 sources/naver/nv-faq-start-register.raw
- https://searchadvisor.naver.com/guide/indexnow-about — IndexNow 소개, fetched 2026-10-11, saved as phase-2 sources/naver/nv-indexnow-about.raw
- https://searchadvisor.naver.com/guide/markup-structure — 선호 URL 및 로봇 메타 태그, fetched 2026-10-11, saved as phase-2 sources/naver/nv-markup-structure.raw
