# Sochi 2017 — Reproduction Targets

**Unique purpose:** independently regenerate selected source results and quantify agreement. This module must not simply restate the source.

**Primary source:** Sochi (2017), *Introduction to Differential Geometry of Space Curves and Surfaces*.

## Reproduction contract

Every reproduction record must contain:

`source anchor -> independent derivation/implementation -> numerical or symbolic result -> error/invariant -> verdict -> limitations`.

A reproduced figure is generated from equations, never copied from the PDF.

## R1 — Helix curvature and torsion

Source anchor: Chapter 2, §2.3, printed p. 66.

For

\[
r(t)=(a\cos t,a\sin t,bt),
\]

reproduce

\[
\kappa=\frac{|a|}{a^2+b^2},
\qquad
\tau=\frac{b}{a^2+b^2}
\]

under the repository's orientation convention.

### Independent method

Compute `r'`, `r''`, `r'''`, then use source Eqs. (126) and (129). Compare symbolic simplification and numerical finite-sample checks.

### Acceptance

Relative error `<1e-12` for nondegenerate floating-point benchmarks and exact equality after symbolic simplification where assumptions are explicit.

## R2 — Torus metric and curvature

Source parameterization: §1.4.1, Eqs. (7)–(9), printed pp. 18–19.

For

\[
X(\theta,\phi)=((R+r\cos\phi)\cos\theta,(R+r\cos\phi)\sin\theta,r\sin\phi),
\]

reproduce

\[
E=(R+r\cos\phi)^2,\qquad F=0,\qquad G=r^2,
\]

then compute Gaussian curvature independently from the first/second fundamental forms and compare with the analytic benchmark already used by the bootstrap.

### Acceptance

- metric off-diagonal term numerically near zero;
- determinant positive for `R>r>0`;
- curvature sign positive at the outer equator and negative at the inner equator;
- analytic and numerical curvature agree to the chosen precision.

## R3 — Gauss–Bonnet on sphere and torus

Source anchor: §4.8, especially global Eq. (396), printed pp. 175–176.

\[
\iint_S K\,d\sigma=2\pi\chi.
\]

Benchmarks:

- sphere: `chi=2`, total curvature `4π`;
- torus: `chi=0`, total curvature `0`.

### Independent method

Numerically integrate `K dA` from independently implemented parameterizations. Report quadrature method, mesh size, convergence sequence, absolute error, and whether singular coordinate locations are handled correctly.

### Acceptance

The convergence study must demonstrate decreasing numerical error as resolution increases. A single lucky grid result is insufficient.

## R4 — Plane-to-cylinder intrinsic invariance

Source anchor: §4.7 Theorema Egregium discussion, printed p. 170.

The book uses rolling a plane into a cylinder to illustrate that principal/mean curvature can change while Gaussian curvature remains zero.

### Reproduction

Construct local parameterizations of a plane and circular cylinder with matching first fundamental forms and verify:

\[
K_{plane}=K_{cylinder}=0,
\]

while the cylinder has nonzero extrinsic curvature.

### Acceptance

Compare first fundamental form coefficients and computed Gaussian curvature; separately report second-form/mean-curvature differences.

## R5 — Catenoid minimality

Source anchor: Chapter 6 exercises 6.42–6.46; catenoid parameterization from §1.4.1, Eqs. (30)–(32).

Compute the first and second fundamental forms and verify

\[
H\approx0
\]

throughout a regular sampled domain, excluding numerical pathologies.

### Acceptance

Maximum sampled `|H|` must be reported together with mesh/domain and method. Symbolic confirmation is preferred.

## R6 — Catenoid/helicoid local isometry

Source anchor: Exercise 6.32.

The source asks the reader to show that catenoid and helicoid are locally isometric. This is a high-value reproduction because it tests parameter transformation and metric equality rather than visual similarity.

### Acceptance

Provide an explicit local coordinate map and demonstrate equality of pulled-back first fundamental forms. A 3-D overlay alone does not count.

## R7 — Geodesic equation invariants

Source anchor: §5.7, Eq. (418), printed pp. 204–205.

Integrate a geodesic on a benchmark surface and verify appropriate invariants, such as constant speed for an affine/natural parameter and conservation laws implied by cyclic coordinates when present.

### Caution

Sochi explicitly distinguishes geodesic character from globally shortest paths (§5.7, printed pp. 201–202). Reproduction reports must not equate the two without additional hypotheses.

## R8 — Tensor metric compatibility

Source anchor: Chapter 7, Eq. (441), printed p. 233.

For a nontrivial surface metric, independently compute the Levi-Civita connection and verify

\[
\nabla_\gamma a_{\alpha\beta}=0.
\]

This becomes a high-value symbolic regression test for the computing stack.

## Reproduction status vocabulary

- `planned`
- `source_checked`
- `implemented`
- `numerically_reproduced`
- `symbolically_reproduced`
- `cross_language_reproduced`
- `failed_with_explanation`

Failure is preserved as evidence and must not be deleted merely to make the repository appear successful.

## Citation

Sochi, T. (2017). *Introduction to Differential Geometry of Space Curves and Surfaces*. User-supplied PDF, internal preface date March 2017.
