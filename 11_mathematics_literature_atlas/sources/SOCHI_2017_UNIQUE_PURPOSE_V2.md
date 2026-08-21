# Sochi 2017 - Literature and Provenance Atlas V2

**Unique purpose:** maintain bibliographic identity, source structure, named mathematical results, notation synonyms, dependencies, and provenance. It does not replace the mathematical derivations stored in other modules.

## Bibliographic identity

```yaml
source_id: SOCHI-DG-2017-UPLOADED
author: Taha Sochi
title: Introduction to Differential Geometry of Space Curves and Surfaces
internal_date: March 2017
internal_date_evidence: signed preface, London
pdf_pages: 252
sha256_current_upload: 75c340af6f6086b8aa4d9884c2911fd2e5f0250d6f7ccacfb158c9475b1dd4ad
external_identifier_status: not inferred from filename
```

The displayed upload filename resembles an external identifier, but no arXiv ID, DOI, ISBN, publisher, or edition is asserted unless directly verified from the source or an independent bibliographic source.

## Chapter atlas

| Chapter | Printed pages | Main concepts |
|---|---:|---|
| Nomenclature | 7-10 | symbols and conventions |
| 1 Preliminaries | 11-54 | topology, maps, regularity, metric preliminaries, Christoffel/Riemann/Ricci |
| 2 Curves in Space | 55-82 | curve parameterization, Frenet frame, curvature, torsion, transport |
| 3 Surfaces in Space | 83-140 | surface charts, metric, curvature tensor, fundamental forms, Gauss-Weingarten, Codazzi |
| 4 Curvature | 141-192 | normal/geodesic/principal/Gaussian/mean curvature, Egregium, Gauss-Bonnet |
| 5 Special Curves | 193-220 | geodesics, curvature lines, asymptotic lines and related classes |
| 6 Special Surfaces | 221-232 | ruled, developable, isometric, tangent, minimal surfaces |
| 7 Tensor Differentiation | 233-240 | covariant/absolute derivatives and surface differential operators |
| References | 241 | source bibliography |

## Named-result index

- Euler characteristic / Euler-Poincare characteristic;
- Euler characteristic-genus relation;
- Schur theorem (background discussion);
- Frenet-Serret formulae;
- fundamental theorem of space curves;
- Bonnet formula for geodesic torsion;
- Gauss equations;
- Weingarten equations;
- Codazzi-Mainardi equations;
- Gauss-Codazzi equation;
- fundamental theorem of surfaces;
- Bonnet theorem in the surface-uniqueness discussion;
- Euler theorem for normal curvature/principal directions;
- Meusnier theorem;
- Gauss Theorema Egregium;
- Gauss-Bonnet theorem.

Each named result should eventually receive a record with:

```yaml
name: ...
source_section: ...
source_equations: []
statement_scope: ...
assumptions: []
prerequisites: []
consequences: []
reproduction_artifacts: []
verification_artifacts: []
historical_primary_source: null
```

The `historical_primary_source` field remains null until independently researched; Sochi's textbook discussion is not automatically treated as the historical primary source.

## Notation synonym atlas

| Source notation | Equivalent/common role |
|---|---|
| `u,v` and `u^1,u^2` | surface coordinates |
| `E,F,G` | first fundamental form / covariant metric coefficients |
| `e,f,g` | second fundamental form / covariant curvature coefficients |
| `a_{alpha beta}` | covariant surface metric tensor |
| `b_{alpha beta}` | covariant surface curvature tensor |
| `b^alpha_beta` | mixed curvature tensor / shape-operator representation |
| `T,N,B` | Frenet tangent, normal, binormal |
| `kappa,tau` | curve curvature and torsion |
| `K,H` | Gaussian and mean curvature |
| `chi,g` | Euler characteristic and genus |

The source deliberately uses multiple common notations. The atlas preserves those synonyms so downstream code can normalize them explicitly rather than silently.

## Concept dependency graph

```text
calculus + linear algebra + tensor notation
  -> coordinate maps and regularity
  -> tangent bases
  -> metric
  -> connection
  -> intrinsic curvature

surface normal + second derivatives
  -> curvature tensor
  -> shape operator
  -> principal curvatures
  -> H, K

metric + curvature tensor
  -> Gauss-Weingarten
  -> compatibility
  -> surface reconstruction theory

K + Euler characteristic
  -> Gauss-Bonnet

connection + curve velocity
  -> geodesic equation / covariant transport
```

## Provenance graph

Every stable artifact links backward:

```text
artifact
 -> module-specific source note
 -> equation_registry_v2.json
 -> SOURCE_AUDIT_V2.md
 -> uploaded PDF
```

and forward to:

```text
implementation
 -> tests
 -> reproduction report
 -> visualization
 -> application/research extension
```

## Literature expansion policy

The book itself says its mathematical background is not comprehensive. Therefore, this atlas is the place to add independent foundational literature for:

- tensor analysis;
- modern Riemannian geometry;
- topology;
- differential equations;
- numerical differential geometry;
- geometric mechanics;
- engineering applications.

New sources must be marked as `FOUNDATIONAL`, `HISTORICAL`, `COMPUTATIONAL`, `PHYSICS`, or `ENGINEERING` so their evidentiary role remains explicit.
