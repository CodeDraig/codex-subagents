---
name: data-science-workflows
description: Use when framing exploratory analysis, statistical questions, experiment interpretation, feature analysis, uncertainty, caveats, or evidence-backed recommendations.
---

# Data Science Workflows

## Overview

Use this skill to turn a data question into a defensible analysis. Keep the focus on the question, the evidence actually reviewed, the method used, and the limits of the conclusion.

## Workflow

1. Restate the question, decision context, and success metric.
2. Identify the data sources, time window, exclusions, and any missing or biased coverage.
3. Choose the smallest method that answers the question: descriptive review, segmentation, statistical test, experiment readout, or feature comparison.
4. Check uncertainty, effect size, sensitivity, and whether the result is practically meaningful.
5. Separate findings from caveats and recommend a decision only when the evidence supports it.

Use `references/analysis-checklist.md` for analysis checks.

## Output Contract

Return exactly these sections:

- `Question`
- `Data Reviewed`
- `Method`
- `Findings`
- `Caveats`
- `Recommended Decision`
- `Validation`

## Stop Conditions

Stop when the question cannot be answered from the available data, the method would overclaim, the sample is too weak for a defensible conclusion, or the recommendation depends on assumptions that are not explicit.
