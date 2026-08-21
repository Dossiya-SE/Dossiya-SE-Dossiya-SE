# Sochi 2017 - Mathematical Computing Contract V2

**Unique purpose:** translate source equations into reproducible computational kernels and assign tools by scientific role. Mathematical authority comes from the source/derivation; software citations document the computational implementation.

## Citation principle

A computational result should cite both:

1. the mathematical source (Sochi equation/section or a later independent mathematical source), and
2. the software/method used to compute it.

For example, NumPy is the numerical array layer described by Harris et al. (2020), SciPy provides scientific numerical algorithms documented by Virtanen et al. (2020), SymPy provides symbolic mathematics described by Meurer et al. (2017), and Julia's numerical-computing design is documented by Bezanson et al. (2017). Full BibTeX records are in `../references.bib`.

## Kernel map

| Mathematical kernel | Source anchor | Preferred implementation roles |
|---|---|---|
| parameterized curves/surfaces | §1.4.1, Chs.2-3 | Python/NumPy, Julia |
| symbolic derivatives | throughout | SymPy, Wolfram Language, SageMath |
| metric/inverse metric | Eqs.193-194 | NumPy/SymPy/Julia |
| Christoffel symbols | Eq.63 | SymPy, Wolfram, Julia/Manifolds |
| Riemann/Ricci | Eqs.88-96 | symbolic tensor engine + numerical cross-check |
| Frenet frame | Eqs.126,129,136-139 | NumPy/SciPy, Julia |
| shape operator/eigenproblem | Eqs.223,343-346 | NumPy/SciPy/Julia |
| K and H | Eqs.355-383 | symbolic + numerical dual-route |
| geodesic IVP | Eq.418 | SciPy integrators, DifferentialEquations.jl |
| covariant derivatives | Ch.7 | SymPy/Wolfram/Julia/Manifolds |
| divergence/Laplace-Beltrami | Eqs.474-475 | symbolic generation + PDE/numerical backends |
| 3D mesh rendering | source parametric geometry | PyVista/VTK, Makie, Blender |
| publication graphics | source concepts | Matplotlib, TikZ/PGFPlots, Asymptote |
| formal theorem checks | selected identities | Lean/mathlib where practical |

## Scientifically cited core tools

### NumPy
Use for dense numerical arrays, vectorized coordinate evaluation, tensor-component storage, linear algebra inputs, and deterministic sampling. Scientific citation: Harris et al. (2020), *Nature*, DOI `10.1038/s41586-020-2649-2`.

### SciPy
Use for ODE/geodesic integration, numerical quadrature, optimization, interpolation, sparse operations, and eigenvalue routines where appropriate. Scientific citation: Virtanen et al. (2020), *Nature Methods*, DOI `10.1038/s41592-019-0686-2`.

### SymPy
Use for exact differentiation of parameterizations and metrics, symbolic Christoffel/curvature derivations, simplification, and generation of independent closed-form oracles. Scientific citation: Meurer et al. (2017), *PeerJ Computer Science*, DOI `10.7717/peerj-cs.103`.

### Matplotlib
Use for conventional publication-quality 2D figures, convergence plots, residual plots, and compact 3D diagnostic figures. Scientific citation: Hunter (2007), *Computing in Science & Engineering*, DOI `10.1109/MCSE.2007.55`.

### PyVista / VTK
Use for triangulated/manifold surface visualization, mesh interrogation, scalar-field rendering, glyphs, slicing, and high-density scientific 3D. PyVista citation: Sullivan & Kaszynski (2019), JOSS, DOI `10.21105/joss.01450`. VTK is recorded through Schroeder, Martin & Lorensen's reference text in `references.bib`.

### Julia
Use for performant generic numerical mathematics, high-order simulations, and cross-language reproduction. Scientific citation: Bezanson et al. (2017), *SIAM Review*, DOI `10.1137/141000671`.

### DifferentialEquations.jl
Use for geodesic systems, moving frames, nonlinear ODE/PDE experiments, event handling, and solver-comparison studies. Scientific citation: Rackauckas & Nie (2017), *Journal of Open Research Software*, DOI `10.5334/jors.151`.

### Manifolds.jl
Use when the computational object should remain manifold-native rather than embedded-array-only: manifold points, tangent vectors, retractions, distances, and higher-dimensional generalization. Scientific citation: Axen et al. (2023), *ACM Transactions on Mathematical Software*, DOI `10.1145/3618296`.

### Lean / mathlib
Use for formal proofs of selected algebraic/tensor identities and theorem dependencies where formalization cost is justified. Lean: de Moura et al. (2015), DOI `10.1007/978-3-319-21401-6_26`; mathlib: the mathlib Community (2020), DOI `10.1145/3372885.3373824`.

### SageMath
Use as an open mathematical integration environment for symbolic algebra, calculus, geometry, topology experiments, and cross-checking other CAS outputs. The repository records the SageMath all-versions Zenodo DOI and requires the exact version-specific DOI for publication-grade reproduction.

## Specialized tool roles

The following tools are useful but their inclusion does not replace source verification:

- **Wolfram Language / Mathematica**: symbolic tensor calculus, exact differential geometry, high-level parametric/implicit graphics;
- **MATLAB**: engineering numerical workflows, matrix calculus, PDE/control integration;
- **TikZ/PGFPlots**: exact vector typography and publication diagrams;
- **Asymptote**: mathematically specified 2D/3D vector geometry;
- **Blender + Python**: high-end rendering after geometry and fields are verified;
- **GLSL/OpenGL/WebGL**: GPU scalar/vector/tensor-field rendering and interactive surfaces;
- **Manim**: equation/geometry animations;
- **C/C++**: performance-critical kernels and library integration;
- **CUDA**: large GPU-parallel sampling/field computation when profiling demonstrates need.

## Source-to-code workflow

```text
source equation
 -> transcribe with domain assumptions
 -> rendered-page check
 -> symbolic reference implementation
 -> independent numerical implementation
 -> unit/invariant tests
 -> convergence tests
 -> cross-language implementation when valuable
 -> version-locked environment
 -> reproducible artifact
```

## Numerical safeguards

1. Test `EG-F^2` before metric inversion.
2. Test curve speed before tangent normalization.
3. Test `|r_dot x r_ddot|` before torsion evaluation.
4. Detect coordinate singularities separately from geometric singularities.
5. Use scale-aware tolerances rather than universal magic constants.
6. Report conditioning for eigenproblems near umbilical points.
7. Report mesh/quadrature refinement for Gauss-Bonnet integrations.
8. Keep symbolic and numerical routes independent when one is used to verify the other.

## Reproducibility metadata

Every computational artifact should record:

```yaml
source_id: SOCHI-DG-2017-UPLOADED
source_equations: []
language: ...
runtime_version: ...
packages:
  package: version
floating_point: ...
solver: ...
tolerances: ...
random_seed: null
hardware_relevance: none | cpu | gpu
verification_tests: []
output_hashes: []
```

The software bibliography is maintained in `07_mathematical_computing/references.bib`; arbitrary package names are not treated as scientific citations.
