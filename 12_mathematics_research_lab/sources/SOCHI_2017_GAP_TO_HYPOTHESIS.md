# Sochi 2017 — Gap-to-Hypothesis Research Map

**Unique purpose:** turn explicit source boundaries into falsifiable research questions. Nothing in this file is promoted to established theory merely because it uses established differential geometry.

## H1 — Curvature of engineered viability boundaries

**Source mathematics:** local surface curvature, principal curvatures, Gaussian/mean curvature (Sochi, 2017, Chapter 4).

**Research question:** if an engineering viable set has a smooth boundary `∂V`, does curvature of that boundary predict sensitivity to disturbances or concentration of exit trajectories?

Candidate hypothesis:

$$
|K_{\partial V}(x)|\uparrow
\quad\Longrightarrow\quad
\text{local viability sensitivity may increase}
$$

under a specifically defined metric and perturbation model.

**Falsification:** demonstrate systems with identical boundary curvature but materially different exit probability/sensitivity, or show the relationship disappears under justified coordinate/metric changes.

**Status:** exploratory extension (`EXT`), not a claim in Sochi.

## H2 — Geodesic recovery versus operationally optimal recovery

**Source mathematics:** intrinsic distance and geodesics (Sochi §§1.4.4 and 5.7; Eq. 418).

**Research question:** can a scientifically constructed metric make geodesic paths approximate minimum-cost infrastructure recovery trajectories?

Test:

1. define an engineering cost functional independently;
2. derive a positive-definite metric candidate from local costs/sensitivities;
3. compute metric geodesics;
4. compare them to direct optimal-control solutions;
5. quantify path/cost discrepancy.

**Critical source constraint:** Sochi explicitly notes that geodesics are not necessarily globally shortest paths. Therefore any global optimality claim must be proved from the engineering objective and domain.

## H3 — Parallel transport as interface-state comparison

**Source mathematics:** path-dependent parallel propagation on curved surfaces (Sochi §2.7 and Chapter 7).

**Research question:** can parallel transport provide a coordinate-consistent way to compare local sensitivity or interface vectors defined at different points of a nonlinear state manifold?

**Falsification:** if transported quantities are not operationally meaningful or if the state space lacks a defensible connection/metric, reject the construction.

## H4 — Topology-aware regime change

**Source mathematics:** Euler characteristic/genus and Gauss–Bonnet (Sochi §§1.4.1, 4.8).

**Research question:** can changes in the topology of feasible/viable regions be detected alongside geometric curvature changes during increasing stress?

Possible observables:

$$
\chi(\mathcal V(\lambda)),\qquad
\int_{\partial\mathcal V(\lambda)}K\,dA,
$$

where `λ` is a stress/control parameter and theorem hypotheses are checked before invoking Gauss–Bonnet.

**Risk:** numerical topology from discretized data can be unstable. Persistent-homology or mesh-topology methods require separate sources and validation.

## H5 — Differential-geometric signatures of coupled dynamics

**Source mathematics:** curve curvature/torsion and moving frames (Sochi Chapter 2).

For a scaled state trajectory `x(t)` in dimension `n>=3`, test whether geometric turning measures detect transitions that conventional derivative-based indicators miss.

**Primary confounder:** coordinate scaling. A Euclidean `κ` computed after arbitrary normalization is not invariant to general rescaling. The research design must therefore compare justified metrics/normalizations.

## H6 — Geometry-aware uncertainty tubes

**Source mathematics:** intrinsic distance, geodesic structure, surface metrics.

**Research question:** can uncertainty around a nominal state trajectory be represented more faithfully by metric balls/tubes than by Euclidean covariance ellipsoids?

Candidate object:

$$
\mathcal T_\epsilon(\gamma)
=\{x:\inf_t d_g(x,\gamma(t))\le\epsilon\}.
$$

This definition is an extension; only the differential-geometric primitives come from Sochi.

## H7 — Curved-domain transport for infrastructure interfaces

**Source mathematics:** covariant differentiation, surface divergence, and surface Laplacian (Sochi Chapter 7, including Eqs. 474–475).

**Research question:** for genuinely curved physical interfaces or lower-dimensional embedded domains, does a manifold PDE materially improve physical fidelity relative to a flat-domain approximation?

**Validation:** compare against measured/simulated reference data and quantify the error introduced by flattening.

## H8 — Cross-language mathematical reproducibility

**Source mathematics:** selected exact benchmark geometry from Sochi.

**Research question:** how often do independently implemented symbolic/numerical pipelines agree on invariant differential-geometric quantities, and what failure modes are caused by conventions, singular coordinates, or numerical differentiation?

Planned stacks:

- SymPy/NumPy/SciPy;
- Julia/DifferentialEquations.jl/Manifolds.jl;
- Wolfram Language;
- SageMath;
- formal fragments in Lean where feasible.

Measure:

$$
E_{cross}=
\frac{\|I_A-I_B\|}{\max(1,\|I_A\|,\|I_B\|)}
$$

for invariant quantity `I` after convention alignment.

## Research promotion gate

A hypothesis moves from `idea` to `research-ready` only when:

- [ ] source mathematics is traceable;
- [ ] new interpretation is labeled as extension;
- [ ] coordinate/metric dependence is analyzed;
- [ ] falsification criterion is stated;
- [ ] baseline alternative is defined;
- [ ] data or simulation validation plan exists;
- [ ] software/reproducibility plan exists;
- [ ] limitations are explicit.

## Citation

Sochi, T. (2017). *Introduction to Differential Geometry of Space Curves and Surfaces*. User-supplied PDF; internal preface date March 2017.
