# Text Lifecycle Verification

Verified on 2026-09-05. The accepted expansion is implemented, with complete manual review of every affected catalog asset, whole-catalog structural checks, current-stable Codex loading, and 22 representative live scenarios. The final artifact from each scenario passed its stated acceptance checks after the corrective reruns documented below.

## Changes

| Asset | Before | After | Added | Existing assets deepened |
| --- | ---: | ---: | ---: | ---: |
| OpenAI agent templates | 111 | 133 | 22 | 10 |
| Skill gateways | 22 | 26 | 4 | 1 |
| Workflows | 76 | 104 | 28 | 8 |
| Supporting artifact references | 74 | 102 | 28 | 8 |

The new gateways are `text-composition` (nine modes), `text-revision` (seven), `text-translation` (three), and `textual-scholarship` (four). Five new publishing modes cover proofing, format review, indexing, general submission preparation, and edition maintenance. All eight prior publishing workflows and kits were deepened. Existing names are preserved; `developmental-manuscript-editor` now owns applied structural revision and `indexing-coordinator` owns actual index creation and revision.

Coverage includes conception, source synthesis, outlines, all seven drafting forms, substantial revision, feedback, rhetoric, continuity, reader orientation, adaptation, translation, witnesses, transcription, collation, editions, line/copy editing, evidence and rights review, proofs, accessible-format inspection, indexes, submission materials, and subsequent corrections. Full-draft and applied-edit requests require the actual text or files. Deliberate form, voice, source uncertainty, and long-manuscript coverage remain explicit.

