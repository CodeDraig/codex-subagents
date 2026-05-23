---
title: "Knowledge Work Subagent Groups Implementation Plan"
design_ref: "docs/maestro/plans/2026-05-20-knowledge-work-subagent-groups-design.md"
created: "2026-05-20T01:35:00-04:00"
status: "implemented"
total_phases: 5
estimated_files: 100
task_complexity: "large"
---

# Knowledge Work Subagent Groups Implementation Plan

## Plan Overview

- **Total phases**: 5
- **Agents involved**: `documentation-engineer`, `prompt-evaluation-engineer`, `implementation-finisher`, `code-reviewer`
- **Estimated effort**: Large catalog expansion completed in two passes. The first pass implemented Legal & Regulatory Operations; the follow-up pass implemented the remaining approved Academic & Research Support, Grants & Sponsored Projects, Finance & Accounting Operations, Procurement & Vendor Management, Policy & Public Affairs, and Publishing & Scholarly Production groups with agent TOMLs, supporting skills, and synchronized registry updates.

## Follow-Up Completion

After review, the original deferred backlog was promoted into active implementation. The completed follow-up scope added:

- 30 additional OpenAI TOML agent templates across the six remaining approved knowledge-work groups.
- 18 repo-local skill folders, each with `SKILL.md`, `agents/openai.yaml`, and a reference checklist.
- Registry lifecycle, routing, model coverage, intentional overlap, and implemented skill asset entries for every new group.
- An updated implementation record at `docs/maestro/plans/2026-05-20-knowledge-work-subagent-groups-backlog.md`.

The original phase plan below documents the first tranche and should be read as historical execution context, not remaining work.

## Dependency Graph

```text
Phase 1: Legal/regulatory skills
    |
    v
Phase 2: Legal/regulatory agent TOMLs
    |
    v
Phase 3: Registry synchronization
    |
    v
Phase 4: Implementation record for remaining groups
    |
    v
Phase 5: Validation and review
```

## Execution Strategy

| Stage | Phases | Execution | Agent Count | Notes |
|-------|--------|-----------|-------------|-------|
| 1 | Phase 1 | Sequential | 1 | Create shared skills first so TOML references resolve. |
| 2 | Phase 2 | Sequential | 1 | Create five high-stakes agent templates with strict stop rules. |
| 3 | Phase 3 | Sequential | 1 | Update the shared registry in one pass. |
| 4 | Phase 4 | Sequential | 1 | Preserve remaining groups first as backlog, then update the artifact to an implementation record after follow-up completion. |
| 5 | Phase 5 | Sequential | 1-2 | Parse, reference, and review checks. |

## Phase 1: Legal and Regulatory Skill Assets

### Objective

Create repo-local skills that support the first approved knowledge-work group: Legal & Regulatory Operations.

### Agent: `documentation-engineer`
### Parallel: No

### Files to Create

- `legal-research-workflows/SKILL.md` — Source-backed legal and regulatory research workflow with jurisdiction/source tracking, issue spotting, authority hierarchy, and counsel questions.
- `legal-research-workflows/agents/openai.yaml` — Skill interface metadata.
- `legal-research-workflows/references/source-authority-checklist.md` — Checklist for jurisdiction, source authority, currency, procedural posture, citations, and non-advice boundaries.
- `contract-review-operations/SKILL.md` — Contract clause review, obligation extraction, risk flagging, negotiation issue logs, and escalation boundaries.
- `contract-review-operations/agents/openai.yaml` — Skill interface metadata.
- `contract-review-operations/references/clause-review-checklist.md` — Checklist for parties, obligations, dates, renewal/termination, liability, confidentiality, data, IP, payment, acceptance, and unresolved counsel questions.
- `records-retention-operations/SKILL.md` — Retention schedule mapping, records inventory, disposition workflows, litigation-hold flags, and approval gates.
- `records-retention-operations/agents/openai.yaml` — Skill interface metadata.
- `records-retention-operations/references/retention-workflow-checklist.md` — Checklist for record classes, retention authority, jurisdiction, disposition, legal hold, privacy, audit trail, and approval gates.

### Files to Modify

- None.

### Implementation Details

Follow the established repo-local skill layout: frontmatter with `name` and `description`, concise heading, `Overview`, `Workflow`, reference pointer, `Output Contract`, and `Stop Conditions`.

Every skill must clearly say it does not provide legal advice. Stop conditions should require escalation when a task asks for legal conclusions, rights determinations, filing decisions, privilege advice, jurisdiction-specific advice, or action without counsel/authorized owner review.

### Validation

- `rg --files legal-research-workflows contract-review-operations records-retention-operations` lists the nine expected files.
- Each new `SKILL.md` has frontmatter, `## Output Contract`, and `## Stop Conditions`.

