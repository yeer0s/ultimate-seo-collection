<!-- split-header: part 5 of 8 of practitioner-playbook.md (step-3 original lines 248–312; boundary H2) -->
# Practitioner layer — professional practitioners
## Contents

- Professional practitioners — primary corpus layer

Other parts of the same original file: [practitioner-index.md](practitioner-index.md), [practitioner-technical-1.md](practitioner-technical-1.md), [practitioner-technical-2.md](practitioner-technical-2.md), [practitioner-agentic.md](practitioner-agentic.md), [practitioner-general.md](practitioner-general.md), [practitioner-secondary-digest-1.md](practitioner-secondary-digest-1.md), [practitioner-secondary-digest-2.md](practitioner-secondary-digest-2.md).

<!-- /split-header -->
## Professional practitioners — primary corpus layer

**The evidence tier.** A collected corpus of public practitioner discussions (anonymised sources), complete for this community: 34,623 threads and 222,690 comments, dated 2013-04-26 to 2026-09-22, collected credential-free. Real gaps: 4 posts short of the platform's own comment count (5 comments), 19 orphan comments. The 989 highest-signal threads were read in 155 half-size chunks by free lanes only — Gemini Flash-Lite (108 chunks) and Cohere Command A (46), one by OpenRouter's free nemotron — through `king_map.py`, which accepts an output only when it has ≥3 usable items and cites ≥25% of the chunk's threads; all 155 passed first time. 743 claims in; 737 usable after dropping 8 fabricated comment ids, 5 fabricated post ids and 5 real comments cited under the wrong thread. Thread coverage averages 0.59 (worst 0.29), with no link to chunk size. 473 distinct practices after merging.

**The label grammar** is the agentic layer's (consensus = ≥2 threads by ≥2 distinct authors and ≥10 summed score). The extraction model called 403 practices `consensus`; the evidence supports **49 of 473**. The grounding pass flagged only 8 — far cleaner than the agentic layer's 49 — and all 8 were read against their full cited bodies (first pass by a free model, every verdict re-checked against the source, two overturned): 2 supported, 6 partial (core in the source; the named tool, framework or number added by the model), 0 unsupported. The 49 consensus clusters were read for four failure shapes; the ones that matter are carried inline below.

**Two reading rules this layer adds.** (1) **Old posts, retired tools.** The corpus runs 13 years; several `consensus` lines are correct history and wrong instructions — Search Console's preferred-domain setting (removed 2019), URL Parameters handling (retired 2022), Fetch & Render (now URL Inspection) and the Mobile-Friendly Test (retired late 2023) all appear as advice. Check the newest-citation date before anything else. (2) **A big cluster's headline is a topic, and sometimes the wrong one.** The representative is the member the rest of the cluster overlaps most, which in a 20–40-thread cluster is often a heading ("Keyword Research", "Content Creation"), and twice it is a narrow claim the cluster itself contradicts. Read the practice, not the headline.

### The practices that survived verification

Format: practice · label · N thr / S · newest citation.

**Technical — this layer's most durable material**
- `robots.txt` stops crawling, not indexing: to de-index, lift the block and serve `noindex` (or use removals) · `consensus` · 4 thr / 20 · 2024-04. Same answer as the technical practitioners.
- For "Crawled – currently not indexed" on a new site: export the URLs with their URL Inspection state, check each has contextual links from indexed pages and a distinct intent, consolidate thin or duplicate pages · `consensus` · 3 thr / 16 · 2026-05.
- Trim low-value, near-duplicate and templated pages to free crawl budget · `consensus` · 11 thr / 152 · 2026-08. Audit before `noindex`ing — consolidation by redirect is often better, and `noindex` alone may not improve how Google rates the site · `consensus` · 3 thr / 25 · 2026-02.
- Link new pages from high-traffic, authoritative pages to raise their crawl priority · `consensus` · 5 thr / 21 · 2026-08.
- Keep redirects to one hop where possible, never more than a few on frequently crawled URLs; check them with `curl` rather than trusting a tool · `consensus` · 3 thr / 30 · 2025-11 and 2 thr / 10.
- Hacked spam URLs: return `410`, do not block them in robots.txt and do not redirect them · `consensus` · 2 thr / 15 · 2018 (old, but unchanged).
- Verify a bot's identity before blocking it from logs — the classic mistake is blocking Googlebot · `consensus` · 3 thr / 16 · 2021.
- Google renders JavaScript, but client-side rendering can overwrite server-rendered content (translations named) · `consensus` · 5 thr / 47 · 2025-11. Diagnose with URL Inspection's rendered HTML (the Fetch & Render and Mobile-Friendly tools cited in 2 more threads are retired).
- Subdirectories over subdomains for a blog (`/blog`, not `blog.`) · `consensus` · 2 thr / 51 · 2026-03. These practitioners' default, not a law.
- Enterprise sitemaps: generate from the backend, split well under the 50,000-URL limit by category, list them in an index file · `consensus` · 2 thr / 16 · 2020.
- Hreflang across country domains: one Search Console property per domain, and content that is localised rather than copied · `consensus` · 8 thr / 47 · 2026-05.

