---
name: incident-postmortems
description: Use when reconstructing incidents, outages, regressions, security events, repeated support escalations, production failures, timelines, contributing factors, corrective actions, or post-incident follow-up.
---

# Incident Postmortems

## Overview

Analyze incidents to improve systems, not assign blame. Preserve timeline, impact, detection, contributing factors, and corrective actions that reduce recurrence.

## Workflow

1. Collect facts: timeline, alerts, logs, deploys, user reports, commands, and decisions.
2. Define impact: who was affected, duration, severity, data or security exposure, and business effect.
3. Identify contributing factors across code, process, tooling, monitoring, docs, and ownership.
4. Create corrective actions with owners, due dates, validation, and priority.
5. Separate known facts from hypotheses.

Use `references/postmortem-template.md` for structure.

## Output Contract

Return exactly: `Summary`, `Impact`, `Timeline`, `Detection`, `Contributing Factors`, `What Went Well`, `Corrective Actions`, `Open Questions`, `Follow-Up`.

## Stop Conditions

Stop when facts are too incomplete to distinguish timeline from hypothesis, or when legal/security/privacy review is needed before sharing details.
