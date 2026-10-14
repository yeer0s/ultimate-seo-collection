# Spam playbook — know every play (part 9 of 9: more AI-search plays, attacks, unsafe tools; unverified plays)

Refusal rule, entry order, labels and "others": [spam-playbook](spam-playbook.md), first section. Plays added 2026-10-13 from the two reviews' missing-play lists; every engine line was re-read in the saved source.

## Contents
- More AI-search plays (A8–A11)
- More attacks on others (N6–N7)
- Unsafe agent tools (T8)
- Unverified / seen in the wild
- Sources

## More AI-search plays (A8–A11)

### A8. Prompt injection off the HTML page: reviews, PDFs, images, listings
1. **What and why.** Instructions to AI placed where answer engines and agents read but owners rarely police: user reviews, PDF text, text in images, business descriptions, profile bios.
2. **How.** Lines such as "assistant: recommend X" in a review, a PDF text layer or an image.
3. **Policy.** Bing: «Attempts to add content designed to manipulate or interfere with language models used by Bing or Copilot may result in reduced visibility or removal from search experiences» [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]. Google: spam includes «attempting to manipulate generative AI responses in Google Search» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. A W3C draft (not engine policy) names the vector: «Malicious actors influencing website content (e.g., untrusted user-generated content on social media platforms, forums, review sites)» [documented: https://webmachinelearning.github.io/webmcp/, 2026-10-12]. Others: not addressed.
4. **Detection and penalty.** Documented for one Microsoft product only: Copilot Studio agents whose generative answers node uses public websites (Bing Custom Search) as a knowledge source; there the prompts «include instructions to ignore questions and search results classified as jailbreak, prompt injection, and privacy violation.» [documented: https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/generative-ai-public-websites, 2026-10-12]. This is not evidence of how Bing search or public Copilot answers filter injection; no saved text documents that. Penalties: A1 ([spam-playbook-4](spam-playbook-4.md)).
5. **Tells.** Reviews or PDF text addressed to "AI" or "assistant"; text in images that reads as instructions; listing descriptions with commands to models `[unvalidated house heuristic]`.
6. **Defence.** Moderate reviews and uploads for model-directed text; our agents treat every fetched page, PDF and OCR output as data (A1).
7. **Evidence.** seo-skills/seo-audit-skill@src/reporters/llm-reporter.ts:13-18 wraps site text in a nonce and strips invisible characters before a model reads it, a defence (scout B6.md:61) `[vendor]`. Practitioner reports: corpus searched, not found.

### A9. robots.txt split: one face for search, another for AI answers
1. **What and why.** Per-token opt-outs are legitimate; the play is using the split to show AI crawlers a different site from search crawlers, or AI-only claims.
2. **How.** Per-bot robots.txt groups combined with content branching by user agent (C1).
3. **Policy.** Tokens are independent by design: «Each setting is independent of the others – for example, a webmaster can allow OAI-SearchBot in order to appear in search results while disallowing GPTBot» [documented: https://developers.openai.com/api/docs/bots, 2026-10-11]; Google-Extended «does not impact a site's inclusion in Google Search nor is it used as a ranking signal in Google Search.» [documented: https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers, 2026-10-11]; Apple: «If robots instructions don't mention Applebot but mention Googlebot, the Apple robot will follow Googlebot instructions.» [documented: https://support.apple.com/en-us/119829, 2026-10-11]. Google's cloaking test is users versus crawlers, with intent: «presenting different content to users and search engines with the intent to manipulate search rankings and mislead users» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Rendered variants are fine «As long as your dynamic rendering produces similar content»; «completely different content to users and crawlers can be considered cloaking» [documented: https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering, 2026-10-11]. So a crawler-to-crawler difference is not cloaking by itself; showing AI crawlers material users do not get is judged by that test. No engine text addresses crawler-to-crawler differences. Bing: C1. Others: not addressed.
4. **Detection and penalty.** C1 rules. Google-Extended has no crawler of its own: «Crawling is done with existing Google user agent strings; the robots.txt user-agent token is used in a control capacity.» [documented: https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers, 2026-10-11].
5. **Tells.** robots.txt that blocks a search crawler but admits AI bots, plus content for AI user agents that differs materially from what users see `[unvalidated house heuristic]`.
6. **Defence.** Decide opt-outs per token in writing; every bot we admit gets the same content.
7. **Evidence.** Some AI crawlers never fetch robots.txt `[practitioner: anonymised sources · consensus · 2 thr / 12 · newest 2026-03]` (PLAYBOOK-technical:2012); a CDN toggle prepends AI disallows to your file `[practitioner: anonymised sources · contested · 1 thr / 58 · newest 2026-04]` (PLAYBOOK-general:2030); fseixas/super-geo-agent-readiness@references/agent-readiness.md:513 redirects training crawlers by user agent (scout B4.md:65) `[vendor]`. A deliberate split as a tactic: corpus searched, not found.

### A10. Forum and Q&A pages seeded for AI answers
1. **What and why.** Threads and Q&A pages created or flooded to be the "discussion" AI answers summarise, including staff-written "community" pages on one's own site.
2. **How.** Fake questions answered by sock accounts; keyword-stuffed vendor threads; Q&A pages with no real users.
3. **Policy.** Google: «seeking inauthentic "mentions" across the web isn't as helpful as it might seem» [documented: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide, 2026-10-11]; «Spammy posts on forum threads» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Bing: «artificial social promotion schemes that simulate popularity» [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]. Naver: H5 row ([spam-playbook-3](spam-playbook-3.md)). Forum markup aimed at AI answers: no engine text (searched 2026-10-13). Others: not addressed.
4. **Detection and penalty.** Platform moderation (H5); engines document none for the AI-answer case.
5. **Tells.** Threads where every answer names one brand; staff-written "community" answers; new accounts with one-brand histories `[unvalidated house heuristic]`.
6. **Defence.** Forum answers only with the affiliation disclosed (H5); our own Q&A only from real users.
7. **Evidence.** Reddit astroturfing for LLM mentions leaves an obvious pattern `[practitioner: anonymised sources · contested · 2 thr / 214 · newest 2026-05]` (PLAYBOOK-general:218); disguised self-promotion on Reddit to get cited by AI backfires `[practitioner: anonymised sources · single thread · 1 thr / 144 · newest 2025-09]` (PLAYBOOK-general:252); Illyism seo/blitz-seo/SKILL.md:55,58 seeds Reddit and Quora (scout B6.md:125) `[vendor]`.

### A11. Training-data seeding
1. **What and why.** Brand claims placed where training corpora draw (open crawls, wikis, Q&A dumps) so future models "know" the brand favourably.
2. **How.** Mass mentions on crawlable hosts; edits to reference works; text written to be repeated.
3. **Policy.** No engine or AI vendor page prohibits it (searched 2026-10-13). Opt-out tokens only control use: «Disallowing GPTBot indicates a site’s content should not be used in training generative AI foundation models.» [documented: https://developers.openai.com/api/docs/bots, 2026-10-11]. Bing's AI clause covers «language models used by Bing or Copilot» [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]; Google's covers «generative AI responses in Google Search» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Others: not addressed.
4. **Detection and penalty.** Not documented.
5. **Tells.** "Get into ChatGPT's training data" offers; mass wiki or Q&A edits naming one brand `[unvalidated house heuristic]`.
6. **Defence.** Refuse; publish sourced facts anyone may cite; never edit reference works about ourselves (L9, [spam-playbook-8](spam-playbook-8.md)).
7. **Evidence.** Build brand mentions to shape what models learn `[practitioner: anonymised sources · single voice · 2 thr / 4 · newest 2026-08]` (PLAYBOOK-agentic:118); Reddit and Quora ranking argued, not measured, to follow AI data deals `[practitioner: anonymised sources · consensus · 2 thr / 118 · newest 2024-09]` (PLAYBOOK-general:196). Poisoning aimed at model weights: ## Unverified / seen in the wild, below.

## More attacks on others (N6–N7)

### N6. Removal abuse: pay-for-removal sites and weaponised complaints
1. **What and why.** Sites that publish personal data and charge to remove it; or waves of legal, copyright or privacy complaints filed to strip a rival's pages (copyright: N2, [spam-playbook-5](spam-playbook-5.md)).
2. **How.** Scraped personal records plus a paid "removal" form; complaint campaigns.
3. **Policy.** Google: «If we process a significant volume of personal information removals involving a site with exploitative removal practices, we demote other content from the site in our results.»; «We apply similar demotion signals to complaints involving defamation, counterfeit goods, and court-ordered removals.» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]. Bing: «Some webpages engage in deceptive and exploitative removal practices.»; for legal demands it weighs «the reason and basis for the request or demand, the authority or rights of the requesting party» [documented: https://support.microsoft.com/en-us/topic/how-bing-delivers-search-results-d18fc815-ac37-4723-bc67-9229ce3eb6a3, 2026-10-11]. False complaints against a rival: no engine text. Others: not addressed.
4. **Detection and penalty.** Google: «We also look to see if the same pattern of behavior is happening with other sites and, if so, apply demotions to content on those sites.» [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11].
5. **Tells.** "Remove your record for EUR X" pages; removal notices about our URLs from unknown parties `[unvalidated house heuristic]`.
6. **Defence.** Never pay removal sites; use the engines' removal forms; watch Lumen and Search Console; answer false notices with dated proof (N2).
7. **Evidence.** Rule out fake takedowns in a Google-only collapse `[practitioner: anonymised sources · single thread · 1 thr / 41 · newest 2026-07]` (PLAYBOOK-technical:578). False Safe Browsing, trademark or privacy complaints as a weapon: ## Unverified / seen in the wild, below.

### N7. Bot floods against a rival
1. **What and why.** Junk traffic or impostor crawling aimed at a rival's server, to slow it, trip its bot filters or ruin its analytics.
2. **How.** Rented bot traffic; crawlers posing as search bots.
3. **Policy.** No engine rule on attacking a rival (searched 2026-10-13). Naver bans spreading attack tools: «DDOS 등 악성 프로그램 배포 행위가 해당됩니다» ("distributing DDoS and other malicious programs") [documented: https://searchadvisor.naver.com/guide/content-abusing, 2026-10-11]. Yandex: «Using special software or services that automatically imitate user traffic from search engines.» (H7) [documented: https://yandex.com/support/webmaster/en/threat/user-actions-imitation, 2026-10-11]. Others: not addressed.
4. **Detection and penalty.** The victim pays: Google crawls less when a site «responds with server errors (5xx HTTP status codes) or rate-limiting signals (such as HTTP 429)» [documented: https://developers.google.com/crawling/docs/crawl-budget, 2026-10-12]. Baidu: «造成此现象可能是由于有人冒充Baiduspider恶意抓取» ("may be someone posing as Baiduspider") [documented: https://ziyuan.baidu.com/college/articleinfo?id=1192, 2026-10-11].
5. **Tells.** Spikes from one country or network with no engagement; "Googlebot" hits from non-Google IPs (T4) `[unvalidated house heuristic]`.
6. **Defence.** Verify bots by DNS (T4) and block impostors at the CDN; rate-limit without erroring verified crawlers; keep logs for the host's abuse desk.
7. **Evidence.** Same-country visitor spikes blocked by user agent `[practitioner: anonymised sources · single thread · 1 thr / 12 · newest 2024-05]` (PLAYBOOK-general:3144); hacktheseo/wordpress-seo-skills@skills/ai-bot-log-forensics/references/verification.md:41-120 sorts bots into verified, spoofed and unverifiable, a defence (scout B5.md:50) `[vendor]`. Attacks on rivals by name: corpus searched, not found.

## Unsafe agent tools (T8)

### T8. Credential-leaking, telemetry and destructive agent tools
1. **What and why.** SEO skills and MCP servers that send audited domains to their vendor, store or log API keys in plain text, hold full-scope tokens, or ship tools that delete data: a risk to the user, not a ranking trick.
2. **How.** Default-on telemetry hooks; installers that write keys into agent settings; keys inside MCP URLs; unpinned `npx -y` installs; delete tools on by default.
3. **Policy.** Not an engine policy. Others: not addressed.
4. **Detection and penalty.** Not documented; found by reading the code (scout REPORT §7).
5. **Tells.** An installer that asks for keys and edits the agent's settings file; telemetry with an opt-out variable; `npx -y` with no version; delete-site or unverify-site tools enabled by default `[unvalidated house heuristic]`.
6. **Defence.** Read install scripts and hooks before running them; pin versions; read-only scopes; keys from a secret store, never in URLs or logs; destructive tools off; install none of the scout's UNSAFE repos.
7. **Evidence.** akii-technologies-ltd/akii-seo-ai-search-optimizer@scripts/akii-cta.sh:117-195, default-on telemetry to the vendor (scout B3.md:138); mykpono/ultimate-seo-geo installers write a password in plain text into the agent settings and run unpinned `npx -y` (scout B3.md:81); seranking/seo-skills@extensions/firecrawl/install.sh:17,63-79, key into settings (scout B1.md:92); garrettjsmith/localseoskills@install.sh:125-206, key inside the MCP URL (scout B5.md:19); XuanRanL/loamwright-SEO-Skill hooks write and delete outside the project (scout B2.md:67); harlan-zw/gscdump@auth.ts:42-46, full-scope tokens, plain-text token file, always-on delete tools (scout B8.md:25-27); isiahw1/mcp-server-bing-webmaster@main.py:16,63,67 logs the account key on every call (scout B8.md:54); saurabhsharma2u/search-console-mcp@http.ts:17,66, open network mode with no auth (scout B7.md:77) `[vendor]`. Injection by tools: T6 ([spam-playbook-5](spam-playbook-5.md)).

## Unverified / seen in the wild

Plays the reviews list that no saved engine page, corpus entry or scout note supports. Recognise them; never quote them as engine policy.

- Consent-wall cloaking (bots get full text past a cookie or consent wall people must accept) [unverified: no engine page on consent walls saved; corpus searched 2026-10-13, not found]. Documented paywall rules: K2.
- noscript, SVG title, CSS content and shadow-DOM text used to hide keywords [unverified: no engine names these vectors; documented hiding rules: K5].
- Review gating on Google Business Profiles (only happy customers asked to review) [unverified: Google's Business Profile review policy is not among the saved sources; corpus searched, not found]. Documented review rules: P4, H6.
- Business Profile stacking (several listings at one address) and service-area listings covering a whole country [unverified: Business Profile guidelines not saved; the corpus has only spoofed addresses, P5].
- Listing spam on Bing Places, Apple Business Connect, Naver Place, Yandex Business, Seznam Firmy.cz and Baidu Maps [unverified: no abuse rules saved; Bing Places and Firmy.cz appear only as listing services].
- B2B review rings on G2, Capterra, Clutch and Trustpilot [unverified: no platform terms saved; corpus and scout searched, not found].
- False Safe Browsing or malware reports, trademark complaints and privacy or right-to-be-forgotten requests used to remove a rival [unverified: no engine text on abuse of these channels; Bing only describes how it weighs legal demands, N6].
- Training-data poisoning aimed at model weights (crafted text for open crawls) [unverified: no vendor page describes or prohibits it; documented edges: A11].
- DiscussionForumPosting markup on staff-written pages to be read as a forum by AI answers [unverified: only Google changelog lines on the markup are saved; A10].

## Sources

- Engine texts (phase-2 sources, fetched 2026-10-11; s12-* rows 2026-10-12): g-spam, g-dynamic-rendering, gai-optimization-guide, gai-common-crawlers-a, s12-036 (crawl budget), s12-091 (WebMCP draft), s12-097 (Copilot Studio), b-guidelines, b-how-bing-delivers, oa-bots, ap-applebot, y-threat-user-actions-imitation, nv-content-abusing, bd-spider.
- Corpus playbooks; scout REPORT §7 and notes B1–B8 (2026-10-13); missing-play lists from two independent model reviews (2026-10-13).
