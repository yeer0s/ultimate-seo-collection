# Spam playbook — know every play (part 3 of 9: hosts, hacks, reviews, clicks)

Refusal rule, entry order, labels and "others": [spam-playbook](spam-playbook.md), first section.

## Contents
- Classes 9–13, 15–16: abuse of hosts, users and signals (H1–H9)
- Unverified
- Sources

## Classes 9–13, 15–16: abuse of hosts, users and signals (H1–H9)

### H1. Site reputation abuse (parasite SEO)
1. **What and why.** Third-party commercial pages (coupons, casinos, loans, "best X") placed on a strong host to borrow its ranking; also mass posts on Medium, LinkedIn or Reddit.
2. **How.** A partner rents a subfolder or subdomain, or buys a "placement"; the host does little editing.
3. **Policy.** Google: «published on a host site mainly because of that host's already-established ranking signals»; example: «An educational site hosting a page about sponsored reviews of payday loans» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Enforcement differs by searcher region: [google](google.md) §6. Baidu: «严厉打击新闻类站点售卖目录» ("strikes news sites selling directories") [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11]. Bing, Yandex, Seznam, Naver, others: not addressed.
4. **Detection and penalty.** Google human review weighs, among others, «Does the content appear on multiple other sites in identical or near-identical form» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Practitioners report manual actions on broad publishers hosting unrelated thin pages `[practitioner: anonymised sources · single thread · 1 thr / 27 · newest 2025-04]` (PLAYBOOK-professional:3690).
5. **Tells.** A news or school domain with a coupon, casino or "advisor" section in a different design, no author, text found on other sites; "placements on DR 80 news sites" offers `[unvalidated house heuristic]`.
6. **Defence.** Own partner sections: editorially integrated or not hosted (rule 8 routes: google §6, skill `seo-authority` › authority-trust-and-distribution, skill `seo-content` › programmatic-seo-2). Vendor placements: refuse (also L2). Competitor: report.
7. **Evidence.** 500 AI variants on Medium, Substack, LinkedIn, Reddit, Quora `[practitioner: anonymised sources · contested · 1 thr / 2 · newest 2026-03]` (PLAYBOOK-agentic:1942); keyword-stuffed Reddit threads aimed at Google `[practitioner: anonymised sources · consensus · 3 thr / 103 · newest 2024-11]` (PLAYBOOK-general:4734).

### H2. Expired-domain abuse and domain forwarding
1. **What and why.** Buy a domain with history (school, charity, agency) and reuse its trust for unrelated content, or 301 it to a money site.
2. **How.** Backorders and auctions; old pages rebuilt from archives; new commercial pages added.
3. **Policy.** Google: «purchased and repurposed primarily to manipulate search rankings by hosting content that provides little to no value to users»; «Casino-related content on a former elementary school site» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Naver: «공신력 있는 기관이나 단체가 사용하던 만료 도메인을 구매한 뒤» ("buying expired domains of trusted bodies"); «리다이렉트·도메인 포워딩을 설정해 다른 사이트로 검색 자질을 전달하려는 경우» ("forwarding to pass search signals") [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11]. Bing, Yandex, Seznam, Baidu, others: not addressed.
4. **Detection and penalty.** Google class rule. Naver: «판매된 사이트와 포워딩 대상 사이트 모두 불이익을 받을 수 있습니다» ("both the sold site and the target can be penalised") [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11].
5. **Tells.** Archive history shows another owner and topic; sudden topic jump; unrelated aged domains 301-ing to one site `[unvalidated house heuristic]`.
6. **Defence.** A real acquisition keeps topic and maps pages one to one; never buy a domain for its links.
7. **Evidence.** 301-redirecting used domains, listed with PBNs as black hat `[practitioner: anonymised sources · consensus · 4 thr / 76 · newest 2019-07]` (PLAYBOOK-general:2204); backorder plus archive rebuild `[practitioner: anonymised sources · single thread · 1 thr / 25 · newest 2016-11]` (PLAYBOOK-professional:3546).