**Measurement**
- GSC position is an average over personalisation, location and device — it will not match what you see; de-personalised searches get closer, never equal · `consensus` · 10 thr / 96 · 2025-11.
- A bounce rate near 0% means analytics is firing twice (GTM plus a hard-coded or plugin tag) · `consensus` · 3 thr / 245 · 2022. Universal Analytics metric, but the double-tagging diagnosis carries to GA4.
- GSC alone cannot show conversions, keyword volume or a full backlink picture · `consensus` · 11 thr / 171 · 2026-08.

**Links**
- Do not disavow spammy links or sudden spam-anchor spikes unless you have a manual action · `consensus` · 2 thr / 14 · 2023-08. **Contradicted** by another `consensus` cluster advising weekly disavows during a negative-SEO attack · 3 thr / 48 · 2021. The newer position is the first, and the technical practitioners' myth list (disavow will not bring rankings back) agrees. Google's page also covers links that likely will cause a manual action, after removal is tried `[documented: https://support.google.com/webmasters/answer/2648487, 2026-10-11]`.
- Guest posts: avoid pay-to-play multi-topic "guest post farms"; target real trade publications · `consensus` · 2 thr / 18 · 2025-04. The DA thresholds and named outlets in the practice text are the model's detail, not the cluster's.
- Competitor backlink gap: sites linking to competitors but not to you · `consensus` · 2 thr / 14 · 2019. Bing Webmaster Tools shows full backlink profiles and anchors free · `consensus` · 5 thr / 64 · 2026-02.

**Strategy and process** — this layer's distinctive material, and why it is worth reading at all
- Moving agency → in-house: relationships, internal workflows and business-aligned goals first; dashboards and training per team · `consensus` · 20 thr / 534 · 2026-03.
- Push back on unrealistic growth targets (e.g. +100% YoY) with internal history, competitor growth curves and, if needed, a third-party audit · `consensus` · 6 thr / 107 · 2024-08.
- Agency red flags: promises of fast results, a hidden team, vanity metrics · `consensus` · 6 thr / 176 · 2026-02.
- Compete with national brands on second-tier head terms and the long tail first · `consensus` · 2 thr / 39 · 2022. Cover the entities the top 5–10 results cover rather than repeating the keyword · `consensus` · 2 thr / 39 · 2025-11.

### High-scored, and a warning, not a practice
- **"Link Building Strategies" · 39 thr / 37 authors / 868 — the largest cluster in this layer — is headlined by a recipe of spun articles, press releases, private-network posts and guest posts.** Spun content and PBNs are link schemes under Google's spam policies, and the cluster's own variants say the opposite (avoid consultants who use PBNs; niche contextual placements over guest-post farms). The 39 threads agree that link building matters and disagree on how; the headline is one member's spam recipe.
- **"Content Creation" · 37 thr / 593** is headlined by advice to write the money pages in-house and outsource the content meant to attract links — the same shape: a narrow link-scheme tactic heading a generic content cluster.
- **Retired-tool instructions**, correct when written: set the preferred domain to HTTPS in Search Console (2 thr / 44 · 2021 — the setting is gone; the 301s and internal-link updates in the same line still apply); handle UTM parameters with GSC parameter handling (5 thr / 71 · 2018 — tool retired; canonicals remain the answer); avoid AMP for e-commerce (3 thr / 81 · 2019 — moot since AMP stopped being a Top Stories requirement).
- **"Keyword Research" · 20 thr / 360** is headlined by advice to mine keywords from affiliate networks such as Commission Junction — a merge artifact; nothing in the cluster's variants or thread titles concerns affiliate networks.

### Myths the community corrects
- *Domain Authority / Domain Rating is a Google metric.* Third-party estimates; Google does not use them · 3 thr, and again in 2.
- *Page-speed scores and domain age are primary ranking factors.* Speed matters when it causes failures or abandonment; age is one weak signal · 3 thr.
- *Content-tool scores (Surfer, MarketMuse) guarantee rankings.* They average the top results and invite over-optimisation · 2 thr.
- *Paid "contributor" or guest-post programmes sold by big SEO platforms are safe.* Scaled guest posting for links violates Google's guidelines, per Mueller · 2 thr.
- *JavaScript sites cannot be indexed.* Google renders JS; complex implementations still break · 2 thr.
- *Google tells the whole truth about ranking.* Treat statements as claims to test · 2 thr.

### Tools
Practitioners' stack, by what it is used for: **Screaming Frog** (crawls; in its crawl settings, tick pagination, hreflang and AMP so those URLs are discovered · `consensus` · 2 thr / 136), **Ahrefs** (backlinks — a short trial covers a one-off audit) and **Semrush** (competitive visibility and intent tagging) · `consensus` · 2 thr / 16, **Bing Webmaster Tools** (free backlink data), **Sitebulb**, **Majestic**, **GSC**, **Looker Studio**. Distrusted by consensus: generic free "SEO analyzer" widgets (Neil Patel's, Sitechecker) · 2 thr / 106, and **BrightEdge** on price and sales tactics · 2 thr / 148 · 2022. Tool thread counts are not shown: the reducer's tool tally caps at 6, so equal counts mean nothing.

### The full corpus

### What has no corpus layer

(corrected 2026-10-11 — the general practitioners now HAVE a primary corpus layer: the next section, collected and read in full, with every cited id checked. What still has no corpus layer is the general-practitioner material in the secondary snippet digest further below — "Consensus canon" onward — whose attributions and scores remain unverified; do not read the new section's rigour as covering those lines.)

