"""Fail-closed validator for the DG00-DG43 dependency registry."""

from __future__ import annotations

import argparse
import html
import json
from collections import deque
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "mathematical_registry" / "dg_objects.jsonl"
DEFAULT_SOURCES = ROOT / "mathematical_registry" / "source_families.json"
DEFAULT_GRAPHML = ROOT / "mathematical_registry" / "dg_dependencies.graphml"

VALID_EVIDENCE = {"S", "D", "M", "C", "V", "R", "E", "P", "H", "T"}
VALID_PROOF = {f"PR{i}" for i in range(6)}
VALID_MATURITY = {f"P{i}" for i in range(7)}
EXPECTED_IDS = {f"DG{i:02d}" for i in range(44)}


class RegistryError(ValueError):
    """Raised when the mathematical dependency registry violates its contract."""


def load_registry(path: Path) -> list[dict[str, Any]]:
    objects: list[dict[str, Any]] = []
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise RegistryError(f"invalid JSONL at line {line_number}: {exc}") from exc
        if not isinstance(obj, dict):
            raise RegistryError(f"line {line_number}: registry record must be an object")
        objects.append(obj)
    return objects


def load_sources(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _source_ids(source_doc: dict[str, Any]) -> set[str]:
    sources = source_doc.get("sources")
    if not isinstance(sources, list):
        raise RegistryError("source registry must contain a 'sources' list")
    ids = [s.get("source_id") for s in sources]
    if any(not isinstance(x, str) or not x for x in ids):
        raise RegistryError("every source must have a non-empty source_id")
    if len(ids) != len(set(ids)):
        raise RegistryError("duplicate source_id detected")
    return set(ids)


def _topological_order(objects_by_id: dict[str, dict[str, Any]]) -> list[str]:
    indegree = {oid: 0 for oid in objects_by_id}
    outgoing = {oid: [] for oid in objects_by_id}
    for oid, obj in objects_by_id.items():
        for dep in obj["dependencies"]:
            indegree[oid] += 1
            outgoing[dep].append(oid)

    queue = deque(sorted(oid for oid, degree in indegree.items() if degree == 0))
    order: list[str] = []
    while queue:
        oid = queue.popleft()
        order.append(oid)
        for nxt in sorted(outgoing[oid]):
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    if len(order) != len(objects_by_id):
        cyclic = sorted(oid for oid, degree in indegree.items() if degree > 0)
        raise RegistryError(f"dependency cycle detected involving: {cyclic}")
    return order


def validate_registry(objects: list[dict[str, Any]], source_doc: dict[str, Any]) -> list[str]:
    """Validate DG identity, dependency, source, evidence, proof, and maturity controls."""
    if len(objects) != 44:
        raise RegistryError("registry must contain exactly 44 DG objects")

    object_ids = [obj.get("object_id") for obj in objects]
    if any(not isinstance(oid, str) for oid in object_ids):
        raise RegistryError("each object must have a string object_id")
    if len(object_ids) != len(set(object_ids)):
        raise RegistryError("duplicate object_id detected")
    if set(object_ids) != EXPECTED_IDS:
        missing = sorted(EXPECTED_IDS - set(object_ids))
        extra = sorted(set(object_ids) - EXPECTED_IDS)
        raise RegistryError(f"DG00-DG43 coverage mismatch; missing={missing}, extra={extra}")

    known_sources = _source_ids(source_doc)
    objects_by_id = {obj["object_id"]: obj for obj in objects}

    for oid, obj in objects_by_id.items():
        if not isinstance(obj.get("name"), str) or not obj["name"].strip():
            raise RegistryError(f"{oid}: missing name")
        if not isinstance(obj.get("object_type"), str) or not obj["object_type"].strip():
            raise RegistryError(f"{oid}: missing object_type")

        deps = obj.get("dependencies")
        if not isinstance(deps, list) or any(not isinstance(x, str) for x in deps):
            raise RegistryError(f"{oid}: dependencies must be a list of IDs")
        if len(deps) != len(set(deps)):
            raise RegistryError(f"{oid}: duplicate dependency")
        if oid in deps:
            raise RegistryError(f"{oid}: self dependency")
        dangling = sorted(set(deps) - EXPECTED_IDS)
        if dangling:
            raise RegistryError(f"{oid}: dangling dependencies {dangling}")

        state = obj.get("evidence_state")
        if state not in VALID_EVIDENCE:
            raise RegistryError(f"{oid}: invalid evidence_state {state!r}")
        proof = obj.get("proof_status")
        if proof not in VALID_PROOF:
            raise RegistryError(f"{oid}: invalid proof_status {proof!r}")
        maturity = obj.get("maturity")
        if maturity not in VALID_MATURITY:
            raise RegistryError(f"{oid}: invalid maturity {maturity!r}")
        if proof == "PR5" and not obj.get("formal_artifact_path"):
            raise RegistryError(f"{oid}: PR5 requires a compiling formal_artifact_path")

        locators = obj.get("source_locators")
        if not isinstance(locators, list) or not locators:
            raise RegistryError(f"{oid}: at least one source locator is required")
        for loc in locators:
            if not isinstance(loc, dict):
                raise RegistryError(f"{oid}: source locator must be an object")
            sid = loc.get("source_id")
            locator = loc.get("locator")
            if sid != "SOURCE_REQUIRED" and sid not in known_sources:
                raise RegistryError(f"{oid}: unknown source_id {sid!r}")
            if not isinstance(locator, str) or not locator.strip():
                raise RegistryError(f"{oid}: empty source locator")
            if sid == "SOURCE_REQUIRED" and state not in {"H", "T"}:
                raise RegistryError(
                    f"{oid}: SOURCE_REQUIRED may not support evidence_state {state}; "
                    "use H/T until an authoritative source is registered"
                )

        for field in ("implementation_paths", "verification_paths"):
            paths = obj.get(field)
            if not isinstance(paths, list) or any(not isinstance(x, str) for x in paths):
                raise RegistryError(f"{oid}: {field} must be a list of paths")

    return _topological_order(objects_by_id)


def generate_graphml(objects: list[dict[str, Any]]) -> str:
    """Return deterministic compact GraphML from registry records."""
    ordered = sorted(objects, key=lambda x: x["object_id"])
    edges = sorted((dep, obj["object_id"]) for obj in ordered for dep in obj["dependencies"])
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<graphml xmlns="http://graphml.graphdrawing.org/xmlns">',
        '  <key id="name" for="node" attr.name="name" attr.type="string"/>',
        '  <key id="evidence" for="node" attr.name="evidence_state" attr.type="string"/>',
        '  <key id="proof" for="node" attr.name="proof_status" attr.type="string"/>',
        '  <key id="maturity" for="node" attr.name="maturity" attr.type="string"/>',
        '  <graph id="DG-DAG-001" edgedefault="directed">',
    ]
    for obj in ordered:
        oid = html.escape(obj["object_id"], quote=True)
        lines.append(
            f'    <node id="{oid}"><data key="name">{html.escape(obj["name"])}</data>'
            f'<data key="evidence">{html.escape(obj["evidence_state"])}</data>'
            f'<data key="proof">{html.escape(obj["proof_status"])}</data>'
            f'<data key="maturity">{html.escape(obj["maturity"])}</data></node>'
        )
    for index, (source, target) in enumerate(edges):
        lines.append(
            f'    <edge id="e{index:03d}" source="{html.escape(source, quote=True)}" '
            f'target="{html.escape(target, quote=True)}"/>'
        )
    lines.extend(['  </graph>', '</graphml>', ''])
    return "\n".join(lines)


