<!-- split-header: part 6 of 8 of practitioner-playbook.md (step-3 original lines 313–410; boundary H2) -->
# Practitioner layer — general practitioners
## Contents

- General practitioners — primary corpus layer

Other parts of the same original file: [practitioner-index.md](practitioner-index.md), [practitioner-technical-1.md](practitioner-technical-1.md), [practitioner-technical-2.md](practitioner-technical-2.md), [practitioner-agentic.md](practitioner-agentic.md), [practitioner-professional.md](practitioner-professional.md), [practitioner-secondary-digest-1.md](practitioner-secondary-digest-1.md), [practitioner-secondary-digest-2.md](practitioner-secondary-digest-2.md).

<!-- /split-header -->
## General practitioners — primary corpus layer

**The evidence tier.** A collected corpus of public practitioner discussions (anonymised sources), complete for this community: 448,424 threads and 1,346,395 comments, dated 2008-04-22 to 2026-10-01, collected credential-free. Real gaps: 45 posts short of the platform's own comment count (71 comments), 590 orphan comments. The 3,930 highest-signal threads were read in 600 half-size chunks by **two extractors**: Grok `grok-4.6` (342 chunks, 7,103 claims, ~21 per chunk) and Claude Opus 5.5 at medium effort (258 chunks, 3,317 claims, ~13 per chunk). One Grok chunk (053) cited none of its threads and was re-mapped by Claude, its every id checked against the chunk. 10,420 claims in, all usable; 6 citations dropped (4 real comments cited under the wrong thread, 2 fabricated comment ids) and 78 scores overwritten with corpus values. Thread coverage averages 0.93 (worst 0.57, skips declared), with no link to chunk size (gap +0.00). 6,197 distinct practices after merging.

**The label grammar** is the professional layer's (consensus = ≥2 threads by ≥2 distinct authors and ≥10 summed score). The extraction models called 2,563 practices `consensus`; the evidence supports **515 of 6,197**. The grounding pass flagged 39 (34 for a headline term no cited body contains, 5 for low overlap alone), and all 39 were read against their full cited bodies: 33 supported, 4 partial, 2 unsupported. 18 of the 34 term flags were the matcher reading "deindex" as `noindex`, or GWMT / "google console" as a missing "Search Console" — read, and none was invented. The 2 unsupported (a "Semrush courses for staff" line whose cited comment says nothing of the kind, and a Search Console thresholding line whose only cited comment is blank in the corpus) are omitted. Verdicts: `exports/general/review_verdicts.json`.

**Three reading rules this layer adds.** (1) **Two producers, unequal verbosity.** Grok wrote ~21 claims per chunk and Claude ~13, so a cluster's size partly measures which model read its threads. **340 of the 515 `consensus` practices rest on one producer's items only** (257 Grok-only, 83 Claude-only), almost all of them 2–3-thread clusters. Every line below carries its item split as `G/C`; a one-producer line is weaker and says so. (2) **The 22 biggest clusters are topics, not practices.** With thousands of generically titled threads (best-tool questions, how-do-I-rank questions), the reducer merged whole conversations: 22 clusters hold 35–492 threads each. The headline is one member's item, and the score mass includes high-scoring posts cited for unrelated members — a 900-score open letter to Google executives, from an owner who says they killed the business, sits under the cluster saying SEO does not depend on WordPress. They appear once, as a map; the practices come from the 4–34-thread band. (3) **Eighteen years, retired features.** `consensus` text still names Google My Business (now Business Profile) and Google+, toolbar PageRank, AMP, Universal Analytics, Google Optimize, Data Studio, FAQ/HowTo rich results and the Structured Data Testing Tool. Check the newest citation before anything else.

### What these practitioners talk about most — topic clusters, not practices

Thread counts and score mass measure how much these practitioners argue about a topic, not agreement with the cluster's headline.

