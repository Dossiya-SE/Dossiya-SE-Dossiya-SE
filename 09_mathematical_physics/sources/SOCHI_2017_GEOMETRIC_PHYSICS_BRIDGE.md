# Sochi 2017 — Geometric Physics Bridge

**Unique purpose:** identify mathematical structures in the source that legitimately support mathematical-physics modeling, while clearly separating source mathematics from later physical interpretation.

## Source-supported bridge 1 — variational structure

In the preliminaries, Sochi introduces the first variation through a Gâteaux-derivative form and the Euler–Lagrange variational principle (printed p. 32, Eqs. 52–53). This provides a legitimate bridge from differential geometry to variational mechanics.

For a functional

\[
\mathcal A[q]=\int L(q,\dot q,t)\,dt,
\]

a stationary trajectory satisfies the Euler–Lagrange equations under the usual regularity and endpoint assumptions. The **physical meaning of `L` is not supplied by the geometry book** and must come from an appropriate mechanics source.

## Source-supported bridge 2 — geodesic motion

Sochi's surface geodesic equation is

\[
\ddot u^\alpha+\Gamma^\alpha_{\beta\gamma}\dot u^\beta\dot u^\gamma=0
\]

(Sochi, 2017, §5.7, Eq. 418). In mathematical physics this is a natural model for free motion constrained by a metric, but the physical metric and parameter interpretation must be separately justified.

**Permitted source claim:** the equation defines geodesics intrinsically through the metric connection.

**Extension claim:** interpreting those geodesics as physical least-action trajectories is an application requiring an external mechanics/relativity source.

## Source-supported bridge 3 — moving frames and angular kinematics

The Frenet–Serret system (Sochi Eqs. 136–143) evolves an orthonormal moving frame along a curve:

\[
T'=\kappa N,\qquad N'=\tau B-\kappa T,\qquad B'=-\tau N.
\]

The source also introduces the Darboux vector

\[
d=\tau T+\kappa B.
\]

This is mathematically useful for rod/filament kinematics, trajectories, and moving-frame mechanics. Constitutive laws, energy functionals, forces, and material parameters are **extensions**, not claims from Sochi.

## Source-supported bridge 4 — curvature and field operators

Chapter 7 gives surface divergence and Laplacian forms using the surface metric (Sochi, 2017, Eqs. 474–475). These are foundational operators for diffusion, heat, wave, and transport equations on curved surfaces.

The bridge is:

\[
\text{surface geometry}
\rightarrow
\nabla_S,\ \nabla_S\!\cdot,\ \Delta_S
\rightarrow
\text{PDE model on a manifold}.
\]

The PDE itself and its constitutive/source terms require domain-specific physical evidence.

## Source-supported bridge 5 — curvature/topology constraints

Global Gauss–Bonnet connects total Gaussian curvature to Euler characteristic:

\[
\iint_S K\,d\sigma=2\pi\chi
\]

(Sochi, 2017, Eq. 396). In physical models of shells, membranes, or interfaces, this can create topology-sensitive constraints. Any energetic interpretation, however, must cite the relevant physical theory separately.

## Source-supported bridge 6 — minimal surfaces

The source treats minimal surfaces and uses vanishing mean curvature as their defining geometric condition in Chapter 6 / Exercises 6.42–6.46. This is directly relevant to equilibrium interfaces such as idealized soap films, but a capillarity/energy argument must be cited from physics rather than inferred from geometry alone.

## Research implementation pattern

Every mathematical-physics artifact should use two provenance channels:

```text
MATHEMATICAL SOURCE
Sochi 2017 -> geometric object/equation/invariant

PHYSICAL SOURCE
mechanics / thermodynamics / continuum physics source -> physical law, energy, units, constitutive assumptions
```

Only after both are present may the combined model be promoted from `geometric analogy` to `physics-grounded model`.

## Citation

Sochi, T. (2017). *Introduction to Differential Geometry of Space Curves and Surfaces*. User-supplied PDF; internal preface date March 2017.
