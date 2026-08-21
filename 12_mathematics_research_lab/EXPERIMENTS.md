# Research experiments

These are hypotheses/questions, not established results.

## EXP-001 — Curvature of a viability boundary

Question: can local curvature of an estimated viability boundary identify fragile state-space regions where small perturbations sharply reduce feasible recovery options?

Required before any claim:

1. define the state manifold and metric;
2. define the viability kernel independently of the visualization;
3. estimate boundary uncertainty;
4. test curvature sensitivity to sampling and model misspecification;
5. compare with simpler sensitivity metrics.

## EXP-002 — Interface uncertainty -> geometry uncertainty

If interface parameters are \(\theta\) with covariance \(\Sigma_\theta\), study

\[
\theta\mapsto \mathcal V(\theta)
\]

using set distances such as Hausdorff distance, while keeping parameter-identification error separate from viability-computation error.

## EXP-003 — Minimum-action recovery

Compare actual/control-optimal recovery trajectories against geodesics induced by candidate cost metrics. Reject the geometric interpretation if it does not add predictive or decision value.
