# Third-party notices

## Contents

- Scope
- COPY sources (text carried verbatim, with attribution)
- INTEGRATE sources (rewritten in our own words)
- Excluded and never used
- MIT License — full text
- Apache License 2.0 — full text

## Scope

This file covers the whole SEO skill tree (`seo-optimizer` and its seven `seo-` sibling skills). It is never loaded by the model. Each destination file that carries COPY text also has its own `## Attribution` section; each destination file that carries INTEGRATE material names the source repo and path in its `## Sources`.

The licence texts below apply to the sources marked MIT or Apache-2.0. The copyright lines are reproduced exactly as recorded in the header of each phase-2 adapted file (research/adapted/), which took them from the source repository's LICENSE.

## COPY sources (text carried verbatim, with attribution)

| ID | Repository | Copyright line (as in the adapted header) | Licence | Adapted file | Destination files |
|---|---|---|---|---|---|
| A02 | AgriciDaniel/claude-seo | Copyright (c) 2026 agricidaniel | MIT | AgriciDaniel__claude-seo/google-ledger-and-ai-guide-delta-2026-10.md | skill `seo-engine-policies` › google-updates-timeline; skill `seo-ai-search` › ai-crawlers-and-bot-policy; skill `seo-ai-search` › ai-retrieval-and-citation |
| A06 | AgriciDaniel/claude-blog | Copyright (c) 2025-2026 AgriciDaniel; ordinal rubric © 2024-2026 Paul Bakaus, Apache-2.0 — NOTICE carried: "adapted from impeccable v3.1.1, https://github.com/pbakaus/impeccable" | MIT (claude-blog); method credit pbakaus/impeccable, Apache-2.0 | AgriciDaniel__claude-blog/editorial-review-gate.md | skill `seo-content` › publishing-gates |
| A17 | AnswerDotAI/llms-txt | © AnswerDotAI; spec author Jeremy Howard | Apache-2.0 | AnswerDotAI__llms-txt/llms-txt-v2-spec.md | skill `seo-ai-search` › geo-audit-and-citability |
| A24 | ai-robots-txt/ai.robots.txt | Copyright (c) 2024 ai.robots.txt | MIT | ai-robots-txt__ai.robots.txt/ai-bot-registry-for-edge-gate.md | skill `seo-ai-search` › ai-crawler-registry; skill `seo-technical` › crawl-and-index |
| A25 | aaron-he-zhu/aaron-marketing-skills | Copyright 2024 Aaron He Zhu; modified — rows already in our library removed, wording condensed | Apache-2.0 | aaron-he-zhu__aaron-marketing-skills/ai-surface-retrieval-controls.md | skill `seo-ai-search` › ai-crawlers-and-bot-policy |
| — (FLOW) | AgriciDaniel/flow (github.com/AgriciDaniel/flow), read as vendored in AgriciDaniel/claude-seo `skills/seo-flow/references/prompts/win/` | © Daniel Agrici (as recorded in the destination file's `## Attribution`; no adapted-file header exists) | CC BY 4.0, as stated in each source file's header `<!-- Source: github.com/AgriciDaniel/flow \| License: CC BY 4.0 \| Synced: 2026-04-26 -->`; **not recorded in research/REPORT.md and not checked against a FLOW LICENSE file** (licence deed: https://creativecommons.org/licenses/by/4.0/) | none (taken from the claude-seo clone, 2026-09-22) | skill `seo-content` › flow-win-prompts — three prompt bodies (bofu-page-brief-generator, conversion-audit-prompt, dual-surface-content-scorecard) reproduced verbatim; their "Use This When", Inputs and Example summarised (modified) |

Apache-2.0 modification notices (section 4(b)):
- A17 AnswerDotAI/llms-txt — modified: background essay, directory and integration lists and the FastHTML example body cut; format rules, v2 changes and the spec's statement of purpose kept; our evidence position added.
- A25 aaron-he-zhu/aaron-marketing-skills — modified: rows already in our library removed, wording condensed.
- A06 method credit pbakaus/impeccable — the 0-4 ordinal scale and P0-P3 severity were adapted by claude-blog from impeccable's heuristics scoring; we carry claude-blog's condensed form (per-heuristic tables cut, one-line criteria kept).

CC BY 4.0 notice (FLOW row): the destination file credits Daniel Agrici, names the repository and the licence in its `## Attribution` section and states which parts are verbatim and which summarised. The original FLOW files and their LICENSE are not in this repository, so the licence is as stated in the per-file headers only.

## INTEGRATE sources (rewritten in our own words)

Every distinct repository behind the 31 INTEGRATE-tagged adapted files, once each, with licence and copyright line as written in the adapted headers.

| Repository | Licence | Copyright line (as in the adapted header) |
|---|---|---|
| AgriciDaniel/claude-seo | MIT | Copyright (c) 2026 agricidaniel |
| AgriciDaniel/claude-blog | MIT | Copyright (c) 2025-2026 AgriciDaniel; upstream method © 2024-2026 Matt Van Horn, MIT |
| mvanhorn/last30days-skill (upstream method of claude-blog research-quality) | MIT | © 2024-2026 Matt Van Horn |
| coreyhaines31/marketingskills | MIT | Copyright (c) 2025 Corey Haines |
| kostja94/marketing-skills | MIT | Copyright (c) 2025 kostja94 |
| AminForou/mcp-gsc | MIT | Copyright (c) 2025 Amin Foroutan |
| nowork-studio/notfair-plugin | MIT | Copyright (c) 2026 Toprank Contributors |
| onvoyage-ai/gtm-engineer-skills | MIT | Copyright (c) 2025 OnVoyage AI |
| TheCraigHewitt/seomachine | MIT | Copyright (c) 2025 Castos (original development); Copyright (c) 2025 SEO Machine Contributors |
| ericosiu/ai-marketing-skills | MIT | "Copyright (c) 2026 Portable Content OS contributors" for content-os-portable-starter; "Copyright (c) 2026 Single Grain" for seo-ops |
| addyosmani/web-quality-skills | MIT | Copyright (c) 2026 Addy Osmani |
| aaron-he-zhu/aaron-marketing-skills | Apache-2.0 | Copyright 2024 Aaron He Zhu; modified — condensed, FAQ/HowTo schema steps and DR<30 rule removed, thresholds relabelled |
| zubair-trabzada/geo-seo-claude | MIT | Copyright (c) 2026 Zubair Trabzada |
| installed/site-improvement | in-house (no third-party licence found) | © Mowei (in-house skill, not distributed) |
| google/robotstxt | Apache-2.0 | © each owner (tool names and README facts restated, no prose copied) |
| GoogleChrome/lighthouse | Apache-2.0 | © each owner (as above) |
| GoogleChrome/lighthouse-ci | Apache-2.0 | © each owner (as above) |
| google/schema-dts | Apache-2.0 | © each owner (as above) |
| schemaorg/schemaorg | Apache-2.0 | © each owner (as above) |
| eliasdabbas/advertools | MIT | © each owner (as above) |
| JustinBeckwith/linkinator | MIT | © each owner (as above) |
| harlan-zw/unlighthouse | MIT | © each owner (as above) |
| PhialsBasement/LibreCrawl | MIT | © each owner (as above) |
| garmeeh/next-seo | MIT | © each owner (as above) |
| iamvishnusankar/next-sitemap | MIT | © each owner (as above) |
| harlan-zw/nuxt-seo | MIT | © each owner (as above) |
| towfiqi/serpbear | MIT | © each owner (as above) — listed only as "not recommended" |
| every-app/open-seo | MIT | © each owner (as above) |
| TecharoHQ/anubis | MIT | © each owner (as above) |

The tool rows from google/robotstxt down come from one adapted file (group-E__readme-tool-repos/tool-stack-by-job.md, README facts of 18 repos). Three repos in that file are LEARN only and no text was taken from them: sethblack/python-seo-analyzer (NOASSERTION), Yoast/wordpress-seo (NOASSERTION), yaojingang/GEOFlow (AGPL-3.0).

## Excluded and never used

- **installed/site-improvement — vendored `axe.min.js`** (MPL-2.0, inspection/AXE-LICENSE): excluded; not reproduced in any adapted file or skill file.
- **EdoStra/Marketing-for-Founders** (CC-BY-SA-4.0): never used, not even as LEARN text, because share-alike would bind our files.
- **AgriciDaniel/claude-seo `content_quality.py` AI-phrase list** (derived from Wikipedia, CC BY-SA, inside an MIT repo): never used, not even as LEARN text.

## MIT License — full text

Applies to every source marked MIT above, each under its own copyright line.

```text
MIT License

Copyright (c) <year> <copyright holders>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Apache License 2.0 — full text

Applies to every source marked Apache-2.0 above, each under its own copyright line.

```text
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```
