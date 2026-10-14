# Comparison pages — schema, fairness, and rollout gates
<!-- split-header-2: part 1 of 2 of comparison-pages.md (original lines 1–125; boundary start) -->
<!-- /split-header-2 -->

## Contents

- The four subtypes
- Schema for these pages
- Fairness, and why it is also the SEO position
- Claim audit
- EU legal gates
- Unverified
- Sources

Other parts of the same original file: [comparison-pages-2.md](comparison-pages-2.md).

## The four subtypes

Each has a distinct query shape, so each needs a distinct template `[practitioner]`:

| Subtype | Target query | Structural requirement |
|---|---|---|
| **X vs Y** | `[A] vs [B]`, `[A] vs [B] for [use case]`, `[A] vs [B] pricing` | Balanced feature-by-feature comparison, one stated verdict with its justification |
| **Alternatives to X** | `[A] alternatives`, `best alternatives to [A]` | Per alternative: summary, pros/cons, and an explicit *best for* case |
| **Best [category] roundup** | `best [category] tools [year]`, `top [category] software` | Ranking criteria stated **before** the ranking |
| **Comparison table** | `[category] comparison`, `[category] comparison chart` | Feature matrix; sortable/filterable if interactive |

Title formulas from the source, carried as conventions rather than measured results `[practitioner]`: `[A] vs [B]: [Key Differentiator] ([Year])` · `[N] Best [A] Alternatives in [Year] (Free & Paid)` · `[N] Best [Category] Tools in [Year], Compared & Ranked`. H1 matches the title's intent and stays under ~70 characters.

**On putting a price in the title: do not decide it here.** The evidence — #155 MAINSTREAM (+12% organic sessions, 3 samples / 2 controlled, all searchpilot) for a *dynamic current lowest price*, against #157 AVOID (−15%) and #158 AVOID (−7%) for *static* price strings — and the staleness-guard conditions under which a test is permissible are set out in skill `seo-evidence` › titles-and-serp-tests. Follow that file; nothing here overrides it.

## Schema for these pages

Shapes and required fields are in skill `seo-technical` › schema-reference; the mapping is what matters here `[practitioner]`:

- **Roundups and "alternatives to" lists → `ItemList`** with `itemListElement` of `ListItem` (`position`, `name`, `url`), plus `numberOfItems` and, where the order is meaningful, `itemListOrder`. The marked-up count and order must match what a user sees.
- **Software comparisons → `SoftwareApplication`** with `applicationCategory`, `operatingSystem`, `offers.price`/`priceCurrency`.
- **Product comparisons → `Product`**, optionally with `aggregateRating`.

Three separate rules on `aggregateRating` — keep them apart:

1. **Imported ratings: never mark up.** Google's review-snippet rules say "Don't aggregate reviews or ratings from other websites" `[documented: https://developers.google.com/search/docs/appearance/structured-data/review-snippet, 2026-10-12]`. A G2 or Trustpilot average (for any product, ours or a rival's) shown in the table is cited and linked in the visible copy and left out of the JSON-LD.
2. **Ratings you collected directly** from genuine users, hosted and displayed on the page: the review-snippet page bars aggregating ratings from other websites and "fake or undisclosed incentivized reviews", and names no rule against a rival's product as subject `[documented: https://developers.google.com/search/docs/appearance/structured-data/review-snippet, 2026-10-12]`. That such markup is therefore allowed for a competitor's product is our reading, not a stated permission `[hypothesis]`.
3. **Self-serving reviews** are a narrower rule: a local business or organisation that controls the reviews about itself is ineligible for star review markup on its own `LocalBusiness`/`Organization` pages `[documented: https://developers.google.com/search/docs/appearance/structured-data/review-snippet, 2026-10-12]`. It is about reviewing yourself, not about naming a competitor.

**Comparison-portal mapping** — for a site that lists offers it does not sell (the Mowei class) `[practitioner]`; eligibility rules in skill `seo-technical` › schema-reference:

| Page content | Markup | Never |
|---|---|---|
| Listings of offers we do not sell | `ItemList` of `Offer` / `FinancialProduct` | `Product` marked up as if we were the merchant |
| Published price/tariff tables | `Dataset` (read by Dataset Search; never a Search rich result) | — |
| Third-party ratings shown in the table | none (cite in visible copy) | `AggregateRating` built from them — ratings aggregated from other websites (rule 1 above); Mowei removed it by editorial decision |
| Any page | `dateModified` only when the content really changed | a bumped date with no change (a false statement); weekly LLM "freshness" rewrites are refused |

`FAQPage` is no longer a SERP play — rich results were fully retired **7 May 2026** (skill `seo-technical` › schema-reference). Comparison-page FAQ *content* still earns its place for comprehension and for answer-engine liftability; the markup does not.

## Fairness, and why it is also the SEO position

The source's guidelines `[practitioner]`, reordered by how often they fail:

