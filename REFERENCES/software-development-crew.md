# Software Development Crew

This reference catalogs reusable Codex custom-agent examples for a full software development lifecycle. Copy individual TOML files from `AGENTS/openai/` into a project's `.codex/agents/` directory when that role is useful.

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
| Manuscript structure, argument, audience fit, major revision priorities | `developmental-manuscript-editor` |
| Fiction premise, plot, character arcs, continuity, genre promise, revision roadmap | `fiction-development-editor` |
| Nonfiction thesis, proposal, chapter architecture, reader promise, evidence plan | `nonfiction-manuscript-editor` |
| Line edits, copyedits, style sheets, query logs, consistency passes | `line-copy-editor` |
| Long-form claim checking against source packets, interviews, datasets, author notes | `fact-checking-editor` |
| Book metadata, back-cover copy, categories, keywords, accessibility fields, package gaps | `book-metadata-packaging-editor` |
| Production editing, style sheets, proof stages, schedules, query logs | `production-editor` |
| Third-party content permissions, license restrictions, attribution needs | `permissions-reviewer` |
| Index term candidates, locators, cross-references, author queries | `indexing-coordinator` |
| Journal submission packages, metadata gaps, disclosures, response matrices | `journal-submission-specialist` |

## Model Coverage

| Model | Reasoning Efforts Used | Representative Agents |
| --- | --- | --- |
| `gpt-5.5` | `low`, `medium`, `high`, `xhigh` | `triage-router`, `observability-incident-engineer`, `systems-architect`, `product-discovery-strategist`, `data-scientist`, `mlops-engineer`, `software-engineering-lead`, `legal-research-analyst`, `literature-reviewer`, `proposal-compliance-reviewer`, `financial-model-reviewer`, `vendor-risk-reviewer`, `policy-analyst`, `permissions-reviewer`, `fiction-development-editor`, `nonfiction-manuscript-editor`, `fact-checking-editor` |
| `gpt-5.4-mini` | `low`, `medium` | `dependency-maintenance-engineer`, `documentation-engineer`, `design-system-engineer`, `peer-review-prep-editor`, `grant-reporting-specialist`, `production-editor`, `indexing-coordinator`, `line-copy-editor`, `book-metadata-packaging-editor` |
| `gpt-5.3-codex` | `medium`, `high` | `backend-domain-engineer`, `frontend-experience-engineer`, `security-fix-engineer`, `implementation-finisher`, `analytics-engineer`, `ml-engineer`, `research-data-curator`, `invoice-reconciliation-specialist`, `audit-evidence-organizer`, `vendor-scorecard-analyst` |
| `gpt-5.3-codex-spark` | `low`, `medium`, `high` | `rapid-prototype-scout`, `developer-experience-engineer`, `test-automation-engineer` |

## Intentional Overlap

Some domains have paired agents because model capability and latency change the right behavior.

