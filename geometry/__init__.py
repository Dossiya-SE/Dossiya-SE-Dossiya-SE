"""Verified local-coordinate differential-geometry primitives."""
from .metrics import MetricChart
from .connections import (
    all_zero,
    levi_civita_christoffel,
    metric_compatibility_residual,
    torsion_residual,
    transform_christoffel,
)
from .curvature import RIEMANN_CONVENTION, ricci_tensor, riemann_tensor, scalar_curvature
from .numerical import finite_difference_christoffel

__all__ = [
    "MetricChart",
    "levi_civita_christoffel",
    "torsion_residual",
    "metric_compatibility_residual",
    "all_zero",
    "transform_christoffel",
    "finite_difference_christoffel",
    "RIEMANN_CONVENTION",
    "riemann_tensor",
    "ricci_tensor",
    "scalar_curvature",
]