- **Every competitor claim verifiable from a public source** — test the feature where possible, cite the documentation otherwise, and link the source per data point.
- **"As of [date]" on every price**, plus a visible *last updated* timestamp. Stale competitor pricing is the most common and most damaging defect on these pages: it is simultaneously a credibility failure and, where it flatters your own product, a misleading-comparison risk.
- **Disclose which product is yours.** Non-negotiable, and it should be visible without scrolling.
- **Acknowledge competitor strengths honestly.** A comparison where the author wins every row reads as marketing and converts like marketing.
- **No defamation** — no false or misleading claim about a competitor.
- **Review quarterly, and whenever a competitor ships a major change.**
- **Methodology disclosure** — how the comparison was conducted, who conducted it, what was tested.

### Evidence rules for every competitor fact

`[practitioner]` The test: each public statement about another company has to hold up when that company's own team reads it.

- **Absent from their page is not absent from their product.** A feature missing from a pricing page tells you about the page. Write "not listed on their pricing page (as of 2026-03)" or drop the row; a ✗ is allowed only when documentation or a hands-on test confirms the absence.
- **Put a date on every competitor fact**, both in the table and in the data file, and re-verify before republishing.
- **A single visit is a snapshot.** Saying something has been "unchanged for years" requires dated history (changelog, archived copies).
- **Report what changed, never why** — a motive is a guess unless the competitor stated it publicly.
- **Keep three layers separate:** what their site says / what that means for the buyer / what we recommend.
- **Do not guess which competitor is meant.** If the request names none, ask; never draft around the most likely candidate.
- **One source of truth per competitor** — a single record holding positioning, every price tier, features, strengths and weaknesses, best-for, review themes and as-of dates. Each page is rendered from that record, so one correction reaches every page.

Naming competitors `[practitioner]` (not legal advice): the source frames this as US "nominative fair use", which generally lets a comparison use a rival's brand name to refer to that rival but never to imply endorsement or affiliation, and never shields a false or unverifiable claim. **That doctrine is not the test for an EU site** — what binds a Portuguese comparison page is the instrument list in [EU legal gates](#eu-legal-gates) below. Trademark law differs by jurisdiction either way; a comparison programme at scale gets counsel before launch, not after the first letter.

## Claim audit

`[practitioner]` Run before any republish and at the quarterly review.

1. List every claim about a competitor, with the asset and line where it appears.
2. Re-check each one against the competitor's current site, documentation or changelog, and record the date checked. Without browsing access, mark the claim *unchecked* and list what needs verifying. A claim is never marked Current without a date.
3. Assign one state:

| State | Meaning | Action |
|---|---|---|
| **Current** | still true | refresh source and date |
| **Changed** | now wrong | record what the competitor says now; correct the page |
| **Unverifiable** | sourced once; nothing current confirms or refutes it | soften to "not listed (as of date)" or remove |
| **Overclaimed** | asserted with no source (unconfirmed ✗, guessed motive, unevidenced "why we win") | rewrite to the evidence or remove |

4. Fix order: public pages first, then anything said on calls, then internal documents; correct shared facts in the competitor's source of truth.
5. Report: assets audited, claims checked, count per state, and the fix list with replacement wording.

A price on a live page that is *Overclaimed* or *Changed* is, for a regulated comparison platform, a misleading-comparison exposure too: it goes through the positioning/claims gate as well as the SEO backlog.

## EU legal gates

The instruments below were checked against EUR-Lex by the source skill on 2026-08-27; only the two application dates were re-checked against saved EUR-Lex texts on 2026-10-11 `[documented: https://eur-lex.europa.eu/eli/dir/2024/825/oj/eng, 2026-10-11]` `[documented: https://eur-lex.europa.eu/eli/dir/2023/2225/oj/eng, 2026-10-11]`. Not legal advice. The fairness list above is good practice; on an EU comparison site these instruments turn parts of it into law. Any ranking, title, snippet or "best" claim that breaches a row is refused, whatever its SEO upside.

