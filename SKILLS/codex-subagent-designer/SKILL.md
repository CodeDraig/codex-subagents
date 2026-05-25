---
name: codex-subagent-designer
description: Design effective Codex subagent workflows, delegation boundaries, and validation prompts. Use when the user asks to create, improve, review, or plan Codex subagents; asks how to split coding work across agents; requests parallel agent execution plans; or needs prompt templates for explorer, worker, reviewer, or validator subagents.
---

# Codex Subagent Designer

Use this skill to decide whether subagents help, how to split the work, and how to write prompts that produce integrable results.

## Core Workflow

1. Restate the user's goal as a concrete outcome.
2. If the task creates, reviews, or changes reusable Skills or Agents, read [quality-rubric.md](../../REFERENCES/quality-rubric.md) before proposing or editing assets.
3. Identify the local critical path: the next task the main agent should do directly.
4. Identify parallel sidecar tasks that can advance the goal without blocking the immediate next step.
5. Select exact custom agent types from the software-development crew when available.
6. Assign each subagent one bounded responsibility with explicit inputs, outputs, and ownership.
7. Define how results will be integrated, reviewed, scored, and verified.
8. Avoid delegation when the work is urgent, tightly coupled, trivial, or impossible to validate from the subagent's output.

Before spawning or recommending subagents, obey the active session's tool and policy constraints. If subagent tools are unavailable or the current instructions require explicit user permission, provide a subagent plan and prompts instead of launching agents.

## Delegation Fit

Use subagents when at least one condition is true:

- Several independent codebase questions can be answered in parallel.
- Implementation can be split by disjoint files, modules, packages, or test areas.
- A verification pass can run while the main agent continues non-overlapping work.
- A realistic forward-test would reveal whether a workflow, skill, prompt, or patch generalizes.

Keep the work local when:

- The main agent's next action depends on the answer.
- The task requires continuous judgment across many changing files.
- The requested change is small enough that delegation adds overhead.
- A subagent would need secrets, production access, or broad destructive authority.
- Ownership cannot be expressed without likely merge conflicts.

## Agent Selection

Default to named custom agents from [software-development-crew.md](../../REFERENCES/software-development-crew.md) when the current runtime exposes them. Use generic `worker`, `explorer`, or `default` only as fallbacks.

Use an exact custom agent when:

- The task has a clear domain: product, architecture, API, database, frontend, backend, AI, security, privacy, performance, tests, release, observability, docs, accessibility, localization, dependencies, developer experience, OSINT, technical support, or newsroom work.
- The task benefits from a standing playbook, model choice, sandbox posture, or output contract.
- The handoff would otherwise need a long prompt to recreate domain behavior.

Use generic fallbacks only when:

- The runtime does not expose the needed custom `agent_type`.
- The task is a pure codebase lookup that fits `explorer`.
- The task is a tiny implementation patch where domain specialization adds no value.
- The task is mixed and no named agent fits better than `default`.

When a custom agent is available, name it explicitly in the plan and dispatch. Do not write `Role: worker` when the intended role is `backend-domain-engineer`, `frontend-experience-engineer`, `test-automation-engineer`, or another named crew member.

Before dispatching, check [software-development-crew.md](../../REFERENCES/software-development-crew.md) for the lifecycle map and intentional overlaps.

## Fallback Roles

Use these only when a custom agent is unavailable or genuinely less appropriate.

- Explorer: answer specific codebase questions, map architecture, locate tests, or inspect failure causes. Prefer read-only outputs with file references.
- Worker: implement a bounded patch in a declared write set. Require changed file paths and verification results in the final response.
- Validator: run focused tests, review a patch, or forward-test a workflow from raw artifacts. Avoid leaking the intended answer.
- Default: use when no specialized role exists or when the task is mixed but still bounded.

## Prompt Contract

Every subagent prompt should include:

