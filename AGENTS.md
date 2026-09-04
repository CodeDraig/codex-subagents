# Repository Instructions

## Scope

These instructions apply to the entire repository.

## Canonical Asset Organization

Keep reusable catalog assets in these top-level locations:

- `AGENTS/openai/` contains reusable OpenAI custom-agent TOML templates.
- `SKILLS/<skill-name>/` contains runnable skill packages.
- `REFERENCES/` contains shared catalog and configuration references used by skills and agent templates.

Do not add reusable skills or agent templates outside these canonical directories.

## Skill Packages

Create each skill under `SKILLS/<skill-name>/`. A package normally contains:

```text
SKILLS/<skill-name>/
  SKILL.md
  agents/openai.yaml
  references/<focused-checklist>.md
```

- The `name` in `SKILL.md` must match `<skill-name>`.
- If an agent template references `$<skill-name>`, the corresponding `SKILLS/<skill-name>/SKILL.md` must exist before claiming registry coverage.
- Review every new skill against `REFERENCES/quality-rubric.md` before adding it to the catalog.
- Do not add scaffold-only skills containing only generic workflow advice.

## Agent Templates

Create each OpenAI agent template at `AGENTS/openai/<agent-name>.toml`.

Every template must parse as TOML and contain:

- `name`
- `description`
- `model`
- `model_reasoning_effort`
- `sandbox_mode`
- `nickname_candidates`
- `developer_instructions`

- Use `REFERENCES/subagent-toml.md` when creating or reviewing a template.
- Review every new template against `REFERENCES/quality-rubric.md` before adding it to the catalog.
- Do not add broad "general expert" agents or templates whose behavior can be replaced without loss by a one-paragraph prompt.

## Shared References And Registry

- Treat `REFERENCES/software-development-crew.md` as the canonical registry for lifecycle coverage, routing rules, model coverage, intentional overlap, and implemented skill assets.
- Update that registry when an asset changes routing, lifecycle coverage, model coverage, intentional overlap, or implemented skill coverage.
- Use `REFERENCES/prompt-patterns.md` for subagent prompt patterns.
- Use `REFERENCES/quality-rubric.md` to determine whether skills and agents are complete enough for reusable catalog inclusion.