def validate_repository_registry(
    registry_path: Path = DEFAULT_REGISTRY,
    sources_path: Path = DEFAULT_SOURCES,
    graphml_path: Path = DEFAULT_GRAPHML,
) -> list[str]:
    objects = load_registry(registry_path)
    sources = load_sources(sources_path)
    order = validate_registry(objects, sources)
    expected_graph = generate_graphml(objects)
    actual_graph = graphml_path.read_text(encoding="utf-8")
    if actual_graph != expected_graph:
        raise RegistryError(
            "committed GraphML differs from deterministic registry rendering; "
            "run scripts/validate_dg_registry.py --write-graphml"
        )
    return order


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--sources", type=Path, default=DEFAULT_SOURCES)
    parser.add_argument("--graphml", type=Path, default=DEFAULT_GRAPHML)
    parser.add_argument("--write-graphml", action="store_true")
    args = parser.parse_args()

    objects = load_registry(args.registry)
    sources = load_sources(args.sources)
    order = validate_registry(objects, sources)
    graph = generate_graphml(objects)
    if args.write_graphml:
        args.graphml.write_text(graph, encoding="utf-8")
    elif args.graphml.read_text(encoding="utf-8") != graph:
        raise RegistryError("GraphML is not the deterministic rendering of the registry")

    print(f"PASS: DG-DAG-001 validated with {len(order)} objects; DAG is acyclic.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
