# Spam playbook — know every play (part 7 of 9: domains, crawl traps, structured data)

Refusal rule, entry order, labels and "others": [spam-playbook](spam-playbook.md), first section. Plays added 2026-10-13 from the two reviews' missing-play lists; every engine line was re-read in the saved source.

## Contents
- Domains, hosts and crawl traps (D1–D5)
- Structured data and SERP features (R1–R4)
- Sources

## Domains, hosts and crawl traps (D1–D5)

### D1. Domain farms: mass second-level domains and subdomains
1. **What and why.** Many generated domains or subdomains running content farms, to occupy results and spread risk.
2. **How.** Bulk registration or wildcard subdomains, one template, little content.
3. **Policy.** Seznam (Doménová farma, forbidden): «Vytváření velkého množství domén 2. řádu a subdomén (často jde o automatické generování), na kterých jsou provozovány obsahové farmy.» ("many second-level domains and subdomains, often generated, running content farms") [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11]. Google: «Creating multiple sites with the intent of hiding the scaled nature of the content» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Yandex, Naver, Bing: C2 rows. Baidu: «控制跨领域采集及站群问题» ("site clusters") [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11]. Others: not addressed.
4. **Detection and penalty.** Seznam: a penalty «nezaniká automaticky ve chvíli, kdy je zakázaná technika ze stránek odstraněna» ("does not end the moment the technique is removed") [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11]. Google: moving spam to new subdomains is circumvention (C5).
5. **Tells.** Dozens of near-identical domains or subdomains with one owner; wildcard DNS serving keyword subdomains `[unvalidated house heuristic]`.
6. **Defence.** One brand, one domain; extra sites only with distinct content and a stated owner.
7. **Evidence.** Free public-suffix subdomains share their neighbours' spam reputation `[practitioner: anonymised sources · contested · 1 thr / 9 · newest 2026-01]` (PLAYBOOK-technical:1412); keep an acquired rival live to hold two results `[practitioner: anonymised sources · single thread · 1 thr / 108 · newest 2023-12]` (PLAYBOOK-general:2370), see R8.

### D2. Cybersquatting and look-alike domains
1. **What and why.** A domain holding someone else's trademark, or a near-miss spelling, to take their traffic or pose as them.
2. **How.** Brand-plus-keyword or typo domains, a copied favicon and look.
3. **Policy.** Seznam (Cybersquatting, forbidden): «Cybersquatting je registrace či obchodování s doménovým jménem, které obsahuje registrovanou obchodní značku jiného subjektu.» ("registering or trading a domain containing another's registered trademark"; favicon clause: P3) [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11]. Google (scam and fraud): «impersonating an official business or service through imposter sites» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Yandex (mimicry): text «optimized to accommodate navigational search queries about the original resource» [documented: https://yandex.com/support/webmaster/en/threat/mimicry, 2026-10-11]. Naver: P3 row. Bing, Baidu, others: not addressed.
4. **Detection and penalty.** Google: «Using automated systems, Google seeks to identify pages with scammy or fraudulent content» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Seznam: semi-automatic (K4).
5. **Tells.** The brand in a domain the brand does not own; the same favicon; titles built on the brand's navigational queries `[unvalidated house heuristic]`.
6. **Defence.** Hold obvious variants of our own domain; watch new registrations; report imitators to engine, host and registrar (N3); trademark remedies are for counsel.
7. **Evidence.** Keyword domains bought defensively and redirected `[practitioner: anonymised sources · single thread · 1 thr / 6 · newest 2025-08]` (PLAYBOOK-professional:1026). Typosquatting: corpus and scout searched, not found.

### D3. Spammy free hosts, open sign-ups and unmanaged subdomains
1. **What and why.** Spam on a host anyone can join, or on a forgotten subdomain a third party can take over, borrowing the parent's trust.
2. **How.** Mass free accounts; DNS records still pointing at released cloud resources; misconfigured hosts serving another site's pages.
3. **Policy.** Google: «Spammy accounts on hosting services that anyone can register for» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Naver (hacked content): «도메인 또는 서브도메인 관리 설정 미흡 등으로 제3자에 의해 본래 목적과 무관한 콘텐츠가 생성·노출되는 경우도 포함될 수 있습니다.» ("weak domain or subdomain settings let third parties publish unrelated content") [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11]. Others: not addressed.
4. **Detection and penalty.** Google manual action «Spammy free host»: «if a significant fraction of the pages on a given web hosting service are spammy, we may take manual action on the whole service.» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11]. Also: «Some hosting misconfigurations may cause unexpected cross-domain URL selection.» [documented: https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting, 2026-10-12].
5. **Tells.** Subdomains nobody recognises in `site:` results; DNS entries for retired services; free-host neighbours full of pharma `[unvalidated house heuristic]`.
6. **Defence.** Inventory DNS, remove dangling records; never host partners on open sub-accounts (H1); moderate any user pages (H4).
7. **Evidence.** Free subdomains carry spam reputation `[practitioner: anonymised sources · contested · 1 thr / 9 · newest 2026-01]` (PLAYBOOK-technical:1412); mass free-blog spam inflates link counts `[practitioner: anonymised sources · single thread · 1 thr / 9 · newest 2021-08]` (PLAYBOOK-professional:3626). Subdomain takeover: corpus searched, not found.

