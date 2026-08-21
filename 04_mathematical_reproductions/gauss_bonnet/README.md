# Reproduction: Gauss--Bonnet on sphere and torus

Target identity for a closed orientable surface \(S\):

\[
\int_S K\,dA=2\pi\chi(S).
\]

Benchmarks:

- unit sphere: \(K=1\), area \(4\pi\), \(\chi=2\), so integral \(=4\pi\);
- standard torus: \(\chi=0\), so integral \(=0\).

`verify.py` evaluates both integrals numerically without inserting the expected values into the integrands. The numerical error is reported against the topological target.
