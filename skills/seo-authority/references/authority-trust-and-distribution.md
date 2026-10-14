<!-- split-header: part 2 of 2 of authority-and-distribution.md (step-3 original lines 67–139; boundary H2) -->
# Authority — E-E-A-T, entity and brand, GEO citation tactics, distribution, site reputation
## Contents

- E-E-A-T and trust engineering
- Entity and brand
- GEO / AI-citation tactics with their marks
- Distribution: Reddit, YouTube, UGC — practitioner territory
- Site reputation abuse — the EEA update

Other parts of the same original file: [authority-links-and-pr.md](authority-links-and-pr.md).

<!-- /split-header -->
## E-E-A-T and trust engineering

**What it is** `[documented: https://developers.google.com/search/docs/fundamentals/creating-helpful-content, 2026-10-12]`: Experience, Expertise, Authoritativeness, Trustworthiness is the framework in Google's Search Quality Rater Guidelines. Raters evaluate results; rater data is not used directly in Google's ranking algorithms, and E-E-A-T itself is not a specific ranking factor. Google's systems give more weight to content with strong E-E-A-T on topics that could significantly affect people's health, finances or safety (YMYL, including personal finance), but the causal path from a byline to a rank is documented nowhere.

**What the study measured** (E-E-A-T and authorship family, mostly AI-citation metrics):

- **#60 Author bylines linking to a profile** — `[measured: MAINSTREAM, n=7, c=1]` headline +113% AI citation rate from one source (seerinteractive.com 2026, 123 pages, before/after with control); the one controlled A/B (searchpilot.com 2023) reports direction only; 4 of 7 designs have no control. Recipe: 20 posts vs 20 matched, one site, 30 days.
- **#61 Author bios + company credentials** — `[measured: MAINSTREAM, n=3, c=1]` headline +40%, median +53.5% AI citation rate, range +40% to +67%; the +40% is one uncontrolled source, size not reported; the controlled sample is direction only. Bundle.
- **#63 Rewrite AI text with human editing + E-E-A-T** — `[measured: MAINSTREAM, n=5, c=2]` headline +67% AI citation rate from one uncontrolled source (2 pages); the controlled test (10 domains) reports +2.2 ranking positions. Bundle: rewrite, credentials, citations, answer formatting in one release.
- **#62 Footnotes → inline citations** — `[measured: EXPERIMENTAL, n=1, c=0]` +40% AI citation rate, 15 vs 15 articles. Do not carry.
- **#66 Citations to authoritative sources** — `[measured: MAINSTREAM, n=2, c=2]` +31.4% impressions, **measured on a benchmark engine (arXiv, 1,000 queries), not a live console**, bundled with other GEO edits; the second sample is direction only; range −30.3% to +115.1%, crosses zero.

Together: authorship has been tested almost entirely on AI-citation metrics, on small page sets, with one or two controlled designs per entry. Direction is consistent; sizes are not transferable. Ship authorship because a reader of a money page has a right to know who wrote and who checked it; measure with a holdout if you want a number.

**Trust engineering for a comparison platform** `[unvalidated house heuristic]`: a **methodology page** — how offers are compared, how the site earns money, how offers rank and ties break, coverage and exclusions, how prices are verified and how often, how to report an error — linked from every comparison surface; a **real organisation** (legal entity, address, contact, About page with the actual team, privacy and terms); **genuine reviews only**.

**YMYL/finance specifics for Portugal** `[unvalidated house heuristic]`:

- **Source rules from the issuing authority, with effective dates**: Autoridade Tributária (IRS tables, retenção na fonte, IMT/IMI), Diário da República (the statute or portaria, number and date), ERSE (tariffs, regulated components, CAV), ANACOM (telecom rules), Banco de Portugal (credit, TAEG, fees), ASF (insurance). Cite the primary document; a blog summarising the rule is not a source.
- **Validate calculators against official worked examples** — AT simulators and published examples, ERSE tariff sheets, BdP's TAEG methodology — plus boundary cases and rounding. Record the validation and date; a result that cannot be reconciled to an official example is not publishable.
- **Visible corrections log** — what was wrong, when fixed, what changed (mowei runs `/correcoes`; link it from the surfaces it corrects).
- **"Reviewed by" on money pages** — a named reviewer of record, the effective date of the rules applied, the algorithm version where one exists. Not because a byline ranks; because someone deciding on a mortgage should see who stands behind the number.

## Entity and brand

- **#64 Schema + directories + brand content** — `[measured: MAINSTREAM, n=3, c=0]` headline +193% (657 sites, no control), median +207.8% impressions, range to +222.6%. Bundle: Organization schema, rewritten product details, directory listings, brand-mention outreach.
- **#65 Entity hubs** — `[measured: EXPERIMENTAL, n=1, c=0]` +29.8% AI citations, one source. Do not carry.

