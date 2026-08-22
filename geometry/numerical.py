"""Independent numerical checks for local-coordinate geometry."""
from __future__ import annotations

from collections.abc import Callable, Sequence

import numpy as np


def finite_difference_christoffel(
    metric_function: Callable[[np.ndarray], np.ndarray],
    point: Sequence[float],
    *,
    step: float = 1e-6,
) -> np.ndarray:
    """Approximate Levi-Civita coefficients by central metric differences.

    This function intentionally does not call the symbolic implementation.
    It provides a numerically independent derivative path for benchmark
    comparisons. ``metric_function(point)`` must return a symmetric ``n x n``
    positive-definite matrix in the neighborhood sampled by the stencil.
    """
    x = np.asarray(point, dtype=float)
    n = x.size
    if step <= 0:
        raise ValueError("step must be positive")
    g0 = np.asarray(metric_function(x), dtype=float)
    if g0.shape != (n, n):
        raise ValueError("metric_function returned wrong shape")
    g_inv = np.linalg.inv(g0)
    dg = np.empty((n, n, n), dtype=float)
    for d in range(n):
        shift = np.zeros(n)
        shift[d] = step
        gp = np.asarray(metric_function(x + shift), dtype=float)
        gm = np.asarray(metric_function(x - shift), dtype=float)
        dg[d] = (gp - gm) / (2.0 * step)
    gamma = np.zeros((n, n, n), dtype=float)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                gamma[k, i, j] = 0.5 * sum(
                    g_inv[k, ell] * (dg[i, j, ell] + dg[j, i, ell] - dg[ell, i, j])
                    for ell in range(n)
                )
    return gamma
