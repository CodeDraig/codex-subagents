# Measurement Plan

## Required Fields

- Metric:
- Baseline:
- Target:
- Environment:
- Dataset:
- Warmup:
- Number of runs:
- Noise sources:
- Tooling:
- Command:

## Common Metrics

- p50/p95/p99 latency.
- Startup time.
- Memory peak and steady state.
- CPU time.
- Query duration and rows scanned.
- Bundle size and render timings.
- Throughput and saturation point.

## Pitfalls

- Cold vs warm cache confusion.
- Network noise.
- Debug builds.
- Tiny samples.
- Measuring implementation detail instead of outcome.
