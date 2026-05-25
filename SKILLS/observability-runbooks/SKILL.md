---
name: observability-runbooks
description: Use when designing or reviewing logs, metrics, traces, alerts, dashboards, SLOs, operational diagnostics, runbook steps, on-call handoffs, incident detection, or telemetry for production systems.
---

# Observability Runbooks

## Overview

Add signals that answer operational questions. A useful runbook links symptom, signal, owner, likely causes, safe checks, and remediation.

## Workflow

1. State the operational question or failure mode.
2. Define logs, metrics, traces, dashboards, and alerts needed to answer it. Every signal should answer a specific triage question, not just add volume.
3. Avoid sensitive data, high-cardinality labels, and unactionable paging. Alerts should name the owner, threshold, action, and whether they are paging or informational.
4. Write runbook steps: detect, triage, mitigate, escalate, verify recovery.
5. Define SLO or threshold when applicable, and note the evidence required to declare the issue resolved.

Use `references/runbook-template.md` for operational handoffs and alert evidence.

## Decision Rules

- Do not page on a signal that cannot lead to a concrete action or safe escalation.
- Prefer a linked dashboard or query over prose when an operator needs to confirm impact.
- If a mitigation is risky or partial, document the rollback or containment step before the repair step.
- If validation requires production access or a privileged command, mark it as an owner-only check.

## Output Contract

Return exactly: `Operational Question`, `Signals`, `Alerts`, `Dashboards`, `Runbook Steps`, `SLO Or Threshold`, `Risks`, `Follow-Up`.

## Stop Conditions

Stop when telemetry would expose sensitive data, create paging noise without action, or require production access without approval.
