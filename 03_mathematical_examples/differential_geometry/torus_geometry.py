"""Analytic geometry of a standard torus."""

from __future__ import annotations
import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Torus:
    major_radius: float
    minor_radius: float

    def __post_init__(self) -> None:
        if not (self.major_radius > self.minor_radius > 0.0):
            raise ValueError("Require major_radius > minor_radius > 0.")

    def point(self, u: float, v: float) -> tuple[float, float, float]:
        R, r = self.major_radius, self.minor_radius
        a = R + r * math.cos(v)
        return (a * math.cos(u), a * math.sin(u), r * math.sin(v))

    def metric(self, v: float) -> tuple[tuple[float, float], tuple[float, float]]:
        R, r = self.major_radius, self.minor_radius
        E = (R + r * math.cos(v)) ** 2
        G = r**2
        return ((E, 0.0), (0.0, G))

    def gaussian_curvature(self, v: float) -> float:
        R, r = self.major_radius, self.minor_radius
        return math.cos(v) / (r * (R + r * math.cos(v)))

    def area_density(self, v: float) -> float:
        R, r = self.major_radius, self.minor_radius
        return r * (R + r * math.cos(v))
