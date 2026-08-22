# DG-LC-001 — Levi-Civita connection gold-standard record

**Evidence state:** `[S]` theorem/source; `[D]` coordinate derivation; `[C]` symbolic implementation; `[V]` benchmark identities only after tests pass.  
**Proof status:** `PR2` — source-linked derivation outline. This repository does **not** claim a machine-checked proof.  
**Scope:** local-coordinate computation on a declared smooth Riemannian chart. It is not a global manifold constructor.

## 1. Mathematical object

Let \((M,g)\) be a smooth Riemannian manifold. The **Levi-Civita connection** is the unique affine connection \(\nabla\) on \(TM\) satisfying

\[
\nabla g=0
\]

(metric compatibility) and

\[
T^\nabla(X,Y)=\nabla_XY-\nabla_YX-[X,Y]=0
\]

(torsion free).

### Hypotheses

- \(M\) is a smooth manifold;
- \(g\) is a smooth Riemannian metric (smooth, symmetric, positive definite on each tangent space);
- local coordinates used computationally lie in a chart where the metric matrix is non-degenerate.

The implementation checks symmetry and that the determinant is not **identically** zero. It does not prove global positive-definiteness or infer the full chart domain from symbolic expressions.

## 2. Koszul formula and uniqueness

For vector fields \(X,V,W\), the Levi-Civita connection is characterized by the Koszul identity

\[
\begin{aligned}
2g(\nabla_VW,X)
={}&V\,g(W,X)+W\,g(X,V)-X\,g(V,W)\\
&-g(V,[W,X])+g(W,[X,V])+g(X,[V,W]).
\end{aligned}
\]

Metric compatibility expands the first three derivatives of inner products, while torsion freedom rewrites the Lie-bracket terms. After cancellation, the left-hand side remains. Since a non-degenerate metric determines a vector from all of its inner products with \(X\), the identity determines \(\nabla_VW\) uniquely.

Conversely, the right-hand side is \(C^\infty(M)\)-linear in \(X\), so it defines a covector and hence, through the metric, a unique vector field \(\nabla_VW\). The standard checks then establish the connection axioms, metric compatibility, and zero torsion. This record gives the derivation path, not a line-by-line formal proof; therefore the proof status remains `PR2`.

## 3. Coordinate derivation

Let \((q^1,\ldots,q^n)\) be local coordinates, \(\partial_i=\partial/\partial q^i\), and

\[
g_{ij}=g(\partial_i,\partial_j).
\]

Coordinate vector fields commute, so \([\partial_i,\partial_j]=0\). Put \(V=\partial_i\), \(W=\partial_j\), \(X=\partial_m\) in the Koszul formula:

\[
2g(\nabla_{\partial_i}\partial_j,\partial_m)
=\partial_i g_{jm}+\partial_j g_{im}-\partial_m g_{ij}.
\]

Define Christoffel coefficients by

\[
\nabla_{\partial_i}\partial_j=\Gamma^a_{ij}\partial_a.
\]

Then

\[
2\Gamma^a_{ij}g_{am}=\partial_i g_{jm}+\partial_j g_{im}-\partial_m g_{ij}.
\]

Multiplication by \(g^{mk}\) and contraction over \(m\) yield

\[
\boxed{\Gamma^k_{ij}=\frac12g^{k\ell}(\partial_i g_{j\ell}+\partial_j g_{i\ell}-\partial_\ell g_{ij})}.
\]

This coordinate formula is the one implemented in `geometry/connections.py`.

## 4. Coordinate behavior

Christoffel symbols are not tensor components. For an overlap map \(x=x(q)\),

\[
\Gamma'^k_{ij}=\frac{\partial q^k}{\partial x^a}\left[\frac{\partial^2 x^a}{\partial q^i\partial q^j}+\Gamma^a_{bc}\frac{\partial x^b}{\partial q^i}\frac{\partial x^c}{\partial q^j}\right].
\]

