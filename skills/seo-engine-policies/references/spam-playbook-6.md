# Spam playbook — know every play (part 6 of 9: translation, cloaking and hiding variants)

Refusal rule, entry order, labels and "others": [spam-playbook](spam-playbook.md), first section. Plays added 2026-10-13 from the two reviews' missing-play lists; every engine line was re-read in the saved source.

## Contents
- Class 14 and more cloaking and hiding (C9, K1–K6)
- Sources

## Class 14 and more cloaking and hiding (C9, K1–K6)

### C9. Machine-translated auto-sites
1. **What and why.** One site auto-translated into many locales to multiply pages. 2. **How.** Bulk translation, no review.
3. **Policy.** Google: «automated transformations like synonymizing, translating, or other obfuscation techniques» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Yandex: «Contain content translated from another language using low-quality, Ai-generated or machine translation.» [documented: https://yandex.com/support/webmaster/en/yandex-indexing/webmaster-advice, 2026-10-11]. Bing names no translation rule. Seznam, Naver, Baidu, others: not addressed.
4. **Detection and penalty.** Google and Yandex: C5 rules ([spam-playbook-2](spam-playbook-2.md)). Bing: only unreviewed bulk output meets its scaled row, «content generated without oversight, quality control, or editorial review» [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11].
5. **Tells.** Many locales at once `[unvalidated house heuristic]`. 6. **Defence.** Translate only what is reviewed (skill `seo-technical` › international-and-hreflang).
7. **Evidence.** March 2026 reportedly deindexed machine-translated pages above all `[practitioner: anonymised sources · single thread · 1 thr / 27 · newest 2026-05]` (PLAYBOOK-technical:852).

### K1. Cloaked images
1. **What and why.** Image results show one picture and the page another: a clean thumbnail to win clicks, or an image Google sees covered by text.
2. **How.** The server answers image requests differently for Google, or overlays a block on the image Google gets.
3. **Policy.** Google: «Serving images to Google that are obscured by another image, for example: a block of text blocking an image.»; «Serving images to Google that are different than the image served to a page visitor.» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11]. Bing, Yandex, Seznam, Naver: general cloaking rows (C1), none names images. Baidu, others: not addressed.
4. **Detection and penalty.** Google manual action «Cloaked images»; the one exception: «Cloaking is acceptable only for opting out of image search inline linking as detailed below.» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11].
5. **Tells.** The image in image search differs from the one on the page; image URLs that answer differently by referrer or user agent `[unvalidated house heuristic]`.
6. **Defence.** Serve one image to everyone; to stop inline display, use Google's documented opt-out, never a swap.
7. **Evidence.** Engine documents only; corpus and scout searched, not found (2026-10-13).

### K2. Paywall and consent-wall cloaking
1. **What and why.** Googlebot gets the full article, people get a paywall, login or consent wall, so the page ranks for text users cannot read.
2. **How.** A gate keyed on crawler user agent or IP, with no paywall markup.
3. **Policy.** Google allows gating only openly: «If you operate a paywall or a content-gating mechanism, we don't consider this to be cloaking if Google can see the full content of what's behind the paywall» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]; publishers should «enclose paywalled content with structured data in order to help Google differentiate paywalled content from the practice of cloaking» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11]. Others: C1 rows; no engine names paywalls. Consent walls: not addressed by any saved page (searched 2026-10-13).
4. **Detection and penalty.** Google manual action «Cloaking and/or sneaky redirects» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11].
5. **Tells.** URL Inspection shows full text that people never see; no paywall markup; free access only for clicks from Google `[unvalidated house heuristic]`.
6. **Defence.** Paywalled pages carry paywall markup; consent banners never hide from people what bots get.
7. **Evidence.** Users liken indexed paywalls to cloaking `[practitioner: anonymised sources · single thread · 1 thr / 250 · newest 2024-04]` (PLAYBOOK-general:6422); paywall markup and free lead-ins as the honest route `[practitioner: anonymised sources · single thread · 1 thr / 40 · newest 2020-11]` (PLAYBOOK-general:2606).