- Goal: one sentence describing the concrete result.
- Scope: files, modules, commands, or artifacts the agent owns.
- Context: only the facts needed to start.
- Constraints: what not to touch, permissions, style requirements, and integration boundaries.
- Output: exact format expected, including changed files, findings, commands run, blockers, and confidence.

For coding workers, include: "You are not alone in the codebase. Do not revert edits made by others; adapt to concurrent changes." Also state the owned files or modules.

For validators, pass raw artifacts and a user-like request. Do not pass your diagnosis, expected result, or intended fix unless the task is explicitly to evaluate that claim.

## Reusable Asset Quality Gate

Use this gate whenever the task creates, expands, reviews, or installs assets under `SKILLS/`, `AGENTS/openai/`, or a deployed skill directory.

Do not treat structural validity as completion. A syntactically valid skill or TOML file can still be too shallow to use.

Before creating assets:

1. Read [quality-rubric.md](../../REFERENCES/quality-rubric.md).
2. Identify the target assets and adjacent existing agents, skills, and registry entries.
3. Define the domain-specific behavior the asset must add beyond generic prompt advice.
4. List the supporting evidence, reference material, tools, commands, templates, examples, or decision rules the asset needs.
5. Decide whether the target should be `Ready` now or explicitly marked as a thinner scaffold for later improvement.

After creating or editing assets:

1. Score each changed Skill or Agent with the rubric before claiming completion.
2. Require every catalog-ready asset to score at least 3 on every required criterion.
3. Record any criterion below 3 as a required fix, not as optional polish.
4. Run structural validation only after the usefulness review has passed.
5. If the user asked for complete coverage, do not stop at a subset that validates structurally.

Reject assets that pass only because they have frontmatter, a workflow list, and an output contract. The asset must contain enough domain-specific checks, boundaries, supporting material, and validation guidance to make future agent behavior more consistent.

## Shallow Asset Rejection Examples

Failing Skill pattern:

```markdown
## Workflow
1. Understand the task.
2. Review relevant information.
3. Consider edge cases.
4. Communicate clearly.
```

This fails because it would work unchanged for almost any domain. It has no domain decisions, no evidence rules, no tools, no examples, no stop conditions, and no reusable artifact.

Passing Skill pattern:

```markdown
## Workflow
1. Classify the invoice as PO-backed, contract-backed, reimbursement, credit, or exception.
2. Match invoice line items to purchase order, receipt, approval, tax treatment, and payment status.
3. Flag duplicate invoice numbers, vendor-bank changes, threshold approvals, stale receipts, and policy exceptions.
4. Return a reconciliation packet with evidence links, unresolved exceptions, and finance-owner questions.
```

This passes because the workflow encodes domain checks and produces a repeatable artifact.

Failing Agent pattern:

```toml
description = "Helps with data tasks."
developer_instructions = "Analyze the data carefully, find insights, and explain your reasoning."
```

This fails because the role is too broad and the instructions do not define intake, evidence, tools, boundaries, or handoffs.

Passing Agent pattern:

```toml
description = "Reviews metric definitions, joins, freshness, and dashboard contracts before analytics changes ship."
developer_instructions = """
Use $analytics-engineering when available.
Restate grain, source tables, metric definition, filters, freshness SLA, and consuming dashboard.
Check null handling, late-arriving data, backfill impact, owner approval, and rollback path.
Hand schema ownership to `database-modeler`, pipeline changes to `data-platform-engineer`, and user-facing dashboard interpretation to `analytics-engineer`.
Return exactly these sections: `Metric Contract`, `Evidence`, `Risks`, `Validation`, `Handoffs`, `Owner Questions`.
"""
```

This passes because it names the real job, required checks, evidence, output contract, and implemented handoffs.

## Asset Authoring Checklist

Before calling a generated Skill or Agent `Ready`, confirm:

