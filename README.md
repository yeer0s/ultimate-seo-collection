<h1 align="center">Ultimate SEO Collection</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="MIT"></a>
  <img src="https://img.shields.io/badge/skills-8-00a8a8" alt="8 skills">
  <img src="https://img.shields.io/badge/spam%20plays-87-00a8a8" alt="87 spam plays">
  <img src="https://img.shields.io/badge/engines-11-00a8a8" alt="11 engines">
  <img src="https://img.shields.io/badge/claims-evidence%20labelled-orange" alt="evidence labelled">
  <a href="https://mowei.pt"><img src="https://img.shields.io/badge/by-mowei.pt-111111" alt="mowei.pt"></a>
  <a href="https://buymeacoffee.com/letsmoweis"><img src="https://img.shields.io/badge/%E2%98%95-buy%20me%20a%20coffee-FFDD00" alt="Buy me a coffee"></a>
  <a href="https://ko-fi.com/letsmowei"><img src="https://img.shields.io/badge/ko--fi-support-FF5E5B" alt="Ko-fi"></a>
</p>

<h3 align="center">
  Eight Claude skills that work as one SEO system.<br>
  Every claim tells you where it came from.
</h3>

<p align="center">
  <b>A router skill plus seven specialists</b> — engine policies, evidence, technical,<br>
  content, authority, AI search and strategy — for Claude Code and any SKILL.md agent.
</p>

---

:fire: ***News*** :fire:

- **[Oct 2026]** v1.1.0 — competitive-landscape research protocol in `seo-optimizer`: map every competitor in a market, verify the claims, stop at saturation, ship a database and dashboard ([changelog](CHANGELOG.md))
- **[Oct 2026]** v1.0.1 — practitioner evidence now cites anonymised sources only
- **[Oct 2026]** First public release — 8 skills, 109 files
- **[Oct 2026]** Engine policy pages for 11 search and AI engines, each claim dated to the day it was read
- **[Oct 2026]** An 87-play spam catalogue built for *defence*: how each manipulation works, its tells, the engine rule and the counter
- **[Oct 2026]** A 32-case eval set ships in `skills/seo-optimizer/evals/` so you can test the pack on your own model

---

## Most SEO advice does not say how it knows

A blog post, a forum thread and Google's own documentation get repeated with the same
confidence. This collection keeps them apart. Every claim carries a label:

| Label | Meaning |
|---|---|
| `[documented: <url>, <date>]` | Stated by the engine or standard itself, with the date it was read |
| `[measured: …]` | A controlled test, with its sample size |
| `[practitioner: …]` | What practitioners report, with thread counts — experience, not engine policy |
| `[unvalidated house heuristic]` | A working rule of ours that is not yet tested |
| `[hypothesis]` | An idea worth testing |

So you can tell a rule Google wrote from a rule somebody on a forum believes.

## What is inside

| Skill | What it covers |
|---|---|
| `seo-optimizer` | The entry point. Runs full SEO audits and sends each question to the right subskill. Holds the full evidence grammar. Also runs the competitive-landscape research protocol: multi-agent discovery by cluster, fact-check and browser-verification loops, search / traffic / backlink / paid / AI-citation dimensions and a saturation stop rule, delivered as one profile per firm, CSV matrices, a two-page snapshot and an HTML dashboard. |
| `seo-engine-policies` | What each search and AI engine allows and penalises — Google, Bing, Yandex, Baidu, Naver, Seznam, Brave, and the AI engines of OpenAI, Perplexity, Anthropic and Microsoft Copilot — plus the update timeline and the 87-play spam catalogue. |
| `seo-evidence` | What really works and what does not: practitioner layers from anonymised sources (general, technical, professional and agentic-SEO practitioners), controlled title and SERP tests, works-vs-doesn't tables. |
| `seo-technical` | Crawling, indexing, sitemaps, hreflang, performance, structured data, Google APIs and quotas, incident triage, drift monitoring. |
| `seo-content` | Keyword research, intent, briefs, comparison pages, programmatic SEO, publishing gates. |
| `seo-authority` | Links, trust signals and distribution, without link schemes. |
| `seo-ai-search` | Getting cited by AI answer engines: AI crawler registry and bot policy, citability audits, llms.txt, data assets. |
| `seo-strategy` | Planning, prioritised playbooks and an ideas register — each idea comes with a test and a kill condition. |

## Install

1. Clone this repo, or download the zip from [Releases](../../releases).
2. Copy the eight folders inside `skills/` into your Claude skills folder:
   - for every project: `~/.claude/skills/` (Windows: `C:\Users\<you>\.claude\skills\`)
   - for one project only: `<project>/.claude/skills/`
3. Restart Claude Code. Ask "audit our SEO" or any SEO question; `seo-optimizer` takes it from there.

Keep the folder names as they are: the skills link to each other by name.

## Tested on

Graded strictly on 20 eval questions (pass only if every required element is met and no
forbidden one appears):

| Model | Passed |
|---|---|
| Claude Opus | 18 of 20 |
| Claude Sonnet | 18 of 20 |
| Claude Haiku | 11 of 20 |

Use Opus or Sonnet for audits. Haiku works for quick lookups but misses detail.

## Worked example

Many references use [mowei.pt](https://mowei.pt), a Portuguese consumer comparison site, as a
worked example. The method carries over to any site; the Portuguese specifics are there for
illustration.

## What it touches

- **Reads and writes:** nothing on its own. The skills are Markdown that Claude reads.
- **Network:** one optional script, `skills/seo-content/scripts/autocomplete_expand.py`, calls
  `suggestqueries.google.com` (Google Autocomplete) to expand keywords. It needs `requests`
  and runs only when you run it.
- **BigQuery:** `skills/seo-content/scripts/gsc_bigquery.sql` holds queries for your own
  Search Console bulk export. Run them yourself, in your own project.
- **Competitor research:** the protocol in `skills/seo-optimizer/references/competitive-landscape-research.md`
  uses your agent's own web search and browser tools; it never submits forms, creates accounts,
  solves CAPTCHAs or clicks ads. Its two scripts, `merge_rows.py` and `build_dashboard.py` in
  `skills/seo-optimizer/scripts/`, use the Python standard library only, make no network calls, and
  read and write only inside the output folder you pass them.

## The thing it refuses to do

The spam catalogue exists so you can recognise and defend against manipulation, never run it.
A request to run, build or hide a play gets a refusal and the safe alternative.

## Limits

- Search engines change their rules. Each documented claim carries the date it was read;
  check the source before acting on an old one.
- No skill can guarantee rankings, traffic or AI citations.
- Answer quality depends on the model — see *Tested on* above.

## Licence

MIT — see [LICENSE](LICENSE). Free to use, change and share, including commercially, as long
as the copyright notice stays with it.

Parts of the collection adapt open-source work under the MIT, Apache 2.0 and CC BY 4.0
licences. Attribution and the full licence texts are in
[`skills/seo-optimizer/THIRD-PARTY-NOTICES.md`](skills/seo-optimizer/THIRD-PARTY-NOTICES.md);
keep that file with any copy.

---

<p align="center"><sub>Free, by <a href="https://mowei.pt">mowei.pt</a> · if it saved you time, a coffee keeps it maintained</sub></p>