The [canonical registry](../REFERENCES/software-development-crew.md#text-composition-and-editing-lifecycle) contains routing, overlap ownership, model counts, and implemented modes. The [accepted plan](text-lifecycle-expansion-plan.md) records scope and acceptance criteria.

## Complete asset review

[Asset review](text-lifecycle-verification/asset-review.md) and its [machine-readable scores and hashes](text-lifecycle-verification/asset-review.json) cover all 36 affected workflow/kit pairs, all five gateway routers and UI metadata files, and all 32 new or modified agents. Every required rubric criterion is at least 3/4. Gateway scores use the weakest mode for each criterion. These are instruction-quality judgments, not claims that every model will always follow them.

Each workflow was read with its linked artifact. Checks included discriminating routing, conditional loading, domain decisions, complete owner-facing outputs, meaningful working fields, examples and failure cases, verification limits, and adjacent-role boundaries. Manual review corrected stale blanket stops around rights evidence and journal preparation, clarified delegated checks as still unresolved until evidence returns, and updated production handoffs.

## Structural and runtime checks

- All 133 agent TOML files and 26 gateway/UI YAML pairs parse; names, required fields, sandbox choices, and skill references resolve.
- All 104 workflows are reachable from gateway tables and all 102 artifact references are reachable from workflows. Local catalog links and named handoffs resolve.
- All 32 affected agent output contracts match their primary workflow contracts. Registry counts, model distribution, routing, and Markdown table structure agree with the files.
- The five affected gateways pass the skill-creator validator. `git diff --check` passes.
- A temporary Codex **0.153.4** binary and matching code-mode helper were used. This was the [current stable release](https://github.com/openai/codex/releases/tag/rust-v0.153.4) checked during this run. The host Codex installation was not replaced.
- With isolated project configuration, `app-server --stdio` initialization, `config/read`, and `skills/list` succeeded. All 26 project skills were discovered with no reported skill errors; configuration resolved the explicit `fiction-drafter` agent file and concurrency value correctly. This configuration read does not claim an independent live run of all 133 agents.

The [catalog check](text-lifecycle-verification/catalog-check.json), [configuration response](text-lifecycle-verification/config-read.json), and [skill discovery response](text-lifecycle-verification/skills-list.json) retain the structural/runtime evidence.

## Representative live checks

Each scenario ran in an ephemeral Codex CLI invocation with delegation disabled. Named-agent cases loaded that template's actual developer instructions, model, reasoning, and sandbox settings. Feedback integration and the combined scholarship pipeline were direct Terra/high gateway cases. Their workflow behavior was tested; no separate runtime claim is made for each scholarship agent.

| Scenario | Final acceptance evidence |
| --- | --- |
| [planning](text-lifecycle-verification/cases/planning/response.md) | Produced a four-receipt brief and drafting handoff; explicitly separated the plan from text not yet drafted. |
| [fiction](text-lifecycle-verification/cases/fiction/response.md) | Delivered the complete four-receipt story from the actual planning output, without an outside narrator in the story; 248 whitespace-delimited words. |
| [nonfiction](text-lifecycle-verification/cases/nonfiction/response.md) | Delivered 272 words excluding title; retained 18/30, entrance recruitment, one Saturday, comparison limits, and a labeled hypothetical example. No unsupported recency or inference about omitted study questions remains. |
| [essay](text-lifecycle-verification/cases/essay/response.md) | Delivered a 232-word complete reflective essay using supplied memories, recurring repair/listening material, and an open ending. |
| [poetry](text-lifecycle-verification/cases/poetry/response.md) | Delivered exactly eight free-verse lines, each beginning Still; retained the refrain and changed the final significance of waiting. |
| [drama](text-lifecycle-verification/cases/drama/response.md) | Delivered a complete 268-word scene with Mina, Sol, one table, coherent key movement, and an altered final relationship; timing remained approximate. |
| [professional](text-lifecycle-verification/cases/professional/response.md) | Delivered a complete proposal memo preserving all supplied facts and no approved staffing/budget commitment. The final run executed wc -w and accurately reported 160 words including headers. |
| [academic](text-lifecycle-verification/cases/academic/response.md) | Delivered a complete abstract retaining 24 volunteers, two weeks, self-report, 3 minutes/day, no control group, and absent uncertainty information. The final run executed wc -w and accurately reported 178 words excluding metadata. |
| [revision](text-lifecycle-verification/cases/revision/response.md) | Applied the requested date discrepancy to the actual preceding fiction draft; wrote the complete four-receipt revision with a responsive final receipt and unresolved memory origin. |
| [feedback](text-lifecycle-verification/cases/feedback/response.md) | Wrote the complete revised passage; retained all three I remember openings, shortened the explanation, and accounted for the accepted and declined comments. |
| [rhetoric](text-lifecycle-verification/cases/rhetoric/response.md) | Delivered the revised passage with all three We waited openings and the clerk's uncertainty preserved. |
| [continuity](text-lifecycle-verification/cases/continuity/response.md) | Reported the paired Tuesday/Wednesday bridge contradiction; distinguished an identified lie and explicitly limited conclusions to supplied excerpts. |
| [readers](text-lifecycle-verification/cases/readers/response.md) | Located undefined concepts and action-order problems; separated predicted effects from absent reader-study evidence and did not modify source files. |
| [adaptation](text-lifecycle-verification/cases/adaptation/response.md) | Delivered a complete community notice within the 90-130-word range, preserving sampling limits and the unapproved extended-hours proposal without adding unsupported survey duration or recency. |
| [translation](text-lifecycle-verification/cases/translation/response.md) | Translated both source sentences with singular they, preserved negation and might, and retained the two-day interval. |
| [translation_review](text-lifecycle-verification/cases/translation_review/response.md) | Compared the actual preceding translation and a deliberately faulty alternative; accepted defensible A and located B's gender, negation, modality/reported-speech, and time-interval errors without applying changes. |
| [scholarship](text-lifecycle-verification/cases/scholarship/response.md) | Wrote witness descriptions, diplomatic transcriptions, collation, edited text, apparatus, and policy. Preserved A's unreadable span and historical spelling, distinguished B variants, and made no physical-source or stemma claim. |
| [proof](text-lifecycle-verification/cases/proof/response.md) | Returned exact public-access and note-number corrections, identified the missed prior correction, and left visual proof coverage unverified. |
| [format](text-lifecycle-verification/cases/format/response.md) | Inspected the actual EPUB ZIP/XML and found the seeded missing ending anchor. Also reported missing XHTML language attributes. Distinguished those checks from unavailable EPUBCheck, rendering, and accessibility certification. |
| [index](text-lifecycle-verification/cases/index/response.md) | Wrote a provisional concept index with only supplied anchors, substantive headings, and resolving see-references; did not invent print pages. |
| [submission](text-lifecycle-verification/cases/submission/response.md) | Wrote complete separate cover note and nine-word biography. Preserved residence and occupation as separate facts, did not invent credentials, and left the absent anonymous story and metadata unverified. |
| [edition](text-lifecycle-verification/cases/edition/response.md) | Wrote the corrected source and log. Independent comparison confirms that the sole source change is table-label 2018 to 2019; caption/discussion agree and unavailable PDF/EPUB updates remain pending. |

The brief → fiction → structural revision and translation → comparative review cases consumed the actual preceding output. Independent checks counted the delivered spans, verified all eight poem openings, preserved the three feedback refrains, checked the nine-word biography, confirmed the EPUB's seeded missing anchor, and compared the exact edition correction against the original source.

[Live results](text-lifecycle-verification/live-results.json) retain per-case status and acceptance notes. Every case directory contains the exact response and a `run.json` with prompt, actual invocation settings, command exit outcomes, and hashes of raw logs. [Inputs](text-lifecycle-verification/inputs/) and [generated output files](text-lifecycle-verification/outputs/) retain the original fixtures and actual artifacts; response links preserve their original temporary execution paths. Original text fixtures were compared with the literal fixture generator inputs. Copied skills and agent templates were compared byte-for-byte with the final catalog.

## Observed failures and corrective reruns

Twelve prior attempts are retained, including unsuccessful content/reporting results rather than only the final successes:

- Nonfiction first inferred a survey-method omission from missing packet detail, then called an undated survey recent. Explicit negative-evidence and unsupported-specificity rules were added; the final draft preserved the supplied evidence limits.
- Drama first gave contradictory table movement. An attempted-versus-completed-action check was added. A later process produced a completion event but timed out before writing the response file; it was preserved separately and not counted as a clean run. The final scene was physically coherent and completed normally.
- Submission copy inferred a workplace location from separate residence and occupation facts. The workflow and role now check those relationships; the final cover note retained them separately.
- Adaptation added the unsupported description brief to a survey. A factual-qualifier check was added. The next draft then missed the minimum length and reported an incorrect count, so measured hard-limit checks were added as well. The final notice retained the known sampling facts and met the requested extent.
- The professional and academic drafts originally met their requested limits but reported incorrect exact counts. Measured-count guidance was added; the final invocations ran `wc -w`, and independent counts matched their 160- and 178-word reports.
- Two attempts timed out amid DNS/connection errors. A translation-review attempt was interrupted after a long connection delay; source reading had begun, but no review had completed. These were environment/interruption results, not content failures, and were rerun with network access.

[Failed-attempt evidence](text-lifecycle-verification/failed-attempts/) retains statuses, available responses or completion events, commands, and raw-log hashes. Raw event streams and stderr remain at `/tmp/text-lifecycle-20260905/live/`; transient model state and account data are not bundled in the repository.

Some successful runs recovered from wrong relative artifact paths or irrelevant `git status` calls in the isolated non-Git fixture directory. The five gateways now explicitly resolve links relative to their containing file. Subsequent nonfiction, submission, translation-review, professional, academic, and adaptation cases exercised the clarification. An unrelated installed-plugin warning about an overlong default prompt was observed and left unchanged. Successful final turns do not imply every intermediate command returned zero.

## Commands and boundaries

Commands executed for final verification included:

```text
python3 /tmp/text-lifecycle-20260905/check_catalog.py
python3 /tmp/text-lifecycle-20260905/runtime_check.py
python3 /home/cadwaladyr/.codex/skills/.system/skill-creator/scripts/quick_validate.py SKILLS/<affected-gateway>
python3 /tmp/text-lifecycle-20260905/run_live.py <selected-case-names>
python3 /tmp/text-lifecycle-20260905/review_assets.py
python3 /tmp/text-lifecycle-20260905/capture_evidence.py
git diff --check
```

The recorded verification scripts preserve the actual temporary paths and harness used. They are evidence for this run, not a new portable installation or test command. Repeating live checks requires a separate prepared fixture directory, compatible Codex binary/helper, network access, and account authorization; no credentials or binaries are included.

The live fixtures are deliberately bounded. They do not prove book-length completion, every language or form, every specialist's runtime behavior, DOCX/PDF rendering, TEI schema conformance, EPUB accessibility, publication readiness, or market response. The EPUB case checked package/XML/navigation evidence and explicitly left rendering and full-validator checks unavailable. No real submission, publication, global installation, or external document transfer was performed. No branch or commit was created.
