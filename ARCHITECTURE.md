# Architecture

## Purpose

This bootstrap is a reference implementation for twelve planned repositories. The split boundary is stable: each top-level numbered directory may become an independent repository later.

## Dependency graph

```text
Foundations ──> Models ──> Examples ──> Computing ──> Visualization
    │              │                         │              │
    └──────────────┴──────────────> Verification <─────────┘
                                      │
                                      v
                               Reproductions
                                      │
                                      v
                            Mathematical Physics
                                      │
                                      v
                           Engineering Applications
                                      │
                                      v
                                Research Lab

Literature Atlas supplies provenance to every layer.
Skills Development supplies learning paths to every layer.
```

## Artifact invariant

No stable mathematical artifact is complete unless it records:

1. definition and notation;
2. domain/codomain and regularity assumptions;
3. governing formula or theorem;
4. derivation or explicit provenance;
5. dimensions/units where physical;
6. executable implementation where computational;
7. verification strategy;
8. limitations and failure modes;
9. source references.

## Flagship demonstrator

The shared V1 demonstrator is the standard torus

$$
X(u,v)=((R+r\cos v)\cos u,(R+r\cos v)\sin u,r\sin v),
\qquad R>r>0.
$$

For this parameterization,

$$
E=(R+r\cos v)^2,\quad F=0,\quad G=r^2,
$$

and

$$
K(v)=\frac{\cos v}{r(R+r\cos v)}.
$$

The Gauss--Bonnet integral over the torus should be zero because $\chi(T^2)=0$.

A second demonstrator couples mathematics to engineering through a four-sector state $x=(P,W,T,SW)$, a time-dependent coupling matrix, hazard forcing, and a viable set.