| topic (cluster headline paraphrased) | threads / score mass | items G/C |
|---|---|---|
| Link building in general (headlined by a PBN recipe — see warnings) | 492 / 20,950 | 401/260 |
| Hiring and screening an SEO agency; what a retainer buys | 319 / 15,293 and 214 / 12,357 | 225/159 and 183/56 |
| Buying links; DA/DR as a buying criterion | 204 / 6,789 | 141/81 |
| AI-written content and AI detectors | 200 / 9,091 | 141/63 |
| Local SEO and the Google business listing | 186 / 6,187 | 137/84 |
| Ranking with content and few or no links | 144 / 4,252 | 89/52 |
| What to measure instead of raw traffic; revenue as the KPI | 139 / 4,645 and 57 / 1,951 | 95/42 and 28/28 |
| Learning SEO on your own site | 134 / 6,465 | 93/49 |
| The paid-tool split (Ahrefs links, Semrush keywords, Screaming Frog crawls) | 133 / 6,734 | 88/63 |
| Keyword research: Keyword Planner, competitor keywords, data over intuition | 125 / 4,593 and 58 / 2,104 | 88/59 and 44/16 |
| Search Console as the free base tool | 93 / 3,132 | 73/22 |
| CMS choice does not decide SEO | 82 / 4,681 | 56/23 |
| Do not depend on Google organic alone; diversify after HCU | 78 / 3,179 and 35 / 2,059 | 49/13 and 21/12 |
| Page speed / CWV is a small ranking factor | 70 / 2,741 | 51/21 |
| Refreshing existing content | 60 / 3,223 | 39/20 |
| "GEO / AEO is SEO" — contested inside the cluster | 58 / 2,400 | **9/48** |
| Reddit in the SERP; users append "reddit" to queries | 48 / 3,049 | 32/7 |
| Image alt text and file names | 45 / 1,960 | 35/12 |

### The practices that survived verification

Format: practice · label · N thr / S · newest citation · items G/C.

**Indexing, crawling and site changes**
- Zero organic traffic: check first for a sitewide `noindex` or `Disallow: /` left by a developer or the previous agency · `consensus` · 13 thr / 481 · 2026-01 · G4/C9. In this layer's fastest-fix thread, one member reports that removing a noindex brought hundreds of thousands of visits in a single day (score 64).
- "Not indexed" does not mean "not crawled", and indexed does not mean ranking · `consensus` · 32 thr / 844 · 2026-09 · G24/C12. Its variants disagree on requesting indexing URL by URL; the technical practitioners' reading (crawled-not-indexed is a quality and demand decision) governs.
- A domain or URL change needs a 301 from every old URL to its matching new URL, not a homepage forward; rebuild the old list from the old sitemap or archive.org · `consensus` · 19 thr / 548 · 2026-03 · G16/C4. One reply: a changed URL structure makes every page new, so rankings start again from zero (score 25).
- Bring SEO in before a redesign, and keep the URLs · `consensus` · 4 thr / 742 · 2025-10 · G3/C1. The anchor case: top pages renamed with no redirects dropped to zero traffic (score 52). **Counter:** a score-39 reply in the same thread blames the latest algorithm changes instead. Most of the score mass is the 356-score post itself.
- Sitemaps are free in every mainstream CMS — do not pay for generation; submit once to Search Console and Bing, and resubmit only if the file name or location changes · `consensus` · 9 thr / 188 · 2025-06 · G4/C5, and 7 thr / 312 · 2026-03 · G4/C3. A sitemap does not force indexing; links from other pages carry the context.
- Do not `nofollow` internal links · `consensus` · 15 thr / 1,091 · 2026-03 · G10/C4. 811 of that score is two list posts (468, 343); the comment-level support is thinner than the number.
- Keep years and company names out of URL slugs · `consensus` · 9 thr / 97 · 2026-08 · G4/C5. Thin score.

