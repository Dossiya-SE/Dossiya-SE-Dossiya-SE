# Sochi Differential Geometry Source Audit V2

## Purpose

This document is the provenance and quality-control record for the user-supplied PDF currently named `2501.0039v1.pdf` / `2501.0039v1(1).pdf` in the conversation workspace.

The file content identifies the work as:

- **Author:** Taha Sochi
- **Title:** *Introduction to Differential Geometry of Space Curves and Surfaces*
- **Internal date:** London, March 2017, from the signed preface
- **PDF extent:** 252 pages
- **Primary mathematical orientation:** tensor-calculus-based differential geometry of curves and surfaces

The uploaded filename resembles an arXiv-style identifier, but the repository does **not** infer an arXiv identifier, DOI, ISBN, publisher, or edition from that filename. Only bibliographic facts visible in the supplied file are treated as source-grounded.

## Binary provenance

For the upload mounted in the current workspace:

```text
SHA-256: 75c340af6f6086b8aa4d9884c2911fd2e5f0250d6f7ccacfb158c9475b1dd4ad
Bytes:   6,972,718
Pages:   252
```

The conversation contains another upload with the same displayed filename and matching title/page/chapter/equation content. This is treated as a **content-level duplicate candidate**, not as a proven binary duplicate, because only the current mounted file was hashed here.

## Source-boundary rule

This book is a primary foundation for the ecosystem's **differential geometry of space curves and surfaces**. It is not promoted to a universal foundation for analysis, probability, algebra, numerical methods, engineering, or physics. The preface itself states that the preliminary mathematical background is restricted to material directly needed by the book.

Therefore:

```text
Sochi source -> differential-geometry foundation
other domains -> require independent foundational sources
engineering claims -> require independent engineering evidence
physics claims -> require independent physics evidence unless explicitly mathematical
software claims -> require software/documentation/scholarly citations
```

## Pagination rule

The PDF cover is page 1. The printed book page numbering begins on the preface. For most printed pages >= 1:

```text
PDF page = printed page + 1
```

Every extracted artifact should record both the printed page and PDF page when a precise anchor is important.

## Extraction classes

Each extracted item must be typed as one of:

1. `DEFINITION`
2. `NOTATION`
3. `ASSUMPTION`
4. `EQUATION`
5. `THEOREM`
6. `DERIVATION_LINK`
7. `EXAMPLE`
8. `EXERCISE`
9. `FIGURE_CONCEPT`
10. `SOURCE_LIMITATION`
11. `EXTENSION`

`EXTENSION` means the item is our own mathematical, physical, engineering, computational, or research development. It must never be presented as a claim of Sochi.

## Verification states

Every source-derived artifact has one of four states:

- `S0_PARSED`: obtained from parsed text only;
- `S1_RENDER_CHECKED`: equation/figure/statement checked against the rendered PDF page;
- `S2_ANALYTICALLY_CHECKED`: independently derived or tested analytically;
- `S3_COMPUTATIONALLY_CHECKED`: verified by executable tests or numerical invariants.

A stable executable artifact should normally reach at least `S1 + S2` or `S1 + S3`.

## Core coverage

The source covers:

- preliminaries, notation, local/global and intrinsic/extrinsic classification;
- topology prototypes and Euler characteristic;
- coordinate mappings, Jacobians, regularity, intrinsic distance;
- Christoffel symbols, Riemann-Christoffel curvature, Ricci tensor/scalar;
- space curves, Frenet frame, curvature, torsion, geodesic torsion;
- surface parameterizations, metric tensor, fundamental forms;
- Gauss-Weingarten and Codazzi-Mainardi equations;
- normal/geodesic/principal/Gaussian/mean curvature;
- Theorema Egregium and Gauss-Bonnet;
- special curves and special surfaces;
- tensor differentiation on surfaces, including covariant/absolute derivatives and surface differential operators.

## High-value source anchors

Examples of anchors used across the ecosystem include:

- Eq. (46): Euler characteristic `chi = V + F - E`;
- Eq. (47): `chi = 2(1-g)` for orientable genus `g`;
- Eq. (55): Jacobian for surface mapping / regularity context;
- Eqs. (62)-(63): Christoffel symbols;
- Eqs. (88)-(89): Riemann-Christoffel curvature;
- Eq. (96): Ricci scalar;
- Eqs. (126), (129): curve curvature and torsion;
- Eqs. (136)-(139): Frenet-Serret system;
- Eqs. (193)-(197): surface metric tensor and transformation behavior;
- Eqs. (218)-(225): curvature tensor, shape operator invariants;
- Eqs. (271)-(282): Gauss-Weingarten equations and normal derivative relations;
- Eqs. (296)-(301): Codazzi-Mainardi / Gauss-Codazzi compatibility;
- Eqs. (343)-(346): principal-curvature eigenproblem;
- Eqs. (355)-(358): Gaussian curvature and determinant relations;
- Eq. (383): mean curvature;
- Eq. (396): global Gauss-Bonnet;
- Eq. (418): geodesic equation;
- Ch. 7: covariant/absolute differentiation;
- Eqs. (474)-(475): surface divergence and Laplace-Beltrami operator.

## Copyright-safe handling

The repository stores:

- compact paraphrase;
- equations needed for mathematical reproducibility;
- page/equation anchors;
- independently written code;
- independently regenerated figures;
- tests and derivations.

It does not store scans of the book, long copied prose, or copied figures.

## Repository uniqueness rule

The same source is **not duplicated semantically** across modules. Each top-level module receives only the source material needed for its own contract:

- foundations -> canonical mathematical statements;
- models -> formal model objects and constraints;
- examples -> worked/parameterized objects;
- reproductions -> independently reproducible targets;
- skills -> competency progression and exercise mapping;
- visualization -> visual encodings and figure reconstruction specifications;
- computing -> algorithms and software/tool roles;
- verification -> independent mathematical/computational oracles;
- mathematical physics -> controlled geometry-to-physics bridge;
- engineering -> controlled mathematics-to-engineering transfer;
- literature atlas -> provenance and intellectual map;
- research lab -> explicitly new, falsifiable extensions.
