# Discovery Brief

## Assumption Table

| Assumption | Evidence | Risk | How To Validate |
| --- | --- | --- | --- |
| User has the problem | interviews, tickets, analytics, request | safe/risky/must-confirm | question, metric, prototype, experiment |

## Assumption Risk Thresholds

- `safe`: supported by current direct evidence, or cheap to reverse if wrong.
- `risky`: plausible but supported by indirect evidence, stale evidence, or only one stakeholder; validate before broad build-out.
- `must-confirm`: would change the user, workflow, business model, compliance posture, data model, architecture, or release scope if wrong.

## Validation Method Choices

| Question | Cheapest useful validation |
| --- | --- |
| Does the user understand the workflow? | clickable prototype, task walkthrough, usability notes |
| Does the user have the problem often enough? | support ticket count, analytics query, interview pattern, sales/support notes |
| Can the process work operationally? | concierge/manual run, runbook trial, internal pilot |
| Will behavior change after release? | instrumented thin slice, cohort metric, before/after comparison |
| Is the market norm or comparable unclear? | competitive scan via `$competitive-research` |

## Acceptance Criteria Quality Bar

- Describes user-visible behavior.
- Includes error, empty, and permission cases when relevant.
- Avoids implementation details unless visible to the user.
- Can be verified by a reviewer or test.
- Names the actor, trigger, visible result, and any state transition or audit record.
- Includes owner decision points when success cannot be fully automated.

## Scope Cut Questions

- What is the smallest release that changes user behavior?
- What can be manual, mocked, or omitted for the first version?
- What would make the release unsafe or misleading?
- Which decisions can wait until after first use?

## Handoff Checklist

- UX handoff: personas, primary task, key states, content constraints, accessibility risks.
- Design-system handoff: existing components, new pattern requests, token or density constraints.
- Architecture handoff: data ownership, integration boundaries, non-functional constraints, reversibility.
- Implementation-planning handoff: acceptance criteria, non-goals, validation gates, rollout constraints.
