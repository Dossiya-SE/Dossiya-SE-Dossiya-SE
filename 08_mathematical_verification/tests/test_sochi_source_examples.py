import importlib.util
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    import sys
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


src = load(
    "03_mathematical_examples/differential_geometry/source_examples.py",
    "sochi_source_examples",
)


def test_torus_parameterization_respects_implicit_ring_relation():
    R, r = 2.0, 0.75
    theta, phi = 0.7, 1.2
    x, y, z = src.torus(theta, phi, R=R, r=r)
    rho = math.sqrt(x * x + y * y)
    residual = (rho - R) ** 2 + z * z - r * r
    assert abs(residual) < 1e-13


def test_torus_domain_guard():
    import pytest
    with pytest.raises(ValueError):
        src.torus(0.0, 0.0, R=1.0, r=1.0)


def test_ellipsoid_parameterization_satisfies_quadric():
    a, b, c = 3.0, 2.0, 1.5
    x, y, z = src.ellipsoid(1.1, 0.4, a, b, c)
    residual = x * x / (a * a) + y * y / (b * b) + z * z / (c * c) - 1.0
    assert abs(residual) < 1e-13


def test_hyperboloid_one_sheet_satisfies_quadric():
    a, b, c = 2.0, 1.5, 0.8
    x, y, z = src.hyperboloid_one_sheet(0.9, 1.3, a, b, c)
    residual = x * x / (a * a) + y * y / (b * b) - z * z / (c * c) - 1.0
    assert abs(residual) < 1e-12


def test_hyperbolic_paraboloid_parameterization_relation():
    a, b, c = 2.0, 3.0, 4.0
    x, y, z = src.hyperbolic_paraboloid(0.6, -1.2, a, b, c)
    expected = c * (x / a) * (y / b)
    assert math.isclose(z, expected, rel_tol=1e-14, abs_tol=1e-14)


def test_catenoid_has_expected_radius():
    xi, theta, a = 0.8, 1.1, 1.3
    x, y, z = src.catenoid(xi, theta, a)
    assert math.isclose(z, xi, rel_tol=0.0, abs_tol=1e-15)
    assert math.isclose(
        math.sqrt(x * x + y * y),
        a * math.cosh(xi / a),
        rel_tol=1e-14,
    )


def test_helicoid_height_tracks_theta():
    xi, theta, a, b = -0.7, 2.3, 1.2, 0.4
    x, y, z = src.helicoid(xi, theta, a, b)
    assert math.isclose(z, b * theta, rel_tol=1e-14)
    assert math.isclose(math.sqrt(x * x + y * y), abs(a * xi), rel_tol=1e-14)


def test_helix_closed_form_curvature_and_torsion():
    kappa, tau = src.helix_curvature_torsion(a=3.0, b=4.0)
    assert math.isclose(kappa, 3.0 / 25.0, rel_tol=1e-14)
    assert math.isclose(tau, 4.0 / 25.0, rel_tol=1e-14)
