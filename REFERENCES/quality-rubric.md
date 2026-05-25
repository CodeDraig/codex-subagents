# Skill and Agent Quality Rubric

Use this rubric when creating, reviewing, or improving assets under `SKILLS/` and `AGENTS/openai/`. The goal is to prevent shallow assets that only restate generic good behavior. A useful asset should change how an agent works: it should supply domain checks, decision rules, artifacts, boundaries, and verification expectations that would be hard to recreate from a one-sentence prompt.

## Rating Scale

Rate each criterion from 0 to 4.

| Score | Meaning |
| --- | --- |
| 0 | Missing or actively harmful. |
| 1 | Present only as generic advice or a placeholder. |
| 2 | Some domain detail, but incomplete enough that reviewers must reconstruct the workflow. |
| 3 | Useful and specific; covers the common workflow, outputs, boundaries, and validation needs. |
| 4 | Strong reusable asset; includes concrete domain heuristics, edge cases, artifacts, tools or references, and clear review gates. |

## Quality Gates

An asset is not ready for catalog inclusion unless:

- It scores at least 3 on every required criterion for its asset type.
- It has no 0 or 1 scores.
- It passes the anti-platitude test.
- Its claims about tools, paths, files, or external authority are true for the repo or clearly labeled as optional.
- It has an explicit owner-facing output contract.

Use a score of 4 for assets that are not just acceptable, but likely to improve future agent behavior without extra prompting.

## Anti-Platitude Test

Mark an asset as failing if removing the domain name would make the guidance still sound equally applicable to almost any task.

Weak examples:

- "Review the code carefully."
- "Follow best practices."
- "Consider edge cases."
- "Communicate clearly."
- "Use appropriate tools."

Strong guidance names concrete checks, artifacts, or decision points:

- "Check request/response shape, error format, idempotency, pagination, compatibility, generated clients, and migration notes."
- "Map each invoice to purchase order, receipt, approval, payment status, duplicate risk, and policy exception."
- "Separate binding authority, persuasive authority, guidance, commentary, and unverified secondary material."

## Fail And Pass Patterns

Failing Skill pattern:

- Trigger: "Use for design work."
- Workflow: "Understand the goal, review options, recommend best practices."
- Output: "Summary and next steps."

Why it fails: removing "design" leaves generic task advice. It lacks artifacts, checks, validation, examples, and stop conditions.

Passing Skill pattern:

- Trigger: "Use when auditing shared UI components, design tokens, interaction states, density, focus behavior, visual consistency, and migration risk."
- Workflow: inspect component inventory, compare token use, check states, capture screenshots, map exceptions to owners, and separate design debt from release blockers.
- Output: `Inventory`, `State Coverage`, `Token Findings`, `Screenshots`, `Release Blockers`, `Owner Questions`.

Why it passes: it changes the agent's behavior and creates reviewable evidence.

Failing Agent pattern:

- Description: "A general research expert."
- Instructions: "Find information, think carefully, and produce a useful report."

Why it fails: the role is not distinct, has no source treatment, and cannot be routed predictably.

Passing Agent pattern:

- Description: "Verifies claims, timestamps, quotes, provenance, edits, and source incentives before evidence is used in reporting, support, or investigations."
- Instructions: require source class, date checked, contradiction search, confidence, non-public data boundaries, publication-risk handoffs, and exact return sections.

Why it passes: it defines dispatch signals, evidence rules, boundaries, and downstream integration.

## Skill Criteria

Apply these criteria to every `SKILLS/<skill-name>/` package.

### 1. Trigger Fit

The frontmatter description must tell the parent agent when to use the skill and when not to use it.

Score 4 requires:

- Specific task signals, not only a broad topic label.
- Named artifact types, workflows, or decisions the skill supports.
- Clear exclusion or escalation boundaries for adjacent domains.

### 2. Workflow Specificity

The workflow must provide a repeatable sequence that changes agent behavior.

Score 4 requires:

- Ordered steps that match the domain's natural work sequence.
- Domain-specific checks in each step.
- Guidance for missing context, ambiguity, and handoffs.
- Enough detail that two agents using the skill should produce similar workplans.

### 3. Domain Heuristics And Decision Rules

The skill must include concrete rules that encode expertise.

Score 4 requires at least three of:

- Compatibility, safety, compliance, quality, or risk rules.
- Thresholds or severity distinctions.
- Known failure modes.
- Positive and negative examples.
- Owner decision points.
- Escalation triggers.

### 4. Supporting Assets

The skill must contain significant guidance beyond the `SKILL.md` body when the domain benefits from it.

Score 4 requires at least one meaningful supporting asset:

- A reference checklist.
- A template.
- A command or validation script.
- A sample artifact.
- A decision matrix.
- A source-quality guide.

The supporting asset must be directly referenced from `SKILL.md` and specific enough to use during execution.

### 5. Tooling And Validation Guidance

The skill must tell agents how to verify outputs or choose tools when verification is possible.

Score 4 requires:

- Concrete commands, file patterns, source classes, parser choices, or inspection steps when applicable.
- Clear distinction between executable checks, manual review, and owner-only decisions.
- Guidance on when not to proceed because validation is impossible.

