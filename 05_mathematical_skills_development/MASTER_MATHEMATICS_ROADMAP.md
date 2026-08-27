# Master Mathematics Roadmap — MMR-001

**Status:** `PROPOSED_ACTIVE_REVIEW`  
**Objective:** Build mathematical fluency, maturity, computation, verification, and research capability without conflating exposure with mastery.

## Governing trajectory

```math
\boxed{
\text{Foundations}
\rightarrow
\text{Maturity}
\rightarrow
\text{Core Research Mathematics}
\rightarrow
\text{Geometry + Dynamics}
\rightarrow
\text{Research Synthesis}
}
```

Progression is dependency-driven, not calendar-driven. A later topic may begin before every earlier topic is complete, but every research claim must satisfy its actual prerequisites.

---

## Phase A — Mathematical fluency

### A1. College algebra

Core objects:

```math
f:\mathbb R\to\mathbb R,\qquad
ax+b=0,\qquad
p(x),\qquad
e^x,\qquad\log x.
```

Required outcomes:

- manipulate equations and inequalities reliably;
- understand functions as mappings rather than formulas only;
- reason about domains, ranges, inverse functions, scaling, and units;
- use exponentials/logarithms without symbolic fragility.

### A2. Linear algebra

Core objects:

```math
V,\quad A:V\to W,\quad
\ker A,\quad \operatorname{im}A,\quad
Av=\lambda v,\quad
A=U\Sigma V^\top.
```

Research bridge:

```math
\dot x=Ax,
\qquad
J_F(x^*),
\qquad
L=D-A,
\qquad
g=[g_{ij}].
```

Minimum L4 benchmarks:

1. solve and interpret linear systems;
2. verify rank/nullity numerically and symbolically;
3. compute eigendecompositions and residuals;
4. implement SVD-based least squares;
5. connect spectra to stability and network structure.

### A3. Differential and integral calculus

Core objects:

```math
f'(x),\qquad
\int_a^b f(x)\,dx,\qquad
\sum_{n=0}^{\infty}a_n.
```

Required outcomes:

- derivative as local linearization;
- integral as accumulation/measure precursor;
- Fundamental Theorem of Calculus;
- Taylor approximation and remainder awareness;
- sequence/series intuition sufficient for later analysis.

### A4. Probability

Core objects:

```math
(\Omega,\mathcal F,P),\qquad
E[X],\qquad
\operatorname{Var}(X),\qquad
P(A\mid B).
```

Required outcomes:

- conditional probability and Bayes' rule;
- random variables and transformations;
- common distributions;
- expectation, variance, covariance;
- joint/conditional distributions;
- laws of large numbers and central-limit intuition before formal treatment.

### A5. Differential equations

Core object:

```math
\dot x=f(t,x).
```

Required outcomes:

- first/second-order ODEs;
- linear systems;
- phase portraits;
- equilibria and local stability;
- numerical integration;
- conservation/energy checks where applicable.

### A6. Python scientific computing

Python is treated as an implementation layer, not a substitute for mathematics.

Core stack:

```text
NumPy → SciPy → SymPy → Matplotlib
        ↓
     testing + reproducibility
```

Minimum benchmark: derive a result, implement it, verify it independently, and document error/limitations.

---

## Phase B — Mathematical maturity

### B1. Logic and proof

Required proof modes:

- direct proof;
- contrapositive;
- contradiction;
- induction;
- construction;
- counterexample.

Core logical distinction:

```math
\forall x\,\exists y\;P(x,y)
\neq
\exists y\,\forall x\;P(x,y).
```

### B2. Discrete mathematics

Core topics:

- sets, relations, functions;
- combinatorics;
- graph basics;
- recurrence;
- proof structures;
- discrete probability.

### B3. Multivariable calculus

Core objects:

```math
\nabla f,\qquad
J_f=\left[\frac{\partial f_i}{\partial x_j}\right],\qquad
H_f=\left[\frac{\partial^2f}{\partial x_i\partial x_j}\right].
```

Research bridges: optimization, nonlinear dynamics, geometry, machine learning, control.

### B4. Real analysis

Core transition:

```math
\text{calculate a limit}
\rightarrow
\text{prove why the limit exists}.
```

Canonical definition:

```math
\forall\varepsilon>0\;\exists\delta>0:
0<|x-a|<\delta
\Rightarrow
|f(x)-L|<\varepsilon.
```

Required topics:

- completeness of `ℝ`;
- sequences and series;
- continuity;
- differentiation/integration from rigorous definitions;
- compactness and convergence;
- metric-space introduction.

### B5. Advanced linear algebra

Required topics:

- abstract vector spaces;
- dual spaces;
- linear operators;
- spectral theory in finite dimensions;
- bilinear/quadratic forms;
- positive definiteness;
- matrix factorizations and conditioning.

---

## Phase C — Core research mathematics

### C1. Numerical analysis

Core questions:

```math
\text{Is the method consistent? Stable? Convergent? Conditioned?}
```

Required topics:

- floating-point error;
- root finding;
- interpolation/approximation;
- numerical differentiation/integration;
- linear systems;
- ODE solvers;
- conditioning and backward error.

