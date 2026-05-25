# Current Repository Layout

This repository uses three top-level canonical asset directories:

- `AGENTS/openai/` contains reusable OpenAI custom-agent TOML templates.
- `SKILLS/<skill-name>/` contains runnable skill packages with `SKILL.md`, `agents/openai.yaml`, and optional `references/` material.
- `REFERENCES/` contains shared catalog and configuration references used by skills and agent templates.

The previous mixed layout has been removed. Do not add new skills or agent templates outside the canonical top-level asset directories.

## Adding Skills

Create each new skill under `SKILLS/<skill-name>/`:

```text
SKILLS/<skill-name>/
  SKILL.md
  agents/openai.yaml
  references/<focused-checklist>.md
```

The `name` in `SKILL.md` must match `<skill-name>`. If any agent template references `$<skill-name>`, the corresponding `SKILLS/<skill-name>/SKILL.md` file must exist before the registry claims full coverage.

Before adding a skill to the catalog, rate it with `REFERENCES/quality-rubric.md`. Do not add scaffold-only skills that contain only generic workflow advice.

## Adding Agents

Create each OpenAI agent template under `AGENTS/openai/<agent-name>.toml`.

Every agent template must parse as TOML and include the expected identity and runtime fields:

- `name`
- `description`
- `model`
- `model_reasoning_effort`
- `sandbox_mode`
- `nickname_candidates`
- `developer_instructions`

Before adding an agent to the catalog, rate it with `REFERENCES/quality-rubric.md`. Do not add broad "general expert" agents or templates whose instructions can be replaced by a one-paragraph prompt with no loss of behavior.

## Shared References

Use `REFERENCES/software-development-crew.md` as the canonical registry for lifecycle coverage, routing rules, model coverage, intentional overlap, and implemented skill assets.

Use `REFERENCES/subagent-toml.md` when creating or reviewing reusable custom-agent TOML files.

Use `REFERENCES/prompt-patterns.md` for subagent prompt patterns.

Use `REFERENCES/quality-rubric.md` to review whether skills and agents are complete enough for reusable catalog inclusion.

## Installing The Designer Skill

When installing `SKILLS/codex-subagent-designer/` outside this repository, preserve its supporting material:

- Copy shared `REFERENCES/*.md` into the installed skill's `references/` directory.
- Copy reusable OpenAI agent examples from `AGENTS/openai/` into `agents/examples/openai/`.
- Rewrite installed links only for the installed copy; keep repository links pointing at canonical top-level `REFERENCES/` and `AGENTS/openai/`.
- Verify no `.DS_Store` or local-only artifacts are copied.
