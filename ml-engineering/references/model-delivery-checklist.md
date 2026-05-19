# Model Delivery Checklist

## Problem Definition

- Target task is explicit.
- Success metric is named and measurable.
- Baseline behavior is documented.

## Data and Features

- Training, validation, and test splits are defined.
- Labels are available and trustworthy.
- Feature availability matches training and inference.
- Leakage checks are documented.

## Training and Evaluation

- Training loop is reproducible.
- Hyperparameters and seeds are captured.
- Evaluation harness covers the target metric.
- Error analysis has representative cases.

## Inference Contract

- Input schema is defined.
- Output schema is defined.
- Latency, throughput, and batching expectations are clear.
- Failure modes and fallback behavior are specified.

## Rollout Limits

- Model artifact format is known.
- Versioning and rollback limits are stated.
- Integration dependencies are listed.
- Approval needs for deployment are called out.
