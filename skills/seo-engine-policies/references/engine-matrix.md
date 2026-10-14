# Engine matrix — 21 engines × 18 violation classes

## Contents

- How to read
- Matrix
- Coverage summary

## How to read

Legend: **Y** = prohibited/controlled and documented (cite the engine page's §5/§8 row with the same ID) · **N** = the engine's documents explicitly allow it · **—** = not addressed in the engine's documents · **?** = unclear, see that page's §11 · **2°** = documented-secondary only. Class names and definitions: [policy-taxonomy.md](policy-taxonomy.md). A cell is derived from the page row; it never fills one engine's gap with another engine's rule. All pages last_verified 2026-10-11. Gemini/AIO classes 1–16 are Google's spam policies applied to «generative AI responses in Google Search», i.e. AI Overviews and AI Mode (google-ai §5 note). They do **not** cover Gemini Apps: no Gemini Apps content or spam policy was found in the documents searched, so a Gemini Apps policy question gets "not found", never these Y cells. Gemini Apps' documented control is the Google-Extended token for training and grounding (class 17, google-ai §8).

## Matrix

| Engine (coverage) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Google (COMPLETE) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Gemini/AIO (1–16: AI Overviews, AI Mode only) (COMPLETE) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Bing (COMPLETE) | Y | Y | — | Y | Y | Y | Y | — | Y | — | — | — | — | Y | Y | — | Y | Y |
| Copilot (COMPLETE) | Y | Y | — | Y | Y | Y | Y | — | Y | — | — | — | — | Y | Y | — | Y | Y |
| DuckDuckGo (ABSENT-SEARCHED) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Y | Y |
| Ecosia (ABSENT-SEARCHED) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Yahoo (ABSENT-SEARCHED) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Qwant (PARTIAL) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Y | — |
| Yandex (PARTIAL) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | — | — | — | Y | Y | Y | Y | — |
| Baidu (PARTIAL) | — | Y | — | Y | — | — | Y | Y | Y | Y | — | Y | — | Y | — | Y | Y | — |
| Naver (COMPLETE) | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | — | Y | Y | — | Y | Y | Y |
| Seznam (COMPLETE) | Y | Y | Y | Y | Y | Y | — | Y | Y | — | — | — | — | Y | — | Y | Y | — |
| Brave (ABSENT-SEARCHED) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Y | — |
| OpenAI (ABSENT-SEARCHED) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Y | Y |
| Perplexity (ABSENT-SEARCHED) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Y | Y |
| Anthropic (ABSENT-SEARCHED) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Y | Y |
| Apple (COMPLETE) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Y | Y |
| Common Crawl (COMPLETE) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Y | — |
| Meta (COMPLETE) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Y | Y |
| ByteDance (ABSENT-SEARCHED) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Amazon (COMPLETE) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | Y | Y |

## Coverage summary

- COMPLETE: 10 — Google, Gemini/AIO, Bing, Copilot, Naver, Seznam, Apple, Common Crawl, Meta, Amazon
- PARTIAL: 3 — Qwant, Yandex, Baidu
- ABSENT-SEARCHED: 8 — DuckDuckGo, Ecosia, Yahoo, Brave, OpenAI, Perplexity, Anthropic, ByteDance
- INCOMPLETE: 0 — none

Goal coverage (computed from the states, PLAN §7.5): 21 of 21 engines covered (COMPLETE/PARTIAL/ABSENT-SEARCHED), 0 INCOMPLETE under a scope exception.
