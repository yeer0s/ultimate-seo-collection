# Google AI features (Gemini/AIO) — policies, enforcement, controls
> last_verified: 2026-10-11 · market relevance: global · doc languages: en · coverage: COMPLETE · scope_exception: none

## Contents
- §1 Users · §2 Documents · §3 Crawlers · §4 Tools · §5 Prohibited · §6 Enforcement · §7 Recovery · §8 AI controls · §9 Delta · §10 Practitioner · §11 Unverified · Sources

## 1. Who uses this index

One owner, "Gemini/AIO": AI Overviews, AI Mode and generative AI in Discover (Googlebot + the GSC control), and Gemini Apps / Vertex AI (the Google-Extended token).
- Rules: AIO / AI Mode eligibility runs on Googlebot crawling and indexing; Google-Extended governs Gemini/Vertex use, not Search inclusion; of the snippet controls, nosnippet and max-snippet also limit direct AI input (§8).
- GSC control (outcome GSC: A): §8 class 18.

## 2. Primary documents

| Document | URL | Language | Fetched | Governs |
|---|---|---|---|---|
| AI features | https://developers.google.com/search/docs/appearance/ai-features | en | 2026-10-11 | eligibility |
| AI optimization guide | https://developers.google.com/search/docs/fundamentals/ai-optimization-guide | en | 2026-10-11 | GSC gate, myths |
| Common crawlers (canonical) | https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers | en | 2026-10-11 | Google-Extended |
| Gen-AI content | https://developers.google.com/search/docs/fundamentals/using-gen-ai-content | en | 2026-10-11 | AI content |
| GSC AI control | https://support.google.com/webmasters/answer/16908024 | en | 2026-10-11 | control |
| GSC AI report | https://support.google.com/webmasters/answer/16984139 | en | 2026-10-11 | measurement |
| Robots meta tag | https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag | en | 2026-10-11 | snippets |
| Spam policies | https://developers.google.com/search/docs/essentials/spam-policies | en | 2026-10-11 | spam |
| Doc updates | https://developers.google.com/search/updates | en | 2026-10-11 | changes |

## 3. Crawlers and verification

- Googlebot preferences affect Google Search "including Discover and all Google Search features". Google-Extended has no user-agent string of its own; its robots.txt token works "in a control capacity". UA strings can be spoofed; verify by IP and rDNS. [documented: https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers, 2026-10-11]

## 4. Webmaster tools and submission

