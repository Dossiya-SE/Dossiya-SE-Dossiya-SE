"""Four-sector normalized-service demonstrator.

This is a pedagogical/reference implementation, not a calibrated empirical model.
"""

from __future__ import annotations
import math


def hazard(t: float) -> float:
    # Smooth flood-like pulse, dimensionless demonstrator forcing.
    return 0.45 * math.exp(-0.5 * ((t - 5.0) / 1.1) ** 2)


def rhs(t: float, x: tuple[float, float, float, float]):
    P, W, T, SW = x
    h = hazard(t)

    # Cross-sector terms illustrate dynamic interfaces.
    dP = 0.18*(1-P) + 0.03*(T-P) - 0.16*h*P
    dW = 0.14*(1-W) + 0.07*(P-W) - 0.22*h*W - 0.05*(1-SW)
    dT = 0.10*(1-T) + 0.03*(P-T) - 0.20*h*T - 0.06*(1-SW)
    dSW = 0.12*(1-SW) + 0.05*(T-SW) - 0.24*h*SW
    return (dP, dW, dT, dSW)


def _add(x, k, scale):
    return tuple(xi + scale*ki for xi, ki in zip(x, k))


def rk4_step(t, x, h):
    k1 = rhs(t, x)
    k2 = rhs(t+h/2, _add(x, k1, h/2))
    k3 = rhs(t+h/2, _add(x, k2, h/2))
    k4 = rhs(t+h, _add(x, k3, h))
    return tuple(xi + h*(a+2*b+2*c+d)/6 for xi,a,b,c,d in zip(x,k1,k2,k3,k4))


def is_viable(x, component_floor=0.35, mean_floor=0.55):
    return min(x) >= component_floor and sum(x)/len(x) >= mean_floor


def simulate_reference(t_end=12.0, h=0.01):
    if h <= 0 or t_end <= 0:
        raise ValueError("Require positive h and t_end.")
    t = 0.0
    x = (0.92, 0.88, 0.82, 0.80)
    ts, xs = [t], [x]
    n = round(t_end / h)
    for _ in range(n):
        x = rk4_step(t, x, h)
        t += h
        ts.append(t)
        xs.append(x)
    return ts, xs


if __name__ == "__main__":
    ts, xs = simulate_reference()
    viable_fraction = sum(map(is_viable, xs)) / len(xs)
    print("minimum components =", tuple(min(x[i] for x in xs) for i in range(4)))
    print("viable_fraction =", viable_fraction)
