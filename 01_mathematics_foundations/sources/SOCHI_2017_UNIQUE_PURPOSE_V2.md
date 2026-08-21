# Sochi 2017 - Foundations V2

**Unique purpose:** canonical mathematical statements only: definitions, notation, assumptions, identities, theorem anchors, and dependency relations.

**Source:** Taha Sochi, *Introduction to Differential Geometry of Space Curves and Surfaces* (preface dated March 2017), source ID `SOCHI-DG-2017-UPLOADED`.

## Scope boundary

This source is adopted as a primary foundation for **classical differential geometry of curves and surfaces in the tensor-calculus style used by the book**. It is not a complete foundation for all of mathematics. The book explicitly says its preliminary background is intentionally restricted.

## Canonical dependency graph

```text
parameterization r
    |
    +--> curve derivative -> T -> N,B -> kappa,tau -> Frenet-Serret
    |
    +--> surface derivatives E_alpha
             |
             +--> metric a_{alpha beta} -> Gamma -> Riemann -> Ricci -> intrinsic K
             |
             +--> normal n -> curvature tensor b_{alpha beta}
                                  |
                                  +--> shape operator b^alpha_beta
                                  +--> principal curvatures kappa_1,kappa_2
                                  +--> H and K

metric + curvature tensor
    -> Gauss-Weingarten
    -> Gauss-Codazzi compatibility
    -> fundamental theorem of surfaces

K + topology
    -> Gauss-Bonnet
```

## Canonical regularity conditions

### Curve

For a parameterized curve `r(t)`, regularity requires a nonzero tangent/velocity at the point under consideration. Any implementation that divides by `|r_dot|` must therefore guard against `|r_dot| = 0`.

### Surface patch

For `r(u,v)` the source requires a rank-2 Jacobian, equivalently independent surface basis vectors:

\[
E_1\times E_2\neq 0.
\]

A numerical geometry routine must reject or flag points where the induced metric determinant approaches zero.

## Metric and intrinsic geometry

The surface metric has matrix representation

\[
[a_{\alpha\beta}] =
\begin{bmatrix}E&F\\F&G\end{bmatrix}
\qquad \text{(Sochi Eq. 193)}
\]

with

\[
a=EG-F^2>0
\]

for a regular Riemannian surface patch.

The inverse metric is

\[
[a^{\alpha\beta}]
=\frac{1}{EG-F^2}
\begin{bmatrix}G&-F\\-F&E\end{bmatrix}
\qquad \text{(Eq. 194)}.
\]

Christoffel symbols are determined by the metric:

\[
\Gamma^k_{ij}=\frac12g^{kl}(\partial_jg_{il}+\partial_i g_{jl}-\partial_lg_{ij})
\qquad \text{(Eq. 63)}.
\]

The Riemann-Christoffel tensor is then built from `Gamma` and its derivatives (Eq. 89). This chain formalizes the book's intrinsic-geometry principle:

\[
g\longrightarrow\Gamma\longrightarrow R.
\]

## Extrinsic surface geometry

The covariant surface curvature tensor is symmetric and represented by

\[
[b_{\alpha\beta}]=
\begin{bmatrix}e&f\\f&g\end{bmatrix}
\qquad \text{(Eq. 222)}.
\]

The mixed tensor / shape operator is

\[
b^\alpha{}_{\beta}=a^{\alpha\gamma}b_{\gamma\beta}
\qquad \text{(Eq. 223 context)}.
\]

Its trace and determinant generate the two principal scalar invariants used by the source:

\[
H=\frac12\operatorname{tr}(b^\alpha{}_{\beta}),
\qquad
K=\det(b^\alpha{}_{\beta})
\qquad \text{(Eq. 225)}.
\]

## Principal curvature eigenproblem

The source formulates principal curvature as a generalized eigenvalue problem between the second and first fundamental forms. Non-trivial tangent increments require

\[
\det\begin{bmatrix}
e-\kappa E & f-\kappa F\\
f-\kappa F & g-\kappa G
\end{bmatrix}=0,
\]

which expands to Sochi Eq. (346). This is the canonical foundation for numerical principal-curvature computation.