- Search Console: Settings › Search generative AI, and the Generative AI performance report (AI Overviews, AI Mode), both rolled out worldwide 2026-08-31. [documented: https://support.google.com/webmasters/answer/16984139, 2026-10-11]
- AI traffic also counts in the Performance report ("Web"); no AI text files, special markup or schema.org are needed. [documented: https://developers.google.com/search/docs/appearance/ai-features, 2026-10-11]

## 5. What is prohibited

| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 1 | Cloaking | — | — | [documented: https://developers.google.com/search/updates, 2026-10-11] |
| 2 | Doorway abuse | — | — | [documented: https://developers.google.com/search/updates, 2026-10-11] |
| 3 | Hidden text and link abuse | — | — | [documented: https://developers.google.com/search/updates, 2026-10-11] |
| 4 | Keyword stuffing | — | — | [documented: https://developers.google.com/search/updates, 2026-10-11] |
| 5 | Link spam | — | — | [documented: https://developers.google.com/search/updates, 2026-10-11] |
| 6 | scaled content abuse (AI-generated pages) | «generative AI tools or other similar tools to generate many pages without adding value for users may violate Google's spam policy on scaled content abuse» {gai-gen-ai-content} | Gen-AI content, intro | [documented: https://developers.google.com/search/docs/fundamentals/using-gen-ai-content, 2026-10-11] |
| 7 | Scraping | — | — | [documented: https://developers.google.com/search/updates, 2026-10-11] |
| 8 | Sneaky redirects | — | — | [documented: https://developers.google.com/search/updates, 2026-10-11] |
| 9 | Malicious practices | — | — | [documented: https://developers.google.com/search/updates, 2026-10-11] |
| 10 | Hacked content | — | — | [documented: https://developers.google.com/search/updates, 2026-10-11] |
| 11 | User-generated spam | — | — | [documented: https://developers.google.com/search/updates, 2026-10-11] |
| 12 | Site reputation policy | — | — | [documented: https://developers.google.com/search/updates, 2026-10-11] |
| 13 | Expired domain abuse | — | — | [documented: https://developers.google.com/search/updates, 2026-10-11] |
| 14 | Thin affiliation | — | — | [documented: https://developers.google.com/search/updates, 2026-10-11] |
| 15 | structured data in AI-generated content | «For structured data, also ensure compliance with the general guidelines, the specific policies for the individual search features» {gai-gen-ai-content} | Focus on accuracy | [documented: https://developers.google.com/search/docs/fundamentals/using-gen-ai-content, 2026-10-11] |
| 16 | Back button hijacking | — | — | [documented: https://developers.google.com/search/updates, 2026-10-11] |

- Rows with no quote: 2026-05-15 «our spam policies also apply to generative AI responses in Google Search» {g-search-updates}: each row = the same-ID google §5 row, for AIO and AI Mode [documented: https://developers.google.com/search/updates, 2026-10-11]

## 6. Enforcement

- Spam includes «attempting to manipulate generative AI responses in Google Search» {g-spam} [documented: https://developers.google.com/search/docs/essentials/spam-policies, 2026-10-11]
- Fan-out pages: «doing so primarily to manipulate rankings or generative AI responses in Google Search violates Google's scaled content abuse spam policy» {gai-optimization-guide} [documented: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide, 2026-10-11]

## 7. Detection and recovery

- «The generative AI performance report shows data about how your site performs in generative AI features on Google Search»; if absent, «This may be because you've excluded your site» {gai-gsc-report} [documented: https://support.google.com/webmasters/answer/16984139, 2026-10-11]
- Preview control ignored: «use the URL Inspection tool to see the HTML that Googlebot received»; «crawling can take anywhere from several days to several months» {gai-ai-features} [documented: https://developers.google.com/search/docs/appearance/ai-features, 2026-10-11]
- «Content will be excluded within 1-2 days after the control goes live» {gai-gsc-control} [documented: https://support.google.com/webmasters/answer/16908024, 2026-10-11]

## 8. AI-use controls

| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 17 | Googlebot robots.txt (Search, AIO, AI Mode); Google-Extended token (Gemini/Vertex, not Search) | «robots.txt directives for Googlebot is the control» {gai-ai-features} · «Google-Extended does not impact a site's inclusion in Google Search nor is it used as a ranking signal» {gai-common-crawlers-a} | AI features; Common crawlers | [documented: https://developers.google.com/search/docs/appearance/ai-features, 2026-10-11] [documented: https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers, 2026-10-11] |
| 18 | Search generative AI control: include (default) / exclude / inherit from parent | «this control isn't used as a ranking or inclusion signal affecting other parts of Search» · «This control doesn't affect AI training» {gai-gsc-control} | GSC Help › exclude | [documented: https://support.google.com/webmasters/answer/16908024, 2026-10-11] |

- Eligibility: «a page must be indexed and eligible to be shown in Google Search with a snippet» {gai-ai-features} [documented: https://developers.google.com/search/docs/appearance/ai-features, 2026-10-11]
- And: «a site must be included in Search generative AI features in Search Console to be eligible for display» {gai-optimization-guide} [documented: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide, 2026-10-11]
- Exclude: «Content crawled from your site won't be eligible to be used as an input to generate an AI response»; training: «to limit training of the models used to generate responses in Search generative AI features, use Google-Extended» {gai-gsc-control} [documented: https://support.google.com/webmasters/answer/16908024, 2026-10-11]
- Google-Extended: «manage whether content Google crawls from their sites may be used for training future generations of Gemini models» {gai-common-crawlers-a} [documented: https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers, 2026-10-11]
- Display limits: «use nosnippet, data-nosnippet, max-snippet, or noindex controls» {gai-ai-features} [documented: https://developers.google.com/search/docs/appearance/ai-features, 2026-10-11]
- nosnippet «will also prevent the content from being used as a direct input for AI Overviews and AI Mode»; max-snippet «will also limit how much of the content may be used as a direct input» {gai-robots-meta} [documented: https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag, 2026-10-11]

## 9. Delta from Google

- No separate AI spam policy found; Google's covers AIO, AI Mode (§5). [documented: https://developers.google.com/search/updates, 2026-10-11]
- Extra gate: the GSC control (§8). [documented: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide, 2026-10-11]
- Extra token: Google-Extended, not a Search signal (§8 row 17). [documented: https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers, 2026-10-11]

## 10. Practitioner layer

- Google's generative AI features still require a crawled, indexed, snippet-eligible page. [practitioner: anonymised sources · consensus · 2 thr / 236 · newest 2026-05]
- Track AI visibility with a fixed prompt set incl. Gemini and AI Overviews. [practitioner: anonymised sources · consensus · 5 thr / 54 · newest 2026-08]

## 11. Unverified

- AI-specific manual action or notice: none named in the docs read [unverified: no primary text]
- Folklore that blocking the Google-Extended token removes a site from AI Overviews: contradicted by §8 row 17 [unverified: no Google doc states the folklore]

## Sources

- https://developers.google.com/search/docs/appearance/ai-features — AI features and your website, fetched 2026-10-11, saved as phase-2 sources/google-ai/gai-ai-features.raw
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide — Optimizing for generative AI, fetched 2026-10-11, saved as phase-2 sources/google-ai/gai-optimization-guide.raw
- https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers — Google's common crawlers (canonical), fetched 2026-10-11, saved as phase-2 sources/google-ai/gai-common-crawlers-a.raw (same page at /search/docs/crawling-indexing/google-common-crawlers: copy -b)
- https://developers.google.com/search/docs/fundamentals/using-gen-ai-content — Gen-AI content guidance, fetched 2026-10-11, saved as phase-2 sources/google-ai/gai-gen-ai-content.raw
- https://support.google.com/webmasters/answer/16908024?hl=en — Search generative AI control, fetched 2026-10-11, saved as phase-2 sources/google-ai/gai-gsc-control.raw
- https://support.google.com/webmasters/answer/16984139?hl=en — Generative AI performance report, fetched 2026-10-11, saved as phase-2 sources/google-ai/gai-gsc-report.raw
- https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag — Robots meta tag spec, fetched 2026-10-11, saved as phase-2 sources/google-ai/gai-robots-meta.raw
- https://developers.google.com/search/docs/essentials/spam-policies — Spam policies, fetched 2026-10-11, saved as phase-2 sources/google/g-spam.raw
- https://developers.google.com/search/updates — Documentation updates, fetched 2026-10-11, saved as phase-2 sources/google/g-search-updates.raw
