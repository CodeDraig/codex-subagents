# Software Development Crew

This reference catalogs reusable Codex custom-agent examples for software development and specialist professional lifecycles. Copy individual TOML files from `AGENTS/openai/` into a project's `.codex/agents/` directory when that role is useful.

## Lifecycle Map

| Stage | Agents |
| --- | --- |
| Intake and shaping | `triage-router`, `product-discovery-strategist`, `market-researcher`, `technical-planner` |
| Architecture and contracts | `systems-architect`, `api-contract-architect`, `database-modeler` |
| UX and product surface | `ux-flow-architect`, `design-system-engineer`, `accessibility-reviewer`, `localization-engineer` |
| Product implementation | `frontend-experience-engineer`, `backend-domain-engineer`, `ai-feature-engineer`, `prompt-evaluation-engineer`, `data-platform-engineer`, `rapid-prototype-scout`, `implementation-finisher` |
| Data, analytics, and ML execution | `data-scientist`, `analytics-engineer`, `ml-engineer`, `mlops-engineer`, `software-engineering-lead` |
| Risk and quality | `security-threat-modeler`, `security-fix-engineer`, `privacy-compliance-reviewer`, `performance-investigator`, `performance-optimizer`, `test-strategy-architect`, `test-automation-engineer`, `code-reviewer`, `refactor-surgeon` |
| Shipping and operations | `build-release-engineer`, `devops-platform-engineer`, `observability-incident-engineer`, `documentation-engineer`, `developer-experience-engineer`, `dependency-maintenance-engineer` |
| Open Source Intelligence | `osint-research-lead`, `source-verification-analyst`, `geolocation-chronolocation-analyst`, `public-records-researcher`, `social-network-analyst`, `misinformation-risk-analyst` |
| Technical Support | `support-triage-specialist`, `customer-diagnostics-engineer`, `escalation-support-engineer`, `knowledge-base-author`, `support-automation-engineer`, `customer-communications-specialist` |
| News Site Staff | `assignment-editor`, `breaking-news-reporter`, `news-fact-checker`, `copy-desk-editor`, `audience-seo-editor`, `standards-ethics-editor` |
| Legal and Regulatory Operations | `legal-research-analyst`, `contract-review-specialist`, `regulatory-monitor`, `records-retention-advisor`, `legal-ops-coordinator` |
| Academic and Research Support | `literature-reviewer`, `research-methods-reviewer`, `citation-integrity-checker`, `research-data-curator`, `peer-review-prep-editor` |
| Grants and Sponsored Projects | `grant-opportunity-scout`, `proposal-compliance-reviewer`, `budget-justification-writer`, `sponsored-projects-coordinator`, `grant-reporting-specialist` |
| Finance and Accounting Operations | `financial-model-reviewer`, `accounting-controls-reviewer`, `invoice-reconciliation-specialist`, `audit-evidence-organizer`, `budget-variance-analyst` |
| Procurement and Vendor Management | `rfp-response-analyst`, `vendor-risk-reviewer`, `procurement-compliance-specialist`, `sow-reviewer`, `vendor-scorecard-analyst` |
| Policy and Public Affairs | `policy-analyst`, `public-comment-drafter`, `stakeholder-map-analyst`, `legislative-tracker`, `impact-assessment-writer` |
| Publishing and Scholarly Production | `developmental-manuscript-editor`, `production-editor`, `permissions-reviewer`, `indexing-coordinator`, `journal-submission-specialist` |
| Book and Long-Form Production | `fiction-development-editor`, `nonfiction-manuscript-editor`, `line-copy-editor`, `fact-checking-editor`, `book-metadata-packaging-editor` |
| Education And Training | `curriculum-designer`, `lesson-materials-author`, `assessment-designer`, `learning-accessibility-reviewer`, `training-evaluation-analyst` |
| Archives And Collections | `accession-intake-coordinator`, `collection-description-specialist`, `digital-preservation-planner`, `collection-access-reviewer`, `exhibit-interpretation-writer` |
| Video And Audio Production | `production-brief-planner`, `script-development-editor`, `recording-preparation-coordinator`, `postproduction-coordinator`, `media-delivery-reviewer` |
| Text Composition | `text-project-planner`, `fiction-drafter`, `nonfiction-drafter`, `essay-writer`, `poetry-writer`, `dramatic-text-writer`, `professional-text-writer`, `academic-manuscript-writer` |
| Text Revision | `rhetorical-style-editor`, `manuscript-continuity-reviewer`, `reader-experience-reviewer`, `text-adaptation-editor` |
| Text Translation | `text-translator`, `translation-reviewer` |
| Textual Scholarship | `textual-witness-analyst`, `documentary-transcriber`, `variant-collator`, `critical-edition-editor` |
| Publication Completion And Edition Maintenance | `proofreader`, `publication-format-reviewer`, `submission-package-editor`, `edition-maintenance-editor` |
| Archaeological Fieldwork | `archaeological-project-planner`, `archaeological-recording-specialist`, `stratigraphic-sequence-reviewer`, `archaeological-finds-coordinator`, `archaeological-report-author` |
| Language Documentation | `language-documentation-planner`, `linguistic-session-designer`, `linguistic-annotation-editor`, `lexicon-corpus-curator`, `language-deposit-coordinator` |
| Oral History | `oral-history-project-planner`, `oral-history-interview-designer`, `oral-history-transcript-editor`, `oral-history-access-reviewer`, `oral-history-interpretation-editor` |
| Heritage Conservation | `conservation-condition-reviewer`, `preventive-conservation-planner`, `conservation-treatment-reviewer`, `historic-fabric-recording-specialist`, `site-conservation-planner`, `conservation-monitoring-coordinator` |

## Routing Rules

Use this crew before falling back to generic `worker` or `explorer`.

