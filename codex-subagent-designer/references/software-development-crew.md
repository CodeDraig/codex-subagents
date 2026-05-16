# Software Development Crew

This reference catalogs reusable Codex custom-agent examples for a full software development lifecycle. Copy individual TOML files from `codex-subagent-designer/agents/examples/openai/` into a project's `.codex/agents/` directory when that role is useful.

## Lifecycle Map

| Stage | Agents |
| --- | --- |
| Intake and shaping | `triage-router`, `product-discovery-strategist`, `market-researcher`, `technical-planner` |
| Architecture and contracts | `systems-architect`, `api-contract-architect`, `database-modeler` |
| UX and product surface | `ux-flow-architect`, `design-system-engineer`, `accessibility-reviewer`, `localization-engineer` |
| Product implementation | `frontend-experience-engineer`, `backend-domain-engineer`, `ai-feature-engineer`, `prompt-evaluation-engineer`, `data-platform-engineer`, `rapid-prototype-scout`, `implementation-finisher` |
| Risk and quality | `security-threat-modeler`, `security-fix-engineer`, `privacy-compliance-reviewer`, `performance-investigator`, `performance-optimizer`, `test-strategy-architect`, `test-automation-engineer`, `code-reviewer`, `refactor-surgeon` |
| Shipping and operations | `build-release-engineer`, `devops-platform-engineer`, `observability-incident-engineer`, `documentation-engineer`, `developer-experience-engineer`, `dependency-maintenance-engineer` |
| Open Source Intelligence | `osint-research-lead`, `source-verification-analyst`, `geolocation-chronolocation-analyst`, `public-records-researcher`, `social-network-analyst`, `misinformation-risk-analyst` |
| Technical Support | `support-triage-specialist`, `customer-diagnostics-engineer`, `escalation-support-engineer`, `knowledge-base-author`, `support-automation-engineer`, `customer-communications-specialist` |
| News Site Staff | `assignment-editor`, `breaking-news-reporter`, `news-fact-checker`, `copy-desk-editor`, `audience-seo-editor`, `standards-ethics-editor` |

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

## Model Coverage

| Model | Reasoning Efforts Used | Representative Agents |
| --- | --- | --- |
| `gpt-5.5` | `low`, `medium`, `high`, `xhigh` | `triage-router`, `observability-incident-engineer`, `systems-architect`, `product-discovery-strategist` |
| `gpt-5.4-mini` | `low`, `medium` | `dependency-maintenance-engineer`, `documentation-engineer`, `design-system-engineer` |
| `gpt-5.3-codex` | `medium`, `high` | `backend-domain-engineer`, `frontend-experience-engineer`, `security-fix-engineer`, `implementation-finisher` |
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

## Future Skills Backlog

The agent examples intentionally reference Skills that may not exist yet. Keep this backlog synchronized whenever the TOML files gain or lose Skill references.

## Implemented Skill Assets

These backlog items now have repository-local skill folders:

- `$product-discovery`: `product-discovery/`
- `$competitive-research`: `competitive-research/`
- `$architecture-decision-records`: `architecture-decision-records/`
- `$implementation-planning`: `implementation-planning/`
- `$ux-flow-mapping`: `ux-flow-mapping/`
- `$design-system-audit`: `design-system-audit/`
- `$dependency-risk-triage`: `dependency-risk-triage/`
- `$api-contract-review`: `api-contract-review/`
- `$data-modeling`: `data-modeling/`
- `$ai-evals`: `ai-evals/`
- `$prompt-injection-defense`: `prompt-injection-defense/`
- `$threat-modeling`: `threat-modeling/`
- `$privacy-review`: `privacy-review/`
- `$performance-profiling`: `performance-profiling/`
- `$test-matrix-design`: `test-matrix-design/`
- `$release-readiness`: `release-readiness/`
- `$observability-runbooks`: `observability-runbooks/`
- `$incident-postmortems`: `incident-postmortems/`
- `$docs-information-architecture`: `docs-information-architecture/`
- `$accessibility-audit`: `accessibility-audit/`
- `$localization-readiness`: `localization-readiness/`

## Remaining Skill Backlog

None. Every Skill currently referenced by the agent templates has a repository-local skill folder.

## Use Guidance

Use high-reasoning `gpt-5.5` agents when the task is ambiguous, cross-cutting, strategic, or expensive to get wrong. Use `gpt-5.3-codex` agents for bounded implementation where correctness and repo adaptation matter. Use `gpt-5.3-codex-spark` for fast scaffolding, test generation, and narrow experiments. Use `gpt-5.4-mini` for well-scoped review, documentation, maintenance, and repetitive cleanup where lower latency matters more than broad reasoning.

These examples are intentionally reusable rather than automatically enabled. A project should copy only the agents it needs and keep `max_depth = 1` unless nested delegation is deliberately designed and reviewed.