### D4. Crawl-trap doorways: facets, calendars, internal search
1. **What and why.** Endless filter, sort, calendar or site-search URLs indexed as landing pages for every query variant; also a channel for others' spam (H4).
2. **How.** Every parameter combination linked and indexable; search pages with the query in the title.
3. **Policy.** Yandex (low-quality marker): «Pages with site search results or results of selecting products, services, or other items by condition, if they are not very informative and not useful for users.» [documented: https://yandex.com/support/webmaster/en/yandex-indexing/webmaster-advice, 2026-10-11]. Seznam: generated search pages out of crawling (C6 row). Google: doorways «closer to search results than a clearly defined, browseable hierarchy» (C2) [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]; guidance names traps: «infinite scrolling pages that duplicate information on linked pages, or differently sorted versions of the same page» [documented: https://developers.google.com/crawling/docs/crawl-budget, 2026-10-12]. Bing: crawl-waste guidance only. Naver, Baidu, others: not addressed.
4. **Detection and penalty.** Google manual action «Site abused with third-party spam» includes «Internal search results where the user's query appears geared at promoting a third-party website or service» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11]; the cost: «this wastes a lot of Google crawling time on your site» [documented: https://developers.google.com/crawling/docs/crawl-budget, 2026-10-12].
5. **Tells.** Indexed parameter URLs far outnumber products; search-page titles with odd queries `[unvalidated house heuristic]`.
6. **Defence.** noindex or block filter, sort, calendar and search URLs; index curated category pages only (skill `seo-technical` › crawl-and-index).
7. **Evidence.** Spam text indexed on site-search URLs `[practitioner: anonymised sources · contested · 1 thr / 91 · newest 2025-08]` (PLAYBOOK-general:2018); ~500,000 calendar URLs `[practitioner: anonymised sources · single thread · 1 thr / 57 · newest 2022-11]` (PLAYBOOK-general:652).

### D5. Open-redirect link spam
1. **What and why.** Links aimed at a trusted site's open redirector (`redirect.php?url=…`) so link tools count a "backlink" from that domain.
2. **How.** Any URL on a trusted host that forwards to a target given in a parameter.
3. **Policy.** No engine text names open redirects (searched 2026-10-13). Closest: Google «Check for URLs on your site that redirect users to somewhere other than where they expected to go.» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11]; Yandex «Make sure that that link destinations match users' expectations and the described purpose.» [documented: https://yandex.com/support/webmaster/en/threat/unexpected-redirection, 2026-10-11]. Others: not addressed.
4. **Detection and penalty.** Host side: C7 and H3 checks. Receiving side: such hops fool link tools, not Google, which ignores them `[practitioner: anonymised sources · single thread · 1 thr / 9 · newest 2022-09]` (PLAYBOOK-technical:4896).
5. **Tells.** Many backlinks sharing one `/redirect?url=` pattern; our logs showing redirect hits to unknown targets `[unvalidated house heuristic]`.
6. **Defence.** Our redirects: allow-list or sign targets. Link audits: classify such links as spam, not earned; disavow only on Google's two conditions: many such links and an actual or likely manual action (N1).
7. **Evidence.** As line 4; scout searched, not found.

