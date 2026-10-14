# Scope exceptions — engines shipped without full coverage

Never loaded by the model. Each exception names the engine, what is missing, why, who approved it, the date, and the condition that
closes it. An engine page in coverage state INCOMPLETE must carry one of these IDs; `engine_pages_check.py --handover` fails if the
exception is not approved.

| ID | Engine | What is missing | Why | Status | Approved by | Date | Closing condition |
|---|---|---|---|---|---|---|---|
| SE-01 | Naver | Proposed in plan round 3 because searchadvisor.naver.com could not be read by WebFetch | — | closed before use: not needed | — | 2026-10-11 | Met on 2026-10-11: the Search Advisor guide was read raw with curl (13 guide posts through the guide's own post endpoint, incl. 웹 콘텐츠 스팸사례, modified 2026-07-03). The Naver page is written from those copies and carries no scope exception. |

No other engine needs an exception on 2026-10-11. If a page later becomes INCOMPLETE (a primary document exists but cannot be
read), add a row here with status "proposed" and ask the skill owner to approve or reject it before handover.
