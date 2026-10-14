# Spam playbook — know every play (part 1 of 9: how to use, index, link schemes)

Defensive catalogue (2026-10-13) from saved engine documents (fetched 2026-10-11 and -12), a scout of 81 SEO repos and the practitioner corpus. Read a play to recognise, explain and defend against it; never to run it.

## Contents
- How to use this catalogue
- Index of plays
- Class 5: link schemes (L1–L8)
- Sources

## How to use this catalogue

**Refusal rule.** A request to run, build, tune, price or hide a play gets a one-sentence refusal, then the play explained in entry order and the safe alternative. A request to understand or recognise one (rival, victim, audit, training) gets the full explanation, no refusal. Mechanism only as far as needed to recognise it: no recipes, no thresholds to stay under, no evasion steps, whatever the framing `[unvalidated house heuristic]`. This is skill `seo-engine-policies` § Rules, rule 5.

**Entry order.** 1 What and why (claimed upside) · 2 How (mechanism only) · 3 Policy per engine · 4 Detection and penalty · 5 Tells · 6 Defence · 7 Evidence.

**No saved spam policy:** Brave, DuckDuckGo, Yahoo, Ecosia, Qwant, OpenAI, Perplexity, Anthropic, Apple, Meta, Common Crawl, Amazon — classes 1–16 "not addressed", searched 2026-10-11 ([engine-matrix](engine-matrix.md)); line 3 calls them "others". Copilot follows the Bing guidelines ([microsoft-copilot](microsoft-copilot.md)).

**Labels.** Engine text: dated documented label. Corpus reports: `[practitioner: anonymised sources · label · threads / score · newest]` plus PLAYBOOK-<layer>:line — what people did or saw, not what an engine does. Scout repo plays: owner/repo@file:line (scout Bn.md:line) `[vendor]`. Our tells and defences: `[unvalidated house heuristic]` unless documented. The link group opens with one row per engine; other groups cite each engine inside line 3.

## Index of plays

| ID | Play | Where |
|---|---|---|
| L1–L8 | PBNs · paid/disguised links · exchanges · guest-post farms · anchor quotas · automated links · widget/contract links · link quotas | this file |
| C1–C8 | cloaking (incl. AI crawlers) · doorways, city pages · hidden text · stuffing · scaled content · scraping · sneaky redirects · thin affiliate | [spam-playbook-2](spam-playbook-2.md) |
| H1–H9 | parasite SEO · expired domains · hacks, injection · UGC spam · astroturfing · fake reviews, star markup · CTR bots · misleading functionality · back-button hijacking | [spam-playbook-3](spam-playbook-3.md) |
| A1–A7, P1–P3, X1–X3 | prompt injection · LLM-only text · mention seeding · GEO rewriting · one article many platforms · invented stats · fake freshness · Business Profile spam · rank-and-rent · impersonation · Indexing API · IndexNow/sitemaps · paid indexing | [spam-playbook-4](spam-playbook-4.md) |
| N1–N5, T1–T7, V1–V5 | toxic-link attacks · fake takedowns · clones · sabotage · listing attacks · CAPTCHA bypass · anti-bot evasion · SERP scraping · bot impersonation · unlicensed data · injecting tools · email probing · guarantees · toxic-link upsell · uncontrolled uplift · invented updates · fake activity | [spam-playbook-5](spam-playbook-5.md) |
| C9, K1–K6 | machine translation · cloaked images · paywalls · conditional cloaking · link cloaking · hiding vectors · canonical hijacks | [spam-playbook-6](spam-playbook-6.md) |
| D1–D5, R1–R4 | domain farms · cybersquatting · free hosts · crawl traps · open redirects · rich-result markup · fake ClaimReview · entity spam · News bait | [spam-playbook-7](spam-playbook-7.md) |
| R5–R8, L9–L11, P4–P5 | bait titles · suggest poisoning · fake expertise · SERP flooding · profile stacking · tiered links · rented links · incentivised reviews · fake addresses | [spam-playbook-8](spam-playbook-8.md) |
| A8–A11, N6–N7, T8 | off-page injection · robots split · AI forum seeding · training data · removal abuse · bot floods · unsafe tools; unsourced plays | [spam-playbook-9](spam-playbook-9.md) |

## Class 5: link schemes (L1–L8)

