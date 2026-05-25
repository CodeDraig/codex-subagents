---
name: ml-engineering
description: Use when designing or reviewing model training and inference code, feature pipelines, evaluation harnesses, integration boundaries, or production-facing ML behavior that needs contract, packaging, and failure-mode checks.
---

# ML Engineering

## Overview

Use this skill to reason about ML implementation from data to inference. Keep the focus on measurable behavior, stable interfaces, packaging choices, and production-safe integration points.

## Workflow

1. Identify the target task, success metric, expected model behavior, and the product or workflow that will consume it.
2. Check training data splits, feature availability, leakage risk, labeling quality, and whether features are owned by the same system at train and inference time.
3. Review the training loop, evaluation harness, baseline, acceptance threshold, and representative error cases.
4. Define the inference contract: inputs, outputs, latency, batching, fallback behavior, and failure handling.
5. Verify model packaging, artifact format, deployment constraints, and integration boundaries for services, jobs, and downstream consumers.
6. Hand off production rollout, monitoring thresholds, and registry promotion once the implementation contract is stable.

Use `references/model-delivery-checklist.md` for delivery review.

## Output Contract

Return exactly: `Problem Framing`, `Data and Feature Contracts`, `Training and Evaluation`, `Inference Contract`, `Integration Risks`, `Recommended Next Step`, `Open Questions`, `Validation Notes`, `Handoffs`.

## Stop Conditions

Stop when model behavior lacks a target metric, labeled evaluation set, clear inference contract, or a known deployment constraint and fallback plan.
