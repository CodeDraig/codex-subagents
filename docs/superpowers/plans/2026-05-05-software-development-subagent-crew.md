# Software Development Subagent Crew Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build reusable per-agent TOML examples for a deep OpenAI software development crew.

**Architecture:** Add one focused TOML file per agent under the skill's example directory, then add a registry reference that explains lifecycle coverage and future Skill dependencies. Keep the current skill lightweight by linking to the registry instead of embedding the whole roster in `SKILL.md`.

**Tech Stack:** Codex custom agent TOML, Markdown references, Python `tomllib` for syntax validation.

---

### Task 1: Add Reusable Agent Examples

**Files:**
- Create: `codex-subagent-designer/agents/examples/openai/*.toml`

- [x] **Step 1: Create the example directory**

Run: `mkdir -p codex-subagent-designer/agents/examples/openai`

Expected: directory exists.

- [x] **Step 2: Add one TOML file per agent**

Create reusable custom-agent files with required identity fields, model overrides, reasoning effort, sandbox posture, nickname candidates, and long-form behavioral instructions.

- [x] **Step 3: Include model coverage**

Confirm the set includes `gpt-5.5` with `low`, `medium`, `high`, and `xhigh`, plus `gpt-5.4-mini`, `gpt-5.3-codex`, and `gpt-5.3-codex-spark`.

### Task 2: Add Registry and Skill Backlog

**Files:**
- Create: `codex-subagent-designer/references/software-development-crew.md`
- Modify: `codex-subagent-designer/agents/openai.yaml`

- [x] **Step 1: Write the registry**

Document every agent, lifecycle stage, model, reasoning effort, sandbox mode, and future Skill references.

- [x] **Step 2: Update the OpenAI agent catalog**

Point `codex-subagent-designer/agents/openai.yaml` at the reusable examples and registry.

### Task 3: Validate

**Files:**
- Read: `codex-subagent-designer/agents/examples/openai/*.toml`
- Read: `codex-subagent-designer/references/software-development-crew.md`

- [x] **Step 1: Parse TOML**

Run: `python3 - <<'PY'
from pathlib import Path
import tomllib
for path in sorted(Path("codex-subagent-designer/agents/examples/openai").glob("*.toml")):
    tomllib.loads(path.read_text())
    print(path)
PY`

Expected: every TOML file path prints without parser errors.

- [x] **Step 2: Check model coverage**

Run: `rg 'model =|model_reasoning_effort' codex-subagent-designer/agents/examples/openai`

Expected: output includes every requested model and all four `gpt-5.5` reasoning levels.

- [x] **Step 3: Inspect future Skill backlog**

Run: `rg '^-' codex-subagent-designer/references/software-development-crew.md`

Expected: the registry includes a maintainable list of future Skills referenced by the agents.
