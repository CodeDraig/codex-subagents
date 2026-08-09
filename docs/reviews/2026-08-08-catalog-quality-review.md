# Catalog Quality Review

Date: 2026-08-08

Scope: every current skill package under `SKILLS/` and every OpenAI subagent profile under `AGENTS/openai/`, scored against `REFERENCES/quality-rubric.md`. The machine-readable record is `docs/reviews/2026-08-08-catalog-quality-review.csv`.

## Outcome

The corrected catalog contains 144 Ready assets and five Useful but Thin assets. All 53 skills now meet the Ready gate; the remaining five findings are public-source agent profiles that omit both a skill reference and an explicit no-skill justification.

| Asset type | Reviewed | Ready | Useful but Thin | Scaffold Only | Unsafe or Misleading |
| --- | ---: | ---: | ---: | ---: | ---: |
| Skills | 53 | 53 | 0 | 0 | 0 |
| Agents | 96 | 91 | 5 | 0 | 0 |
| Total | 149 | 144 | 5 | 0 | 0 |

## Scoring Method

- Skills: trigger fit / workflow specificity / domain heuristics / supporting assets / tooling and validation / output contract / boundaries and stop conditions.
- Agents: role distinctness / skill and reference use / instruction depth / model, reasoning, and sandbox fit / handoffs and boundaries / output contract / catalog integration.
- Every `SKILL.md`, referenced support file, `agents/openai.yaml`, and agent TOML was reviewed. Sampling was not used.
- The Ready gate requires all seven criteria to score at least 3. Sidecar metadata conformance is included in the supporting-assets assessment for skills.
- Scores measure reusable package quality and current structural conformance; they are not behavioral win-rate measurements.

## Findings

### 1. Resolved: all sidecar descriptions now meet the UI contract

The 26 descriptions previously exceeding 64 characters were shortened without changing their display names, default prompts, skill instructions, references, or package behavior. All 53 quoted descriptions now fall between 25 and 64 characters.

| Skill | Corrected short description | Characters |
| --- | --- | ---: |
| `academic-literature-review` | Synthesize scholarly evidence, disagreements, and gaps | 54 |
| `audit-evidence-management` | Organize audit evidence, traceability, and exceptions | 53 |
| `book-metadata-packaging` | Prepare book metadata and launch package checks | 47 |
| `citation-integrity-review` | Check citations, quotations, and bibliography integrity | 55 |
| `fact-checking-source-review` | Verify manuscript claims against source evidence | 48 |
| `fiction-development-workflows` | Develop fiction structure, arcs, continuity, and revisions | 58 |
| `finance-operations-review` | Review finance assumptions, variances, controls, and evidence | 61 |
| `grant-budget-justification` | Draft grant budget narratives and restriction checks | 52 |
| `grant-proposal-compliance` | Build grant proposal compliance matrices | 40 |
| `invoice-reconciliation-workflows` | Reconcile invoices, orders, receipts, and approvals | 51 |
| `journal-submission-workflows` | Prepare journal submissions and reviewer responses | 50 |
| `legal-research-workflows` | Organize source-backed legal and regulatory research | 52 |
| `legislative-tracking` | Track legislation, amendments, votes, and deadlines | 51 |
| `line-copyediting-workflows` | Perform line edits, copyedits, and consistency passes | 53 |
| `mlops-readiness` | Review model release, monitoring, and rollback readiness | 56 |
| `nonfiction-manuscript-development` | Develop nonfiction arguments, chapters, and evidence plans | 58 |
| `permissions-rights-review` | Track permissions, licenses, attribution, and restrictions | 58 |
| `policy-analysis-workflows` | Analyze policy impacts, tradeoffs, and evidence gaps | 52 |
| `procurement-vendor-review` | Compare vendors, requirements, evidence, and risks | 50 |
| `public-comment-drafting` | Draft sourced public comments and submission checks | 51 |
| `publishing-production-workflows` | Coordinate manuscripts, proofs, schedules, and blockers | 55 |
| `records-retention-operations` | Map records, retention, holds, and approval gates | 49 |
| `research-methods-review` | Review study validity, methods, and reproducibility | 51 |
| `rfp-response-workflows` | Build RFP response matrices and compliance checks | 49 |
| `sow-review-workflows` | Review SOW deliverables, milestones, and acceptance criteria | 60 |
| `sponsored-projects-reporting` | Organize sponsored-project reporting and closeout | 49 |

