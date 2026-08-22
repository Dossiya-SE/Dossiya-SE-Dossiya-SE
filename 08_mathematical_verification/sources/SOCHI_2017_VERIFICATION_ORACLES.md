# Sochi 2017 — Verification Oracles

**Unique purpose:** define analytic, invariant, topological, dimensional, and numerical checks for source-derived mathematics. This module does not define the mathematics (module 01) or the reproduction targets (module 04); it decides whether implementations satisfy them.

## Oracle classes

### O1 — domain and regularity

A curve quantity requiring `r' != 0` must fail or return an explicit undefined state at nonregular points. A surface quantity requiring a regular patch must guard

$$
\|X_u\times X_v\|>0.
$$

Source anchors: Sochi (2017), §§1.4.3, 2.1.

### O2 — frame orthonormality

For the Frenet frame where defined:

$$
T\cdot T=N\cdot N=B\cdot B=1,
$$

$$
T\cdot N=T\cdot B=N\cdot B=0,
$$

and under the source orientation convention

$$
B=T\times N.
$$

Source anchor: Sochi (2017), Eqs. (113), (115)–(117), printed pp. 62–63.

### O3 — Frenet–Serret structure

The coefficient matrix in Sochi Eq. (139) is skew-symmetric. A numerical integrator should therefore preserve frame orthonormality to within integration error; large drift is a diagnostic.

### O4 — metric symmetry and positive definiteness

For a regular Riemannian surface patch,

$$
g_{12}=g_{21},\qquad \det g=EG-F^2>0.
$$

The determinant is also tied to the squared area density. A negative determinant signals a derivation/implementation error for the Euclidean embedded surfaces considered here.

### O5 — Christoffel lower-index symmetry

For the Levi-Civita connection used in the source:

$$
\Gamma^k_{ij}=\Gamma^k_{ji}.
$$

Source anchor: Sochi Eq. (66).

### O6 — metric compatibility

Chapter 7 requires

$$
\nabla_\gamma g_{\alpha\beta}=0.
$$

Source anchor: Sochi Eq. (441). This is a strong symbolic oracle for any Christoffel implementation.

### O7 — intrinsic-flatness tests

The source states that intrinsic flatness is characterized by vanishing Riemann-Christoffel curvature. For 2-D surfaces, vanishing Gaussian curvature is the corresponding scalar criterion.

Use benchmark cases:

- plane: `K=0`;
- cylinder: `K=0` intrinsically while extrinsic curvature is nonzero;
- sphere radius `R`: `K=1/R^2`;
- standard torus: `K` changes sign between outer and inner regions.

Source anchors: Sochi §§1.4.6 and 4.7.

### O8 — topology/curvature consistency

For compact orientable closed benchmark surfaces satisfying the theorem hypotheses:

$$
\iint_S K\,d\sigma=2\pi\chi.
$$

Source anchor: Sochi Eq. (396), printed p. 175.

Benchmarks:

- sphere: `chi=2`, integral `4π`;
- torus: `chi=0`, integral `0`.

### O9 — geodesic invariants

For an affine/natural parameter, check constant metric speed where appropriate:

$$
E_g=g_{ij}\dot u^i\dot u^j.
$$

If a coordinate is cyclic in the metric, test the corresponding conserved momentum. Do not use Euclidean straightness as the oracle on a curved surface.

Source anchor: Sochi §5.7, Eq. (418).

### O10 — minimal-surface oracle

For regular patches represented with a declared orientation, a minimal surface satisfies

$$
H=0.
$$

Source anchor: Sochi Chapter 6, §6.7 and Exercises 6.42–6.46.

Benchmark candidates from the book include catenoid/helicoid-related tasks. Numerical verification must report domain and residual, not simply render the shape.

## Error reporting

Every numerical verification record must report:

- absolute error;
- relative error where meaningful;
- tolerance and reason for tolerance;
- resolution / step size;
- convergence evidence for integral/differential approximations;
- whether comparison is against an exact theorem, analytic benchmark, or second software implementation.

## Cross-software independence

Two outputs are not independent if they share the same low-level algorithm/library without disclosure. For example, a PyVista result and a VTK result may share the VTK backend. Prefer symbolic-vs-numerical, Python-vs-Julia, or topology-vs-quadrature checks for stronger independence.

## Citation

Sochi, T. (2017). *Introduction to Differential Geometry of Space Curves and Surfaces*. User-supplied PDF; internal preface date March 2017.
