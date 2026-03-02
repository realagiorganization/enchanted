#!/usr/bin/env python
"""Lightweight BDD runner for Gherkin-style feature files."""
from __future__ import annotations

import glob
import sys
from dataclasses import dataclass
from pathlib import Path

FEATURE_DIR = Path("bdd/features")

@dataclass
class ScenarioResult:
    feature: str
    scenario: str
    has_given: bool
    has_when: bool
    has_then: bool


def load_feature_files() -> list[Path]:
    files = [Path(p) for p in glob.glob(str(FEATURE_DIR / "*.feature"))]
    return sorted(files)


def parse_feature(path: Path) -> tuple[str, list[ScenarioResult]]:
    feature_name = ""
    current_scenario = ""
    has_given = has_when = has_then = False
    results: list[ScenarioResult] = []

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("Feature:"):
            feature_name = line[len("Feature:"):].strip()
        elif line.startswith("Scenario:"):
            if current_scenario:
                results.append(
                    ScenarioResult(feature_name, current_scenario, has_given, has_when, has_then)
                )
            current_scenario = line[len("Scenario:"):].strip()
            has_given = has_when = has_then = False
        elif line.startswith("Given "):
            has_given = True
        elif line.startswith("When "):
            has_when = True
        elif line.startswith("Then "):
            has_then = True

    if current_scenario:
        results.append(ScenarioResult(feature_name, current_scenario, has_given, has_when, has_then))

    return feature_name, results


def main() -> int:
    files = load_feature_files()
    if not files:
        print("No feature files found in bdd/features", file=sys.stderr)
        return 1

    all_results: list[ScenarioResult] = []
    for path in files:
        feature_name, results = parse_feature(path)
        if not feature_name:
            print(f"{path}: missing Feature header", file=sys.stderr)
            return 1
        if not results:
            print(f"{path}: missing Scenario entries", file=sys.stderr)
            return 1
        all_results.extend(results)

    failures = [r for r in all_results if not (r.has_given and r.has_when and r.has_then)]
    if failures:
        print("BDD checks failed:")
        for result in failures:
            print(
                f"- Feature '{result.feature}' Scenario '{result.scenario}' is missing"
                f" Given/When/Then coverage"
            )
        return 1

    print("BDD suite summary")
    print(f"- Features: {len({r.feature for r in all_results})}")
    print(f"- Scenarios: {len(all_results)}")
    for result in all_results:
        print(f"  [ok] {result.feature} :: {result.scenario}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