### 6. Output Contract

The skill must define a stable output shape.

Score 4 requires:

- Named output sections.
- Sections aligned to the workflow and target artifact.
- Required evidence fields such as file paths, source links, commands run, examples, caveats, or owner questions.
- No generic "Summary" as the only deliverable.

### 7. Boundaries And Stop Conditions

The skill must prevent unsafe or misleading behavior.

Score 4 requires:

- Stop conditions that are specific to the domain.
- Clear handoffs to humans or other agents.
- Explicit handling of high-stakes domains such as legal, financial, security, privacy, medical, policy, or public-source investigation when relevant.
- Prohibition of fabricated evidence, hidden uncertainty, or unauthorized action.

## Agent Criteria

Apply these criteria to every `AGENTS/openai/<agent-name>.toml` file.

### 1. Role Distinctness

The agent must have a non-overlapping reason to exist.

Score 4 requires:

- A description that separates the agent from nearby roles.
- Named task signals for dispatch.
- Explicit handoffs for adjacent roles.
- No broad "general expert" phrasing.

### 2. Skill And Reference Use

The agent must use the relevant skill assets instead of duplicating shallow guidance.

Score 4 requires:

- Explicit `$skill-name` references when a supporting skill exists.
- A fallback summary for the workflow if the skill is unavailable.
- Handoffs to specific agents, not future groups or vague teams.
- Alignment with `REFERENCES/software-development-crew.md`.

### 3. Instruction Depth

The `developer_instructions` must provide operational behavior, not tone guidance.

Score 4 requires:

- Domain-specific intake questions.
- Domain-specific checks or artifacts.
- Expected evidence or source treatment.
- Risk handling and edge cases.
- Concrete things the agent should not do.

### 4. Model, Reasoning, And Sandbox Fit

Runtime settings must match the role's risk and work mode.

Score 4 requires:

- Read-only sandbox for review, analysis, high-stakes advice-adjacent, or investigation roles unless file edits are central.
- Workspace-write only for implementation, artifact creation, or documentation roles that need it.
- Higher reasoning for ambiguous, high-stakes, strategic, or cross-domain roles.
- Lower-latency models only for bounded repetitive tasks.

### 5. Handoffs And Boundaries

The agent must route work cleanly.

Score 4 requires:

- Specific handoffs to implemented agents for adjacent domains.
- Hard stops for unsafe, unauthorized, or out-of-scope work.
- Clear owner or human review gates.
- No stale references to future groups once implemented agents exist.

### 6. Output Contract

The agent must return a predictable artifact.

Score 4 requires:

- Exact section names in `Return exactly these sections`.
- Sections that match the agent's role and downstream integration.
- Inclusion of evidence, commands, paths, source links, owner questions, risks, blockers, or handoffs when relevant.
- No vague final response requirement such as "give useful feedback."

### 7. Catalog Integration

The agent must fit the catalog and install path.

Score 4 requires:

- Filename matches `name`.
- TOML parses.
- Referenced skills resolve to `SKILLS/<skill-name>/SKILL.md`.
- Agent appears in `REFERENCES/software-development-crew.md` lifecycle and routing coverage.
- Intentional overlap notes cover likely confusion with adjacent agents.

## Minimum Review Procedure

For every new or modified skill:

1. Read `SKILLS/<skill-name>/SKILL.md`.
2. Read every referenced file under `SKILLS/<skill-name>/references/`.
3. Score each skill criterion.
4. Fail the review if the skill has no meaningful supporting asset and the domain would benefit from one.
5. Fail the review if the workflow could apply unchanged to most other skills.

For every new or modified agent:

1. Parse `AGENTS/openai/<agent-name>.toml`.
2. Confirm the filename matches `name`.
3. Check every `$skill` reference resolves.
4. Check handoffs refer to implemented agents when possible.
5. Score each agent criterion.
6. Fail the review if the agent can be replaced by a one-paragraph prompt with no loss of behavior.

For generated batches, sample-based review is not enough. Every generated asset must receive an explicit score, and any repeated shallow phrase such as "best practices", "communicate clearly", or "consider edge cases" must be replaced with domain-specific checks before the batch is marked complete.

## Readiness Labels

Use these labels in reviews and planning docs:

- `Ready`: all required criteria are at least 3, no platitude failures, validation passes.
- `Useful but Thin`: no correctness blocker, but at least one criterion is 2 and should be improved before broad reuse.
- `Scaffold Only`: mostly placeholders or generic prose; not ready for catalog claims.
- `Unsafe or Misleading`: contains fabricated authority, missing stop conditions, wrong paths, or instructions that could cause harmful behavior.

## Reviewer Summary Template

```markdown
Rating: Ready | Useful but Thin | Scaffold Only | Unsafe or Misleading

Scores:
- Trigger or role fit: N/4
- Workflow or instruction depth: N/4
- Domain heuristics: N/4
- Supporting assets or skill use: N/4
- Tooling and validation: N/4
- Output contract: N/4
- Boundaries and catalog integration: N/4

Required fixes:
- ...

Evidence:
- Files reviewed: ...
- Commands run: ...
- Stale path or unresolved reference checks: ...
```
