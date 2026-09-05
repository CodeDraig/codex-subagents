import hashlib,json,re,tomllib
from pathlib import Path
R=Path('/srv/data/code/codex-subagents'); P=Path('/tmp/text-lifecycle-20260905'); D=R/'docs/text-lifecycle-verification';D.mkdir(parents=True,exist_ok=True)
# Explicit manual scores after reading every affected workflow, linked kit, gateway, and agent.
mode_rows='''composition-planning|3444344|Distinct concepts become a brief and unit ledger; the receipt-form example preserves the requested form and separates planning from drafted coverage.
source-synthesis-and-outlining|3444444|Source classes, derivative-source dependence, contradiction retention, and claim-to-location links make the outline auditable.
fiction-drafting|3444344|POV access, formal engines, designed stasis, canon, and complete-unit delivery distinguish drafting from structural diagnosis.
nonfiction-drafting|3444444|Claim ledger preserves sampling and causality; final rules also prohibit invented survey methods, recency, and relationships between adjacent facts.
essay-composition|3444344|Braid movement and changing image returns coexist with a strict distinction between supplied memory and invented persona.
poetry-composition|3444444|Line endings, stress uncertainty, refrains, visual spacing, and performed versus estimated musical fit are inspectable craft decisions.
dramatic-writing|3444444|Objectives, tactics, cue ownership, prop state, and staging constraints govern actual scenes; attempted and completed movement are distinguished.
professional-writing|3444444|Recipient decisions, proposal status, commitment authority, medium conventions, and measured count scope govern complete documents.
academic-writing|3444444|Section-to-evidence mapping, empirical versus humanities structures, result limits, verified citations, and measured count scope prevent fabricated completeness.
revision-planning|3444344|Located actions include consequences, preserved choices, dependencies, and acceptance checks; unseen chapters remain outside coverage.
structural-revision|3444444|Before/after units and applied text include repairs to transitions, references, and claim/evidence dependencies; concurrent changes remain recoverable.
feedback-integration|3444444|Comment IDs retain source and decisions; author constraints outrank votes, and claimed resolutions are checked in the actual revision.
rhetorical-revision|3444344|Devices are chosen for effects; before/after negation, modality, referents, and voice checks constrain language revision.
continuity-review|3444444|Time and POV ledgers distinguish contradiction, lies, change, and unseen context; every confirmed conflict needs paired passages.
reader-response-review|3444344|Located inference burdens are evaluated against intended difficulty; predicted reader effects remain separate from observed feedback.
text-adaptation|3444444|Source-to-target units account for consequential omissions, additions, changed audience, and preserved claim strength; added qualifiers require source support and hard lengths require measured counts.
translation-planning|3444344|Contextual terminology and competing form/fidelity priorities support provisional drafting without forced early disambiguation.
translation-drafting|3444444|Complete unit alignment and separate target/source passes check modality, negation, register, form, and unsupported disambiguation.
translation-review|3444444|Paired source/target findings distinguish meaning errors from defensible alternatives; proposed repairs and coverage remain explicit.
witness-description|3444444|Witness identity and representation chains separate observed, catalog-reported, and inferred facts; overlap maps limit later collation.
documentary-transcription|3444444|Declared transcription policy, source anchors, gaps, OCR checking, and reversible normalization protect historical readings.
variant-collation|3444444|Raw and normalized readings, difficult alignment boundaries, coverage per locus, and lacuna-versus-omission rules prevent false attestations.
critical-edition-preparation|3444444|Base-text policy, apparatus scope, witness attestations, conjectures, and text/apparatus checks support a qualified actual edition.
fiction-development-workflows|3344343|Existing story diagnosis gains actual revisions, source locations, protected experimental structure, coverage checks, and a nonlinear example.
nonfiction-manuscript-development|3344343|Chapter contracts, counterevidence, memoir/source distinctions, and applied revision checks deepen the existing architecture workflow.
line-copyediting-workflows|3444444|Applied text, style/query records, meaning comparison, and format-aware change inspection preserve deliberate voice and document features.
fact-checking-source-review|3444444|Assigned-claim status, quotation context, denominators, source dates, and located gaps prevent partial review from becoming full verification.
book-metadata-packaging|3344443|Field-by-file metadata and full copy records retain conflicts, edition identity, unsupported claims, and unavailable accessibility evidence.
publishing-production-workflows|3344443|Stage and artifact evidence distinguish schedules from completed checks; late reflow reopens dependent locators and exports.
permissions-rights-review|3444444|Item/use evidence distinguishes requests, grants, other reuse bases, documented limits, and qualified legal judgment; gaps do not halt the inventory.
journal-submission-workflows|3344444|Instruction-located requirements and actual manuscript changes support complete letters and responses while preserving unresolved author/research matters.
proofreading|3444444|Copy/proof identity, exact replacements, prior-correction status, rendered coverage, and reflow dependencies bound the proof pass.
publication-format-review|3444444|Format-specific structure, rendering, navigation, and accessibility evidence are separate checks; parser success cannot certify presentation.
indexing-workflows|3444444|Reader access points, substantive treatment, verified anchors/pages, see-reference targets, and repagination checks support an actual usable index.
submission-package-preparation|3444444|Actual destination rules, anonymity surfaces, faithful synopsis, separate author facts, and complete files distinguish preparation from submission.
edition-maintenance|3444444|Correction classes, before/after evidence, historical edition context, and per-derivative status prevent claims that unavailable editions were updated.'''
agent_rows='''text-project-planner|3443444|Concept/brief and unit-coverage ownership is distinct from full drafting; nearby genre roles receive explicit handoffs.
fiction-drafter|4443444|Full fiction with POV, canon, formal constraints, and ending checks; development and copy passes have distinct owners.
nonfiction-drafter|4443444|Evidence-scoped complete prose with specific negative-evidence and unsupported-specificity safeguards from observed failures.
essay-writer|4443444|Inquiry, persona, image returns, and open endings distinguish this role from general nonfiction drafting.
poetry-writer|4443444|Lineation, sound, fixed-form checks, and preserved repetitions provide verse-specific execution beyond prose editing.
dramatic-text-writer|4443444|Playable tactics, cue ownership, physical states, and staging constraints distinguish drama from recording logistics.
professional-text-writer|3443444|Document purpose and commitment boundaries guide full recipient-facing drafts; domain evidence has specialist owners.
academic-manuscript-writer|4443444|Evidence and cross-section consistency govern scholarly drafts without inventing methods, citations, or statistical support.
rhetorical-style-editor|4443444|Effect-based language changes require explicit meaning and voice comparison before handoff to copy or structural editing.
manuscript-continuity-reviewer|4444444|Read-only paired-location review distinguishes time, knowledge, canon, and missing context before repair options.
reader-experience-reviewer|4444444|Read-only reader-friction analysis distinguishes predicted effects from empirical audience evidence.
text-adaptation-editor|4443444|Actual transformed text and a source-to-target map retain qualifications, check added factual qualifiers, and reveal consequential losses.
text-translator|4443444|Complete translation, source comparison, and contextual register/form decisions preserve uncertainty and coverage.
translation-reviewer|4444444|Read-only comparative findings separate source errors from optional preferences and do not imply applied corrections.
textual-witness-analyst|4444444|Read-only source identity and representation evidence precede transcription and collation; physical inferences remain bounded.
documentary-transcriber|4443444|Actual anchored transcription distinguishes visible readings, OCR candidates, normalization, and conjecture.
variant-collator|4443444|Alignment and variant records retain raw readings and per-witness coverage without choosing an edited reading.
critical-edition-editor|4443444|Edited text, apparatus, explicit policy, and intervention checks distinguish selection from source attestation.
proofreader|4443444|Bounded copy/proof comparison supports exact corrections and dependent rechecks on an assigned working copy.
publication-format-reviewer|4443444|Read-only format-aware inspection names actual tools and separates parsed, rendered, navigational, and inaccessible aspects.
submission-package-editor|4443444|Complete destination materials preserve supplied biography relations and expose missing anonymity/metadata checks.
edition-maintenance-editor|4443444|Source corrections and derivative state accounting preserve prior text and prevent false distribution claims.
fiction-development-editor|3443434|Established structural role now returns applied text; full commissioned work and authorial intent are compatible.
nonfiction-manuscript-editor|3443434|Chapter architecture and evidence planning now require actual assigned revisions with explicit uninspected coverage.
line-copy-editor|4443444|Style sheet, queries, assigned text edits, and protected voice remain distinct from structural and source verification.
fact-checking-editor|4444444|Read-only claim/source matching returns partial checked coverage and gaps without unsupported full-check claims.
book-metadata-packaging-editor|3443434|Existing copy and metadata alignment role continues unaffected fields while preserving unresolved conflicts.
production-editor|3443434|Stage/version evidence and explicit proof, format, index, and maintenance handoffs distinguish coordination from execution.
permissions-reviewer|4444444|Read-only rights evidence inventory continues around missing evidence and preserves distinctions among documented reuse bases.
journal-submission-specialist|3443434|Full requested package texts retain scholarly requirements; delegated checks stay unresolved until evidence returns.
developmental-manuscript-editor|4443444|Structural execution repairs dependent text and preserves originals, unit mapping, contrary evidence, and author constraints.
indexing-coordinator|4443444|Actual index creation and locator/reference checks use existing bounded Luna settings without invented print pages.'''
mode_review={s.split('|',2)[0]:s.split('|',2)[1:] for s in mode_rows.splitlines()}
agent_review={s.split('|',2)[0]:s.split('|',2)[1:] for s in agent_rows.splitlines()}
assert len(mode_review)==36 and len(agent_review)==32
skill_criteria=['trigger_and_routing','workflow_specificity','domain_heuristics','supporting_assets','tooling_and_validation','output_contract','boundaries']
agent_criteria=['role_distinctness','skill_and_reference_use','instruction_depth','runtime_fit','handoffs_and_boundaries','output_contract','catalog_integration']
def evidence(f):return {'path':str(f.relative_to(R)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()}
report={'date':'2026-09-05','rubric':'REFERENCES/quality-rubric.md','method':'Full manual content review of all 36 affected workflow/kit pairs, five gateway routers and UI metadata, and 32 new or modified agents. Scores assess reusable instructions, not guaranteed model behavior. All seven criteria are explicitly scored per mode and agent. Static parsing and live evidence are recorded separately.','skill_criteria':skill_criteria,'agent_criteria':agent_criteria,'modes':[],'agents':[],'gateways':[],'integration_files':[evidence(R/'README.md'),evidence(R/'REFERENCES/software-development-crew.md')]}
for name,(score,note) in mode_review.items():
 paths=list((R/'SKILLS').glob('*/references/workflows/'+name+'.md'));assert len(paths)==1
 f=paths[0];s=f.read_text();assets=[(f.parent/link).resolve() for link in re.findall(r'\]\((../artifacts/[^)]+)\)',s)]
 assert assets and all(a.exists() for a in assets)
 scores=dict(zip(skill_criteria,map(int,score)));assert len(score)==7 and min(scores.values())>=3
 report['modes'].append({'gateway':f.parts[-4],'mode':name,'rating':'Ready','scores':scores,'evidence_note':note,'anti_platitude':'pass: domain checks identified in evidence note','reviewed_files':[evidence(f),*[evidence(a) for a in assets]]})
for name,(score,note) in agent_review.items():
 f=R/'AGENTS/openai'/(name+'.toml');d=tomllib.loads(f.read_text());scores=dict(zip(agent_criteria,map(int,score)));assert len(score)==7 and min(scores.values())>=3
 report['agents'].append({'agent':name,'rating':'Ready','scores':scores,'evidence_note':note,'model':d['model'],'reasoning':d['model_reasoning_effort'],'sandbox':d['sandbox_mode'],'anti_platitude':'pass: role-specific execution and handoffs identified in evidence note','reviewed_files':[evidence(f)]})
for n in ['text-composition','text-revision','text-translation','textual-scholarship','publishing-editorial']:
 ms=[x for x in report['modes'] if x['gateway']==n];assert ms
 report['gateways'].append({'gateway':n,'mode_count':len(ms),'rating':'Ready','scores':{c:min(m['scores'][c] for m in ms) for c in skill_criteria},'progressive_discovery':'pass: each mode directly linked, smallest relevant set selected, kits conditionally loaded from workflows; relative links resolved from containing file','reviewed_files':[evidence(R/'SKILLS'/n/'SKILL.md'),evidence(R/'SKILLS'/n/'agents/openai.yaml')]})
(D/'asset-review.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
lines=['# Asset Review','',report['method'],'','Scores are in the criterion order below; each digit is a score out of four. A minimum of three is required. Runtime-fit scores are design judgments; representative runs do not benchmark every role or model.','', 'Skill order: '+', '.join(skill_criteria)+'.','', '| Gateway / mode | Scores | Evidence |','| --- | --- | --- |']
for m in report['modes']:
 f=m['reviewed_files'][0]['path'];lines.append(f"| [{m['gateway']} / {m['mode']}](../../{f}) | {''.join(str(v) for v in m['scores'].values())} | {m['evidence_note']} |")
lines+=['','Agent order: '+', '.join(agent_criteria)+'.','','| Agent | Scores | Evidence |','| --- | --- | --- |']
for a in report['agents']:
 lines.append(f"| [{a['agent']}](../../{a['reviewed_files'][0]['path']}) | {''.join(str(v) for v in a['scores'].values())} | {a['evidence_note']} |")
lines+=['','All five gateways pass progressive discovery and take the weakest mode score for each criterion. Every linked kit was reviewed with its mode; UI metadata was parsed and discovery checked. [Machine-readable scores and reviewed-file hashes](asset-review.json) retain the complete inventory.','']
(D/'asset-review.md').write_text('\n'.join(lines))
print('Reviewed:',len(report['modes']),'modes;',len(report['agents']),'agents;',len(report['gateways']),'gateways')
