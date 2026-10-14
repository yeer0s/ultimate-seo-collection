<!-- split-header: part 3 of 8 of practitioner-playbook.md (step-3 original lines 141–186; boundary H3) -->
# Practitioner layer — technical practitioners (2 of 2): myths, tools, who answers, corpus
## Contents


Other parts of the same original file: [practitioner-index.md](practitioner-index.md), [practitioner-technical-1.md](practitioner-technical-1.md), [practitioner-agentic.md](practitioner-agentic.md), [practitioner-professional.md](practitioner-professional.md), [practitioner-general.md](practitioner-general.md), [practitioner-secondary-digest-1.md](practitioner-secondary-digest-1.md), [practitioner-secondary-digest-2.md](practitioner-secondary-digest-2.md).

<!-- /split-header -->
### Myths the community corrects

The belief, then the correction — the ones these practitioners say cost practitioners the most time.

- *llms.txt gets you cited / blocks AI bots.* Neither. Unofficial proposal, reported not crawled by Google and not respected by providers; bot control is robots.txt and per-bot user-agent rules.
- *Schema + CWV + crawl health is what gets a brand cited in ChatGPT or AI Overviews.* The score-13 reply says LLMs do not care about technical-SEO health; the higher-scored answers point at topical coverage, query fan-out, front-loaded answers and off-site co-occurrence. LLM crawlers also have no index and no ranking algorithm, and fetch shares in logs are not citation rates.
- *Optimising for LLMs means ignoring links, canonicals and PageRank.* The higher-scored reply (9 vs 5) says the model draws from page 1 of Google or Bing and rewrites the query — you still have to rank.
- *Lighthouse/PSI 100 means technical SEO is done.* Lab scores simulate a slow phone; the field bar is CrUX. A faster page does not beat a more relevant one, and 92→98 is wasted budget.
- *robots.txt Disallow keeps a URL out of the index.* It blocks crawling only — the URL can still be listed, and your noindex will never be seen.
- *"Discovered – currently not indexed" is a discovery failure* fixable with sitemaps, IndexNow or pings. Google already discovered them; sitemaps and internal links cannot create demand.
- *Adding schema makes a URL rank.* Mueller, April 2025: it feeds search-gallery features. A dip three days after adding markup was not the markup.
- *Google does not render JavaScript.* It does — contradicted by the highest-scored reply on the thread that claimed otherwise.
- *Disavow the links a tool marks "toxic".* Mueller: disavow will not bring rankings back. Toxic scores are tool-invented, and disavowing can remove links that help.
- *Google refuses to index AI-written content.* The stated distinction is helpfulness, not authorship; unedited slop gets dropped.

### Tools, and what practitioners actually use them for

Ranked by how many of the 732 read threads mention them.

- **Google Search Console** (111 threads) — page-indexing states, URL Inspection verdicts, the Google-selected canonical, crawl stats. Its sitemap report's "Success" row can be months stale.
- **Screaming Frog** (54 + 9 + 6) — full-site crawl to diff against the indexed set, migration change detection, orphan and depth segmentation. Free cap 500 URLs; crawling your own Cloudflare site needs a user-agent allow-rule. **Sitebulb** (14) fills the same role on large segmented sites.
- **Ahrefs** (37) / **Semrush** (20) — backlink and keyword data whose value is crawl size, not the UI. Both audit scores, and Semrush's "toxic" percentage, are explicitly distrusted.
- **Bing Webmaster Tools** (17) — faster URL-inspection debugging, and the differential test above.
- **GA4** (16) — splitting a traffic collapse by source, page and country; finding ChatGPT UTMs. **Cloudflare** (15) — edge blocking of AI crawlers, plus a named cache-poisoning risk.
- **PageSpeed Insights / Lighthouse** (11 + 6) — lab debugging of LCP and CLS; the threads say it misses INP (thread-dated); web.dev says tools like Lighthouse that load pages "without a user cannot measure INP" and names TBT as the lab proxy `[documented: https://web.dev/articles/vitals, 2026-10-14]`; can score ~100 while never loading most of the page.
- **Server logs** (7 + 4) — which bot, which URL, how often, what status. Preferred over any AI-visibility dashboard.
- **Google Indexing API** (9) — JobPosting and BroadcastEvent VideoObject only; every other use is folklore. **IndexNow** (4) pushes changes to Bing, Yandex and Yahoo, and ranks nothing.
- **Prerender.io**, **Botify**, **DeepCrawl**, **Oncrawl** (7/7/6/5) — prerendering and enterprise crawl/log suites, with prices and learning-curve complaints attached. A cluster of GEO/AI-visibility products (Profound, MentionDesk, Writesonic, BotRank) is named, but few of those mentions describe a reproducible method, and one recommendation came from a disclosed employee.

### Who answers correctly

Cumulative comment score is a crude authority proxy, but it surfaces whom these practitioners repeatedly score highly. Google staff post under their own accounts: **John Mueller's** (2,058, the single highest) and **Gary Illyes's** (766). Twelve consistently high-scoring practitioner accounts follow, at 1,653, 1,387, 1,204, 1,036, 933, 882, 843, 790 and 744, then 650/632/599. The mod-team account (1,545) is not a person.

**Authority is a prior, not a proof.** A Google staffer describes intended behaviour, which is not always observed behaviour, and Mueller's answers carry dates that age. A high-scoring practitioner can also be the one contested: the schema PSA above was posted by one of the corpus's highest-scoring accounts, at post score 0, and rebutted by the higher-scored replies. Weight the argument, not the handle.

### The full corpus


- `PLAYBOOK-technical.md` — the full 113,908-word distillation across 22 categories, with each practice's reasoning, variants, date-sensitivity note and citations.
- `reduced.json` — 1,169 practices as records (`evidence`, `consensus`, `contested_by`, `date_sensitivity`, `threads`, `score_mass`, `newest_citation`, `rank`), plus 659 questions, 588 myths, 808 tool entries. Slice with Python; do not read whole.
- `census.json`/`.md` — corpus composition. `eras.json`/`.md` — the topic shares behind the table above.
- the corpus database — 93 MB: every post and comment with scores, authors, dates and parents. The only place to re-verify a citation.

Go there when a practice needs its full evidence array, when a `contested` practice needs its actual counter-comments, when you need a topic this fold omits (content quality, ecommerce facets, local SEO, programmatic SEO, log analysis, measurement, site architecture), or to re-derive a score, date or author.

