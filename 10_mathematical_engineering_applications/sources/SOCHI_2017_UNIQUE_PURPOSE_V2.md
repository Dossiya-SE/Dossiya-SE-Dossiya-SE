# Sochi 2017 - Engineering Transfer Contract V2

**Unique purpose:** govern transfer of source differential geometry into engineering models without falsely attributing engineering validity to the mathematical source.

## Evidence states

Every application artifact must carry exactly one primary state:

1. `MATHEMATICS_ONLY` - geometry is implemented, no engineering meaning claimed;
2. `ENGINEERING_ANALOGY` - a possible engineering interpretation is proposed but not validated;
3. `ENGINEERING_MODEL` - governing engineering assumptions and external sources are defined;
4. `ENGINEERING_VALIDATED` - engineering model has validation evidence appropriate to its intended use.

A change of vocabulary does not move an artifact between states; evidence does.

## Transfer A - geometric path analysis

Source tools:
- curve parameterization;
- arc length;
- curvature/torsion;
- geodesics;
- Frenet frames.

Potential engineering domains:
- trajectory/path planning;
- route geometry;
- pipe/cable alignment;
- inspection paths.

Required external evidence: cost function, kinematic/physical constraints, obstacle model, safety limits, and validation data.

## Transfer B - surface/shape representation

Source tools:
- parameterized surfaces;
- metric and area;
- normals;
- principal curvatures;
- Gaussian/mean curvature.

Potential domains:
- shells and membranes;
- terrain/topography;
- structural surfaces;
- manufacturing geometry;
- interfaces.

The source does not provide material constitutive laws, structural resistance, or design-code criteria.

## Transfer C - differential operators on curved domains

Source tools:
- covariant differentiation;
- divergence;
- Laplace-Beltrami.

Potential domains:
- heat/moisture/species transport on surfaces;
- distributed sensing;
- surface flow approximations;
- PDE-constrained design.

External sources must supply conservation equations, coefficients, units, boundary/initial conditions, and validation.

## Transfer D - manifold state representations

The mathematical idea of a state trajectory on a manifold may support nonlinear engineering state-space models. However, a state manifold is not established merely by drawing a curved surface.

Minimum evidence to promote an engineering state manifold:

- explicit state variables and dimensions;
- admissible-state set;
- coordinate/chart definition;
- metric or distance with engineering meaning;
- governing dynamics;
- empirical/calibration basis;
- sensitivity and uncertainty treatment.

## Transfer E - infrastructure resilience research

Candidate mathematical constructions include:

```text
system trajectory -> curve
safe/admissible states -> subset/manifold
recovery path -> constrained curve
interface variables -> coupling coordinates/parameters
sensitivity field -> scalar/tensor field
```

These are **model-design options**, not facts established by Sochi. In particular:

- trajectory curvature is not automatically resilience loss;
- geodesic length is not automatically recovery cost;
- Gaussian curvature is not automatically fragility;
- topology of a smooth surface is not automatically graph/network topology.

Any such identification requires a separately defined engineering map and validation.

## Dual-source citation rule

A publication-grade application must contain both:

```text
Mathematical statement -> Sochi or another mathematical source
Engineering interpretation/claim -> engineering/domain source + validation
```

Example:

```text
K = det(shape operator)      [mathematics source]
K predicts interface risk    [new hypothesis; requires data and engineering evidence]
```

## Transfer artifact schema

```yaml
math_source_id: SOCHI-DG-2017-UPLOADED
math_equations: []
math_verification: []
engineering_domain: ...
engineering_sources: []
engineering_variables: []
units: {}
assumptions: []
calibration_data: ...
validation_data: ...
uncertainty_model: ...
state: MATHEMATICS_ONLY | ENGINEERING_ANALOGY | ENGINEERING_MODEL | ENGINEERING_VALIDATED
limitations: []
```

## Acceptance gate

No source-derived mathematical artifact is allowed to enter `ENGINEERING_VALIDATED` solely because:

- its code runs;
- its dimensional geometry looks plausible;
- a mathematical invariant is satisfied;
- a high-quality image was produced.

Engineering validation is a separate evidentiary layer.
