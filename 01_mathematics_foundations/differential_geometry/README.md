# Differential geometry foundation

## Surface

Let \(X:U\subset\mathbb R^2\to\mathbb R^3\) be a regular parameterized surface with local coordinates \(q^1=u,q^2=v\).

The metric is

\[
g_{ij}=\left\langle \partial_iX,\partial_jX\right\rangle.
\]

The Levi-Civita connection in coordinates is

\[
\Gamma^k{}_{ij}
=\frac12g^{k\ell}
(\partial_i g_{j\ell}+\partial_jg_{i\ell}-\partial_\ell g_{ij}).
\]

A geodesic satisfies

\[
\ddot q^k+\Gamma^k{}_{ij}\dot q^i\dot q^j=0.
\]

## Curves

For a unit-speed regular curve \(\gamma(s)\),

\[
T=\gamma'(s),\qquad T'=\kappa N,\qquad B=T\times N,
\]

with Frenet--Serret equations

\[
T'=\kappa N,\quad N'=-\kappa T+\tau B,\quad B'=-\tau N.
\]

## Torus benchmark

For \(R>r>0\),

\[
X(u,v)=((R+r\cos v)\cos u,(R+r\cos v)\sin u,r\sin v).
\]

The induced metric is diagonal:

\[
g=\mathrm{diag}((R+r\cos v)^2,r^2),
\]

and Gaussian curvature is

\[
K(v)=\frac{\cos v}{r(R+r\cos v)}.
\]

The area element is

\[
dA=r(R+r\cos v)\,du\,dv.
\]

Therefore

\[
\int_{0}^{2\pi}\int_{0}^{2\pi}K\,dA
=\int_0^{2\pi}\int_0^{2\pi}\cos v\,du\,dv
=0
=2\pi\chi(T^2).
\]
