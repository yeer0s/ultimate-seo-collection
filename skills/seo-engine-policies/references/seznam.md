# Seznam — policies, enforcement, controls
> last_verified: 2026-10-11 · market relevance: Czech Republic · doc languages: cs, en · coverage: COMPLETE · scope_exception: none

## Contents
- §1 Who uses this index · §2 Primary documents · §3 Crawlers and verification · §4 Webmaster tools and submission
- §5 What is prohibited · §6 Enforcement · §7 Detection and recovery · §8 AI-use controls
- §9 Delta from Google · §10 Practitioner layer · §11 Unverified · Sources

## 1. Who uses this index
- Seznam.cz and search.seznam.cz: «the first place of choice for millions of Internet users from the Czech Republic» {sz-en-index} [documented: https://o-seznam.cz/napoveda/vyhledavani/en/, 2026-10-11]
- Policy pages are Czech: quotes stay Czech, translation in (“…”).

## 2. Primary documents
| Document | URL | Language | Fetched | Governs |
|---|---|---|---|---|
| Zakázané a nevhodné techniky | https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/ | cs | 2026-10-11 | webspam, penalties |
| Optimalizační minimum | https://o-seznam.cz/napoveda/vyhledavani/optimalizace/optimalizacni-minimum/ | cs | 2026-10-11 | on-page basics |
| Crawling control | https://o-seznam.cz/napoveda/vyhledavani/en/crawling-control/ | en | 2026-10-11 | robots.txt, Request-rate |
| Indexing control | https://napoveda.seznam.cz/en/full-text-search/indexing-control | en | 2026-10-11 | meta robots, nofollow |
| Search help (EN index) | https://o-seznam.cz/napoveda/vyhledavani/en/ | en | 2026-10-11 | SeznamBot, tools |

## 3. Crawlers and verification
- SeznamBot; Seznam asks owners to «consider whitelisting IP addresses of our web crawler» (no list or rDNS method saved; §11). {sz-en-index} [documented: https://o-seznam.cz/napoveda/vyhledavani/en/, 2026-10-11]

## 4. Webmaster tools and submission
- «the Add Page Form or the API Tool»; robot access via «the Check Form». {sz-en-index} [documented: https://o-seznam.cz/napoveda/vyhledavani/en/, 2026-10-11]

### Optimalizační minimum (“optimisation minimum”)
- «Optimalizace by měla být zaměřena především na uživatele» (“should focus mainly on users”) {sz-minimum} [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/optimalizacni-minimum/, 2026-10-11]
- «Stránky s jiným než výše uvedeným kódováním se do indexu nedostanou.» (“other encodings are not indexed”: iso-8859-2, windows-1250, utf-8, utf-16 only); «Dokumenty, jejichž zdrojový kód přesahuje 4 MiB, SeznamBot ignoruje» (“over 4 MiB ignored”) {sz-minimum} [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/optimalizacni-minimum/, 2026-10-11]

## 5. What is prohibited
- Tiers: «Webspam», «Zakázané optimalizační techniky» (“forbidden”), «Nevhodné optimalizační techniky» (“unsuitable”). {sz-forbidden} [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11]

| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 1 | Cloaking | «vydávání jiného obsahu robotovi vyhledávače než lidem pro stejnou adresu URL» (“other content to the robot than to people, same URL”) {sz-forbidden} | Zakázané | [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11] |
| 2 | Doorway | «skupina stránek, které obsahují odkazy na jeden konkrétní web» (“pages linking to one site”) {sz-forbidden} | Webspam | [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11] |
| 3 | Cloaking (skrývání textu) | «skrývání částí textu pomocí CSS nebo obrázků» (“hiding text with CSS or images”) {sz-forbidden} | Zakázané | [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11] |
| 4 | Keyword stuffing | «nepřirozeně vysoký počet vybraného klíčového slova nebo fráze» (“unnaturally high keyword count”) {sz-forbidden} | Zakázané | [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11] |
| 5 | Linkfarmy; Nepřirozené odkazy; SEO PR | «hodnotu ranku získávaného ze zpětných odkazů» (“rank from backlinks”); paid link bars and link exchanges too {sz-forbidden} | Webspam | [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11] |
| 6 | Obsahové farmy; Doménová farma | «pomocí automatického generování neužitečného obsahu» (“auto-generated useless content”) {sz-forbidden} | Webspam | [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11] |
| 7 | — | not addressed | — | — |
| 8 | Skrytá přesměrování | «za krátký čas po načtení automaticky přesměrovávají» (“auto-redirect soon after load”) {sz-forbidden} | Webspam | [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11] |
| 9 | Phishing | «vymámit od nich citlivé údaje nebo rovnou peníze» (“extract sensitive data or money”) {sz-forbidden} | Webspam | [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11] |
| 10 | — | not addressed | — | — |
| 11 | — | not addressed | — | — |
| 12 | — | not addressed | — | — |
| 13 | — | not addressed | — | — |
| 14 | MFA (Made For Advert) | «text s minimální informační hodnotou» (“text of minimal value”) {sz-forbidden} | Webspam | [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11] |
| 15 | — | not addressed | — | — |
| 16 | Nepřirozené odkazy (klamavé) | «odkazy, které vedou jinam, než stránka naznačuje» (“links leading elsewhere than shown”) {sz-forbidden} | Zakázané | [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11] |

### Outside the 16 classes
- Cybersquatting: «vydávání se za jiný subjekt s úmyslem na něm parazitovat» (“impersonating another entity to parasitise on it”) {sz-forbidden} [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11]
- Duplicitní weby: «ostatní budou penalizovány» (“the other domains will be penalised”) {sz-forbidden} [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11]
- Open list: «neuvedení konkrétní techniky na této stránce znamená souhlas» is unsafe to assume (“not listed ≠ allowed”) {sz-forbidden} [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11]

## 6. Enforcement
- «posuzovány a postihovány automaticky a korigovány administrátory podle jasně daných, ale neveřejných pravidel» (“judged and penalised automatically, corrected by admins under non-public rules”) {sz-forbidden} [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11]
- Forbidden techniques: «posuzovány poloautomaticky» (“judged semi-automatically”); unsuitable ones «snižují relevanci stránek» (“lower relevance”) {sz-forbidden} [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11]
- «Stránky porušující zákony platné v České republice se vystavují riziku postihu.» (“breaking Czech law risks a penalty”) {sz-forbidden} [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11]

## 7. Detection and recovery
- «Majitel stránek nemůže postih zrušit ani jinak přímo ovlivňovat.» (“The owner cannot cancel or directly influence the penalty.”) {sz-forbidden} [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11]
- «Postih stránky nezaniká automaticky ve chvíli, kdy je zakázaná technika ze stránek odstraněna» (“does not end when the technique is removed”) {sz-forbidden} [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11]
- «Doba trvání postihu je závislá na typu použité techniky» (“duration depends on the technique”) and on database update cycles {sz-forbidden} [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11]
- Check the crawl side before assuming a penalty: SeznamBot obeys robots.txt and the `Request-rate` directive («Request-rate: <number of documents>/<time>» {sz-crawling}), so a `Disallow` or a very low rate limits what it fetches [documented: https://o-seznam.cz/napoveda/vyhledavani/en/crawling-control/, 2026-10-11]

## 8. AI-use controls
| ID | Engine's own term | Quote (≤25 words) | Doc | Label |
|---|---|---|---|---|
| 17 | robots.txt, Request-rate, meta robots | «SeznamBot fully complies with the robots exclusion standard» {sz-crawling} | Crawling control | [documented: https://o-seznam.cz/napoveda/vyhledavani/en/crawling-control/, 2026-10-11] |
| 18 | — | not addressed | — | — |
- `User-agent: SeznamBot` / `Disallow: /`; Allow, `*`, `$`; «Request-rate: <number of documents>/<time>» {sz-crawling} [documented: https://o-seznam.cz/napoveda/vyhledavani/en/crawling-control/, 2026-10-11]
- «The minimum download rate for SeznamBot is 1 document every 10 seconds.» {sz-crawling} [documented: https://o-seznam.cz/napoveda/vyhledavani/en/crawling-control/, 2026-10-11]
- robots.txt recheck: «it can take up to several weeks» {sz-crawling} [documented: https://o-seznam.cz/napoveda/vyhledavani/en/crawling-control/, 2026-10-11]
- noindex blocked by robots.txt: «won’t be able to see and obey the indexing restriction» {sz-indexing} [documented: https://napoveda.seznam.cz/en/full-text-search/indexing-control, 2026-10-11]
- A recommendation, not a prohibition: «It is recommended to use the rel="nofollow" attribute with links that possibly cannot be trusted», e.g. «user content on your web page that you cannot fully control» {sz-indexing} [documented: https://napoveda.seznam.cz/en/full-text-search/indexing-control, 2026-10-11]

## 9. Delta from Google
- Owner cannot cancel a penalty (§7). [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/, 2026-10-11]
- Request-rate honoured (§8). [documented: https://o-seznam.cz/napoveda/vyhledavani/en/crawling-control/, 2026-10-11]
- «Kvalitní zpětný odkaz získáte například registrací do katalogu firem Firmy.cz.» (“a quality backlink via Firmy.cz”) {sz-minimum} [documented: https://o-seznam.cz/napoveda/vyhledavani/optimalizace/optimalizacni-minimum/, 2026-10-11]

## 10. Practitioner layer
- None in the corpora (engine-corpus-items.md: seznam 0).

## 11. Unverified
- SeznamBot verification: no IP list or rDNS method saved [unverified: SeznamBot page not fetched]
- AI-use controls: none in the saved pages [unverified: no AI-use search logged for Seznam]

## Sources
- https://o-seznam.cz/napoveda/vyhledavani/optimalizace/zakazane-a-nevhodne-techniky/ — Zakázané a nevhodné techniky, fetched 2026-10-11, saved as phase-2 sources/seznam/sz-forbidden.raw
- https://o-seznam.cz/napoveda/vyhledavani/optimalizace/optimalizacni-minimum/ — Optimalizační minimum, fetched 2026-10-11, saved as phase-2 sources/seznam/sz-minimum.raw
- https://o-seznam.cz/napoveda/vyhledavani/en/crawling-control/ — Crawling control, fetched 2026-10-11, saved as phase-2 sources/seznam/sz-crawling.raw
- https://napoveda.seznam.cz/en/full-text-search/indexing-control — Indexing control, fetched 2026-10-11, saved as phase-2 sources/seznam/sz-indexing.raw
- https://o-seznam.cz/napoveda/vyhledavani/en/ — Seznam search help (EN index), fetched 2026-10-11, saved as phase-2 sources/seznam/sz-en-index.raw
