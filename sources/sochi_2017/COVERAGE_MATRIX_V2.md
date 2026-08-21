# Sochi 2017 Chapter-to-Module Coverage Matrix V2

This matrix prevents semantic duplication. A chapter can feed several modules, but each module consumes it for a different artifact class.

| Source block | Foundations | Models | Examples | Reproductions | Skills | Visualization | Computing | Verification | Math Physics | Engineering | Literature Atlas | Research Lab |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nomenclature | canonical symbols | variable dictionaries | labels | notation parity | fluency | label grammar | API names | convention checks | notation transfer | units/naming discipline | synonym index | extension notation |
| Ch.1 Preliminaries | definitions, topology, coordinate maps, Christoffel/Riemann/Ricci | regularity and metric primitives | prototype surfaces | Jacobian/topology benchmarks | prerequisites | parameter-domain diagrams | symbolic kernels | rank/invariance tests | variational and curvature preliminaries | transfer constraints | chapter map | gap statements |
| Ch.2 Curves | Frenet frame, curvature, torsion | curve-state model | helix/curve examples | kappa/tau/Frenet reproduction | derivations/exercises | T-N-B animations | differential kernels | orthonormality/invariance | moving frames | path geometry | named concepts | trajectory hypotheses |
| Ch.3 Surfaces | metric, curvature tensor, fundamental forms, Gauss-Weingarten, Codazzi | surface state and compatibility model | parametric surfaces | metric/shape/Gauss-Codazzi reproduction | tensor skill track | tangent plane/normal/curvature figures | metric/connection algorithms | positive-definiteness and compatibility | constrained motion geometry | shell/manifold transfer | theorem graph | geometry-of-state-space hypotheses |
| Ch.4 Curvature | principal/K/H, Egregium, Gauss-Bonnet | curvature-state descriptors | Monge patch, torus, sphere | K/H/topology benchmarks | proof/exercise track | curvature maps | curvature algorithms | intrinsic/extrinsic invariant checks | curvature effects | structural/path mapping only with external evidence | theorem provenance | curvature-risk hypotheses |
| Ch.5 Special Curves | special-curve definitions | constrained curve classes | geodesics/lines of curvature/asymptotic lines | geodesic benchmarks | advanced curve skills | special-curve atlas | ODE solvers | residual tests | least-action bridge | path planning transfer | named-result map | control/geodesic comparisons |
| Ch.6 Special Surfaces | ruled/developable/isometric/minimal definitions | constrained surface classes | catenoid/helicoid/etc. | H=0/isometry/developability tests | surface classification | surface gallery | mesh/symbolic pipeline | curvature/isometry tests | minimal-surface bridge | design analogy only unless externally validated | source index | morphology hypotheses |
| Ch.7 Tensor differentiation | covariant/absolute derivatives, divergence, Laplacian | field-on-manifold model | tensor-field examples | operator reproduction | tensor calculus mastery | vector/tensor field visuals | operator implementations | metric-compatibility/operator tests | diffusion/transport bridge | PDE-on-surface transfer with external evidence | notation/equation index | manifold-PDE experiments |

## Acceptance rule

An item may appear in more than one module only if its **function changes**. For example, Eq. (356) may be:

- a canonical identity in Foundations;
- an observable definition in Models;
- a target value in Reproductions;
- an oracle in Verification;
- a color field in Visualization.

The text surrounding those appearances must not be copied mechanically between modules.
