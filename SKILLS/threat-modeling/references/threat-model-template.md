# Threat Model Template

## Scope

- Feature or system:
- In scope:
- Out of scope:
- Assumptions:
- Owners:

## Assets

- Identities and privileges:
- Secrets and credentials:
- Personal or regulated data:
- Business-sensitive data:
- Compute, storage, or billing resources:
- AI tool authority or automation:

## Trust Boundaries

Describe each boundary as:

`Actor or system A -> boundary crossed -> system B -> data/action`

Include browser/server, tenant/tenant, user/admin, service/service, CI/runtime, model/tool, third-party/internal, and file/input parser boundaries when relevant.

## Attack Path Format

- Threat:
- Attacker:
- Entry point:
- Preconditions:
- Steps:
- Impact:
- Existing controls:
- Missing controls:
- Severity:
- Required mitigation:
- Test or monitoring:

## Mitigation Quality Bar

A mitigation is actionable only when it names:

- The control to add or strengthen.
- The file, module, service, or owner likely responsible.
- The acceptance criterion.
- The validation method.
- The residual risk if the mitigation is partial.