| Domain | Thinking Agent | Execution Agent |
| --- | --- | --- |
| Security | `security-threat-modeler` uses `gpt-5.5` with `xhigh` reasoning for threat modeling and attack-path analysis. | `security-fix-engineer` uses `gpt-5.3-codex` with `high` reasoning for bounded remediation patches. |
| Performance | `performance-investigator` uses `gpt-5.5` with `high` reasoning to interpret measurements and isolate causes. | `performance-optimizer` uses `gpt-5.3-codex` with `high` reasoning to implement focused optimizations. |
| Testing | `test-strategy-architect` uses `gpt-5.5` with `high` reasoning to design risk-based coverage. | `test-automation-engineer` uses `gpt-5.3-codex-spark` with `high` reasoning to quickly add executable tests. |
| Architecture | `systems-architect` uses `gpt-5.5` with `xhigh` reasoning for durable system boundaries. | `rapid-prototype-scout` uses `gpt-5.3-codex-spark` with `low` reasoning to test feasibility quickly. |
| News verification | `news-fact-checker` uses `gpt-5.5` with `high` reasoning for publication risk. | `copy-desk-editor` uses `gpt-5.4-mini` with `medium` reasoning for line edits and packaging. |
| Support operations | `escalation-support-engineer` uses `gpt-5.5` with `high` reasoning for complex cases. | `support-automation-engineer` uses `gpt-5.3-codex` with `high` reasoning for support tooling. |
| OSINT | `osint-research-lead` uses `gpt-5.5` with `xhigh` reasoning for lawful scope and synthesis. | `source-verification-analyst` uses `gpt-5.5` with `high` reasoning for claim-level corroboration. |
| Data platform vs analysis | `data-scientist` uses `gpt-5.5` with `high` reasoning for exploratory analysis, experiment interpretation, and evidence-backed recommendations. | `data-platform-engineer` uses `gpt-5.3-codex` with `high` reasoning for production ingestion, transformation, warehouse, lakehouse, lineage, backfill, and reporting implementation. |
| Analytics semantics vs data modeling | `analytics-engineer` uses `gpt-5.3-codex` with `high` reasoning for metric contracts, semantic models, dashboards, and BI-ready transformations. | `database-modeler` uses `gpt-5.5` with `high` reasoning for persistence shape, indexing, retention, migrations, and durable data ownership decisions. |
| ML delivery vs ML operations | `ml-engineer` uses `gpt-5.3-codex` with `high` reasoning for training, inference, feature pipelines, and eval harnesses. | `mlops-engineer` uses `gpt-5.5` with `high` reasoning for registry, release controls, drift, monitoring, reproducibility, rollback, and production model readiness. |
| Engineering execution | `software-engineering-lead` uses `gpt-5.5` with `high` reasoning for read-only delivery sequencing, integration risk, validation gates, and handoff review. | `technical-planner` creates durable implementation plans, while `systems-architect` owns architecture decisions and long-term system boundaries. |
| Legal research vs public records | `legal-research-analyst` uses `gpt-5.5` with `high` reasoning for source-backed legal/regulatory research, issue spotting, authority maps, caveats, and counsel questions. | `public-records-researcher` owns official record, docket, registry, filing, and entity-disambiguation searches. |
| Contract review vs privacy/security/procurement | `contract-review-specialist` uses `gpt-5.5` with `high` reasoning for clause extraction, obligations, operational impacts, and owner questions. | `privacy-compliance-reviewer` owns personal-data risk; `vendor-risk-reviewer`, `procurement-compliance-specialist`, and `sow-reviewer` own procurement evidence, policy, and SOW workflow slices. |
| Regulatory monitoring vs policy analysis | `regulatory-monitor` uses `gpt-5.5` with `high` reasoning for official source monitoring, changes, effective dates, and owner questions. | `policy-analyst`, `public-comment-drafter`, `stakeholder-map-analyst`, `legislative-tracker`, and `impact-assessment-writer` own policy-position, stakeholder, and public-affairs artifacts. |
| Records retention operations | `records-retention-advisor` uses `gpt-5.5` with `medium` reasoning for retention inventories, schedules, hold flags, disposition workflows, and approval gates. | `privacy-compliance-reviewer` owns privacy law and personal-data implications, while counsel or authorized owners make final retention decisions. |
| Legal operations coordination | `legal-ops-coordinator` uses `gpt-5.5` with `medium` reasoning for intake, matter tracking, source packages, deadlines, owner questions, and routing. | Specialist legal/regulatory agents own research, contract, regulatory, and retention analysis; this role coordinates handoffs without legal judgment. |
| Academic research support | `literature-reviewer`, `research-methods-reviewer`, and `citation-integrity-checker` use `gpt-5.5` for source-backed synthesis, validity critique, and citation integrity. | `research-data-curator` uses `gpt-5.3-codex` for repo-local metadata and reproducibility artifacts; `peer-review-prep-editor` uses `gpt-5.4-mini` for manuscript preparation. |
| Grants and sponsored projects | `proposal-compliance-reviewer` uses `gpt-5.5` with `high` reasoning for sponsor compliance matrices. | `budget-justification-writer`, `sponsored-projects-coordinator`, and `grant-reporting-specialist` support budget narratives, award calendars, and reporting evidence without official submission authority. |
| Finance and accounting operations | `financial-model-reviewer` and `accounting-controls-reviewer` use `gpt-5.5` for high-stakes model and control review. | `invoice-reconciliation-specialist` and `audit-evidence-organizer` use `gpt-5.3-codex` for operational artifacts; none provide tax, investment, legal, valuation, or audit-opinion advice. |
| Procurement and vendor management | `vendor-risk-reviewer`, `procurement-compliance-specialist`, and `sow-reviewer` use `gpt-5.5` for high-stakes vendor, policy, and SOW review. | `rfp-response-analyst` and `vendor-scorecard-analyst` create matrices and scorecards from disclosed criteria without award authority. |
| Policy and public affairs | `policy-analyst` and `impact-assessment-writer` use `gpt-5.5` with high reasoning for source-backed tradeoff and impact analysis. | `public-comment-drafter`, `stakeholder-map-analyst`, and `legislative-tracker` support drafting, aggregate mapping, and official-source monitoring without legal advice, deceptive advocacy, or political microtargeting. |
| Publishing and scholarly production | `developmental-manuscript-editor` and `permissions-reviewer` use `gpt-5.5` for structural and rights-sensitive review. | `production-editor`, `indexing-coordinator`, and `journal-submission-specialist` coordinate production, indexing, and submissions without publisher approval, legal clearance, or research-integrity certification. |
| Book and long-form production | `fiction-development-editor`, `nonfiction-manuscript-editor`, and `fact-checking-editor` use `gpt-5.5` for story or argument architecture, source-sensitive claim review, and revision risk. | `line-copy-editor` and `book-metadata-packaging-editor` use `gpt-5.4-mini` for applied editing, style sheets, metadata, positioning copy, and package cleanup without ghostwriting, legal clearance, retailer approval, or guaranteed sales claims. |

