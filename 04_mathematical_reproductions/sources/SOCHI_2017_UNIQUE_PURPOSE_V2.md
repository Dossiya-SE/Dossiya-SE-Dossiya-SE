# Sochi 2017 - Reproduction Program V2

**Unique purpose:** independently regenerate mathematical results from source equations and report quantitative agreement. This module does not merely restate source formulas.

## Reproduction principle

A reproduction is accepted only when the result is computed from a declared implementation and compared against an **independent oracle**. Reusing the same algebra twice is not an independent reproduction.

General error measures:

\[
E_{abs}=|\hat y-y_*|,
\qquad
E_{rel}=\frac{|\hat y-y_*|}{\max(|y_*|,\epsilon)}.
\]

For vector/tensor outputs use a declared norm. For trajectories use residual, invariant drift, and/or endpoint error.

## R1 - Parametric geometry identities

Regenerate the source prototypes and verify implicit relations:

- torus;
- ellipsoid;
- one- and two-sheet hyperboloids;
- elliptic/hyperbolic paraboloids;
- parabolic cylinder;
- catenoid;
- selected special surfaces.

Acceptance: residual below a scale-aware floating-point tolerance at deterministic and randomized parameter samples.

## R2 - Circular helix curvature and torsion

For

\[
r(t)=(a\cos t,a\sin t,bt),
\]

compute `kappa` and `tau` from derivative definitions (Sochi Eqs. 126 and 129), then compare with the closed forms

\[
\kappa=\frac{|a|}{a^2+b^2},
\qquad
\tau=\frac{b}{a^2+b^2}.
\]

The implementation computing derivatives must not call the closed-form oracle.

## R3 - Frenet-Serret frame

Numerically or symbolically construct `T,N,B` for a regular curve and check:

\[
T\cdot N=T\cdot B=N\cdot B=0,
\]

\[
\|T\|=\|N\|=\|B\|=1,
\]

plus residuals of Eqs. (136)-(138). Record the torsion sign convention.

## R4 - Metric and inverse metric

For a parametric surface compute

\[
a_{\alpha\beta}=E_\alpha\cdot E_\beta
\]

and verify

\[
a^{\alpha\gamma}a_{\gamma\beta}=\delta^\alpha_\beta.
\]

Also check positive definiteness away from singular points.

## R5 - Connection and metric compatibility

Construct Christoffel symbols from the metric (Eq. 63) and verify symmetry of the Levi-Civita lower indices and metric compatibility from Chapter 7.

Useful benchmark surfaces: plane, sphere, cylinder, torus.

## R6 - Gaussian curvature by independent routes

At the same points compute `K` using at least two independent routes, e.g.:

1. second fundamental form:
   \[
   K=(eg-f^2)/(EG-F^2);
   \]
2. shape-operator determinant;
3. intrinsic Riemann tensor route;
4. metric-only expression where numerically stable.

Agreement is required within a declared tolerance.

## R7 - Principal curvatures and mean curvature

Solve the generalized eigenproblem of Eq. (346), then verify

\[
\kappa_1+\kappa_2=2H,
\qquad
\kappa_1\kappa_2=K.
\]

Under normal reversal, verify `kappa_i -> -kappa_i`, `H -> -H`, while `K` is unchanged.

## R8 - Gauss-Codazzi compatibility

For analytic benchmark surfaces compute residuals of the Gauss and Codazzi-Mainardi equations. This is the compatibility gate before treating arbitrary first/second fundamental-form data as a realizable surface.

## R9 - Theorema Egregium benchmark

Construct an explicit local isometry between a plane strip and circular cylinder. Verify preservation of the first fundamental form and `K=0`, while the second fundamental form/mean curvature changes.

This reproduction demonstrates intrinsic versus extrinsic geometry without relying on visual similarity.

## R10 - Global Gauss-Bonnet

Numerically integrate `K dA` and compare with the topological oracle:

\[
\iint_S K\,dA=2\pi\chi.
\]

Minimum benchmarks:

- sphere: `chi=2`, target `4*pi`;
- torus: `chi=0`, target `0`;
- ellipsoid: same Euler characteristic as sphere, target `4*pi`.

Report mesh/quadrature resolution and convergence, not only a single result.

## R11 - Geodesic integration

Integrate Eq. (418) as an IVP and report:

- equation residual;
- metric-speed drift;
- chart-domain violations;
- convergence under step refinement.

For known cases, compare with analytic geodesics (e.g. great circles on a sphere).

## R12 - Surface differential operators

Implement source Eqs. (474)-(475). Reproduce benchmark identities on a plane and sphere, and compare symbolic versus numerical differentiation when possible.

## Reproduction status

```text
R0 target identified
R1 source anchor checked
R2 independent derivation prepared
R3 implementation complete
R4 deterministic tests pass
R5 convergence/invariance tests pass
R6 reproduced
R7 cross-language reproduced
```

A result is never labeled `reproduced` solely because a plot looks similar to a source figure.
