# Skills and Agents Quality Audit

Date: 2026-05-24

Scope: all current `SKILLS/` packages and `AGENTS/openai/` TOML templates, scored against `REFERENCES/quality-rubric.md`.

Score order for skills: trigger fit / workflow specificity / domain heuristics / supporting assets / tooling and validation / output contract / boundaries and stop conditions.

Score order for agents: role distinctness / skill and reference use / instruction depth / model, reasoning, and sandbox fit / handoffs and boundaries / output contract / catalog integration.

## Summary

- Skills reviewed: 48
- Skills Ready: 4
- Skills Useful but Thin: 44
- Agents reviewed: 91
- Agents Ready: 61
- Agents Useful but Thin: 30

No assets scored as `Unsafe or Misleading`. The dominant weakness is not basic structure; it is depth: many assets lack concrete tooling, verification commands, examples, or richer supporting reference material.

## Highest Priority Skill Improvements

| Asset | Rating | Scores | Avg | Required fixes |
| --- | --- | --- | --- | --- |
| `engineering-execution` | Useful but Thin | 3/3/2/3/2/4/2 | 2.71 | raise domain heuristics; raise tooling/validation; raise boundaries |
| `architecture-decision-records` | Useful but Thin | 4/3/2/3/2/3/3 | 2.86 | raise domain heuristics; raise tooling/validation |
| `audit-evidence-management` | Useful but Thin | 3/3/2/3/2/4/3 | 2.86 | raise domain heuristics; raise tooling/validation |
| `data-modeling` | Useful but Thin | 4/3/2/3/2/3/3 | 2.86 | raise domain heuristics; raise tooling/validation |
| `data-science-workflows` | Useful but Thin | 3/3/2/3/2/4/3 | 2.86 | raise domain heuristics; raise tooling/validation |
| `design-system-audit` | Useful but Thin | 4/3/2/3/2/3/3 | 2.86 | raise domain heuristics; raise tooling/validation |
| `observability-runbooks` | Useful but Thin | 4/3/2/3/2/3/3 | 2.86 | raise domain heuristics; raise tooling/validation |
| `publishing-production-workflows` | Useful but Thin | 3/3/2/3/2/3/4 | 2.86 | raise domain heuristics; raise tooling/validation |
| `release-readiness` | Useful but Thin | 4/3/2/3/2/3/3 | 2.86 | raise domain heuristics; raise tooling/validation |
| `ux-flow-mapping` | Useful but Thin | 4/3/2/3/2/3/3 | 2.86 | raise domain heuristics; raise tooling/validation |
| `academic-literature-review` | Useful but Thin | 3/3/2/3/2/4/4 | 3.00 | raise domain heuristics; raise tooling/validation |
| `accessibility-audit` | Useful but Thin | 4/3/2/3/2/4/3 | 3.00 | raise domain heuristics; raise tooling/validation |

## Highest Priority Agent Improvements

| Asset | Rating | Scores | Avg | Required fixes |
| --- | --- | --- | --- | --- |
| `customer-communications-specialist` | Useful but Thin | 4/2/3/3/3/3/4 | 3.14 | raise skill/reference use |
| `implementation-finisher` | Useful but Thin | 4/2/3/3/2/4/4 | 3.14 | raise skill/reference use; raise handoffs/boundaries |
| `audience-seo-editor` | Useful but Thin | 4/2/3/3/3/4/4 | 3.29 | raise skill/reference use |
| `backend-domain-engineer` | Useful but Thin | 4/2/3/4/2/4/4 | 3.29 | raise skill/reference use; raise handoffs/boundaries |
| `copy-desk-editor` | Useful but Thin | 4/2/3/3/3/4/4 | 3.29 | raise skill/reference use |
| `frontend-experience-engineer` | Useful but Thin | 4/2/3/4/2/4/4 | 3.29 | raise skill/reference use; raise handoffs/boundaries |
| `geolocation-chronolocation-analyst` | Useful but Thin | 4/2/3/4/3/3/4 | 3.29 | raise skill/reference use |
| `knowledge-base-author` | Useful but Thin | 4/2/3/3/3/4/4 | 3.29 | raise skill/reference use |
| `news-fact-checker` | Useful but Thin | 4/2/3/4/3/3/4 | 3.29 | raise skill/reference use |
| `performance-optimizer` | Useful but Thin | 4/2/3/4/2/4/4 | 3.29 | raise skill/reference use; raise handoffs/boundaries |
| `rapid-prototype-scout` | Useful but Thin | 4/2/3/4/2/4/4 | 3.29 | raise skill/reference use; raise handoffs/boundaries |
| `refactor-surgeon` | Useful but Thin | 4/2/3/3/3/4/4 | 3.29 | raise skill/reference use |
| `source-verification-analyst` | Useful but Thin | 4/2/3/3/3/4/4 | 3.29 | raise skill/reference use |
| `standards-ethics-editor` | Useful but Thin | 4/2/3/4/3/3/4 | 3.29 | raise skill/reference use |
| `support-triage-specialist` | Useful but Thin | 4/2/3/3/3/4/4 | 3.29 | raise skill/reference use |