| Engine | Own term | Quote | Label |
|---|---|---|---|
| Google | Link spam | «creating links to or from a site primarily for the purpose of manipulating search rankings» | [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11] |
| Bing, Copilot | Link Schemes and Artificial Promotion | «link buying, link spamming, private networks, and artificial social promotion schemes that simulate popularity» | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |
| Yandex | deceptive external links | «include external links not as recommendations to visit another site, but with the goal of deceiving the search engine» | [documented: https://yandex.com/support/webmaster/en/yandex-indexing/webmaster-advice, 2026-10-11] |
| Seznam | Linkfarmy; SEO PR; SEO katalogy; Nepřirozené odkazy | «placené články s cílem manipulovat s ranky» ("paid articles meant to manipulate rank") | [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11] |
| Naver | 백링크 악용 (backlink abuse) | «외부 링크를 인위적으로 대량 생성하여» ("mass-creating external links") | [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11] |
| Baidu | — | not addressed as a policy; its notices only say «超链算法升级，外链拒绝功能下线» ("link algorithm upgraded, disavow function withdrawn") | [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11] |

**Google detection and penalty (all L entries).** «Buying links or participating in link schemes in order to manipulate ranking in Google Search results is a violation of our spam policies»; «This can result in some or all of your site getting a manual action». Recovery: remove or qualify links, disavow the rest, then request review; «Blindly adding all backlinks to the disavow file is not considered a good-faith effort» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11]. Bing: «Manipulating inbound links to inflate authority violates guidelines» [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]. A link penalty also opens skill `seo-authority` › authority-links-and-pr (disavow scope).

### L1. Private blog networks (PBNs)
1. **What and why.** Sites one seller controls, posting links to client money pages; sold as controllable "authority" links.
2. **How.** Often rebuilt expired domains (H2) on separate hosts, with thin posts written to carry the link.
3. **Policy.** Bing names «private networks» (class table). Google: «Creating low-value content primarily for the purposes of manipulating linking and ranking signals» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Seznam: «Linkfarma je skupina stránek» ("a link farm is a group of pages" built to pass rank) [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11]. Yandex, Naver: class table. Baidu, others: not addressed.
4. **Detection and penalty.** Google and Bing: class rules above. Practitioners report PBN buyers hit, secondhand, in a low-score dissent `[practitioner: anonymised sources · consensus · 2 thr / 61 · newest 2024-05]` (PLAYBOOK-technical:4668).
5. **Tells.** Linking sites share host or owner, have little traffic, random topics and outbound links to many unrelated commercial sites; a price per post `[unvalidated house heuristic]`.
6. **Defence.** Competitor: report it (Google spam report, Bing feedback); never copy. Bought in the past: remove; disavow the rest on N1's terms. Vendor: decline in writing; Mowei's line is "no bought followed links, no PBNs" `[unvalidated house heuristic]`.
7. **Evidence.** The general layer's largest link cluster is headed by PBN ranking links `[practitioner: anonymised sources · consensus · 492 thr / 20,950 · newest 2026-09]` (PLAYBOOK-general:5566). The professional layer's largest cluster headline (private-network posts) is contradicted by its own variants `[practitioner: anonymised sources · consensus · 39 thr / 868 · newest 2025-07]` (PLAYBOOK-professional:3446).

### L2. Paid links, incl. disguised as editorial; niche edits; sponsored columns
1. **What and why.** Paying for a followed link in an article, a "link insert" into an old post, or a branded column, so it passes ranking credit while looking organic.
2. **How.** Prices per link, often by a third-party "DR/DA" score; anchors varied so the links "look editorial"; payment may be cash, product, a donation or a service.
3. **Policy.** Google: «Exchanging money for links, or posts that contain links»; «Exchanging goods or services for links»; «Advertorials or native advertising where payment is received for articles that include links that pass ranking credit»; allowed only «qualified with a rel="nofollow" or rel="sponsored" attribute value» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Bing: «link buying». Seznam: «SEO PR» paid articles (class table). Yandex: «Don't add links to the site just because someone asked you to» [documented: https://yandex.com/support/webmaster/en/yandex-indexing/webmaster-advice, 2026-10-11]. Naver: class table. Baidu, others: not addressed.
4. **Detection and penalty.** Google manual actions «Unnatural links to your site» and «Unnatural links from your site» (seller side) [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11]. Practitioners: 300 bought links on DA 40+ sites left rankings flat `[practitioner: anonymised sources · single thread · 1 thr / 17 · newest 2019-02]` (PLAYBOOK-technical:4812).
5. **Tells.** A rate card by DA/DR; a "link insertion fee"; a newsroom column bylined by the brand's staff; tracked `utm_medium=cpc` "donation" links; followed links on "parceria" or "patrocinado" pages; a tool promising links that "look editorial" `[unvalidated house heuristic]`.
6. **Defence.** Vendor: refuse followed paid links; a sponsorship bought for traffic carries `rel="sponsored"`. Competitor: log URLs and dates (it may be legitimate sponsorship); report clear cases only. Manual action: remove or qualify each link, document it, request review.
7. **Evidence.** Illyism/seo-skills seo/linkdr/SKILL.md:32-36,147 sells DR-tiered links "so links look editorial" (scout B6.md:123) `[vendor]`. DA is no basis for buying links `[practitioner: anonymised sources · consensus · 204 thr / 6,789 · newest 2026-09]` (PLAYBOOK-general:5578). PT: partner-bylined SAPO columns (payment unverified) and followed CRESCER "donation" links, verified as paid affiliate links :48).