| Task Signal | Prefer |
| --- | --- |
| Ambiguous request, routing, scope split | `triage-router` |
| Fuzzy product idea, user problem, acceptance criteria | `product-discovery-strategist` |
| Competitor, ecosystem, or external-product research | `market-researcher` |
| Approved design needs execution plan | `technical-planner` |
| Cross-module architecture, service boundaries, migration path | `systems-architect` |
| API, event, webhook, SDK, schema, or integration contract | `api-contract-architect` |
| Data model, migration, indexing, retention, lineage | `database-modeler` |
| User workflow, interaction states, UX copy | `ux-flow-architect` |
| Shared UI components, tokens, visual consistency | `design-system-engineer` |
| Frontend workflow implementation | `frontend-experience-engineer` |
| Backend service/domain implementation | `backend-domain-engineer` |
| AI product behavior, prompts, retrieval, tool use | `ai-feature-engineer` |
| AI eval datasets, judge rubrics, prompt regression checks | `prompt-evaluation-engineer` |
| Data pipelines, analytics, warehouse, reporting | `data-platform-engineer` |
| Exploratory analysis, statistical framing, experiment interpretation | `data-scientist` |
| Metric contracts, semantic models, BI transformations, dashboards | `analytics-engineer` |
| Model training, inference code, feature pipelines, ML eval harnesses | `ml-engineer` |
| Model registry, release controls, drift, monitoring, rollback | `mlops-engineer` |
| Multi-slice implementation sequencing, integration risk, delivery coherence | `software-engineering-lead` |
| Quick feasibility spike or throwaway prototype | `rapid-prototype-scout` |
| Last-mile integration and cleanup | `implementation-finisher` |
| Security design, trust boundaries, abuse cases | `security-threat-modeler` |
| Bounded security remediation patch | `security-fix-engineer` |
| Privacy, retention, consent, personal data handling | `privacy-compliance-reviewer` |
| Performance diagnosis before code changes | `performance-investigator` |
| Focused performance fix after evidence exists | `performance-optimizer` |
| Test strategy and risk matrix | `test-strategy-architect` |
| Add or repair executable tests | `test-automation-engineer` |
| Diff review for correctness and regressions | `code-reviewer` |
| Behavior-preserving cleanup | `refactor-surgeon` |
| Build, package, release, rollback, migration readiness | `build-release-engineer` |
| CI, deployment automation, infrastructure, secrets plumbing | `devops-platform-engineer` |
| Logs, metrics, traces, alerts, runbooks, incidents | `observability-incident-engineer` |
| User, developer, operator, or reviewer docs | `documentation-engineer` |
| Local setup, scripts, fixtures, linting, DX | `developer-experience-engineer` |
| Dependency upgrades, advisories, lockfiles | `dependency-maintenance-engineer` |
| Accessibility review | `accessibility-reviewer` |
| Localization and internationalization readiness | `localization-engineer` |
| Lawful public-source investigation planning | `osint-research-lead` |
| Claim verification, provenance, corroboration | `source-verification-analyst` |
| Public imagery location or time analysis | `geolocation-chronolocation-analyst` |
| Official records, filings, dockets, registries | `public-records-researcher` |
| Public social-media coordination or network analysis | `social-network-analyst` |
| Misinformation, manipulated media, rumor assessment | `misinformation-risk-analyst` |
| Support queue triage, severity, routing | `support-triage-specialist` |
| Customer logs, repro, diagnostic hypotheses | `customer-diagnostics-engineer` |
| Complex support escalation ownership | `escalation-support-engineer` |
| Support KB articles and troubleshooting docs | `knowledge-base-author` |
| Support tooling, macros, diagnostic automation | `support-automation-engineer` |
| Customer-safe support replies and updates | `customer-communications-specialist` |
| News assignment planning and source list | `assignment-editor` |
| Fast sourced breaking-news draft or update | `breaking-news-reporter` |
| News copy fact-checking and claim verification | `news-fact-checker` |
| News copy editing, headlines, captions | `copy-desk-editor` |
| News SEO, audience, social, newsletter packaging | `audience-seo-editor` |
| Newsroom ethics, standards, fairness, privacy | `standards-ethics-editor` |
| Source-backed legal or regulatory research, issue spotting, authority map | `legal-research-analyst` |
| Contract clauses, obligations, dates, risk flags, owner questions | `contract-review-specialist` |
| Regulatory source monitoring, changes, effective dates, owner questions | `regulatory-monitor` |
| Records inventories, retention schedules, disposition workflows, hold flags | `records-retention-advisor` |
| Legal operations intake, matter tracking, source packages, handoffs | `legal-ops-coordinator` |
| Scholarly literature synthesis, evidence themes, disagreements, gaps | `literature-reviewer` |
| Study design, methodology, validity, reproducibility, analysis-plan critique | `research-methods-reviewer` |
| Citation support, quote accuracy, provenance, bibliography defects | `citation-integrity-checker` |
| Research dataset metadata, lineage, reproducibility, sharing readiness | `research-data-curator` |
| Manuscript peer-review preparation, argument gaps, reviewer questions | `peer-review-prep-editor` |
| Grant opportunity fit, eligibility signals, deadlines, review criteria | `grant-opportunity-scout` |
| Grant solicitation requirements, compliance matrices, attachment checks | `proposal-compliance-reviewer` |
| Grant budget narratives, cost assumptions, sponsor restrictions | `budget-justification-writer` |
| Sponsored-project reporting calendars, deliverables, closeout coordination | `sponsored-projects-coordinator` |
| Grant progress-report inputs, evidence gaps, closeout items | `grant-reporting-specialist` |
| Financial model assumptions, formula risks, source ties | `financial-model-reviewer` |
| Accounting control design, evidence expectations, remediation questions | `accounting-controls-reviewer` |
| Invoice, PO, receipt, approval, payment matching and exceptions | `invoice-reconciliation-specialist` |
| Audit evidence inventories, request lists, traceability maps | `audit-evidence-organizer` |
| Budget-to-actual variance drivers, evidence gaps, assumption changes | `budget-variance-analyst` |
| RFP parsing, response matrices, owner assignments, package checks | `rfp-response-analyst` |
| Vendor risk evidence, specialist handoffs, diligence questions | `vendor-risk-reviewer` |
| Procurement policy requirements, approvals, exceptions, sourcing evidence | `procurement-compliance-specialist` |
| Statement-of-work deliverables, milestones, acceptance criteria, ambiguities | `sow-reviewer` |
| Vendor comparison scorecards, disclosed criteria, evidence gaps | `vendor-scorecard-analyst` |
| Source-backed policy analysis, issue maps, impacts, tradeoffs | `policy-analyst` |
| Public comments, testimony, consultation responses, submission checklists | `public-comment-drafter` |
| Stakeholder group mapping, aggregate interests, impact blind spots | `stakeholder-map-analyst` |
| Bills, amendments, hearings, votes, effective dates, official source logs | `legislative-tracker` |
| Policy impact assessments, costs, benefits, assumptions, evidence gaps | `impact-assessment-writer` |
| Applied structural revision, argument and chapter flow, unit mapping, and dependent text repairs | `developmental-manuscript-editor` |
| Fiction premise, plot, character arcs, continuity, genre promise, revision diagnosis and execution | `fiction-development-editor` |
| Nonfiction thesis, proposal, chapter architecture, reader promise, evidence plan | `nonfiction-manuscript-editor` |
| Line edits, copyedits, style sheets, query logs, consistency passes | `line-copy-editor` |
| Long-form claim checking against source packets, interviews, datasets, author notes | `fact-checking-editor` |
| Book metadata, back-cover copy, categories, keywords, accessibility fields, package gaps | `book-metadata-packaging-editor` |
| Production editing, style sheets, proof stages, schedules, query logs | `production-editor` |
| Third-party content permissions, license restrictions, attribution needs | `permissions-reviewer` |
| Actual index creation and revision, substantive term selection, verified locators, and cross-reference checks | `indexing-coordinator` |
| Journal submission packages, metadata gaps, disclosures, response matrices | `journal-submission-specialist` |
| Designs learning outcomes, prerequisites, instructional sequences, and assessment alignment for courses or training programs before lesson authoring. | `curriculum-designer` |
| Authors timed lesson plans, learner activities, worked examples, and facilitator notes from supplied learning outcomes and source material. | `lesson-materials-author` |
| Designs assessment blueprints, items, answer rationales, and scoring rubrics aligned to learning outcomes without grading individual learners. | `assessment-designer` |
| Reviews learning materials and activities for participation barriers, usable alternatives, and verification needs without certifying accessibility or deciding individual accommodations. | `learning-accessibility-reviewer` |
| Plans training evaluation and interprets supplied participation, learning, transfer, and outcome evidence without inventing effectiveness or causal claims. | `training-evaluation-analyst` |
| Prepares collection intake inventories, provenance and transfer evidence, condition notes, and accession questions without authorizing acquisition or changing ownership. | `accession-intake-coordinator` |
| Creates hierarchical collection descriptions, finding-aid drafts, and terminology decisions from supplied inventories while preserving provenance and original-order evidence. | `collection-description-specialist` |
| Plans fixity, format-risk review, storage independence, recovery verification, and reversible migration for digital collections without altering original assets. | `digital-preservation-planner` |
| Reviews collection access requests against supplied donor terms, restrictions, privacy concerns, and institutional policy without authorizing release or resolving legal conflicts. | `collection-access-reviewer` |
| Writes source-backed exhibit narratives, object labels, and accessible interpretive alternatives from collection evidence without inventing provenance or granting publication clearance. | `exhibit-interpretation-writer` |
| Plans video and audio production briefs, deliverables, schedules, dependencies, and resource assumptions before scripting or recording. | `production-brief-planner` |
| Develops and edits video or audio scripts for audience, spoken timing, visual or sound cues, continuity, and factual support. | `script-development-editor` |
| Prepares shot and recording lists, session logistics, equipment checks, asset needs, and readiness notes without booking resources or directing unsafe production. | `recording-preparation-coordinator` |
| Organizes media inventories, edit instructions, synchronization notes, versions, and review handoffs while preserving original recordings. | `postproduction-coordinator` |
| Reviews video and audio delivery packages against supplied technical specifications, content versions, caption and transcript coverage, and approval evidence. | `media-delivery-reviewer` |
| Develops writing briefs, concept alternatives, unit coverage, and stage-specific handoffs from an idea or commission. | `text-project-planner` |
| Writes complete fiction drafts and scene or chapter revisions with controlled viewpoint, continuity, formal choices, and ending consequences. | `fiction-drafter` |
| Produces complete nonfiction drafts with coherent argument or narrative, explicit source status, and preserved factual qualifications. | `nonfiction-drafter` |
| Writes complete personal, reflective, critical, lyric, and braided essays with controlled inquiry, persona, and associative structure. | `essay-writer` |
| Composes and revises complete poems or lyrics through sound, image, lineation, stanza movement, and explicit formal constraints. | `poetry-writer` |
| Writes complete dramatic texts with playable action, subtext, distinct speech, staging constraints, and scene continuity. | `dramatic-text-writer` |
| Drafts complete professional documents around reader decisions, evidence, medium conventions, and accurately bounded commitments. | `professional-text-writer` |
| Drafts complete scholarly manuscripts or sections from supplied research with consistent claims, source provenance, and visible evidence gaps. | `academic-manuscript-writer` |
| Revises cadence, emphasis, syntax, figurative language, and register while preserving meaning and deliberate authorial effects. | `rhetorical-style-editor` |
| Checks located manuscript contradictions in time, entities, knowledge, terminology, and repeated claims with explicit coverage limits. | `manuscript-continuity-reviewer` |
| Reviews reader orientation, comprehension, engagement, and textual access barriers without inventing audience evidence. | `reader-experience-reviewer` |
| Creates complete audience, medium, length, and purpose adaptations with traceable omissions, additions, and preserved source meaning. | `text-adaptation-editor` |
| Produces complete translations and revisions that preserve source meaning, register, ambiguity, and form with explicit material tradeoffs. | `text-translator` |
| Reviews aligned source and translation for omissions, meaning changes, register, terminology, and form with located corrections and coverage limits. | `translation-reviewer` |
| Describes textual witnesses, representation chains, passage coverage, and uncertain provenance before transcription or collation. | `textual-witness-analyst` |
| Transcribes supplied textual sources with stable anchors, declared normalization policy, and visible uncertain or editorial readings. | `documentary-transcriber` |
| Aligns textual witnesses and records variants, omissions, transpositions, and coverage under a declared comparison policy. | `variant-collator` |
| Prepares edited texts, critical apparatus, and editorial introductions with explicit source support, selection policy, and intervention records. | `critical-edition-editor` |
| Checks final copy and proofs for residual text errors, missed corrections, and reflow-dependent issues with exact correction locations. | `proofreader` |
| Reviews publication files for format structure, rendering, navigation, and accessibility evidence without conflating parsing with presentation quality. | `publication-format-reviewer` |
| Prepares complete submission letters, synopses, biographies, component sets, and destination-specific checks from verified manuscript and author facts. | `submission-package-editor` |
| Applies documented corrections and revised-edition changes while tracking source versions, derivative dependencies, and actual update coverage. | `edition-maintenance-editor` |
| Produces archaeological research designs linking questions, investigation coverage, sampling, recording, post-fieldwork analysis, and archive requirements. | `archaeological-project-planner` |
| Builds traceable context, spatial, photograph, and sample registers from supplied archaeological observations while preserving observation and interpretation separately. | `archaeological-recording-specialist` |
| Reviews context relationships and proposed archaeological sequences for cycles, missing references, unsupported equivalences, and uncertainty before grouping or dating. | `stratigraphic-sequence-reviewer` |
| Reconciles finds and sample inventories with archaeological contexts, container identifiers, movement records, conservation flags, and archive requirements. | `archaeological-finds-coordinator` |
| Writes archaeological reports that connect research questions to inspected records, distinguish observation from interpretation, and prepare traceable archive handoffs. | `archaeological-report-author` |
| Creates language documentation plans connecting community priorities, speaker and genre coverage, recording sessions, annotation capacity, access terms, and useful return materials. | `language-documentation-planner` |
| Designs language documentation sessions with traceable prompts, natural-context tasks, participant review points, and recording metadata without manufacturing linguistic responses. | `linguistic-session-designer` |
| Produces or edits source-linked language transcripts and annotation tiers while keeping attested forms, segmentation, glosses, translations, and uncertainty distinct. | `linguistic-annotation-editor` |
| Builds lexical and corpus records with attestation links, sense distinctions, variety information, analytical uncertainty, and reversible deduplication proposals. | `lexicon-corpus-curator` |
| Prepares language recording and annotation deposits with manifests, participant metadata, resource relationships, access decisions, and community-return copies. | `language-deposit-coordinator` |
| Develops oral-history project designs linking historical questions, narrator coverage, interview preparation, review processes, stewardship, and intended uses. | `oral-history-project-planner` |
| Creates historically grounded oral-history interview guides with open prompts, source-aware follow-ups, narrator choice, and recording/review preparation. | `oral-history-interview-designer` |
| Edits oral-history transcripts into traceable reading or documentary versions while preserving narrator meaning, source anchors, speech conventions, and unresolved hearing. | `oral-history-transcript-editor` |
| Reviews oral-history agreements, narrator decisions, transcript versions, excerpts, and proposed uses to identify supported access, conflicts, and unresolved release conditions. | `oral-history-access-reviewer` |
| Builds source-linked oral-history narratives, excerpts, and editions that preserve context, distinguish memory from corroboration, and respect documented use restrictions. | `oral-history-interpretation-editor` |
| Reviews supplied condition records for objects or historic fabric, separating observations, material identifications, deterioration hypotheses, and inspection limits. | `conservation-condition-reviewer` |
| Creates evidence-based preventive-care plans for collections and historic interiors, linking material sensitivities, environmental exposure, handling, storage, and review priorities. | `preventive-conservation-planner` |
| Reviews proposed conservation interventions against condition evidence, significance, material compatibility, prior treatment, alternatives, and documentation requirements. | `conservation-treatment-reviewer` |
| Builds traceable records of historic building and site fabric, separating observed configuration, material descriptions, alteration evidence, phase interpretation, and inspection coverage. | `historic-fabric-recording-specialist` |
| Develops conservation plans for archaeological places and historic structures linking significance, fabric condition, site pressures, management options, and staged decisions. | `site-conservation-planner` |
| Organizes repeatable condition monitoring and maintenance records for objects and historic places, separating measured change, comparison limits, triggers, and completed work. | `conservation-monitoring-coordinator` |

