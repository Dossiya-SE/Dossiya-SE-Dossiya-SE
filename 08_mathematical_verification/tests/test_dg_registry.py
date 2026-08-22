import copy
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.validate_dg_registry import (  # noqa: E402
    EXPECTED_IDS,
    RegistryError,
    generate_graphml,
    load_registry,
    load_sources,
    validate_registry,
    validate_repository_registry,
)

REGISTRY = ROOT / "mathematical_registry" / "dg_objects.jsonl"
SOURCES = ROOT / "mathematical_registry" / "source_families.json"
GRAPHML = ROOT / "mathematical_registry" / "dg_dependencies.graphml"


@pytest.fixture()
def documents():
    return load_registry(REGISTRY), load_sources(SOURCES)


def test_repository_registry_passes_and_covers_dg00_through_dg43():
    order = validate_repository_registry(REGISTRY, SOURCES, GRAPHML)
    assert len(order) == 44
    assert set(order) == EXPECTED_IDS


def test_graphml_is_deterministic_from_registry(documents):
    objects, sources = documents
    validate_registry(objects, sources)
    first = generate_graphml(objects)
    second = generate_graphml(copy.deepcopy(objects))
    assert first == second
    assert GRAPHML.read_text(encoding="utf-8") == first


def test_duplicate_id_fails_closed(documents):
    objects, sources = documents
    bad = copy.deepcopy(objects)
    bad[-1]["object_id"] = bad[0]["object_id"]
    with pytest.raises(RegistryError, match="duplicate object_id"):
        validate_registry(bad, sources)


def test_dangling_dependency_fails_closed(documents):
    objects, sources = documents
    bad = copy.deepcopy(objects)
    bad[1]["dependencies"].append("DG99")
    with pytest.raises(RegistryError, match="dangling dependencies"):
        validate_registry(bad, sources)


def test_cycle_fails_closed(documents):
    objects, sources = documents
    bad = copy.deepcopy(objects)
    by_id = {obj["object_id"]: obj for obj in bad}
    by_id["DG00"]["dependencies"] = ["DG43"]
    with pytest.raises(RegistryError, match="dependency cycle"):
        validate_registry(bad, sources)


def test_invalid_evidence_state_fails_closed(documents):
    objects, sources = documents
    bad = copy.deepcopy(objects)
    bad[0]["evidence_state"] = "VERIFIED_BY_ASSERTION"
    with pytest.raises(RegistryError, match="invalid evidence_state"):
        validate_registry(bad, sources)


def test_pr5_without_formal_artifact_fails_closed(documents):
    objects, sources = documents
    bad = copy.deepcopy(objects)
    bad[0]["proof_status"] = "PR5"
    bad[0]["formal_artifact_path"] = None
    with pytest.raises(RegistryError, match="PR5 requires"):
        validate_registry(bad, sources)


def test_unknown_source_fails_closed(documents):
    objects, sources = documents
    bad = copy.deepcopy(objects)
    bad[0]["source_locators"] = [
        {"source_id": "SRC-NOT-REGISTERED", "locator": "fabricated"}
    ]
    with pytest.raises(RegistryError, match="unknown source_id"):
        validate_registry(bad, sources)


def test_source_required_cannot_promote_to_source_grounded(documents):
    objects, sources = documents
    bad = copy.deepcopy(objects)
    by_id = {obj["object_id"]: obj for obj in bad}
    by_id["DG42"]["evidence_state"] = "S"
    with pytest.raises(RegistryError, match="SOURCE_REQUIRED may not support"):
        validate_registry(bad, sources)