### L3. Link exchanges, triangular exchanges, link wheels
1. **What and why.** Sites swap links; networks rotate links through three or more sites so no pair links both ways.
2. **How.** Manual "link swap" offers, partner pages, or an automated platform that assigns links across members.
3. **Policy.** Google: «Excessive link exchanges ("Link to me and I'll link to you") or partner pages exclusively for the sake of cross-linking» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Seznam: «Umisťování předplacených odkazových lišt a jiných výměnných odkazových systémů» ("placing paid link bars and other link-exchange systems") [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11]. Bing, Yandex, Naver: class table. Baidu, others: not addressed.
4. **Detection and penalty.** Google class rule. A Major Spam manual-action recovery included nofollowing link-exchange links `[practitioner: anonymised sources · single thread · 1 thr / 50 · newest 2026-08]` (PLAYBOOK-technical:790).
5. **Tells.** "Link swap" emails; a "partners" page of off-topic links; a platform promising to hide the reciprocal pattern (the evasion is the admission) `[unvalidated house heuristic]`.
6. **Defence.** Decline; link to real partners only where it helps users. Audit outbound links before any review request.
7. **Evidence.** HeiGeAi/HeiGe-GEO-SEO source/knowledge/03-publishing-channels.md:182 recommends 友链交换 (scout B5.md:80) `[vendor]`. Triangular exchanges `[practitioner: anonymised sources · contested · 1 thr / 123 · newest 2026-03]` (PLAYBOOK-agentic:902). Link wheels: searched, not found in the corpus; tiered links: L10 in [spam-playbook-8](spam-playbook-8.md).

### L4. Guest-post farms and paid contributor programmes
1. **What and why.** Articles placed mainly to carry keyword links; sites that sell "guest post" slots.
2. **How.** Multi-topic, low-traffic sites take paid posts; programmes sell contributor seats.
3. **Policy.** Google: «links with optimized anchor text in articles, guest posts, or press releases distributed on other sites» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]; manual action «Thin content» lists «low-quality guest blog posts» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11]. Seznam «SEO PR»; Bing, Yandex, Naver: class table. Baidu, others: not addressed.
4. **Detection and penalty.** Google class rule. Secondhand: three guest-posting domains deindexed in March `[practitioner: anonymised sources · consensus · 2 thr / 61 · newest 2024-05]` (PLAYBOOK-technical:4668).
5. **Tells.** "Write for us" sites covering everything; the same author bio with commercial anchors on many sites; a link quota per post; the brand's anchor in the body instead of a byline `[unvalidated house heuristic]`.
6. **Defence.** Guest articles for audience only, with `rel` values on any commercial link; refuse "DR 30+ guest post" packages.
7. **Evidence.** siddiqss/semantic-seo-suite framework/off-page-authority.md:31 (scout B2.md:54); noique/cross-border-ecommerce-skills brand-strategy/dsite-seo-playbook.md:645-656 (scout B2.md:103) `[vendor]`. Guest-post farms `[practitioner: anonymised sources · consensus · 2 thr / 18 · newest 2025-04]` (PLAYBOOK-professional:3458).

### L5. Exact-match anchor quotas and "natural profile" engineering
1. **What and why.** A target mix of anchor texts (branded, exact match, generic) and of follow/nofollow for links you place, so a built profile "looks natural".
2. **How.** A plan sets shares per anchor type and enforces them in a prospect sheet or script. Shares are not repeated here.
3. **Policy.** Google: «links with optimized anchor text in articles, guest posts, or press releases» (L4) and «Forum comments with optimized links in the post or signature» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Others: class table; no engine names quotas.
4. **Detection and penalty.** Google class rule; no engine documents an anchor threshold.
5. **Tells.** Anchor percentages in a proposal; "you control anchors only where you place the link" admits placement `[unvalidated house heuristic]`.
6. **Defence.** Treat any anchor-mix target as a link-scheme plan; earned links carry the linker's anchor.
7. **Evidence.** siddiqss framework/off-page-authority.md:37-49 (scout B2.md:54); noique dsite-seo-playbook.md:686-704 (scout B2.md:102) `[vendor]`. Blending nofollow and dofollow to look natural `[practitioner: anonymised sources · consensus · 3 thr / 55 · newest 2022-07]` (PLAYBOOK-general:5654).

