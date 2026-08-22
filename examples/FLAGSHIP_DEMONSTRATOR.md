# Flagship demonstrator: one object, twelve skills

The torus + coupled-infrastructure example is designed to prove that the ecosystem is not a folder taxonomy.

| Skill | Concrete artifact |
|---|---|
| Foundations | metric, Christoffel symbols, curvature, Frenet--Serret equations |
| Models | manifold-constrained viability formulation |
| Examples | analytic torus implementation |
| Reproductions | Gauss--Bonnet numerical reproduction |
| Skills development | L0--L5 differential-geometry ladder |
| Visualization art | curvature-driven surface rendering |
| Computing | Python, Julia, Wolfram, Asymptote, TikZ, GLSL |
| Verification | analytic identities, invariant tests, topology benchmarks |
| Mathematical physics | geodesic action / kinetic-energy interpretation |
| Engineering applications | four-sector P-W-T-SW viability demonstrator |
| Literature atlas | canonical references and provenance protocol |
| Research lab | curvature/viability/interface hypotheses |

## End-to-end acceptance test

A V1 release is acceptable when:

1. Python tests pass;
2. torus $K$ has correct sign at inner/outer equators;
3. torus Gauss--Bonnet error is numerically near zero;
4. sphere Gauss--Bonnet error converges toward zero;
5. geodesic energy drift is below the stated tolerance;
6. engineering demonstrator states remain numerically bounded;
7. every top-level skill has at least one concrete artifact;
8. exploratory claims remain clearly marked exploratory.
