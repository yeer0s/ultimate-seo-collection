# Spam playbook — know every play (part 5 of 9: attacks, tools, vendors)

Refusal rule, entry order, labels and "others": [spam-playbook](spam-playbook.md), first section. Tool and vendor plays are mostly outside engine policy; line 3 says so instead of inventing a rule.

## Contents
- Negative SEO: attacks on others (N1–N5)
- Tooling and terms-of-service abuse (T1–T7)
- Agency and vendor red flags (V1–V5)
- Unverified
- Sources

## Negative SEO: attacks on others (N1–N5)

### N1. Toxic-link attacks and link extortion
1. **What and why.** Point junk links or spam anchors at a rival to trigger a link penalty; or email threats ("pay or we spam you").
2. **How.** Bulk links from spam domains, casino or crypto anchors; sellers who spam a site and then sell "removal".
3. **Policy.** No engine has a negative-SEO rule, but Google speaks to it: «Google works very hard to make sure that actions on third-party sites do not negatively affect a website»; «In most cases, Google can assess which links to trust without additional guidance, so most sites will not need to use this tool.» [documented: https://support.google.com/webmasters/answer/2648487, 2026-10-11]. Baidu withdrew its disavow tool: «外链拒绝功能下线» [documented: https://ziyuan.baidu.com/wiki/7, 2026-10-11]. Bing, Yandex, Seznam, Naver, others: not addressed.
4. **Detection and penalty.** None documented for victims; a manual action, if one comes, is handled as in L1–L8 ([spam-playbook](spam-playbook.md)).
5. **Tells.** Referring domains jump in weeks, mostly new TLD spam; anchors unrelated to your business; an email demanding money or a link `[unvalidated house heuristic]`.
6. **Defence.** Log the spike with exports and dates; never pay; disavow only when both of Google's conditions hold: «You have a considerable number of spammy, artificial, or low-quality links pointing to your site» AND «The links have caused a manual action, or likely will cause a manual action, on your site.» [documented: https://support.google.com/webmasters/answer/2648487, 2026-10-11]. A clear pattern alone is not enough; a likely action is (skill `seo-authority` › authority-links-and-pr).
7. **Evidence.** Blackmail emails with no follow-through seen `[practitioner: anonymised sources · single thread · 1 thr / 167 · newest 2022-01]` (PLAYBOOK-general:5940); if spammy inbound links hurt is a two-sided debate (ignore vs audit-and-disavow), one commenter calling an attack very damaging `[practitioner: anonymised sources · consensus · 3 thr / 54 · newest 2026-03]` (PLAYBOOK-general:5872); spam-domain spikes as an ad for a link seller `[practitioner: anonymised sources · single thread · 1 thr / 81 · newest 2025-06]` (PLAYBOOK-general:5992).

### N2. Fake copyright takedowns and legal complaints
1. **What and why.** File false copyright notices against a rival's URLs to remove or demote them.
2. **How.** Notices claim the rival copied the attacker's (often backdated) copy.
3. **Policy.** Google acts on valid notices and demotes sites with a «significant volume of valid copyright removal requests» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. False notices: not addressed by any engine page. Others: not addressed.
4. **Detection and penalty.** Not documented.
5. **Tells.** Rankings collapse on Google only for specific URLs; a notice about your URL in the Lumen database `[practitioner: anonymised sources · single thread · 1 thr / 41 · newest 2026-07]` (PLAYBOOK-technical:578).
6. **Defence.** Monitor Lumen for your domain; file a counter-notice with proof of first publication; keep dated originals `[unvalidated house heuristic]`.
7. **Evidence.** A mistaken self-filed removal dropped the owner's homepage irreversibly `[practitioner: anonymised sources · single thread · 1 thr / 111 · newest 2021-10]` (PLAYBOOK-general:6034).

### N3. Scraper clones and framing copycats (victim side of C6)
1. **What and why.** Copy your whole site to outrank you or to harvest your traffic.
2. **How.** Proxies rewrite your hostname to theirs, or frame your pages with added text.
3. **Policy.** Scraping rows in C6 ([spam-playbook-2](spam-playbook-2.md)); Bing adds that copying «offers little benefit to users and may violate copyright expectations» [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11].
4. **Detection and penalty.** C6 rules apply to the copier.
5. **Tells.** Your text, images and even internal links on another domain; your analytics showing a foreign hostname `[unvalidated house heuristic]`.
6. **Defence.** Self-referencing canonicals and absolute links; block the proxy at the CDN; notices to host and registrar; copyright removal request; spam report.
7. **Evidence.** Clones that rewrite the hostname, stopped at the CDN `[practitioner: anonymised sources · single thread · 1 thr / 107 · newest 2017-12]` (PLAYBOOK-general:1754); a cloned client site handled through hosting, registrar and Safe Browsing reports `[practitioner: anonymised sources · single thread · 1 thr / 316 · newest 2024-04]` (PLAYBOOK-general:6090).

### N4. Access sabotage: malicious disavow, former agencies, "let me fix your robots.txt"
1. **What and why.** Someone with Search Console or CMS access uploads a disavow of good links, blocks pages, or plants links.
2. **How.** Old agency accounts never removed; a cold "free fix" offer that asks for access.
3. **Policy.** Not an engine policy; Google's disavow file applies per property ([google](google.md) §7). Others: not addressed.
4. **Detection and penalty.** Not documented as an attack; Google warns the tool «can potentially harm your site’s performance in Google Search results» if misused [documented: https://support.google.com/webmasters/answer/2648487, 2026-10-11].
5. **Tells.** Unknown users in Search Console; a disavow file you did not write; robots.txt changes nobody made `[unvalidated house heuristic]`.
6. **Defence.** Quarterly access review; remove ex-vendors; read the disavow file before any link work; never give access to cold contacts.
7. **Evidence.** If someone uploads a disavow of your good domains, delete it at once: a score-68 post (2025-09; seo-evidence › practitioner-general:65), top of the cluster `[practitioner: anonymised sources · consensus · 14 thr / 347 · newest 2026-05]` (PLAYBOOK-general:5816); former agencies can deindex or disallow pages `[practitioner: anonymised sources · single thread · 1 thr / 5 · newest 2018-05]` (PLAYBOOK-professional:3728); cold robots.txt help as a route to blackmail or malware `[practitioner: anonymised sources · single thread · 1 thr / 28 · newest 2025-03]` (PLAYBOOK-general:6150).

### N5. Attacks on listings and reviews
1. **What and why.** Fake negative reviews, fake rival listings, or edits that move a rival's pin or mark it closed.
2. **How.** Account farms and public edit suggestions.
3. **Policy.** Yandex: fake reviews (H6, [spam-playbook-3](spam-playbook-3.md)). Google listing rules: not in saved sources (P1, [spam-playbook-4](spam-playbook-4.md)). Others: not addressed.
4. **Detection and penalty.** Not documented. 5. **Tells.** Review bursts from new profiles; pin or hours changed without your edit `[unvalidated house heuristic]`.
6. **Defence.** Watch the profile weekly; report with screenshots; reply factually to reviews.
7. **Evidence.** Fraudulent listings reported through the redress form during attacks `[practitioner: anonymised sources · consensus · 3 thr / 48 · newest 2021-03]` (PLAYBOOK-professional:3682).

## Tooling and terms-of-service abuse (T1–T7)

### T1. CAPTCHA bypass in SEO tools
1. **What and why.** "Free Ahrefs-grade data": a tool solves a vendor's CAPTCHA to call endpoints meant for people.
2. **How.** Paid CAPTCHA-solving services and spoofed referers.
3. **Policy.** Not a search-engine policy. For Google's own pages: automated access without permission violates «our spam policies and the Google Terms of Service» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Credential and destructive risks of such tools: T8 ([spam-playbook-9](spam-playbook-9.md)). Vendor terms: the scout read Ahrefs Terms §4.4 as breached (scout reading, not legal advice). Others: not addressed.
4. **Detection and penalty.** Vendor blocks and legal exposure; not documented by engines.
5. **Tells.** A tool asking for a CAPTCHA-solver key; "no Ahrefs seat needed" `[unvalidated house heuristic]`.
6. **Defence.** Do not install; Mowei uses licensed APIs only.
7. **Evidence.** egebese/dataseo-mcp src/seo_mcp/captcha.py:15,73-141 (scout B8.md:60-61); akii-technologies-ltd/akii-seo-ai-search-optimizer skills/ai-visibility/SKILL.md:102,379 (scout B3.md:140) `[vendor]`.

### T2. Anti-bot evasion against third-party sites
1. **What and why.** Crawl competitors or review sites that block bots. 2. **How.** Fingerprint-randomising browsers, rotating residential IPs, proxy chains.
3. **Policy.** Not a search-engine policy; site owners' terms apply. Others: not addressed.
4. **Detection and penalty.** Not documented. 5. **Tells.** "Bypass all Cloudflare layers" claims; stealth fetchers as the default `[unvalidated house heuristic]`.
6. **Defence.** Crawl only our own sites or with permission; respect blocks.
7. **Evidence.** XuanRanL/loamwright-SEO-Skill@references/init/cloudflare-handling.md:183-233 (scout B2.md:67,75); popiliadam/platinum-seo-engine skills/discovery/competitive-analysis/SKILL.md:183-190 (scout B3.md:93); iklynow-hue/seo-geo-skills@references/architecture.md:31,39 (scout B3.md:122); noique tools/trustpilot/chain_proxy.py:11-31 (scout B2.md:105) `[vendor]`.

### T3. Google SERP scraping, direct or bought
1. **What and why.** Rank tracking and AI-answer tracking from scraped result pages. 2. **How.** Own scrapers, or resellers' SERP APIs.
3. **Policy.** Google: «scraping results for rank-checking purposes or other types of automated access to Google Search conducted without express permission» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Naver: «네이버 정보 무단 추출 프로그램의 배포·홍보» ("distributing unauthorised Naver extraction programs") [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11]. Others: not addressed.
4. **Detection and penalty.** Not documented beyond the terms.
5. **Tells.** SERP-API keys in a tool's setup; "SERP scraping without getting blocked" `[unvalidated house heuristic]`.
6. **Defence.** Own data first (Search Console API); buying SERP data is a terms risk for the site owner to accept or refuse `[unvalidated house heuristic]`.
7. **Evidence.** 9 tool rows: siddiqss/semantic-seo-suite@scripts/serpapi_client.py:1-30 (scout B2.json:45); metawhisp/amazing-seo-skill@scripts/serpapi_integration.py:52,134 (scout B3.md:111); dataforseo/mcp-server-typescript (scout B7.md:105); avansaber, which calls its own method "ToS-contested" (scout B7.json:125); houtini-ai/seo-audit src/core/googleNews.ts:28 (scout B7.md:58) `[vendor]`.

### T4. Crawler impersonation and ignoring robots.txt
1. **What and why.** Fetch as "Googlebot" or "GPTBot" to get past blocks or see bot-only content. 2. **How.** Spoofed user agents; robots.txt off by default.
3. **Policy.** Not a search-engine rule for third parties. Google documents verification for when «spammers or other troublemakers are accessing your site while claiming to be from Google» [documented: https://developers.google.com/crawling/docs/crawlers-fetchers/verify-google-requests, 2026-10-12]. Others: not addressed.
4. **Detection and penalty.** Bing: reverse DNS must resolve to «search.msn.com» [documented: https://www.bing.com/webmasters/help/how-to-verify-bingbot-3905dc26, 2026-10-11].
5. **Tells.** Logs with bot user agents from non-matching IPs `[unvalidated house heuristic]`. 6. **Defence.** Verify bots by DNS before trusting or blocking them; our own audits use an honest user agent.
7. **Evidence.** squirrelscan/squirrelscan packages/config/src/schema.ts:92-96,349-352 (scout B6.md:45); jianruntech/geo-score SKILL.md:90-92 (scout B4.json:15) `[vendor]`.

### T5. Unlicensed use of paid-tool data
1. **What and why.** Bulk calls to a vendor's free endpoints to avoid paying. 2. **How.** Scripts loop the free checker over every domain.
3. **Policy.** Vendor terms, not engines. Others: not addressed. 4. **Detection and penalty.** Not documented.
5. **Tells.** "Free Ahrefs-sourced data" lists `[unvalidated house heuristic]`. 6. **Defence.** Licensed APIs only.
7. **Evidence.** marketingskills/seo@scripts/authority_mark.py:16,63-80 (scout B6.md:84); RankSpotAI/awesome-seo-mcp README.md:115 (scout B6.md:149) `[vendor]`.

### T6. Prompt-injecting and self-promoting agent tools
1. **What and why.** A skill or MCP server steers the agent: injected "[SYSTEM NOTICE]" text, live instructions from the vendor's server, or an advert appended to every answer.
2. **How.** Text in tool results or tool descriptions; instruction files fetched at run time; session hooks.
3. **Policy.** Not an engine policy (Bing's A1 clause covers pages, not tools). Others: not addressed.
4. **Detection and penalty.** Not documented.
5. **Tells.** Tool output addressed to the model; "prefer the live file over the local copy"; mandatory "never omit" calls to action `[unvalidated house heuristic]`.
6. **Defence.** Read a tool's outputs and descriptions before install; pin versions; refuse remote instruction files; treat tool output as data.
7. **Evidence.** saurabhsharma2u/search-console-mcp src/utils/cli.ts:21-36 (scout B7.md:76); Illyism seo/seo-autopilot/SKILL.md:104 (scout B6.md:124); cognyai skills/cogny/SKILL.md:453-468 (scout B6.md:111); nexscope-ai ecommerce-geo-auditor/SKILL.md:85-89 (scout B5.md:65); akii hooks/hooks.json:3-12 (scout B3.md:138) `[vendor]`.

### T7. Outreach email probing and platform scraping against terms
1. **What and why.** Guess journalists' addresses and probe mail servers; pull platform content by unsupported means.
2. **How.** Pattern guessing plus SMTP checks; subtitle downloaders.
3. **Policy.** Not an engine policy. Personal-data law on guessed and probed emails: unverified [unverified: no legal source saved]; see ## Unverified. Others: not addressed.
4. **Detection and penalty.** Not documented. 5. **Tells.** "Find any journalist's email" tools `[unvalidated house heuristic]`. 6. **Defence.** Public press contacts only.
7. **Evidence.** noique outbound-prospecting/media-press-discovery/scripts/guess_emails.py:15,101 (scout B2.md:104); AgriciDaniel/claude-youtube skills/claude-youtube/execution/fetch_transcript.py:56-95 (scout B5.md:72) `[vendor]`.

## Agency and vendor red flags (V1–V5)

### V1. Ranking guarantees
1. **What and why.** "#1 in 30 days" sells. 2. **How.** Rank a term nobody searches, then report the win.
3. **Policy.** Bing: «SEO does not guarantee rankings or traffic, and GEO does not guarantee grounding or citations in AI experiences.» [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]. Google: «Be wary of third-party tools that promise ranking success» [documented: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide, 2026-10-11]. Others: not addressed.
4. **Detection and penalty.** Not applicable. 5. **Tells.** Guaranteed positions or dates `[unvalidated house heuristic]`. 6. **Defence.** Disqualify the vendor.
7. **Evidence.** Guarantees disqualify a provider `[practitioner: anonymised sources · consensus · 8 thr / 771 · newest 2025-08]` (seo-evidence practitioner-general); Illyism seo/blitz-seo/SKILL.md:71,85 "page-one movement around day 14-20" (scout B6.json:80) `[vendor]`.

### V2. Toxic-link scores and the disavow upsell
1. **What and why.** A tool's "toxic %" sells monthly disavow work. 2. **How.** Score every linking domain; disavow the "toxic" ones.
3. **Policy.** Google: most sites do not need disavow (N1 quote); «Blindly adding all backlinks to the disavow file is not considered a good-faith effort» [documented: https://support.google.com/webmasters/answer/9044175, 2026-10-11]. Others: not addressed.
4. **Detection and penalty.** Misuse is self-harm: the tool «can potentially harm your site’s performance in Google Search results» [documented: https://support.google.com/webmasters/answer/2648487, 2026-10-11]; practitioners agree (line 7). 5. **Tells.** Disavow with no actual or likely manual action `[unvalidated house heuristic]`.
6. **Defence.** Disavow only on Google's two conditions (N1): many bad links and an actual or likely manual action.
7. **Evidence.** Do not disavow by a tool's toxic score `[practitioner: anonymised sources · consensus · 27 thr / 778 · newest 2026-06]` (PLAYBOOK-general:5804); a disavow that likely backfired `[practitioner: anonymised sources · consensus · 14 thr / 347 · newest 2026-05]` (PLAYBOOK-general:5816); metawhisp/amazing-seo-skill@scripts/backlinks_toxicity.py (scout B3.md:112) `[vendor]`.

### V3. Uplift claims without control, invented scores, simulated AI visibility
1. **What and why.** Big before/after numbers and 0–100 scores sell audits. 2. **How.** One customer's lift, no control; a model answering prompts itself recorded as an engine run.
3. **Policy.** Google: «No third-party tool has access to our internal ranking or AI systems.» [documented: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide, 2026-10-11]. Others: not addressed.
4. **Detection and penalty.** Not applicable. 5. **Tells.** "+271% in 3 weeks"; scores with no method `[unvalidated house heuristic]`.
6. **Defence.** Read claims through skill `seo-evidence` (denominators, controls).
7. **Evidence.** cognyai/claude-code-marketing-skills README.md:178-195 (scout B6.json:262); petar-nauka/ai-visibility-skill SKILL.md:80-92 (scout B4.md:90); made-up scores in about 30 repos (scout REPORT §8) `[vendor]`.

### V4. Invented algorithm updates
1. **What and why.** Blame a drop on an "update" that never happened. 2. **How.** A placeholder update in a tool's list.
3. **Policy.** Not a site policy; dated updates: skill `seo-engine-policies` › google-updates-timeline. Others: not addressed.
4. **Detection and penalty.** Not applicable. 5. **Tells.** An update missing from the engine's status page `[unvalidated house heuristic]`. 6. **Defence.** Match drops to dated, documented updates only.
7. **Evidence.** saurabhsharma2u src/bing/tools/advanced-analytics.ts:40 "Projected AI Relevance Update" (scout B7.md:84) `[vendor]`.

### V5. Padded reports, bot traffic, dark patterns
1. **What and why.** Activity sold as results; pressure UX sold as conversion. 2. **How.** Submission counts, bot visits, urgency and scarcity cues.
3. **Policy.** Bot visits: H7. Others: not addressed. 4. **Detection and penalty.** H7.
5. **Tells.** Reports counting tasks; traffic that ends with the contract `[unvalidated house heuristic]`. 6. **Defence.** Pay on outcomes in GSC; no fake urgency on a regulated comparison site.
7. **Evidence.** Report padding `[practitioner: anonymised sources · contested · 1 thr / 7 · newest 2026-07]` (PLAYBOOK-technical:4370); bot traffic `[practitioner: anonymised sources · single thread · 1 thr / 9 · newest 2025-05]` (PLAYBOOK-professional:2250); cognyai skills/landing-page-review/SKILL.md:66 (scout B6.md:110) `[vendor]`.

## Unverified

- Ahrefs Terms §4.4 breach by CAPTCHA-solving tools [unverified: the terms were read by the scout's B8 agent; the terms text is not among the saved phase-2 sources].
- Personal-data law on guessed and probed emails [unverified: no legal source saved; a question for counsel].

## Sources

- Engine texts (phase-2 sources, fetched 2026-10-11; s12-* rows 2026-10-12): g-spam, g-disavow, g-manual-actions, s12-102 (verify Google requests), gai-optimization-guide, b-guidelines, b-verify-bingbot, nv-content-abusing, bd-wiki7.
- Scout notes B2–B8 and REPORT §8 (2026-10-13); corpus playbooks.
