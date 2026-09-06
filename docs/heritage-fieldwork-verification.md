# Heritage and Fieldwork Verification

The four categories are implemented and verified as of 2026-09-06. All 71 new catalog assets received a manual quality review, all structural checks passed, and eight representative synthetic scenarios passed after three targeted instruction corrections. No actionable defects remain from this implementation review. The live checks used the declared model, reasoning effort, sandbox, and instructions through standalone Codex executions; native custom-agent dispatch was not tested.

## Implemented scope

| Category | Gateway | Agents | Workflows | Artifact kits |
| --- | --- | ---: | ---: | ---: |
| Archaeological fieldwork | [`$archaeological-fieldwork`](../SKILLS/archaeological-fieldwork/SKILL.md) | 5 | 5 | 5 |
| Language documentation | [`$language-documentation`](../SKILLS/language-documentation/SKILL.md) | 5 | 5 | 5 |
| Oral history | [`$oral-history`](../SKILLS/oral-history/SKILL.md) | 5 | 5 | 5 |
| Heritage conservation | [`$heritage-conservation`](../SKILLS/heritage-conservation/SKILL.md) | 6 | 6 | 6 |

Conservation covers movable objects, archaeological sites, and historic building fabric. The [canonical registry](../REFERENCES/software-development-crew.md#heritage-and-fieldwork-lifecycle) records lifecycle stages, routing, deliberate overlap, model coverage, and all implemented modes. The [manifest](heritage-fieldwork-verification/manifest.json) lists every new role and its exact return sections and settings.

| Catalog measure | Before | After |
| --- | ---: | ---: |
| Agent templates | 133 | 154 |
| Gateways and matching sidecars | 26 | 30 |
| Workflows | 104 | 125 |
| Artifact kits | 102 | 123 |
| Workflow and artifact references combined | 206 | 248 |

The new templates comprise four `gpt-5.6-sol/high` read-only reviewers, three `gpt-5.6-terra/medium` record coordinators, and fourteen `gpt-5.6-terra/high` authors. All seventeen authoring/coordinating roles use workspace-write sandboxes for assigned local deliverables.

## Complete asset review

The [asset review](heritage-fieldwork-verification/asset-review.md) covers all 21 agents, all 21 workflow/kit pairs, all four gateway routers, and all four sidecars: 71 files. Each workflow/kit pair was walked through against its worked example and failure case, giving 42 static walkthroughs. The [machine-readable record](heritage-fieldwork-verification/asset-review.json) retains per-asset evidence, rubric scores, final source hashes, and the three corrections re-reviewed after live execution.

Every required rubric criterion scored at least 3/4. These scores are manual instruction-quality judgments, not independent review, model performance scores, or professional certification. Supporting assets remain adaptable working records rather than destination-specific production schemas. Agent fallbacks are deliberately condensed; the selected workflow supplies the detailed procedure.

## Structural and discovery checks

The [catalog checker](heritage-fieldwork-verification/check_catalog.py) passed across all 154 templates and 30 gateways. It checks TOML fields and settings, skill and sidecar YAML, implemented skill references, registry/model counts, local links, reachability of all workflows and kits, named handoffs, and the 21 new agent/workflow output contracts. It resolved 259 local links. All four new gateways also passed the skill creator's `quick_validate.py`; their [validation output](heritage-fieldwork-verification/skill-validation.json) is retained. The [catalog result](heritage-fieldwork-verification/catalog-check.json) records the counts and successful `git diff --check`.

With installed Codex CLI 0.153.4, a fresh temporary project registered all 21 new template paths and discovered all 30 copied project skills with zero skill errors. This exercised `app-server --stdio`, `config/read`, and `skills/list` against the final files. The [discovery record](heritage-fieldwork-verification/runtime-discovery.json) includes the resolved configuration paths and hashes of the original discovery responses. It verifies discovery and path resolution; it does not establish native subagent invocation.

## Representative live scenarios

Each test received only an explicitly synthetic text packet in an isolated temporary project, the selected template, and the four new gateways. The harness passed the template's actual developer instructions and model settings to `codex exec`. Delegation, web search, hooks, and apps were disabled. Three scenarios used read-only sandboxes and five produced requested local artifacts in workspace-write sandboxes. All eight preserved their supplied inputs byte-for-byte.

| Scenario | Accepted attempt / model | Observed result and retained response |
| --- | --- | --- |
| Archaeological recording | 3 / terra high | [Complete context and finds records](heritage-fieldwork-verification/cases/archaeology_records/response.md): three contexts, two finds, and one sample retain their source links; missing coordinates remain missing. |
| Stratigraphic sequence | 2 / sol high | [Located sequence review](heritage-fieldwork-verification/cases/archaeology_sequence/response.md): preserves the three-edge cycle, identifies missing C999, retains the valid C205-before-C204 ordering, and separates object dating from deposition. |
| Linguistic annotation | 2 / terra high | [Completed supported annotation tiers](heritage-fieldwork-verification/cases/language_annotation/response.md): three source forms and intervals retained; unknown `lo` remains unresolved; no audio inspection claimed. |
| Lexicon curation | 2 / terra high | [Four lexical records](heritage-fieldwork-verification/cases/language_lexicon/response.md): preserves `tal`/`tál`, separate senses and varieties, unmatched U99, and the research-only/public-export conflict. |
| Oral-history transcript | 2 / terra high | [Complete reading transcript](heritage-fieldwork-verification/cases/oral_transcript/response.md): preserves eight turns, negation, dialect, repetition, uncertainty, and hearsay; July remains a separate narrator annotation. |
| Narrator review and access | 3 / sol high | [Version-specific access review](heritage-fieldwork-verification/cases/oral_access/response.md): distinguishes internal, booklet, excerpt, and web uses; identifies the restricted interval and required V1 package removal; scopes the archival handoff to read-only assessment. |
| Conservation monitoring | 3 / terra medium | [Monitoring and maintenance records](heritage-fieldwork-verification/cases/conservation_monitoring/response.md): calculates +4 percentage points and +0.2 mm for comparable pairs, preserves unavailable comparisons, and distinguishes unverified completion from non-performance. |
| Treatment proposal review | 3 / sol high | [Located proposal findings](heritage-fieldwork-verification/cases/conservation_treatment/response.md): challenges unsupported material, reversibility, stability, and structural-safety claims while permitting bounded preventive planning with unresolved causes. |

Model names in the table abbreviate `gpt-5.6-terra` and `gpt-5.6-sol`. The [live results](heritage-fieldwork-verification/live-results.json) retain exact settings, elapsed time, acceptance evidence, selected-source hashes, output hashes, and completed command counts. Each case directory contains its exact input, response, invocation record, command outcomes, and any produced files. Absolute paths inside verbatim model responses refer to the original temporary projects; the corresponding retained artifacts are under each case's `outputs/` directory.

The [independent output checker](heritage-fieldwork-verification/check_outputs.py) passed against the retained evidence. It verifies all eight cases' provenance and all 71 reviewed asset hashes, then checks structured outputs from the five authoring scenarios: record identities and links, supplied linguistic forms, transcript speech and timestamps, baseline/change arithmetic, comparison limits, and maintenance evidence. The three prose-only reviews were assessed manually; their correctness is not inferred from keyword matching. See [output-check.json](heritage-fieldwork-verification/output-check.json).

## Corrections and unsuccessful attempts

Three completed model outputs prompted bounded instruction changes and successful reruns:

1. The oral-history access handoff assigned repository implementation to `collection-access-reviewer`, whose role is read-only. The template and workflow now request an assessment; authorized repository operators implement approved controls and metadata changes.
2. Monitoring assigned scheduling/non-performance states unsupported by the packet and assessed a change trigger at an initial baseline without a prior reading. The template, workflow, and kit now distinguish missing observations, scheduled work, unverified completion, and confirmed non-performance, and separate absolute-value triggers from change/rate triggers.
3. Treatment review delayed preventive planning until causes were established. The template and workflow now permit bounded planning with unresolved causes and proposed measurements while retaining evidence and authorization requirements for implementation.

The first batch of eight invocations failed before a model turn because the default runtime home was read-only. A writable temporary home resolved startup. One subsequent sandboxed network probe could not reach the model and timed out after 300 seconds; the authorized network-enabled executions then completed. Together with the three superseded model outputs, these are twelve retained prior attempts and twenty CLI invocations overall. The [prior-attempt ledger](heritage-fieldwork-verification/live-results.json) links each retained record and explains its disposition.

Successful scenarios sometimes recovered from intermediate shell-launch or path errors; success does not mean every attempted command succeeded. `commands.json` preserves those exit statuses. Original event-stream and stderr hashes are recorded in each `run.json`; full event streams remain in the task's temporary workspace. Earlier passing cases copied sibling workflows that were subsequently corrected, but their selected template, router, workflow, and kit still match the final catalog byte-for-byte. The results explicitly list changed, unselected siblings.

## Commands and reproducibility

These local checks can be rerun from the repository with Python 3.11+ and PyYAML:

```bash
python3 docs/heritage-fieldwork-verification/check_catalog.py
python3 docs/heritage-fieldwork-verification/check_outputs.py
git diff --check
```

The skill validation command was run separately for each of the four gateway directories:

```bash
python3 /home/cadwaladyr/.codex/skills/.system/skill-creator/scripts/quick_validate.py SKILLS/archaeological-fieldwork
python3 /home/cadwaladyr/.codex/skills/.system/skill-creator/scripts/quick_validate.py SKILLS/language-documentation
python3 /home/cadwaladyr/.codex/skills/.system/skill-creator/scripts/quick_validate.py SKILLS/oral-history
python3 /home/cadwaladyr/.codex/skills/.system/skill-creator/scripts/quick_validate.py SKILLS/heritage-conservation
```

The actual runtime commands used the prepared temporary workspace:

```bash
python3 /tmp/heritage-fieldwork-20260906/runtime_check.py
python3 /tmp/heritage-fieldwork-20260906/run_live.py
python3 /tmp/heritage-fieldwork-20260906/run_live.py archaeology_records
python3 /tmp/heritage-fieldwork-20260906/run_live.py archaeology_sequence language_annotation language_lexicon oral_transcript oral_access conservation_monitoring conservation_treatment
python3 /tmp/heritage-fieldwork-20260906/run_live.py oral_access conservation_monitoring conservation_treatment
```

[run_live.py](heritage-fieldwork-verification/run_live.py), [runtime_check.py](heritage-fieldwork-verification/runtime_check.py), and [fixtures.py](heritage-fieldwork-verification/fixtures.py) are snapshots of the verification harnesses, not a general test API. The live harness uses [fixtures.json](heritage-fieldwork-verification/fixtures.json) and the gateway selection retained in [catalog-data.json](heritage-fieldwork-verification/catalog-data.json). Running these harnesses again requires a fresh temporary working directory, the actual repository path configured in the scripts, an installed compatible Codex CLI, and model access. The writable-home change is reflected in the retained final harness; the earlier invocation records preserve the startup failures. Model outputs are not expected to reproduce byte-for-byte.

The isolated live homes linked the existing authentication file; credentials were not copied into the evidence. All twelve task-created authentication symlinks were removed after verification, preserving the original authentication file. No authentication files, temporary runtime homes, binaries, or account configuration dumps are included. The evidence preserves model responses verbatim, including original Markdown whitespace.

## Assumptions and limits

### Discovery reader correction (2026-09-06)

The retained `runtime_check.py` was corrected after review: its RPC reader now uses
`os.read()` with a persistent byte buffer, draining complete newline-delimited
messages before waiting for descriptor readiness. This prevents buffered
notifications from hiding a following response or configuration error. Partial
frames remain subject to the request deadline, and trailing bytes survive between
requests. The default deadline remains 25 seconds.

`python3 docs/heritage-fieldwork-verification/test_runtime_reader.py` passed five
real-pipe regression tests covering coalesced notifications/error/next response,
fragmented UTF-8, partial-frame timeout and resume, incomplete-frame EOF, and a
complete response before EOF. The tests load the exact reader function without
executing the harness's workspace setup.

The corrected discovery harness was also copied into a fresh temporary directory
and run with Python 3 against Codex 0.153.4: all 21 agents and 30 project skills
were discovered without skill errors. A separate local app-server probe loaded
the same reader, introduced an unclosed array into only the temporary home config,
and received error -32603 in 0.001 seconds. Restoring that config allowed the next
request to resolve all 21 agent registrations. Temporary files were removed.
These checks made no model calls; the historical discovery and live-model evidence
above remains unchanged.

The selected uncommon domains and object/site conservation scope implement the accepted plan. Missing evidence permits useful bounded drafts with explicit unresolved items. Source conventions, destination requirements, participant decisions, and institutional authority remain assignment inputs.

Coverage is complete for manual asset review and catalog structure, and representative for model behavior: eight of the 21 roles were exercised live. No physical fieldwork, media inspection, conservation intervention, professional certification, external deposit, publication, or global installation was performed. No domain expert independently reviewed these synthetic results. Native custom-agent dispatch and the remaining thirteen roles' live behavior remain untested. Existing text-lifecycle assets and historical verification records were preserved.
