# Performance Profiling

## Purpose

Measure before optimizing. A useful profiling pass names the metric, baseline, reproduction, evidence, hypothesis, and acceptance threshold.

## Workflow

1. Define metric and user or system impact.
2. Reproduce with controlled inputs and environment notes.
3. Capture evidence: profiles, traces, logs, query plans, bundle analysis, screenshots, or benchmark output.
4. Rank hypotheses and isolate bottlenecks.
5. Recommend experiments or fixes with acceptance thresholds.

Read [measurement-plan.md](../artifacts/measurement-plan.md) when designing benchmarks.

## Output Contract

Return exactly: `Metric`, `Baseline Evidence`, `Reproduction`, `Hypotheses`, `Likely Bottlenecks`, `Recommended Experiments`, `Acceptance Threshold`, `Risks`.

## Handoffs

Hand optimization experiments to the owning implementation role and benchmark or regression coverage to the test owner; keep acceptance tied to the measured baseline and threshold.

## Stop Conditions

Stop when measurements are absent, non-reproducible, confounded, or not tied to a user or operational outcome.
