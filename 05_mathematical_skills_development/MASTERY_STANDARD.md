# Mathematics Mastery Standard — MMS-001

**Status:** `PROPOSED_ACTIVE_REVIEW`  
**Scope:** Mathematics Research Ecosystem  
**Purpose:** Prevent claim inflation between exposure, competence, computation, verification, and research.

## 1. Governing principle

A mathematical topic `τ` has a vector-valued competence state

```math
\mathbf c(\tau)=
(c_R,c_U,c_D,c_P,c_I,c_V,c_G),
```

with components:

- `R` — recognize;
- `U` — understand;
- `D` — derive;
- `P` — prove / independently solve;
- `I` — implement;
- `V` — verify;
- `G` — generalize / research transfer.

The vector is intentionally **non-compensatory**. High computational skill cannot erase a proof gap; a proof cannot substitute for empirical validation; visual sophistication cannot raise mathematical status.

## 2. Promotion rule

Let `𝒢_k(τ)` be the set of gates required for maturity level `k`. Promotion is permitted only if

```math
\boxed{
P_k(\tau)
=
\bigwedge_{g\in\mathcal G_k(\tau)} g(\tau)
=1
}
```

where every required gate is binary at promotion time: `PASS` or not `PASS`.

Suggested gate sets:

| Level | Required gates |
|---|---|
| `L0 Recognize` | object identification, notation/domain recognition |
| `L1 Understand` | L0 + definition explanation + assumptions + interpretation |
| `L2 Derive` | L1 + independent derivation + dimensional/domain checks |
| `L3 Prove/Solve` | L2 + proof or independent solution + counterexample/edge-case reasoning |
| `L4 Implement/Verify` | L3 + tested implementation + numerical/symbolic verification + error analysis |
| `L5 Generalize/Research` | L4 + literature boundary + new question/model + falsification criteria + limitations |

A topic may have `L4` computational competence without `L3` proof competence when proof is not structurally required; such exceptions must be declared in the topic record with rationale. The system must never infer equivalence automatically.

## 3. Evidence states

The profile-wide evidence states remain authoritative:

| Code | Meaning | Permitted claim |
|---|---|---|
| `[S]` | source-grounded | accurately attributed mathematical/source statement |
| `[D]` | derived | independently derived from declared assumptions |
| `[M]` | model | mathematical representation or hypothesis |
| `[C]` | computed | produced by symbolic/numerical computation |
| `[V]` | verified | passed declared mathematical/computational checks |
| `[E]` | empirical | supported by observations/data under declared protocol |
| `[H]` | hypothesis | unresolved proposition or transfer claim |
| `[T]` | target | engineering/design objective, not achieved fact |

Evidence states are not an ordinal ladder. For example, `[E]` does not replace `[D]`, and `[V]` does not imply `[E]`.

## 4. Required topic record

Every stable mathematical topic must record at minimum:

```yaml
topic_id: LA-EIG-001
title: Eigenvalues and eigenvectors
domain: linear_algebra
status: ACTIVE
source_provenance: []
assumptions: []
objects: []
competencies:
  recognize: NOT_TESTED
  understand: NOT_TESTED
  derive: NOT_TESTED
  prove_or_solve: NOT_TESTED
  implement: NOT_TESTED
  verify: NOT_TESTED
  generalize: NOT_TESTED
verification:
  tests: []
  tolerances: []
limitations: []
research_connections: []
```

Allowed competency states are defined in `progress/competency_registry.json`.

## 5. Independent-work rule

The following do **not** constitute mastery evidence by themselves:

- watching a lecture;
- reading a solution;
- copying a proof;
- retyping source code;
- obtaining a plausible plot;
- receiving a correct answer from a CAS/LLM;
- matching a textbook result without an independent check.

Independent evidence should include one or more of:

1. closed-notes derivation;
2. unseen problem solution;
3. proof reconstruction;
4. counterexample construction;
5. implementation from mathematical specification;
6. error/convergence study;
7. reproduction of a source result;
8. oral/written explanation of assumptions and failure modes.

## 6. Numerical verification contract

For a numerical result `\hat y_h` approximating `y`, a verification claim must state a diagnostic such as

```math
E(h)=\|\hat y_h-y\|
```

or, when the exact solution is unavailable, an internally justified surrogate such as residual, conservation defect, mesh-refinement difference, or independent-method discrepancy.

A statement such as `the solver converged` is insufficient without:

- convergence criterion;
- tolerance;
- iteration/discretization details;
- conditioning or stability considerations where relevant;
- reproducible environment;
- failure cases or limitations.

## 7. Proof and derivation contract

A derivation must identify:

1. starting assumptions;
2. definitions invoked;
3. theorem identities used;
4. nontrivial algebraic/logical steps;
5. domain restrictions;
6. result;
7. independent check.

A proof must additionally identify the proof strategy when useful: direct, contrapositive, contradiction, induction, construction, exhaustion, probabilistic, variational, or other justified method.

## 8. Research-transition gate

A topic enters the research layer only when the transfer package includes:

```math
\boxed{
G_R
=
G_{\mathrm{definition}}
\land G_{\mathrm{assumption}}
\land G_{\mathrm{provenance}}
\land G_{\mathrm{derivation}}
\land G_{\mathrm{implementation}}
\land G_{\mathrm{verification}}
\land G_{\mathrm{falsification}}
}
```

A failed required gate blocks promotion. No weighted score can compensate for a failed critical gate.

## 9. Differential-geometry transfer rule

For an application state space `X` to be called a differentiable/Riemannian manifold in research, the artifact must explicitly define or justify, as applicable:

- point/state semantics;
- topology;
- charts/coordinates and transition regularity;
- tangent-space meaning;
- metric `g` and its interpretation;
- differentiability assumptions;
- distance/geodesic meaning;
- curvature or connection meaning if used;
- estimator/calibration procedure;
- validation/falsification conditions.

A curved visualization is not evidence that these structures exist.

## 10. Mathematics-art verification

For a visual encoding map

```math
\Phi:\mathcal M\rightarrow\mathcal V,
```

where `𝓜` is the mathematical object and `𝓥` its rendered representation, the scientific contract requires a declared invariant set `I` such that

```math
I(\mathcal M)=I(\Phi(\mathcal M))
```

within declared numerical/rendering tolerance.

Potential invariants include topology, orientation, coordinates, critical points, level-set ordering, field extrema, signs, units, adjacency, and error bands.

## 11. Completion meaning

The repository should prefer statements such as:

- `source reviewed`;
- `derivation independently reproduced`;
- `benchmark verified within tolerance`;
- `competency L3 passed for topic X`;
- `research transfer remains hypothesis`.

It should avoid broad unsupported statements such as `mastered linear algebra`, `proved the model`, or `validated differential geometry for infrastructure` unless the exact claim is operationally defined and evidenced.
