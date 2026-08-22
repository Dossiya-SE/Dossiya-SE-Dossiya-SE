# Sochi 2017 — Differential Geometry to Engineering Transfer Contract

**Unique purpose:** govern how differential-geometry concepts are transferred into engineering models without misrepresenting the textbook as an engineering source.

## Core rule

A source-grounded engineering artifact must distinguish:

$$
\boxed{
\text{geometric mathematics}
\neq
\text{engineering meaning}
}
$$

Sochi (2017) supplies mathematical definitions, equations, geometric objects, and theorem anchors. It does **not** establish infrastructure-resilience, energy-system, climate, reliability, or sustainability interpretations.

## Transfer pattern

Every engineering use must document five layers:

1. **Geometric object** — e.g. curve, surface, metric, connection, curvature, geodesic.
2. **Source anchor** — precise section/page/equation in Sochi.
3. **Engineering mapping** — what engineering quantity is represented by the geometric object.
4. **Independent engineering evidence** — physical/empirical/domain source justifying the mapping.
5. **Validation test** — evidence that the geometric representation improves or faithfully represents the engineering problem.

## Permitted candidate transfers

### T1 — state trajectory as a curve

Mathematical source:

$$
r(t)\in\mathbb R^n
$$

with tangent, curvature, and higher-order change measures (Sochi, Chapter 2).

Engineering candidate:

$$
x(t)=[P,W,T,SW,\ldots]^\top
$$

as a system-state trajectory.

**Constraint:** `κ` and `τ` have no engineering meaning until state coordinates are scaled and a metric is justified. Euclidean curvature in arbitrary normalized coordinates is not automatically a resilience indicator.

### T2 — feasible/viable state set as a manifold or surface

Mathematical source: regular surfaces, parameter mappings, tangent spaces, metric structure (Sochi, Chapters 1 and 3).

Engineering candidate: a lower-dimensional feasible state manifold embedded in a larger state space.

**Constraint:** regularity, dimension, and coordinate validity must be established from the engineering model; a decorative surface does not constitute a manifold model.

### T3 — state-dependent transition cost as a metric

Mathematical source: surface metric tensor, intrinsic distance, geodesics (Sochi §§1.4.4, 3.3, 5.7).

Engineering candidate:

$$
g_{ij}(x)
$$

encodes locally varying transition difficulty/cost.

**Constraint:** positive definiteness and units/scaling must be justified. The metric must be derived from interpretable costs, sensitivities, information geometry, or physics—not selected solely to create desired curvature.

### T4 — recovery path as a geodesic or minimum-action curve

Mathematical source: geodesic equation (Sochi Eq. 418).

Engineering candidate: compare observed/optimized recovery trajectories with metric geodesics.

**Constraint:** Sochi explicitly notes that geodesics need not be globally shortest paths. Therefore `geodesic = optimal recovery` is prohibited unless the optimization criterion and conditions are independently demonstrated.

### T5 — local fragility as curvature hypothesis

Mathematical source: principal/Gaussian/mean curvature (Sochi, Chapter 4).

Engineering candidate: investigate whether curvature of a constraint/viability boundary correlates with sensitivity or failure concentration.

**Status:** research hypothesis only until validated. Curvature is a coordinate/geometric quantity whose engineering interpretation depends on the model construction.

### T6 — interface transport on curved domains

Mathematical source: covariant derivatives, surface divergence, surface Laplacian (Sochi, Chapter 7).

Engineering candidate: transport/diffusion of quantities over curved physical interfaces or state manifolds.

**Constraint:** physical flux laws, material coefficients, and boundary conditions require independent domain sources.

## Mandatory validation checklist

An engineering artifact using Sochi-derived geometry cannot be promoted beyond `exploratory` unless:

- [ ] mathematical formula traced to source;
- [ ] engineering interpretation sourced independently;
- [ ] dimensions/units are consistent;
- [ ] coordinate/normalization choices are documented;
- [ ] sensitivity to coordinate scaling is tested where relevant;
- [ ] numerical convergence is checked;
- [ ] an alternative non-geometric baseline is compared;
- [ ] limitations and failure cases are recorded.

## Citation policy

Use dual citations in scientific text. Example:

> The recovery trajectory is represented as a curve on a state manifold, with geodesics defined through the Levi-Civita connection (Sochi, 2017, §5.7, Eq. 418); the engineering interpretation of the metric is defined independently from domain-specific transition costs [engineering source].

## Citation

Sochi, T. (2017). *Introduction to Differential Geometry of Space Curves and Surfaces*. User-supplied PDF; internal preface date March 2017.
