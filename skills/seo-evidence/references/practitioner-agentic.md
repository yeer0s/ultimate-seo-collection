<!-- split-header: part 4 of 8 of practitioner-playbook.md (step-3 original lines 187–247; boundary H2) -->
# Practitioner layer — agentic-SEO practitioners
## Contents

- Agentic-SEO practitioners — primary corpus layer

Other parts of the same original file: [practitioner-index.md](practitioner-index.md), [practitioner-technical-1.md](practitioner-technical-1.md), [practitioner-technical-2.md](practitioner-technical-2.md), [practitioner-professional.md](practitioner-professional.md), [practitioner-general.md](practitioner-general.md), [practitioner-secondary-digest-1.md](practitioner-secondary-digest-1.md), [practitioner-secondary-digest-2.md](practitioner-secondary-digest-2.md).

<!-- /split-header -->
## Agentic-SEO practitioners — primary corpus layer

**The evidence tier.** A collected corpus of public practitioner discussions (anonymised sources), complete for this community: 3,703 threads and 21,071 comments, dated 2025-08-15 to 2026-09-22 (the community is young — 77% of posts are from 2026), collected credential-free. Real gaps, not the tautological coverage ratio: 0 posts short of the platform's own comment count, 0 orphan comments. The 500 highest-signal threads were read in 37 chunks by `nemotron-3-super-120b` on OpenRouter's free tier — a weaker extractor than the technical layer's, and it showed. It returned 724 claims. Before anything was counted, those claims went through checks: 19 claims whose every citation was an invented id were dropped (sequences like `q0a1b2c`, `r0b2c3d`), 9 fabricated comment ids dropped their citation, 5 post ids written into the comment field were repaired, 12 real comments cited under the wrong thread were dropped, and 52 scores were overwritten with corpus values. Six chunks came back unusable or near-empty on first pass (a bare `{"type":"string"}`, synonym field names, one chunk citing a single thread 35 times) and were re-mapped. Result: 690 verified claims, 544 distinct practices. Thread coverage — the share of each chunk's threads that any claim cites — averages 0.57 with no link to chunk size (large vs small +0.02), so the gaps are the model's judgement, not truncated input. Three chunks stay below 0.15 after two attempts; the fold is thinner there.

**What that buys.** Attribution, as on the technical layer — and less than the technical layer in one respect: **this community is vendor-brigaded.** Its highest-scored threads are tool launches and AMA posts from people announcing they automated their SEO, and the medoid headline of several merged practices names a product (SEO45, Clarico.ai, MentionDesk, Rankspot) that one member of the cluster mentioned. A score here is weaker evidence of practitioner agreement than on the technical layer. Everything stays `[practitioner]`.

**The label grammar** is the technical layer's, with one tightening that this community forced: **independent threads now means independent authors.** One user cross-posted the same autopilot promo twice, and the two threads earned `consensus` for a link-exchange scheme; the gate now counts distinct thread authors. That rule changed 1 label here and 0 of the technical layer's 60. The extraction model called 296 practices `consensus`; the evidence supports **28 of 544**. The grounding pass flagged 49 practices; each was hand-read against the full cited body (not the id — the body): 14 supported (the flag was paraphrase or a typo such as "robotx.txt"), 15 partial (the core is in the source; the model added tools or steps — only the core is carried below), **20 unsupported**. Six of the unsupported cite one comment that says only that a human strategist supervises the AI, while the practices attributed to it describe context repositories, humanizer rules, cron cadences and feedback logging — misattribution inside one thread. The 20 are omitted here; verdicts and reasons are in `exports/agentic/review_verdicts.json`. That is a reading, not a threshold: nothing was cut on its score.

No by-year topic table: `eras.py`'s topic list is tuned to technical SEO, and a one-year-old community has no eras.

### The practices that survived verification

Format as above: practice · label · N thr / S summed score · newest citation.

**Search Console as the agent's data source** — this layer's most useful material
- Triage GSC exports with an AI assistant: high impressions with low CTR, positions 5–10, URLs gaining impressions — flagged for a human to act on · `consensus` · 5 thr / 88 · 2026-09-07.
- Rewrite titles and meta descriptions where CTR sits well below the expected CTR for the position, from 90 days of query data · `consensus` · 2 thr / 18 · 2026-06-17.
- Use GSC's newer Performance features — the branded-query filter to separate brand demand, and chart annotations to mark site changes · `consensus` · 3 thr / 34 · 2025-11-25.
- Automate the discovery of weak internal links and decaying pages; push recommendations, not edits · `consensus` · 10 thr / 60 · 2026-08-09.
- Feed agents real keyword data through an API (DataForSEO named) instead of letting them estimate volume and difficulty · `consensus` · 3 thr / 14 · 2026-09-02. This is the community's own answer to overclaim pattern 2 in "Agentic SEO" below.