## Structured data and SERP features (R1–R4)

### R1. Rich-result markup spam: jobs, events, products, recipes, lists, hidden markup
1. **What and why.** Markup that says a page is a job, event, product, recipe or list item when it is not, to win rich results and space.
2. **How.** Event markup on coupons, JobPosting on ads or expired jobs, Product on a company, one aggregate element for a whole list, markup on hidden elements.
3. **Policy.** Google manual-action rows: «JobPosting structured data found on pages that don't have job posting content. This is against our guidelines.»; «A non-event item has been marked as an event. For example, a holiday or a coupon.»; «A non-product, or generic item, has been marked as a product.»; «Aggregating data from multiple items into one structured data element is against our spam policies.»; «Structured data found on elements that are not visible to the user. This is against our guidelines.» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11]. FAQ and HowTo rich results are retired for every site: «How-to results no longer appear in Google Search» [documented: https://developers.google.com/search/blog/2023/08/howto-faq-changes, 2026-10-11]; «The FAQ rich result feature is no longer shown in Google Search results» (from 2026-05-07) [documented: https://developers.google.com/search/updates, 2026-10-11]. Unused markup is harmless («Structured data that's not being used does not cause problems for Search» [documented: https://developers.google.com/search/blog/2023/08/howto-faq-changes, 2026-10-11]); misleading FAQ or HowTo markup is still a «Structured data issue» (line 4). Bing: «Structured data must accurately represent visible content» (H6). Others: not addressed.
4. **Detection and penalty.** Google manual action «Structured data issue»: «marking up content that is invisible to users, marking up irrelevant or misleading content, or other manipulative behavior.» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11]. Bing: such markup «may be ignored and can affect trust and eligibility for enhanced features» [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11].
5. **Tells.** Markup types that do not match what a visitor sees; event markup on promotions; JobPosting with no way to apply `[unvalidated house heuristic]`.
6. **Defence.** Mark up only what is visible and true; check each template in the Rich Results Test and against the rendered page.
7. **Evidence.** Misuse removes the rich result, not rankings `[practitioner: anonymised sources · consensus · 2 thr / 27 · newest 2025-04]` (PLAYBOOK-technical:2454); squirrelscan/squirrelscan@docs/rules/content/date-agreement.mdx compares visible, JSON-LD and sitemap dates, a detector (scout B6.md:26) `[vendor]`. Review stars: H6 ([spam-playbook-3](spam-playbook-3.md)).

### R2. Fake fact-checks: ClaimReview on pages that review no claim
1. **What and why.** Fact-check markup that "rates" a rival's claim false, or dresses a sales page as a fact-check, to borrow a fact-check label.
2. **How.** ClaimReview with no review on the page, or no source behind the verdict.
3. **Policy.** Google: «ClaimReview structured data found on pages that don't contain a claim review. This is against our guidelines.»; «Pages with ClaimReview structured data do not include a supporting source or reference. This is against our guidelines.» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11]. Google has since dropped the rich result: Claim Review is listed under «The following structured data types will no longer be supported in Google Search results» [documented: https://developers.google.com/search/blog/2025/06/simplifying-search-results, 2026-10-12]. Others: not addressed.
4. **Detection and penalty.** Google manual action «Structured data issue» (R1).
5. **Tells.** ClaimReview on commercial pages; verdicts about competitors; no cited source `[unvalidated house heuristic]`.
6. **Defence.** Never mark up our comparisons as fact-checks; report a rival's fake fact-check with dated screenshots.
7. **Evidence.** A proposal to tag unique facts with claimReviewed to become the origin node was rejected in replies `[practitioner: anonymised sources · contested · 1 thr / 58 · newest 2026-01]` (PLAYBOOK-technical:204). Scout: searched, not found.

