# Mathematics Computing Toolchain and Scientific Roles

This file defines **roles**, not brand preferences. A tool enters the core stack only when its mathematical purpose, reproducibility role, and citation can be stated clearly.

The differential-geometry source layer is Sochi (2017). Computing tools are cited independently because software capability must not be attributed to the mathematics textbook.

## Core stack

### Python + NumPy — numerical representation layer

**Role:** vectors, matrices, multidimensional sampled fields, parameter grids, numerical geometry arrays, and interoperability across the scientific Python stack.

NumPy is the primary array-programming foundation of scientific Python and is appropriate for evaluating parameterized curves/surfaces over dense grids and storing metric, curvature, and trajectory arrays (Harris et al., 2020, DOI: `10.1038/s41586-020-2649-2`).

**Use here:**

- evaluate `X(u,v)` and `r(t)`;
- vectorized tangent/normal calculations;
- sampled scalar/tensor fields;
- numerical comparison between implementations.

### SciPy — numerical algorithms layer

**Role:** integration, optimization, interpolation, algebraic equations, sparse structures, and differential-equation support. SciPy provides foundational numerical algorithms on top of NumPy (Virtanen et al., 2020, DOI: `10.1038/s41592-019-0686-2`).

**Use here:**

- quadrature for arc length, area, and curvature integrals;
- ODE solution for geodesics/Frenet systems when solver sophistication is needed;
- root solving for geometric constraints;
- optimization for closest-point or inverse-parameter problems.

### SymPy — symbolic mathematics layer

**Role:** exact differentiation, algebraic simplification, symbolic matrices, tensor-related manipulations, and exact verification. SymPy is an open-source computer algebra system designed for symbolic computing in Python (Meurer et al., 2017, DOI: `10.7717/peerj-cs.103`).

**Use here:**

- derive `X_u`, `X_v`, `g_ij`, and Christoffel symbols;
- simplify helix curvature/torsion formulas;
- verify `∇g=0` symbolically;
- derive analytic curvature expressions before numerical rendering.

### Matplotlib — publication plotting layer

**Role:** reproducible 2-D and conventional 3-D scientific figures, diagnostics, convergence plots, and publication-quality static outputs. Hunter (2007) describes Matplotlib as a scientific graphics environment and its project recommends this citation (DOI: `10.1109/MCSE.2007.55`).

**Use here:**

- convergence/error plots;
- curve diagnostics;
- curvature profiles;
- reproducible static figures where full VTK rendering is unnecessary.

### PyVista + VTK — scientific 3-D geometry/mesh layer

**Role:** mesh construction, 3-D scalar/vector field visualization, geometric interrogation, and scientific rendering. PyVista provides a streamlined Python interface to VTK for 3-D plotting and mesh analysis (Sullivan & Kaszynski, 2019, DOI: `10.21105/joss.01450`). VTK's official scientific citation is Schroeder, Martin, and Lorensen (2006), *The Visualization Toolkit*, 4th ed., ISBN `978-1-930934-19-1`.

**Use here:**

- curvature-colored surfaces;
- coordinate grids and normals;
- tangent planes and Frenet frames;
- mesh-quality checks;
- interactive inspection before publication rendering.

### Julia — high-performance scientific language layer

**Role:** high-level mathematical code with performance-oriented multiple dispatch, generic programming, parallel/scientific computing, and reusable numerical abstractions. Bezanson et al. (2017) present Julia as a language designed to combine high-level expressiveness with high performance (SIAM Review, DOI: `10.1137/141000671`).

**Use here:**

- large geodesic ensembles;
- parameter sweeps;
- nonlinear dynamical systems;
- high-performance cross-language reproduction.

### DifferentialEquations.jl — differential-equation solver layer

**Role:** broad differential-equation ecosystem for ODEs, SDEs, DDEs, DAEs, jump systems, and PDE-related workflows. Rackauckas and Nie (2017) describe the Julia ecosystem and unified solver interface (DOI: `10.5334/jors.151`).

**Use here:**

- geodesic initial-value problems;
- Frenet–Serret ODEs;
- geometric mechanics extensions;
- stiff or event-driven research models where a basic RK method is inadequate.

### Manifolds.jl — manifold-native computation layer

**Role:** computational operations directly on Riemannian manifolds and Lie groups. Axen et al. (2023) describe Manifolds.jl as an extensible Julia framework for manifold data analysis (ACM TOMS 49(4), Article 33, DOI: `10.1145/3618296`).

**Use here:**

- manifold-aware distances and exponential/logarithmic maps;
- Riemannian optimization experiments;
- cross-checking custom differential-geometry implementations;
- future higher-dimensional extensions beyond embedded surfaces.

### SageMath — integrated open-source mathematics layer

**Role:** integrated mathematical experimentation across algebra, calculus, number theory, geometry, graph theory, and related areas. SageMath identifies itself as a free open-source mathematics software system and supplies versioned software citations through Zenodo; the all-versions DOI is `10.5281/zenodo.8042260`.

**Use here:**

- independent computer-algebra cross-checks;
- access to specialist algebraic/topological packages;
- educational derivations and exact computations outside the Python-only path.

### Lean + mathlib — formal verification layer

**Role:** machine-checked theorem proving based on dependent type theory. Lean was introduced as an interactive/automated theorem prover by de Moura et al. (2015, CADE-25, DOI: `10.1007/978-3-319-21401-6_26`). The Lean mathematical library provides a large formalized mathematics ecosystem (mathlib Community, 2020, DOI: `10.1145/3372885.3373824`).

**Use here:**

