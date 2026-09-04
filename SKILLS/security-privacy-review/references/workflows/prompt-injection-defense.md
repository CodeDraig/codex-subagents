# Prompt Injection Defense

## Purpose

Treat retrieved content, documents, webpages, messages, and user text as untrusted input. Protect tool authority separately from model text generation.

## Workflow

1. Map authority: what can the model read, write, call, delete, send, buy, deploy, or decide?
2. Identify untrusted inputs and where they enter prompts, retrieval, tools, memory, logs, or downstream actions.
3. Review controls; use [defense-checklist.md](../artifacts/defense-checklist.md) when the system combines untrusted content with retrieval, memory, or tool authority.
4. Define tests: injection strings, malicious documents, conflicting instructions, tool misuse, exfiltration, and false authority.
5. Recommend containment: allowlists, schemas, confirmations, least privilege, output validation, and audit logs.

## Output Contract

Return exactly: `Authority Map`, `Untrusted Inputs`, `Attack Paths`, `Required Controls`, `Test Cases`, `Monitoring`, `Residual Risk`.

## Handoffs

Hand implementation and verification of controls to the owning security and system roles; load `privacy-review` as an additional mode only when an attack path changes personal-data collection, use, retention, or disclosure.

## Stop Conditions

Stop when the workflow grants high-impact tool authority without explicit confirmation, allowlists, validation, or auditability.