### K3. Conditional cloaking: by time, place or test bucket
1. **What and why.** A page is clean when checked and spam later, or spam only for some countries, IP ranges or an experiment bucket that holds every bot, so reviews miss it.
2. **How.** Rules keyed on time, IP location, referrer, or an experiment bucket pinned for crawlers.
3. **Policy.** Naver: «레퍼러나 브라우저의 에이전트명 등 기준으로, 특정 경로나 기기에서만 전혀 다른 내용을 보여주는 경우도 해당됩니다.» ("entirely different content only on certain paths or devices") [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11]; delayed redirects: C7. Yandex draws the line: not cloaking when «The site's content differs depending on the user’s region.» or «You're running an A/B test, and users and search engines see the same content in different design or UI.» [documented: https://yandex.com/support/webmaster/en/threat/cloaking, 2026-10-11]; a test that shows bots other content is outside it. Google, Bing, Seznam: C1 cloaking rows. Baidu, others: not addressed.
4. **Detection and penalty.** Google checks redirects that fire «only users coming from Google search, or only users coming from a particular range of IP addresses» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11]. Splitting Googlebot and users by user agent, IP or host for a test is called cloaking `[practitioner: anonymised sources · contested · 1 thr / 29 · newest 2023-06]` (PLAYBOOK-technical:1338).
5. **Tells.** Content changes after the first crawl; country-only redirects to unrelated offers; a test tool that holds crawlers in a different content variant `[unvalidated house heuristic]`.
6. **Defence.** Tests change design, not content, and canonical the variants; regional pages keep the same core content; re-check from several regions and after a delay.
7. **Evidence.** hreflang served only to bot user agents fits Google's own cloaking examples `[practitioner: anonymised sources · single thread · 1 thr / 17 · newest 2020-05]` (PLAYBOOK-technical:3640); tigerless-labs/seo-ops@references/checklist/checklist.md:13-44 checks that two anonymous fetches match, a detector (scout B1.md:45) `[vendor]`. Time-based cloaking: corpus searched, not found.

### K4. Link cloaking: rel swaps and links that go elsewhere than href
1. **What and why.** A link passes credit to crawlers but is nofollowed or different for people, or its real target differs from what the page shows.
2. **How.** Different rel values or hrefs by user agent; script that rewrites the destination on click.
3. **Policy.** Seznam: «Za nepřirozené odkazy se označují také odkazy, které vedou jinam, než stránka naznačuje nebo je uvedeno v atributu „href“, a tím klamou uživatele.» ("links that lead elsewhere than the page or the href says") [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11]. Google names no rel swap; paid links must not pass credit, as in «Text advertisements or text links that don't block ranking credit» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11], and bot-only markup is cloaking (C1). Yandex: deceptive external links (L class table, [spam-playbook](spam-playbook.md)). Bing: C1 row. Naver, Baidu, others: not addressed.
4. **Detection and penalty.** Google: L rules and the C1 manual action. Seznam: «Zakázané optimalizační techniky jsou posuzovány poloautomaticky» ("judged semi-automatically") [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11].
5. **Tells.** rel differs between a Googlebot-UA fetch and a browser; hrefs rewritten on click; paid links followed only in the server HTML `[unvalidated house heuristic]`.
6. **Defence.** Diff raw and rendered HTML per user agent (C1 method); sponsored links carry `rel="sponsored"` in every version.
7. **Evidence.** Script-only links drop out of Google's link graph `[practitioner: anonymised sources · single thread · 1 thr / 12 · newest 2025-11]` (PLAYBOOK-technical:662); iklynow-hue/seo-geo-skills@references/architecture.md:21-26,83-92 compares raw and rendered hrefs, a detector (scout B3.md:120) `[vendor]`. Rel swaps by user agent: corpus searched, not found.

