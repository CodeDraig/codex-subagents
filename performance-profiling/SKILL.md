---
name: performance-profiling
description: Use when investigating latency, throughput, startup, memory, CPU, rendering, query cost, bundle size, benchmark design, profiler output, performance regressions, SLO misses, or optimization targets before changing code.
---

# Performance Profiling

## Overview

Measure before optimizing. A useful profiling pass names the metric, baseline, reproduction, evidence, hypothesis, and acceptance threshold.

## Workflow

1. Define metric and user or system impact.
2. Reproduce with controlled inputs and environment notes.
3. Capture evidence: profiles, traces, logs, query plans, bundle analysis, screenshots, or benchmark output.
4. Rank hypotheses and isolate bottlenecks.
5. Recommend experiments or fixes with acceptance thresholds.

Use `references/measurement-plan.md` when designing benchmarks.

## Output Contract

Return exactly: `Metric`, `Baseline Evidence`, `Reproduction`, `Hypotheses`, `Likely Bottlenecks`, `Recommended Experiments`, `Acceptance Threshold`, `Risks`.

## Stop Conditions

Stop when measurements are absent, non-reproducible, confounded, or not tied to a user or operational outcome.
