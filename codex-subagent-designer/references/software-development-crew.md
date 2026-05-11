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