**Search Console and measurement**
- Chain the Performance filters: click a query, then Pages, to see every page ranking for it; click a page, then Queries, for the reverse · `consensus` · 8 thr / 260 · 2025-11 · G2/C6.
- Do not chase a zero-error Search Console; act on a sudden wave (hundreds of new errors overnight), not on the standing list · `consensus` · 10 thr / 206 · 2026-01 · G6/C4. The top reply says only agencies padding their client sales care about the standing list (score 29).
- Third-party traffic estimates are keyword-model guesses and can be off by orders of magnitude — one owner: Ahrefs said 3K pageviews a month against 234K real · `consensus` · 8 thr / 138 · 2026-01 · G3/C5.
- Wait until a core update has finished rolling out before judging rankings, and check seasonality first · `consensus` · 7 thr / 188 · 2025-12 · G5/C1.
- GA4 is a different measuring stick from Universal Analytics: an engaged session is >10 s, 2+ page views or a conversion, and bounce rate is the inverse of engagement rate, so GA4 bounce rates fall without behaviour changing · `consensus` · 5 thr / 741 · 2025-09 · G3/C2. The definitions come from one 176-score post; the other threads mostly agree GA4 is hard to read.
- Google Ads on the same keywords can take clicks the organic listing would have had · `consensus` label, contested content · 9 thr / 281 · 2025-05 · G7/C2. Top reply: most likely a coincidence, otherwise the ads are cannibalising the organic clicks (score 22).

**Links and penalties**
- Disavow only under a manual action, and never pick links by a tool's "toxic" score · `consensus` · 27 thr / 778 · 2026-06 · G17/C9, and 14 thr / 347 · 2026-05 · G9/C4. Same answer as the technical and professional practitioners. **Counter (grounding flag, supported):** in one thread a score-72 and a score-29 comment say spam links can hurt and cite attacks; the ignore side (score 29 and a long practitioner answer) cites Google saying such links are ignored. If someone uploads a disavow of your good domains, delete the file at once (68-score post). **Bridge:** Google's page is wider than these practitioners — it also covers links that likely will cause a manual action, after removal is tried `[documented: https://support.google.com/webmasters/answer/2648487, 2026-10-11]`.

**Performance**
- A Lighthouse or PageSpeed 100 does not rank a page; fix real slowness for users and conversions · `consensus` · 6 thr / 378 · 2025-09 · G5/C1. One commenter: about 95% of top-ranking sites fail page-speed tests, yet lifting a score of 20 to 80 is worth the work (score 51). Agrees with the technical practitioners' reading that CWV is a floor.

**Content and AI**
- AI-content detectors are unreliable: one flagged a blog post written ten years ago as 95% likely AI (score 25) · `consensus` · 9 thr / 257 · 2024-12 · G4/C4. (The 200-thread cluster with the same headline is a topic soup; this smaller one is the claim.)
- Google rewrites meta descriptions with page text when it judges that a better match for the query; you cannot force yours · `consensus` · 8 thr / 236 · 2025-04 · G2/C7. Write the description to answer the query.
- One H1 per page is the convention; whether extra H1s hurt is disputed · `consensus` label, contested content · 8 thr / 358 · **newest 2022-09** · G7/C1.

**AI search**
- llms.txt does nothing for AI visibility; bot control is robots.txt · `consensus` · 11 thr / 1,016 · 2026-06 · **G0/C11**, and 9 thr / 460 · 2026-08 · **G0/C9 — one producer only.** Weaker for that, but the technical practitioners reached the same consensus independently, and two server-log reports agree: one host saw no LLM user-agent request the file on any of its hosted client sites (score 14).
- AI Overviews answer informational queries in the SERP and cut clicks there; commercial and local queries still click through — split a decline by intent before diagnosing it · `consensus` · 11 thr / 363 · 2025-06 · G7/C3.
- ChatGPT search does not simply reuse Google's top results · `consensus` label, contested content · 10 thr / 187 · 2025-12 · G6/C2. For: a practitioner whose site is not on Google's first two pages got a client who found them through ChatGPT (score 9). **Counter:** the higher-scored reply in the same thread (score 24) says GEO is the same thing as SEO and calls LLMs-as-independent-search-engines GEO disinformation. The extractor recorded these two the wrong way round; this is the reading of the comments themselves.