### Dependencies

- Blocked by: None
- Blocks: Phase 2

---

## Phase 2: Legal and Regulatory Agent Templates

### Objective

Create five OpenAI TOML agent examples for the Legal & Regulatory Operations group.

### Agent: `prompt-evaluation-engineer`
### Parallel: No

### Files to Create

- `codex-subagent-designer/agents/examples/openai/legal-research-analyst.toml` — Source-backed legal/regulatory research and issue-spotting analyst.
- `codex-subagent-designer/agents/examples/openai/contract-review-specialist.toml` — Contract clause, obligation, risk, and question extraction specialist.
- `codex-subagent-designer/agents/examples/openai/regulatory-monitor.toml` — Regulatory source monitoring, change tracking, effective-date tracking, and action-summary specialist.
- `codex-subagent-designer/agents/examples/openai/records-retention-advisor.toml` — Records inventory, retention schedule, disposition workflow, and hold-flag specialist.
- `codex-subagent-designer/agents/examples/openai/legal-ops-coordinator.toml` — Legal operations workflow coordinator for matter intake, task tracking, counsel questions, and evidence packaging.

### Files to Modify

- None.

### Implementation Details

Each TOML must follow the existing structure: `name`, `description`, `model`, `model_reasoning_effort`, `sandbox_mode`, `nickname_candidates`, and a triple-quoted `developer_instructions`.

Recommended model posture:

- Use `gpt-5.5` with `high` reasoning for `legal-research-analyst`, `contract-review-specialist`, and `regulatory-monitor`.
- Use `gpt-5.5` with `medium` reasoning for `records-retention-advisor` and `legal-ops-coordinator`.
- Use `read-only` unless a role is explicitly writing repo-local workflow artifacts; high-stakes legal/regulatory agents should not modify project files by default.

Each agent must:

- Invoke one or more of `$legal-research-workflows`, `$contract-review-operations`, and `$records-retention-operations`.
- Include a strong non-advice boundary.
- Require source citations or source inventory for claims.
- Include hard stops for legal advice, confidential/privileged material uncertainty, non-public records, filing decisions, rights determinations, or counsel-only judgment.
- Return exact output sections tailored to the role.

### Validation

- Parse all OpenAI TOML files with the same Python interpreter used for prior TOML validation, preferably `python3.11` if `python3` lacks `tomllib`.
- Assert required TOML keys exist for the five new agent files.
- Confirm every `$skill` reference resolves to a repo-local skill folder.

### Dependencies

- Blocked by: Phase 1
- Blocks: Phase 3

---

## Phase 3: Crew Registry Synchronization

### Objective

Update the canonical crew registry with Legal & Regulatory Operations coverage and keep skill references synchronized.

### Agent: `implementation-finisher`
### Parallel: No

### Files to Create

- None.

### Files to Modify

- `codex-subagent-designer/references/software-development-crew.md` — Add lifecycle, routing, model coverage, intentional overlap, and implemented skill asset entries for the new group.

### Implementation Details

Registry updates should include:

- Lifecycle row: `Legal & Regulatory Operations`.
- Routing rules for legal/regulatory research, contract review, regulatory monitoring, records retention, and legal ops coordination.
- Model coverage updates for the new `gpt-5.5` agents.
- Intentional overlap with existing `privacy-compliance-reviewer`, `public-records-researcher`, `source-verification-analyst`, procurement roles, and `standards-ethics-editor` where relevant.
- Implemented skill assets:
  - `$legal-research-workflows`: `legal-research-workflows/`
  - `$contract-review-operations`: `contract-review-operations/`
  - `$records-retention-operations`: `records-retention-operations/`

Keep `Remaining Skill Backlog` accurate and separate historical planning notes from missing active TOML skill references.

### Validation

- `rg -n "legal-research-analyst|contract-review-specialist|regulatory-monitor|records-retention-advisor|legal-ops-coordinator" codex-subagent-designer/references/software-development-crew.md`
- `rg -n "legal-research-workflows|contract-review-operations|records-retention-operations" codex-subagent-designer/references/software-development-crew.md`

### Dependencies

- Blocked by: Phase 2
- Blocks: Phase 4

---

## Phase 4: Knowledge-Work Implementation Record

### Objective

Preserve the remaining approved group recommendations, first as implementation backlog and then as an implementation record once TOML and skill files exist.

### Agent: `documentation-engineer`
### Parallel: No

### Files to Create