## Text Composition and Editing Lifecycle

Select the stage and deliverable actually requested. A project can enter at any stage; full drafting or applied revision must produce the text, not only a plan. Use stable unit/version references for long works and report actual coverage.

| Stage | Primary routing | Result |
| --- | --- | --- |
| Conception, brief, source synthesis, outline | `text-project-planner`, `$text-composition`; existing research specialists supply domain evidence. | Working brief, source/outline map, next writing task. |
| Complete composition | `fiction-drafter`, `nonfiction-drafter`, `essay-writer`, `poetry-writer`, `dramatic-text-writer`, `professional-text-writer`, `academic-manuscript-writer`. | Complete requested text with source/form checks and remaining-unit coverage. |
| Development and revision | Existing fiction/nonfiction development roles; `developmental-manuscript-editor` uses `$text-revision` for applied structural work. | Located diagnosis, revision plan, reconciled feedback, or actual revised text as assigned. |
| Language, continuity, reader orientation, adaptation | `rhetorical-style-editor`, `line-copy-editor`, `manuscript-continuity-reviewer`, `reader-experience-reviewer`, `text-adaptation-editor`. | Applied language changes or evidence-backed review; source-to-target adaptation map. |
| Translation | `text-translator`, `translation-reviewer`, `$text-translation`. | Complete translation, terminology/treatment record, located comparative findings. |
| Textual scholarship | `textual-witness-analyst`, `documentary-transcriber`, `variant-collator`, `critical-edition-editor`. | Witness register, anchored transcription, variants, edited text and apparatus. |
| Verification and production | Existing fact/citation/rights specialists; `production-editor`, `proofreader`, `publication-format-reviewer`, `indexing-coordinator`. | Claim/rights evidence, correction records, actual format checks, verified or provisional index. |
| Packaging and submission preparation | `book-metadata-packaging-editor`, `submission-package-editor`, `journal-submission-specialist`. | Complete requested package texts and destination-specific component checks. |
| Corrections and new editions | `edition-maintenance-editor` with production, translation, indexing, and format reviewers as needed. | Revised source, edition/correction log, actual derivative-update status. |

