#!/usr/bin/env python3
"""Audit the full catalog uplift matrix for ready-state scores."""

from __future__ import annotations

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MATRIX = ROOT / "docs/reviews/2026-05-24-full-catalog-uplift-matrix.csv"


def parse_scores(value: str) -> list[int] | None:
    parts = value.split("/")
    if len(parts) != 7:
        return None
    scores: list[int] = []
    for part in parts:
        if not part.isdigit():
            return None
        score = int(part)
        if score < 0 or score > 4:
            return None
        scores.append(score)
    return scores


def main() -> int:
    errors: list[str] = []
    with MATRIX.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    if len(rows) != 139:
        errors.append(f"{MATRIX.relative_to(ROOT).as_posix()}: expected 139 rows, found {len(rows)}")

    for index, row in enumerate(rows, start=2):
        name = row.get("name", f"row {index}")
        if row.get("after_rating") != "Ready":
            errors.append(f"row {index} {name}: after_rating must be Ready")
        scores = parse_scores(row.get("after_scores", ""))
        if scores is None:
            errors.append(f"row {index} {name}: after_scores must be seven slash-separated integers 0..4")
        elif any(score < 3 for score in scores):
            errors.append(f"row {index} {name}: after_scores values must all be >=3")
        if not row.get("validation_evidence", "").strip():
            errors.append(f"row {index} {name}: validation_evidence must be non-empty")

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("score audit passed: all assets Ready")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
