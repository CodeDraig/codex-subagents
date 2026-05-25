---
name: grant-proposal-compliance
description: Use when parsing grant solicitations, building compliance matrices, checking proposal requirements, or preparing sponsor-question logs before submission.
---

# Grant Proposal Compliance

## Overview

Turn sponsor requirements into a traceable compliance matrix. Support proposal teams without making institutional submission, eligibility, legal, or budget authority decisions.

## Workflow

1. Restate sponsor, opportunity ID, deadline, program goals, eligibility, submission channel, amendment history, and any known institutional routing rule.
2. Extract required sections, page limits, attachments, forms, certifications, formatting rules, review criteria, and any portal-specific or file-naming constraints.
3. Build a compliance matrix with requirement, owner, evidence, status, and unresolved question fields, then tie budget sections to the narrative and sponsor instructions.
4. Flag submission blockers, late-breaking changes, ambiguous requirements, institution-owned certifications, and anything that must go to sponsored-programs, legal, or an authorized signer.
5. Produce sponsor questions, a readiness check, and handoffs that separate draft support from final submission authority.

Use `references/proposal-compliance-checklist.md` for solicitation parsing.

## Output Contract

Return exactly: `Opportunity Scope`, `Requirement Matrix`, `Eligibility Flags`, `Attachment Checklist`, `Review Criteria`, `Submission Blockers`, `Sponsor Questions`, `Owner Handoffs`.

## Stop Conditions

Stop when asked to submit proposals, certify compliance, decide eligibility without an authorized owner, bypass sponsor rules, fabricate institutional approvals, or provide legal advice.
