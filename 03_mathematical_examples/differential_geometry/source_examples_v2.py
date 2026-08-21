"""Additional auditable geometry kernels from Sochi (2017), §1.4.1.

These functions implement source-grounded parameterizations while preserving the
parameter-domain restrictions stated in the book.  They deliberately contain no
plotting code so that numerical checks can be performed independently.

Source ID: SOCHI-DG-2017-UPLOADED
"""

from __future__ import annotations

import math
from collections.abc import Callable
from typing import Tuple

Point3 = Tuple[float, float, float]


def _nonzero(*values: float) -> None:
    if any(v == 0.0 for v in values):
        raise ValueError("Source scale parameters must be nonzero.")


def surface_of_revolution(z: float, phi: float, profile: Callable[[float], float]) -> Point3:
    """Sochi Eqs. (1)-(3): revolve x=f(z) around the z-axis."""
    rho = float(profile(z))
    return (rho * math.cos(phi), rho * math.sin(phi), z)


def hyperboloid_two_sheets(
    xi: float,
    theta: float,
    a: float,
    b: float,
    c: float,
) -> Point3:
    """Sochi Eqs. (16)-(18): one chart of a two-sheet hyperboloid.

    The source parameterization states xi >= 0.  With c>0 this chart covers the
    positive-z sheet; changing the sign of c covers the reflected sheet.
    """
    _nonzero(a, b, c)
    if xi < 0.0:
        raise ValueError("Require xi >= 0 for the source chart.")
    return (
        a * math.sinh(xi) * math.cos(theta),
        b * math.sinh(xi) * math.sin(theta),
        c * math.cosh(xi),
    )


def elliptic_paraboloid(
    xi: float,
    theta: float,
    a: float,
    b: float,
    c: float,
) -> Point3:
    """Sochi Eqs. (19)-(21): elliptic paraboloid with xi >= 0."""
    _nonzero(a, b, c)
    if xi < 0.0:
        raise ValueError("Require xi >= 0 because sqrt(xi) occurs in the source form.")
    root = math.sqrt(xi)
    return (a * root * math.cos(theta), b * root * math.sin(theta), c * xi)


def parabolic_cylinder(
    xi: float,
    omega: float,
    a: float = 1.0,
    b: float = 1.0,
) -> Point3:
    """Sochi Eqs. (25)-(27): parabolic cylinder."""
    _nonzero(a, b)
    return (xi, a * xi * xi, b * omega)


def catenary(xi: float, a: float = 1.0) -> Point3:
    """Sochi Eqs. (28)-(29), embedded in the xz-plane as y=0."""
    _nonzero(a)
    return (a * math.cosh(xi / a), 0.0, xi)


def enneper(xi: float, omega: float) -> Point3:
    """Sochi Eqs. (39)-(41): Enneper parameterization."""
    return (
        -(xi**3) / 3.0 + xi + xi * omega * omega,
        -(xi * xi) * omega - omega + (omega**3) / 3.0,
        xi * xi - omega * omega,
    )


def beltrami_pseudosphere(
    theta: float,
    phi: float,
    a: float = 1.0,
) -> Point3:
    """Sochi Eqs. (43)-(45): Beltrami pseudosphere parameterization.

    Domain follows the source: 0 < theta < pi and 0 <= phi < 2*pi.
    The function accepts equivalent periodic phi values numerically, but rejects
    theta at the singular endpoints where tan(theta/2) causes the source chart to
    degenerate.
    """
    _nonzero(a)
    if not (0.0 < theta < math.pi):
        raise ValueError("Require 0 < theta < pi for the source pseudosphere chart.")
    radial = a * math.sin(theta)
    z = a * (math.cos(theta) + math.log(math.tan(theta / 2.0)))
    return (radial * math.cos(phi), radial * math.sin(phi), z)


def torus_implicit_residual(
    point: Point3,
    R: float,
    r: float,
) -> float:
    """Independent implicit-relation residual for the standard ring torus."""
    if not (R > r > 0.0):
        raise ValueError("Require R > r > 0.")
    x, y, z = point
    return (math.hypot(x, y) - R) ** 2 + z * z - r * r


def ellipsoid_implicit_residual(point: Point3, a: float, b: float, c: float) -> float:
    """Independent implicit-relation residual for an ellipsoid."""
    _nonzero(a, b, c)
    x, y, z = point
    return (x / a) ** 2 + (y / b) ** 2 + (z / c) ** 2 - 1.0


def hyperboloid_two_sheets_residual(point: Point3, a: float, b: float, c: float) -> float:
    """Residual of -(x/a)^2-(y/b)^2+(z/c)^2=1."""
    _nonzero(a, b, c)
    x, y, z = point
    return -(x / a) ** 2 - (y / b) ** 2 + (z / c) ** 2 - 1.0


def elliptic_paraboloid_residual(point: Point3, a: float, b: float, c: float) -> float:
    """Residual of (x/a)^2+(y/b)^2=z/c."""
    _nonzero(a, b, c)
    x, y, z = point
    return (x / a) ** 2 + (y / b) ** 2 - z / c


def parabolic_cylinder_residual(point: Point3, a: float) -> float:
    """Residual of y=a*x^2."""
    _nonzero(a)
    x, y, _ = point
    return y - a * x * x


def catenary_residual(point: Point3, a: float) -> float:
    """Residual of x=a*cosh(z/a) in the source orientation."""
    _nonzero(a)
    x, y, z = point
    return math.hypot(x - a * math.cosh(z / a), y)
