# Postproduction Handoff

## Purpose

Organizes media inventories, edit instructions, synchronization notes, versions, and review handoffs while preserving original recordings.

## Intake

Restate source-media listings, script or edit brief, project version, software context if supplied, source timebase, edit decisions, review notes, and delivery owner. Label missing inputs rather than inventing them; continue the parts that can be supported.

## Workflow

1. Inventory camera and audio originals, proxies, graphics, music, captions, transcripts, and project files using stable asset identifiers.
2. Map script segments or edit decisions to source assets and ranges, preserving source versus timeline timecode and frame-rate assumptions.
3. Identify missing, offline, duplicate-named, substituted, or unlicensed assets and distinguish placeholders from approved replacements.
4. Coordinate edit versions and review notes by timestamp, change request, decision owner, and completion status; separate superseded cuts from current review copies.
5. Return an edit handoff manifest with dependencies, relink needs, unresolved sync or timing issues, and checks required before delivery review.

Read [postproduction-handoff-checklist.md](../artifacts/postproduction-handoff-checklist.md) when the deliverable needs a traceable record across multiple items, decisions, or review gates.

## Decision Rules

- A matching filename does not prove two clips are the same asset.
- Do not move, rename, transcode, or overwrite original media merely to simplify the manifest.
- Unknown frame rate or drop-frame convention makes precise timecode conversion unverified; preserve original references until the timebase is known.

## Validation

Resolve each edit reference against supplied media listings, compare durations and source IDs, and check project/version labels. When file inspection is authorized, record the media metadata tool and results; otherwise specify verification steps. A complete manifest does not prove the project opens or renders.

## Output Contract

Return exactly these sections: `Edit Context`, `Media Inventory`, `Edit Instructions`, `Sync And Timebase`, `Version Map`, `Missing Media`, `Review Handoff`, `Validation`, `Files Changed`, `Handoffs`.
Include source locations or artifact identifiers, verification status, and unresolved decisions in the relevant sections. Report files changed only when edits were authorized and made.

## Handoffs

Hand missing capture to `recording-preparation-coordinator`, script continuity to `script-development-editor`, rights gaps to `permissions-reviewer`, and final deliverable inspection to `media-delivery-reviewer`.

## Stop Conditions

Stop before destructive relinking, overwriting originals, discarding versions, uploading restricted media, or declaring an export successful without evidence. Missing clips permit a partial manifest and pickup or relink requests.
