---
name: ai-evals
description: Use when evaluating AI product behavior, prompts, retrieval, tool use, model settings, judge prompts, golden datasets, regression suites, safety behavior, refusal behavior, hallucination risk, or automated scoring for AI features.
---

# AI Evals

## Overview

Treat AI behavior as product behavior that needs examples, rubrics, regression checks, and interpretation. Do not tune prompts without knowing what success and failure mean.

## Workflow

1. Define behavior under test and failure modes.
2. Build a small high-signal dataset: happy path, edge cases, adversarial inputs, empty context, malformed input, and tool failure.
3. Define scoring: exact, rubric, human review, automated judge, or hybrid.
4. Run or specify eval procedure and thresholds.
5. Interpret results and identify overfitting or missing coverage.

Use `references/eval-case-template.md` for case design.

## Output Contract

Return exactly: `Behavior Under Test`, `Eval Design`, `Cases`, `Rubric`, `Commands Or Procedure`, `Results Interpretation`, `Risks`.

## Stop Conditions

Stop when expected behavior, labeled examples, safety requirements, or scoring criteria are unavailable for high-impact AI behavior.
