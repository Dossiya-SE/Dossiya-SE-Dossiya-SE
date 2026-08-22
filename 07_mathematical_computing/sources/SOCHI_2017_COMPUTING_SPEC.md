# Sochi 2017 — Source-to-Computation Specification

**Unique purpose:** translate source mathematics into auditable computational kernels across languages without changing the mathematics silently.

**Primary source:** Sochi (2017), especially curve/surface parameterizations, Christoffel symbols, Frenet–Serret equations, curvature, geodesics, and tensor differentiation.

## Translation contract

For every computational implementation derived from the book:

1. cite the printed page and source equation(s);
2. state source notation and code notation;
3. state parameter domains and regularity assumptions;
4. separate exact/symbolic quantities from numerical approximations;
5. expose numerical tolerances explicitly;
6. include at least one independent verification oracle;
7. record software/library versions for research outputs.

## Kernel families

### K1 — parameterized curves

Source: Chapters 1–2.

Inputs: `t`, parameter values.

Outputs: `r(t)`, derivatives, speed, optional arc length, `T,N,B,kappa,tau` where defined.

Recommended implementations:

- SymPy for exact differentiation and simplification;
- NumPy for vectorized evaluation;
- SciPy for quadrature/root solving if reparameterization is needed;
- Julia for high-performance parameter sweeps.

### K2 — parameterized surfaces

Source: §§1.4.3, 3.2–3.6.

Inputs: `(u,v)` and geometry parameters.

Outputs:

$$
X,\ X_u,\ X_v,\ n,\ g_{ij},\ b_{ij},\ dA,
$$

plus curvature fields where regular.

### K3 — connection and intrinsic curvature

Source: §§1.4.9–1.4.11 and Chapter 4.

Compute

$$
\Gamma^k_{ij},\quad R^i{}_{jkl},\quad R_{ij},\quad R,
$$

with the source convention documented. Symbolic implementations should simplify tensor symmetries and metric compatibility.

### K4 — Frenet–Serret dynamics

Source: Eqs. (136)–(139).

Integrate

$$
Y'=A(\kappa,\tau)Y,
$$

where `A` is skew-symmetric under the source convention. Monitor orthonormal-frame drift as a numerical diagnostic.

### K5 — geodesic dynamics

Source: Eq. (418).

Integrate

$$
\ddot u^\alpha=-\Gamma^\alpha_{\beta\gamma}\dot u^\beta\dot u^\gamma.
$$

The implementation must distinguish coordinate singularities from true geometric failure and must not label every geodesic globally shortest.

### K6 — tensor differentiation

Source: Chapter 7.

Implement covariant and absolute derivatives, then test metric compatibility and contraction/product rules. This kernel is suitable for symbolic regression tests because the source supplies explicit tensor identities.

## Precision policy

- **symbolic:** exact rational/algebraic form where practical;
- **float64:** default visualization and routine numerical work;
- **high precision:** theorem/reproduction checks sensitive to cancellation;
- **interval/validated numerics:** optional future extension when rigorous numerical bounds are required.

## Cross-language equivalence

A cross-language reproduction must compare invariant outputs, not textual code similarity. Example: Python, Julia, and Wolfram implementations of a torus should agree on `g`, `K`, and selected geodesic invariants within declared tolerances.

## Citation

Sochi, T. (2017). *Introduction to Differential Geometry of Space Curves and Surfaces*. User-supplied PDF; internal preface date March 2017.
