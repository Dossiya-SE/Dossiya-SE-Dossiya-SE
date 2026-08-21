# Literature Atlas Record — SOCHI-DG-2017-UPLOADED

## Bibliographic identity

**Author:** Taha Sochi  
**Title:** *Introduction to Differential Geometry of Space Curves and Surfaces*  
**Internal date evidence:** preface signed “London, March 2017”  
**User-supplied artifact:** `2501.0039v1.pdf`  
**Extent:** 252 PDF pages  
**Primary scope stated by source:** differential geometry of space curves and surfaces, largely using a tensor-calculus approach.

No DOI, ISBN, journal, publisher, or edition claim is entered until independently verified from reliable metadata. This prevents metadata guessing.

## Scope classification

| Axis | Atlas classification |
|---|---|
| Mathematical field | differential geometry |
| Main objects | curves and 2-D surfaces embedded mainly in 3-D space |
| Main formalism | tensor calculus / coordinate differential geometry |
| Level | intermediate, per source preface |
| Strongest use in ecosystem | foundational definitions/equations + worked geometry + exercise anchors |
| Explicit source limitation | preliminary mathematics is not comprehensive |

## Chapter evidence map

| Chapter | Printed pages | Main atlas topics |
|---|---:|---|
| Nomenclature | 7–10 | symbol ontology, tensor/index conventions |
| 1 Preliminaries | 11–54 | local/global, intrinsic/extrinsic, topology, maps, metrics, Christoffel, Riemann/Ricci |
| 2 Curves in Space | 55–82 | parameterization, Frenet frame, curvature, torsion, parallel propagation |
| 3 Surfaces in Space | 83–140 | surface maps, metric, curvature tensor, fundamental forms, Gauss-Weingarten/Codazzi-Mainardi |
| 4 Curvature | 141–192 | normal/geodesic/principal/Gaussian/mean curvature, Theorema Egregium, Gauss–Bonnet |
| 5 Special Curves | 193–220 | geodesics, lines of curvature, asymptotic lines, special curve classes |
| 6 Special Surfaces | 221–232 | quadratic, ruled, developable, isometric, tangent, minimal surfaces |
| 7 Tensor Differentiation | 233–240 | covariant/absolute derivatives, surface divergence/Laplacian |
| References | 241 | source bibliography |

## Named-result index

This index records named mathematical constructs appearing in the source; it does not claim historical priority beyond the source terminology.

- Euler characteristic / Euler–Poincaré characteristic — §1.4.1, Eq. (46).
- Euler–Lagrange variational principle — §1.4.2, Eq. (53).
- Christoffel symbols — §1.4.9, Eqs. (62)–(87).
- Riemann–Christoffel curvature tensor — §1.4.10.
- Ricci tensor/scalar — §1.4.11.
- Frenet frame / Frenet–Serret formulae — §§2.2, 2.5, Eqs. (136)–(139).
- Lancret relation/theorem context — Chapter 2.
- Darboux vector/frame concepts — Chapters 2 and 4.
- Codazzi–Mainardi equations — §3.9.1.
- Meusnier theorem — §4.2.1.
- Gauss Theorema Egregium — §4.7.
- Gauss–Bonnet theorem — §4.8, local Eq. (386), global Eq. (396).
- Bonnet formula for geodesic torsion — §2.4, Eq. (135).

## Concept dependency graph

```text
parameterization + regularity
        -> tangent bases
        -> metric / first fundamental form
        -> Christoffel connection
        -> geodesics + covariant differentiation
        -> Riemann curvature
        -> Gaussian curvature
        -> Theorema Egregium
        -> Gauss–Bonnet <-> Euler characteristic / genus

curve derivatives
        -> Frenet frame
        -> curvature + torsion
        -> Frenet–Serret dynamics
        -> special curves / osculating geometry

surface normal + second derivatives
        -> second fundamental form
        -> principal curvatures
        -> Gaussian/mean curvature
        -> local shape + minimal surfaces
```

## Source-to-repository coverage

The source has been mapped to all twelve ecosystem modules through `/sources/sochi_2017/source_manifest.json`. Each module receives a different transformation of the source rather than duplicate prose:

- foundations -> canonical mathematics;
- models -> reusable mathematical state structures;
- examples -> executable objects;
- reproductions -> independent replication targets;
- skills -> competency evidence;
- visualization -> mathematical-art reconstructions;
- computing -> code translation and tool roles;
- verification -> oracles/invariants;
- physics -> source-bounded geometric-physics bridges;
- engineering -> dual-source transfer contracts;
- literature atlas -> provenance/dependency record;
- research lab -> falsifiable extensions.

## Computing literature linked to this source

The atlas also tracks software literature used to implement the mathematics. Examples include NumPy (Harris et al., 2020, DOI `10.1038/s41586-020-2649-2`), SciPy (Virtanen et al., 2020, DOI `10.1038/s41592-019-0686-2`), SymPy (Meurer et al., 2017, DOI `10.7717/peerj-cs.103`), Julia (Bezanson et al., 2017, DOI `10.1137/141000671`), DifferentialEquations.jl (Rackauckas & Nie, 2017, DOI `10.5334/jors.151`), PyVista (Sullivan & Kaszynski, 2019, DOI `10.21105/joss.01450`), Manifolds.jl (Axen et al., 2023, DOI `10.1145/3618296`), and Lean (de Moura et al., 2015, DOI `10.1007/978-3-319-21401-6_26`). Full role descriptions are maintained in module 07.

## Provenance status

- source identity: **verified from uploaded artifact**;
- internal date: **verified from preface**;
- chapter/page structure: **verified from table of contents and parsed/rendered PDF**;
- equation anchors used in executable code: **must be individually rendered-page checked before `verified` promotion**;
- external publication metadata for the book: **not asserted**.

## Citation

Sochi, T. (2017). *Introduction to Differential Geometry of Space Curves and Surfaces*. User-supplied PDF; internal preface date March 2017.