## Cross-Cutting Findings

1. Many skills have a valid five-step workflow and a checklist, but the checklist is often short. To reach `Ready`, add concrete examples, decision tables, source-quality rules, or validation commands.
2. Tooling and validation is the most common skill weakness. Skills should say what to inspect, which commands or parsers to prefer, what evidence is acceptable, and when manual owner review is the only valid gate.
3. Several older agents are operationally useful but do not reference a dedicated skill asset. Under the rubric, those remain `Useful but Thin` until a skill exists or the agent explicitly explains why no skill applies.
4. Handoffs are uneven. New knowledge-work agents often name adjacent agents; many older software, support, OSINT, and newsroom agents rely on boundaries but do not route to specific implemented peers.
5. Output contracts are mostly present, but many could be improved by requiring evidence fields such as commands run, files inspected, source links, risks, blockers, owner questions, and validation status.

## Skill Scores

| Skill | Rating | Scores | Avg | Required fixes |
| --- | --- | --- | --- | --- |
| `academic-literature-review` | Useful but Thin | 3/3/2/3/2/4/4 | 3.00 | raise domain heuristics; raise tooling/validation |
| `accessibility-audit` | Useful but Thin | 4/3/2/3/2/4/3 | 3.00 | raise domain heuristics; raise tooling/validation |
| `ai-evals` | Useful but Thin | 4/3/3/3/2/4/4 | 3.29 | raise tooling/validation |
| `analytics-engineering` | Useful but Thin | 3/3/2/4/2/4/3 | 3.00 | raise domain heuristics; raise tooling/validation |
| `api-contract-review` | Ready | 4/4/4/4/4/4/4 | 4.00 | none required |
| `architecture-decision-records` | Useful but Thin | 4/3/2/3/2/3/3 | 2.86 | raise domain heuristics; raise tooling/validation |
| `audit-evidence-management` | Useful but Thin | 3/3/2/3/2/4/3 | 2.86 | raise domain heuristics; raise tooling/validation |
| `citation-integrity-review` | Useful but Thin | 3/3/2/3/2/4/4 | 3.00 | raise domain heuristics; raise tooling/validation |
| `codex-subagent-designer` | Ready | 4/4/4/4/4/3/3 | 3.71 | none required |
| `competitive-research` | Useful but Thin | 4/3/2/3/2/4/4 | 3.14 | raise domain heuristics; raise tooling/validation |
| `contract-review-operations` | Useful but Thin | 3/3/3/4/2/4/4 | 3.29 | raise tooling/validation |
| `data-modeling` | Useful but Thin | 4/3/2/3/2/3/3 | 2.86 | raise domain heuristics; raise tooling/validation |
| `data-science-workflows` | Useful but Thin | 3/3/2/3/2/4/3 | 2.86 | raise domain heuristics; raise tooling/validation |
| `dependency-risk-triage` | Ready | 4/4/4/4/4/4/4 | 4.00 | none required |
| `design-system-audit` | Useful but Thin | 4/3/2/3/2/3/3 | 2.86 | raise domain heuristics; raise tooling/validation |
| `docs-information-architecture` | Useful but Thin | 4/3/2/3/2/4/4 | 3.14 | raise domain heuristics; raise tooling/validation |
| `engineering-execution` | Useful but Thin | 3/3/2/3/2/4/2 | 2.71 | raise domain heuristics; raise tooling/validation; raise boundaries |
| `finance-operations-review` | Useful but Thin | 3/3/3/3/2/4/4 | 3.14 | raise tooling/validation |
| `grant-budget-justification` | Useful but Thin | 3/3/3/3/2/4/4 | 3.14 | raise tooling/validation |
| `grant-proposal-compliance` | Useful but Thin | 3/3/3/3/2/4/4 | 3.14 | raise tooling/validation |
| `implementation-planning` | Useful but Thin | 4/3/2/3/2/4/3 | 3.00 | raise domain heuristics; raise tooling/validation |
| `incident-postmortems` | Useful but Thin | 4/3/2/3/2/4/4 | 3.14 | raise domain heuristics; raise tooling/validation |
| `invoice-reconciliation-workflows` | Useful but Thin | 3/3/2/3/2/4/4 | 3.00 | raise domain heuristics; raise tooling/validation |
| `journal-submission-workflows` | Useful but Thin | 3/3/2/3/2/4/4 | 3.00 | raise domain heuristics; raise tooling/validation |
| `legal-research-workflows` | Useful but Thin | 4/3/2/4/2/4/4 | 3.29 | raise domain heuristics; raise tooling/validation |
| `legislative-tracking` | Useful but Thin | 3/3/2/3/2/4/4 | 3.00 | raise domain heuristics; raise tooling/validation |
| `localization-readiness` | Useful but Thin | 4/3/2/3/2/4/4 | 3.14 | raise domain heuristics; raise tooling/validation |
| `ml-engineering` | Useful but Thin | 3/3/2/4/3/3/3 | 3.00 | raise domain heuristics |
| `mlops-readiness` | Useful but Thin | 3/3/2/4/2/4/3 | 3.00 | raise domain heuristics; raise tooling/validation |
| `observability-runbooks` | Useful but Thin | 4/3/2/3/2/3/3 | 2.86 | raise domain heuristics; raise tooling/validation |
| `performance-profiling` | Useful but Thin | 4/3/2/3/2/4/3 | 3.00 | raise domain heuristics; raise tooling/validation |
| `permissions-rights-review` | Useful but Thin | 3/3/2/3/2/4/4 | 3.00 | raise domain heuristics; raise tooling/validation |
| `policy-analysis-workflows` | Useful but Thin | 3/3/2/3/2/4/4 | 3.00 | raise domain heuristics; raise tooling/validation |
| `privacy-review` | Useful but Thin | 4/3/2/3/2/4/4 | 3.14 | raise domain heuristics; raise tooling/validation |
| `procurement-vendor-review` | Useful but Thin | 3/3/3/3/2/4/4 | 3.14 | raise tooling/validation |
| `product-discovery` | Useful but Thin | 4/3/2/3/2/4/3 | 3.00 | raise domain heuristics; raise tooling/validation |
| `prompt-injection-defense` | Useful but Thin | 4/3/2/3/2/3/4 | 3.00 | raise domain heuristics; raise tooling/validation |
| `public-comment-drafting` | Useful but Thin | 3/3/3/3/2/4/4 | 3.14 | raise tooling/validation |
| `publishing-production-workflows` | Useful but Thin | 3/3/2/3/2/3/4 | 2.86 | raise domain heuristics; raise tooling/validation |
| `records-retention-operations` | Useful but Thin | 3/3/3/3/2/4/4 | 3.14 | raise tooling/validation |
| `release-readiness` | Useful but Thin | 4/3/2/3/2/3/3 | 2.86 | raise domain heuristics; raise tooling/validation |
| `research-methods-review` | Useful but Thin | 3/3/2/3/2/4/4 | 3.00 | raise domain heuristics; raise tooling/validation |
| `rfp-response-workflows` | Useful but Thin | 3/3/3/3/2/4/4 | 3.14 | raise tooling/validation |
| `sow-review-workflows` | Useful but Thin | 3/3/3/3/2/3/4 | 3.00 | raise tooling/validation |
| `sponsored-projects-reporting` | Useful but Thin | 3/3/3/3/2/4/4 | 3.14 | raise tooling/validation |
| `test-matrix-design` | Useful but Thin | 4/3/2/3/3/4/4 | 3.29 | raise domain heuristics |
| `threat-modeling` | Ready | 4/4/4/4/4/4/4 | 4.00 | none required |
| `ux-flow-mapping` | Useful but Thin | 4/3/2/3/2/3/3 | 2.86 | raise domain heuristics; raise tooling/validation |