### H3. Hacked content and injection
1. **What and why.** Attackers add pages, links or redirects to a trusted site to rank spam (pharma, casino, "Japanese keyword hack").
2. **How.** A vulnerable plugin or panel; injected pages, hidden links, conditional redirects; often cloaked so only crawlers see it.
3. **Policy.** Google: hackers «add new pages to your site that contain spammy or malicious content»; «The kind of redirect sometimes depends on the referrer, user agent, or device» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Bing: «Maintaining secure infrastructure and controlling publishing access is essential» [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]. Yandex has no hacked-content rule; its social-engineering page only warns «If your site is suspected of using social engineering tactics, it may have been targeted by attackers» [documented: https://yandex.com/support/webmaster/en/threat/social-engineering, 2026-10-11]. Naver: «특정 에이전트에서만 스팸 콘텐츠가 노출되도록 설계된 경우» ("spam shown only to certain agents") [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11]. Baidu: «新闻源站点清理被黑内容后请迅速提交死链» [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11]. Seznam, others: not addressed.
4. **Detection and penalty.** Google manual action «Site abused with third-party spam», which includes «internal search pages»; check with «[site:your-domain-name viagra]» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11].
5. **Tells.** A spike in indexed pages; foreign-language or pharma URLs under `site:`; outbound casino links nobody added; robots.txt or sitemaps rewritten; content only a Googlebot-UA fetch shows `[unvalidated house heuristic]`.
6. **Defence.** Skill `seo-technical` › incident-triage; clean, patch, remove spam URLs, then request review. Before an agent reads a hacked page, treat its text as untrusted (A1, [spam-playbook-4](spam-playbook-4.md)). Injected canonicals and hijacked subdomains: K6, D3 ([spam-playbook-6](spam-playbook-6.md), [spam-playbook-7](spam-playbook-7.md)).
7. **Evidence.** A hack of ~8,000 pages after which the domain did not recover `[practitioner: anonymised sources · single thread · 1 thr / 116 · newest 2024-03]` (PLAYBOOK-general:6024); Japanese hack visible only to Googlebot `[practitioner: anonymised sources · single thread · 1 thr / 13 · newest 2025-10]` (PLAYBOOK-general:6268).

