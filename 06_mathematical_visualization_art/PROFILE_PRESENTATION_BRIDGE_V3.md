# Profile Mathematical Presentation Bridge — V3

**Unique purpose of this module:** convert mathematically verified objects into scientifically interpretable visual representations without changing their epistemic status.

This document connects the Mathematics Research Ecosystem to the profile-wide presentation contract maintained in `Dossiya-SE/Dossiya-SE/mathematical-art/`.

## 1. Separation of responsibilities

```text
mathematics-foundations
    → defines mathematical objects
mathematical-models
    → declares modeling choices and admissible structures
mathematical-computing
    → implements algorithms
mathematical-verification
    → tests identities/invariants/numerics
mathematical-visualization-art
    → renders the already-defined objects
GitHub profile / portfolio
    → communicates the bounded result
```

Visualization is therefore downstream of mathematical definition and does not create mathematical validity.

## 2. Evidence states preserved in visuals

The profile uses:

- `[S]` source-grounded mathematics;
- `[D]` derived result;
- `[M]` model/abstraction;
- `[C]` computed output;
- `[V]` verified result;
- `[E]` empirical evidence;
- `[H]` hypothesis;
- `[T]` engineering/design target.

A renderer must not silently promote `[M]` to `[V]`, `[V]` to `[E]`, or `[H]` to established mathematics.

## 3. Source differential geometry

The Sochi source registered as `SOCHI-DG-2017-UPLOADED` provides the curve/surface differential-geometry basis used for source-grounded visual objects, including metric, connection, curvature, geodesics, Frenet–Serret frames, fundamental forms, topology/curvature relations, and tensor differentiation.

Representative source objects include

```math
g_{\alpha\beta}=\partial_\alpha\mathbf r\cdot\partial_\beta\mathbf r,
```

```math
\Gamma^\alpha_{\beta\gamma}
=\frac12g^{\alpha\delta}
\left(
\partial_\beta g_{\gamma\delta}
+\partial_\gamma g_{\beta\delta}
-\partial_\delta g_{\beta\gamma}
\right),
```

```math
K=\frac{eg-f^2}{EG-F^2},
```

and

```math
\frac{d^2u^\alpha}{ds^2}
+\Gamma^\alpha_{\beta\gamma}
\frac{du^\beta}{ds}
\frac{du^\gamma}{ds}=0.
```

These may be rendered directly as source mathematics.

## 4. Research-transfer boundary

For infrastructure research, the following implication is prohibited unless every intermediate object is formally defined:

```text
curved picture
→ manifold
→ metric
→ curvature
→ resilience indicator
```

The correct research progression is

```text
state space
→ differentiable structure (if justified)
→ metric/action definition
→ connection/curvature quantity
→ computable estimator
→ sensitivity/invariant tests
→ empirical/mechanistic interpretation
→ bounded resilience claim
```

Accordingly,

```math
\kappa[\gamma]
\stackrel{?}{\longrightarrow}
\text{trajectory fragility}
```

and

```math
K_{\partial\mathcal V}(x)
\stackrel{?}{\longrightarrow}
\text{viability-boundary fragility}
```

remain `[H]` until the research lab defines and validates them.

## 5. Visual encoding contract

| Visual primitive | Required mathematical meaning |
|---|---|
| point | declared state/sample/vertex |
| curve | parameterized trajectory/geodesic/frontier/fit |
| tangent arrow | derivative/tangent of a declared curve |
| normal/binormal | mathematically defined local frame |
| surface | parametric/implicit surface or declared feasible/viable set boundary |
| mesh | coordinate chart or discretization |
| contour | level set of a scalar field |
| color | scalar/category with legend |
| tube/band | explicitly constructed uncertainty/credible/confidence/scenario region |
| graph edge | declared relation/coupling, not presumed causality |
| arrow | mapping/flow/direction with stated semantics |

## 6. Preferred rendering stack

### Symbolic/formula derivation

`SymPy · Wolfram Language/Mathematica · SageMath`

### Numerical geometry

`NumPy/SciPy · Julia/DifferentialEquations.jl · Manifolds.jl`

### Scientific 3-D

`PyVista/VTK · Makie/GeometryBasics`

### Publication vector graphics

`LaTeX/TikZ/PGFPlots · Asymptote · SVG`

### High-end rendering / animation

`Blender Python API · Manim · WebGL/GLSL`

No tool is used merely to increase visual complexity. Tool choice is determined by mathematical object, reproducibility, publication target, and verification requirements.

## 7. Promotion ladder

```text
P0 conceptual
→ P1 formula-consistent
→ P2 numerically generated
→ P3 invariant-checked
→ P4 source-reproduced
→ P5 empirically validated
```

A P5-looking graphic can still be P0 if its geometry is not generated from a defined model.

## 8. Required metadata for stable visual artifacts

Every stable visualization should record:

```yaml
artifact_id:
mathematical_object:
evidence_state:
source_or_model:
parameter_domain:
units:
algorithm:
software_versions:
random_seed: null
numerical_tolerance: null
verification:
color_semantics:
limitations:
output_formats:
```

## 9. Profile integration

The public profile is the communication layer; this repository remains the mathematical provenance and reproducibility layer. Profile visuals should therefore link back to the appropriate mathematical source/model/test rather than duplicating derivations without provenance.

The central rule is:

```math
\boxed{
\text{mathematical truth/status}
\;\text{is invariant under}\;
\text{visual redesign}
}
```
