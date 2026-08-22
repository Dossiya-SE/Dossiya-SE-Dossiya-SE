"""Local-coordinate metric objects for symbolic differential geometry.

This module is intentionally local: a MetricChart represents one declared
coordinate chart together with a symmetric, non-degenerate metric matrix.
It does not claim to construct a global manifold or prove positive-definiteness
outside the caller's declared domain.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import sympy as sp


@dataclass(frozen=True)
class MetricChart:
    """A symbolic metric tensor in one coordinate chart."""

    coordinates: tuple[sp.Symbol, ...]
    metric: sp.ImmutableMatrix
    chart_name: str = "unnamed-chart"
    domain_note: str = "domain must be declared by caller"

    def __init__(
        self,
        coordinates: Iterable[sp.Symbol],
        metric: sp.MatrixBase | Iterable[Iterable[sp.Expr]],
        *,
        chart_name: str = "unnamed-chart",
        domain_note: str = "domain must be declared by caller",
    ) -> None:
        coords = tuple(coordinates)
        g = sp.ImmutableMatrix(metric)
        if not coords:
            raise ValueError("At least one coordinate is required.")
        if g.rows != g.cols or g.rows != len(coords):
            raise ValueError("Metric must be square with size equal to coordinate count.")
        if any(sp.simplify(g[i, j] - g[j, i]) != 0 for i in range(g.rows) for j in range(g.cols)):
            raise ValueError("Metric matrix must be symmetric.")
        det = sp.simplify(g.det())
        if det == 0:
            raise ValueError("Metric determinant is identically zero.")
        object.__setattr__(self, "coordinates", coords)
        object.__setattr__(self, "metric", g)
        object.__setattr__(self, "chart_name", chart_name)
        object.__setattr__(self, "domain_note", domain_note)

    @property
    def dimension(self) -> int:
        return len(self.coordinates)

    @property
    def determinant(self) -> sp.Expr:
        return sp.simplify(self.metric.det())

    @property
    def inverse_metric(self) -> sp.ImmutableMatrix:
        return sp.ImmutableMatrix(self.metric.inv().applyfunc(sp.simplify))