## Gaussian and mean curvature

\[
K=\kappa_1\kappa_2
\qquad \text{(Eq. 355)},
\]

and

\[
K=\frac{eg-f^2}{EG-F^2}=\frac{b}{a}=\frac{R_{1212}}{a}
\qquad \text{(Eq. 356)}.
\]

The source uses this identity to connect extrinsic and intrinsic formulations and to motivate Theorema Egregium.

Mean curvature is

\[
H=\frac{\kappa_1+\kappa_2}{2}
\qquad \text{(Eq. 382)},
\]

or

\[
H=\frac{eG-2fF+gE}{2(EG-F^2)}
=\frac12\operatorname{tr}(b^\alpha{}_{\beta})
\qquad \text{(Eq. 383)}.
\]

Orientation rule: reversing the unit normal reverses the sign of `H` and the principal curvatures, while `K` is unchanged.

## Gauss-Weingarten and compatibility

Gauss equations:

\[
\partial_\beta E_\alpha
=\Gamma^\gamma_{\alpha\beta}E_\gamma+b_{\alpha\beta}n
\qquad \text{(Eq. 274)}.
\]

Weingarten equations:

\[
\partial_\alpha n=-b^\beta{}_{\alpha}E_\beta
\qquad \text{(Eq. 279)}.
\]

Codazzi-Mainardi:

\[
b_{\alpha\beta;\gamma}=b_{\alpha\gamma;\beta}
\qquad \text{(Eq. 298)}.
\]

These are compatibility statements, not optional numerical decorations. A reconstructed surface model must satisfy the relevant integrability conditions within tolerance.

## Curves and Frenet frame

For a generally parameterized curve:

\[
\kappa=\frac{\|\dot r\times\ddot r\|}{\|\dot r\|^3}
\qquad \text{(Eq. 126)},
\]

\[
\tau=\frac{\dot r\cdot(\ddot r\times\dddot r)}{\|\dot r\times\ddot r\|^2}
\qquad \text{(Eq. 129)}.
\]

For arc length `s` and the sign convention used in the source:

\[
T'=\kappa N,\qquad
N'=\tau B-\kappa T,\qquad
B'=-\tau N
\qquad \text{(Eqs. 136-138)}.
\]

The source explicitly warns that torsion sign convention differs among authors; repository artifacts must record the convention.

## Geodesics

The intrinsic geodesic equation is

\[
\frac{d^2u^\alpha}{ds^2}
+\Gamma^\alpha_{\beta\gamma}
\frac{du^\beta}{ds}
\frac{du^\gamma}{ds}=0
\qquad \text{(Eq. 418)}.
\]

The equation is local. It must not be silently reinterpreted as a proof of global shortest-path optimality.

## Topology and Gauss-Bonnet

For polyhedral decompositions:

\[
\chi=V+F-E
\qquad \text{(Eq. 46)}.
\]

For orientable genus `g`:

\[
\chi=2(1-g)
\qquad \text{(Eq. 47)}.
\]

Global Gauss-Bonnet:

\[
\iint_S K\,d\sigma=2\pi\chi
\qquad \text{(Eq. 396)}.
\]

This gives a controlled local-geometry/global-topology bridge.

## Tensor differentiation and field operators

Chapter 7 supplies the covariant/absolute derivative layer and metric compatibility. It also gives the surface divergence

\[
\nabla\cdot A=\frac{1}{\sqrt a}\partial_\alpha(\sqrt a A^\alpha)
\qquad \text{(Eq. 474)},
\]

and Laplace-Beltrami operator

\[
\nabla^2 f
=\frac{1}{\sqrt a}\partial_\alpha
\left(\sqrt a\,a^{\alpha\beta}\partial_\beta f\right)
\qquad \text{(Eq. 475)}.
\]

These equations are the mathematical foundation for later manifold-field models; physical interpretations require separate evidence.

## Foundation promotion rule

A source equation becomes `canonical` in this repository only after:

1. source page/equation anchor recorded;
2. parameter/domain conditions recorded;
3. notation normalized without changing meaning;
4. ambiguity or sign convention documented;
5. executable use paired with a verification oracle.