## Implemented Skill Assets

Every Skill referenced by the agent examples has a repository-local skill folder:

- `$product-discovery`: `SKILLS/product-discovery/`
- `$competitive-research`: `SKILLS/competitive-research/`
- `$architecture-decision-records`: `SKILLS/architecture-decision-records/`
- `$implementation-planning`: `SKILLS/implementation-planning/`
- `$ux-flow-mapping`: `SKILLS/ux-flow-mapping/`
- `$design-system-audit`: `SKILLS/design-system-audit/`
- `$dependency-risk-triage`: `SKILLS/dependency-risk-triage/`
- `$api-contract-review`: `SKILLS/api-contract-review/`
- `$data-modeling`: `SKILLS/data-modeling/`
- `$ai-evals`: `SKILLS/ai-evals/`
- `$prompt-injection-defense`: `SKILLS/prompt-injection-defense/`
- `$threat-modeling`: `SKILLS/threat-modeling/`
- `$privacy-review`: `SKILLS/privacy-review/`
- `$performance-profiling`: `SKILLS/performance-profiling/`
- `$test-matrix-design`: `SKILLS/test-matrix-design/`
- `$release-readiness`: `SKILLS/release-readiness/`
- `$observability-runbooks`: `SKILLS/observability-runbooks/`
- `$incident-postmortems`: `SKILLS/incident-postmortems/`
- `$docs-information-architecture`: `SKILLS/docs-information-architecture/`
- `$accessibility-audit`: `SKILLS/accessibility-audit/`
- `$localization-readiness`: `SKILLS/localization-readiness/`
- `$data-science-workflows`: `SKILLS/data-science-workflows/`
- `$analytics-engineering`: `SKILLS/analytics-engineering/`
- `$ml-engineering`: `SKILLS/ml-engineering/`
- `$mlops-readiness`: `SKILLS/mlops-readiness/`
- `$engineering-execution`: `SKILLS/engineering-execution/`
- `$legal-research-workflows`: `SKILLS/legal-research-workflows/`
- `$contract-review-operations`: `SKILLS/contract-review-operations/`
- `$records-retention-operations`: `SKILLS/records-retention-operations/`
- `$academic-literature-review`: `SKILLS/academic-literature-review/`
- `$research-methods-review`: `SKILLS/research-methods-review/`
- `$citation-integrity-review`: `SKILLS/citation-integrity-review/`
- `$grant-proposal-compliance`: `SKILLS/grant-proposal-compliance/`
- `$sponsored-projects-reporting`: `SKILLS/sponsored-projects-reporting/`
- `$grant-budget-justification`: `SKILLS/grant-budget-justification/`
- `$finance-operations-review`: `SKILLS/finance-operations-review/`
- `$audit-evidence-management`: `SKILLS/audit-evidence-management/`
- `$invoice-reconciliation-workflows`: `SKILLS/invoice-reconciliation-workflows/`
- `$procurement-vendor-review`: `SKILLS/procurement-vendor-review/`
- `$rfp-response-workflows`: `SKILLS/rfp-response-workflows/`
- `$sow-review-workflows`: `SKILLS/sow-review-workflows/`
- `$policy-analysis-workflows`: `SKILLS/policy-analysis-workflows/`
- `$public-comment-drafting`: `SKILLS/public-comment-drafting/`
- `$legislative-tracking`: `SKILLS/legislative-tracking/`
- `$publishing-production-workflows`: `SKILLS/publishing-production-workflows/`
- `$permissions-rights-review`: `SKILLS/permissions-rights-review/`
- `$journal-submission-workflows`: `SKILLS/journal-submission-workflows/`
- `$fiction-development-workflows`: `SKILLS/fiction-development-workflows/`
- `$nonfiction-manuscript-development`: `SKILLS/nonfiction-manuscript-development/`
- `$line-copyediting-workflows`: `SKILLS/line-copyediting-workflows/`
- `$fact-checking-source-review`: `SKILLS/fact-checking-source-review/`
- `$book-metadata-packaging`: `SKILLS/book-metadata-packaging/`

## Remaining Skill Backlog

None. Every Skill currently referenced by the agent templates has a repository-local skill folder.

## Use Guidance

Use high-reasoning `gpt-5.5` agents when the task is ambiguous, cross-cutting, strategic, or expensive to get wrong. Use `gpt-5.3-codex` agents for bounded implementation where correctness and repo adaptation matter. Use `gpt-5.3-codex-spark` for fast scaffolding, test generation, and narrow experiments. Use `gpt-5.4-mini` for well-scoped review, documentation, maintenance, and repetitive cleanup where lower latency matters more than broad reasoning.

These examples are intentionally reusable rather than automatically enabled. A project should copy only the agents it needs and keep `max_depth = 1` unless nested delegation is deliberately designed and reviewed.