The inhomogeneous second-derivative term is essential. The test suite verifies this explicitly by transforming the zero Cartesian connection on the Euclidean plane to polar coordinates and comparing it with the connection computed directly from \(g=\operatorname{diag}(1,r^2)\).

## 5. Curvature convention

The implementation declares

\[
R^\rho{}_{\sigma\mu\nu}=\partial_\mu\Gamma^\rho_{\nu\sigma}-\partial_\nu\Gamma^\rho_{\mu\sigma}+\Gamma^\rho_{\mu\lambda}\Gamma^\lambda_{\nu\sigma}-\Gamma^\rho_{\nu\lambda}\Gamma^\lambda_{\mu\sigma}.
\]

Ricci contraction is \(\operatorname{Ric}_{\sigma\nu}=R^\rho{}_{\sigma\rho\nu}\), and scalar curvature is \(\mathcal R=g^{\sigma\nu}\operatorname{Ric}_{\sigma\nu}\). Under this convention the unit two-sphere has \(\mathcal R=2\), and on a two-dimensional Riemannian manifold \(\mathcal R=2K\).

## 6. Independent verification paths

The V1 benchmark suite requires all of the following:

1. **Cartesian plane:** \(g=I\), all Christoffel symbols and curvature vanish.
2. **Polar plane:** \(g=\operatorname{diag}(1,r^2)\); selected Christoffel symbols are nonzero but scalar curvature is zero.
3. **Coordinate transformation:** Cartesian zero connection transforms to the direct polar result through the inhomogeneous connection law.
4. **Unit sphere:** \(g=\operatorname{diag}(1,\sin^2\theta)\) gives scalar curvature \(2\) on the regular spherical chart.
5. **Standard torus:** intrinsic scalar curvature equals twice the independent analytic Gaussian-curvature formula already present in `torus_geometry.py`.
6. **Independent numerical differentiation:** finite-difference metric derivatives at a sphere point agree with the symbolic Christoffel coefficients within a declared tolerance.
7. **Structural invariants:** generated torsion and metric-compatibility residuals simplify to zero on the symbolic benchmarks.

A successful test establishes only the declared benchmark identity. It does not establish empirical validity, global regularity, or correctness on arbitrary user-supplied metrics.

## 7. Sources

### Primary open derivation anchor

Shlomo Sternberg, *Semi-Riemann Geometry and General Relativity*, Chapter 3, §§3.8–3.9, pp. 65–67. Harvard-hosted notes. The source states Levi-Civita existence/uniqueness, gives the Koszul formula, explains the uniqueness/existence argument, and derives the coordinate Christoffel formula.

`https://people.math.harvard.edu/~shlomo/docs/semi_riemannian_geometry.pdf`

### Independent open coordinate/moving-frame anchor

MIT 18.966, *Geometry of Manifolds*, Spring 2005 Lecture Notes, Lecture 1, §§1.2–1.3, pp. 3–5. The notes characterize metric compatibility and torsion freedom, give the coordinate Christoffel formula, and present the uniqueness argument through moving frames.

`https://math.mit.edu/~mrowka/Math966notesSp05.pdf`

### Bibliographic architecture

John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed. The official author page and front matter place “The Levi-Civita Connection” in Chapter 5. The repository does not treat the author webpage as a substitute for theorem-level page/equation locators.

`https://sites.math.washington.edu/~lee/Books/RM/`

## 8. Limitations and stop rules

- A coordinate chart may become singular even when the underlying geometry is regular.
- Symbolic nonzero determinant is not a proof of positive-definiteness over an undeclared domain.
- Riemann-tensor sign conventions differ in the literature; comparisons must translate conventions explicitly.
- SymPy simplification can fail to recognize mathematically zero expressions; tests use conservative trigonometric expansion/simplification and analytic oracles rather than treating raw expression form as truth.
- No formal theorem prover artifact exists for this theorem in V1; `PR5` is prohibited.
