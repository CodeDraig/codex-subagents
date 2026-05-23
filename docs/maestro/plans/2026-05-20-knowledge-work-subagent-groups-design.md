---
title: "Knowledge Work Subagent Group Recommendations"
created: "2026-05-20T01:22:32-04:00"
status: "approved"
authors: ["TechLead", "User"]
type: "design"
design_depth: "quick"
task_complexity: "medium"
---

# Knowledge Work Subagent Group Recommendations

## Problem Statement

The `codex-subagents` catalog already covers software delivery, OSINT, technical support, newsroom workflows, and a complementary data/analytics/ML crew. The next useful expansion should avoid duplicating those groups and instead add knowledge-work domains where subagent outputs can be operational, evidence-backed, and reviewable.

The requested recommendation should prioritize groups whose artifacts have clear source inputs, checklists, stop rules, and handoff boundaries. The goal is not to create general advice agents. The goal is to identify additional reusable subagent groups that can produce concrete work products such as research matrices, compliance checklists, budget reviews, policy summaries, vendor comparisons, publication workflows, and counsel-facing questions.

## Recommendation

Prioritize these groups:

1. **Legal & Regulatory Operations**
   - Candidate agents: `legal-research-analyst`, `contract-review-specialist`, `regulatory-monitor`, `records-retention-advisor`, `legal-ops-coordinator`.
   - Best fit because outputs can be source-backed and bounded by strong stop rules.
   - Boundary: issue spotting, source-backed summaries, clause checklists, filing or records workflows, and counsel questions. Never practice law or provide legal advice.

2. **Academic & Research Support**
   - Candidate agents: `literature-reviewer`, `research-methods-reviewer`, `citation-integrity-checker`, `research-data-curator`, `peer-review-prep-editor`.
   - Best fit for citation discipline, methodology review, and evidence-backed synthesis.
   - Boundary: research synthesis and methodology critique, not fabricating claims or replacing domain experts.

3. **Grants & Sponsored Projects**
   - Candidate agents: `grant-opportunity-scout`, `proposal-compliance-reviewer`, `budget-justification-writer`, `sponsored-projects-coordinator`, `grant-reporting-specialist`.
   - Strong fit because outputs map to solicitations, deadlines, budgets, compliance matrices, and reporting requirements.
   - Boundary: proposal assembly and compliance review. Finance, legal, or institutional officials own restricted budget, legal, or submission decisions.

4. **Finance & Accounting Operations**
   - Candidate agents: `financial-model-reviewer`, `accounting-controls-reviewer`, `invoice-reconciliation-specialist`, `audit-evidence-organizer`, `budget-variance-analyst`.
   - Useful for operational workflows with clear artifacts, but requires tight advice boundaries.
   - Boundary: reconciliation, controls, variance analysis, audit evidence organization, and model-assumption review. No tax, legal, investment, or regulated financial advice.

5. **Procurement & Vendor Management**
   - Candidate agents: `rfp-response-analyst`, `vendor-risk-reviewer`, `procurement-compliance-specialist`, `sow-reviewer`, `vendor-scorecard-analyst`.
   - Good practical operations group with clear source documents and comparison artifacts.
   - Boundary: RFP matrices, vendor comparisons, SOW checklists, risk summaries, and procurement workflow support. Specialist legal, privacy, security, or finance agents handle their slices.

6. **Policy & Public Affairs**
   - Candidate agents: `policy-analyst`, `public-comment-drafter`, `stakeholder-map-analyst`, `legislative-tracker`, `impact-assessment-writer`.
   - Strong fit for source-backed policy analysis and public comment drafting.
   - Boundary: summarize policy, trace source claims, draft public-facing artifacts, and identify stakeholder implications. Avoid unsourced persuasion and political microtargeting.

7. **Publishing & Scholarly Production**
   - Candidate agents: `developmental-manuscript-editor`, `production-editor`, `permissions-reviewer`, `indexing-coordinator`, `journal-submission-specialist`.
   - Useful as a non-newsroom editorial group for books, reports, journals, institutional publications, and scholarly workflows.
   - Boundary: publication workflow, style, permissions tracking, indexing coordination, and submission packages. Existing newsroom agents continue to own breaking-news and newsroom standards work.

## Recommended Skill Assets

Implement relevant skills alongside any new agent group. Each skill should be a repo-local folder with `SKILL.md`, `agents/openai.yaml`, and at least one focused reference checklist. Skills should carry the reusable workflow, source-quality expectations, stop conditions, and output contract so the TOML agents can stay focused on role behavior and handoff boundaries.