- `docs/maestro/plans/2026-05-20-knowledge-work-subagent-groups-backlog.md` — An implementation record listing Academic & Research Support, Grants & Sponsored Projects, Finance & Accounting Operations, Procurement & Vendor Management, Policy & Public Affairs, and Publishing & Scholarly Production with implemented agents and skills from the approved design.

### Files to Modify

- None, unless registry cross-references need to point to the implementation record. Add agent names to routing tables only after TOML files exist.

### Implementation Details

The implementation record should preserve:

- Implemented agent names.
- Implemented skill names.
- Priority order.
- Non-advice or source-quality boundaries.
- Implementation gating: each group is implemented as an agent-plus-skill tranche with registry sync and validation.

### Validation

- `sed -n '1,200p' docs/maestro/plans/2026-05-20-knowledge-work-subagent-groups-backlog.md` confirms all six completed groups are present.

### Dependencies

- Blocked by: Phase 3
- Blocks: Phase 5

---

## Phase 5: Validation and Review

### Objective

Validate the first knowledge-work group and review the catalog for routing clarity and safety boundaries.

### Agent: `code-reviewer`
### Parallel: No

### Files to Create

- None required.

### Files to Modify

- None expected. Patch any issues found before marking complete.

### Implementation Details

Run focused checks:

- TOML parseability for all files under `codex-subagent-designer/agents/examples/openai/`.
- Required-key checks for the five new Legal & Regulatory Operations TOMLs.
- `$skill` reference resolution for all TOML files.
- Skill frontmatter, output contract, and stop condition checks for the three new skills.
- Registry consistency for lifecycle, routing, model coverage, intentional overlap, and implemented skills.
- Findings-first review for legal-advice boundary, source requirements, and overlap with public-records, privacy, source-verification, and compliance roles.

### Validation

- `python3.11` TOML parse and required-key checks, or the repo-local current Python if it provides `tomllib`.
- `rg --files legal-research-workflows contract-review-operations records-retention-operations`
- `git diff --check`

### Dependencies

- Blocked by: Phase 4
- Blocks: None

---

## File Inventory

| # | File | Phase | Purpose |
|---|------|-------|---------|
| 1 | `legal-research-workflows/SKILL.md` | 1 | Legal/regulatory research skill. |
| 2 | `legal-research-workflows/agents/openai.yaml` | 1 | Skill interface metadata. |
| 3 | `legal-research-workflows/references/source-authority-checklist.md` | 1 | Source authority checklist. |
| 4 | `contract-review-operations/SKILL.md` | 1 | Contract review operations skill. |
| 5 | `contract-review-operations/agents/openai.yaml` | 1 | Skill interface metadata. |
| 6 | `contract-review-operations/references/clause-review-checklist.md` | 1 | Clause review checklist. |
| 7 | `records-retention-operations/SKILL.md` | 1 | Records retention operations skill. |
| 8 | `records-retention-operations/agents/openai.yaml` | 1 | Skill interface metadata. |
| 9 | `records-retention-operations/references/retention-workflow-checklist.md` | 1 | Retention workflow checklist. |
| 10 | `codex-subagent-designer/agents/examples/openai/legal-research-analyst.toml` | 2 | Legal research agent template. |
| 11 | `codex-subagent-designer/agents/examples/openai/contract-review-specialist.toml` | 2 | Contract review agent template. |
| 12 | `codex-subagent-designer/agents/examples/openai/regulatory-monitor.toml` | 2 | Regulatory monitoring agent template. |
| 13 | `codex-subagent-designer/agents/examples/openai/records-retention-advisor.toml` | 2 | Records retention agent template. |
| 14 | `codex-subagent-designer/agents/examples/openai/legal-ops-coordinator.toml` | 2 | Legal operations coordination agent template. |
| 15 | `codex-subagent-designer/references/software-development-crew.md` | 3 | Registry synchronization. |
| 16 | `docs/maestro/plans/2026-05-20-knowledge-work-subagent-groups-backlog.md` | 4 | Future group backlog. |

## Risk Classification

| Phase | Risk | Rationale |
|-------|------|-----------|
| 1 | MEDIUM | Legal/regulatory skills need precise non-advice stop rules. |
| 2 | HIGH | High-stakes TOML agents must not imply legal advice or action authority. |
| 3 | MEDIUM | Registry sync can create misleading routing if boundaries are vague. |
| 4 | LOW | Backlog artifact only; no active routing impact. |
| 5 | LOW | Validation and review are read-mostly. |

## Execution Profile

```text
Execution Profile:
- Total phases: 5
- Parallelizable phases: 0
- Sequential-only phases: 5
- Estimated parallel wall time: 5 stages
- Estimated sequential wall time: 5 stages

Note: This plan is intentionally sequential because each phase depends on prior skill, TOML, and registry decisions.
```
