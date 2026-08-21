# Mathematics Research Ecosystem — Bootstrap

This repository is the executable bootstrap and integration reference for the planned Dossiya-SE Mathematics Research Ecosystem.

It is intentionally organized as a monorepo prototype because the currently connected GitHub interface can modify repositories but cannot create or rename repositories or edit GitHub Projects v2. Each top-level module is designed so it can later be split into its own repository without changing its internal contract.

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

The user-supplied book by **Taha Sochi, _Introduction to Differential Geometry of Space Curves and Surfaces_** (preface dated March 2017) is now registered as source ID:

`SOCHI-DG-2017-UPLOADED`

It is used as a primary foundation for **curve/surface differential geometry**, not as a universal source for all mathematics, physics, or engineering. The source itself states that its preliminary mathematical background is not comprehensive.

High-rigor extraction controls are in:

- `sources/sochi_2017/EXTRACTION_PROTOCOL.md`
- `sources/sochi_2017/source_manifest.json`

Each of the twelve modules contains a source-specific file with a unique transformation of the book: canonical foundations, model primitives, executable examples, reproduction targets, skill evidence, visual reconstruction, computing translation, verification oracles, geometric-physics bridges, engineering transfer rules, literature provenance, or research hypotheses.

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

The Sochi foundation extension adds source-grounded parameterizations, exercise-linked skill progression, reproduction targets, tensor-differentiation oracles, and cross-language computing governance.

## Rigor contract

Every stable mathematical artifact should state: definition, domain, assumptions, derivation or provenance, units where applicable, implementation, tests, limitations, and references.

Source-grounded artifacts must additionally preserve section/page/equation or exercise anchors and explicitly distinguish **source mathematics** from **new applications or research hypotheses**.

See `GOVERNANCE.md`, `ARCHITECTURE.md`, `examples/FLAGSHIP_DEMONSTRATOR.md`, and `sources/sochi_2017/EXTRACTION_PROTOCOL.md`.
