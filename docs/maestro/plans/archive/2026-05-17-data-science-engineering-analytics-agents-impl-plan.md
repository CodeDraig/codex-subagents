---
title: "Data Science, Engineering, and Analytics Agents Implementation Plan"
design_ref: "docs/maestro/plans/2026-05-17-data-science-engineering-analytics-agents-design.md"
created: "2026-05-17T00:00:00-04:00"
status: "approved"
total_phases: 5
estimated_files: 21
task_complexity: "medium"
---

# Data Science, Engineering, and Analytics Agents Implementation Plan

## Plan Overview

- **Total phases**: 5
- **Agents involved**: `technical-writer`, `prompt-engineer`, `coder`, `tester`, `code-reviewer`
- **Estimated effort**: Medium catalog expansion. The work creates five skill folders, five OpenAI TOML agent examples, and synchronized crew-registry updates. Most file creation can happen in parallel; registry editing and final validation must remain sequential.

## Dependency Graph

```text
Phase 1: Data + Analytics skills ─┐
                                  ├─> Phase 3: Agent TOMLs ─> Phase 4: Registry sync ─> Phase 5: Validation + review
Phase 2: ML + Engineering skills ─┘
```

## Execution Strategy

| Stage | Phases | Execution | Agent Count | Notes |
|-------|--------|-----------|-------------|-------|
| 1 | Phase 1, Phase 2 | Parallel | 2 | Create disjoint skill folders with no shared files. |
| 2 | Phase 3 | Sequential | 1 | Create agent TOMLs after skill names and output contracts are available. |
| 3 | Phase 4 | Sequential | 1 | Update the shared registry in one pass to avoid merge conflicts. |
| 4 | Phase 5 | Sequential | 2 | Validate parseability, missing references, and routing clarity. |

## Phase 1: Data Science and Analytics Skills

### Objective

Create the repo-local skills that support data-science and analytics-engineering agents.

### Agent: `technical-writer`
### Parallel: Yes

### Files to Create

- `data-science-workflows/SKILL.md` — Defines the reusable workflow for exploratory analysis, statistical framing, experiment interpretation, feature analysis, uncertainty, caveats, and evidence-backed recommendations. Output contract should include `Question`, `Data Reviewed`, `Method`, `Findings`, `Caveats`, `Recommended Decision`, and `Validation`.
- `data-science-workflows/agents/openai.yaml` — Skill interface metadata with display name, short description, and default prompt.
- `data-science-workflows/references/analysis-checklist.md` — Checklist for data inputs, assumptions, missingness, bias, leakage, experiment validity, uncertainty, and reproducibility.
- `analytics-engineering/SKILL.md` — Defines the reusable workflow for metric contracts, semantic layers, BI-ready transformations, dashboard validation, dbt-style models, and stakeholder definitions.
- `analytics-engineering/agents/openai.yaml` — Skill interface metadata.
- `analytics-engineering/references/metrics-contract-checklist.md` — Checklist for metric grain, dimensions, filters, ownership, freshness, tests, lineage, dashboard consumers, and breaking-change handling.

### Files to Modify

- None.

### Implementation Details

Follow the existing skill-folder convention used by `data-modeling/`, `ai-evals/`, and `observability-runbooks/`: frontmatter with `name` and `description`, a concise `#` heading, `Overview`, `Workflow`, reference pointer, `Output Contract`, and `Stop Conditions`.

Use kebab-case skill names:

- `$data-science-workflows`
- `$analytics-engineering`

Keep instructions concise and operational. Avoid broad educational prose; these skills should be checklists and workflows that agents can execute.

### Validation

- `rg --files data-science-workflows analytics-engineering` should list exactly the six expected files.
- `sed -n '1,80p' data-science-workflows/SKILL.md` and `sed -n '1,80p' analytics-engineering/SKILL.md` should show valid frontmatter and output contracts.

### Dependencies

- Blocked by: None
- Blocks: Phase 3

---

## Phase 2: ML, MLOps, and Engineering Execution Skills

### Objective

Create the repo-local skills that support ML implementation, model operations, and execution-engineering coordination.

### Agent: `technical-writer`
### Parallel: Yes

### Files to Create

