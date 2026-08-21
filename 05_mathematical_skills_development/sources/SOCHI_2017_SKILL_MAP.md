# Sochi 2017 — Differential-Geometry Skill Map

**Unique purpose:** turn the book's concepts and exercises into measurable competencies. This module does not duplicate the book chapter order; it reorganizes learning around demonstrated capability.

**Primary source:** Sochi (2017), Chapters 1–7 and end-of-chapter exercises.

## Mastery ladder

| Level | Capability | Evidence required |
|---|---|---|
| L0 — Recognize | identify objects, notation, intrinsic/extrinsic distinctions | terminology quiz + annotated figure |
| L1 — Explain | explain definitions and hypotheses without formula substitution | written explanation with source anchors |
| L2 — Derive | derive core formulas from definitions | hand/LaTeX derivation with intermediate steps |
| L3 — Solve | solve analytic problems and worked examples | checked solutions with units/domains where applicable |
| L4 — Implement | translate mathematics into tested software and scientific graphics | code + tests + reproducible environment |
| L5 — Verify | independently check invariants/theorems and diagnose failures | symbolic/numerical verification report |
| L6 — Extend | formulate a defensible new model or theorem-level question | explicit source/extension boundary + validation plan |

## Skill family A — coordinates, mappings, regularity

Source anchors: §§1.4.2–1.4.3, Exercises 1.42–1.47.

Required competencies:

- distinguish map, parameter domain, trace, coordinate curves, and embedding;
- compute a Jacobian and rank;
- test `E1 × E2 != 0` for a surface patch;
- distinguish representation singularity from geometric singularity;
- enforce smoothness class required by the target quantity.

**L4 implementation task:** build a function that receives `X(u,v)` and numerically flags near-singular regions using the norm of `X_u×X_v`, while documenting that a numerical threshold is not a proof of regularity.

## Skill family B — curve geometry

Source anchors: Chapter 2; especially Exercises 2.21–2.30 and 2.74–2.91.

Required competencies:

\[
T,\quad N,\quad B,\quad \kappa,\quad \tau,
\]

plus osculating/rectifying/normal planes, osculating circle/sphere, Darboux vector, and parallel propagation.

**L2 derivation:** derive the curvature formula for a general parameter from the arc-length definition.

**L4 implementation:** compute the Frenet frame for a helix and verify orthonormality.

**L5 verification:** reverse parameter orientation and check which frame components/signs change consistently with the adopted convention.

## Skill family C — surface metric and fundamental forms

Source anchors: Chapter 3, especially §§3.2–3.9.

Required competencies:

- tangent basis and unit normal;
- metric tensor / first fundamental form;
- arc length, area, and angle;
- curvature tensor / second fundamental form;
- first/second/third fundamental forms;
- Gauss-Weingarten and Codazzi-Mainardi relations.

**L4 implementation:** derive `E,F,G` from a parameterization and compute the area density `sqrt(EG-F^2)`.

## Skill family D — curvature

Source anchors: Chapter 4.

Required competencies:

- curvature vector decomposition;
- normal and geodesic curvature;
- principal curvatures/directions;
- Gaussian and mean curvature;
- local shape classification;
- umbilical points.

**L5 verification:** classify sampled points on a hyperbolic paraboloid from the sign of Gaussian curvature and cross-check with principal curvatures.

## Skill family E — intrinsic geometry and topology

Source anchors: §§1.3.2, 1.4.1, 1.4.4, 4.7, 4.8, 5.7, 6.5.

Required competencies:

- intrinsic distance;
- local/global distinction;
- isometry;
- geodesics versus global shortest paths;
- Euler characteristic/genus;
- Theorema Egregium;
- local and global Gauss–Bonnet.

Relevant exercise anchors include 1.24–1.30, 4.98–4.111, and 6.27–6.33.

**L5 verification:** reproduce total curvature `4π` for a sphere and `0` for a torus from both numerical integration and topology.

## Skill family F — special curves and surfaces

Source anchors: Chapters 5–6.

Skills include geodesic curves, lines of curvature, asymptotic lines, ruled/developable/isometric/tangent/minimal surfaces.

**L4 implementation:** regenerate catenoid and helicoid from parameterizations and compute their metric/curvature fields.

**L5 task:** establish catenoid-helicoid local isometry analytically, not visually (Exercise 6.32).

## Skill family G — tensor differentiation

Source anchor: Chapter 7.

Required competencies:

- covariant differentiation;
- absolute differentiation along a curve;
- metric compatibility;
- contraction/product rules;
- surface gradient/divergence/Laplacian using metric factors.

**L5 verification:** select a non-Cartesian surface metric and symbolically verify `∇g=0`.

## Assessment evidence standard

Every completed skill item should contain:

1. source citation `(Sochi, 2017, §x, p. y, Eq./Exercise z)`;
2. mathematical work;
3. implementation where L4+;
4. verification oracle where L5+;
5. failure/limitation notes;
6. exact software environment for computational evidence.

## Citation

Sochi, T. (2017). *Introduction to Differential Geometry of Space Curves and Surfaces*. User-supplied PDF; internal preface date March 2017.