### K5. Hiding vectors beyond colour and size
1. **What and why.** Keyword or link text hidden by `display: none`, off-screen placement, images, or DOM that never renders, including text aimed at AI (A1, A2).
2. **How.** CSS rules, positioning, image overlays, collapsed elements with no control to open them.
3. **Policy.** Google: «Hiding text behind an image»; «Using CSS to position text off-screen»; not a violation: «Text that's only accessible to screen readers and is intended to improve the experience for those using screen readers» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Yandex: «Text hidden using special techniques: display: none, shifting the text from the visible part of the site.»; not hidden: «Text truncation (provided the hidden part can be expanded) to improve usability.» [documented: https://yandex.com/support/webmaster/en/threat/seo-text, 2026-10-11]. Naver: «화면 밖 영역에 텍스트를 배치하는 경우» ("placing text outside the screen") [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11]. Seznam: C3 (filed under cloaking). Bing, Baidu, others: not addressed. `noscript`, SVG titles, CSS `content:` and shadow DOM: no engine names them (searched 2026-10-13); Google's renderer «flattens the shadow DOM and light DOM content» [documented: https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics, 2026-10-11].
4. **Detection and penalty.** Google manual action «Hidden text and/or keyword stuffing»: «Check for any text hidden using CSS styling or positioning.» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11].
5. **Tells.** Hidden elements with no toggle; rendered text missing from a screenshot; keyword lists in `noscript` `[unvalidated house heuristic]`.
6. **Defence.** Lint rendered pages for hidden text with no control (tabs, accordions and screen-reader text are fine).
7. **Evidence.** `display: none` H1s read as engine-only content `[practitioner: anonymised sources · single thread · 1 thr / 32 · newest 2021-09]` (PLAYBOOK-professional:632); accordion text in the first HTML counts `[practitioner: anonymised sources · single thread · 1 thr / 18 · newest 2026-04]` (PLAYBOOK-technical:1110); mykpono/ultimate-seo-geo@scripts/hidden_instructions.py finds CSS-hidden and invisible-Unicode text, a detector (scout B3.md:74) `[vendor]`.

### K6. Canonical hijacking
1. **What and why.** Google is made to pick someone else's URL as canonical: a hack injects a cross-domain canonical or redirect, or a copy outranks the original.
2. **How.** Injected `rel="canonical"` or 3xx on a compromised site; script that changes the canonical after load; clones with rewritten canonicals.
3. **Policy.** Google lists it as an attack: «Some attacks on websites introduce code that returns an HTTP 3xx redirect or inserts a cross-domain rel="canonical" link annotation into the HTML <head> or HTTP header» [documented: https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting, 2026-10-12]; guidance: «specify the canonical URL in the HTML source code and make sure that JavaScript doesn't change the canonical link element.» [documented: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls, 2026-10-12]. Bing: «Canonical tags help signal preference but do not replace fixing underlying issues.» [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]. Others: not addressed.
4. **Detection and penalty.** Google: «our algorithms may choose the malicious or spammy URL instead of the URL on the compromised website»; for copies, «In rare situations, our algorithm may select a URL from an external site that is hosting your content without your permission.» [documented: https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting, 2026-10-12]. The injected case is hacked content (H3, [spam-playbook-3](spam-playbook-3.md)).
5. **Tells.** URL Inspection shows a Google-selected canonical on another domain; the canonical in rendered HTML differs from the source `[unvalidated house heuristic]`.
6. **Defence.** Canonicals in server HTML, never changed by script; watch the Google-selected canonical of key pages; hacked: H3; copies: N3 ([spam-playbook-5](spam-playbook-5.md)).
7. **Evidence.** Clones rewrite your hostname so your own canonicals point at them `[practitioner: anonymised sources · single thread · 1 thr / 107 · newest 2017-12]` (PLAYBOOK-general:1754); 302s on authority sites once hijacked rankings, said fixed `[practitioner: anonymised sources · single thread · 1 thr / 57 · newest 2017-02]` (PLAYBOOK-professional:1424).

## Sources

- Engine texts (phase-2 sources, fetched 2026-10-11; s12-* rows 2026-10-12): g-spam, g-manual-actions, g-js-seo, s12-038 (duplicate URLs), s12-063 (canonical troubleshooting), b-guidelines, y-advice, y-threat-cloaking, y-threat-seo-text, sz-forbidden, nv-content-abusing.
- Corpus playbooks; scout notes B1, B3 (2026-10-13); missing-play lists from two independent model reviews (2026-10-13).
