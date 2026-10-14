# Baidu — policies, enforcement, controls
> last_verified: 2026-10-11 · market relevance: mainland China (Chinese-language search, Baidu APP) · doc languages: zh · coverage: PARTIAL · scope_exception: none

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
- Baidu web search, mobile search and the Baidu APP; the quality guide applies to «所有与百度搜索合作的内容生产者» {bd-quality-guide} (“all content producers working with Baidu Search”), incl. mini-programs, 百家号, H5 and PC sites. [documented: https://ziyuan.baidu.com/college/articleinfo?id=2947, 2026-10-11]
- Blocking Baiduspider also removes pages from «所有百度提供搜索引擎服务的搜索引擎» {bd-spider} (“all search engines to which Baidu provides search service”). [documented: https://ziyuan.baidu.com/college/articleinfo?id=1192, 2026-10-11]
- Newest official algorithm post found: «促进下载生态良性发展，清风算法4.0即将上线» {bd-qingfeng4} (“清风 algorithm 4.0 coming soon”), dated «发布日期：2021-09-02» {bd-qingfeng4}. [documented: https://ziyuan.baidu.com/wiki/3294, 2026-10-11]
- In the saved announcements list (wiki/7, newest first, no dates shown) no named-algorithm post appears above 清风4.0; the entries above it are tool and governance notices, e.g. «【功能上线】AI流量分析功能上线公告» {bd-wiki7} (“AI traffic analysis feature launched”). No 2025–26 algorithm announcement was found in the saved list. [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11]

## 2. Primary documents
| Document | URL | Language | Fetched | Governs |
|---|---|---|---|---|
| 搜索资源平台公告 (algorithm and platform announcements list) | https://ziyuan.baidu.com/wiki/7 | zh | 2026-10-11 | named algorithms and notices (titles only in the saved copy) |
| 百度搜索优质内容指南 (2020-04-01) | https://ziyuan.baidu.com/college/articleinfo?id=2947 | zh | 2026-10-11 | quality content standard |
| 百度spider介绍 (2019-04-24) | https://ziyuan.baidu.com/college/articleinfo?id=1192 | zh | 2026-10-11 | user-agents, rDNS check, robots |
| 百度搜索引擎网页质量白皮书 (2019-09-18) | https://ziyuan.baidu.com/college/articleinfo?id=1337 | zh | 2026-10-11 | page quality (saved copy = page 1 of 4) |
| 百度搜索页面质量标准 (2022-07-27) | https://ziyuan.baidu.com/college/articleinfo?id=3436 | zh | 2026-10-11 | page quality (saved copy = page 1 of 5) |
| 清风算法4.0 (2021-09-02) | https://ziyuan.baidu.com/wiki/3294 | zh | 2026-10-11 | low-quality download sites |

## 3. Crawlers and verification
- User-agents per product: web and mobile search «Baiduspider», plus Baiduspider-image, -video, -news, -favo, -cpro, -ads. [documented: https://ziyuan.baidu.com/college/articleinfo?id=1192, 2026-10-11] {bd-spider}
- Verification by reverse DNS (host / nslookup / dig): «Baiduspider的hostname以 *.baidu.com 或 *.baidu.jp 的格式命名» {bd-spider} (“Baiduspider hostnames take the form *.baidu.com or *.baidu.jp”); anything else is an impostor. [documented: https://ziyuan.baidu.com/college/articleinfo?id=1192, 2026-10-11]
- Exceptions: «Baiduspider-cpro抓取的网页并不会建入索引» {bd-spider} (“pages fetched by Baiduspider-cpro are not indexed”); -cpro and -ads do not obey robots. [documented: https://ziyuan.baidu.com/college/articleinfo?id=1192, 2026-10-11]

## 4. Webmaster tools and submission
- 搜索资源平台 (Baidu Search Resource Platform) menus in the saved pages: «快速抓取» {bd-wiki7} (fast crawl), «普通收录» {bd-wiki7} (normal inclusion), «死链提交» {bd-wiki7} (dead-link submission), Robots, 抓取诊断 (crawl diagnosis), 索引量 (index volume). [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11]
- Sitemaps: «sitemap全网开放及建议启用Etag的公告» {bd-wiki7} (“sitemap opened to all sites; ETag recommended”); quota notice «关于回收网站提交配额的通知» {bd-wiki7} (“reclaiming site submission quotas”). [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11]
- Abnormal crawling is reported through «反馈中心» {bd-spider} (feedback centre), with access logs. [documented: https://ziyuan.baidu.com/college/articleinfo?id=1192, 2026-10-11]

## 5. What is prohibited
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 1 | — | not addressed | — | — |
| 2 | 站群 (site clusters) | «飓风算法3.0即将上线，控制跨领域采集及站群问题» (“飓风 3.0: controls cross-domain scraping and site clusters”) {bd-wiki7} | wiki/7 list | [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11] |
| 3 | — | not addressed | — | — |
| 4 | 网页标题作弊 (web-page title cheating; nearest class) | «百度推出清风算法，严惩网页标题作弊» (“清风 algorithm punishes title cheating”) {bd-wiki7} | wiki/7 list | [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11] |
| 5 | — | not addressed | — | — |
| 6 | — | not addressed | — | — |
| 7 | 恶劣采集 (malicious scraping) | «百度推出飓风算法，严厉打击恶劣采集» (“飓风 algorithm strikes malicious scraping”) {bd-wiki7} | wiki/7 list | [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11] |
| 8 | 网络劫持 (hijacking) | «百度烽火算法升级，持续打击网络劫持问题» (“烽火 upgrade keeps striking hijacking”) {bd-wiki7} | wiki/7 list | [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11] |
| 9 | 捆绑下载 (bundled downloads) | «捆绑下载了多个软件且用户无法取消下载» (“several programs bundled, user cannot cancel”) {bd-qingfeng4} | 清风4.0 问题类型二 | [documented: https://ziyuan.baidu.com/wiki/3294, 2026-10-11] |
| 10 | 被黑 (hacked) | «新闻源站点清理被黑内容后请迅速提交死链» (“after cleaning hacked content, submit dead links quickly”) {bd-wiki7} | wiki/7 list | [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11] |
| 11 | — | not addressed | — | — |
| 12 | 售卖目录 (selling directories) | «百度推出蓝天算法，严厉打击新闻类站点售卖目录» (“蓝天 strikes news sites selling directories”) {bd-wiki7} | wiki/7 list | [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11] |
| 13 | — | not addressed | — | — |
| 14 | 低质页面 (low-quality pages) | «低质页面（页面死链、空白、内容空短）» (“low-quality pages: dead, blank, empty or short content”) {bd-quality-guide} | 优质内容指南 §2 说明 | [documented: https://ziyuan.baidu.com/college/articleinfo?id=2947, 2026-10-11] |
| 15 | — | not addressed | — | — |
| 16 | 刷点击作弊 (click fraud); 回退按钮失效 (back button broken) | «百度搜索推出惊雷算法 严厉打击刷点击作弊行为» «烽火算法持续升级，控制回退按钮失效问题» {bd-wiki7} | wiki/7 list | [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11] |

## 6. Enforcement
- Algorithmic and announced by name; effect stated as limiting display: «将限制其在百度搜索结果中的展现» {bd-qingfeng4} (“will limit its display in Baidu results”). [documented: https://ziyuan.baidu.com/wiki/3294, 2026-10-11]
- Quality standard is applied in inclusion, ranking and display; bad pages are suppressed: «对一些影响用户体验、欺骗搜索引擎的恶劣低质网页进行打压» {bd-quality-1337} (“pages that hurt users or deceive the engine are suppressed”). [documented: https://ziyuan.baidu.com/college/articleinfo?id=1337, 2026-10-11]
- Porn, illegal and cheating pages are «百度搜索算法严厉打击的低质作弊问题» {bd-quality-guide} (“low-quality cheating that Baidu algorithms strike hard”). [documented: https://ziyuan.baidu.com/college/articleinfo?id=2947, 2026-10-11]
- Other named algorithms in the list: «冰桶算法4.5更新：发力打击Landing Page恶劣广告行为» {bd-wiki7} (landing-page ads); «杜绝翻页诱导行为，百度搜索信风算法即将上线» {bd-wiki7} (pagination lures). [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11]
- «“天网算法”出台，百度严打盗取用户隐私» {bd-wiki7} (privacy theft); «针对B2B领域低质内容，细雨算法即将升级» {bd-wiki7} (B2B low quality); «百度搜索上线极光算法 倡导重视落地页时间规范» {bd-wiki7} (page dates). [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11]
- Platform sanctions: «关于回收违规站点平台权限的通知» {bd-wiki7} (“revoking platform permissions of violating sites”). [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11]

## 7. Detection and recovery
- Notifications in the platform: «消息提醒重拳出击：被黑提醒&作弊提醒» {bd-wiki7} (“message alerts: hacked alerts and cheating alerts”). [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11]
- Rectification feedback: «整改反馈功能上线：首批通知石榴算法命中站点» {bd-wiki7} (“rectification feedback launched; first sites hit by 石榴 notified”). [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11]
- Self-check before the algorithm runs: «对站点内容进行全面的自查整改，避免站点因违规内容被算法覆盖» {bd-qingfeng4} (“self-inspect and fix, so the algorithm does not cover the site”). [documented: https://ziyuan.baidu.com/wiki/3294, 2026-10-11]
- Removal after robots: index data «可能需要数月时间才会清除» {bd-spider} (“may take months to clear”); urgent cases via 反馈中心. [documented: https://ziyuan.baidu.com/college/articleinfo?id=1192, 2026-10-11]
- Recovery timeline after a penalty: unverified [unverified: no saved Baidu text gives one]; see §11.

## 8. AI-use controls
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 17 | robots协议 (robots protocol) | «Baiduspider遵守互联网robots协议» (“Baiduspider obeys the robots protocol”) {bd-spider} | 百度spider介绍 §6 | [documented: https://ziyuan.baidu.com/college/articleinfo?id=1192, 2026-10-11] |
| 18 | — | not addressed | — | — |

## 9. Delta from Google
Only Baidu-documented points; Google's side is on the google page, not restated here.
- Penalties are public, named algorithms (飓风, 清风, 细雨, 惊雷, 烽火, 蓝天, 冰桶, 天网, 信风, 极光, 劲风, 闪电, 石榴) announced in the platform list. [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11]
- Link disavow removed: «超链算法升级，外链拒绝功能下线» {bd-wiki7} (“hyperlink algorithm upgraded, link-disavow feature taken offline”). [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11]
- Quality judged on four dimensions: «“出身”、“颜值”、“内涵”和“口碑”» {bd-quality-guide} (“origin, looks, substance, reputation”), incl. creator accounts focused on one field. [documented: https://ziyuan.baidu.com/college/articleinfo?id=2947, 2026-10-11]
- Two Baidu crawlers ignore robots (-cpro, -ads); rDNS hosts may end in .baidu.jp. [documented: https://ziyuan.baidu.com/college/articleinfo?id=1192, 2026-10-11]
- Baidu's own figure: «仅有7%可以达到高质量标准» {bd-quality-1337} (“only 7% reach the high-quality standard”). [documented: https://ziyuan.baidu.com/college/articleinfo?id=1337, 2026-10-11]

## 10. Practitioner layer
- None in the corpora (engine-corpus-items.md: baidu 0).

## 11. Unverified
- Recovery timeline after a penalty [unverified: no saved Baidu text gives one; individual algorithm posts other than 清风4.0 were not saved].
- Scope of each named algorithm beyond its announcement title [unverified: only titles saved in wiki/7].
- Content of pages 2+ of the page-quality white paper (id=1337) and standard (id=3436) [unverified: saved copies hold page 1 only].
- Baidu stance on AI-generated content and any AI-training opt-out [unverified: not found in the saved texts; «AI流量分析» {bd-wiki7} is a traffic report, not a control].

## Sources
- https://ziyuan.baidu.com/wiki/7 — 搜索资源平台公告 (announcements list), fetched 2026-10-11, saved as phase-2 sources/baidu/bd-wiki7.raw
- https://ziyuan.baidu.com/college/articleinfo?id=2947 — 百度搜索优质内容指南, fetched 2026-10-11, saved as phase-2 sources/baidu/bd-quality-guide.raw
- https://ziyuan.baidu.com/college/articleinfo?id=1192 — 百度spider介绍, fetched 2026-10-11, saved as phase-2 sources/baidu/bd-spider.raw
- https://ziyuan.baidu.com/college/articleinfo?id=1337 — 百度搜索引擎网页质量白皮书, fetched 2026-10-11, saved as phase-2 sources/baidu/bd-quality-1337.raw
- https://ziyuan.baidu.com/college/articleinfo?id=3436 — 百度搜索页面质量标准, fetched 2026-10-11, saved as phase-2 sources/baidu/bd-quality-3436.raw
- https://ziyuan.baidu.com/wiki/3294 — 清风算法4.0, fetched 2026-10-11, saved as phase-2 sources/baidu/bd-qingfeng4.raw