### L6. Automated links: tools, comments, forums, profiles, directories, bookmarks
1. **What and why.** Volume links from software or cheap labour: comments, forum signatures, profiles, web 2.0 blogs, directories, bookmarks.
2. **How.** Posting tools work from site lists; agencies count submissions as monthly output.
3. **Policy.** Google: «Using automated programs or services to create links to your site»; «Low-quality directory or bookmark site links» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Seznam: «SEO katalogy» built to «generovat zpětné odkazy» ("generate backlinks") [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11]. Naver: «링크만으로 구성된 페이지를 생성해» ("creating pages made only of links") [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11]. Bing, Yandex: class table. Baidu, others: not addressed.
4. **Detection and penalty.** Google class rule. Practitioners: links anyone can create are long abused and discounted `[practitioner: anonymised sources · consensus · 4 thr / 467 · newest 2024-01]` (PLAYBOOK-general:5590). Open-redirect "backlinks": D5 in [spam-playbook-7](spam-playbook-7.md).
5. **Tells.** "Submit to 500+ directories"; monthly reports counting submissions, bookmarks or profiles; sudden batches of forum-profile links `[unvalidated house heuristic]`.
6. **Defence.** Refuse; judge a vendor by links on sites people read. Past mass links, actual or likely manual action (N1): remove, disavow the rest, request review if actioned.
7. **Evidence.** Report padding with directory and bookmark submissions `[practitioner: anonymised sources · contested · 1 thr / 7 · newest 2026-07]` (PLAYBOOK-technical:4370); a 500+ directory tool posted by its maker `[practitioner: anonymised sources · single thread · 1 thr / 17 · newest 2026-03]` (PLAYBOOK-agentic:2220).

### L7. Widget, badge, footer and contract-required links
1. **What and why.** A free widget, calculator or award badge embedded on other sites, with a followed (often keyword) link back; links demanded in terms or contracts.
2. **How.** The embed code carries the link; an "award" is granted on condition of displaying the badge.
3. **Policy.** Google: «Keyword-rich, hidden, or low-quality links embedded in widgets that are distributed across various sites»; «Widely distributed links in the footers or templates of various sites»; «Requiring a link as part of a Terms of Service, contract, or similar arrangement» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Others: class table or not addressed.
4. **Detection and penalty.** Google class rule.
5. **Tells.** Embed code with a followed keyword anchor; "winners must display the badge"; data given only if the recipient links `[unvalidated house heuristic]`.
6. **Defence.** Mowei embeds: credit link outside the iframe, `rel="nofollow"`; a link is never a condition of data or awards `[unvalidated house heuristic]`.
7. **Evidence.** A model review of Mowei's link plan tied the embed link to the widget clause and called the badge case reasoning, not policy text :43) `[hypothesis]`.

### L8. Link-velocity quotas and "backlinks on autopilot" outreach
1. **What and why.** A fixed count of new links per day or month; tools that mass-mail link requests.
2. **How.** A schedule drives placements; alias inboxes send generated pitches.
3. **Policy.** Google: «Using automated programs or services to create links to your site» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Others: class table.
4. **Detection and penalty.** Class rule; a sudden batch may look spammy by itself `[practitioner: anonymised sources · single thread · 1 thr / 17 · newest 2026-03]` (PLAYBOOK-technical:4746).
5. **Tells.** "N backlinks a day for 30 days"; monthly link budgets; outreach from many alias domains `[unvalidated house heuristic]`.
6. **Defence.** Refuse quotas; measure outreach by placements earned on relevant sites, not by count.
7. **Evidence.** Illyism seo/blitz-seo/SKILL.md:55,58 (scout B6.md:125); noique dsite-seo-playbook.md:645-656 (scout B2.md:103) `[vendor]`. Mass alias outreach `[practitioner: anonymised sources · contested · 1 thr / 24 · newest 2019-10]` (PLAYBOOK-professional:3614).

## Sources

- Engine texts: phase-2 sources g-spam, g-manual-actions, b-guidelines, y-advice, sz-forbidden, nv-content-abusing, bd-wiki7 (fetched 2026-10-11; quotes checked against the saved text).
- Scout: scout REPORT §8 and assess notes B1–B8 (2026-10-13). Corpus: PLAYBOOK-general, -professional, -technical, -agentic; an internal backlink plan.
