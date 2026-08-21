# Sochi 2017 — Geometric Example Catalog

**Unique purpose:** executable, inspectable examples. Canonical definitions remain in module 01; reproduction accuracy belongs to module 04; verification assertions belong to module 08.

**Primary source:** Sochi (2017), especially §1.4.1, printed pp. 17–28; Chapters 2, 5, and 6 supply curve/special-object extensions.

## Source-grounded catalog

| ID | Object | Source anchor | Mathematical representation | Domain / guard |
|---|---|---|---|---|
| EX-HELIX | circular helix | p. 18, Eqs. (4)–(6) | `x=a cos θ`, `y=a sin θ`, `z=bθ` | θ real; source prototype uses nonzero a,b |
| EX-TORUS | torus | pp. 18–19, Eqs. (7)–(9) | `x=(R+r cos φ)cos θ`, `y=(R+r cos φ)sin θ`, `z=r sin φ` | `0<r<R`; θ,φ in `[0,2π)` |
| EX-ELLIPSOID | ellipsoid | p. 19, Eqs. (10)–(12) | `x=a sin θ cos φ`, `y=b sin θ sin φ`, `z=c cos θ` | standard angular ranges; nonzero semiaxes |
| EX-HYP1 | hyperboloid, one sheet | pp. 19–20, Eqs. (13)–(15) | `x=a cosh ξ cos θ`, `y=b cosh ξ sin θ`, `z=c sinh ξ` | ξ real |
| EX-HYP2 | hyperboloid, two sheets | pp. 20–21, Eqs. (16)–(18) | `x=a sinh ξ cos θ`, `y=b sinh ξ sin θ`, `z=c cosh ξ` | source display uses `ξ>=0` |
| EX-EPAR | elliptic paraboloid | p. 21, Eqs. (19)–(21) | `x=a√ξ cos θ`, `y=b√ξ sin θ`, `z=cξ` | `ξ>=0` |
| EX-HPAR | hyperbolic paraboloid | p. 21, Eqs. (22)–(24) | `x=aξ`, `y=bω`, `z=cξω` | ξ,ω real |
| EX-PCYL | parabolic cylinder | pp. 21–22, Eqs. (25)–(27) | `x=ξ`, `y=aξ²`, `z=bω` | ξ,ω real |
| EX-CATENARY | catenary | p. 23, Eqs. (28)–(29) | `x=a cosh(ξ/a)`, `z=ξ` | `a≠0` |
| EX-CATENOID | catenoid | pp. 23–24, Eqs. (30)–(32) | `x=a cosh(ξ/a)cos θ`, `y=a cosh(ξ/a)sin θ`, `z=ξ` | `a≠0` |
| EX-HELICOID | helicoid | p. 24, Eqs. (33)–(35) | `x=aξ cos θ`, `y=aξ sin θ`, `z=bθ` | ξ,θ real |
| EX-MONKEY | monkey saddle | p. 25, Eqs. (36)–(38) | `x=ξ`, `y=ω`, `z=ξ³−3ξω²` | ξ,ω real |
| EX-ENNEPER | Enneper surface | pp. 25–26, Eqs. (39)–(41) | source polynomial parameterization | ξ,ω real |
| EX-PSEUDO | Beltrami pseudosphere | pp. 26–27, Eqs. (43)–(45) | tractrix surface of revolution | `0<θ<π`, `0≤φ<2π` |

The source explicitly notes that these objects may admit other parameterizations; therefore the repository stores a `source_parameterization_id` instead of treating one representation as the object itself (Sochi, 2017, p. 27).

## Worked-example progression

### Level 1 — parameterization and domain

For every catalog object:

1. evaluate points from admissible parameters;
2. enforce parameter/domain restrictions;
3. identify coordinate singularities versus geometric singularities;
4. plot coordinate curves without claiming the plot proves regularity.

### Level 2 — differential structure

Compute

\[
X_u,\quad X_v,\quad X_u\times X_v,
\]

and test regularity on the selected domain. For a curve, compute `r'`, `r''`, and where needed `r'''`.

### Level 3 — intrinsic/extrinsic quantities

For a regular surface patch compute

\[
g_{ij}=\langle X_i,X_j\rangle,
\]

then Christoffel symbols and Gaussian curvature. Separately compute normal-dependent quantities such as the second fundamental form and mean curvature. This maintains Sochi's intrinsic/extrinsic distinction (§1.3.2).

### Level 4 — theorem-linked examples

- sphere/ellipsoid/torus: Euler characteristic and Gauss–Bonnet;
- plane/cylinder: local isometry and Theorema Egregium;
- catenoid/helicoid: local isometry exercise anchor (Sochi, Ch. 6, Exercise 6.32);
- minimal surfaces: verify `H=0` where the hypotheses and implementation permit;
- geodesics: integrate Eq. (418) and distinguish local geodesic character from global shortest-path claims (Sochi, §5.7).

## Computational source

`source_examples.py` independently implements a selected subset of the catalog. It is intentionally small enough to audit against the source equations line by line.

## Citation

Sochi, T. (2017). *Introduction to Differential Geometry of Space Curves and Surfaces*. User-supplied PDF; internal preface date March 2017. Source anchors are reported as printed pages/equation numbers.