- `ml-engineering/SKILL.md` — Defines the reusable workflow for model training/inference code, feature pipelines, evaluation harnesses, integration boundaries, and production-facing ML behavior.
- `ml-engineering/agents/openai.yaml` — Skill interface metadata.
- `ml-engineering/references/model-delivery-checklist.md` — Checklist for data splits, feature contracts, baseline metrics, evaluation criteria, model artifacts, inference APIs, and rollback limits.
- `mlops-readiness/SKILL.md` — Defines the reusable workflow for model registry, deployment, monitoring, reproducibility, drift, rollback, and model release controls.
- `mlops-readiness/agents/openai.yaml` — Skill interface metadata.
- `mlops-readiness/references/model-operations-checklist.md` — Checklist for model versioning, promotion gates, observability, drift thresholds, rollback, reproducibility, runtime constraints, and approval points.
- `engineering-execution/SKILL.md` — Defines the reusable workflow for multi-agent execution coordination, technical sequencing, integration risks, ownership boundaries, and delivery coherence.
- `engineering-execution/agents/openai.yaml` — Skill interface metadata.
- `engineering-execution/references/delivery-coordination-checklist.md` — Checklist for scope decomposition, file ownership, dependency order, validation gates, integration risk, handoffs, and final readiness.

### Files to Modify

- None.

### Implementation Details

Follow the same skill-folder convention as Phase 1. Make stop conditions explicit:

- `$ml-engineering` should stop when model behavior lacks a target metric, labeled evaluation set, or clear inference contract.
- `$mlops-readiness` should stop when deployment, registry, production monitoring, or rollback actions could mutate remote infrastructure or production behavior without approval.
- `$engineering-execution` should stop when ownership, dependency order, or validation gates are unresolved.

### Validation

- `rg --files ml-engineering mlops-readiness engineering-execution` should list exactly the nine expected files.
- `sed -n '1,80p'` for each new `SKILL.md` should show valid frontmatter and output contracts.

### Dependencies

- Blocked by: None
- Blocks: Phase 3

---

## Phase 3: Agent TOML Templates

### Objective

Create five OpenAI TOML agent examples that invoke the new skills and preserve existing catalog boundaries.

### Agent: `prompt-engineer`
### Parallel: No

### Files to Create

- `codex-subagent-designer/agents/examples/openai/data-scientist.toml` — Data science analysis and experiment interpretation agent. Use `gpt-5.5` with `high` reasoning and `workspace-write` so it can create notebooks/scripts or analysis artifacts when assigned.
- `codex-subagent-designer/agents/examples/openai/analytics-engineer.toml` — Metric, semantic-model, BI, and analytics transformation agent. Use `gpt-5.3-codex` with `high` reasoning and `workspace-write`.
- `codex-subagent-designer/agents/examples/openai/ml-engineer.toml` — Model training/inference and evaluation implementation agent. Use `gpt-5.3-codex` with `high` reasoning and `workspace-write`.
- `codex-subagent-designer/agents/examples/openai/mlops-engineer.toml` — Model operations, registry, monitoring, drift, release, and rollback agent. Use `gpt-5.5` with `high` reasoning and `workspace-write`.
- `codex-subagent-designer/agents/examples/openai/software-engineering-lead.toml` — Execution-coordination agent for multi-slice implementation, integration readiness, and technical delivery coherence. Use `gpt-5.5` with `high` reasoning and `read-only` unless assigned to write implementation plans; if write access is needed for handoff artifacts, use `workspace-write` with strict non-implementation instructions.

### Files to Modify

- None.

### Implementation Details

Each TOML must follow the established structure:

```toml
name = "<agent-name>"
description = "<one-sentence role description>"
model = "<model>"
model_reasoning_effort = "<effort>"
sandbox_mode = "<read-only|workspace-write>"
nickname_candidates = ["<Name>", "<Name>", "<Name>"]

developer_instructions = """
...
Return exactly these sections: ...
"""
```

Each agent must include:

- A clear first step that restates owned surface, inputs, outputs, and validation target.
- "You are not alone in the codebase" concurrency guidance.
- Skill invocation guidance for its new skill.
- Explicit handoff boundaries to existing agents:
  - `data-platform-engineer` for core pipeline/warehouse/lakehouse implementation.
  - `database-modeler` for persistence shape, retention, indexing, and migrations.
  - `devops-platform-engineer` for general infrastructure and CI/CD.
  - `systems-architect` and `technical-planner` for architecture and planning.
