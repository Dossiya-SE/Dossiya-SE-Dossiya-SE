# Sochi 2017 — Differential Geometry Foundation

**Module purpose:** preserve canonical definitions, notation, assumptions, equations, and theorem anchors. This file is not an example gallery, a programming tutorial, or an engineering interpretation.

**Primary source:** Taha Sochi, *Introduction to Differential Geometry of Space Curves and Surfaces*, user-supplied PDF `2501.0039v1.pdf`; preface dated London, March 2017.

## Source scope used here

The book explicitly frames itself as an intermediate treatment of differential geometry of curves and surfaces, largely through tensor calculus. Its preliminary material is intentionally not comprehensive. Accordingly, this repository treats it as a primary foundation for **curve/surface differential geometry**, while other mathematical domains require additional primary sources.

## Canonical notation layer

From the Nomenclature and §§1.1–1.4 (printed pp. 7–49; PDF pp. 8–50):

- `s`: natural curve parameter / arc length;
- `t`: general curve parameter;
- `T, N, B`: tangent, principal normal, binormal unit vectors;
- `E_alpha`: covariant surface basis vectors;
- `n`: surface unit normal;
- `a_{alpha beta}`: surface covariant metric tensor;
- `b_{alpha beta}`: surface covariant curvature tensor;
- `E,F,G`: first fundamental form coefficients;
- `e,f,g`: second fundamental form coefficients;
- `Gamma^gamma_{alpha beta}`: surface Christoffel symbols of the second kind;
- `K`: Gaussian curvature;
- `H`: mean curvature;
- `kappa`, `tau`: curve curvature and torsion;
- `chi`: Euler characteristic.

Greek indices are used for surface coordinates and Latin indices for space coordinates in the book's principal convention. Any repository artifact that changes this notation must state the conversion.

## Structural definitions

### Regular curve

A parameterized curve is regular at a point when its velocity exists and is nonzero. See §2.1, printed pp. 55–59.

### Regular surface patch

For a mapping `S(u,v) = (S1,S2,S3)`, regularity requires sufficient differentiability and a Jacobian matrix of rank 2. The source gives the equivalent basis condition

$$
E_1\times E_2 \neq 0.
$$

See §1.4.3, printed pp. 34–36, especially Eq. (55) and the discussion immediately following it.

### Intrinsic versus extrinsic geometry

The source distinguishes properties determined by the metric / first fundamental form from properties requiring embedding information / the second fundamental form. This distinction is foundational and must be preserved in later modeling. See §1.3.2, printed pp. 15–16.

## Core equations

### Christoffel symbols

From §1.4.9, printed pp. 43–46:

$$
\Gamma^k_{ij}=\frac12 g^{kl}
\left(\partial_j g_{il}+\partial_i g_{jl}-\partial_l g_{ij}\right),
\tag{Sochi Eq. 63}
$$

with symmetry in the lower paired indices for the Levi-Civita connection used in the text.

### Riemann-Christoffel curvature

From §1.4.10, printed pp. 46–48:

$$
R^i{}_{jkl}
=\partial_k\Gamma^i_{jl}-\partial_l\Gamma^i_{jk}
+\Gamma^r_{jl}\Gamma^i_{rk}-\Gamma^r_{jk}\Gamma^i_{rl}.
\tag{Sochi Eq. 89}
$$

The book uses vanishing of the Riemann-Christoffel tensor as the intrinsic-flatness criterion.

### Curve curvature and torsion

For a generally parameterized space curve `r(t)`, §2.3 gives

$$
\kappa=\frac{\lVert \dot r\times \ddot r\rVert}{\lVert\dot r\rVert^3},
\tag{Sochi Eq. 126, equivalent form}
$$

and

$$
\tau=\frac{\dot r\cdot(\ddot r\times \dddot r)}{\lVert\dot r\times\ddot r\rVert^2}.
\tag{Sochi Eq. 129}
$$

The formulas require the regularity/nondegeneracy conditions stated in the surrounding text.

### Frenet–Serret system

From §2.5, printed p. 72:

$$
\frac{dT}{ds}=\kappa N,
\qquad
\frac{dN}{ds}=\tau B-\kappa T,
\qquad
\frac{dB}{ds}=-\tau N.
\tag{Sochi Eqs. 136–138}
$$

The source explicitly notes that torsion sign convention varies in the literature. Reproductions must therefore preserve or document the convention.

### Geodesic equation

From §5.7:

$$
\frac{d^2u^\alpha}{ds^2}
+\Gamma^\alpha_{\beta\gamma}
\frac{du^\beta}{ds}
\frac{du^\gamma}{ds}=0.
\tag{Sochi Eq. 418}
$$

The text emphasizes that this is an intrinsic condition because the Christoffel symbols depend on the surface metric.

### Tensor differentiation

Chapter 7 gives metric compatibility and covariant/absolute differentiation. In particular,

$$
a_{\alpha\beta\mid\gamma}=0
\tag{Sochi Eq. 441}
$$

and for a contravariant surface vector,

$$
A^\alpha{}_{;\beta}=\frac{\partial A^\alpha}{\partial u^\beta}
+\Gamma^\alpha_{\gamma\beta}A^\gamma.
\tag{Sochi Eq. 450}
$$

See printed pp. 233–238.

## Topological bridge

The source defines, for polyhedral surfaces,

$$
\chi=V+F-E,
\tag{Sochi Eq. 46}
$$

and for orientable genus `g`,

$$
\chi=2(1-g).
\tag{Sochi Eq. 47}
$$

These are used later with Gauss–Bonnet. See printed pp. 27–28 and §4.8.

## Promotion rule

A formula extracted here is `source-grounded`, not automatically `verified`. Promotion to verified requires:

1. source equation/page checked against rendered PDF;
2. domain assumptions recorded;
3. notation conversion documented if any;
4. analytic or machine-checkable invariant test where possible.

See `/sources/sochi_2017/EXTRACTION_PROTOCOL.md`.