### C2. Optimization

Core form:

```math
\min_x f(x)
\quad\text{s.t.}\quad
g_i(x)\le0,\;h_j(x)=0.
```

Required topics:

- convexity;
- linear/quadratic programming;
- KKT conditions;
- duality;
- sensitivity;
- constrained nonlinear optimization.

### C3. Graph theory and network science

Core objects:

```math
G=(V,E),\qquad
A,\qquad
L=D-A.
```

Required topics:

- connectivity;
- paths/cuts;
- flows;
- spectra;
- percolation/network robustness foundations;
- multilayer/interdependent-network representations with explicit semantics.

### C4. Dynamical systems

Core form:

```math
\dot x=F(x;\theta).
```

Required topics:

- fixed points;
- linearization;
- stability;
- bifurcations;
- invariant sets;
- Lyapunov functions;
- nonlinear trajectories.

### C5. Mathematical statistics

Core topics:

```math
\hat\theta_n\xrightarrow{P}\theta,
\qquad
\sqrt n(\hat\theta_n-\theta)
\xrightarrow{d}N(0,\Sigma).
```

Required outcomes:

- likelihood;
- estimation;
- uncertainty intervals;
- hypothesis testing;
- regression/model diagnostics;
- Bayesian foundations;
- asymptotic reasoning.

### C6. Stochastic processes

Core objects:

```math
\{X_t:t\ge0\},\qquad
W_t,\qquad
dX_t=\mu(X_t,t)dt+\sigma(X_t,t)dW_t.
```

Research bridges: finance, reliability, climate risk, uncertain dynamics.

---

## Phase D — Geometry, fields, control, and viability

### D1. Topology

Core topics:

- topological spaces;
- open/closed sets;
- continuity;
- compactness;
- connectedness;
- product/quotient constructions;
- manifold prerequisites.

### D2. Differential geometry

Core objects:

```math
M,\quad T_pM,\quad X\in\Gamma(TM),\quad
\omega\in\Omega^k(M),\quad g.
```

### D3. Riemannian geometry

Core objects:

```math
\nabla_XY,\qquad
\nabla_{\dot\gamma}\dot\gamma=0,\qquad
R(X,Y)Z.
```

Required research discipline: no application manifold without explicit state semantics, topology/charts, metric meaning, and validation pathway.

### D4. Partial differential equations

Canonical families:

```math
u_t=\alpha\Delta u,
\qquad
u_{tt}=c^2\Delta u,
\qquad
\Delta u=f.
```

Required topics:

- classification;
- boundary/initial conditions;
- weak/variational ideas;
- numerical discretization;
- conservation and stability.

### D5. Control theory

Canonical form:

```math
\dot x=f(x,u,t),
\qquad
u=\pi(x,t).
```

Required topics:

- controllability/observability;
- feedback;
- optimal control;
- constraints;
- robustness.

### D6. Viability theory

Core object:

```math
\operatorname{Viab}_F(K)
=
\left\{x_0\in K:\exists u(\cdot),\;x(t)\in K\;\forall t\ge0\right\}.
```

The viability kernel must not be treated as a generic “resilience score.” State, constraint set, dynamics, controls, and uncertainty semantics must be explicit.

### D7. Uncertainty quantification

Required topics:

- parameter uncertainty;
- aleatory vs epistemic distinctions where operationally useful;
- sensitivity analysis;
- propagation;
- surrogate models;
- calibration/validation separation;
- probabilistic and interval/robust alternatives where justified.

---

## Phase E — Research mathematics

A research topic must move through

```math
\boxed{
\text{Question}
\rightarrow
\text{Definitions}
\rightarrow
\text{Assumptions}
\rightarrow
\text{Literature Boundary}
\rightarrow
\text{Model / Conjecture}
\rightarrow
\text{Derivation}
\rightarrow
\text{Implementation}
\rightarrow
\text{Verification}
\rightarrow
\text{Falsification / Validation}
\rightarrow
\text{Contribution}
}
```

Permitted research outputs include:

- theorem/proposition with proof;
- conjecture with evidence and counterexample search;
- new model with explicit assumptions;
- numerical method with verification study;
- rigorous reproduction;
- bounded transfer of existing mathematics into a new domain;
- negative result establishing where a transfer fails.

Negative results are scientifically valuable and must not be hidden by visual polish.

---

## Initial priority order

The practical initial order is:

```text
1  Linear algebra
2  Differential calculus
3  Integral calculus
4  Probability
5  Differential equations
6  Python scientific computing
7  Proof writing
8  Discrete mathematics
9  Multivariable calculus
10 Real analysis
11 Advanced linear algebra
12 Numerical analysis
13 Optimization
14 Graph theory
15 Dynamical systems
16 Mathematical statistics
17 Stochastic processes
18 Topology
19 Differential geometry
20 Riemannian geometry
21 PDEs
22 Control theory
23 Viability theory
24 Uncertainty quantification
25 Research synthesis
```

This is a dependency-aware default, not a claim that all learners or research questions must follow one immutable sequence.