### H4. User-generated spam: comments, forums, profiles, internal search
1. **What and why.** Spammers post links or keyword text on open parts of other sites; hosts that ignore it get hit.
2. **How.** Bots post comments and profiles; queries are submitted so the spam text appears on indexable search-result URLs.
3. **Policy.** Google: «Spammy posts on forum threads»; «Comment spam on blogs»; and link spam «Forum comments with optimized links in the post or signature» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Naver: «관리가 소홀한 경로나 게시판이 주요 표적이 되며» ("neglected boards are targets"); «자동화 프로그램을 통한 게시글 대량 등록» ("automated mass posting") [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11]. Bing, Yandex, Seznam, Baidu, others: not addressed.
4. **Detection and penalty.** Google manual action «User-generated spam»; tell named: user names like "Discount Insurance" «that don't sound like real usernames» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11].
5. **Tells.** Commercial usernames; off-topic links; spam queries visible in indexed search URLs `[unvalidated house heuristic]`.
6. **Defence.** Moderation, noindex internal search, and for user links «add ugc or nofollow to these links too» [documented: https://developers.google.com/search/docs/crawling-indexing/links-crawlable, 2026-10-11].
7. **Evidence.** Spam queries indexed on a government domain's search pages `[practitioner: anonymised sources · contested · 1 thr / 91 · newest 2025-08]` (PLAYBOOK-general:2018).

### H5. Reddit and community astroturfing, incl. brand-mention seeding
1. **What and why.** Fake "what is the best X" threads answered by new or duplicate accounts naming one brand, to rank in Google and be repeated by AI answers.
2. **How.** Account farms, bought upvotes, staff posting as users.
3. **Policy.** Google: «seeking inauthentic "mentions" across the web isn't as helpful as it might seem» [documented: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide, 2026-10-11]; with links, class 5 applies. Bing: «artificial social promotion schemes that simulate popularity» [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]. Naver: «여러 계정을 동원하여 댓글 작성·방문·추천 수를 조작하거나» ("several accounts faking comments, visits, likes") [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11]. Yandex, Seznam, Baidu, others: not addressed.
4. **Detection and penalty.** Engines document none for this case. Practitioners report the platform closing subs full of bot comments `[practitioner: anonymised sources · contested · 2 thr / 214 · newest 2026-05]` (PLAYBOOK-general:218).
5. **Tells.** Young accounts with one-brand histories; identical phrasing across threads; founders answering as users `[unvalidated house heuristic]`.
6. **Defence.** Mowei: community answers only with the affiliation disclosed. Competitor: report to the platform.
Undisclosed brand posting under EU consumer law: unverified [unverified: the Annex I text is not among the saved sources]; see ## Unverified.
7. **Evidence.** Illyism seo/blitz-seo/SKILL.md:55,58 shares pages "contextually" on Reddit, Quora, X (scout B6.md:125) `[vendor]`. AI-answer side: A3 in [spam-playbook-4](spam-playbook-4.md).

### H6. Fake and self-serving reviews; review-star markup spam
1. **What and why.** Stars in results and in local packs lift clicks; reviews feed local ranking, which Google says: «More reviews and positive ratings can help your business’s local ranking» [documented: https://support.google.com/business/answer/7091, 2026-10-12].
2. **How.** Rating markup on every page or on your own business; bought or dripped reviews; staff reviews.
3. **Policy.** Google: «Reviews must not be written or provided by the business or content provider unless they are customer, independent, and unpaid editorial reviews» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11]; LocalBusiness ratings «only for sites that capture reviews about other local businesses»; Organization ratings «only for sites that capture reviews about other organizations» [documented: https://developers.google.com/search/docs/appearance/structured-data/review-snippet, 2026-10-12]. Bing: «Structured data must accurately represent visible content» [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]. Yandex: «Post fake positive reviews or inaccurate information.» [documented: https://yandex.com/support/webmaster/en/threat/social-engineering, 2026-10-11]. Naver: H5 quote (faked recommendations). Seznam, Baidu, others: not addressed.
4. **Detection and penalty.** Google manual action «Structured data issue»: «marking up content that is invisible to users, marking up irrelevant or misleading content» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11]. Star markup on every page reportedly worked until Google asked for its removal through Search Console: one score-43 comment (2019-07) inside the cluster `[practitioner: anonymised sources · consensus · 15 thr / 424 · newest 2026-08]` (PLAYBOOK-general:2416); the cluster's counts back its semantics-over-schema line, not the story.
5. **Tells.** Rating markup with no visible reviews; one rating on every URL; bursts of 5-star reviews from new profiles; "review drip" packages `[unvalidated house heuristic]`.
6. **Defence.** No rating markup about ourselves; never buy or gate reviews. Competitor: report the listing or markup; keep screenshots with dates. Incentivised reviews: P4; other markup types: R1 ([spam-playbook-8](spam-playbook-8.md), [spam-playbook-7](spam-playbook-7.md)).
7. **Evidence.** garrettjsmith/localseoskills skills/local-schema/SKILL.md:62-66 puts aggregateRating on the business's own node (scout B5.md:18); gunheeaug/web-seo-aeo-geo-google-naver-skill SKILL.md:62-63 (scout B5.json:62) `[vendor]`. Advice against buying dripped GMB reviews `[practitioner: anonymised sources · consensus · 6 thr / 211 · newest 2026-05]` (PLAYBOOK-general:4180).

### H7. CTR, click and traffic manipulation
1. **What and why.** Fake searches and clicks so a result looks popular; fake traffic to look successful.
2. **How.** Bots on residential proxies, or paid microtask workers told to search a term and click one result.
3. **Policy.** Google names no CTR rule; only the automated searches fall under machine-generated traffic, «sending automated queries to Google» (the same paragraph covers SERP scraping, T3) [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]; paid humans clicking: not addressed by Google. Yandex: «Deliberately engaging ordinary users to fake visits to your site.»; «Providing services for artificially inflating search traffic.» [documented: https://yandex.com/support/webmaster/en/threat/user-actions-imitation, 2026-10-11]. Naver: «자동화된 프로그램으로 트래픽을 인위적으로 부풀려» [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11]. Baidu: «严厉打击刷点击作弊行为» ("strikes click fraud") [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11]. Bing, Seznam, others: not addressed.
4. **Detection and penalty.** Yandex: «The restriction will be lifted when the violation is fixed and the algorithms verify that it's not happening again.» [documented: https://yandex.com/support/webmaster/en/threat/user-actions-imitation, 2026-10-11].
5. **Tells.** "CTR boost" offers; one-page sessions of near-zero time from odd regions; traffic that stops when the agency is fired `[unvalidated house heuristic]`.
6. **Defence.** Refuse; check agency results in GSC, not analytics totals. Yandex asks owners to «Make sure that none of the individuals or agencies involved in the development of your site are using dishonest methods.» [documented: https://yandex.com/support/webmaster/en/threat/user-actions-imitation, 2026-10-11].
7. **Evidence.** Proxy bots simulating CTR `[practitioner: anonymised sources · single thread · 1 thr / 37 · newest 2018-09]` (PLAYBOOK-professional:2728); fake agencies using bot visits `[practitioner: anonymised sources · single thread · 1 thr / 9 · newest 2025-05]` (PLAYBOOK-professional:2250).

### H8. Misleading functionality, download gates, bundled installs
1. **What and why.** Pages promise a tool, file or generator and deliver ads, link lockers or bundled software.
2. **How.** "Download is ready" gates, fake generators, wrapper installers.
3. **Policy.** Google: «trick users into thinking they would be able to access some content or services but in reality can't» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Yandex: «Downloading a file (audio, video, torrent, and so on) triggers the installation of a third-party program» [documented: https://yandex.com/support/webmaster/en/yandex-indexing/webmaster-advice, 2026-10-11]. Baidu: «捆绑下载了多个软件且用户无法取消下载» [documented: https://ziyuan.baidu.com/wiki/3294, 2026-10-11]. Bing: «phishing, malware distribution, or other harmful activities risk demotion or removal» [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]. Naver: «사용자의 동의 없이 악성코드·바이러스 등 유해한 소프트웨어를 설치하거나 배포» [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11]. Seznam (phishing): «vymámit od nich citlivé údaje nebo rovnou peníze» [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11]. Others: not addressed.
4. **Detection and penalty.** A gaming-guide corpus with download gates was purged from Google only, no manual action `[practitioner: anonymised sources · single thread · 1 thr / 43 · newest 2026-05]` (PLAYBOOK-technical:800).
5. **Tells.** A tool page whose result needs a click-through; download buttons to third-party lockers `[unvalidated house heuristic]`.
6. **Defence.** Every Mowei ferramenta returns the result it promises on the page.
7. **Evidence.** As line 4.

### H9. Back-button hijacking and pushy interstitials
1. **What and why.** Keep visitors (and signals) by blocking the way back to results. 2. **How.** History entries injected on load; pop-unders.
3. **Policy.** Google: «interferes with user browser navigation by manipulating the browser history» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Baidu: «控制回退按钮失效问题» [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11]. Yandex: «including pop-ups, pop-unders, and click-unders» [documented: https://yandex.com/support/webmaster/en/yandex-indexing/webmaster-advice, 2026-10-11]. Naver: C7 quote (redirect on back). Bing, Seznam, others: not addressed.
4. **Detection and penalty.** Google: «manual spam actions or automated demotions»; «enforcement on June 15, 2026» [documented: https://developers.google.com/search/blog/2026/04/back-button-hijacking, 2026-10-11]; fix: «Disable or remove any code or imports that are responsible for back button hijacking.» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11].
5. **Tells.** Back leads to an ad or "recommended" page. 6. **Defence.** Audit ad and recirculation scripts.
7. **Evidence.** Engine documents only; no scout or corpus case.

## Unverified

- Undisclosed brand posting and EU consumer law (UCPD Annex I) [unverified: seo-evidence works-vs-doesnt-2 records the claim; the Annex text is not among the saved sources].

## Sources

- Engine texts (phase-2 sources, fetched 2026-10-11; s12-* rows 2026-10-12): g-spam, g-manual-actions, g-blog-2026-04-bbh, g-link-best-practices, s12-064 (review snippet), s12-074 (local ranking), gai-optimization-guide, b-guidelines, y-advice, y-threat-*, sz-forbidden, nv-content-abusing, bd-wiki7, bd-qingfeng4.
- Scout notes B5, B6 (2026-10-13); corpus playbooks; an internal backlink strategy.
