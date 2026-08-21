# Mathematics Research Ecosystem — Bootstrap

<p align="center">
  <img src="assets/mathematics-ecosystem-v4.svg" width="100%" alt="Adaptive Mathematics Research Ecosystem architecture" />
</p>

This repository is the executable bootstrap and integration reference for the planned Dossiya-SE Mathematics Research Ecosystem.

It is intentionally organized as a monorepo prototype because the currently connected GitHub interface can modify repositories but cannot create or rename repositories or edit GitHub Projects v2. Each top-level module is designed so it can later be split into its own repository without changing its internal contract.

The top visual is a single adaptive SVG: it preserves mathematical content and evidence status while switching contrast and semantic color tokens with the viewer's light/dark system preference.

## Scientific pipeline

\[
\text{Learn} \rightarrow \text{Define} \rightarrow \text{Derive} \rightarrow \text{Model} \rightarrow \text{Implement} \rightarrow \text{Visualize} \rightarrow \text{Verify} \rightarrow \text{Reproduce} \rightarrow \text{Apply} \rightarrow \text{Research}
\]

## Modules

1. `01_mathematics_foundations/`
2. `02_mathematical_models/`
3. `03_mathematical_examples/`
4. `04_mathematical_reproductions/`
5. `05_mathematical_skills_development/`
6. `06_mathematical_visualization_art/`
7. `07_mathematical_computing/`
8. `08_mathematical_verification/`
9. `09_mathematical_physics/`
10. `10_mathematical_engineering_applications/`
11. `11_mathematics_literature_atlas/`
12. `12_mathematics_research_lab/`

## Primary differential-geometry foundation

The user-supplied book by **Taha Sochi, _Introduction to Differential Geometry of Space Curves and Surfaces_** (preface dated March 2017) is registered as source ID:

`SOCHI-DG-2017-UPLOADED`

It is used as a primary foundation for **curve/surface differential geometry**, not as a universal source for all mathematics, physics, or engineering. The source itself states that its preliminary mathematical background is not comprehensive.

### High-rigor source audit V2

The V2 source layer adds binary provenance for the current upload, a wider equation registry, explicit extraction/verification states, chapter-to-module coverage control, and a unique-purpose source artifact for every module:

- `sources/sochi_2017/SOURCE_AUDIT_V2.md`
- `sources/sochi_2017/source_manifest_v2.json`
- `sources/sochi_2017/equation_registry_v2.json`
- `sources/sochi_2017/COVERAGE_MATRIX_V2.md`
- `01_mathematics_foundations/sources/SOCHI_2017_UNIQUE_PURPOSE_V2.md`
- `02_mathematical_models/sources/SOCHI_2017_UNIQUE_PURPOSE_V2.md`
- `03_mathematical_examples/sources/SOCHI_2017_UNIQUE_PURPOSE_V2.md`
- `04_mathematical_reproductions/sources/SOCHI_2017_UNIQUE_PURPOSE_V2.md`
- `05_mathematical_skills_development/sources/SOCHI_2017_UNIQUE_PURPOSE_V2.md`
- `06_mathematical_visualization_art/sources/SOCHI_2017_UNIQUE_PURPOSE_V2.md`
- `07_mathematical_computing/sources/SOCHI_2017_UNIQUE_PURPOSE_V2.md`
- `08_mathematical_verification/sources/SOCHI_2017_UNIQUE_PURPOSE_V2.md`
- `09_mathematical_physics/sources/SOCHI_2017_UNIQUE_PURPOSE_V2.md`
- `10_mathematical_engineering_applications/sources/SOCHI_2017_UNIQUE_PURPOSE_V2.md`
- `11_mathematics_literature_atlas/sources/SOCHI_2017_UNIQUE_PURPOSE_V2.md`
- `12_mathematics_research_lab/sources/SOCHI_2017_UNIQUE_PURPOSE_V2.md`

The V2 rule is that the same source equation may enter several modules only when its **role changes**. Example: Gaussian curvature may be a canonical identity in Foundations, an observable in Models, a target in Reproductions, an oracle in Verification, and a scalar field in Visualization. The surrounding module artifact must remain purpose-specific rather than copied.

The legacy V1 extraction controls remain preserved in:

- `sources/sochi_2017/EXTRACTION_PROTOCOL.md`
- `sources/sochi_2017/source_manifest.json`

## Computing evidence stack

`07_mathematical_computing/COMPUTING_TOOLCHAIN.md` defines scientific roles and in-text scholarly/software citations for the principal computing systems used in the ecosystem, including NumPy, SciPy, SymPy, Matplotlib, PyVista/VTK, Julia, DifferentialEquations.jl, Manifolds.jl, SageMath, and Lean/mathlib. Specialized roles are also defined for Wolfram Language/Mathematica, MATLAB, LaTeX/TikZ, Asymptote, Blender, GLSL, Manim, C/C++, and CUDA.

The core rule is dual provenance:

\[
\boxed{\text{mathematical source citation} + \text{software citation}}
\]

for computational research outputs.

## Flagship demonstrator

Version 1 uses differential geometry as the common thread across all twelve modules:

- parametric surfaces and Riemannian metrics;
- Christoffel symbols and geodesics;
- Frenet–Serret frames;
- Gaussian curvature and Gauss–Bonnet checks;
- numerical simulation and symbolic verification;
- mathematical-art rendering;
- a coupled infrastructure viability example.

The Sochi V2 foundation adds broader source-grounded parameterizations, metric/shape compatibility controls, exercise-linked skill progression, reproduction targets, tensor-differentiation and Laplace-Beltrami oracles, and strict mathematics-to-physics/engineering evidence boundaries.

## Rigor contract

Every stable mathematical artifact should state: definition, domain, assumptions, derivation or provenance, units where applicable, implementation, tests, limitations, and references.

Source-grounded artifacts must additionally preserve section/page/equation or exercise anchors and explicitly distinguish **source mathematics** from **new applications or research hypotheses**.

See `GOVERNANCE.md`, `ARCHITECTURE.md`, `examples/FLAGSHIP_DEMONSTRATOR.md`, `sources/sochi_2017/EXTRACTION_PROTOCOL.md`, and `sources/sochi_2017/SOURCE_AUDIT_V2.md`.
