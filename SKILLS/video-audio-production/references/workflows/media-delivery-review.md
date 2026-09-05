# Media Delivery Review

## Purpose

Reviews video and audio delivery packages against supplied technical specifications, content versions, caption and transcript coverage, and approval evidence.

## Intake

Restate delivery manifest, target specifications and version, intended destinations, reference cut, actual exports, captions or transcripts, and review authority. Label missing inputs rather than inventing them; continue the parts that can be supported.

## Workflow

1. Inventory required versions, destinations, languages, exports, captions, transcripts, thumbnails, metadata, and accompanying approval evidence.
2. Compare actual files or supplied probe reports to the supplied codec, container, dimensions, frame rate, channels, sample rate, loudness, and naming requirements that apply.
3. Check exported content against the approved cut or script, noting missing segments, placeholders, obsolete versions, and continuity or sync problems.
4. Review caption and transcript coverage, timing, speaker labels, meaningful sounds, reading order, and important visual information needed by the audience.
5. Return pass, fail, or unverified status for each requirement, separating technical inspection from content approval and publication authority.

Read [media-delivery-review-checklist.md](../artifacts/media-delivery-review-checklist.md) when the deliverable needs a traceable record across multiple items, decisions, or review gates.

## Decision Rules

- A file extension alone does not establish codec or conformance.
- Spot-checking cannot support a full-program caption or content-completeness claim; disclose coverage.
- Do not invent a universal loudness or encoding target; compare against the actual destination specification.

## Validation

Record filename, version, duration, inspected time ranges, and evidence per requirement. Use supplied metadata reports or, when authorized and available, ffprobe and a media player; check caption cues against duration and sampled playback. Mark uninspected streams, missing specs, and untested destinations unverified.

## Output Contract

Return exactly these sections: `Delivery Scope`, `Specification Matrix`, `Content And Version Checks`, `Caption And Transcript Review`, `Technical Evidence`, `Blockers`, `Owner Approvals`, `Handoffs`.
Include source locations or artifact identifiers, verification status, and unresolved decisions in the relevant sections. Report files changed only when edits were authorized and made.

## Handoffs

Hand export or version corrections to `postproduction-coordinator`, script differences to `script-development-editor`, scope decisions to `production-brief-planner`, rights evidence to `permissions-reviewer`, and accessibility-policy interpretation to `accessibility-reviewer`.

## Stop Conditions

Stop before publishing, uploading, approving rights, modifying exports, or declaring delivery ready while required checks or approvals are missing. Missing media permits a checklist and evidence request, not a passed delivery review.
