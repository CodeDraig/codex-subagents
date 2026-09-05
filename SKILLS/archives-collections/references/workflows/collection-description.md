# Collection Description

## Purpose

Creates hierarchical collection descriptions, finding-aid drafts, and terminology decisions from supplied inventories while preserving provenance and original-order evidence.

## Intake

Restate collection identifier, creator context, existing hierarchy, inventory, description conventions if supplied, languages, access restrictions, and output format. Label missing inputs rather than inventing them; continue the parts that can be supported.

## Workflow

1. Inspect existing collection, series, file, and item relationships and distinguish observed arrangement from proposed intellectual organization.
2. Draft descriptions at the appropriate level with scope, content, dates, extent, creator context, and language grounded in inventory evidence.
3. Preserve inherited context without assigning unsupported item-level details; identify gaps, mixed provenance, and uncertain dates.
4. Record supplied titles separately from devised titles, identify descriptive language changes, and retain historical wording as attributed evidence when relevant.
5. Return a finding-aid draft and cross-reference checks; propose rearrangement separately from any physical or digital moves.

Read [collection-description-checklist.md](../artifacts/collection-description-checklist.md) when the deliverable needs a traceable record across multiple items, decisions, or review gates.

## Decision Rules

- Do not infer item contents from a folder title alone.
- Preserve uncertainty in dates and creators; do not manufacture exact ranges or authority identifiers.
- Keep changes to harmful or obsolete descriptive language traceable rather than silently altering quoted source titles.

## Validation

Check parent-child relationships, unique identifiers, cross-references, date consistency, and extent units against the source inventory. If an export schema is supplied, validate against that version; otherwise label output as a descriptive draft, not standards-certified.

## Output Contract

Return exactly these sections: `Collection Context`, `Hierarchy`, `Description Draft`, `Terminology Decisions`, `Source Evidence`, `Unresolved Description`, `Validation`, `Files Changed`, `Handoffs`.
Include source locations or artifact identifiers, verification status, and unresolved decisions in the relevant sections. Report files changed only when edits were authorized and made.

## Handoffs

Hand provenance gaps to `accession-intake-coordinator`, access wording to `collection-access-reviewer`, preservation matters to `digital-preservation-planner`, and public interpretation to `exhibit-interpretation-writer`.

## Stop Conditions

Stop before moving or renaming originals, inventing authority records, asserting uninspected contents, or exposing restricted description. Missing inventory permits a partial hierarchy with unknowns.
