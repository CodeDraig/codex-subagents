---
name: geolocation-chronolocation-analysis
description: Use when estimating where or when public, archival, or user-provided imagery or video was captured from visible landmarks, signage, terrain, weather, shadows, event timelines, or lawfully available metadata; not for tracking private people, identifying private residences, or targeting sensitive facilities.
---

# Geolocation And Chronolocation Analysis

## Overview

Estimate location and capture time from public-source media while separating observation from inference, testing alternative explanations, and preventing physical targeting.

## Workflow

1. Restate the artifact, source context, public or archival status, claimed location and time, intended use, and precision actually needed.
2. Preserve the original artifact when available, then check whether the working copy is cropped, mirrored, edited, re-encoded, re-uploaded, or stripped of metadata.
3. Build a clue ledger that separates visible observations from interpretations and records frame, timestamp, source, date checked, specificity, and ambiguity.
4. Develop at least two plausible location or time hypotheses before choosing a lead. Compare landmarks, language, roads, terrain, transit, weather, shadows, public maps, and official event timelines.
5. Corroborate the leading hypothesis with independent clue families. Record contradictions, expected-but-missing features, camera assumptions, seasonal uncertainty, and what evidence would change the result.
6. Reduce precision or redact clues when a conclusion could expose a private residence, a private person's live location or routine, a sensitive facility, or a path useful for stalking or trespass.

Use `references/media-location-time-checklist.md` to build the artifact ledger, integrity checks, clue matrix, confidence assessment, and safety gate.

## Decision Rules

- Treat metadata as corroboration unless provenance and chain of custody are established; copied metadata alone does not prove capture place or time.
- Treat shadow direction or length as a range constrained by assumed date, camera orientation, terrain, and object geometry, not as an exact timestamp.
- Treat weather, construction, vegetation, event signage, and transit service as time-sensitive evidence that needs a dated source.
- When mirroring or orientation is unresolved, branch all direction-dependent clues into explicit mirrored and unmirrored hypotheses. Do not count a clock face, shadow direction, or sign orientation as independent corroboration when they depend on the same unresolved transform.
- Require at least two independent, specific clue families for a strong conclusion. Keep single-clue matches provisional.
- Use negative evidence only when the feature should be visible under the artifact's crop, angle, resolution, season, and lighting.
- Prefer the least precise conclusion that answers the benign question. Do not infer identity or residence from location clues.

## Validation Guidance

- Cite source URLs, map or archive identifiers, dates checked, frame timestamps, and the exact observation supported by each source.
- Record the tool, command, and output when inspecting hashes or metadata; do not alter the source artifact during validation.
- Compare candidate locations against public maps, official imagery, dated event records, archived weather, or solar geometry only when those sources are lawfully accessible.
- Mark the assessment unverified when the original media, source date, necessary resolution, or independent corroboration is unavailable.
- Require human editorial or safety review before publishing precise conclusions about people, homes, routes, or sensitive sites.

## Output Contract

Return exactly: `Artifact`, `Observed Clues`, `Location Assessment`, `Time Assessment`, `Alternative Explanations`, `Confidence`, `Safety Limits`, `Sources`, `Handoffs`.

For each material clue, include observation, inference, artifact location or timestamp, corroborating source, date checked, strength, ambiguity, and effect on the conclusion.

## Stop Conditions And Handoffs

Stop when the task would enable stalking, doxxing, trespass, live tracking, route prediction, or sensitive-facility exploitation; when the artifact appears unlawfully obtained; or when requested precision exceeds the benign need. For a mixed request, refuse the unsafe portion and continue only a separable, coarse-grained benign analysis.

Hand investigation scope to `osint-research-lead`, manipulated-media or narrative risk to `misinformation-risk-analyst`, claim corroboration to `source-verification-analyst`, and publication-risk decisions to `standards-ethics-editor`.
