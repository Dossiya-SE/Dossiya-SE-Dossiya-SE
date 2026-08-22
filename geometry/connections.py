"""Levi-Civita connection in local coordinates.

Convention: ``Gamma[k][i][j]`` represents Γ^k_{ij}.
"""
from __future__ import annotations

import sympy as sp

from .metrics import MetricChart


def _canonical(expr: sp.Expr) -> sp.Expr:
    """Conservative symbolic normalization for algebraic/trigonometric identities."""
    return sp.simplify(sp.expand_trig(expr))


def levi_civita_christoffel(chart: MetricChart) -> tuple:
    """Return Γ^k_{ij} from the metric using the Levi-Civita formula."""
    n = chart.dimension
    g = chart.metric
    g_inv = chart.inverse_metric
    q = chart.coordinates
    gamma = []
    for k in range(n):
        gamma_k = []
        for i in range(n):
            gamma_ki = []
            for j in range(n):
                value = sp.Rational(1, 2) * sum(
                    g_inv[k, ell]
                    * (
                        sp.diff(g[j, ell], q[i])
                        + sp.diff(g[i, ell], q[j])
                        - sp.diff(g[i, j], q[ell])
                    )
                    for ell in range(n)
                )
                gamma_ki.append(_canonical(value))
            gamma_k.append(tuple(gamma_ki))
        gamma.append(tuple(gamma_k))
    return tuple(gamma)


def torsion_residual(gamma: tuple) -> tuple:
    """Return T^k_{ij}=Γ^k_{ij}-Γ^k_{ji} in a coordinate frame."""
    n = len(gamma)
    return tuple(
        tuple(
            tuple(_canonical(gamma[k][i][j] - gamma[k][j][i]) for j in range(n))
            for i in range(n)
        )
        for k in range(n)
    )


def metric_compatibility_residual(chart: MetricChart, gamma: tuple) -> tuple:
    """Return (∇_k g)_{ij}; Levi-Civita output should simplify to zero."""
    n = chart.dimension
    g = chart.metric
    q = chart.coordinates
    return tuple(
        tuple(
            tuple(
                _canonical(
                    sp.diff(g[i, j], q[k])
                    - sum(g[ell, j] * gamma[ell][k][i] for ell in range(n))
                    - sum(g[i, ell] * gamma[ell][k][j] for ell in range(n))
                )
                for j in range(n)
            )
            for i in range(n)
        )
        for k in range(n)
    )


def all_zero(tensor: tuple) -> bool:
    """Recursively test whether every symbolic tensor entry normalizes to zero."""
    for item in tensor:
        if isinstance(item, tuple):
            if not all_zero(item):
                return False
        elif _canonical(item) != 0:
            return False
    return True


def transform_christoffel(
    old_gamma: tuple,
    old_coordinates: tuple[sp.Symbol, ...],
    old_coordinates_as_functions_of_new: tuple[sp.Expr, ...],
    new_coordinates: tuple[sp.Symbol, ...],
) -> tuple:
    """Transform connection coefficients under a coordinate change.

    If ``x=x(q)`` is the old-coordinate map expressed in new coordinates,
    the returned coefficients satisfy

    Γ'^k_ij = (∂q^k/∂x^a)[∂²x^a/(∂q^i∂q^j)
              + Γ^a_bc (∂x^b/∂q^i)(∂x^c/∂q^j)].

    This inhomogeneous law is why Christoffel symbols are not tensor
    components. The map must have an invertible Jacobian on the declared
    overlap domain.
    """
    old_coordinates = tuple(old_coordinates)
    old_map = tuple(old_coordinates_as_functions_of_new)
    new_coordinates = tuple(new_coordinates)
    n = len(old_coordinates)
    if not (len(old_map) == len(new_coordinates) == n == len(old_gamma)):
        raise ValueError("Coordinate and connection dimensions must agree.")
    jac = sp.ImmutableMatrix(old_map).jacobian(new_coordinates)
    if sp.simplify(jac.det()) == 0:
        raise ValueError("Coordinate-change Jacobian is identically singular.")
    inv_jac = jac.inv().applyfunc(_canonical)
    subs = dict(zip(old_coordinates, old_map))
    return tuple(
        tuple(
            tuple(
                _canonical(
                    sum(
                        inv_jac[k, a]
                        * (
                            sp.diff(old_map[a], new_coordinates[i], new_coordinates[j])
                            + sum(
                                sp.sympify(old_gamma[a][b][c]).subs(subs)
                                * jac[b, i]
                                * jac[c, j]
                                for b in range(n)
                                for c in range(n)
                            )
                        )
                        for a in range(n)
                    )
                )
                for j in range(n)
            )
            for i in range(n)
        )
        for k in range(n)
    )
