# Sochi 2017 - Example Atlas V2

**Unique purpose:** executable and worked geometric examples. Definitions and theorem statements belong in Foundations; acceptance tests belong in Verification.

## Level A - parameterization prototypes from §1.4.1

| Object | Source equations | Domain/condition | Independent check |
|---|---:|---|---|
| surface of revolution | (1)-(3) | profile `f(z)` and angle | radial distance equals `|f(z)|` |
| helix | (4)-(6) | `a,b != 0`, real theta | `x^2+y^2=a^2`; analytic kappa/tau |
| torus | (7)-(9) | `0<r<R`, angles in `[0,2pi)` | `(sqrt(x^2+y^2)-R)^2+z^2=r^2` |
| ellipsoid | (10)-(12) | nonzero semi-axes | `(x/a)^2+(y/b)^2+(z/c)^2=1` |
| hyperboloid one sheet | (13)-(15) | nonzero scales | `(x/a)^2+(y/b)^2-(z/c)^2=1` |
| hyperboloid two sheets | (16)-(18) | `xi>=0` in source chart | `-(x/a)^2-(y/b)^2+(z/c)^2=1` |
| elliptic paraboloid | (19)-(21) | `xi>=0` | `(x/a)^2+(y/b)^2=z/c` |
| hyperbolic paraboloid | (22)-(24) | real xi,omega | `z=(c/(ab))xy` |
| parabolic cylinder | (25)-(27) | real xi,omega | `y=a x^2` |
| catenary | (28)-(29) | `a!=0` | `x=a cosh(z/a)` in the source orientation |
| catenoid | (30)-(32) | `a!=0` | `sqrt(x^2+y^2)=a cosh(z/a)` |
| helicoid | (33)-(35) | `a,b!=0` | radius `=|a xi|`, height linear in theta |
| monkey saddle | (36)-(38) | real xi,omega | `z=x^3-3xy^2` |
| Enneper surface | (39)-(41) | real xi,omega | direct substitution + minimal-surface benchmark |
| tractrix | (42) | `0<x<=rho` | ODE residual |
| Beltrami pseudosphere | (43)-(45) | `0<theta<pi` | constant negative-curvature benchmark after derivation |

## Level B - curve examples

1. Straight line: `kappa=0`, `tau=0`.
2. Circle radius `R`: `kappa=1/R`, `tau=0`.
3. Circular helix `r(t)=(a cos t,a sin t,bt)`:

\[
\kappa=\frac{|a|}{a^2+b^2},\qquad
\tau=\frac{b}{a^2+b^2}
\]

under the orientation/sign convention used in the source.

These are independent benchmark objects for Frenet-frame implementations.

## Level C - surface geometry examples

### Sphere
- constant positive Gaussian curvature;
- all points umbilical;
- Gauss-Bonnet total curvature `4pi`.

### Plane and cylinder
Theorema Egregium benchmark: a plane and a circular cylinder can share intrinsic geometry even though their extrinsic curvature differs. Computational exercise: compare metrics under an explicit isometric parameterization.

### Torus
- variable Gaussian curvature;
- positive outer region, negative inner region for the standard embedded ring torus;
- Euler characteristic zero;
- total Gaussian curvature zero.

### Catenoid and helicoid
The source classifies both among canonical special surfaces and discusses minimal surfaces later. They form high-value examples for checking `H=0` when parameterized consistently.

## Level D - advanced worked problems from chapter exercises

The exercise sets are not copied wholesale. They are converted into reproducible tasks such as:

- prove/compute regularity of an elliptic paraboloid;
- locate coordinate singularities of spherical coordinates;
- derive selected Christoffel components;
- evaluate principal curvatures for a Monge patch;
- verify Gauss-Bonnet for sphere/torus;
- classify points as elliptic/parabolic/hyperbolic using `K` and the second fundamental form;
- numerically integrate a geodesic and check metric-speed conservation;
- implement covariant derivatives and Laplace-Beltrami on a known surface.

## Execution contract

Every code example must include:

1. source equation/section;
2. parameter domain;
3. singularity guards;
4. one independent relation not used to generate the geometry;
5. a deterministic test;
6. no copied source artwork.

See `differential_geometry/source_examples.py` and `source_examples_v2.py`.