- Hard stop conditions for unsafe scope, missing evidence, or production-risking actions.
- Exact output sections tailored to the role.

### Validation

- Parse all new TOML files with Python `tomllib`.
- Confirm each new TOML references the expected skill name.
- Confirm each new TOML has `name`, `description`, `model`, `model_reasoning_effort`, `sandbox_mode`, `nickname_candidates`, and `developer_instructions`.

### Dependencies

- Blocked by: Phase 1, Phase 2
- Blocks: Phase 4

---

## Phase 4: Crew Registry Synchronization

### Objective

Update the canonical crew registry so the new agents and skills are discoverable, routable, and documented alongside existing coverage.

### Agent: `coder`
### Parallel: No

### Files to Create

- None.

### Files to Modify

- `codex-subagent-designer/references/software-development-crew.md` — Add the new crew to lifecycle coverage, routing rules, model coverage, intentional overlap, implemented skill assets, and use guidance.

### Implementation Details

Registry updates should include:

- A new lifecycle row or expanded product implementation/data row that includes `data-scientist`, `analytics-engineer`, `ml-engineer`, `mlops-engineer`, and `software-engineering-lead`.
- Routing rules for:
  - Exploratory analysis, statistical framing, experiment interpretation -> `data-scientist`.
  - Metric definitions, semantic models, dashboards, BI transformations -> `analytics-engineer`.
  - Model training/inference code, feature pipelines, eval harnesses -> `ml-engineer`.
  - Model registry, deployment readiness, drift, model monitoring, rollback -> `mlops-engineer`.
  - Multi-slice execution sequencing, integration risk, delivery coherence -> `software-engineering-lead`.
- Intentional-overlap entries documenting the boundaries with `data-platform-engineer`, `database-modeler`, `devops-platform-engineer`, `systems-architect`, and `technical-planner`.
- Model coverage updates for the chosen models.
- Implemented skill assets entries for:
  - `$data-science-workflows`: `data-science-workflows/`
  - `$analytics-engineering`: `analytics-engineering/`
  - `$ml-engineering`: `ml-engineering/`
  - `$mlops-readiness`: `mlops-readiness/`
  - `$engineering-execution`: `engineering-execution/`

Keep "Remaining Skill Backlog" as `None` if every referenced skill is implemented.

### Validation

- `rg -n "data-scientist|analytics-engineer|ml-engineer|mlops-engineer|software-engineering-lead" codex-subagent-designer/references/software-development-crew.md` should show lifecycle and routing coverage.
- `rg -n "data-science-workflows|analytics-engineering|ml-engineering|mlops-readiness|engineering-execution" codex-subagent-designer/references/software-development-crew.md` should show implemented skill coverage.

### Dependencies

- Blocked by: Phase 3
- Blocks: Phase 5

---

## Phase 5: Validation and Review

### Objective

Validate the new catalog assets and review routing clarity before execution is considered complete.

### Agents: `tester`, `code-reviewer`
### Parallel: No

### Files to Create

- None required. If useful, create a short repo-local validation note only when a command produces non-obvious results that should be preserved.

### Files to Modify

- None expected. Any corrections found during validation should be patched before the final review is closed.

### Implementation Details

Run a focused validation pass:

- TOML parseability for all files under `codex-subagent-designer/agents/examples/openai/`.
- Required-key checks for the five new TOML files.
- Skill-folder existence checks for every new skill referenced from TOML or registry text.
- Basic frontmatter checks for new `SKILL.md` files.
- Registry consistency checks for lifecycle, routing, intentional overlap, model coverage, and implemented-skill entries.

Then perform a findings-first review focused on:

- Whether each new agent has a distinct routing signal.
- Whether stop rules protect existing agent boundaries.
- Whether supporting skills are concise and reusable.
- Whether any new role should instead route to an existing agent.

### Validation

- `python3 - <<'PY' ... PY` using `tomllib` to parse all OpenAI TOML examples and assert required keys for the five new agents.
- `rg --files data-science-workflows analytics-engineering ml-engineering mlops-readiness engineering-execution` confirms all skill assets exist.
- `rg -n` consistency checks from Phase 4 pass.
- Optional installed-copy validation should be deferred unless the user explicitly asks to install under `~/.codex`.

