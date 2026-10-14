<!-- split-header: part 2 of 2 of google-updates-timeline.md (step-3 original lines 57–138; boundary H2) -->
# Google updates timeline (2 of 2) — core and spam rollouts, data-reliability windows, unverified claims
## Contents

- Core and spam updates — for incident classification only
- Data-reliability windows — check these before any before/after
- Unverified — needs a primary source
- The reason the gate exists
- Cross-references
- Attribution
- Sources

Other parts of the same original file: [google-updates-timeline.md](google-updates-timeline.md).

<!-- /split-header -->
## Core and spam updates — for incident classification only

Rollout dates, nothing more. Use them to rule a core update in or out before blaming a deploy. Source for every row without its own blog post: `status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history` (Google's Search Status Dashboard), `last_verified` 2026-09-10.

| Date started | Update | Rollout | Own primary URL if any |
|---|---|---|---|
| 2024-03-05 | March 2024 Core Update | 45 days | status dashboard (Ranking history, read 2026-10-11) |
| 2024-03-05 | March 2024 Spam Update | 14 days 21 h | status dashboard (Ranking history, read 2026-10-11) |
| 2024-06-20 | June 2024 Spam Update | 7 days 1 h | status dashboard (Ranking history, read 2026-10-11) |
| 2024-08-15 | August 2024 Core Update | 19 days 4 h | developers.google.com/search/blog/2024/08/august-2024-core-update · status dashboard (Ranking history, read 2026-10-11) |
| 2024-11-11 | November 2024 Core Update | 23 days 13 h | status dashboard (Ranking history, read 2026-10-11) |
| 2024-12-12 | December 2024 Core Update | 6 days 4 h | status dashboard (Ranking history, read 2026-10-11) |
| 2024-12-19 | December 2024 Spam Update | 7 days 2 h, completed 2024-12-26; Google named no target | status dashboard (Ranking history, read 2026-10-11) |
| 2025-03-13 | March 2025 Core Update | 13 days 21 h | status dashboard (Ranking history, read 2026-10-11) |
| 2025-06-30 | June 2025 Core Update | 16 days 18 h | status dashboard (Ranking history, read 2026-10-11) |
| 2025-08-26 | August 2025 Spam Update | 26 days 15 h | status dashboard (Ranking history, read 2026-10-11) |
| 2025-12-11 | December 2025 Core Update | 18 days 2 h | status dashboard (Ranking history, read 2026-10-11) |
| 2026-03-24 | March 2026 Spam Update | under 1 day | status dashboard |
| 2026-03-27 | March 2026 Core Update | 12 days, completed Apr 8 | status dashboard |
| 2026-05-21 | May 2026 Core Update | completed Jun 2 | status.search.google.com/incidents/wdAXJk6LRRihEjpzEeWE |
| 2026-06-24 | June 2026 Spam Update | Jun 24–26 | status dashboard |
| 2026-08-18 | August 2026 Spam Update | Aug 18–21 | status.search.google.com/incidents/LEubPCm2octf2uMqCFKE |
| 2026-09-24 | September 2026 Spam Update | 13 days 16 h, complete 2026-10-08; global, all languages; **no target named** | https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history (Ranking history, read 2026-10-11) · https://status.search.google.com/incidents/XhUDXP7A67iHCD2kmbVu |

## Data-reliability windows — check these before any before/after

🔴 **GSC impressions, CTR and average position were unreliable from 2025-05-13 to 2026-04-27.** A logging error; **clicks were unaffected**; after the fix Google says you may notice a decrease in impressions, an artefact, not a regression. **Any before/after spanning that window is not comparable on those three metrics** — restrict the comparison to clicks, or move both windows to one side of 2026-04-27. `[documented: https://support.google.com/webmasters/answer/6211453, 2026-10-12]`

⚠️ **GA4 "AI Assistant" default channel is not total AI traffic.** It covers sources like ChatGPT, Gemini, Deepseek, Copilot or Grok (`medium=ai-assistant`, set when the referrer matches Google's list of AI assistants) and **excludes** Google AI Overviews and AI Mode, which count under Organic Search. Never present this channel as total AI traffic. `[documented: https://support.google.com/analytics/answer/9756891, 2026-10-12]`

GA4 AI Assistant channel gaps: unverified [unverified: launch date, Claude as a listed source, Referral/Direct leakage and no backfill are not on the saved channel-group page]; see ## Unverified.

⚠️ **GSC API country codes are ISO 3166-1 alpha-3** (3-letter), and `byProperty` aggregation is not supported for `type=discover` or `type=googleNews`. `[documented: https://developers.google.com/webmaster-tools/v1/searchanalytics/query, 2026-10-12]`

GSC lag, retention and Discover dimensions: unverified [unverified: 2–3 day lag, ~16 months history, and no query or position for discover and googleNews are not on the saved Search Analytics query page]; see ## Unverified.

⚠️ **EU before/after across the DMA date (2024-03-07 `[memory]`) or a consent-mode change: check before comparing.** Compare CTR or GA4 organic only if the consent setup and measurement were the same in both windows; otherwise compare clicks, or keep both windows on one side of the change `[unvalidated house heuristic]`. Consent mode v2 added `ad_user_data` and `ad_personalization` `[documented: https://developers.google.com/tag-platform/security/guides/consent, 2026-10-12]`. No saved primary source states the DMA date or a CTR effect; see skill `seo-technical` › google-apis-and-quotas § DMA and Consent Mode v2 — the EU measurement boundary. Procedure: skill `seo-evidence` › experiments-and-revert-2.

## Unverified — needs a primary source

Each of these is *probably* true and is **not usable in a report** until a Google-owned URL is attached. Promote a row into the table above only when you have fetched the primary source yourself. Promoted on 2026-10-14 after re-reading the saved copies: the sitelinks search box removal (now a dated row in [google-updates-timeline.md](google-updates-timeline.md)), the GSC logging-error window (the documented paragraph above) and the Bing AI Performance post URL.

| Claim | Where it came from | Primary source to check | Status |
|---|---|---|---|
| GA4 "AI Assistants" channel group, live **~2026-05-13** | `claude-seo@skills/seo-google/SKILL.md:199` — the date is approximate in the source itself | support.google.com/analytics — default channel group definitions | Cite the behaviour, not the date |
| CrUX experimental ad metrics (ad count, density, weight), **2026-09-15** — **not Core Web Vitals, no thresholds** | `claude-seo@data/google-updates.json` (cites developer.chrome.com/blog/crux-ad-metrics); A02 row check 2026-10-11: no saved official page states it | https://developer.chrome.com/blog/crux-ad-metrics | `[unverified: no official page read on 2026-10-11 confirms the row]` Do not report them as CWV |
| "SAFE" (from Google's paper *The Synthetic Gap*) is a Search system and part of the September 2026 spam update | `claude-seo@data/google-updates.json` unverified list (status at 2026-09-28) | Search Status Dashboard incident or developers.google.com | `[unverified: no Google Search source; the paper is about YouTube channel-cluster forensics and never mentions Search]` **Never encode SAFE as a Search ranking system.** |
| The September 2026 spam update does not target link spam | `claude-seo@data/google-updates.json` unverified list — third-party assertion | A Google quote on the incident page | `[unverified: no Google quote]` **Do not tell clients links are unaffected.** |
| Sept 25–27 volatility (Semrush Sensor 9.4/10) caused by the spam update | `claude-seo@data/google-updates.json` unverified list — vendor reading | none possible (vendor sensor) | `[vendor]` Context only while the update was rolling out |
| A "September 2026 Authority Signals Update" | `claude-seo@data/google-updates.json` unverified list | Search Status Dashboard | `[unverified: refuted — no Search Status Dashboard incident]` Do not cite |
| Google moved JSON-LD extraction to single-pass HTML unescaping (double-escaped entities no longer unrolled) | `claude-seo@data/google-updates.json` unverified list — SER cites a LinkedIn post | developers.google.com entry | `[unverified: no developers.google.com entry]` Hold. Worth a defensive test: never double-escape JSON-LD |
| AI Overview links opening AI Mode, AI Mode search-bar button, new goto parameters | `claude-seo@data/google-updates.json` unverified list — SERP tests | Google documentation | `[unverified: SERP tests, no Google documentation]` Exclude |

- GA4 AI Assistant channel gaps: the channel went live ~2026-05-13, recognises Claude among its sources, leaves unsupported sources in Referral and referrer-less AI sessions in Direct, and is forward-only with no backfill [unverified: launch date, Claude as a listed source, Referral/Direct leakage and no backfill are not on the saved channel-group page]
- GSC lag, retention and Discover dimensions: GSC data has a 2–3 day lag and ~16 months of history; `discover` and `googleNews` support neither the `query` dimension nor the `position` metric [unverified: 2–3 day lag, ~16 months history, and no query or position for discover and googleNews are not on the saved Search Analytics query page]

`[practitioner]` The source file's own `unverified[]` array is **empty** — every one of its 42 entries carries a Google-owned URL, enforced by its stated policy: *"Every entry must cite a Google-owned URL. Third-party-only claims belong in unverified[]."* That is the gate worth copying, and this file's Unverified section exists because applying the gate honestly to items *outside* that file produced them.

## The reason the gate exists

`[practitioner]` The source repo records a release whose entire "Fixed (fact accuracy)" section is self-correction after re-confirming every time-sensitive Google claim against primary sources: an invented **E-E-A-T 20/25/25/30 weighting** relabelled as the plugin's own model because *"Google publishes no numeric E-E-A-T weights"*; **"FID was never in Lighthouse"** removed from seven files; **QAPage is not the FAQ replacement** reworded; a deprecation date corrected 2025-06-19 → 2025-06-12; a January-2026 tooling sunset over-generalised from Practice Problems to all retired types and re-scoped; and a **dead citation** (HTTP 404) repointed to the real post.

⚠️ **Discrepancy with the extraction list.** The topic list attributes to `CHANGELOG.md:487-492` a fabricated *"December 2025 watershed, 71-67-52% drops"* claim shipped and corrected two releases later. **That claim does not exist in the clone** — a repo-wide grep for `watershed` and `71-67-52` returns nothing, and lines 485-493 hold the six corrections quoted above instead. The lesson survives intact and is better evidenced by what is actually there: six dated Google claims in a shipped SEO tool were wrong, including two invented numbers and one URL that 404'd. **Attach the primary URL or leave the row out.**

## Cross-references

- skill `seo-technical` › incident-triage § Classify the incident first — what to do once a date matches a core update.
- skill `seo-evidence` › experiments-and-revert-2 — the before/after procedure these reliability windows constrain.
- skill `seo-evidence` › metadata-at-scale § Answer formatting and SERP features — the live rich-result register; this file supplies the retirement dates behind it.
- skill `seo-technical` › rendering-and-sitemaps — which schemas are worth shipping now.
- skill `seo-ai-search` › ai-crawlers-and-bot-policy — the 2026 AI citation surfaces in operational form.

## Attribution

- AgriciDaniel/claude-seo — Copyright (c) 2026 agricidaniel — MIT License. Dated rows, the September 2026 spam update row, the December 2024 spam correction and the Unverified rows above are carried from its `claude-seo@data/google-updates.json` (via the phase-2 adapted file), lightly condensed.

## Sources

- AgriciDaniel/claude-seo@data/google-updates.json (last_verified 2026-09-28) (phase-2 adapted file research/adapted/AgriciDaniel__claude-seo/google-ledger-and-ai-guide-delta-2026-10.md) — new dated rows 2026-07-29 to 2026-09-24, the September 2026 spam update row (rollout figures replaced by the Search Status Dashboard's, read 2026-10-11), the December 2024 spam update correction, and the Unverified rows; each confirmed row re-checked against a Google page on 2026-10-11 (phase2/sources/A02-CHECK.md). COPY, MIT.
- `claude-seo@data/google-updates.json` (324 lines, 42 entries, `last_verified: 2026-09-10`, `unverified[]` empty) — the shape (date · name · kind · Google-owned source · notes), the citation policy, and the entries carried above. Every row copied here was read from this file; rollout durations and notes are its wording, condensed.
- `claude-seo@skills/seo-google/SKILL.md:133-137` — Generative AI performance report and the GSC logging-error window; the window is now checked against Google's data-anomalies page `[documented: https://support.google.com/webmasters/answer/6211453, 2026-10-14]`.
- `claude-seo@skills/seo-google/SKILL.md:199` — GA4 AI Assistants channel group, recognised sources, exclusions, undercount.
- `claude-seo@skills/seo-google/references/search-console-api.md:63-67` — lag, retention, dimension limits, and the logging-window caution restated at the API layer.
- `claude-seo@skills/seo-schema/references/deprecated-types-2024-2026.md:8-49` — HowTo/FAQ retirement dates and the doc-removal timeline.
- `claude-seo@CHANGELOG.md:485-493` — the fact-accuracy corrections quoted above; the topic list's "watershed" attribution could not be reproduced and is flagged as a discrepancy.
