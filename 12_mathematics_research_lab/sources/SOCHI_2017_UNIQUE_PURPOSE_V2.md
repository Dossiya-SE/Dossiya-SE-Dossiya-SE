# Sochi 2017 - Research Hypothesis Program V2

**Unique purpose:** generate explicitly new and falsifiable research questions from source-grounded differential geometry. Nothing in this file is attributed to Sochi unless labeled `SOURCE_MATH`.

## Hypothesis template

```yaml
hypothesis_id: H...
source_math: []
extension_statement: ...
null_hypothesis: ...
observable: ...
experiment: ...
acceptance_criterion: ...
falsification_criterion: ...
required_external_sources: []
status: IDEA | FORMULATED | IMPLEMENTED | TESTED | REJECTED | SUPPORTED
```

## H1 - Geometry of viability boundaries

**SOURCE_MATH:** regular surfaces, metric, principal curvatures, `K`, `H`.

**EXTENSION:** if a high-dimensional engineering viability boundary can be represented by a sufficiently regular manifold, local geometric quantities may encode sensitivity of feasible-state geometry.

Null hypothesis: curvature fields provide no predictive information beyond conventional local sensitivity/Jacobian/Hessian measures.

Required experiment: construct controlled benchmark systems where the true viability boundary is known; compare curvature-derived indicators with baseline sensitivity measures under perturbation.

Falsification: no reproducible out-of-sample benefit or no stable geometric meaning under admissible reparameterization.

## H2 - Geodesic versus engineering-optimal recovery

**SOURCE_MATH:** Eq. (418), intrinsic geodesic equation.

**EXTENSION:** under a deliberately defined engineering metric, geodesics might approximate minimum-cost recovery paths.

Null hypothesis: geodesic paths are not closer to the engineering optimum than ordinary baseline paths.

Critical requirement: define the metric from engineering cost/constraints first. Do not retrofit a metric merely to make an observed optimum geodesic.

## H3 - Moving-frame signatures of dynamic trajectories

**SOURCE_MATH:** Frenet-Serret frame, curvature `kappa`, torsion `tau`.

**EXTENSION:** curvature/torsion of a suitably normalized state trajectory may identify changes in dynamic regime.

Null hypothesis: these geometric descriptors add no robust regime-change information beyond derivatives of the original state variables.

Tests must include reparameterization sensitivity, noise sensitivity, derivative-estimation bias, and comparison with conventional change-point methods.

## H4 - Topological transition and total-curvature analogy

**SOURCE_MATH:** Euler characteristic, genus, global Gauss-Bonnet.

**EXTENSION:** changes in topology of a continuous feasible-state manifold may correspond to qualitative changes in system flexibility or accessibility.

Warning: smooth-manifold topology is not graph/network topology. Any bridge between them requires a formally defined mapping.

Null hypothesis: topology changes of the chosen continuous representation do not track meaningful engineering transitions.

## H5 - Manifold diffusion for coupled-state uncertainty

**SOURCE_MATH:** surface divergence and Laplace-Beltrami operator (Eqs. 474-475).

**EXTENSION:** if uncertain system states are constrained to a manifold, manifold-native diffusion may represent some uncertainty-evolution processes better than Euclidean diffusion.

Null hypothesis: manifold-aware diffusion offers no measurable improvement over an appropriately transformed Euclidean baseline.

Required external foundations: stochastic processes/PDEs, dimensional model, empirical calibration.

## H6 - Intrinsic versus extrinsic resilience descriptors

**SOURCE_MATH:** intrinsic/extrinsic distinction; Theorema Egregium.

**EXTENSION:** separating descriptors invariant to representation from descriptors dependent on embedding may improve interpretability of engineering state-space models.

Experiment: construct multiple isometric or coordinate-transformed representations of the same benchmark model and test which proposed resilience indicators remain invariant.

Falsification: purported intrinsic indicators change materially under admissible representation changes.

## H7 - Compatibility-constrained learned surfaces

**SOURCE_MATH:** Gauss-Weingarten, Codazzi-Mainardi, Gauss-Codazzi.

**EXTENSION:** machine-learned first/second fundamental-form fields could be regularized by geometric compatibility residuals.

Null hypothesis: compatibility regularization does not improve geometric validity or predictive performance relative to unconstrained learning.

This is a computational-research extension and needs independent machine-learning literature.

## H8 - Curvature-aware visualization as scientific inference aid

**SOURCE_MATH:** `K`, `H`, principal directions, geodesics.

**EXTENSION:** mathematically encoded 3D visualization may improve expert detection of model regimes compared with generic aesthetic rendering.

Experiment: blinded expert/user study with controlled tasks and identical underlying data.

Null hypothesis: no significant improvement in accuracy/time/calibration.

## Promotion rule

```text
Research Lab hypothesis
 -> explicit mathematical definition
 -> implementation
 -> verification
 -> external domain evidence
 -> preregistered/declared test
 -> result
 -> only then candidate transfer to stable model/application module
```

Unsupported analogies remain here and must not silently migrate into Foundations or Engineering Applications.
