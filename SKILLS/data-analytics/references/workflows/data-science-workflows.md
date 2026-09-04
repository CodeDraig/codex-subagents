# Data Science Workflows

## Purpose

This workflow helps turn a data question into a defensible analysis. Keep the focus on the question, the evidence actually reviewed, the method used, and the limits of the conclusion.

## Workflow

1. Restate the question, decision context, success metric, and the exact hypothesis or comparison being tested.
2. Identify the data sources, provenance, time window, unit of analysis, exclusions, and any missing, biased, or partially observed coverage.
3. Check whether the dataset or sample leaks target information, mixes train and test populations, or hides assignment and selection bias.
4. Choose the smallest method that answers the question: descriptive review, segmentation, statistical test, experiment readout, feature comparison, or sensitivity check.
5. Check uncertainty, effect size, baseline, confidence limits, and whether the result is practically meaningful or just statistically detectable.
6. Separate findings from caveats and recommend a decision only when the evidence supports it and the assumptions are explicit.

Read [analysis-checklist.md](../artifacts/analysis-checklist.md) when recording question framing, provenance, method choice, interpretation limits, and reproducibility.

## Output Contract

Return exactly these sections:

- `Question`
- `Data Reviewed`
- `Method`
- `Findings`
- `Caveats`
- `Recommended Decision`
- `Validation`
- `Reproducibility Notes`
- `Open Questions`

## Handoffs

Hand metric-definition or transformation changes to analytics engineering, schema or grain changes to data modeling, and decisions that depend on domain judgment to the named subject-matter owner.

## Stop Conditions

Stop when the question cannot be answered from the available data, the method would overclaim, the sample is too weak for a defensible conclusion, the dataset provenance is unclear, or the recommendation depends on assumptions that are not explicit.
