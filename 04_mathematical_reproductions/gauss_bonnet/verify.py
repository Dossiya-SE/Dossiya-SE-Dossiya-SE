"""Numerical Gauss--Bonnet benchmarks using midpoint quadrature."""

from __future__ import annotations
import math


def midpoint_integral_2d(f, a, b, c, d, n=800):
    du = (b - a) / n
    dv = (d - c) / n
    total = 0.0
    for i in range(n):
        u = a + (i + 0.5) * du
        for j in range(n):
            v = c + (j + 0.5) * dv
            total += f(u, v)
    return total * du * dv


def sphere_gauss_bonnet(n=500):
    # Unit sphere: K=1 and dA = sin(theta) dtheta dphi.
    val = midpoint_integral_2d(
        lambda phi, theta: math.sin(theta),
        0.0, 2.0 * math.pi, 0.0, math.pi, n=n
    )
    target = 4.0 * math.pi
    return val, abs(val - target)


def torus_gauss_bonnet(R=2.0, r=0.75, n=500):
    if not (R > r > 0):
        raise ValueError("Require R > r > 0.")
    def integrand(u, v):
        K = math.cos(v) / (r * (R + r * math.cos(v)))
        dA = r * (R + r * math.cos(v))
        return K * dA
    val = midpoint_integral_2d(
        integrand, 0.0, 2.0 * math.pi, 0.0, 2.0 * math.pi, n=n
    )
    return val, abs(val)


if __name__ == "__main__":
    print("sphere:", sphere_gauss_bonnet())
    print("torus :", torus_gauss_bonnet())
