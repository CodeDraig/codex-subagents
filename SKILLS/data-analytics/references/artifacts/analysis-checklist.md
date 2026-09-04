# Analysis Checklist

## Question Framing

- State the decision or hypothesis.
- Define the population, unit of analysis, and time window.
- Note the baseline, comparator, or experiment variant.
- Record the expected decision threshold or practical significance rule.

## Data Review

- List sources and filters used.
- Check missingness, duplicates, outliers, and coverage gaps.
- Call out joins, leakage risks, and known biases.
- State provenance, sampling method, and any manual exclusions.

## Method Checks

- Match the method to the question.
- Confirm sample size and variance are adequate.
- Verify assumptions for any statistical test or model summary.
- Prefer the least complex method that answers the question defensibly.

## Interpretation

- Report effect size, direction, and uncertainty.
- Separate correlation from causation.
- Note sensitivity to segmentation, thresholds, and exclusions.
- Distinguish statistically detectable effects from decision-relevant effects.

## Reproducibility

- Record query, notebook, or code path.
- Capture parameters, date range, and dataset version.
- Flag any manual cleaning or untracked judgment calls.
- Include artifact hashes, seed values, or rerun instructions when available.
