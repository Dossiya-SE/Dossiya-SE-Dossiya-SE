"""Torus geodesic in local coordinates using fixed-step RK4.

For g = diag((R+r cos v)^2, r^2), the non-zero Christoffel symbols are
Gamma^u_uv = Gamma^u_vu = -r sin(v)/(R+r cos(v))
Gamma^v_uu = (R+r cos(v)) sin(v)/r
"""

from __future__ import annotations
import math


def rhs(state, R=2.0, r=0.75):
    u, v, du, dv = state
    a = R + r * math.cos(v)
    gamma_u_uv = -r * math.sin(v) / a
    gamma_v_uu = a * math.sin(v) / r
    ddu = -2.0 * gamma_u_uv * du * dv
    ddv = -gamma_v_uu * du * du
    return (du, dv, ddu, ddv)


def _add(y, k, scale):
    return tuple(yi + scale*ki for yi, ki in zip(y, k))


def rk4_step(y, h, R=2.0, r=0.75):
    k1 = rhs(y, R, r)
    k2 = rhs(_add(y, k1, h/2), R, r)
    k3 = rhs(_add(y, k2, h/2), R, r)
    k4 = rhs(_add(y, k3, h), R, r)
    return tuple(yi + h*(a + 2*b + 2*c + d)/6
                 for yi, a, b, c, d in zip(y, k1, k2, k3, k4))


def energy(state, R=2.0, r=0.75):
    _, v, du, dv = state
    return 0.5 * ((R+r*math.cos(v))**2 * du**2 + r**2 * dv**2)


def integrate(initial=(0.0, 0.6, 0.45, 0.9), h=1e-3, steps=10000):
    y = tuple(map(float, initial))
    out = [y]
    for _ in range(steps):
        y = rk4_step(y, h)
        out.append(y)
    return out


if __name__ == "__main__":
    path = integrate()
    e0 = energy(path[0])
    e1 = energy(path[-1])
    print("final_state =", path[-1])
    print("relative_energy_drift =", abs(e1-e0)/abs(e0))
