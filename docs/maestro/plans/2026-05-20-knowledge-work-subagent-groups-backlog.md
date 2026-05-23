---
title: "Knowledge Work Subagent Groups Backlog"
source_design: "docs/maestro/plans/2026-05-20-knowledge-work-subagent-groups-design.md"
created: "2026-05-22T00:00:00-04:00"
status: "implemented"
---

# Knowledge Work Subagent Groups Implementation Record

This record preserves the approved knowledge-work group recommendations that were implemented after the first Legal & Regulatory Operations tranche. The groups below now have TOML agent templates, repo-local skill folders, and synchronized entries in `codex-subagent-designer/references/software-development-crew.md`.

## Implementation Rule

Each group was implemented as an agent-plus-skill tranche:

1. Create repo-local skills first.
2. Create TOML agent templates that reference only existing skills.
3. Synchronize `codex-subagent-designer/references/software-development-crew.md`.
4. Validate TOML parseability, skill reference resolution, registry routing, and boundary language.

## 1. Academic & Research Support

Implemented agents:

- `literature-reviewer`
- `research-methods-reviewer`
- `citation-integrity-checker`
- `research-data-curator`
- `peer-review-prep-editor`

Implemented skills:

- `$academic-literature-review`
- `$research-methods-review`
- `$citation-integrity-review`

Boundary: research synthesis, citation integrity, methodology critique, and reproducibility support. Do not fabricate claims, hide uncertainty, or replace domain expert review.

## 2. Grants & Sponsored Projects

Implemented agents:

- `grant-opportunity-scout`
- `proposal-compliance-reviewer`
- `budget-justification-writer`
- `sponsored-projects-coordinator`
- `grant-reporting-specialist`

Implemented skills:

- `$grant-proposal-compliance`
- `$sponsored-projects-reporting`
- `$grant-budget-justification`

Boundary: solicitation parsing, compliance matrices, reporting calendars, and budget narrative support. Finance, legal, or institutional officials own restricted budget, legal, or submission decisions.

## 3. Finance & Accounting Operations

Implemented agents:

- `financial-model-reviewer`
- `accounting-controls-reviewer`
- `invoice-reconciliation-specialist`
- `audit-evidence-organizer`
- `budget-variance-analyst`

Implemented skills:

- `$finance-operations-review`
- `$audit-evidence-management`
- `$invoice-reconciliation-workflows`

Boundary: operational finance review, reconciliation, control evidence, and model-assumption checks. No tax, legal, investment, or regulated financial advice.

## 4. Procurement & Vendor Management

Implemented agents:

- `rfp-response-analyst`
- `vendor-risk-reviewer`
- `procurement-compliance-specialist`
- `sow-reviewer`
- `vendor-scorecard-analyst`

Implemented skills:

- `$procurement-vendor-review`
- `$rfp-response-workflows`
- `$sow-review-workflows`

Boundary: RFP matrices, vendor comparisons, SOW checklists, scorecards, and procurement workflow support. Legal, privacy, security, and finance specialists own their slices.

## 5. Policy & Public Affairs

Implemented agents:

- `policy-analyst`
- `public-comment-drafter`
- `stakeholder-map-analyst`
- `legislative-tracker`
- `impact-assessment-writer`

Implemented skills:

- `$policy-analysis-workflows`
- `$public-comment-drafting`
- `$legislative-tracking`

Boundary: source-backed policy analysis, stakeholder impact mapping, public comment structure, and monitoring. Avoid unsourced persuasion and political microtargeting.

## 6. Publishing & Scholarly Production

Implemented agents:

- `developmental-manuscript-editor`
- `production-editor`
- `permissions-reviewer`
- `indexing-coordinator`
- `journal-submission-specialist`

Implemented skills:

- `$publishing-production-workflows`
- `$permissions-rights-review`
- `$journal-submission-workflows`

Boundary: manuscript workflow, production schedules, style sheets, permissions tracking, indexing coordination, and submission packages. Existing newsroom agents continue to own breaking-news and newsroom standards work.