## Agent Scores

| Agent | Rating | Scores | Avg | Required fixes |
| --- | --- | --- | --- | --- |
| `accessibility-reviewer` | Ready | 4/4/3/4/3/4/4 | 3.71 | none required |
| `accounting-controls-reviewer` | Ready | 3/3/3/4/4/4/4 | 3.57 | optional: deepen examples, evidence fields, and handoffs |
| `ai-feature-engineer` | Ready | 4/4/3/4/3/4/4 | 3.71 | none required |
| `analytics-engineer` | Ready | 4/4/4/4/4/4/4 | 4.00 | none required |
| `api-contract-architect` | Ready | 4/4/3/4/3/4/4 | 3.71 | none required |
| `assignment-editor` | Useful but Thin | 4/2/3/4/3/4/4 | 3.43 | raise skill/reference use |
| `audience-seo-editor` | Useful but Thin | 4/2/3/3/3/4/4 | 3.29 | raise skill/reference use |
| `audit-evidence-organizer` | Ready | 3/3/3/3/4/4/4 | 3.43 | optional: deepen examples, evidence fields, and handoffs |
| `backend-domain-engineer` | Useful but Thin | 4/2/3/4/2/4/4 | 3.29 | raise skill/reference use; raise handoffs/boundaries |
| `breaking-news-reporter` | Useful but Thin | 4/2/3/4/3/4/4 | 3.43 | raise skill/reference use |
| `budget-justification-writer` | Ready | 4/3/3/4/4/4/4 | 3.71 | none required |
| `budget-variance-analyst` | Ready | 3/3/3/4/4/4/4 | 3.57 | optional: deepen examples, evidence fields, and handoffs |
| `build-release-engineer` | Ready | 4/4/3/4/3/4/4 | 3.71 | none required |
| `citation-integrity-checker` | Ready | 4/3/3/4/4/4/4 | 3.71 | none required |
| `code-reviewer` | Useful but Thin | 4/2/3/4/3/4/4 | 3.43 | raise skill/reference use |
| `contract-review-specialist` | Ready | 4/4/4/4/4/4/4 | 4.00 | none required |
| `copy-desk-editor` | Useful but Thin | 4/2/3/3/3/4/4 | 3.29 | raise skill/reference use |
| `customer-communications-specialist` | Useful but Thin | 4/2/3/3/3/3/4 | 3.14 | raise skill/reference use |
| `customer-diagnostics-engineer` | Useful but Thin | 4/2/3/4/3/4/4 | 3.43 | raise skill/reference use |
| `data-platform-engineer` | Ready | 4/4/3/4/3/4/4 | 3.71 | none required |
| `data-scientist` | Ready | 4/4/4/4/4/4/4 | 4.00 | none required |
| `database-modeler` | Ready | 4/4/3/4/3/4/4 | 3.71 | none required |
| `dependency-maintenance-engineer` | Ready | 4/4/3/3/3/4/4 | 3.57 | optional: deepen examples, evidence fields, and handoffs |
| `design-system-engineer` | Ready | 4/4/3/4/3/4/4 | 3.71 | none required |
| `developer-experience-engineer` | Useful but Thin | 4/2/3/4/3/4/4 | 3.43 | raise skill/reference use |
| `developmental-manuscript-editor` | Ready | 3/3/3/3/4/4/4 | 3.43 | optional: deepen examples, evidence fields, and handoffs |
| `devops-platform-engineer` | Useful but Thin | 4/2/3/4/3/4/4 | 3.43 | raise skill/reference use |
| `documentation-engineer` | Ready | 4/4/3/3/3/4/4 | 3.57 | optional: deepen examples, evidence fields, and handoffs |
| `escalation-support-engineer` | Useful but Thin | 4/2/3/4/4/4/4 | 3.57 | raise skill/reference use |
| `financial-model-reviewer` | Ready | 4/3/3/4/4/4/4 | 3.71 | none required |
| `frontend-experience-engineer` | Useful but Thin | 4/2/3/4/2/4/4 | 3.29 | raise skill/reference use; raise handoffs/boundaries |
| `geolocation-chronolocation-analyst` | Useful but Thin | 4/2/3/4/3/3/4 | 3.29 | raise skill/reference use |
| `grant-opportunity-scout` | Ready | 3/3/3/4/4/4/4 | 3.57 | optional: deepen examples, evidence fields, and handoffs |
| `grant-reporting-specialist` | Ready | 3/3/3/4/4/4/4 | 3.57 | optional: deepen examples, evidence fields, and handoffs |
| `impact-assessment-writer` | Ready | 4/3/3/4/4/4/4 | 3.71 | none required |
| `implementation-finisher` | Useful but Thin | 4/2/3/3/2/4/4 | 3.14 | raise skill/reference use; raise handoffs/boundaries |
| `indexing-coordinator` | Ready | 3/3/3/3/4/4/4 | 3.43 | optional: deepen examples, evidence fields, and handoffs |
| `invoice-reconciliation-specialist` | Ready | 3/3/3/4/4/4/4 | 3.57 | optional: deepen examples, evidence fields, and handoffs |
| `journal-submission-specialist` | Ready | 4/3/3/3/4/4/4 | 3.57 | optional: deepen examples, evidence fields, and handoffs |
| `knowledge-base-author` | Useful but Thin | 4/2/3/3/3/4/4 | 3.29 | raise skill/reference use |
| `legal-ops-coordinator` | Ready | 4/4/4/4/4/4/4 | 4.00 | none required |
| `legal-research-analyst` | Ready | 4/4/4/4/4/4/4 | 4.00 | none required |
| `legislative-tracker` | Ready | 3/3/3/4/4/4/4 | 3.57 | optional: deepen examples, evidence fields, and handoffs |
| `literature-reviewer` | Ready | 4/3/3/4/4/4/4 | 3.71 | none required |
| `localization-engineer` | Ready | 4/4/3/3/3/4/4 | 3.57 | optional: deepen examples, evidence fields, and handoffs |
| `market-researcher` | Ready | 4/4/3/4/3/4/4 | 3.71 | none required |
| `misinformation-risk-analyst` | Useful but Thin | 4/2/3/4/3/4/4 | 3.43 | raise skill/reference use |
| `ml-engineer` | Ready | 4/4/4/4/4/4/4 | 4.00 | none required |
| `mlops-engineer` | Ready | 4/4/4/4/4/4/4 | 4.00 | none required |
| `news-fact-checker` | Useful but Thin | 4/2/3/4/3/3/4 | 3.29 | raise skill/reference use |
| `observability-incident-engineer` | Ready | 4/4/3/4/3/4/4 | 3.71 | none required |
| `osint-research-lead` | Useful but Thin | 4/2/3/4/3/4/4 | 3.43 | raise skill/reference use |
| `peer-review-prep-editor` | Ready | 4/3/3/3/4/4/4 | 3.57 | optional: deepen examples, evidence fields, and handoffs |
| `performance-investigator` | Ready | 4/4/3/4/3/4/4 | 3.71 | none required |
| `performance-optimizer` | Useful but Thin | 4/2/3/4/2/4/4 | 3.29 | raise skill/reference use; raise handoffs/boundaries |
| `permissions-reviewer` | Ready | 3/3/3/4/4/4/4 | 3.57 | optional: deepen examples, evidence fields, and handoffs |
| `policy-analyst` | Ready | 3/3/3/4/4/4/4 | 3.57 | optional: deepen examples, evidence fields, and handoffs |
| `privacy-compliance-reviewer` | Ready | 4/4/3/4/3/4/4 | 3.71 | none required |
| `procurement-compliance-specialist` | Ready | 4/3/3/4/4/4/4 | 3.71 | none required |
| `product-discovery-strategist` | Useful but Thin | 4/4/3/4/2/4/4 | 3.57 | raise handoffs/boundaries |
| `production-editor` | Ready | 4/3/3/4/4/4/4 | 3.71 | none required |
| `prompt-evaluation-engineer` | Ready | 4/4/3/4/3/4/4 | 3.71 | none required |
| `proposal-compliance-reviewer` | Ready | 4/3/3/4/4/4/4 | 3.71 | none required |
| `public-comment-drafter` | Ready | 4/3/3/4/4/4/4 | 3.71 | none required |
| `public-records-researcher` | Useful but Thin | 4/2/3/4/3/4/4 | 3.43 | raise skill/reference use |
| `rapid-prototype-scout` | Useful but Thin | 4/2/3/4/2/4/4 | 3.29 | raise skill/reference use; raise handoffs/boundaries |
| `records-retention-advisor` | Ready | 4/4/4/4/4/4/4 | 4.00 | none required |
| `refactor-surgeon` | Useful but Thin | 4/2/3/3/3/4/4 | 3.29 | raise skill/reference use |
| `regulatory-monitor` | Ready | 4/4/4/4/4/4/4 | 4.00 | none required |
| `research-data-curator` | Ready | 4/3/3/4/4/4/4 | 3.71 | none required |
| `research-methods-reviewer` | Ready | 3/3/3/4/4/4/4 | 3.57 | optional: deepen examples, evidence fields, and handoffs |
| `rfp-response-analyst` | Ready | 4/3/3/4/4/4/4 | 3.71 | none required |
| `security-fix-engineer` | Useful but Thin | 4/2/3/4/3/4/4 | 3.43 | raise skill/reference use |
| `security-threat-modeler` | Ready | 4/4/3/4/3/4/4 | 3.71 | none required |
| `social-network-analyst` | Useful but Thin | 4/2/3/4/3/4/4 | 3.43 | raise skill/reference use |
| `software-engineering-lead` | Ready | 4/4/4/4/4/4/4 | 4.00 | none required |
| `source-verification-analyst` | Useful but Thin | 4/2/3/3/3/4/4 | 3.29 | raise skill/reference use |
| `sow-reviewer` | Ready | 4/3/3/4/4/4/4 | 3.71 | none required |
| `sponsored-projects-coordinator` | Ready | 3/3/3/4/4/4/4 | 3.57 | optional: deepen examples, evidence fields, and handoffs |
| `stakeholder-map-analyst` | Ready | 4/3/3/4/4/4/4 | 3.71 | none required |
| `standards-ethics-editor` | Useful but Thin | 4/2/3/4/3/3/4 | 3.29 | raise skill/reference use |
| `support-automation-engineer` | Useful but Thin | 4/2/3/4/3/4/4 | 3.43 | raise skill/reference use |
| `support-triage-specialist` | Useful but Thin | 4/2/3/3/3/4/4 | 3.29 | raise skill/reference use |
| `systems-architect` | Ready | 4/4/3/4/3/4/4 | 3.71 | none required |
| `technical-planner` | Ready | 4/4/3/4/3/4/4 | 3.71 | none required |
| `test-automation-engineer` | Useful but Thin | 4/2/3/4/3/4/4 | 3.43 | raise skill/reference use |
| `test-strategy-architect` | Ready | 4/4/3/4/3/4/4 | 3.71 | none required |
| `triage-router` | Ready | 4/3/3/3/3/4/4 | 3.43 | optional: deepen examples, evidence fields, and handoffs |
| `ux-flow-architect` | Ready | 4/4/3/4/3/3/4 | 3.57 | optional: deepen examples, evidence fields, and handoffs |
| `vendor-risk-reviewer` | Ready | 3/3/3/4/4/4/4 | 3.57 | optional: deepen examples, evidence fields, and handoffs |
| `vendor-scorecard-analyst` | Ready | 3/3/3/4/4/4/4 | 3.57 | optional: deepen examples, evidence fields, and handoffs |

## Validation Evidence

- Parsed all TOML files under `AGENTS/openai/`.
- Checked every `$skill` reference against `SKILLS/<skill-name>/SKILL.md`.
- Checked agent registry membership against `REFERENCES/software-development-crew.md`.
- Reviewed `SKILL.md` plus local `references/` content for each skill package.
- Used `REFERENCES/quality-rubric.md` readiness labels and criteria.
