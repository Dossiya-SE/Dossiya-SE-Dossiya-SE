"""Auditable parameterizations from Sochi (2017), §1.4.1.

The functions implement selected source equations without importing plotting or
symbolic libraries. They are intended as geometry kernels for independent tests.
"""

from __future__ import annotations

import math
from typing import Tuple

Point3 = Tuple[float, float, float]


def helix(theta: float, a: float = 2.0, b: float = 0.5) -> Point3:
    """Sochi Eqs. (4)–(6): circular helix."""
    if a == 0.0 or b == 0.0:
        raise ValueError("Source prototype assumes nonzero a and b.")
    return (a * math.cos(theta), a * math.sin(theta), b * theta)


def torus(theta: float, phi: float, R: float = 2.0, r: float = 0.75) -> Point3:
    """Sochi Eqs. (7)–(9): torus with 0 < r < R."""
    if not (R > r > 0.0):
        raise ValueError("Require R > r > 0 for the source torus parameterization.")
    rho = R + r * math.cos(phi)
    return (rho * math.cos(theta), rho * math.sin(theta), r * math.sin(phi))


def ellipsoid(theta: float, phi: float, a: float, b: float, c: float) -> Point3:
    """Sochi Eqs. (10)–(12): ellipsoid."""
    if a == 0.0 or b == 0.0 or c == 0.0:
        raise ValueError("Ellipsoid semiaxis parameters must be nonzero.")
    return (
        a * math.sin(theta) * math.cos(phi),
        b * math.sin(theta) * math.sin(phi),
        c * math.cos(theta),
    )


def hyperboloid_one_sheet(xi: float, theta: float, a: float, b: float, c: float) -> Point3:
    """Sochi Eqs. (13)–(15): hyperboloid of one sheet."""
    if a == 0.0 or b == 0.0 or c == 0.0:
        raise ValueError("Scale parameters must be nonzero.")
    return (
        a * math.cosh(xi) * math.cos(theta),
        b * math.cosh(xi) * math.sin(theta),
        c * math.sinh(xi),
    )


def hyperbolic_paraboloid(xi: float, omega: float, a: float = 1.0, b: float = 1.0, c: float = 1.0) -> Point3:
    """Sochi Eqs. (22)–(24): hyperbolic paraboloid."""
    if a == 0.0 or b == 0.0 or c == 0.0:
        raise ValueError("Scale parameters must be nonzero.")
    return (a * xi, b * omega, c * xi * omega)


def catenoid(xi: float, theta: float, a: float = 1.0) -> Point3:
    """Sochi Eqs. (30)–(32): catenoid."""
    if a == 0.0:
        raise ValueError("Require a != 0.")
    rho = a * math.cosh(xi / a)
    return (rho * math.cos(theta), rho * math.sin(theta), xi)


def helicoid(xi: float, theta: float, a: float = 1.0, b: float = 1.0) -> Point3:
    """Sochi Eqs. (33)–(35): helicoid."""
    if a == 0.0 or b == 0.0:
        raise ValueError("Source prototype assumes nonzero a and b.")
    return (a * xi * math.cos(theta), a * xi * math.sin(theta), b * theta)


def monkey_saddle(xi: float, omega: float) -> Point3:
    """Sochi Eqs. (36)–(38): monkey saddle."""
    return (xi, omega, xi**3 - 3.0 * xi * omega**2)


def helix_curvature_torsion(a: float, b: float) -> tuple[float, float]:
    """Closed-form benchmark reported in Sochi §2.3 for r=(a cos t,a sin t,bt)."""
    if a == 0.0 and b == 0.0:
        raise ValueError("Degenerate constant curve is excluded.")
    denom = a * a + b * b
    return (abs(a) / denom, b / denom)
