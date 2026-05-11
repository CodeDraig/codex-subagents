---
name: codex-subagent-designer
description: Design effective Codex subagent workflows, delegation boundaries, and validation prompts. Use when the user asks to create, improve, review, or plan Codex subagents; asks how to split coding work across agents; requests parallel agent execution plans; or needs prompt templates for explorer, worker, reviewer, or validator subagents.
---

# Codex Subagent Designer

Use this skill to decide whether subagents help, how to split the work, and how to write prompts that produce integrable results.

## Core Workflow

1. Restate the user's goal as a concrete outcome.
2. Identify the local critical path: the next task the main agent should do directly.
3. Identify parallel sidecar tasks that can advance the goal without blocking the immediate next step.
4. Assign each subagent one bounded responsibility with explicit inputs, outputs, and ownership.
5. Define how results will be integrated, reviewed, and verified.
6. Avoid delegation when the work is urgent, tightly coupled, trivial, or impossible to validate from the subagent's output.

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

## Agent Roles

Use role names that match the available subagent system when possible.

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

## Planning Pattern

Use this structure for a subagent plan:

```markdown
Main agent:
- Immediate task: ...
- Why local: ...

Subagents:
- Role: ...
  Task: ...
  Owns: ...
  Output: ...
  Integration point: ...

Verification:
- ...
```

## Prompt Templates

When concrete prompt language would help, read [prompt-patterns.md](references/prompt-patterns.md). Use it for explorer, worker, validator, and forward-test prompts.

## TOML Configs

When creating or reviewing reusable Codex subagent configuration files, read [subagent-toml.md](references/subagent-toml.md). Keep generated TOML minimal: required identity fields first, optional runtime overrides only when the role truly needs them.

For a full reusable OpenAI software-development crew, read [software-development-crew.md](references/software-development-crew.md). The examples live under `agents/examples/openai/` as one TOML file per agent.
