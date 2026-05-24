---
title: "Data Science, Engineering, and Analytics Agents"
created: "2026-05-17T00:00:00-04:00"
status: "approved"
authors: ["TechLead", "User"]
type: "design"
design_depth: "standard"
task_complexity: "medium"
---

# Data Science, Engineering, and Analytics Agents Design Document

## Problem Statement

The current `codex-subagents` catalog already covers a broad software lifecycle, including backend, frontend, platform, database modeling, data platform work, AI feature engineering, prompt evaluation, and operations. However, it does not yet provide complete, explicit coverage for a modern data and execution-engineering crew: data science, analytics engineering, ML engineering, MLOps, and technical delivery coordination. The existing `data-platform-engineer` agent covers ingestion, transformation, warehouses, lakehouses, reporting, lineage, and backfills, but that role is too platform-oriented to stand in for data-science experimentation, product analytics, semantic modeling, ML model implementation, or MLOps productionization.

The design adds a complementary domain crew that reuses the existing catalog where it already has strong ownership and adds new agents and supporting skills only where coverage is incomplete. The goal is not to replace `data-platform-engineer`, `database-modeler`, `backend-domain-engineer`, `devops-platform-engineer`, `systems-architect`, or `technical-planner`; the goal is to make routing more precise when tasks involve data science, analytics models, ML implementation, model operations, and cross-cutting execution engineering.

## Requirements

### Functional Requirements

1. **REQ-1**: Add a complementary data and execution-engineering crew to the agent examples, with coverage for data science, analytics engineering, ML engineering, MLOps, and software engineering delivery coordination.
2. **REQ-2**: Add repo-local skills for the new agent domains so the agents can invoke reusable methodology instead of carrying all workflow logic only inside TOML instructions.
3. **REQ-3**: Reuse existing agents wherever they already provide sufficient coverage. `data-platform-engineer` remains the owner for ingestion, transformation, warehouse/lakehouse, reporting pipelines, lineage, and backfills; `database-modeler` remains the owner for persistence shape, retention, indexing, and migrations; `devops-platform-engineer` remains the owner for general infrastructure and CI/CD.
4. **REQ-4**: Update `REFERENCES/software-development-crew.md` so lifecycle coverage, routing rules, model coverage, intentional overlap, implemented skill assets, and remaining backlog stay synchronized.
5. **REQ-5**: Ensure every new TOML file parses cleanly and follows the established template pattern: `name`, `description`, `model`, `model_reasoning_effort`, `sandbox_mode`, `nickname_candidates`, and exact output sections.

### Non-Functional Requirements

1. **REQ-6**: Preserve routing clarity. New roles must have explicit stop rules and handoff boundaries to reduce generic `worker`/`explorer` fallback and avoid duplicate ownership.
2. **REQ-7**: Keep maintenance cost proportional. The catalog should be complete for the selected domain crew, but not become a full data-organization taxonomy unless needed.
3. **REQ-8**: Preserve installability. The resulting repo-local assets should remain copyable into `~/.codex/agents` and `~/.codex/skills`.

### Constraints

- Follow the existing repo layout and examples.
- Avoid replacing or weakening existing agents.
- Keep skill names and agent names kebab-case and specific enough for routing.

## Approach

### Selected Approach

**Complementary Domain Crew**

Add a bounded but complete domain crew that fills the gaps around the existing catalog instead of replacing it. The core new agents should be:

- `data-scientist`: Owns exploratory analysis, statistical framing, experiment design support, feature analysis, notebooks/scripts, and evidence-backed findings.
- `analytics-engineer`: Owns semantic models, metric definitions, BI-ready transformations, dashboards, dbt-style models, data tests, and stakeholder-facing analytical contracts.
- `ml-engineer`: Owns model training/inference code, feature pipelines, evaluation harnesses, model integration, and production-facing ML behavior.
- `mlops-engineer`: Owns model deployment, monitoring, registry/release workflows, drift checks, reproducibility, and operational controls.
- `software-engineering-lead`: Owns execution coordination across implementation slices, integration risks, technical sequencing, and final delivery coherence without becoming a people-management role.

This approach is selected because it matches the requested full-domain coverage while incorporating the existing build wherever possible. The main design decision is complementary ownership: `data-platform-engineer` continues to own data infrastructure and pipeline correctness; `database-modeler` owns durable data shape; `devops-platform-engineer` owns general platform automation; the new roles own data science, analytics semantics, ML implementation, ML operations, and software execution coordination.

### Alternatives Considered

#### Full Data Organization Crew

- **Description**: Add a broader roster including BI engineer, experimentation analyst, data engineer, and separate staff or engineering manager roles.
- **Pros**: Stronger coverage for a large data organization; more specialized routing for niche analytics and experimentation tasks.
- **Cons**: More files, more skills, and more overlap with existing `data-platform-engineer`, `database-modeler`, and platform roles.
- **Rejected Because**: It would add more overlap and maintenance than the current request requires.

#### Broad Lead Agents

- **Description**: Add only `data-science-lead`, `engineering-lead`, and `analytics-lead`, plus supporting skills.
- **Pros**: Lowest file count and a simple mental model.
- **Cons**: Weak fit for direct execution; likely to blur into `systems-architect`, `technical-planner`, and generic coordination work.
- **Rejected Because**: It conflicts with the selected execution-engineering direction and would be less useful for direct implementation delegation.