### 2. Five public-source profiles still need explicit skill integration

These profiles have strong domain instructions, safety boundaries, handoffs, and exact return contracts. Agent criterion 2 remains below Ready because each lacks both a relevant `$skill-name` reference and a written explanation that no catalog skill fits.

| Agent | Required fix |
| --- | --- |
| `geolocation-chronolocation-analyst` | Reference a relevant Skill with fallback, or explicitly document why no repo-local Skill fits. |
| `misinformation-risk-analyst` | Reference a relevant Skill with fallback, or explicitly document why no repo-local Skill fits. |
| `osint-research-lead` | Reference a relevant Skill with fallback, or explicitly document why no repo-local Skill fits. |
| `public-records-researcher` | Reference a relevant Skill with fallback, or explicitly document why no repo-local Skill fits. |
| `social-network-analyst` | Reference a relevant Skill with fallback, or explicitly document why no repo-local Skill fits. |

### 3. Cross-catalog references and runtime declarations are coherent

- All 96 TOMLs parse, filenames match `name`, required fields are present, all 88 explicit skill references resolve, and all named handoffs inspected resolve to implemented profiles.
- All 96 agents and all 52 registry-managed skills appear in `REFERENCES/software-development-crew.md`; `codex-subagent-designer` is intentionally the meta-catalog exception.
- Model choices use the current documented Codex roster: `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, and `gpt-5.3-codex-spark`.

### 4. The catalog validator still does not enforce the length rule

`scripts/catalog_quality/validate_catalog.py` checks sidecar field presence but not the 25-64 character constraint. No validator change was made because this remediation was explicitly limited to descriptions and audit updates. `scripts/catalog_quality/score_audit.py` remains bound to the unchanged May all-Ready matrix and does not validate this review.

## Highest-Scoring Assets

These assets scored 4 on all seven criteria:

- Skills: `analytics-engineering`, `api-contract-review`, `codex-subagent-designer`, `competitive-research`, `dependency-risk-triage`, `product-discovery`, `threat-modeling`.
- Agents: `analytics-engineer`, `api-contract-architect`, `data-scientist`, `knowledge-base-author`, `market-researcher`, `ml-engineer`, `mlops-engineer`, `product-discovery-strategist`, `security-threat-modeler`, `support-automation-engineer`.

## Family Results

| Family | Skills | Agents | Ready | Useful but Thin | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| `data-analytics-ml` | 4 | 5 | 9 | 0 | 9 |
| `legal-policy-procurement-finance-grants` | 15 | 25 | 40 | 0 | 40 |
| `meta-catalog` | 1 | 0 | 1 | 0 | 1 |
| `product-ux-design-support-docs` | 2 | 8 | 10 | 0 | 10 |
| `research-news-publishing-editorial` | 11 | 26 | 32 | 5 | 37 |
| `software-engineering-core` | 20 | 32 | 52 | 0 | 52 |

## Skill Scores

| Skill | Family | Scores | Total | Rating | Required fix |
| --- | --- | --- | ---: | --- | --- |
| `academic-literature-review` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `accessibility-audit` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `ai-evals` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `analytics-engineering` | `data-analytics-ml` | `4/4/4/4/4/4/4` | 28 | Ready | None. |
| `api-contract-review` | `software-engineering-core` | `4/4/4/4/4/4/4` | 28 | Ready | None. |
| `architecture-decision-records` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `audit-evidence-management` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `book-metadata-packaging` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `citation-integrity-review` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `codex-subagent-designer` | `meta-catalog` | `4/4/4/4/4/4/4` | 28 | Ready | None. |
| `competitive-research` | `product-ux-design-support-docs` | `4/4/4/4/4/4/4` | 28 | Ready | None. |
| `contract-review-operations` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `data-modeling` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `data-science-workflows` | `data-analytics-ml` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `dependency-risk-triage` | `software-engineering-core` | `4/4/4/4/4/4/4` | 28 | Ready | None. |
| `design-system-audit` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `docs-information-architecture` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `engineering-execution` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `fact-checking-source-review` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `fiction-development-workflows` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `finance-operations-review` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `grant-budget-justification` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `grant-proposal-compliance` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `implementation-planning` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `incident-postmortems` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `invoice-reconciliation-workflows` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `journal-submission-workflows` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `legal-research-workflows` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `legislative-tracking` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `line-copyediting-workflows` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `localization-readiness` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `ml-engineering` | `data-analytics-ml` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `mlops-readiness` | `data-analytics-ml` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `nonfiction-manuscript-development` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `observability-runbooks` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `performance-profiling` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `permissions-rights-review` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `policy-analysis-workflows` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `privacy-review` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `procurement-vendor-review` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `product-discovery` | `product-ux-design-support-docs` | `4/4/4/4/4/4/4` | 28 | Ready | None. |
| `prompt-injection-defense` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `public-comment-drafting` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `publishing-production-workflows` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `records-retention-operations` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `release-readiness` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `research-methods-review` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `rfp-response-workflows` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `sow-review-workflows` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `sponsored-projects-reporting` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `test-matrix-design` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `threat-modeling` | `software-engineering-core` | `4/4/4/4/4/4/4` | 28 | Ready | None. |
| `ux-flow-mapping` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |

## Agent Scores

| Agent | Family | Scores | Total | Rating | Required fix |
| --- | --- | --- | ---: | --- | --- |
| `accessibility-reviewer` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `accounting-controls-reviewer` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `ai-feature-engineer` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `analytics-engineer` | `data-analytics-ml` | `4/4/4/4/4/4/4` | 28 | Ready | None. |
| `api-contract-architect` | `software-engineering-core` | `4/4/4/4/4/4/4` | 28 | Ready | None. |
| `assignment-editor` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `audience-seo-editor` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `audit-evidence-organizer` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `backend-domain-engineer` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `book-metadata-packaging-editor` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `breaking-news-reporter` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `budget-justification-writer` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `budget-variance-analyst` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `build-release-engineer` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `citation-integrity-checker` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `code-reviewer` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `contract-review-specialist` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `copy-desk-editor` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `customer-communications-specialist` | `product-ux-design-support-docs` | `4/3/4/4/4/4/4` | 27 | Ready | None. |
| `customer-diagnostics-engineer` | `product-ux-design-support-docs` | `4/3/4/4/4/4/4` | 27 | Ready | None. |
| `data-platform-engineer` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `data-scientist` | `data-analytics-ml` | `4/4/4/4/4/4/4` | 28 | Ready | None. |
| `database-modeler` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `dependency-maintenance-engineer` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `design-system-engineer` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `developer-experience-engineer` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `developmental-manuscript-editor` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `devops-platform-engineer` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `documentation-engineer` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `escalation-support-engineer` | `product-ux-design-support-docs` | `4/3/4/4/4/4/4` | 27 | Ready | None. |
| `fact-checking-editor` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `fiction-development-editor` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `financial-model-reviewer` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `frontend-experience-engineer` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `geolocation-chronolocation-analyst` | `research-news-publishing-editorial` | `4/2/4/4/4/4/4` | 26 | Useful but Thin | Reference a relevant $skill with a fallback, or state explicitly that no repo-local Skill fits and identify these instructions as the fallback workflow. |
| `grant-opportunity-scout` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `grant-reporting-specialist` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `impact-assessment-writer` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `implementation-finisher` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `indexing-coordinator` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `invoice-reconciliation-specialist` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `journal-submission-specialist` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `knowledge-base-author` | `product-ux-design-support-docs` | `4/4/4/4/4/4/4` | 28 | Ready | None. |
| `legal-ops-coordinator` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `legal-research-analyst` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `legislative-tracker` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `line-copy-editor` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `literature-reviewer` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `localization-engineer` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `market-researcher` | `product-ux-design-support-docs` | `4/4/4/4/4/4/4` | 28 | Ready | None. |
| `misinformation-risk-analyst` | `research-news-publishing-editorial` | `4/2/4/4/4/4/4` | 26 | Useful but Thin | Reference a relevant $skill with a fallback, or state explicitly that no repo-local Skill fits and identify these instructions as the fallback workflow. |
| `ml-engineer` | `data-analytics-ml` | `4/4/4/4/4/4/4` | 28 | Ready | None. |
| `mlops-engineer` | `data-analytics-ml` | `4/4/4/4/4/4/4` | 28 | Ready | None. |
| `news-fact-checker` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `nonfiction-manuscript-editor` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `observability-incident-engineer` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `osint-research-lead` | `research-news-publishing-editorial` | `4/2/4/4/4/4/4` | 26 | Useful but Thin | Reference a relevant $skill with a fallback, or state explicitly that no repo-local Skill fits and identify these instructions as the fallback workflow. |
| `peer-review-prep-editor` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `performance-investigator` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `performance-optimizer` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `permissions-reviewer` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `policy-analyst` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `privacy-compliance-reviewer` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `procurement-compliance-specialist` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `product-discovery-strategist` | `product-ux-design-support-docs` | `4/4/4/4/4/4/4` | 28 | Ready | None. |
| `production-editor` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `prompt-evaluation-engineer` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `proposal-compliance-reviewer` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `public-comment-drafter` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `public-records-researcher` | `research-news-publishing-editorial` | `4/2/4/4/4/4/4` | 26 | Useful but Thin | Reference a relevant $skill with a fallback, or state explicitly that no repo-local Skill fits and identify these instructions as the fallback workflow. |
| `rapid-prototype-scout` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `records-retention-advisor` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `refactor-surgeon` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `regulatory-monitor` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `research-data-curator` | `data-analytics-ml` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `research-methods-reviewer` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `rfp-response-analyst` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `security-fix-engineer` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `security-threat-modeler` | `software-engineering-core` | `4/4/4/4/4/4/4` | 28 | Ready | None. |
| `social-network-analyst` | `research-news-publishing-editorial` | `4/2/4/4/4/4/4` | 26 | Useful but Thin | Reference a relevant $skill with a fallback, or state explicitly that no repo-local Skill fits and identify these instructions as the fallback workflow. |
| `software-engineering-lead` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `source-verification-analyst` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `sow-reviewer` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `sponsored-projects-coordinator` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `stakeholder-map-analyst` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `standards-ethics-editor` | `research-news-publishing-editorial` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `support-automation-engineer` | `product-ux-design-support-docs` | `4/4/4/4/4/4/4` | 28 | Ready | None. |
| `support-triage-specialist` | `product-ux-design-support-docs` | `4/3/4/4/4/4/4` | 27 | Ready | None. |
| `systems-architect` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `technical-planner` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `test-automation-engineer` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `test-strategy-architect` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `triage-router` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `ux-flow-architect` | `software-engineering-core` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `vendor-risk-reviewer` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |
| `vendor-scorecard-analyst` | `legal-policy-procurement-finance-grants` | `3/3/3/3/3/3/3` | 21 | Ready | None. |

## Validation Evidence

- PyYAML and exact sidecar checks -> 53/53 descriptions are quoted strings 25-64 characters; all 26 approved replacements match exactly.
- `.validate-venv/bin/python` with the bundled skill validator -> 53/53 packages returned `Skill is valid!`.
- `python3.11 scripts/catalog_quality/validate_catalog.py` -> passed: `catalog validation passed`.
- CSV integrity check -> 149 unique assets, exact catalog coverage, score arithmetic, gate-consistent ratings, and `144 Ready / 5 Useful but Thin`.
- `python3.11 scripts/catalog_quality/score_audit.py` -> passed against the unchanged legacy May matrix only.
- Report UTF-8, final-newline, whitespace, coverage, and final-diff checks are recorded after the final pass.

Current product assumptions were checked against the official [Codex models](https://learn.chatgpt.com/docs/models), [custom subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), and [skill authoring](https://learn.chatgpt.com/docs/build-skills) documentation.

## Assumptions And Remaining Uncertainty

- Only the 26 approved `short_description` values changed. The 27 valid values, all display names, all default prompts, SKILL.md bodies, references, agents, and validators remain untouched.
- The short-description field contract is 25-64 characters. This review verifies conformance but does not claim that a runtime rejects longer values.
- The extra top-level `examples` mapping in `SKILLS/codex-subagent-designer/agents/openai.yaml` remains untested and was not changed because unknown-key behavior was not demonstrated.
- The pre-existing edit to `REFERENCES/software-development-crew.md` was preserved.
- Static review does not prove task performance. The next sharp edge is to add the length guard to the catalog validator and resolve the five remaining agent-integration findings.
