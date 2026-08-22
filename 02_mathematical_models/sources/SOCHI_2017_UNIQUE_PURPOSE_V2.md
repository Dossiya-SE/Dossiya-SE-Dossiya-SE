# Sochi 2017 - Mathematical Model Contracts V2

**Unique purpose:** convert source mathematics into explicit model objects with inputs, state variables, constraints, observables, and validity conditions. This file does not serve as a theorem catalog or worked-example gallery.

## M1 - Regular space-curve model

$$
\mathcal M_C=(I,r,t,\dot r,T,N,B,\kappa,\tau).
$$

### Inputs
- interval `I`;
- parameter `t` or arc length `s`;
- differentiable mapping `r:I->R^3`.

### Admissibility
- `|r_dot|>0` at regular points;
- curvature formulas need the appropriate derivative order;
- torsion formula additionally requires `|r_dot x r_ddot|>0` at evaluation points.

### Observables
- tangent `T`;
- curvature `kappa` from Eq. (126);
- torsion `tau` from Eq. (129);
- Frenet frame dynamics from Eqs. (136)-(139).

### Invariants/checks
- `T.N=T.B=N.B=0`;
- `|T|=|N|=|B|=1` where the frame is defined;
- rigid motions preserve `kappa` and `tau`.

## M2 - Regular parametric-surface model

$$
\mathcal M_S=(\Omega,r,E_1,E_2,n,a_{\alpha\beta},a^{\alpha\beta},b_{\alpha\beta}).
$$

### Inputs
- open parameter domain `Omega subset R^2`;
- sufficiently differentiable `r(u,v):Omega->R^3`.

### Admissibility
$$
E_1\times E_2\neq0,
\qquad a=EG-F^2>0.
$$

### Derived state
$$
E_\alpha=\partial_\alpha r,
\qquad
n=\frac{E_1\times E_2}{\|E_1\times E_2\|},
$$

$$
a_{\alpha\beta}=E_\alpha\cdot E_\beta,
\qquad
b_{\alpha\beta}=n\cdot\partial_{\alpha\beta}r
$$

for the Cartesian-embedding convention used by the source.

### Observables
- line element and surface area;
- Christoffel symbols;
- principal curvatures;
- Gaussian curvature `K`;
- mean curvature `H`.

## M3 - Intrinsic connection/curvature model

$$
\mathcal M_I=(a_{\alpha\beta},a^{\alpha\beta},\Gamma^\alpha_{\beta\gamma},R^\alpha{}_{\beta\gamma\delta},K).
$$

Pipeline:

```text
metric -> inverse metric -> metric derivatives -> Christoffel -> Riemann -> K
```

This model is explicitly independent of the surface normal once the metric is supplied. It is the correct model contract for testing Theorema Egregium computationally.

## M4 - Shape-operator model

$$
S^\alpha{}_{\beta}=a^{\alpha\gamma}b_{\gamma\beta}.
$$

The principal curvatures are eigenvalues of `S`. Hence:

$$
\kappa^2-2H\kappa+K=0,
$$

with

$$
H=\frac12\operatorname{tr}S,
\qquad
K=\det S.
$$

Validity depends on a regular surface patch and consistent surface orientation.

## M5 - Surface compatibility model

A six-field description `(E,F,G,e,f,g)` is not accepted as an arbitrary surface model. It must obey:

- positive-definiteness of the first fundamental form;
- Gauss compatibility;
- Codazzi-Mainardi compatibility.

The source's Gauss-Weingarten and Gauss-Codazzi relations are treated as structural constraints. Numerically reconstructed surfaces must report compatibility residuals.

## M6 - Geodesic initial-value model

State:

$$
y=(u^1,u^2,v^1,v^2),
\qquad v^\alpha=\frac{du^\alpha}{ds}.
$$

Dynamics from Eq. (418):

$$
\frac{du^\alpha}{ds}=v^\alpha,
\qquad
\frac{dv^\alpha}{ds}
=-\Gamma^\alpha_{\beta\gamma}v^\beta v^\gamma.
$$

Inputs:
- metric or Christoffel field;
- initial position;
- initial tangent.

Checks:
- remain inside chart domain;
- preserve metric speed for affine/arc-length parameterization within numerical tolerance;
- switch charts if a coordinate singularity is reached.

## M7 - Parallel-transport / moving-vector model

For a vector field along a curve, the absolute/covariant derivative layer in Chapter 7 supplies the transport law. A parallel-transport model sets the appropriate absolute derivative to zero along the path.

This model must distinguish:
- coordinate-component change;
- geometric vector change;
- basis change induced by the connection.

## M8 - Scalar field on a surface

$$
\mathcal M_f=(S,a_{\alpha\beta},f,\nabla f,\Delta_S f).
$$

The source provides the Laplace-Beltrami form

$$
\Delta_S f
=\frac{1}{\sqrt a}\partial_\alpha
(\sqrt a\,a^{\alpha\beta}\partial_\beta f)
$$

(Eq. 475). This model is purely mathematical here. Heat, diffusion, wave, or transport interpretations belong in Mathematical Physics and require separate constitutive assumptions.

## M9 - Tangent vector field / divergence model

For tangent components `A^alpha`:

$$
\nabla\cdot A
=\frac{1}{\sqrt a}\partial_\alpha(\sqrt a A^\alpha)
$$

(Eq. 474).

Required model metadata:
- chart;
- basis convention;
- metric determinant;
- domain/boundary;
- regularity of `A`.

## M10 - Topology-curvature model

For compact orientable surfaces of the class stated in the source:

$$
\iint_S K\,d\sigma=2\pi\chi,
\qquad
\chi=2(1-g).
$$

This is a global constraint model, not a pointwise local model. It is especially useful as a reproduction/verification oracle.

## Model metadata contract

Every model instantiated from this source must declare:

```yaml
source_id: SOCHI-DG-2017-UPLOADED
source_equations: []
parameter_domain: ...
regularity: ...
orientation_convention: ...
state_variables: ...
inputs: ...
outputs: ...
constraints: ...
numerical_method: ...
verification_oracles: ...
known_singularities: ...
extension_status: SOURCE | DERIVED | EXTENSION
```

Engineering or physical parameters must never be inserted into these source models without being marked `EXTENSION` and supported separately.
