# Performance Profiling

## Purpose

Measure before optimizing. A useful profiling pass names the metric, baseline, reproduction, evidence, hypothesis, and acceptance threshold.

## Workflow

1. Define metric and user or system impact.
2. If measurements are absent, non-reproducible, or confounded, design the measurement procedure first: controlled inputs, environment, warmup, repetitions, instrumentation, and commands or manual steps. Return this plan when execution is unavailable or outside scope; missing measurements do not block planning.
3. When execution is authorized and available, reproduce with controlled inputs and capture evidence: profiles, traces, logs, query plans, bundle analysis, screenshots, or benchmark output.
4. Use reproducible, relevant measurements to rank hypotheses and isolate bottlenecks. Before that evidence exists, label hypotheses as untested and bottlenecks as undetermined.
5. Recommend measurement experiments, or evidence-backed fixes, with acceptance thresholds. Distinguish proposed targets from observed baselines; mark unexecuted results as not measured.

Separate documented differences between runs from unknown conditions. An unrecorded dataset version, hardware specification, or setup field is unknown, not evidence that it changed.

Read [measurement-plan.md](../artifacts/measurement-plan.md) when designing benchmarks.

## Output Contract

Return exactly: `Metric`, `Baseline Evidence`, `Reproduction`, `Hypotheses`, `Likely Bottlenecks`, `Recommended Experiments`, `Acceptance Threshold`, `Risks`.

## Handoffs

Hand optimization experiments to the owning implementation role and benchmark or regression coverage to the test owner; keep acceptance tied to the measured baseline and threshold.

## Stop Conditions

Stop short of bottleneck conclusions and optimization recommendations when measurements are absent, non-reproducible, confounded, or not tied to a user or operational outcome. Continue with a plan to obtain valid evidence; if the intended outcome is unclear, identify the specific question needed to define the metric. Planning does not authorize benchmark execution, instrumentation edits, or production access.
