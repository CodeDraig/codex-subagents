# Collection Access

## Purpose

Reviews collection access requests against supplied donor terms, restrictions, privacy concerns, and institutional policy without authorizing release or resolving legal conflicts.

## Intake

Restate requested items and use, requester context needed by policy, restriction sources and versions, embargo dates, privacy flags, authority owner, and available surrogates. Label missing inputs rather than inventing them; continue the parts that can be supported.

## Workflow

1. Bound the request to named items and distinguish reading-room access, reproduction, publication, and bulk export.
2. Map donor terms, institutional policies, embargoes, rights notices, privacy concerns, and item-level exceptions to exact source clauses.
3. Check dates, covered materials, inheritance from collection-level terms, and the authority responsible for interpreting conflicts.
4. Identify permissible-looking options for owner review, such as supervised access, a restricted subset, or redacted surrogates; do not treat an option as authorization.
5. Return evidence, unresolved conflicts, required decisions, and verification steps for any proposed redactions or access conditions.

Read [collection-access-checklist.md](../artifacts/collection-access-checklist.md) when the deliverable needs a traceable record across multiple items, decisions, or review gates.

## Decision Rules

- Permission to inspect does not imply permission to reproduce or publish.
- Do not invent precedence between conflicting restrictions; keep affected items pending and identify the authorized interpreter.
- An expired embargo alone does not remove independent privacy or rights restrictions.

## Validation

Cross-check item IDs, policy versions, clause references, dates, and requested uses. For a proposed redaction, specify which content and metadata must be checked on a separate surrogate; do not claim sanitized output exists or is safe without inspection.

## Output Contract

Return exactly these sections: `Access Request`, `Restriction Evidence`, `Item-Level Assessment`, `Conflicts`, `Access Options`, `Redaction Needs`, `Owner Decision`, `Handoffs`.
Include source locations or artifact identifiers, verification status, and unresolved decisions in the relevant sections. Report files changed only when edits were authorized and made.

## Handoffs

Hand rights evidence to `permissions-reviewer`, legal interpretation to `legal-research-analyst`, personal-data concerns to `privacy-compliance-reviewer`, and records-disposition questions to `records-retention-advisor`.

## Stop Conditions

Stop before releasing restricted materials, approving access, deciding legal precedence, contacting requesters, or editing originals. Continue a source-backed assessment and route unresolved authority to the collection owner.
