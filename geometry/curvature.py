"""Intrinsic curvature tensors for a local metric chart.

Riemann sign/index convention
-----------------------------
``R[rho][sigma][mu][nu]`` represents

R^rho_{ sigma mu nu }
 = ∂_mu Γ^rho_{nu sigma} - ∂_nu Γ^rho_{mu sigma}
   + Γ^rho_{mu lambda} Γ^lambda_{nu sigma}
   - Γ^rho_{nu lambda} Γ^lambda_{mu sigma}.

Ricci is ``Ric[sigma][nu] = R^rho_{ sigma rho nu}`` and scalar curvature
is ``g^{sigma nu} Ric_{sigma nu}``. With this convention the unit 2-sphere
has scalar curvature +2.
"""
from __future__ import annotations

import sympy as sp

from .connections import levi_civita_christoffel
from .metrics import MetricChart

RIEMANN_CONVENTION = (
    "R^rho_{sigma mu nu} = d_mu Gamma^rho_{nu sigma} - d_nu Gamma^rho_{mu sigma} "
    "+ Gamma^rho_{mu lambda} Gamma^lambda_{nu sigma} "
    "- Gamma^rho_{nu lambda} Gamma^lambda_{mu sigma}"
)


def riemann_tensor(chart: MetricChart, gamma: tuple | None = None) -> tuple:
    gamma = levi_civita_christoffel(chart) if gamma is None else gamma
    n = chart.dimension
    q = chart.coordinates
    return tuple(
        tuple(
            tuple(
                tuple(
                    sp.simplify(
                        sp.diff(gamma[rho][nu][sigma], q[mu])
                        - sp.diff(gamma[rho][mu][sigma], q[nu])
                        + sum(
                            gamma[rho][mu][lam] * gamma[lam][nu][sigma]
                            - gamma[rho][nu][lam] * gamma[lam][mu][sigma]
                            for lam in range(n)
                        )
                    )
                    for nu in range(n)
                )
                for mu in range(n)
            )
            for sigma in range(n)
        )
        for rho in range(n)
    )


def ricci_tensor(chart: MetricChart, riemann: tuple | None = None) -> sp.ImmutableMatrix:
    R = riemann_tensor(chart) if riemann is None else riemann
    n = chart.dimension
    return sp.ImmutableMatrix(
        n,
        n,
        lambda sigma, nu: sp.simplify(sum(R[rho][sigma][rho][nu] for rho in range(n))),
    )


def scalar_curvature(chart: MetricChart, ricci: sp.MatrixBase | None = None) -> sp.Expr:
    Ric = ricci_tensor(chart) if ricci is None else ricci
    g_inv = chart.inverse_metric
    n = chart.dimension
    return sp.simplify(sum(g_inv[i, j] * Ric[i, j] for i in range(n) for j in range(n)))