**Agencies and audits**
- A guarantee of rankings or placement disqualifies an SEO provider · `consensus` · 8 thr / 771 · 2025-08 · G4/C4. Top reply: rankings are Google's decision, not an agency's (score 142). The myth list below makes the same correction.
- A Semrush site audit is not an SEO audit · `consensus` · 14 thr / 538 · 2025-11 · G13/C2. Top answer: Semrush cannot do an SEO audit for you; it is one input to one (score 32).

### High-scored, and a warning, not a practice
- **PBNs as ranking links · 492 thr / 20,950 — the largest cluster in this layer — is headlined by a PBN recipe** (unique IPs, posts on the homepage, branded anchors). PBNs are a link scheme under Google's spam policies; the cluster's own variants are outreach, local partnerships and directories. Same shape as the professional practitioners' link cluster.
- **Fake review stars through structured data** — one member added fake star reviews to every page of a site and reports that organic traffic shot up (score 43), until Google asked for removal through Search Console. Structured-data spam.
- **Dripped review vendors** — inside a cluster headlined against buying dripped Google My Business reviews, the second-highest citation (score 34) names a vendor and points readers to the commenter's own profile. Fake reviews break Google's policies.
- **Keyword density up to 3–4%** · 7 thr / 101 — the headline is contradicted by its own cited comments (one says not to fixate on density, another simply says no); density targets are folklore.
- **Spam indexing and bulk AI as strategies** — one spam-indexing project went to $18k a month and ran for almost 2 years before it was deindexed (score 5); a bulk-AI success post came from a domain registered on October 7th whose owner was promoting their own tool (score 9), and the reply warned that one manual action could deindex the whole site (score 85). An AI "bypasser" paraphrasing tool is pushed by repeated sales comments across unrelated threads.
- **Retired features inside `consensus` text**, correct when written: Google Places plus a Google+ page in a local checklist, Google Optimize in a tool stack, AMP as routine technical work, a variant predicting the toolbar PageRank shutdown. History, not instructions; the surrounding advice can still stand.

### Myths the community corrects
Thin — 3 to 12 threads each — so read as leads.
- *SEO is dead* (12 thr, the most repeated): mocked as declared every year since 2007. A separate 3-thread correction: after HCU the casualty posts cluster on content, news, review, affiliate and ad-funded sites, while local service businesses report search working.
- *A good agency guarantees first-page rankings* (5 + 3 thr): an immediate red flag; the usual dodge is ranking a long-tail term nobody searches.
- *DA / DR is how Google evaluates links* (5 thr): a third-party estimate that can be inflated with spam links.
- *Duplicate content earns a penalty* (3 + 3 thr): no manual penalty; Google filters to one version.
- *The March 2024 update only hit AI content* (4 thr): human-written sites reported 60–80% drops too.
- *Google detects and deindexes all AI content* (3 thr): commenters say it cannot detect AI; Google's line is helpfulness.
- *Domain age is a ranking factor* (3 thr): one voice says Google denied it; a reply asked for a source.

### Tools
Practitioners' stack: **Search Console** (the free base tool — indexing, queries, the Performance filters above), **a crawler first — Screaming Frog** (`consensus` · 11 thr / 336 · G7/C2: a crawler is a must-have, score 37), **Ahrefs** for backlinks (subscribe month by month rather than yearly — single thread, score 39), **Semrush** for keyword and competitor research, **Google Keyword Planner** (free, inside Google Ads), **Bing Webmaster Tools**, **GA4**. Distrusted by consensus: anything sold by Neil Patel (13 thr / 713 · G6/C7) and AI-content detectors (above). Tool thread counts are not shown: a mention count is not usage, and on the professional layer the reducer's tally capped at 6.

### The full corpus

