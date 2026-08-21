# Sochi 2017 - Mathematical Physics Bridge V2

**Unique purpose:** identify mathematical structures from the source that can support physics models, while sharply separating source mathematics from physical laws and constitutive assumptions supplied elsewhere.

## Evidence boundary

Sochi is a differential-geometry source, not a general physics textbook. Therefore each physical artifact is labeled:

```text
SOURCE_MATH       equation/definition directly supported by Sochi
MATH_DERIVATION   our mathematically derived consequence
PHYSICS_EXTENSION physical interpretation/model requiring independent physics evidence
```

## Bridge P1 - variational structure

Chapter 1 introduces first variation and a generic Euler-Lagrange form. This supports the mathematical language of stationary functionals.

Physics extension examples, requiring independent physics sources:
- action principles;
- constrained particle mechanics;
- elastic-energy minimization;
- field theories.

## Bridge P2 - geodesic dynamics

Source mathematics:

\[
\frac{d^2u^\alpha}{ds^2}
+\Gamma^\alpha_{\beta\gamma}
\frac{du^\beta}{ds}
\frac{du^\gamma}{ds}=0.
\]

This defines intrinsic geodesic motion mathematically. A statement such as "a free particle follows this curve" is **not** attributed to the book unless separately sourced in the relevant physical theory.

Computational physics experiment:
- specify a metric;
- integrate the geodesic IVP;
- track metric speed and geodesic residual;
- only then connect it to a physical model with external evidence.

## Bridge P3 - moving frames

Frenet-Serret equations provide a moving-frame description of a spatial curve:

\[
T'=\kappa N,
\qquad
N'=\tau B-\kappa T,
\qquad
B'=-\tau N.
\]

Possible physics extensions:
- rod/filament kinematics;
- trajectory curvature;
- frame transport;
- geometric phases.

The source supplies the geometry, not the constitutive mechanics of rods or filaments.

## Bridge P4 - surface kinematics and shape operator

Gauss-Weingarten equations separate changes of the surface basis into tangential connection terms and normal curvature terms. This is the correct geometric precursor for many shell/membrane formulations.

Physical stresses, strains, material laws, thickness effects, and energy densities require separate continuum-mechanics sources.

## Bridge P5 - scalar transport on curved surfaces

The source gives the Laplace-Beltrami operator:

\[
\Delta_S f
=\frac{1}{\sqrt a}\partial_\alpha
(\sqrt a\,a^{\alpha\beta}\partial_\beta f).
\]

This is a geometry operator. It can enter externally sourced physical PDEs such as:

\[
\partial_t c=D\Delta_S c
\]

only after the diffusion coefficient, conservation law, units, boundary conditions, and physical interpretation are independently specified.

## Bridge P6 - tangent flux/divergence

The source divergence

\[
\nabla\cdot A=\frac{1}{\sqrt a}\partial_\alpha(\sqrt aA^\alpha)
\]

supports conservation-law formulations on a surface. Again, the conserved quantity and flux law are physics/model inputs, not provided by differential geometry alone.

## Bridge P7 - curvature-energy hypotheses

Gaussian and mean curvature are mathematically established by the source. Any energy of the form

\[
\mathcal E=\int_S \Phi(H,K,\ldots)\,dA
\]

is classified as a physics/model extension unless independently sourced. This prevents a common error: inferring an energy law merely because curvature quantities exist.

## Physics reproducibility contract

Every physical use of source geometry must state:

```yaml
geometry_source: SOCHI-DG-2017-UPLOADED
geometry_equations: []
physics_source: ...
physical_state: ...
constitutive_law: ...
units: ...
boundary_conditions: ...
initial_conditions: ...
conservation_law: ...
validation_evidence: ...
```

## Prohibited inference

Do not make any of the following transitions without independent evidence:

```text
geodesic -> globally optimal engineering recovery
curvature -> physical stress
mean curvature -> energy
Gaussian curvature -> fragility
topological genus -> infrastructure redundancy
Laplace-Beltrami -> a specific transport process
```

These can become research hypotheses, but not source facts.