Regardless of marks: **Organization and WebSite structured data** on the home page so engines can associate site name, logo and official profiles: Google says WebSite structured data on the home page is the most important way to state a site-name preference `[documented: https://developers.google.com/search/docs/appearance/site-names, 2026-10-12]`, and that Organization markup helps disambiguate the organization and can influence the logo shown `[documented: https://developers.google.com/search/docs/appearance/structured-data/organization, 2026-10-12]` — eligibility for a displayed name, not a ranking lever. **Consistent name, address, phone and legal identity** across the site, registries and controlled profiles `[unvalidated house heuristic]`. **Brand-search demand is the output to track** `[hypothesis]` — branded impressions and clicks in Search Console, branded volume in Bing Webmaster Tools, as the series digital PR, community work and video are supposed to move. Separate brand demand with Search Console's branded-query filter `[practitioner: anonymised sources · consensus · 3 thr / 34 · newest 2025-11-25]`. Links are an intermediate; brand search is what a person does after they trust you.

## GEO / AI-citation tactics with their marks

The loudest discourse and the thinnest record: 10 AI-visibility entries against 36 on content depth, most measured on small query sets or benchmarks.

- **#72 Schema + datasets + answer threads** — `[measured: MAINSTREAM, n=5, c=1]` +47 AI citations (absolute count), from 50 queries; 5 publishers, 1 before/after with control, 0 randomised A/B, the other four designs uncontrolled. Bundle: FAQPage + dateModified schema, datasets, entity profiles, forum threads. FAQ rich results were retired 7 May 2026 `[documented: https://developers.google.com/search/updates, 2026-10-11]`.
- **#73 Structured text captions on visuals** — `[measured: MAINSTREAM, n=7, c=1]` headline +20% organic sessions from a controlled A/B (arXiv 2026, size not reported), median +47.5%, range to +75%; benchmark-flagged. Recipe: 200 image pages vs 200 controls.
- **#74 Rewrite text using GEO tactics** — `[measured: MAINSTREAM, n=12, c=2]` +83.2% AI citation rate, median +83.8% across 2 samples; **benchmark-measured** (arXiv 2024, 1,000 queries), with 5 academic studies and 5 uncontrolled before/afters behind it. Highest evidence score in the family and still not a live-console number.
- **#75 Modular posts for generative search** — `[measured: MAINSTREAM, n=4 across 2 publishers, c=0]` +49 indexed pages (index coverage, not citations), 7 days, headline from 3 pages. Direction only.
- **#66** — see above; benchmark, bundle, crosses zero.
- **#69 Quantitative statistics** `[measured: ACADEMIC, n=1, c=0]` +37% AI citation rate; **#70 Quotations from credible sources** `[measured: ACADEMIC, n=1, c=0]` +22% impressions. Princeton GEO benchmark lineage: simulated engine, effect sizes not comparable to a live site.
- **#67 Keyword-stuffed passages "for AI"** — `[measured: AVOID, n=1, c=0]` −10% impressions, benchmark. The family's one negative, and the one most consistent with engine documentation.
- **#68 llms.txt + schema** `[measured: MAINSTREAM, n=4, c=0]` headline +22%, median +53.5% AI citation rate; **#71 llms.txt alone** `[measured: MAINSTREAM, n=3, c=0]` +25% organic sessions, **no median — values run −19.7% to +81% and cross zero**. Both marked "mechanism unconfirmed". Google states Google Search does not use llms.txt, that it "will neither harm nor help" visibility in Google Search, and that no new machine-readable file is needed for its AI features `[documented: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide, 2026-10-11]`; the same page allows the file "for other services or systems that use these files". For other engines and model providers we hold no official statement; practitioners report the file is rarely fetched `[practitioner: anonymised sources · consensus · 5 thr / 123 · newest 2026-07-27]`. **Ship as a no-claim** — one static file, if the client wants it — or skip.

**The edge gate, before any of the above** `[unvalidated house heuristic]`: confirm the target engine's crawler is allowed through the CDN/WAF. On mowei the Cloudflare AI-crawler policy decides which bots read anything; a blocked bot reads nothing and every GEO tactic aimed at it is dead on arrival. List allowed user agents against the engine's documented bot names, then propose page changes. Re-check after every Cloudflare rule edit.

**Measure citations directly where the engine offers it**: Bing Webmaster Tools' AI Performance report (public preview, 10 Feb 2026) gives total citations, average cited pages, sampled grounding queries and page-level citation counts across Copilot, Bing AI summaries and partner integrations; Bing states its average-cited-pages figure "does not indicate ranking, authority, or the role of any page" `[documented: https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview, 2026-10-11]`. This replaces "Bing page-1 = citation pool". Google's nearest read is Search Console's generative AI performance report (all sites "As of August 31, 2026"): impressions in Search generative AI features, not citations `[documented: https://support.google.com/webmasters/answer/16984139?hl=en, 2026-10-11]`.

