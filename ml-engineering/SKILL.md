---
name: ml-engineering
description: Use when designing or reviewing model training and inference code, feature pipelines, evaluation harnesses, integration boundaries, or production-facing ML behavior.
---

# ML Engineering

## Overview

Use this skill to reason about ML implementation from data to inference. Keep the focus on measurable behavior, stable interfaces, and production-safe integration points.

## Workflow

1. Identify the target task, success metric, and expected model behavior.
2. Check training data splits, feature availability, leakage risk, and labeling quality.
3. Review the training loop, evaluation harness, baseline, and acceptance threshold.
4. Define the inference contract: inputs, outputs, latency, batching, and failure handling.
5. Verify integration boundaries for services, jobs, and downstream consumers.

Use `references/model-delivery-checklist.md` for delivery review.

## Output Contract

Return exactly: `Problem Framing`, `Data and Feature Contracts`, `Training and Evaluation`, `Inference Contract`, `Integration Risks`, `Recommended Next Step`, `Open Questions`.

## Stop Conditions

Stop when model behavior lacks a target metric, labeled evaluation set, or clear inference contract.
