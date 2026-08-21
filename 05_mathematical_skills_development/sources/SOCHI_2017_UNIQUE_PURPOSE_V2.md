# Sochi 2017 - Differential-Geometry Competency System V2

**Unique purpose:** convert the source into measurable learning and research competencies. This module stores mastery evidence, not a duplicate textbook summary.

## Mastery ladder

| Level | Competency | Required evidence |
|---|---|---|
| L0 | Recognize | identify symbols, objects, domains |
| L1 | Explain | precise verbal interpretation and assumptions |
| L2 | Derive | reproduce derivation with justified steps |
| L3 | Calculate | solve source-grounded analytical problems |
| L4 | Implement | produce tested symbolic/numerical code |
| L5 | Verify | construct independent invariants and failure cases |
| L6 | Generalize | transfer to a new manifold/problem with assumptions explicit |
| L7 | Research | formulate and test a falsifiable extension beyond the source |

## Skill track A - notation and tensor fluency

Source basis: Nomenclature and Chapter 1.

Competencies:
- distinguish Greek surface indices from Latin space indices;
- lower/raise indices with the correct metric;
- distinguish partial, covariant, and absolute derivatives;
- translate `E,F,G` to `a_11,a_12,a_22` and `e,f,g` to `b_11,b_12,b_22`;
- detect conflicting curvature/torsion sign conventions.

Gate to L4: implement notation-aware tensor operations without silent index-range errors.

## Skill track B - curves

Source basis: Chapter 2 and Chapter 5.

Progression:
1. parameterize a regular curve;
2. distinguish general and natural parameterizations;
3. compute `T,N,B`;
4. derive `kappa` and `tau`;
5. verify Frenet-Serret;
6. classify straight/plane/helix/geodesic/special curves;
7. integrate curve-frame dynamics computationally.

Mastery benchmark: circular helix with analytic `kappa,tau`, followed by a nonconstant-curvature curve.

## Skill track C - surfaces and metric geometry

Source basis: Chapter 3.

Progression:
- construct `E_1,E_2,n`;
- test rank-2 regularity;
- derive `a_{alpha beta}` and its inverse;
- compute line length, angles, area;
- construct `b_{alpha beta}`;
- derive the three fundamental forms;
- implement Gauss-Weingarten relations;
- verify compatibility conditions.

L5 evidence must include at least one deliberately singular parameterization and a correct diagnosis.

## Skill track D - curvature

Source basis: Chapter 4.

Required capabilities:
- normal and geodesic curvature;
- principal directions/eigenproblem;
- Gaussian and mean curvature;
- orientation dependence of `H` versus invariance of `K`;
- Theorema Egregium;
- local/global Gauss-Bonnet;
- point classification by curvature.

L6 challenge: compute `K` by an intrinsic route and an extrinsic route and prove numerical agreement.

## Skill track E - topology bridge

Source basis: Chapter 1 topology preliminaries + Chapter 4 Gauss-Bonnet.

Evidence sequence:
- calculate Euler characteristic from a cell/polygon decomposition;
- relate `chi` to genus;
- use topology to predict total curvature;
- verify by numerical surface integration.

## Skill track F - special surfaces

Source basis: Chapter 6.

Students/researchers must classify and implement:
- plane/quadratic;
- ruled/developable;
- isometric;
- tangent;
- minimal surfaces.

L5 benchmark: independently test a minimal-surface condition rather than accepting the label from the source.

## Skill track G - tensor differentiation and surface PDE operators

Source basis: Chapter 7.

Progression:
1. covariant differentiation;
2. absolute differentiation along curves;
3. metric compatibility;
4. tangent-vector divergence;
5. Laplace-Beltrami operator;
6. implementation on analytic surfaces;
7. coordinate-invariance checks.

## Exercise conversion rule

The source's end-of-chapter exercises are used as **skill anchors**, but repository tasks should be rewritten as original competency prompts. For each task record:

```yaml
source_chapter: ...
source_exercise_anchor: ...
skill_level: L0-L7
concepts: []
required_output: proof | derivation | code | visualization | verification
verification_criterion: ...
```

## Mastery evidence policy

A learner is not promoted on self-report. Every level requires a durable artifact such as:

- derivation note;
- passing test;
- reproducible notebook/script;
- vector-quality figure;
- numerical convergence report;
- formal proof;
- research hypothesis plus experiment.