### Dependencies

- Blocked by: Phase 4
- Blocks: None

---

## File Inventory

| # | File | Phase | Purpose |
|---|------|-------|---------|
| 1 | `data-science-workflows/SKILL.md` | 1 | Data science workflow skill. |
| 2 | `data-science-workflows/agents/openai.yaml` | 1 | Skill interface metadata. |
| 3 | `data-science-workflows/references/analysis-checklist.md` | 1 | Data science checklist. |
| 4 | `analytics-engineering/SKILL.md` | 1 | Analytics engineering workflow skill. |
| 5 | `analytics-engineering/agents/openai.yaml` | 1 | Skill interface metadata. |
| 6 | `analytics-engineering/references/metrics-contract-checklist.md` | 1 | Metrics contract checklist. |
| 7 | `ml-engineering/SKILL.md` | 2 | ML engineering workflow skill. |
| 8 | `ml-engineering/agents/openai.yaml` | 2 | Skill interface metadata. |
| 9 | `ml-engineering/references/model-delivery-checklist.md` | 2 | Model delivery checklist. |
| 10 | `mlops-readiness/SKILL.md` | 2 | MLOps readiness workflow skill. |
| 11 | `mlops-readiness/agents/openai.yaml` | 2 | Skill interface metadata. |
| 12 | `mlops-readiness/references/model-operations-checklist.md` | 2 | Model operations checklist. |
| 13 | `engineering-execution/SKILL.md` | 2 | Engineering execution workflow skill. |
| 14 | `engineering-execution/agents/openai.yaml` | 2 | Skill interface metadata. |
| 15 | `engineering-execution/references/delivery-coordination-checklist.md` | 2 | Delivery coordination checklist. |
| 16 | `codex-subagent-designer/agents/examples/openai/data-scientist.toml` | 3 | Data scientist agent template. |
| 17 | `codex-subagent-designer/agents/examples/openai/analytics-engineer.toml` | 3 | Analytics engineer agent template. |
| 18 | `codex-subagent-designer/agents/examples/openai/ml-engineer.toml` | 3 | ML engineer agent template. |
| 19 | `codex-subagent-designer/agents/examples/openai/mlops-engineer.toml` | 3 | MLOps engineer agent template. |
| 20 | `codex-subagent-designer/agents/examples/openai/software-engineering-lead.toml` | 3 | Software engineering lead agent template. |
| 21 | `codex-subagent-designer/references/software-development-crew.md` | 4 | Registry and routing synchronization. |

## Risk Classification

| Phase | Risk | Rationale |
|-------|------|-----------|
| 1 | LOW | Creates disjoint skill folders following established patterns. |
| 2 | LOW | Creates disjoint skill folders following established patterns; MLOps stop rules need care. |
| 3 | MEDIUM | Agent instructions must balance complete coverage with clear handoff boundaries. |
| 4 | MEDIUM | Single shared registry file has the highest drift and conflict risk. |
| 5 | LOW | Validation and review are read-mostly and reversible. |

## Resource Estimate

| Phase | Agent | Est. Files Read | Est. Files Written | Retry Risk | Notes |
|-------|-------|-----------------|--------------------|------------|-------|
| 1 | `technical-writer` | 3 | 6 | LOW | Follows existing skill templates. |
| 2 | `technical-writer` | 3 | 9 | LOW | Follows existing skill templates. |
| 3 | `prompt-engineer` | 8 | 5 | MEDIUM | Requires precise output contracts and stop rules. |
| 4 | `coder` | 8 | 1 | MEDIUM | Registry synchronization is the main shared edit. |
| 5 | `tester`, `code-reviewer` | 21 | 0 | LOW | Shell validation plus read-only review. |

## Execution Profile

```text
Execution Profile:
- Total phases: 5
- Parallelizable phases: 2 (in 1 batch: Phases 1 and 2)
- Sequential-only phases: 3
- Estimated parallel wall time: 4 stages
- Estimated sequential wall time: 5 stages

Note: Native subagents currently run without user approval gates.
All tool calls are auto-approved without user confirmation.
```