| Instrument | What it binds on a comparison URL |
|---|---|
| **P2B Reg. (EU) 2019/1150 Art. 5** | P2B Art. 5 ranking-parameter duty: unverified [unverified: EUR-Lex text not readable by curl on 2026-10-12]; see ## Unverified. A "Recomendado" badge or a pre-selected default depends on this. The **methodology page discharges the duty** — and it must match the ranking code actually running, at every rollout percentage (a ranking flag is a compliance event, not a test). |
| **UCPD 2005/29/EC as amended by the Omnibus Dir. (EU) 2019/2161** | UCPD and Omnibus ranking and review rules: unverified [unverified: EUR-Lex texts not readable by curl on 2026-10-12]; see ## Unverified. A savings claim in a title or meta description must be quantified, sourced and reproducible. |
| **DSA Reg. (EU) 2022/2065 Arts. 25, 27** | DSA Arts. 25 and 27 duties: unverified [unverified: EUR-Lex text not readable by curl on 2026-10-12]; see ## Unverified. Whether a comparison portal qualifies is open (see Unverified) — design to the standard anyway. |
| **Dir. (EU) 2024/825** (empowering consumers for the green transition) | Art. 4(1): transposition by 27 March 2026; Member States "shall apply those measures from 27 September 2026" — **in force now**. Annex I points added to the UCPD: a generic environmental claim ("sustentável") is banned unless the trader can demonstrate recognised excellent environmental performance relevant to the claim (4a); an offset-based neutral/reduced-emissions product claim ("carbono neutro") is banned (4c); a sustainability label must be based on a certification scheme (third-party monitored) **or** established by public authorities (2a) `[documented: https://eur-lex.europa.eu/eli/dir/2024/825/oj/eng, 2026-10-11]`. Audit every "energia verde" title, H1, badge and schema `description`. |
| **CCD2 Dir. (EU) 2023/2225** | Art. 48(1): transposition by 20 November 2025; Member States "shall apply those measures from 20 November 2026" (the same date Directive 2008/48/EC is repealed, Art. 47). The date is set in the Directive, so late transposition does not move it. Credit advertising: TAEG plus a representative example alongside any rate or saving figure — titles and meta descriptions included. Re-check Portuguese transposition before the date. |
| **Vertical regulators (PT)** | Credit: DL 81-C/2017 intermediary regime (capturing leads = intermediation exposure). Insurance: IDD / ASF (proposing a product can be distribution). Energy: ERSE comparator conduct. Telecom: EECC Art. 103 / ANACOM certification of independent comparison tools. Investment: the MiFID II boundary — no advice, no loss-framing. Regime details: see Unverified. |

**Gate in the audit** `[practitioner]`: a finding names the instrument it touches — never just "legal risk". Rows with a deadline stay in every audit's shortlist reasoning until they pass.

### Legal gate before a precise number (credit, insurance, investment)

(CCD2 Dir. (EU) 2023/2225 from 2026-11-20.) CCD2 requires credit advertising that indicates an interest rate or any cost figure to carry standard information, including the annual percentage rate of charge, specified by a representative example `[documented: https://eur-lex.europa.eu/eli/dir/2023/2225/oj/eng, 2026-10-11]`. Generic GEO advice says to write liftable, declarative sentences with exact figures. On a credit page an exact rate or saving figure triggers the TAEG and representative-example duties.
CCD 2008/48/EC, IDD and MiFID II perimeters: unverified [unverified: EUR-Lex texts not readable by curl on 2026-10-12]; see ## Unverified.
So a precise number on these pages passes a legal gate before publishing: it ships **with** its mandated disclosure, or it does not ship. Being precise never exempts copy from this gate. Never illustrate the rule with a made-up figure — models copy the example.

Use the methodology page twice over `[practitioner]`: it is the P2B Art. 5 artefact, and the inputs, dates and scope it publishes are information gain no competitor page carries.

The published "what we deliberately don't do" trust block that the same source proposes lives in skill `seo-strategy` › strategy-playbooks.

The often-quoted conversion figure — comparison pages at **4–7%** against **0.5–1.8%** for standard blog content — comes from the same source and is `[vendor, Intergrowth November 2025 survey; neither the page sample nor the respondent count is published]`. The survey's own headline was that 35.8% of surveyed marketers said comparison content performs "better than ever". **Do not set 4–7% as a target or quote it to a stakeholder as an expectation** — use it only as the reason comparison pages deserve engineering attention at all.

## Unverified

- P2B Art. 5 ranking-parameter duty: the main parameters that drive the ranking, and their relative weight, must be published, together with every way a payment can affect position (Reg. (EU) 2019/1150) [unverified: EUR-Lex text not readable by curl on 2026-10-12].
- UCPD and Omnibus ranking and review rules: undisclosed paid ranking is blacklisted; fake or unverified reviews are banned; Art. 7(4a) imposes a duty to inform about ranking parameters (Dir. 2005/29/EC as amended by Dir. (EU) 2019/2161) [unverified: EUR-Lex texts not readable by curl on 2026-10-12].
- DSA Arts. 25 and 27 duties: dark-pattern ban and recommender-system transparency for "online platforms" (Reg. (EU) 2022/2065) [unverified: EUR-Lex text not readable by curl on 2026-10-12].
- CCD 2008/48/EC, IDD and MiFID II perimeters: on an insurance page an exact figure falls inside the IDD (Dir. (EU) 2016/97) distribution perimeter; on an investment page, the MiFID II (Dir. 2014/65/EU) advice boundary; CCD 2008/48/EC credit-advertising duties apply until CCD2 applies [unverified: EUR-Lex texts not readable by curl on 2026-10-12].

## Sources

- claude-seo@skills/seo-competitor-pages/SKILL.md:24-45, 72-121, 173-182 — the four subtypes, the schema mapping, the fairness guidelines.

