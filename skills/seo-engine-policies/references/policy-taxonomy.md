# Policy taxonomy — the 18 violation classes

## Contents

- How to use the classes
- The 18 classes
- Sources

## How to use the classes

Every engine page maps the engine's own wording onto these classes and quotes the engine's term beside ours, so pages compare cell by cell. "Not addressed" is a recorded answer: it means the engine's documents read on the page's `last_verified` date do not mention the class. It is never filled from Google or from another engine. Classes 1–16 are a page's §5 (what is prohibited); 17–18 are its §8 (AI-use controls). The matrix (`engine-matrix.md`) shows one cell per engine and class. A class names a topic, not a verdict: whether a practice violates depends on the engine's own definition, conditions and exceptions on its page (e.g. Google: cloaking needs intent to manipulate rankings and mislead users, and a paywall is exempt only if Google can see its full content and the site follows Google's Flexible Sampling guidance; expired-domain abuse needs little-to-no-value content; copying, paraphrasing or AI use alone is not the test).

## The 18 classes

| ID | Class | Covers (one line) | Page section |
|---|---|---|---|
| 1 | Cloaking | different content for crawlers than for users, to deceive | §5 |
| 2 | Doorway / gateway pages | many near-identical pages or domains built to rank and funnel | §5 |
| 3 | Hidden text and links | text or links invisible to users but present for crawlers | §5 |
| 4 | Keyword stuffing | repeating terms to manipulate relevance | §5 |
| 5 | Link schemes | buying/selling links, link exchanges, PBNs, manipulative anchor networks | §5 |
| 6 | Scaled / auto-generated content | mass-produced pages with little value, incl. the engine's stance on AI-generated content | §5 |
| 7 | Scraped / copied content | republishing others' content without added value | §5 |
| 8 | Sneaky redirects | redirecting users somewhere other than what crawlers saw | §5 |
| 9 | Malware, phishing, unwanted software | harmful downloads, deceptive installs, credential theft | §5 |
| 10 | Hacked content | content injected by a third party without the owner's consent | §5 |
| 11 | User-generated spam | spam posted by users in comments, forums or profiles | §5 |
| 12 | Site reputation abuse / parasite hosting | third-party pages riding a host site's signals | §5 |
| 13 | Expired-domain abuse | buying expired domains to reuse their signals for low-value content | §5 |
| 14 | Thin affiliate / no added value | affiliate or aggregated pages adding nothing original | §5 |
| 15 | Structured-data / review spam | misleading markup, fake or self-serving reviews | §5 |
| 16 | Click or behaviour manipulation | CTR bots, misleading UX, back-button hijacking | §5 |
| 17 | Crawler access & directive handling | robots.txt dialect, meta robots, X-Robots-Tag, IndexNow | §8 |
| 18 | AI-use controls | training opt-out, answer/grounding opt-out, snippet limits | §8 |

A row on an engine page is: the class ID, the engine's own term (original language and translation), a quote of at most 25 words from the engine's document, the document reference, and a dated label. Coverage states per engine (COMPLETE, PARTIAL, ABSENT-SEARCHED, INCOMPLETE) are defined in the skill's SKILL.md and the plan's §7.5.

## Sources

- Class list and definitions: the phase-2 build plan (PLAN round 6, §7.1a). The Google examples under "How to use" restate google §5 rows 1 and 13 and the QRG note in google-updates-timeline; no other engine claim is made here.
