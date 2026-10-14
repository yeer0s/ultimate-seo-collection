# Microsoft Copilot — policies, enforcement, controls
> last_verified: 2026-10-11 · market relevance: global; Copilot and Bing AI answers grounded in the Bing index · doc languages: en · coverage: COMPLETE · scope_exception: none

## Contents
- 1. Who uses this index
- 2. Primary documents
- 3. Crawlers and verification
- 4. Webmaster tools and submission
- 5. What is prohibited
- 6. Enforcement
- 7. Detection and recovery
- 8. AI-use controls
- 9. Delta from Google
- 10. Practitioner layer
- 11. Unverified
- Sources

## 1. Who uses this index
- Copilot grounds on the Bing index: «Bing and Copilot search experiences rely on the same core crawling, indexing, and ranking foundation as traditional search.» {b-guidelines} [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]
- AI Performance reports citations across Microsoft Copilot, AI summaries in Bing and select partner integrations [documented: https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview, 2026-10-11].
- Search rules: `bing.md`. Prompt injection fits no class: extra class in §6.

## 2. Primary documents
| Document | URL | Language | Fetched | Governs |
|---|---|---|---|---|
| Bing Webmaster Guidelines | https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a | en | 2026-10-11 | grounding rules, abuse |
| Robots meta tags | https://www.bing.com/webmasters/help/robots-meta-tags-and-attributes-that-bing-supports-5198d240 | en | 2026-10-11 | Copilot directives |
| Bing Chat controls 2023-09-22 | https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat | en | 2026-10-11 | NOCACHE/NOARCHIVE |
| AI Performance 2026-02-10 | https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview | en | 2026-10-11 | citation report |
| AI Visibility Insights 2026-06-16 | https://blogs.bing.com/search/June-2026/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare | en | 2026-10-11 | citation report |
| Google AI features (§9) | https://developers.google.com/search/docs/appearance/ai-features | en | 2026-10-11 | baseline |

## 3. Crawlers and verification
- Crawlers and verification: see `bing.md` §3 (Copilot grounds on the Bing index, §1).
- «Bing respects all content owner preferences expressed through robots.txt and other supported control mechanisms.» {b-blog-2026-02-aiperf} [documented: https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview, 2026-10-11]