Recommended skill assets by group:

1. **Legal & Regulatory Operations**
   - `$legal-research-workflows`: source-backed legal and regulatory research, jurisdiction/source tracking, issue spotting, authority hierarchy, and counsel questions.
   - `$contract-review-operations`: clause checklist review, obligation extraction, risk flagging, negotiation issue logs, and escalation boundaries.
   - `$records-retention-operations`: retention schedule mapping, records inventory, disposition workflows, litigation-hold flags, and approval gates.

2. **Academic & Research Support**
   - `$academic-literature-review`: search strategy, inclusion/exclusion criteria, source quality, synthesis matrices, disagreement tracking, and citation discipline.
   - `$research-methods-review`: methodology critique, sampling, validity, limitations, reproducibility, ethics flags, and reviewer questions.
   - `$citation-integrity-review`: citation verification, claim-source alignment, bibliographic consistency, and missing-source flags.

3. **Grants & Sponsored Projects**
   - `$grant-proposal-compliance`: solicitation parsing, compliance matrices, required attachments, deadline checks, eligibility constraints, and submission-readiness gates.
   - `$sponsored-projects-reporting`: reporting calendars, deliverable tracking, funder requirements, evidence collection, and closeout workflows.
   - `$grant-budget-justification`: budget narrative alignment, allowable-cost checks, personnel/equipment/travel justification structure, and finance handoff questions.

4. **Finance & Accounting Operations**
   - `$finance-operations-review`: budget variance analysis, forecast assumption review, reconciliation checks, and operational finance caveats.
   - `$audit-evidence-management`: control evidence inventory, audit request tracking, evidence sufficiency checks, and reviewer-ready packaging.
   - `$invoice-reconciliation-workflows`: purchase order, invoice, receipt, approval, and exception reconciliation workflows.

5. **Procurement & Vendor Management**
   - `$procurement-vendor-review`: vendor comparison matrices, evaluation criteria, source-document tracking, scorecards, and decision caveats.
   - `$rfp-response-workflows`: RFP requirement extraction, response compliance, answer ownership, deadline tracking, and submission package checks.
   - `$sow-review-workflows`: scope, deliverables, acceptance criteria, dependencies, assumptions, change control, and specialist handoff flags.

6. **Policy & Public Affairs**
   - `$policy-analysis-workflows`: policy source review, stakeholder impact mapping, implementation implications, uncertainty, and evidence-backed summaries.
   - `$public-comment-drafting`: docket/source tracking, comment structure, claim support, affected-stakeholder framing, and non-deceptive advocacy boundaries.
   - `$legislative-tracking`: bill/regulation status tracking, amendment comparison, source provenance, effective dates, and monitoring cadence.

7. **Publishing & Scholarly Production**
   - `$publishing-production-workflows`: manuscript-to-publication workflow, style sheets, production schedules, proof cycles, and handoff tracking.
   - `$permissions-rights-review`: third-party material inventory, permission status, rights-holder tracking, license constraints, and escalation flags.
   - `$journal-submission-workflows`: author guidelines, submission package readiness, cover letter/checklist support, revision response tracking, and publication ethics flags.

Skill implementation can be phased. A first implementation pass should create skills only for the first approved group, then keep `software-development-crew.md` synchronized so no TOML references a missing skill.

## Deferred Groups

Defer these until the catalog has stronger artifact definitions for them:

- HR and people operations.
- General education and tutoring.
- Strategy consulting.
- Fundraising and donor relations.
- Creative production.
- Community management.

These groups may be useful later, but they are more likely to become generic advice roles unless the agent contracts define concrete inputs, outputs, validation checks, and stop conditions.

## Recommended Implementation Order

1. Legal & Regulatory Operations.
2. Academic & Research Support.
3. Grants & Sponsored Projects.
4. Finance & Accounting Operations.
5. Procurement & Vendor Management.
6. Policy & Public Affairs.
7. Publishing & Scholarly Production.

## Success Criteria

- Each implemented group has a lifecycle-map row or clearly documented placement in `software-development-crew.md`.
- Every new agent has a distinct routing signal, handoff boundaries, stop rules, and exact output sections.
- Any new skill references have matching repo-local skill folders with `SKILL.md`, `agents/openai.yaml`, and reference checklists before the registry claims "Remaining Skill Backlog: None."
- Agent TOML instructions reference the relevant group skills rather than duplicating full workflow methodology inline.
- High-stakes groups include explicit non-advice boundaries and escalation language.
- The implementation preserves existing OSINT, newsroom, technical support, software, and data/analytics/ML role ownership.
