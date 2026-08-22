# Verification

Verification is layered:

1. **analytic identities** — compare implementation against known formulas;
2. **invariants** — e.g. geodesic kinetic energy should be conserved for an affinely parameterized geodesic;
3. **topological benchmarks** — Gauss--Bonnet on sphere and torus;
4. **convergence** — reduce time step or increase quadrature resolution;
5. **domain guards** — reject invalid geometry such as $R\le r$ for this embedded-ring-torus benchmark.

`tests/test_geometry.py` implements the minimal CI gate.
