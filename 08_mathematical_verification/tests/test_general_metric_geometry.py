import sympy as sp

from geometry import (
    MetricChart,
    all_zero,
    levi_civita_christoffel,
    metric_compatibility_residual,
    scalar_curvature,
    torsion_residual,
)


def test_cartesian_plane_connection_and_curvature_are_zero():
    x, y = sp.symbols("x y", real=True)
    chart = MetricChart((x, y), sp.eye(2), chart_name="R2-cartesian")
    gamma = levi_civita_christoffel(chart)
    assert all_zero(gamma)
    assert all_zero(torsion_residual(gamma))
    assert all_zero(metric_compatibility_residual(chart, gamma))
    assert sp.simplify(scalar_curvature(chart)) == 0


def test_polar_plane_nonzero_connection_but_flat_scalar_curvature():
    r, theta = sp.symbols("r theta", positive=True, real=True)
    chart = MetricChart((r, theta), sp.diag(1, r**2), chart_name="R2-polar", domain_note="r>0")
    gamma = levi_civita_christoffel(chart)
    assert sp.simplify(gamma[0][1][1] + r) == 0
    assert sp.simplify(gamma[1][0][1] - 1/r) == 0
    assert sp.simplify(gamma[1][1][0] - 1/r) == 0
    assert all_zero(torsion_residual(gamma))
    assert all_zero(metric_compatibility_residual(chart, gamma))
    assert sp.simplify(scalar_curvature(chart)) == 0


def test_unit_sphere_scalar_curvature_is_two_on_regular_chart():
    theta, phi = sp.symbols("theta phi", positive=True, real=True)
    chart = MetricChart(
        (theta, phi), sp.diag(1, sp.sin(theta) ** 2), chart_name="S2-spherical",
        domain_note="0<theta<pi; phi local modulo 2pi",
    )
    gamma = levi_civita_christoffel(chart)
    assert all_zero(torsion_residual(gamma))
    assert all_zero(metric_compatibility_residual(chart, gamma))
    assert sp.trigsimp(scalar_curvature(chart) - 2) == 0


def test_torus_intrinsic_scalar_curvature_matches_two_times_gaussian_curvature():
    u, v = sp.symbols("u v", real=True)
    R, a = sp.symbols("R a", positive=True, real=True)
    chart = MetricChart(
        (u, v), sp.diag((R + a * sp.cos(v)) ** 2, a**2), chart_name="standard-torus",
        domain_note="R>a>0; u,v local modulo 2pi",
    )
    scalar = sp.trigsimp(scalar_curvature(chart))
    expected = 2 * sp.cos(v) / (a * (R + a * sp.cos(v)))
    assert sp.trigsimp(scalar - expected) == 0


def test_rejects_nonsymmetric_and_identically_degenerate_metrics():
    x, y = sp.symbols("x y")
    try:
        MetricChart((x, y), [[1, x], [0, 1]])
    except ValueError as exc:
        assert "symmetric" in str(exc)
    else:
        raise AssertionError("nonsymmetric metric must be rejected")
    try:
        MetricChart((x, y), [[1, 0], [0, 0]])
    except ValueError as exc:
        assert "determinant" in str(exc)
    else:
        raise AssertionError("degenerate metric must be rejected")


def test_connection_transformation_cartesian_to_polar_includes_inhomogeneous_term():
    from geometry import transform_christoffel

    x, y = sp.symbols("x y", real=True)
    r, theta = sp.symbols("r theta", positive=True, real=True)
    cart = MetricChart((x, y), sp.eye(2), chart_name="R2-cartesian")
    polar = MetricChart((r, theta), sp.diag(1, r**2), chart_name="R2-polar", domain_note="r>0")
    gamma_from_transform = transform_christoffel(
        levi_civita_christoffel(cart), (x, y),
        (r * sp.cos(theta), r * sp.sin(theta)), (r, theta),
    )
    gamma_polar = levi_civita_christoffel(polar)
    for k in range(2):
        for i in range(2):
            for j in range(2):
                residual = gamma_from_transform[k][i][j] - gamma_polar[k][i][j]
                assert sp.simplify(sp.expand_trig(residual)) == 0


def test_symbolic_and_finite_difference_christoffel_agree_on_sphere_point():
    import numpy as np
    from geometry import finite_difference_christoffel

    theta, phi = sp.symbols("theta phi", real=True)
    chart = MetricChart((theta, phi), sp.diag(1, sp.sin(theta)**2), chart_name="S2-spherical")
    gamma_symbolic = levi_civita_christoffel(chart)
    point = np.array([1.1, 0.7])
    gamma_eval = np.empty((2, 2, 2), dtype=float)
    for k in range(2):
        for i in range(2):
            for j in range(2):
                gamma_eval[k, i, j] = float(gamma_symbolic[k][i][j].subs({theta: point[0], phi: point[1]}))

    def metric_fn(q):
        th = q[0]
        return np.array([[1.0, 0.0], [0.0, np.sin(th)**2]], dtype=float)

    gamma_fd = finite_difference_christoffel(metric_fn, point, step=2e-6)
    assert np.max(np.abs(gamma_eval - gamma_fd)) < 2e-7