- It names the trigger signals and exclusion boundaries that distinguish it from adjacent assets.
- It includes at least three domain-specific checks, failure modes, decision rules, or severity distinctions.
- It references supporting material such as a checklist, template, decision matrix, validation command, source-quality guide, or sample artifact when the domain benefits from one.
- It defines a stable output contract with evidence fields, not only `Summary`.
- It gives validation guidance: commands, file patterns, source classes, parsers, screenshots, review gates, or explicit limits when validation is impossible.
- It names implemented handoff targets for adjacent work instead of vague teams or future groups.
- It states stop conditions for unsafe, unauthorized, high-stakes, or evidence-poor work.
- It is recorded in [software-development-crew.md](../../REFERENCES/software-development-crew.md) when it is an agent or referenced skill.

If any item is missing, either revise the asset or mark it `Useful but Thin` rather than installing it as reusable catalog content.

## Skill Package Definition Of Done

A reusable Skill package is complete only when it includes:

- Trigger guidance that says when to use the skill and how it differs from nearby skills.
- A workflow with domain-specific checks in each step.
- At least one meaningful supporting file when the domain benefits from a checklist, template, source-quality guide, decision table, example, or validation script.
- Concrete heuristics such as failure modes, severity distinctions, owner decisions, escalation triggers, compatibility rules, or source-quality rules.
- Tooling or validation guidance: commands, file patterns, parsers, source classes, evidence requirements, manual review gates, or reasons validation cannot proceed.
- A stable output contract with evidence fields, not just a generic summary.
- Domain-specific stop conditions and handoffs.

If those elements are missing, label the skill `Useful but Thin` or `Scaffold Only` in the review output and do not describe it as ready.

## Agent Template Definition Of Done

A reusable Agent template is complete only when it includes:

- A distinct role that cannot be replaced by a one-paragraph prompt without loss of behavior.
- An explicit `$skill-name` reference when a relevant skill exists, or a written justification when no skill applies.
- A fallback workflow summary for runtimes where the skill is unavailable.
- Domain-specific intake questions, checks, evidence expectations, edge cases, and things the agent must not do.
- Model, reasoning, and sandbox settings that match risk and work mode.
- Concrete handoffs to implemented agents for adjacent domains.
- Exact return sections aligned to downstream integration.
- Registry coverage in [software-development-crew.md](../../REFERENCES/software-development-crew.md).

Do not create broad "general expert" agents. Split the role or add supporting skill material until the behavior is specific and reviewable.

## Planning Pattern

Use this structure for a subagent plan:

```markdown
Main agent:
- Immediate task: ...
- Why local: ...

Subagents:
- Agent type: exact custom agent name, or fallback role with reason
  Task: ...
  Owns: ...
  Output: ...
  Integration point: ...
  Why this agent: ...

Verification:
- ...
```

## Prompt Templates

When concrete prompt language would help, read [prompt-patterns.md](../../REFERENCES/prompt-patterns.md). Use it for explorer, worker, validator, and forward-test prompts.

## TOML Configs

When creating or reviewing reusable Codex subagent configuration files, read [subagent-toml.md](../../REFERENCES/subagent-toml.md). Keep generated TOML minimal: required identity fields first, optional runtime overrides only when the role truly needs them.

For a full reusable OpenAI software-development crew, read [software-development-crew.md](../../REFERENCES/software-development-crew.md). The examples live under `AGENTS/openai/` as one TOML file per agent.

When judging whether a Skill or Agent is complete enough for catalog inclusion, read [quality-rubric.md](../../REFERENCES/quality-rubric.md). Reject scaffold-only assets that contain generic workflow platitudes without domain-specific checks, supporting references, tools, validation guidance, boundaries, and output contracts.

When this skill is installed outside this repository, copy the shared references into `references/` and the reusable agent examples into `agents/examples/openai/` inside the installed skill directory. Use those bundled copies when the repository-level `../../REFERENCES/` and `AGENTS/openai/` paths are not available.