**Fan-out in three lines**: Google says AI Overviews and AI Mode «may use a "query fan-out" technique — issuing multiple related searches across subtopics and data sources — to develop a response» `[documented: https://developers.google.com/search/docs/appearance/ai-features, 2026-10-11]`. That other AI answer surfaces work the same way, retrieving from a conventional index and their own stores, and that a page is retrieved for the rewritten queries rather than the head term and can be cited from outside the classical top 10, is `[hypothesis]`. No pure-GEO bypass of being retrievable exists. Full treatment: skill `seo-ai-search` › ai-retrieval-and-citation.

## Distribution: Reddit, YouTube, UGC — practitioner territory

The study's author states the corpus cannot see LinkedIn, Slack/Discord, conference decks or NDA'd client work, and the catalogue has **zero entries** on Reddit, YouTube or community distribution. Each line carries its own label, mostly house judgment; present it to a client as judgment, not evidence.

- **Answer genuine community questions with disclosure and original evidence** `[unvalidated house heuristic]` — in r/portugal, r/literaciafinanceira and Portuguese finance forums, answer in the thread, disclose the affiliation, bring the number (tariff table, bracket, fee) rather than the link; link only when thread rules and usefulness both call for it. Never multiple accounts, never seeded questions, never paid placement — astroturfing is found.
- **Reddit-in-SERP reality** — Reddit in the SERP is one of the general practitioners' most argued topics (a topic cluster, not a practice: 48 thr / 3,049, skill `seo-evidence` › practitioner-general); its share of Portuguese commercial queries is unmeasured here, so sample the target SERPs first. The play is not to be in the thread but to publish the page that answers the thread's question better than the thread does; ranking threads are free query research and the bar your page must clear `[unvalidated house heuristic]`.
- **Portuguese calculator walkthrough videos** `[unvalidated house heuristic]` — short recordings of one real scenario ("quanto pago de IRS com dois titulares e um dependente"), transcript on the page. Video as a second discovery surface and trust signal, with the transcript as the part that gets indexed and cited, is a `[hypothesis]`.
- **Turn recurring questions into content and product** `[unvalidated house heuristic]` — recurring questions are the content backlog; recurring misunderstandings are calculator UX defects.
- **Search Console reporting for social and video platform content** — Google added a guide (29 July 2026) on how to analyse social and video platform content performance in Search Console `[documented: https://developers.google.com/search/updates, 2026-10-11]`; do not assume Reddit has the same integration until the page confirms it.
- **Measure platform discovery and qualified referrals separately from rankings** `[unvalidated house heuristic]` — referral sessions by source, assisted conversions, branded-search lift after a thread or video, in their own report. Folding them into "organic" hides both the win and the null.
- **Hosted UGC** — moderate and keep author provenance `[unvalidated house heuristic]`; where users can insert links, Google says to add `ugc` or `nofollow` to them `[documented: https://developers.google.com/search/docs/crawling-indexing/links-crawlable, 2026-10-11]`.

The detailed practitioner layer — what general, professional and technical practitioners (anonymised sources) report about these channels — lives in skill `seo-evidence` › practitioner-index.

## Site reputation abuse — the EEA update

`[documented: https://developers.google.com/search/blog/2026/08/update-site-reputation-policy, 2026-10-14]` «Following discussion with the European Commission», from 30 August 2026 Google applies **no manual action affecting rankings for searchers in the EEA** under the site reputation abuse policy. It may instead **separate the affected section** so it ranks on its own merits. **Outside the EEA, manual actions still apply** to the affected portion. Portugal is in the EEA. The action is still issued and notified in Search Console; only its ranking effect is limited to searchers outside the EEA. `[documented: https://developers.google.com/search/blog/2026/08/update-site-reputation-policy, 2026-10-11]`

This changes nothing about what to publish. Google's own worked example puts an integrated, disclosed, publisher-curated coupons section under «Not likely to take action» `[documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-14]`. The policy targets third-party content published on a host «mainly because of that host site's already-established ranking signals»; integration is one of the human-review factors, and «not one of these factors is either necessary or sufficient on its own» `[documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-14]`. The house refusal `[unvalidated house heuristic]` is broader: no third-party sections the host cannot validate — gambling reviews, partner-written "sponsored guides", outsourced coupon feeds — and it stands on three grounds untouched by the change: **correctness** (a YMYL platform's authority is its accuracy; a section it cannot validate is a hole in the brand), **reputation** (distrust earned on the parasite section carries to the calculator), and **non-EEA exposure** (Portuguese-speaking searchers in Brazil, Switzerland, the UK and the diaspora are outside the EEA; the manual action still applies to them). Penalty fear was never the right reason; the EEA change removes it without removing the others. Any third-party section is a owner-level decision, with editorial control and validation stated before a URL exists.

---

**Study entries covered:** 8, 9, 10, 11, 12, 13, 14, 15, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 145. Marks verified against the study catalogue and Evidence Appendix on 2026-09-22; where the headline differs from the study's median (#10, #12, #61, #64, #73, #145), both are printed.
