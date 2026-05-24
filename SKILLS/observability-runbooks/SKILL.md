---
name: observability-runbooks
description: Use when designing or reviewing logs, metrics, traces, alerts, dashboards, SLOs, operational diagnostics, runbook steps, on-call handoffs, incident detection, or telemetry for production systems.
---

# Observability Runbooks

## Overview

Add signals that answer operational questions. A useful runbook links symptom, signal, owner, likely causes, safe checks, and remediation.

## Workflow

1. State the operational question or failure mode.
2. Define logs, metrics, traces, dashboards, and alerts needed to answer it.
3. Avoid sensitive data, high-cardinality labels, and unactionable paging.
4. Write runbook steps: detect, triage, mitigate, escalate, verify recovery.
5. Define SLO or threshold when applicable.

Use `references/runbook-template.md` for operational handoffs.

## Output Contract

Return exactly: `Operational Question`, `Signals`, `Alerts`, `Dashboards`, `Runbook Steps`, `SLO Or Threshold`, `Risks`, `Follow-Up`.

## Stop Conditions

Stop when telemetry would expose sensitive data, create paging noise without action, or require production access without approval.
