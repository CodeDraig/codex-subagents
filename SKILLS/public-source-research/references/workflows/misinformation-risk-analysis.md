# Misinformation Risk Analysis

## Purpose

Assess a public claim's evidence, provenance, narrative path, and correction needs without amplifying the harmful framing or overstating certainty.

## Workflow

1. Restate the claim in the minimum detail needed for analysis, the affected audience, the public-interest reason, the decision needed, and the harm caused by repetition.
2. Build a provenance timeline from the earliest accessible appearance through major amplifiers, edits, re-uploads, official statements, corrections, and later contradictory evidence.
3. Inspect attached media for cropping, splicing, relabeling, old footage, synthetic or altered elements, missing context, and mismatches between the artifact and its caption.
4. Classify the claim as false, misleading, unverified, out of context, satire, manipulated media, coordinated influence, ordinary error, or a documented mixture. Keep classification separate from intent or attribution.
5. Assess amplification risk from reach, novelty, vulnerable audiences, real-world harm, platform migration, correction visibility, and whether rebuttal would repeat the claim unnecessarily.
6. Recommend a correction that leads with verified context, cites primary evidence, uses proportional detail, identifies remaining uncertainty, and avoids a reusable false-claim headline or slogan.

Read [misinformation-assessment-matrix.md](../artifacts/misinformation-assessment-matrix.md) when you need classification, narrative-path evidence, amplification severity, and correction selection.

## Decision Rules

- Treat the earliest accessible post as a provenance lead, not proof of origin, authorship, or coordination.
- Do not infer coordination from virality, shared ideology, common hashtags, or simultaneous reaction to breaking news alone.
- Do not classify a claim as false only because officials have not confirmed it. Distinguish absent evidence, contrary evidence, and unavailable evidence.
- Distinguish authentic satire from deceptive recirculation after labels or context are removed.
- Separate claim accuracy, media authenticity, narrative framing, distribution behavior, and speaker intent; they may require different assessments.
- Match the correction to demonstrated harm and audience exposure. Sometimes a quiet record correction is safer than a prominent rebuttal.

## Validation Guidance

- Prefer original media, primary documents, official statements, archived copies, direct transcripts, and independent corroboration; record URLs, timestamps, versions, and access dates.
- Quote only the minimum false or harmful wording required to identify the claim. Paraphrase when verbatim repetition would create a shareable artifact.
- Record what evidence would change the classification and mark unresolved provenance, intent, or coordination separately.
- Define the case-specific reach, harm, audience, velocity, and correction-status signals used for amplification severity. Reassess at stated times; do not downgrade risk merely because a correction was published.
- Treat automated manipulation detectors, similarity tools, and platform metrics as leads that require human review and source context.
- Keep the assessment provisional when the original artifact, relevant context, or independent evidence cannot be obtained lawfully.

## Output Contract

Return exactly: `Claim`, `Narrative Path`, `Evidence`, `Assessment`, `Amplification Risk`, `Correction Guidance`, `Uncertainty`, `Sources`, `Handoffs`.

For each material evidence item, include source class, source or artifact location, date checked, claim supported or contradicted, provenance limits, confidence, and amplification implications.

## Stop Conditions And Handoffs

Stop when asked to fabricate deceptive content, optimize persuasion for a false claim, target vulnerable groups, harass alleged amplifiers, expose private people, or make a harmful attribution without adequate evidence.

Hand claim-level corroboration to `source-verification-analyst`, public-network patterns to `social-network-analyst`, media location or timing to `geolocation-chronolocation-analyst`, and publication-risk decisions to `standards-ethics-editor` or `news-fact-checker`.