Existing `documentation-engineer` and `knowledge-base-author` own product documentation; newsroom roles own reporting and news copy; education, grant, policy, archives, and video/audio roles retain their domain-specific work. Broad composition roles draft from that evidence rather than claiming those checks themselves.

## Heritage and Fieldwork Lifecycle

Use these categories for domain-specific records, planning, editing, and review. Projects can enter at any stage; missing evidence permits a bounded deliverable with unresolved items. Field observations, linguistic analysis, narrator decisions, and conservation diagnoses must remain distinguishable from proposals.

| Category | Gateway and stages | Deliverables |
| --- | --- | --- |
| Archaeology | `$archaeological-fieldwork`: project design, field recording, stratigraphic review, finds registers, post-fieldwork reporting. | Evidence-to-method plans, context and finds records, located sequence findings, actual reports, archive handoffs. |
| Language documentation | `$language-documentation`: planning, session design, transcription/annotation, lexicon curation, archive preparation. | Session guides, source-linked tiers and lexical entries, access-aware manifests, community-return packages. |
| Oral history | `$oral-history`: project planning, interview preparation, transcript editing, narrator review/access, interpretation/edition. | Interview guides, complete edited transcripts and editions, version-specific access matrices, traceable excerpts. |
| Heritage conservation | `$heritage-conservation`: condition assessment, preventive care, treatment-proposal review, historic fabric recording, site conservation planning, monitoring/maintenance. | Condition evidence, care and site plans, proposal findings, component records, comparable monitoring logs. |

