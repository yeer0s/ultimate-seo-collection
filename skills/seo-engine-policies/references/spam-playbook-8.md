# Spam playbook — know every play (part 8 of 9: trust signals, SERP occupation, more links, local)

Refusal rule, entry order, labels and "others": [spam-playbook](spam-playbook.md), first section. Plays added 2026-10-13 from the two reviews' missing-play lists (L9 moved here from part 1); every engine line was re-read in the saved source.

## Contents
- Trust signals and SERP occupation (R5–R8)
- More link schemes (L9–L11)
- More local and review plays (P4–P5)
- Sources

## Trust signals and SERP occupation (R5–R8)

### R5. Bait titles and snippets (Naver 낚시성)
1. **What and why.** Titles or snippets carrying popular queries the page does not answer, to catch clicks.
2. **How.** Trending terms in titles and descriptions; snippets promising content the body lacks.
3. **Policy.** Naver (낚시성): «실제 콘텐츠와 무관한 검색어를 제목이나 본문에 삽입하여 검색 유입만을 노리는 경우입니다. 제목·설명과 실제 내용이 일치하지 않는 것이 특징입니다.» ("unrelated search terms in title or body; title and description do not match the content") [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11]; «브랜드와 관련 없는 인기 검색어·화제의 키워드 삽입 시 품질 평가에 불이익을 받을 수 있습니다.» ("unrelated trending keywords can lower the quality rating") [documented: https://searchadvisor.naver.com/guide/content-basic, 2026-10-11]. Google: Discover and News, R4 ([spam-playbook-7](spam-playbook-7.md)); web results, keyword stuffing (C4). Others: not addressed.
4. **Detection and penalty.** Naver: as quoted. Google rewrites descriptions that the page does not support (line 7).
5. **Tells.** A title promising an answer the page lacks; trending names or events on unrelated pages `[unvalidated house heuristic]`.
6. **Defence.** Title and description state what the page delivers; no trending terms we do not cover.
7. **Evidence.** Google swaps in page text for descriptions `[practitioner: anonymised sources · consensus · 8 thr / 236 · newest 2025-04]` (PLAYBOOK-general:6294); script-injected descriptions dropped when visible text does not confirm them `[practitioner: anonymised sources · single thread · 1 thr / 12 · newest 2025-05]` (PLAYBOOK-technical:1162).

### R6. Search-suggestion poisoning: autocomplete, related searches
1. **What and why.** Fake query volume so suggestions pair a brand with a term ("<brand> best insurance"), or a rival with "scam".
2. **How.** Bots or paid workers typing the phrase again and again (H7 machinery, [spam-playbook-3](spam-playbook-3.md)).
3. **Policy.** No engine's webmaster rules name it (searched 2026-10-13). Bing describes the input and its guard: suggestions are «based on the popularity of related searches on Bing»; «Bing takes steps to ensure that users are not inadvertently led to potentially harmful, offensive, or misleading content via search suggestions.» [documented: https://support.microsoft.com/en-us/topic/how-bing-delivers-search-results-d18fc815-ac37-4723-bc67-9229ce3eb6a3, 2026-10-11]. The automated queries themselves: Google machine-generated traffic, Yandex user-action imitation (H7). Others: not addressed.
4. **Detection and penalty.** Bing uses «a combination of proactive and reactive algorithmic and manual interventions» [documented: https://support.microsoft.com/en-us/topic/how-bing-delivers-search-results-d18fc815-ac37-4723-bc67-9229ce3eb6a3, 2026-10-11].
5. **Tells.** A suggestion pairing a small brand with a head term overnight; "autocomplete marketing" offers `[unvalidated house heuristic]`.
6. **Defence.** Refuse such offers; a defamatory suggestion about us goes to the engine's feedback channel.
7. **Evidence.** The corpus mentions suggestions only as keyword research `[practitioner: anonymised sources · single thread · 1 thr / 186 · newest 2021-04]` (PLAYBOOK-general:5432); manipulation: corpus and scout searched, not found.

### R7. Fabricated expertise: fake authors, reviewers, credentials, addresses
1. **What and why.** Invented experts, "reviewed by" lines or company details, to look trustworthy on money and health topics.
2. **How.** AI headshots, made-up names and bios, borrowed credentials, virtual-office addresses.
3. **Policy.** Google: fabricated creator profiles, «using AI-generated headshots, made-up names, or false credentials to make content appear as if it was written by human experts», are «a form of deception» [documented: https://developers.google.com/search/docs/fundamentals/creating-helpful-content, 2026-10-12]; News and Discover: «Google doesn't allow content or accounts that mislead or confuse users by pretending to be someone else or pretend to represent an organization you do not.» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11]. Naver: «잘못된 전화번호·주소·신청 링크, 합성 또는 생성 이미지·동영상 등 명백히 허위이거나» ("false phone numbers, addresses, links, synthetic images") [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11]. Yandex (mimicry): «The site doesn't explain how it is connected to the original resource (ownership, partnership, licensing), or does so in a vague, unclear way.» [documented: https://yandex.com/support/webmaster/en/threat/mimicry, 2026-10-11]. Baidu: «创作者的账号应该是真实可信的» ("creator accounts must be real and credible") [documented: https://ziyuan.baidu.com/college/articleinfo?id=2947, 2026-10-11]. Bing, Seznam, others: not addressed.
4. **Detection and penalty.** Google: «Any form of deception makes a page untrustworthy to both users and our automated quality systems, and is a signal of a low-quality page.» [documented: https://developers.google.com/search/docs/fundamentals/creating-helpful-content, 2026-10-12]; News manual action «Transparency (News and Discover)».
5. **Tells.** Author photos found on stock or AI sites; bios with no trace elsewhere; one reviewer for every topic; a virtual-office address `[unvalidated house heuristic]`.
6. **Defence.** Real named authors with checkable profiles; "reviewed by" only after a real review; Mowei's legal entity and address on the About page.
7. **Evidence.** An AI portrait plus a fake profile is not a signal `[practitioner: anonymised sources · single thread · 1 thr / 22 · newest 2025-03]` (PLAYBOOK-technical:2516); obvious AI images and anonymous authorship called an E-E-A-T failure `[practitioner: anonymised sources · consensus · 2 thr / 21 · newest 2026-05]` (PLAYBOOK-technical:820); siddiqss/semantic-seo-suite@scripts/validate_draft.py rejects unsourced claims, a detector (scout B2.md:48) `[vendor]`.

### R8. Brand-SERP occupation and reputation flooding
1. **What and why.** Many owned sites, profiles or microsites built to fill every result for a name or query, to bury a bad review or a rival.
2. **How.** Exact-name domains and profiles, interlinked; acquired rival domains kept live (D1, [spam-playbook-7](spam-playbook-7.md)).
3. **Policy.** Google (doorways): «Having multiple websites with slight variations to the URL and home page to maximize their reach for any specific query» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Yandex: groups of sites «Created to occupy multiple positions in search results and drive traffic.» [documented: https://yandex.com/support/webmaster/en/yandex-indexing/webmaster-advice, 2026-10-11]. Seznam (doorway): «Jejich účelem je umístit se na širokou škálu dotazů na jakékoliv pozici» ("meant to rank for a wide range of queries"); duplicate sites: one is kept and «ostatní budou penalizovány» ("the others will be penalised") [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11]. Naver: «검색 결과를 점유할 목적으로» ("to occupy search results") [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11]. Bing intervenes where «bad actors are intentionally manipulating search results to surface low authority content, exploiting a data void» [documented: https://support.microsoft.com/en-us/topic/how-bing-delivers-search-results-d18fc815-ac37-4723-bc67-9229ce3eb6a3, 2026-10-11]. Baidu: D1. Others: not addressed.
4. **Detection and penalty.** C2 and D1 rules. Real profiles on real platforms are not doorways `[unvalidated house heuristic]`.
5. **Tells.** New same-owner sites ranking only for one name; thin interlinked "about X" microsites `[unvalidated house heuristic]`.
6. **Defence.** Answer criticism on our own pages and real profiles; never build sites to bury a review; a rival's flood: report clear doorways.
7. **Evidence.** Owned properties in an exact name to outrank a negative result `[practitioner: anonymised sources · consensus · 3 thr / 285 · newest 2023-01]` (PLAYBOOK-general:4658); flooding results with positive free blogs `[practitioner: anonymised sources · single thread · 1 thr / 38 · newest 2017-06]` (PLAYBOOK-professional:2710).

## More link schemes (L9–L11)

### L9. Profile stacking and wiki or encyclopedia reference links
1. **What and why.** Brand profiles on 20+ platforms reported as "referring domains"; own links inserted into Baike or wiki reference lists.
2. **How.** Profiles carry a homepage link; reference lists are edited to cite the brand.
3. **Policy.** Google: «Creating low-value content primarily for the purposes of manipulating linking and ranking signals» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Bing: «artificial social promotion schemes that simulate popularity» [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]. Others: L class table ([spam-playbook](spam-playbook.md)) or not addressed.
4. **Detection and penalty.** Class rule; no engine documents profile links as a separate case.
5. **Tells.** Profile links counted as month-1 referring domains; reference edits by the brand `[unvalidated house heuristic]`.
6. **Defence.** Keep only profiles users need; never edit reference works about yourself.
7. **Evidence.** inhouseseo/superseo-skills skills/linkbuilding/SKILL.md:49 (scout B1.md:38); HeiGe 03-publishing-channels.md:184 (scout B5.md:81) `[vendor]`.

### L10. Tiered link building
1. **What and why.** Spam links (tier 2, 3) point at pages that link to the money site (tier 1), so the spam never touches it directly.
2. **How.** Automated links aimed at guest posts, profiles or network pages that carry the money link.
3. **Policy.** Google: «Creating low-value content primarily for the purposes of manipulating linking and ranking signals»; «Using automated programs or services to create links to your site» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Bing: «link buying, link spamming, private networks» [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]. No engine names tiers. Yandex, Seznam, Naver: L class table. Baidu, others: not addressed.
4. **Detection and penalty.** Google's L rules apply to every tier; no engine documents how tiers are found.
5. **Tells.** "Tier 2" or "link juice boost" packages; spam domains linking to your guest posts `[unvalidated house heuristic]`.
6. **Defence.** Refuse; in audits, follow links one hop out from your best-linked pages.
7. **Evidence.** Mass automated links aimed straight at a main site ended in a penalty `[practitioner: anonymised sources · single thread · 1 thr / 96 · newest 2015-07]` (PLAYBOOK-professional:3466); force-indexing the links you build `[practitioner: anonymised sources · consensus · 3 thr / 102 · newest 2024-02]` (PLAYBOOK-general:352). "Tiered" by name: corpus searched, not found.

### L11. Rented links: link leasing and paid link bars
1. **What and why.** Followed links rented by the month (sidebar, footer or in-content), removed when payment stops.
2. **How.** Subscription placements; link bars sold per month.
3. **Policy.** Seznam: «Umisťování předplacených odkazových lišt a jiných výměnných odkazových systémů do HTML kódu stránky je bráno jako snaha o manipulaci s přirozeným rozdělením ranku.» ("prepaid link bars and exchange systems in the HTML are manipulation") [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11]. Google: «Exchanging money for links, or posts that contain links» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Bing, Yandex, Naver: L class table. Baidu, others: not addressed.
4. **Detection and penalty.** Google manual actions «Unnatural links to your site» and «Unnatural links from your site» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11].
5. **Tells.** Monthly link invoices; links that vanish when a contract ends; sitewide footer links to unrelated businesses `[unvalidated house heuristic]`.
6. **Defence.** Refuse; any paid placement carries `rel="sponsored"`.
7. **Evidence.** Illyism/seo-skills@seo/linkdr/SKILL.md:32-36,147 sells DR-tiered paid links (scout B6.md:123); noique dsite-seo-playbook.md:645-656 sets monthly link quotas (scout B2.md:103) `[vendor]`. Leasing by name: corpus searched, not found.

## More local and review plays (P4–P5)

### P4. Incentivised and gated reviews
1. **What and why.** Reviews paid for with discounts, vouchers or gifts and not disclosed; or only happy customers sent to the public review page ("gating").
2. **How.** "Review for a discount" offers; a pre-survey that routes low scores to a private form.
3. **Policy.** Google (review snippets): «Don't include fake or undisclosed incentivized reviews on your page or in your structured data markup.»; banned: «Reviews written in exchange for a benefit (such as money, discounts, vouchers, or free products) that don't clearly and prominently disclose the incentivization» [documented: https://developers.google.com/search/docs/appearance/structured-data/review-snippet, 2026-10-12]; self-written reviews: H6 ([spam-playbook-3](spam-playbook-3.md)). Yandex: «Post fake positive reviews or inaccurate information.» [documented: https://yandex.com/support/webmaster/en/threat/social-engineering, 2026-10-11]. Google's Business Profile review policy (gating) is not among the saved sources: see Unverified in [spam-playbook-9](spam-playbook-9.md). Others: not addressed.
4. **Detection and penalty.** Yandex: «The algorithms also consider the fact that user reviews can be manipulated, so such cases don't affect their decision.» [documented: https://yandex.com/support/webmaster/en/threat/unfair-actions, 2026-10-11]. Google markup: «Structured data issue» (R1, [spam-playbook-7](spam-playbook-7.md)).
5. **Tells.** "Leave a review, get 10 %" emails; review requests sent only after a top score; review counts jumping after a promotion `[unvalidated house heuristic]`.
6. **Defence.** Ask every customer the same way; no reward unless the platform allows it and it is disclosed; never route by score.
7. **Evidence.** Advice against buying dripped GMB reviews `[practitioner: anonymised sources · consensus · 6 thr / 211 · newest 2026-05]` (PLAYBOOK-general:4180). Review gating by name: corpus searched, not found.

### P5. Fake addresses, keyword names and citation stuffing
1. **What and why.** Listings at addresses where the business is not, keyword-padded names, and the same false data pushed to many directories, to show in more local packs.
2. **How.** Virtual offices, co-working desks, a spoofed address per city; directory blasts with keyword names.
3. **Policy.** Google Business Profile rules: not saved (P1, [spam-playbook-4](spam-playbook-4.md)). Google's web rules cover the page side: «Blocks of text that list cities and regions that a web page is trying to rank for» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Naver: «잘못된 전화번호·주소·신청 링크» ("wrong phone numbers, addresses, application links") [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11]. Others: not addressed.
4. **Detection and penalty.** Not in saved sources. Spoofed-address listings were removed for good, with their reviews `[practitioner: anonymised sources · single thread · 1 thr / 95 · newest 2019-03]` (PLAYBOOK-general:4344).
5. **Tells.** Several listings at one co-working address; a city in the business name; one phone across brands `[unvalidated house heuristic]`.
6. **Defence.** One listing per real staffed location; report rivals with photos and dates (P1).
7. **Evidence.** As line 4; fake listings reported through the redress form `[practitioner: anonymised sources · single thread · 1 thr / 23 · newest 2020-02]` (PLAYBOOK-professional:2430); garrettjsmith/localseoskills@skills/gbp-suspension-recovery/SKILL.md:13-181, a reinstatement playbook (scout B5.md:15) `[vendor]`. Other listing platforms: Unverified ([spam-playbook-9](spam-playbook-9.md)).

## Sources

- Engine texts (phase-2 sources, fetched 2026-10-11; s12-* rows 2026-10-12): g-spam, g-manual-actions, s12-064 (review snippet), s12-079 (helpful content), b-guidelines, b-how-bing-delivers, y-advice, y-threat-mimicry, y-threat-social-engineering, y-threat-unfair-actions, sz-forbidden, nv-content-abusing, nv-content-basic, bd-quality-guide.
- Corpus playbooks; scout notes B1, B2, B5, B6 (2026-10-13); missing-play lists from two independent model reviews (2026-10-13).
