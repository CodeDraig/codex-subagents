---
name: threat-modeling
description: Use when analyzing security risk for new features, architecture changes, data flows, authentication, authorization, AI tool use, external integrations, file handling, webhooks, multi-tenant systems, privileged operations, or code changes that cross trust boundaries.
---

# Threat Modeling

## Overview

Build practical threat models that turn security concerns into concrete engineering decisions. Focus on assets, trust boundaries, attacker goals, exploit paths, mitigations, tests, monitoring, and residual risk.

## Workflow

1. Define scope.
   - Name the feature, system, code path, deployment, actors, data, and decisions under review.
   - Exclude out-of-scope systems explicitly so the model does not sprawl.

2. Map assets and trust boundaries.
   - Use `references/threat-model-template.md` for the working structure.
   - Include identities, privileges, secrets, personal data, business data, compute resources, model/tool authority, and operational controls.

3. Identify entry points and attacker capabilities.
   - External users, authenticated users, tenants, admins, internal services, CI, webhooks, third-party APIs, uploaded files, prompts, retrieval content, browser clients, and operators.
   - State what each attacker can observe, influence, replay, or mutate.

4. Generate abuse cases.
   - Cover spoofing, tampering, repudiation, information disclosure, denial of service, privilege escalation, confused deputy, supply-chain compromise, prompt injection, and unsafe automation when relevant.
   - Prefer concrete attack paths over abstract category labels.

5. Evaluate mitigations.
   - Identify existing controls, missing controls, testable requirements, monitoring signals, and owner decisions.
   - Separate required fixes from optional hardening.

6. Report residual risk.
   - If a risk remains, name who must accept it and what evidence or monitoring supports that acceptance.

## Risk Prioritization

Prioritize findings by exploitability and impact:

- Critical: likely or plausible path to unauthorized privileged action, sensitive data exposure, remote code execution, cross-tenant compromise, credential theft, or irreversible destructive operation.
- High: meaningful bypass, data access, automation abuse, durable denial of service, or missing control on a sensitive boundary.
- Medium: constrained exploit, defense-in-depth gap, weak auditability, or failure mode that needs a planned fix.
- Low: hardening or clarity improvement with limited direct exploitability.

## AI And Automation Boundaries

When the system includes model calls, tools, retrieval, documents, or autonomous actions:

- Treat user-controlled text and retrieved content as untrusted input.
- Identify tool authority separately from model text generation.
- Check whether the model can influence file writes, network calls, code execution, emails, tickets, payments, infrastructure, or user-visible decisions.
- Require explicit allowlists, confirmation gates, output validation, and audit logs for high-impact actions.

## Output Contract

Return exactly these sections:

- `Scope`: system, feature, data, actors, assumptions, and exclusions.
- `Assets`: sensitive data, privileges, secrets, resources, and business operations.
- `Trust Boundaries`: diagrams in text or bullet form, plus entry points.
- `Attacker Capabilities`: what each attacker can do.
- `Threats`: severity-ordered attack paths with evidence and impacted assets.
- `Required Mitigations`: concrete engineering tasks with acceptance criteria.
- `Optional Hardening`: useful but non-blocking improvements.
- `Tests And Monitoring`: regression tests, security tests, logs, metrics, alerts, and audit events.
- `Residual Risk`: what remains, who must accept it, and why.

## Stop Conditions

Stop and escalate when:

- The system handles secrets, payments, health data, regulated data, tenant isolation, privileged automation, or production infrastructure and ownership is unclear.
- A critical or high risk is discovered and the user asks to proceed without mitigation or acceptance.
- Required details are missing: auth model, data classification, trust boundary, tool authority, deployment context, or attacker capabilities.
- Validation would require probing live systems or third-party services without explicit authorization.
