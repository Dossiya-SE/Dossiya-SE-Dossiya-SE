# Differential geometry mastery ladder

| Level | Competency | Demonstration |
|---|---|---|
| L0 | Recognize | identify curve, surface, tangent, normal, metric, curvature |
| L1 | Understand | explain intrinsic vs extrinsic geometry |
| L2 | Derive | derive $g_{ij}$, selected $\Gamma^k{}_{ij}$, and $K$ for benchmark surfaces |
| L3 | Apply | solve a geodesic initial-value problem numerically |
| L4 | Implement | build tested Python/Julia/Wolfram implementations and publication figures |
| L5 | Generalize | formulate and defend a new geometry-aware research model |

## Required L2 benchmark

For the torus, derive

$$
E=(R+r\cos v)^2,\quad F=0,\quad G=r^2.
$$

Then derive or independently verify

$$
K(v)=\frac{\cos v}{r(R+r\cos v)}.
$$

## Required L4 benchmark

1. integrate a torus geodesic;
2. compute energy drift;
3. render the surface with curvature-based appearance;
4. verify Gauss--Bonnet numerically;
5. document convergence and limitations.

## L5 research challenge

Define a non-arbitrary metric on an infrastructure state manifold from interpretable costs or sensitivities, then determine whether shortest or minimum-action recovery paths have operational meaning.