These 21 agents use 21 workflows and 21 artifact kits. Conservation includes movable objects, archaeological sites, and historic building fabric. Four reviewers use `gpt-5.6-sol/high` with read-only sandboxes; three record coordinators use `gpt-5.6-terra/medium`; the remaining authors use `gpt-5.6-terra/high` with workspace-write sandboxes for assigned local artifacts. External deposits, publication, physical interventions, and institutional decisions require their own applicable authorization.

The [verification record](../docs/heritage-fieldwork-verification.md) separates complete asset review, catalog structure, runtime discovery, and eight representative live scenarios.

## Model Coverage

The 154 templates in `AGENTS/openai/` are distributed as follows:

| Model | Reasoning Effort | Agent Templates | Representative Agents |
| --- | --- | ---: | --- |
| `gpt-5.6-sol` | `high` | 20 | `accounting-controls-reviewer`, `citation-integrity-checker`, `source-verification-analyst` |
| `gpt-5.6-sol` | `xhigh` | 4 | `systems-architect`, `security-threat-modeler`, `product-discovery-strategist`, `osint-research-lead` |
| `gpt-5.6-terra` | `low` | 2 | `dependency-maintenance-engineer`, `triage-router` |
| `gpt-5.6-terra` | `medium` | 38 | `documentation-engineer`, `peer-review-prep-editor`, `accessibility-reviewer` |
| `gpt-5.6-terra` | `high` | 76 | `backend-domain-engineer`, `security-fix-engineer`, `software-engineering-lead` |
| `gpt-5.6-luna` | `medium` | 11 | `audience-seo-editor`, `copy-desk-editor`, `support-triage-specialist` |
| `gpt-5.3-codex-spark` | `low` | 1 | `rapid-prototype-scout` |
| `gpt-5.3-codex-spark` | `medium` | 1 | `developer-experience-engineer` |
| `gpt-5.3-codex-spark` | `high` | 1 | `test-automation-engineer` |

## Intentional Overlap

Some domains have paired agents because model capability and latency change the right behavior.

