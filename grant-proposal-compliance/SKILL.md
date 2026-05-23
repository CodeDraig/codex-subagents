---
name: grant-proposal-compliance
description: Use when parsing grant solicitations, building compliance matrices, checking proposal requirements, or preparing sponsor-question logs.
---

# Grant Proposal Compliance

## Overview

Turn sponsor requirements into a traceable compliance matrix. Support proposal teams without making institutional submission, eligibility, legal, or budget authority decisions.

## Workflow

1. Restate sponsor, opportunity ID, deadline, program goals, eligibility, and submission channel.
2. Extract required sections, page limits, attachments, forms, certifications, formatting rules, and review criteria.
3. Build a compliance matrix with owner, evidence, status, and unresolved question fields.
4. Flag restricted, ambiguous, late-breaking, or institution-owned requirements.
5. Produce sponsor questions and handoffs for authorized officials.

Use `references/proposal-compliance-checklist.md` for solicitation parsing.

## Output Contract

Return exactly: `Opportunity Scope`, `Requirement Matrix`, `Eligibility Flags`, `Attachment Checklist`, `Review Criteria`, `Sponsor Questions`, `Owner Handoffs`.

## Stop Conditions

Stop when asked to submit proposals, certify compliance, decide eligibility without an authorized owner, bypass sponsor rules, fabricate institutional approvals, or provide legal advice.
