"""Structural and mathematical-registry audit for the twelve-module ecosystem."""

from pathlib import Path

from validate_dg_registry import RegistryError, validate_repository_registry

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "01_mathematics_foundations",
    "02_mathematical_models",
    "03_mathematical_examples",
    "04_mathematical_reproductions",
    "05_mathematical_skills_development",
    "06_mathematical_visualization_art",
    "07_mathematical_computing",
    "08_mathematical_verification",
    "09_mathematical_physics",
    "10_mathematical_engineering_applications",
    "11_mathematics_literature_atlas",
    "12_mathematics_research_lab",
]

missing = [p for p in REQUIRED if not (ROOT / p).is_dir()]
if missing:
    raise SystemExit(f"Missing required modules: {missing}")

try:
    order = validate_repository_registry()
except (RegistryError, FileNotFoundError, ValueError) as exc:
    raise SystemExit(f"DG registry audit failed: {exc}") from exc

print("PASS: all 12 mathematics ecosystem modules are present.")
print(f"PASS: DG-DAG-001 validated with {len(order)} objects and deterministic GraphML.")
