#!/usr/bin/env python3
"""Fail-closed structural audit for the Mathematics Mastery → Research System."""

from __future__ import annotations

import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
MODULE = ROOT / "05_mathematical_skills_development"
ATLAS = ROOT / "11_mathematics_literature_atlas" / "educational_sources"

ERRORS: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # fail closed
        ERRORS.append(f"JSON parse failure: {path}: {exc}")
        return {}


def load_yaml(path: Path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # fail closed
        ERRORS.append(f"YAML parse failure: {path}: {exc}")
        return {}


def audit_core_files() -> None:
    required = [
        MODULE / "README.md",
        MODULE / "MASTER_MATHEMATICS_ROADMAP.md",
        MODULE / "MATHEMATICS_DEPENDENCY_GRAPH.md",
        MODULE / "MASTERY_STANDARD.md",
        MODULE / "progress" / "competency_registry.json",
        MODULE / "progress" / "mastery_matrix.yaml",
        MODULE / "templates" / "SUBJECT_TEMPLATE.md",
        MODULE / "assets" / "mathematics-mastery-research-lattice.svg",
        ATLAS / "WQU_MATHEMATICS_FOUNDATION_RESOURCES_2024.md",
    ]
    for path in required:
        require(path.is_file(), f"Missing required artifact: {path.relative_to(ROOT)}")


def audit_registry_and_matrix() -> None:
    registry = load_json(MODULE / "progress" / "competency_registry.json")
    matrix = load_yaml(MODULE / "progress" / "mastery_matrix.yaml")

    allowed_states = set(registry.get("allowed_states", []))
    dimensions = registry.get("competency_dimensions", [])
    subjects = matrix.get("subjects", []) if isinstance(matrix, dict) else []

    require(bool(allowed_states), "Competency registry has no allowed states")
    require("PASS" in allowed_states and "NOT_TESTED" in allowed_states, "Required states absent")
    require(len(dimensions) == 7, "Expected seven competency dimensions")
    require(len(subjects) == 25, f"Expected 25 subjects, found {len(subjects)}")

    ids = [s.get("id") for s in subjects]
    require(len(ids) == len(set(ids)), "Duplicate subject IDs in mastery matrix")
    id_set = set(ids)

    graph: dict[str, list[str]] = {}
    for subject in subjects:
        sid = subject.get("id")
        state = subject.get("state")
        prereqs = subject.get("prerequisites", []) or []
        require(state in allowed_states, f"Invalid state {state!r} for {sid}")
        require(isinstance(prereqs, list), f"Prerequisites must be a list for {sid}")
        graph[sid] = list(prereqs)
        for prereq in prereqs:
            require(prereq in id_set, f"Unknown prerequisite {prereq} referenced by {sid}")

        try:
            number = int(str(sid).split("-")[-1])
        except Exception:
            ERRORS.append(f"Malformed subject ID: {sid}")
            continue
        matches = list(MODULE.glob(f"{number:02d}_*/README.md"))
        require(len(matches) == 1, f"Expected exactly one subject README for {sid}; found {len(matches)}")

    template = matrix.get("competency_template", {})
    require(set(template.keys()) == set(dimensions), "Competency template does not match registry dimensions")
    for dimension, state in template.items():
        require(state in allowed_states, f"Invalid template state {state!r} for {dimension}")

    # DAG validation: prerequisite edges must be acyclic.
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}

    def visit(node: str, trail: tuple[str, ...]) -> None:
        if color[node] == GRAY:
            ERRORS.append("Prerequisite cycle detected: " + " -> ".join((*trail, node)))
            return
        if color[node] == BLACK:
            return
        color[node] = GRAY
        for prereq in graph.get(node, []):
            if prereq in graph:
                visit(prereq, (*trail, node))
        color[node] = BLACK

    for node in graph:
        if color[node] == WHITE:
            visit(node, ())


def audit_scientific_contracts() -> None:
    standard = (MODULE / "MASTERY_STANDARD.md").read_text(encoding="utf-8")
    require("non-compensatory" in standard.lower(), "Mastery standard must declare non-compensatory promotion")
    require("falsification" in standard.lower(), "Mastery standard must include falsification")
    require("## 9. Differential-geometry transfer rule" in standard, "Differential-geometry transfer rule missing")
    require("application state space" in standard.lower(), "Application-state-space semantics missing from geometry transfer rule")

    source = (ATLAS / "WQU_MATHEMATICS_FOUNDATION_RESOURCES_2024.md").read_text(encoding="utf-8")
    require("USER_PROVIDED_SOURCE" in source, "WQU source provenance status missing")
    require("NOT_PERFORMED" in source, "External-link verification status missing")
    require("Course completion is not" in source, "Source exposure/mastery boundary missing")


def audit_svg() -> None:
    svg = MODULE / "assets" / "mathematics-mastery-research-lattice.svg"
    try:
        root = ET.parse(svg).getroot()
    except Exception as exc:
        ERRORS.append(f"SVG parse failure: {exc}")
        return
    require(root.tag.endswith("svg"), "Visual asset root is not SVG")
    text = svg.read_text(encoding="utf-8")
    for token in ["Research Transfer", "Non-compensatory gate", "scientific semantics"]:
        require(token in text, f"SVG scientific-semantic token missing: {token}")


def main() -> int:
    audit_core_files()
    audit_registry_and_matrix()
    audit_scientific_contracts()
    audit_svg()

    if ERRORS:
        print("MATHEMATICS MASTERY AUDIT: FAIL")
        for index, error in enumerate(ERRORS, start=1):
            print(f"{index:02d}. {error}")
        return 1

    print("MATHEMATICS MASTERY AUDIT: PASS")
    print("- core artifacts present")
    print("- competency registry and YAML parse")
    print("- 25 subject IDs unique")
    print("- all prerequisite references resolve")
    print("- prerequisite graph acyclic")
    print("- subject README coverage complete")
    print("- scientific/evidence contracts present")
    print("- adaptive SVG parses successfully")
    return 0


if __name__ == "__main__":
    sys.exit(main())
