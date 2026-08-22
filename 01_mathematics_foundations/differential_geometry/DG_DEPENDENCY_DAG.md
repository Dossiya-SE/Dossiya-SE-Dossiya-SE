# DG-DAG-001 — Differential-geometry dependency registry

**Protocol:** `DOSSYA_MRX_BENCHMARKED_100K_V2`  
**Status:** ontology/dependency skeleton, not a claim that all 44 objects are fully proved or implemented.

## Purpose

The registry makes the dependency structure of the differential-geometry programme machine-checkable before deeper implementation. Numeric IDs are stable identifiers, **not** a teaching order and not a claim that dependencies must follow numeric order.

The first nontrivial example is deliberate:

```text
topological manifold
→ charts / atlas
→ smooth structure
```

Therefore `DG03 → DG02` is legitimate even though `03 > 02`.

## Machine-readable artifacts

- `mathematical_registry/dg_objects.jsonl` — exactly one record for each `DG00` through `DG43`;
- `mathematical_registry/source_families.json` — source families plus access/authority boundaries;
- `mathematical_registry/dg_dependencies.graphml` — deterministic directed dependency graph;
- `scripts/validate_dg_registry.py` — fail-closed validator and GraphML generator;
- `08_mathematical_verification/tests/test_dg_registry.py` — positive and adversarial tests.

## Evidence and proof states

Evidence states are restricted to:

`S D M C V R E P H T`

Proof status is restricted to:

`PR0 PR1 PR2 PR3 PR4 PR5`.

`PR5` is rejected unless a formal artifact path is present.

Registry membership does not imply proof completion. Most objects remain `PR1/P1`. `DG12` (Levi-Civita connection) is the current reference object with `PR2/P3` status under its declared benchmark scope.

## Current dependency spine

```text
DG00 Foundations
  ↓
DG01 Topological manifolds
  ↓
DG03 Charts and atlases
  ↓
DG02 Smooth structures
  ↓
DG04 Tangent spaces
  ├─→ DG05 Cotangent spaces
  ├─→ DG06 Vector fields
  └─→ DG07 Tensor algebra
          ├─→ DG08 Differential forms → DG09 Exterior derivative
          └─→ DG11 Riemannian metrics
                  ↓
              DG13 Covariant derivative
                  ↓
              DG12 Levi-Civita connection
                  ├─→ DG15 Geodesics → DG16 Exponential map
                  ├─→ DG14 Parallel transport
                  └─→ DG18 Riemann tensor
                         ├─→ DG19 Sectional curvature
                         ├─→ DG20 Ricci → DG21 Scalar curvature
                         └─→ DG22 Jacobi fields → DG23 Conjugate points
```

The embedded-surface branch proceeds through `DG26` immersion/embedding, first and second fundamental forms, shape operator, principal curvatures, Gaussian/mean curvature, Gauss/Codazzi, Theorema Egregium, Gauss–Bonnet and minimal surfaces.

`DG41` and `DG42` intentionally distinguish smooth level-set geometry from nonsmooth geometry. `DG42` remains `SOURCE_REQUIRED` and cannot be promoted to `[S]` until an exact authoritative nonsmooth-analysis source is registered.

## Source policy

The source registry distinguishes theorem sources from software-architecture benchmarks.

- Lee's smooth/Riemannian manifold books are authoritative bibliographic families; exact theorem/page locators remain required before `PR2+`.
- Sternberg and MIT 18.966 provide open derivation anchors already used by `DG-LC-001`.
- the repository-controlled Sochi source provides verified curve/surface equation locators where frozen;
- Crane's CMU DDG notes anchor numerical/discrete geometry;
- Geomstats and Manifolds.jl documentation are **Tier D software references**, not sole theorem authorities.

## Fail-closed conditions

CI fails on:

- missing or duplicate `DG00`–`DG43` IDs;
- dangling dependencies;
- dependency cycles;
- duplicate dependencies;
- invalid evidence/proof/maturity states;
- unregistered source IDs;
- unsupported `SOURCE_REQUIRED → [S]` promotion;
- `PR5` without a formal artifact;
- committed GraphML differing from deterministic registry generation.

## Scope boundary

An acyclic dependency graph does not establish theorem correctness. It establishes only that the programme's declared mathematical objects form a syntactically consistent, source-aware dependency skeleton. Each object must still earn proof, implementation, verification, reproduction, and validation maturity independently.