### Decision Matrix

| Criterion | Weight | Complementary Domain Crew | Full Data Organization Crew | Broad Lead Agents |
|-----------|--------|---------------------------|-----------------------------|-------------------|
| Boundary clarity | 30% | 5: Complements existing roles with explicit overlap notes. | 3: Complete but creates more duplicate edges. | 2: Broad leads are harder to route precisely. |
| Coverage depth | 25% | 4: Covers the major requested domains. | 5: Covers the widest data-org surface. | 3: Covers labels but not execution lanes. |
| Maintenance cost | 20% | 4: Moderate additions and synchronized registry changes. | 2: More files, more skills, more routing upkeep. | 5: Fewest files. |
| Execution usefulness | 25% | 5: Strong direct delegation fit. | 5: Strongest direct delegation fit. | 2: Better for planning than implementation. |
| **Weighted Total** | | **4.55** | **3.85** | **2.85** |

## Architecture & Coverage

The implementation should preserve the current repository architecture: agent templates are TOML files under `AGENTS/openai/`, reusable methodologies are skill folders under `SKILLS/`, and the crew registry is `REFERENCES/software-development-crew.md`.

### Component Diagram

```text
AGENTS/openai/
  data-scientist.toml
  analytics-engineer.toml
  ml-engineer.toml
  mlops-engineer.toml
  software-engineering-lead.toml

REFERENCES/
  software-development-crew.md

SKILLS/
  data-science-workflows/
    SKILL.md
    agents/openai.yaml
    references/analysis-checklist.md
  analytics-engineering/
    SKILL.md
    agents/openai.yaml
    references/metrics-contract-checklist.md
  ml-engineering/
    SKILL.md
    agents/openai.yaml
    references/model-delivery-checklist.md
  mlops-readiness/
    SKILL.md
    agents/openai.yaml
    references/model-operations-checklist.md
  engineering-execution/
    SKILL.md
    agents/openai.yaml
    references/delivery-coordination-checklist.md
```

### Coverage Boundaries

- `data-scientist` handles statistical and exploratory analysis, experiment interpretation, feature analysis, data caveats, and decision evidence.
- `analytics-engineer` handles metric contracts, semantic layers, dbt-style transformations, dashboards, BI validation, and stakeholder-facing definitions.
- `ml-engineer` handles ML model code, feature pipelines, inference paths, eval harnesses, and integration with product behavior.
- `mlops-engineer` handles model release, monitoring, reproducibility, registry/versioning, drift, rollback, and runtime operational safety.
- `software-engineering-lead` handles multi-agent technical sequencing, integration readiness, cross-slice risk, and delivery coherence.

Existing role reuse remains explicit: use `data-platform-engineer` for core data pipeline and warehouse/lakehouse implementation, `database-modeler` for persistence design, `devops-platform-engineer` for general platform and CI/CD, and `systems-architect` or `technical-planner` for architecture/planning before execution.

## Agent Team

| Phase | Agent(s) | Parallel | Deliverables |
|-------|----------|----------|--------------|
| 1 | `technical-planner` | No | Implementation plan with file ownership and validation gates. |
| 2 | `documentation-engineer`, `prompt-evaluation-engineer` | Yes | Skill folder drafts, reference checklists, and TOML instruction consistency review. |
| 3 | `implementation-finisher` | No | Registry synchronization and final consistency pass. |
| 4 | `code-reviewer` | No | Findings-first review of routing clarity, overlap boundaries, and validation evidence. |

## Risk Assessment

| Risk | Severity | Likelihood | Mitigation |
|------|----------|------------|------------|
| New agents overlap too much with existing `data-platform-engineer`, `database-modeler`, or `devops-platform-engineer` | MEDIUM | MEDIUM | Add explicit routing rules, stop rules, and intentional-overlap notes in `software-development-crew.md` and in each TOML instruction block. |
| "Engineering" becomes too broad to route well | MEDIUM | MEDIUM | Define `software-engineering-lead` as execution coordination only: sequencing, integration risk, technical delivery coherence, and handoffs. Exclude people management and architecture ownership. |
| Supporting skills add maintenance burden | MEDIUM | LOW-MEDIUM | Keep each skill concise, checklist-driven, and aligned to one agent domain. Avoid building large generic textbooks. |
| Registry and implemented-skill sections drift from files added | MEDIUM | LOW | Validate with `rg --files`, TOML parsing, and a simple check that every referenced skill folder exists. |
| Coverage is still incomplete after the first pass | LOW-MEDIUM | MEDIUM | Treat existing roles as part of the complete coverage map and document exact handoffs. Add only missing roles now; leave niche roles such as BI engineer or experimentation analyst as future expansion only if still needed. |

## Success Criteria

1. Five new TOML agent examples exist and parse cleanly.
2. Five new repo-local skill folders exist with `SKILL.md`, `agents/openai.yaml`, and at least one focused reference checklist each.
3. `software-development-crew.md` includes the new crew in lifecycle coverage, routing rules, model coverage, intentional overlap, and implemented skill assets.
4. The coverage map clearly distinguishes new roles from existing `data-platform-engineer`, `database-modeler`, `backend-domain-engineer`, `devops-platform-engineer`, `systems-architect`, and `technical-planner`.
5. Validation confirms there are no missing skill references and no malformed TOML files.
