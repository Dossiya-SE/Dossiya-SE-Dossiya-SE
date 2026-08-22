# Sochi 2017 — Model Primitives

**Unique purpose of this module:** convert source geometry into reusable mathematical model primitives. This file does not serve as the canonical definition store (module 01), example gallery (module 03), or verification oracle (module 08).

## 1. Curve model primitive

Source anchor: Chapter 2, especially §§2.1–2.3, printed pp. 55–70.

A parameterized curve is represented as

$$
C:I\subset\mathbb R\to\mathbb R^n,
\qquad t\mapsto r(t).
$$

A model instance must record:

- parameter domain `I`;
- whether `t` is general or natural (`s`);
- regularity set where `\dot r\neq0`;
- differentiability required by the requested quantities;
- curvature `\kappa` and torsion `\tau` when defined;
- orientation convention.

For natural parameterization, the source uses `|dr/ds|=1`.

## 2. Frenet-frame state model

Source anchor: §§2.2 and 2.5, printed pp. 60–73.

Define the moving state

$$
Y(s)=\begin{bmatrix}T(s)\\N(s)\\B(s)\end{bmatrix}.
$$

Then the source Frenet–Serret system is a first-order matrix ODE

$$
Y'(s)=
\begin{bmatrix}
0&\kappa&0\\
-\kappa&0&\tau\\
0&-\tau&0
\end{bmatrix}Y(s).
$$

This is a reusable model primitive for reconstruction of a curve from curvature/torsion data, subject to the source's regularity and sign-convention conditions.

## 3. Surface model primitive

Source anchors: §1.4.3 and Chapter 3, printed pp. 34–36 and 83–131.

Represent a patch as

$$
X:U\subset\mathbb R^2\to\mathbb R^3,
\qquad (u,v)\mapsto X(u,v).
$$

Model contract:

- `X` has the differentiability required by the derived quantities;
- `rank(DX)=2` on the regular patch;
- tangent basis `E_1=X_u`, `E_2=X_v`;
- metric `a_{\alpha\beta}=E_\alpha\cdot E_\beta`;
- unit normal only where `E_1\times E_2\neq0`;
- extrinsic curvature quantities require embedding information.

## 4. Intrinsic metric model

Source anchors: §§1.3.2, 1.4.4, 3.3, and 3.5.

The metric model is

$$
G(u,v)=
\begin{bmatrix}
E&F\\F&G
\end{bmatrix},
\qquad EG-F^2>0
$$

on a regular Riemannian surface patch.

Derived model objects include:

- arc length;
- intrinsic angles;
- surface area element;
- Christoffel symbols;
- intrinsic distance;
- geodesic dynamics;
- intrinsic curvature quantities.

The determinant/positive-definiteness conditions are not optional metadata: they are model-domain guards.

## 5. Geodesic initial-value model

Source anchor: §5.7, especially Sochi Eq. (418).

State:

$$
y=(u^1,u^2,\dot u^1,\dot u^2).
$$

Dynamics:

$$
\ddot u^\alpha=-\Gamma^\alpha_{\beta\gamma}(u)
\dot u^\beta\dot u^\gamma.
$$

Required model inputs:

- metric or explicit Christoffel field;
- initial point `u(0)`;
- initial tangent `\dot u(0)`;
- parameter convention;
- integration interval;
- coordinate-domain boundaries.

The source states that geodesic equations are generally nonlinear and need not have closed-form explicit solutions.

## 6. Curvature-state model

Source anchors: Chapter 4, especially §§4.4–4.9, printed pp. 152–181.

For a regular surface, a local curvature state may be represented as

$$
\mathcal K(P)=(\kappa_1,\kappa_2,K,H),
$$

where `\kappa_1,\kappa_2` are principal curvatures, `K` is Gaussian curvature, and `H` is mean curvature.

This state supports local shape classification and must preserve orientation dependence: Gaussian curvature is orientation independent, while the sign of mean curvature depends on the chosen surface normal convention.

## 7. Parallel-transport model

Source anchor: §2.7 and Chapter 7.

For a surface vector field `A^alpha` along `u^beta(t)`, parallel propagation is modeled by vanishing absolute derivative:

$$
\frac{\delta A^\alpha}{\delta t}=0.
$$

This yields a path-dependent transport model on curved surfaces. Path dependence is part of the mathematics, not numerical noise.

## 8. Topology-curvature model bridge

Source anchors: §1.4.1 and §4.8.

For suitable compact orientable closed surfaces, the model connects:

$$
\chi=2(1-g)
$$

with the global Gauss–Bonnet integral. This is the foundation for topology-aware verification, not a license to infer topology from an arbitrary sampled mesh without checking hypotheses.

## Explicit non-source extensions

The following concepts may be built elsewhere in the ecosystem but are **not attributed to this book** unless separately sourced:

- infrastructure viability manifolds;
- resilience metrics;
- climate forcing;
- network interdependency models;
- digital twins;
- optimal-control objectives;
- stochastic uncertainty models.

When these use a geometry primitive above, their records must mark the geometry as `SOCHI-DG-2017-UPLOADED` and the application layer as `EXT`.
