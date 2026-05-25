---
name: research-methods-review
description: Use when reviewing study design, methodology, sampling, measurement, validity, reproducibility, ethics boundaries, or analysis plans for research workflows; not for certifying validity or replacing statistician, IRB, or sponsor review.
---

# Research Methods Review

## Overview

Review research methods for clarity, validity, reproducibility, and fit to the stated question. Provide critique and owner questions without claiming final expert approval.

## Workflow

1. Restate the research question, design, population, data sources, measures, and analysis plan.
2. Check sampling frame, selection bias, controls, randomization or matching, measurement validity, missing data, confounders, and outcome definitions.
3. Assess reproducibility artifacts such as protocols, code, preregistration, data dictionaries, transformations, seeds, and versioning.
4. Separate fatal blockers from fixable clarity issues, then identify method limitations, alternative explanations, and needed expert review.
5. Produce an actionable critique with severity, evidence, and open questions.

Use `references/methods-review-checklist.md` for review coverage.

## Decision Rules

- Causal claims need a design that supports them; otherwise label the result as associational, exploratory, or hypothesis-generating.
- Convenience samples, uncontrolled designs, unblinded measurement, post-hoc outcome changes, and weak comparison groups reduce confidence materially.
- Missing data, measurement drift, undocumented transformations, or unverifiable code/versioning must be surfaced as validity risks.
- If ethics, consent, privacy, data-use, or preregistration requirements are missing where expected, stop and escalate rather than certifying the study.

## Output Contract

Return exactly: `Study Context`, `Method Summary`, `Validity Risks`, `Reproducibility Checks`, `Analysis Concerns`, `Open Questions`, `Recommended Fixes`.
Include the severity of each issue and the evidence used to reach it.

## Stop Conditions

Stop when asked to certify a study as valid, fabricate methods or results, ignore ethics or consent issues, or replace domain expert, IRB, statistician, or sponsor review.
