# Sochi 2017 - Verification Oracle Matrix V2

**Unique purpose:** challenge source-derived and implemented mathematics using independent analytic, numerical, invariance, topology, and formal checks. Verification is distinct from extraction and from reproduction.

## Four-gate policy

```text
V0 source anchor
V1 mathematical domain/regularity
V2 independent invariant or derivation
V3 executable numerical/formal check
```

A plotting success is never a verification gate.

## Oracle matrix

| Artifact | Required oracle(s) | Failure meaning |
|---|---|---|
| curve parameterization | independent implicit/geometric relation | transcription/domain error |
| tangent/Frenet frame | unit norms, orthogonality, handedness | derivative/normalization error |
| curvature/torsion | analytic benchmark + reparameterization check | formula/convention error |
| surface chart | rank 2; `EG-F^2>0` | chart singularity or invalid surface point |
| metric inverse | `a^αγ a_γβ=δ^α_β` | inversion/index error |
| Christoffel | lower-index symmetry + metric compatibility | connection implementation error |
| Riemann tensor | tensor symmetries + flat-space zero | curvature implementation error |
| shape operator | eigenvalue invariants | metric/curvature tensor mismatch |
| Gaussian curvature | intrinsic/extrinsic dual-route agreement | sign/index/derivative error |
| mean curvature | principal-curvature sum + normal reversal | orientation/sign error |
| Gauss-Weingarten | tangent/normal decomposition residual | basis derivative error |
| Codazzi-Mainardi | compatibility residual | non-realizable or miscomputed forms |
| geodesic | ODE residual + metric-speed drift | solver/connection/chart error |
| Gauss-Bonnet | integrated K vs `2*pi*chi` + convergence | geometry/quadrature/topology error |
| divergence/Laplacian | known analytic field benchmark | differential-operator error |

## Curve invariants

At each valid Frenet point:

$$
T\cdot N=T\cdot B=N\cdot B=0,
\quad
\|T\|=\|N\|=\|B\|=1,
\quad
T\times N=B
$$

under the source's right-handed convention.

For a helix use the analytic `kappa,tau` values as oracles. For a planar curve verify `tau=0` away from degenerate points.

## Surface regularity

For a chart `r(u,v)` verify both equivalent conditions numerically:

$$
\|E_1\times E_2\|>0,
\qquad
\det(a_{\alpha\beta})=EG-F^2>0.
$$

Near zero, report conditioning instead of converting a coordinate singularity into a false geometric statement.

## Metric/connection verification

Verify:

$$
a^{\alpha\gamma}a_{\gamma\beta}=\delta^\alpha_\beta
$$

and metric compatibility from Chapter 7. A Christoffel implementation derived from a symbolic metric should also be cross-checked at sampled points with finite differences or a second CAS/library where feasible.

## Curvature verification

Gaussian curvature should be compared by independent routes:

$$
K=\frac{eg-f^2}{EG-F^2},
\qquad
K=\det(b^\alpha{}_{\beta}),
\qquad
K=\frac{R_{1212}}{a}.
$$

Mean curvature should satisfy:

$$
H=\frac12(\kappa_1+\kappa_2)
=\frac12\operatorname{tr}(b^\alpha{}_{\beta}).
$$

Normal reversal oracle:

```text
n -> -n
b -> -b
kappa_1,kappa_2 -> negatives
H -> -H
K -> K
```

## Compatibility verification

The source's Codazzi-Mainardi equation

$$
b_{\alpha\beta;\gamma}=b_{\alpha\gamma;\beta}
$$

is an executable residual oracle. Gauss-Codazzi should also be checked when reconstructing a surface from fundamental-form data.

## Topological verification

For compact orientable benchmark surfaces:

$$
R_{GB}=\left|\iint_S K\,dA-2\pi\chi\right|.
$$

Report `R_GB` under increasing quadrature/mesh resolution. One low residual at one resolution is insufficient evidence of convergence.

## Geodesic verification

For integrated state `(u^alpha,v^alpha)`:

$$
R^\alpha_g
=\dot v^\alpha+\Gamma^\alpha_{\beta\gamma}v^\beta v^\gamma.
$$

Also monitor metric speed

$$
q(s)=a_{\alpha\beta}v^\alpha v^\beta.
$$

For arc-length parameterization, `q` should remain approximately 1; for affine parameterization it should remain constant under the relevant assumptions.

## Differential-operator verification

For Eq. (474) divergence and Eq. (475) Laplace-Beltrami:

- plane Cartesian chart must reduce to the familiar Euclidean expressions;
- known spherical eigenfunctions provide later high-value checks;
- coordinate transformations should not alter scalar Laplace-Beltrami results at corresponding points.

## Current automated scope

`tests/test_sochi_source_examples.py` and `tests/test_sochi_v2_examples.py` implement deterministic source-geometry checks. Future gates should add symbolic metric/connection tests, curvature dual-route tests, Gauss-Codazzi residuals, and surface-PDE operator benchmarks.

## Formal verification

Lean/mathlib is reserved for identities whose value justifies formalization, e.g. finite-dimensional algebraic invariants, matrix identities, or theorem dependency checks. Formal proof complements but does not replace floating-point convergence tests for numerical algorithms.