### R3. Entity and site-name spam: keyword names, false sameAs
1. **What and why.** Push a keyword or a false identity into the site name, Organization markup or entity links, so the brand matches generic queries or looks bigger.
2. **How.** Keyword site names, sameAs links to profiles the organisation does not own, Organization markup borrowing another company's identity.
3. **Policy.** Google, guidance not a spam rule: «Choose a unique name that accurately reflects the identity of your site and isn't misleading for users. The name you choose must follow Search content policies.»; «A generic name like "Best Dentists In Iowa" is unlikely to be selected by our system as a site name» [documented: https://developers.google.com/search/docs/appearance/site-names, 2026-10-12]. Organization markup warns «If your site violates one or more of these guidelines, then Google may take manual action against it.» [documented: https://developers.google.com/search/docs/appearance/structured-data/organization, 2026-10-12]. Bing guidance: «Use clear and consistent naming for people, organizations, products, and locations.» [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]. Yandex: mimicry (D2). Others: not addressed.
4. **Detection and penalty.** «Google's generation of site names on the Google Search results page is completely automated» [documented: https://developers.google.com/search/docs/appearance/site-names, 2026-10-12]; markup misuse: R1.
5. **Tells.** Keyword site names; sameAs to unrelated or bought profiles; knowledge-panel edits by the brand `[unvalidated house heuristic]`.
6. **Defence.** Our site name is our brand; sameAs only to profiles we control; never edit reference works about ourselves (L9, [spam-playbook-8](spam-playbook-8.md)).
7. **Evidence.** Honest entity work: sameAs to verification profiles `[practitioner: anonymised sources · single thread · 1 thr / 8 · newest 2025-10]` (PLAYBOOK-professional:2774); metawhisp/amazing-seo-skill@scripts/schema_graph_checker.py:5-19 checks @id consistency, a detector (scout B3.md:107) `[vendor]`. Knowledge-panel and Wikidata spam: corpus searched, not found.

### R4. Discover and News bait, AMP mismatch, hidden publishers
1. **What and why.** Headlines and images that promise what the article lacks; sites posing as news outlets or hiding who runs them, to win Discover and Top Stories traffic.
2. **How.** Curiosity-gap headlines and thumbnails, AMP versions that differ from the page, fake bylines, hidden owner or country.
3. **Policy.** Google (News and Discover manual actions): content that «misleads users into engaging with it by promising details which are not reflected in the content.»; «Google has detected content on your site that appears to conceal or misrepresent the site ownership or purpose.»; news sources «should provide clear dates and bylines» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11]. Naver: «조회수를 높일 목적으로 내용과 무관한 자극적인 제목이나 낚시성 썸네일을 사용하지 마세요.» ("no sensational titles or bait thumbnails unrelated to the content") [documented: https://searchadvisor.naver.com/guide/content-basic, 2026-10-11]. Others: not addressed.
4. **Detection and penalty.** Google manual actions per policy; AMP: «There is a difference in content between the AMP version and its canonical web page.»; such AMP pages «will not be shown in Google Search: the canonical page will be shown instead.» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11]. Circumvention costs features: «restricting or removing eligibility for some of our search features (for example, Top Stories, Discover)» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11].
5. **Tells.** The headline's answer withheld; a thumbnail unrelated to the article; no owner, address or editors; an AMP page shorter than the original `[unvalidated house heuristic]`.
6. **Defence.** Headlines say what the page delivers; About page with owner, address and editors; one content version.
7. **Evidence.** Guides in a News sitemap grouped with risk signals on a deindexed site `[practitioner: anonymised sources · single thread · 1 thr / 27 · newest 2026-05]` (PLAYBOOK-technical:2124). Clickbait thumbnails, fake publishers: corpus and scout searched, not found.

## Sources

- Engine texts (phase-2 sources, fetched 2026-10-11; s12-* rows 2026-10-12): g-spam, g-manual-actions, g-faq-howto, g-search-updates, s12-036 (crawl budget), s12-052 (simplified results), s12-063 (canonical troubleshooting), s12-112 (site names), s12-113 (organization), b-guidelines, y-advice, y-threat-mimicry, y-threat-unexpected-redirection, sz-forbidden, nv-content-abusing, nv-content-basic, bd-wiki7.
- Corpus playbooks; scout notes B3, B6 (2026-10-13); missing-play lists from two independent model reviews (2026-10-13).
