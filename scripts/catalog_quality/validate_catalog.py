#!/usr/bin/env python3
"""Validate the repo-local skill and OpenAI agent catalog."""

from __future__ import annotations

import os
import re
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REQUIRED_TOML_KEYS = {
    "name",
    "description",
    "model",
    "model_reasoning_effort",
    "sandbox_mode",
    "nickname_candidates",
    "developer_instructions",
}
SKILL_REF_RE = re.compile(r"\$([A-Za-z0-9][A-Za-z0-9_-]*)")


try:
    import tomllib
except ModuleNotFoundError:
    python311 = shutil.which("python3.11")
    if python311 and Path(python311).resolve() != Path(sys.executable).resolve():
        os.execv(python311, [python311, *sys.argv])
    raise


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_toml(path: Path, errors: list[str]) -> dict[str, object]:
    try:
        with path.open("rb") as handle:
            data = tomllib.load(handle)
    except tomllib.TOMLDecodeError as exc:
        errors.append(f"{rel(path)}: invalid TOML: {exc}")
        return {}
    return data


def check_agents(errors: list[str]) -> None:
    for path in sorted((ROOT / "AGENTS/openai").glob("*.toml")):
        data = load_toml(path, errors)
        missing = sorted(REQUIRED_TOML_KEYS - set(data))
        if missing:
            errors.append(f"{rel(path)}: missing required TOML keys: {', '.join(missing)}")
        name = data.get("name")
        if name != path.stem:
            errors.append(f"{rel(path)}: name {name!r} does not match filename stem {path.stem!r}")
        text = path.read_text(encoding="utf-8")
        for skill_name in sorted(set(SKILL_REF_RE.findall(text))):
            skill_path = ROOT / "SKILLS" / skill_name / "SKILL.md"
            if not skill_path.exists():
                errors.append(f"{rel(path)}: unresolved skill reference ${skill_name}")


def check_skill_frontmatter(errors: list[str]) -> None:
    for path in sorted((ROOT / "SKILLS").glob("*/SKILL.md")):
        lines = path.read_text(encoding="utf-8").splitlines()
        if not lines or lines[0] != "---":
            errors.append(f"{rel(path)}: frontmatter must start with ---")
            continue
        try:
            end_index = lines[1:].index("---") + 1
        except ValueError:
            errors.append(f"{rel(path)}: frontmatter must end with ---")
            continue
        fields = {}
        for line in lines[1:end_index]:
            if ":" in line:
                key, value = line.split(":", 1)
                fields[key.strip()] = value.strip()
        for key in ("name", "description"):
            if not fields.get(key):
                errors.append(f"{rel(path)}: frontmatter missing {key}")
        if fields.get("name") and fields["name"] != path.parent.name:
            errors.append(
                f"{rel(path)}: frontmatter name {fields['name']!r} "
                f"does not match directory {path.parent.name!r}"
            )


def check_reference_registry(errors: list[str]) -> None:
    registry_path = ROOT / "REFERENCES/software-development-crew.md"
    text = registry_path.read_text(encoding="utf-8")
    for path in sorted((ROOT / "AGENTS/openai").glob("*.toml")):
        if path.stem not in text:
            errors.append(f"{rel(registry_path)}: missing agent mention {path.stem}")
    for path in sorted((ROOT / "SKILLS").glob("*/SKILL.md")):
        skill_name = path.parent.name
        if skill_name == "codex-subagent-designer":
            continue
        if skill_name not in text:
            errors.append(f"{rel(registry_path)}: missing skill mention {skill_name}")


def check_skill_agent_yaml(errors: list[str]) -> None:
    for skill_path in sorted((ROOT / "SKILLS").glob("*/SKILL.md")):
        path = skill_path.parent / "agents/openai.yaml"
        if not path.exists():
            errors.append(f"{rel(path)}: missing skill agent sidecar")
            continue
        text = path.read_text(encoding="utf-8")
        if re.search(r"(?m)^(models|agents):", text):
            continue
        if re.search(r"(?m)^interface:\s*$", text):
            required_interface_keys = {
                "display_name",
                "short_description",
                "default_prompt",
            }
            present = {
                match.group(1)
                for match in re.finditer(r"(?m)^  ([A-Za-z0-9_-]+):\s*.+$", text)
            }
            missing = sorted(required_interface_keys - present)
            if missing:
                errors.append(f"{rel(path)}: interface missing keys: {', '.join(missing)}")
            continue
        errors.append(f"{rel(path)}: must contain models:, agents:, or interface:")


def check_ds_store(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob(".DS_Store")):
        errors.append(f"{rel(path)}: .DS_Store files are not allowed")


def main() -> int:
    errors: list[str] = []
    check_agents(errors)
    check_skill_frontmatter(errors)
    check_reference_registry(errors)
    check_skill_agent_yaml(errors)
    check_ds_store(errors)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("catalog validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
