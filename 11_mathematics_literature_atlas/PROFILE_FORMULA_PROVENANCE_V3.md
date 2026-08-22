# Profile Formula Provenance — V3

**Unique purpose of this module:** provide the bibliographic and epistemic provenance layer for formulas that are displayed across the `Dossiya-SE` profile.

This file does not replace domain-specific derivations or software tests. It answers a narrower question:

> **Where does a displayed mathematical object come from, and what kind of claim is it?**

## Provenance classes

| Class | Meaning | Example |
|---|---|---|
| `PRIMARY_SOURCE` | directly anchored to a book/paper/standard | Sochi geodesic equation |
| `STANDARD_IDENTITY` | standard mathematical definition used by project | covariance, graph Laplacian |
| `PROJECT_MODEL` | explicit project-level mathematical abstraction | coupled infrastructure dynamics |
| `DERIVED_PROJECT_RESULT` | derived from a project's assumptions | an analytical bias expression or reduced model consequence |
| `COMPUTED_OUTPUT` | numerical output tied to code/configuration | Monte Carlo quantile |
| `EMPIRICAL_ESTIMATE` | estimate tied to observed data and procedure | fitted/calibrated parameter |
| `RESEARCH_HYPOTHESIS` | new proposed relation requiring tests | curvature as fragility proxy |
| `ENGINEERING_TARGET` | design requirement/target | prototype voltage or performance threshold |

## Source-grounded differential geometry

`SOCHI-DG-2017-UPLOADED` is the current primary differential-geometry source for the ecosystem's curve/surface foundation. Its scope is deliberately bounded to an intermediate tensor-calculus-oriented treatment of space curves and surfaces.

Profile-visible source objects may include:

| Formula family | Source role | Required anchor |
|---|---|---|
| surface metric | intrinsic geometry | source section/page/equation where available |
| Christoffel symbols | Levi-Civita connection | source Eq. 63/general form |
| Riemann-Christoffel tensor | intrinsic curvature | source Eqs. 88–89 |
| curve curvature/torsion | space-curve geometry | source Eqs. 126, 129 |
| Frenet–Serret system | moving frame | source Eqs. 136–138 |
| Gaussian curvature | surface curvature | source curvature chapter/equation registry |
| Gauss–Bonnet | global curvature/topology | source theorem section |
| geodesic equation | intrinsic path equation | source Eq. 418 |
| covariant/absolute derivative | tensor differentiation | source Ch. 7 equation registry |

Before a source formula is promoted to stable profile use, its equation/page should be checked against the rendered PDF under the source-audit policy.

## Cross-domain profile provenance

The profile also displays repository-specific mathematics. These formulas remain under their own domain evidence rather than being attributed to the Sochi source.

### Infrastructure dynamics / viability

Provenance class: `PROJECT_MODEL` unless a specific external theorem is being cited.

Examples:

```math
\dot X=F(X,Z,m,u,\eta;\theta),
```

```math
\mathcal V_R
=
\{x_0\in K_R:\exists u(\cdot),\;X(t)\in K_R\;\forall t\ge0\}.
```

### Probability / inverse problems

A Bayesian posterior relation such as

```math
\pi(\theta\mid y)\propto L(y\mid\theta)\pi_0(\theta)
```

is a standard inferential identity/modeling relation; a particular posterior estimate is a separate `COMPUTED_OUTPUT` or `EMPIRICAL_ESTIMATE` depending on the data.

### Energy systems

An energy-balance equation is a conservation/accounting model under declared boundaries. Project parameter values and performance outputs require separate engineering/data provenance.

### Quantitative finance

SDE model families, calibration objectives, numerical pricing outputs, and empirical market calibration have distinct provenance states. A calibrated parameter is not the same kind of object as the model equation.

### Machine learning

Empirical-risk expressions define training/evaluation structures. A displayed loss equation does not establish that a trained model exists or generalizes.

### Metrology / valuation

Measurement equations distinguish latent quantity, measurement error, and reported valuation. Field validity requires instrument calibration, measurement-system analysis, and empirical evidence.

## Profile formula record contract

A stable profile formula record should contain:

```json
{
  "id": "DOMAIN-TOPIC-NNN",
  "name": "...",
  "latex": "...",
  "provenance_class": "...",
  "evidence_state": "S|D|M|C|V|E|H|T",
  "source_or_project": "...",
  "anchor": "...",
  "assumptions": ["..."],
  "domain": "...",
  "repository_role": "...",
  "verification": "...",
  "limitations": "..."
}
```

The public profile currently maintains a compact machine-readable registry in `Dossiya-SE/Dossiya-SE/mathematical-art/formula_registry.json`. This literature-atlas module is the provenance authority for deciding how source-grounded entries should be classified and anchored.

## Prohibited provenance errors

1. A formula from a textbook must not be presented as an original formula.
2. A project abstraction must not be attributed to a source that did not propose it.
3. A computed result must not be labeled empirical unless real-world observations support it.
4. A simulated state must not be labeled observed.
5. A visual resemblance must not establish a mathematical equivalence.
6. A repository README equation must not imply implementation if executable evidence is absent.
7. A citation to software does not replace a citation to the mathematics, and a citation to mathematics does not replace software/version provenance for computation.

## Canonical profile provenance chain

```text
formula ID
→ provenance class
→ source/project anchor
→ assumptions/domain
→ derivation/model
→ software implementation
→ verification
→ validation/evidence
→ displayed claim
```

Every arrow in this chain is auditable independently.
