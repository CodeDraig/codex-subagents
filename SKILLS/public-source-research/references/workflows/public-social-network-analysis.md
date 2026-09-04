# Public Social Network Analysis

## Purpose

Analyze observable public-platform behavior and coordination signals while preserving alternative explanations, reproducibility, and privacy boundaries.

## Workflow

1. Restate the research question, public accounts, hashtags, URLs, platforms, timeframe, collection method, intended use, and populations excluded from analysis.
2. Define a reproducible observation set with query terms, sampling window, platform-visible fields, missing-data limits, account and post counts, and any collection bias.
3. Map observable nodes and edges such as posts, reposts, replies, mentions, shared links, repeated phrases, posting cadence, amplification chains, cross-platform reuse, and public account-age signals.
4. Compare suspected coordination against plausible baselines: fandom, shared ideology, scheduled campaigns, platform affordances, common source material, bots acting independently, and breaking-news convergence.
5. Require multiple independent signal classes before assessing coordination. Separate behavioral coordination from identity, sponsorship, intent, authenticity, or centralized control.
6. Report aggregate patterns whenever individual identity is unnecessary, minimize quoted harmful content, preserve uncertainty, and specify further verification that would reduce false positives.

Read [public-network-analysis-checklist.md](../artifacts/public-network-analysis-checklist.md) when you need scope provenance, signal grading, alternative explanations, confidence, reproducibility, and privacy review.

## Decision Rules

- Treat a shared hashtag, URL, viewpoint, or posting window as weak evidence by itself.
- Treat repeated rare phrasing, unusually synchronized sequences, shared infrastructure, or consistent amplification roles as stronger only after checking common-source and platform explanations.
- Do not infer real identity, protected traits, employment, location, sponsorship, or intent from network position or pseudonymous behavior.
- Do not treat automation indicators as proof of malicious coordination; automation, coordination, and deception are separate findings.
- Treat missing, deleted, private, rate-limited, or algorithmically hidden content as unavailable, not as evidence supporting the preferred hypothesis.
- Prefer the least identifying representation that still answers the research question.

## Validation Guidance

- Record platform, query, collection window, timezone, visible fields, sample size, exclusions, API or manual method, and known coverage gaps.
- Preserve representative public URLs, post identifiers, timestamps, exports, or screenshots when lawful and necessary; avoid unnecessary copies of personal data.
- Recalculate key patterns with high-degree hubs, duplicates, reposts, and obvious scheduled accounts removed to test sensitivity.
- Compare cadence and content similarity against an appropriate baseline rather than using absolute thresholds without context.
- When raw timestamps or repeated orders are available, preregister the ordering or synchrony statistic, baseline, tie handling, and multiple-comparison treatment; otherwise keep the assessment qualitative and state the missing calibration.
- Mark coordination or attribution inconclusive when data provenance, denominator, platform coverage, or alternative explanations cannot be tested.

## Output Contract

Return exactly: `Scope`, `Observed Network`, `Coordination Signals`, `Alternative Explanations`, `Representative Evidence`, `Confidence`, `Privacy Limits`, `Recommended Verification`, `Handoffs`.

For each material signal, include observation window, public source or artifact, signal class, baseline comparison, alternative explanation, sensitivity check, confidence effect, and privacy treatment.

## Stop Conditions And Handoffs

Stop when asked to deanonymize users, infer protected traits, create harassment or employment target lists, expose private accounts, evade platform controls, or recommend persuasion or engagement tactics against identified people. For a mixed request, refuse the targeting portion and continue only the separable aggregate analysis.

Hand narrative and correction risk to `misinformation-risk-analyst`, claim corroboration to `source-verification-analyst`, broader lawful scope to `osint-research-lead`, and publication or platform-policy decisions to `standards-ethics-editor`.