| Domain | Thinking Agent | Execution Agent |
| --- | --- | --- |
| Security | `security-threat-modeler` uses `gpt-5.6-sol` with `xhigh` reasoning for threat modeling and attack-path analysis. | `security-fix-engineer` uses `gpt-5.6-terra` with `high` reasoning for bounded remediation patches. |
| Performance | `performance-investigator` uses `gpt-5.6-terra` with `high` reasoning to design initial measurements or repair confounded measurement plans, then interpret valid evidence and isolate causes. Missing measurements block diagnosis and optimization recommendations, not measurement planning. | `performance-optimizer` uses `gpt-5.6-terra` with `high` reasoning to implement focused optimizations. |
| Testing | `test-strategy-architect` uses `gpt-5.6-terra` with `high` reasoning to design risk-based coverage. | `test-automation-engineer` remains on `gpt-5.3-codex-spark` with `high` reasoning to quickly add executable tests. |
| Architecture | `systems-architect` uses `gpt-5.6-sol` with `xhigh` reasoning for durable system boundaries. | `rapid-prototype-scout` remains on `gpt-5.3-codex-spark` with `low` reasoning to test feasibility quickly. |
| News verification | `news-fact-checker` uses `gpt-5.6-terra` with `high` reasoning for publication risk. | `copy-desk-editor` uses `gpt-5.6-luna` with `medium` reasoning for line edits and packaging. |
| Support operations | `escalation-support-engineer` uses `gpt-5.6-terra` with `high` reasoning for complex cases. | `support-automation-engineer` uses `gpt-5.6-terra` with `high` reasoning for support tooling. |
| OSINT | `osint-research-lead` uses `gpt-5.6-sol` with `xhigh` reasoning for lawful scope and synthesis. | `source-verification-analyst` uses `gpt-5.6-sol` with `high` reasoning for claim-level corroboration. |
| Data platform vs analysis | `data-scientist` uses `gpt-5.6-terra` with `high` reasoning for exploratory analysis, experiment interpretation, and evidence-backed recommendations. | `data-platform-engineer` uses `gpt-5.6-terra` with `high` reasoning for production ingestion, transformation, warehouse, lakehouse, lineage, backfill, and reporting implementation. |
| Analytics semantics vs data modeling | `analytics-engineer` uses `gpt-5.6-terra` with `high` reasoning for metric contracts, semantic models, dashboards, and BI-ready transformations. | `database-modeler` uses `gpt-5.6-terra` with `high` reasoning for persistence shape, indexing, retention, migrations, and durable data ownership decisions. |
| ML delivery vs ML operations | `ml-engineer` uses `gpt-5.6-terra` with `high` reasoning for training, inference, feature pipelines, and eval harnesses. | `mlops-engineer` uses `gpt-5.6-terra` with `high` reasoning for registry, release controls, drift, monitoring, reproducibility, rollback, and production model readiness. |
| Engineering execution | `software-engineering-lead` uses `gpt-5.6-terra` with `high` reasoning for read-only delivery sequencing, integration risk, validation gates, and handoff review. | `technical-planner` creates durable implementation plans, while `systems-architect` on `gpt-5.6-sol` owns architecture decisions and long-term system boundaries. |
| Legal research vs public records | `legal-research-analyst` uses `gpt-5.6-sol` with `high` reasoning for source-backed legal/regulatory research, issue spotting, authority maps, caveats, and counsel questions. | `public-records-researcher` on `gpt-5.6-terra` owns official record, docket, registry, filing, and entity-disambiguation searches. |
| Contract review vs privacy/security/procurement | `contract-review-specialist` uses `gpt-5.6-sol` with `high` reasoning for clause extraction, obligations, operational impacts, and owner questions. | `privacy-compliance-reviewer`, `vendor-risk-reviewer`, `procurement-compliance-specialist`, and `sow-reviewer` use `gpt-5.6-sol` for their high-stakes review slices. |
| Regulatory monitoring vs policy analysis | `regulatory-monitor` uses `gpt-5.6-terra` with `high` reasoning for official source monitoring, changes, effective dates, and owner questions. | `policy-analyst`, `public-comment-drafter`, `stakeholder-map-analyst`, `legislative-tracker`, and `impact-assessment-writer` use `gpt-5.6-terra` for policy-position, stakeholder, and public-affairs artifacts. |
| Records retention operations | `records-retention-advisor` uses `gpt-5.6-terra` with `medium` reasoning for retention inventories, schedules, hold flags, disposition workflows, and approval gates. | `privacy-compliance-reviewer` on `gpt-5.6-sol` owns privacy law and personal-data implications, while counsel or authorized owners make final retention decisions. |
| Legal operations coordination | `legal-ops-coordinator` uses `gpt-5.6-terra` with `medium` reasoning for intake, matter tracking, source packages, deadlines, owner questions, and routing. | Specialist legal/regulatory agents own research, contract, regulatory, and retention analysis; this role coordinates handoffs without legal judgment. |
| Academic research support | `literature-reviewer` uses `gpt-5.6-terra`; `research-methods-reviewer` and `citation-integrity-checker` use `gpt-5.6-sol` for source-backed synthesis, validity critique, and citation integrity. | `research-data-curator` and `peer-review-prep-editor` use `gpt-5.6-terra` for reproducibility artifacts and manuscript preparation. |
| Grants and sponsored projects | `proposal-compliance-reviewer` uses `gpt-5.6-terra` with `high` reasoning for sponsor compliance matrices. | `budget-justification-writer` and `sponsored-projects-coordinator` use `gpt-5.6-terra`; `grant-reporting-specialist` uses `gpt-5.6-luna` for reporting evidence without official submission authority. |
| Finance and accounting operations | `financial-model-reviewer` and `accounting-controls-reviewer` use `gpt-5.6-sol` for high-stakes model and control review. | `invoice-reconciliation-specialist` and `audit-evidence-organizer` use `gpt-5.6-terra` for operational artifacts; none provide tax, investment, legal, valuation, or audit-opinion advice. |
| Procurement and vendor management | `vendor-risk-reviewer`, `procurement-compliance-specialist`, and `sow-reviewer` use `gpt-5.6-sol` for high-stakes vendor, policy, and SOW review. | `rfp-response-analyst` and `vendor-scorecard-analyst` use `gpt-5.6-terra` for matrices and scorecards from disclosed criteria without award authority. |
| Policy and public affairs | `policy-analyst` and `impact-assessment-writer` use `gpt-5.6-terra` with high reasoning for source-backed tradeoff and impact analysis. | `public-comment-drafter`, `stakeholder-map-analyst`, and `legislative-tracker` use `gpt-5.6-terra` for drafting, aggregate mapping, and official-source monitoring without legal advice, deceptive advocacy, or political microtargeting. |
| Publishing and scholarly production | `developmental-manuscript-editor` and `permissions-reviewer` use `gpt-5.6-terra` for structural and rights-sensitive review. | `production-editor` and `indexing-coordinator` use `gpt-5.6-luna`; `journal-submission-specialist` uses `gpt-5.6-terra` for production, indexing, and submissions without publisher approval, legal clearance, or research-integrity certification. |
| Book and long-form production | `fiction-development-editor` and `nonfiction-manuscript-editor` use `gpt-5.6-terra`; `fact-checking-editor` uses `gpt-5.6-sol` for source-sensitive claim review. | `line-copy-editor` and `book-metadata-packaging-editor` use `gpt-5.6-luna` for applied editing, style sheets, metadata, positioning copy, and package cleanup with complete requested drafting/editing, truthful attribution, and no invented legal clearance, retailer approval, or guaranteed sales claims. |
| Education design and delivery | `curriculum-designer` defines outcome alignment; `assessment-designer` defines assessment evidence and scoring proposals. | `lesson-materials-author` creates teachable materials; `learning-accessibility-reviewer` reviews participation barriers; `training-evaluation-analyst` plans or interprets effectiveness evidence. Existing `research-methods-reviewer` owns scholarly validity questions and `accessibility-reviewer` owns product UI review. |
| Archives and collections | `accession-intake-coordinator` prepares provenance and transfer evidence; `collection-description-specialist` owns archival hierarchy and description; `digital-preservation-planner` plans fixity and recovery verification. | `collection-access-reviewer` maps access restrictions; `exhibit-interpretation-writer` drafts interpretation. Existing `records-retention-advisor` handles disposition authority questions, `research-data-curator` owns research-dataset reproducibility, and `permissions-reviewer` handles rights evidence. |
| Video and audio production | `production-brief-planner` defines deliverables and dependencies; `script-development-editor` owns spoken scripts and timing; `recording-preparation-coordinator` prepares capture sessions. | `postproduction-coordinator` owns media manifests and edit handoffs; `media-delivery-reviewer` checks actual exports and caption coverage. Existing `production-editor` owns manuscript production, `audience-seo-editor` owns news packaging, and `permissions-reviewer` handles rights evidence. |
| Composition vs development | `text-project-planner` defines the writing brief; existing development editors diagnose form-specific structure. | The seven drafting specialists produce full texts; `developmental-manuscript-editor` applies structural revisions using `text-revision`, while line/copy and rhetorical editors own language passes. |
| Reader and continuity review | `manuscript-continuity-reviewer` reports paired textual evidence; `reader-experience-reviewer` distinguishes predicted effects from actual feedback. | Editing roles apply repairs; neither review implies reader-study evidence or a mandate to normalize deliberate form. |
| Translation vs adaptation | `translation-reviewer` compares source and target without changing either; `textual-witness-analyst` establishes source identity. | `text-translator` owns complete translation and its revisions; `text-adaptation-editor` changes audience, form, or purpose. Software localization readiness remains with `localization-engineer`. |
| Textual scholarship vs archives | `textual-witness-analyst` owns text-specific source/representation coverage; archival description remains with `collection-description-specialist`. | `documentary-transcriber`, `variant-collator`, and `critical-edition-editor` keep transcription, comparison, and editorial selection distinct. |
| Proof, format, and edition maintenance | `publication-format-reviewer` reports actual structural/rendering/accessibility checks. | `proofreader` owns located corrections, `indexing-coordinator` owns verified locators, and `edition-maintenance-editor` tracks changes and derivative updates; `production-editor` coordinates their stages. |
| General vs scholarly submissions | `submission-package-editor` prepares literary/general destination materials from actual requirements. | `journal-submission-specialist` retains scholarly requirements, disclosures, and reviewer responses; neither preparation role submits automatically. |
| Archaeological records vs archives | `archaeological-recording-specialist`, `archaeological-finds-coordinator`, and `stratigraphic-sequence-reviewer` own context provenance, material registers, and relative-sequence evidence; `archaeological-project-planner` and `archaeological-report-author` connect design and synthesis. | `accession-intake-coordinator`, `collection-description-specialist`, and `digital-preservation-planner` retain custody/intake, archival hierarchy, and preservation planning; `research-methods-reviewer` owns broader study-validity critique. |
| Language evidence vs translation | `language-documentation-planner` and `linguistic-session-designer` plan evidence collection; `linguistic-annotation-editor` and `lexicon-corpus-curator` preserve attestation and analytical uncertainty; `language-deposit-coordinator` packages linked resources and restrictions. | `text-translator` owns separately requested target-language literary translation; `recording-preparation-coordinator` handles capture logistics; archive specialists retain preservation and description. |
| Oral history vs media and textual scholarship | `oral-history-project-planner` and `oral-history-interview-designer` own historical questions and narrator-centered preparation; `oral-history-transcript-editor`, `oral-history-access-reviewer`, and `oral-history-interpretation-editor` separate source speech, edits, decisions, and contextual use. | `documentary-transcriber` owns supplied written textual witnesses; `postproduction-coordinator` owns media synchronization; `collection-access-reviewer` and `permissions-reviewer` handle adjacent repository and rights evidence. |
| Conservation objects and places | `conservation-condition-reviewer` reviews supplied observations; `preventive-conservation-planner` plans care; `conservation-treatment-reviewer` critiques proposals; `historic-fabric-recording-specialist` records buildings and sites; `site-conservation-planner` connects significance and site pressures; `conservation-monitoring-coordinator` maintains observation and action records. | These roles do not replace physical examination, qualified conservator or structural decisions, or custodian authority. Archives roles retain provenance and custody; archaeological roles retain excavation-record relationships and sequence analysis. |