## 4. Webmaster tools and submission
- AI Performance (public preview, 2026-02-10): Total Citations, Average Cited Pages, Grounding queries (a sample), page-level citations, trends; IndexNow advised for freshness [documented: https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview, 2026-10-11].
- AI Visibility Insights (preview, 2026-06-16): Intents, Topics, Citation Share (your % of citations for a grounding query; no competitor domains), Compare [documented: https://blogs.bing.com/search/June-2026/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare, 2026-10-11].

## 5. What is prohibited
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 1 | Cloaking | «serving materially different experiences to crawlers and visitors» {b-guidelines} | Abuse list | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |
| 2 | Consolidate Duplicate URLs (nearest) | «reduce Bing’s confidence in selecting a URL for grounding results or citations» {b-guidelines} | Guidelines §6 | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |
| 3 | — | not addressed | — | — |
| 4 | Artificially Engineered Language | «not to manipulate ranking systems or trigger citations or AI responses» {b-guidelines} | Abuse list | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |
| 5 | Link Schemes and Artificial Promotion | «Manipulating inbound links to inflate authority violates guidelines.» {b-guidelines} | Abuse list | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |
| 6 | Automatically Generated Content at Scale | «often lacks usefulness, accuracy, and originality, and may be excluded from indexing» {b-guidelines} | Abuse list | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |
| 7 | Scraped or Republished Content | «Copying content from other sites without adding original value» {b-guidelines} | Abuse list | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |
| 8 | — | not addressed | — | — |
| 9 | Malicious Behavior | «phishing, malware distribution, or other harmful activities risk demotion or removal» {b-guidelines} | Abuse list | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |
| 10 | — | not addressed | — | — |
| 11 | — | not addressed | — | — |
| 12 | — | not addressed | — | — |
| 13 | — | not addressed | — | — |
| 14 | Thin, ad heavy, or affiliate-only URLs | «may lose ranking eligibility and grounding visibility» {b-guidelines} | Guidelines §11 | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |
| 15 | Misleading Structured Data | «Markup must accurately reflect visible content.» {b-guidelines} | Guidelines §14 | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |
| 16 | — | not addressed | — | — |

## 6. Enforcement
- Scope: «The following practices reduce ranking eligibility and grounding visibility, across Bing and Copilot experiences» {b-guidelines} [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]
- Effects include «suppressed grounding visibility, loss of grounding eligibility» {b-guidelines} [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]
- Extra class, Prompt Injection and AI Manipulation: «content designed to manipulate or interfere with language models used by Bing or Copilot may result in reduced visibility» {b-guidelines} [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]
- Site-owner notification of a grounding action: unverified [unverified: no channel in the read docs]; see §11.

## 7. Detection and recovery
- «Site owners can contact support through Bing Webmaster Tools if action was taken in error» {b-guidelines} [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]
- AI Performance helps «Validate which pages are already being used as references in AI answers.» {b-blog-2026-02-aiperf} [documented: https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview, 2026-10-11]
- Citation Share «is designed as an observational metric – not a ranking system or a competitive scoreboard» {b-blog-2026-06-aivis} [documented: https://blogs.bing.com/search/June-2026/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare, 2026-10-11]

## 8. AI-use controls
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 17 | NOINDEX | «Use NOINDEX when a URL should NOT appear in Bing search, Copilot experiences, or grounding API results.» {b-guidelines} | Guidelines §10 | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |
| 18 | NOARCHIVE; NOCACHE | «NOARCHIVE prevents content from being used in Copilot responses and grounding results.» «NOCACHE limits Copilot to using only the URL, title, and snippet» {b-guidelines} | Guidelines §10 | [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11] |

- nocache: «Display only URL/Snippet/Title in Chat or Copilot.» noarchive: «Do not link in Chat and Copilot.» {b-robots-meta} [documented: https://www.bing.com/webmasters/help/robots-meta-tags-and-attributes-that-bing-supports-5198d240, 2026-10-11]
- «avoid using NOCACHE on content intended for Copilot or grounding experiences» {b-guidelines}; NOSNIPPET «may limit Copilot citation quality» {b-guidelines} [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11]
- Paywalls: «we recommend adding the NOCACHE value to the NOARCHIVE value» {b-blog-2023-09-chat} [documented: https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat, 2026-10-11]

## 9. Delta from Google
- Google: AI features need no extra optimisation, controls are Googlebot robots.txt, snippet rules and Google-Extended [documented: https://developers.google.com/search/docs/appearance/ai-features, 2026-10-11]. Bing: grounding-specific guidance (one topic per URL, key facts early) and NOARCHIVE/NOCACHE for Copilot [documented: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a, 2026-10-11].

## 10. Practitioner layer
- None in the corpora (engine-corpus-items.md: microsoft-copilot 0).

## 11. Unverified
- Site-owner notification of a grounding action [unverified: the read docs name no notice for grounding or Copilot penalties].

## Sources
- https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a — Bing Webmaster Guidelines, fetched 2026-10-11, saved as phase-2 sources/bing/b-guidelines.raw
- https://www.bing.com/webmasters/help/robots-meta-tags-and-attributes-that-bing-supports-5198d240 — Robots meta tags, fetched 2026-10-11, saved as phase-2 sources/bing/b-robots-meta.raw
- https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat — Bing Chat controls, fetched 2026-10-11, saved as phase-2 sources/bing/b-blog-2023-09-chat.raw
- https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview — AI Performance, fetched 2026-10-11, saved as phase-2 sources/microsoft-copilot/b-blog-2026-02-aiperf.raw
- https://blogs.bing.com/search/June-2026/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare — AI Visibility Insights, fetched 2026-10-11, saved as phase-2 sources/microsoft-copilot/b-blog-2026-06-aivis.raw
- https://developers.google.com/search/docs/appearance/ai-features — Google: AI features and your website, fetched 2026-10-11, saved as phase-2 sources/google-ai/gai-ai-features.raw