- formalize stable definitions/theorems after ordinary derivation and testing;
- verify algebraic identities and hypotheses at theorem level;
- separate numerical evidence from formal proof.

## Secondary/specialized stack

### Wolfram Language / Mathematica

**Role:** symbolic tensor manipulation, exact differential geometry, high-level parametric visualization, and independent CAS reproduction.

**Governance:** use as a second symbolic engine, not as an opaque source of truth. Export assumptions and exact expressions; cite the exact software/version used in publication outputs.

### MATLAB

**Role:** engineering-oriented numerical linear algebra, ODE/PDE workflows, matrix computation, and comparison with established engineering code.

**Governance:** preserve script/toolbox version information and do not mix toolbox-specific results with base-language claims.

### LaTeX + TikZ/PGFPlots

**Role:** publication typography, exact annotated diagrams, vector output, equation-consistent labels, architecture drawings, and final PDF/SVG figure assembly.

### Asymptote

**Role:** coordinate-driven mathematical vector graphics and 3-D technical illustrations with LaTeX-quality typesetting. Use when precise geometry/annotation is more important than interactive mesh analysis.

### Blender + Python

**Role:** high-end 3-D rendering and animation **after** geometry and fields are generated/verified scientifically. Blender is a rendering layer, not the verification layer.

### GLSL / GPU shaders

**Role:** real-time evaluation/encoding of scalar and vector fields at very high visual resolution. Use for interactive curvature/field art after CPU reference calculations establish correctness.

### Manim

**Role:** mathematical animation of derivations, moving frames, geodesics, parallel transport, and theorem demonstrations. Animation timing must not alter mathematical meaning.

### C/C++ and CUDA

**Role:** performance-critical kernels, custom meshing, large parameter sweeps, and GPU acceleration when profiling shows Python/Julia pathways are insufficient.

## Tool-selection matrix

| Mathematical task | Primary | Independent check | Visualization |
|---|---|---|---|
| exact derivatives | SymPy | Wolfram/SageMath | — |
| metric/Christoffel derivation | SymPy | Wolfram/Manifolds.jl | TikZ/PyVista |
| geodesic ODE | SciPy or DifferentialEquations.jl | independent solver / invariant | PyVista/Makie/Manim |
| Gauss–Bonnet integral | SciPy/Julia quadrature | topology + symbolic special cases | Matplotlib/PyVista |
| surface mesh inspection | PyVista/VTK | analytic parameterization | PyVista |
| theorem proof | Lean/mathlib | conventional derivation | LaTeX |
| cinematic surface art | Blender/GLSL | CPU reference geometry | Blender/GLSL |

## Reproducibility rule

A scientific result must cite both:

1. the **mathematical source** used for the formula/theorem, e.g. `(Sochi, 2017, §5.7, Eq. 418)`; and
2. the **computational software** materially used to obtain the result, using its recommended scholarly/software citation.

A result is not considered independently reproduced merely because two packages call the same underlying library.

## References

Axen, S. D., Baran, M., Bergmann, R., & Rzecki, K. (2023). Manifolds.jl: An Extensible Julia Framework for Data Analysis on Manifolds. *ACM Transactions on Mathematical Software, 49*(4), Article 33. https://doi.org/10.1145/3618296

Bezanson, J., Edelman, A., Karpinski, S., & Shah, V. B. (2017). Julia: A Fresh Approach to Numerical Computing. *SIAM Review, 59*(1), 65–98. https://doi.org/10.1137/141000671

de Moura, L., Kong, S., Avigad, J., van Doorn, F., & von Raumer, J. (2015). The Lean Theorem Prover (System Description). In *Automated Deduction – CADE-25*, 378–388. https://doi.org/10.1007/978-3-319-21401-6_26

Harris, C. R., Millman, K. J., van der Walt, S. J., et al. (2020). Array programming with NumPy. *Nature, 585*, 357–362. https://doi.org/10.1038/s41586-020-2649-2

Hunter, J. D. (2007). Matplotlib: A 2D Graphics Environment. *Computing in Science & Engineering, 9*(3), 90–95. https://doi.org/10.1109/MCSE.2007.55

Meurer, A., Smith, C. P., Paprocki, M., et al. (2017). SymPy: symbolic computing in Python. *PeerJ Computer Science, 3*, e103. https://doi.org/10.7717/peerj-cs.103

Rackauckas, C., & Nie, Q. (2017). DifferentialEquations.jl – A Performant and Feature-Rich Ecosystem for Solving Differential Equations in Julia. *Journal of Open Research Software, 5*(1). https://doi.org/10.5334/jors.151

Schroeder, W., Martin, K., & Lorensen, B. (2006). *The Visualization Toolkit* (4th ed.). Kitware. ISBN 978-1-930934-19-1.

Sullivan, C. B., & Kaszynski, A. A. (2019). PyVista: 3D plotting and mesh analysis through a streamlined interface for the Visualization Toolkit (VTK). *Journal of Open Source Software, 4*(37), 1450. https://doi.org/10.21105/joss.01450

The mathlib Community. (2020). The Lean Mathematical Library. *Proceedings of CPP 2020*, 367–381. https://doi.org/10.1145/3372885.3373824

Virtanen, P., Gommers, R., Oliphant, T. E., et al. (2020). SciPy 1.0: fundamental algorithms for scientific computing in Python. *Nature Methods, 17*, 261–272. https://doi.org/10.1038/s41592-019-0686-2

The SageMath Developers. *SageMath*. All-versions software DOI: https://doi.org/10.5281/zenodo.8042260

Sochi, T. (2017). *Introduction to Differential Geometry of Space Curves and Surfaces*. User-supplied PDF; internal preface date March 2017.