## Implemented Skill Assets

The catalog exposes 30 progressively disclosed Skill packages. Agent templates name the gateway and one or more modes; a gateway loads only the smallest workflow set needed.

| Gateway | Modes |
| --- | --- |
| `$product-strategy` | `product-discovery`, `competitive-research` |
| `$interface-design-review` | `ux-flow-mapping`, `design-system-audit`, `accessibility-audit`, `localization-readiness` |
| `$architecture-contracts` | `architecture-decision-records`, `api-contract-review` |
| `$data-analytics` | `data-modeling`, `analytics-engineering`, `data-science-workflows` |
| `$software-delivery` | `implementation-planning`, `engineering-execution` |
| `$software-assurance` | `dependency-risk-triage`, `performance-profiling`, `test-matrix-design` |
| `$production-operations` | `release-readiness`, `observability-runbooks`, `incident-postmortems` |
| `$ai-ml-lifecycle` | `ai-evals`, `ml-engineering`, `mlops-readiness` |
| `$security-privacy-review` | `threat-modeling`, `prompt-injection-defense`, `privacy-review` |
| `$docs-information-architecture` | `docs-information-architecture` |
| `$public-source-research` | `osint-research-planning`, `public-records-research`, `geolocation-chronolocation-analysis`, `public-social-network-analysis`, `misinformation-risk-analysis` |
| `$research-quality` | `academic-literature-review`, `research-methods-review`, `citation-integrity-review` |
| `$legal-operations` | `legal-research-workflows`, `contract-review-operations`, `records-retention-operations` |
| `$grant-operations` | `grant-proposal-compliance`, `grant-budget-justification`, `sponsored-projects-reporting` |
| `$finance-audit-operations` | `finance-operations-review`, `audit-evidence-management`, `invoice-reconciliation-workflows` |
| `$procurement-commercial-review` | `procurement-vendor-review`, `rfp-response-workflows`, `sow-review-workflows` |
| `$policy-public-affairs` | `policy-analysis-workflows`, `public-comment-drafting`, `legislative-tracking` |
| `$publishing-editorial` | `fiction-development-workflows`, `nonfiction-manuscript-development`, `line-copyediting-workflows`, `fact-checking-source-review`, `book-metadata-packaging`, `publishing-production-workflows`, `permissions-rights-review`, `journal-submission-workflows`, `proofreading`, `publication-format-review`, `indexing-workflows`, `submission-package-preparation`, `edition-maintenance` |
| `$codex-subagent-designer` | `delegation-design`, `subagent-prompting`, `catalog-asset-design`, `agent-template-review` |
| `$education-training` | `curriculum-design`, `lesson-materials`, `assessment-design`, `learning-accessibility`, `training-evaluation` |
| `$archives-collections` | `accession-intake`, `collection-description`, `digital-preservation`, `collection-access`, `exhibit-interpretation` |
| `$video-audio-production` | `production-planning`, `script-development`, `recording-preparation`, `postproduction-handoff`, `media-delivery-review` |
| `$text-composition` | `composition-planning`, `source-synthesis-and-outlining`, `fiction-drafting`, `nonfiction-drafting`, `essay-composition`, `poetry-composition`, `dramatic-writing`, `professional-writing`, `academic-writing` |
| `$text-revision` | `revision-planning`, `structural-revision`, `feedback-integration`, `rhetorical-revision`, `continuity-review`, `reader-response-review`, `text-adaptation` |
| `$text-translation` | `translation-planning`, `translation-drafting`, `translation-review` |
| `$textual-scholarship` | `witness-description`, `documentary-transcription`, `variant-collation`, `critical-edition-preparation` |
| `$archaeological-fieldwork` | `project-design`, `field-recording`, `stratigraphic-review`, `finds-register`, `post-fieldwork-reporting` |
| `$language-documentation` | `documentation-planning`, `session-design`, `transcription-annotation`, `lexicon-curation`, `archive-preparation` |
| `$oral-history` | `project-planning`, `interview-preparation`, `transcript-editing`, `narrator-review-access`, `interpretation-edition` |
| `$heritage-conservation` | `condition-assessment`, `preventive-care`, `treatment-proposal-review`, `historic-fabric-recording`, `site-conservation-planning`, `monitoring-maintenance` |

The `architecture-decision-records` mode supports `Proposed` drafts before owner approval. Approval gates acceptance and implementation, not preparation of the review artifact.

## Remaining Skill Backlog

None. Every Skill currently referenced by the agent templates has a repository-local skill folder.

## Use Guidance

Use `gpt-5.6-sol` for the catalog’s explicitly high-stakes or highest-complexity roles. Use `gpt-5.6-terra` as the default for bounded implementation, analysis, review, and documentation work. Use `gpt-5.6-luna` for the selected repeatable editorial and support roles. Retain `gpt-5.3-codex-spark` only for fast scaffolding, test generation, and narrow experiments.

These examples are intentionally reusable rather than automatically enabled. Copy only the agents a project needs and use only the dispatch mechanism exposed by the active session; validation work does not imply a built-in `validator` agent. Keep nested delegation deliberately bounded by task ownership and the active tool contract. See [subagent-toml.md](subagent-toml.md#runtime-agent-limits) for current concurrency settings and the limits of legacy depth and timeout fields.