**Content**
- Build topical authority around entities instead of chasing keyword volume · `consensus` · 29 thr / 232 · 2026-09-14 — the broadest agreement in this layer (26 distinct authors), and correspondingly generic.
- Choose keywords by intent before volume · `consensus` · 6 thr / 18 · 2026-07-29 · and answer questions rather than target keywords · `consensus` · 5 thr / 15 · 2026-05-21.
- A human reviews every AI draft before publishing · `consensus` · 4 thr / 24 · 2026-05-23. Fact-check addresses, figures and dates — one practitioner's AI placed a client's lodge ~1,800 km from its real location · `single-voice`.
- Programmatic pages need at least three content differentiators beyond the swapped variable · `consensus` · 6 thr / 50 · 2026-06-14. **Bridge:** the March 2026 scaled-content enforcement below is what happens without them.

**Technical before scale**
- Fix sitemap, robots, canonicals, structured data and "crawled – currently not indexed" before automating content production · `consensus` · 2 thr / 237 · 2026-07-19.
- Schema markup (FAQ, HowTo, Organization) · `consensus` · 10 thr / 22 — ten threads, thin score; the technical practitioners' reading (rich-result eligibility, no special AI schema) governs.

**AI-visibility measurement**
- Track AI visibility by running a fixed prompt set across ChatGPT, Perplexity, Gemini and AI Overviews and logging citations and brand mentions · `consensus` · 5 thr / 54 · 2026-08-16. **Tension:** the technical practitioners' consensus prefers crawler logs over prompt dashboards, and most tools named here are the vendors posting.
- A self-run study of 270 AI answers (by one practitioner): ~10% of pages ChatGPT cites also rank in Google's top 10; citation overlap between engines 9–14%; Gemini names a brand ~82% of the time but links ~53% · `single-thread` · 1 thr / 41–44 · 2026-06-18. One author's unreplicated study — a hypothesis to test, never a percentage for a client report.

### High-scored, and a warning, not a practice

These cleared the numeric bar, or came close, and must never be repeated as recommendations. The score records that the community liked them.
- **Fully automated SEO with no manual step at all** — end-to-end pipelines that crawl, research, write, illustrate and publish daily · `consensus` · 4 thr / 265 and 8 thr / 161 · 2026-07-19. The highest-scored practice in this layer, carried by a 226-score AMA and launch posts; a reply in the thread dismisses it as pure advertising. It contradicts the community's own human-review consensus above and overclaim patterns 1 and 3 below.
- **Google Indexing API at scale, rotating service accounts past the 200/day quota** · `consensus` · 2 thr / 20. The API is documented for JobPosting and BroadcastEvent pages only (see Tools, technical layer); account rotation is quota evasion.
- **Triangular (A→B→C→A) link exchanges, designed so the reciprocal pattern cannot be detected** · `single-thread` after the author rule, and `contested` · 1 thr / 123 in another cluster. A link scheme under Google's spam policies — the evasion design is the admission.
- **Parasite SEO: 500 AI variants published at once on Medium, Substack, LinkedIn, Reddit, Quora** · `contested` · 1 thr / 11. Scaled content abuse and site-reputation abuse.
- **"Acquire backlinks"** · `consensus` · 5 thr / 13 — five threads agree on those two words and nothing more specific; one merged variant says directory submissions raise DA, which is a third-party metric (the community's own myth list says so).

### Myths the community corrects

Thin — one or two threads each — so read as leads.
- *A GSC data delay means a penalty.* It is processing lag; URL Inspection shows live status · 2 thr.
- *Domain Authority is a Google ranking factor.* A third-party metric · 1 thr. *More links beat better links* · 1 thr.
- *Core Web Vitals outrank content.* A tie-breaker between comparable pages · 1 thr.
- *Meta descriptions are obsolete because AI rewrites them.* They still move CTR · 1 thr.
- *You must buy an AI-visibility SaaS.* A self-hosted tracker over DataForSEO or SerpApi does the same job · 1 thr.

### Tools

Thread counts are not usage counts in this layer: the top ten by mentions include `getmorebacklinks.org`, `RankPilot.dev` and `MentionAgent`, posted by their makers. The stack practitioners describe using, not selling: **Search Console** (the data source for nearly every workflow above), **DataForSEO** (real numbers behind an agent), **Ahrefs/Semrush**, **Screaming Frog**, and **Claude connected to GSC/GA4 over MCP** — `contested` · 1 thr / 16; the counter-comment objects that the connector is closed-source third-party code reading your GSC and GA4 data through Google OAuth.

### The full corpus


