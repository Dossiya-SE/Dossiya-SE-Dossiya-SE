import importlib.util
import math
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]


def load(path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    import sys

    sys.modules[name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


v2 = load(
    "03_mathematical_examples/differential_geometry/source_examples_v2.py",
    "sochi_source_examples_v2",
)


def test_surface_of_revolution_radial_identity():
    p = v2.surface_of_revolution(1.25, 0.73, lambda z: 2.0 + z * z)
    expected_radius = 2.0 + 1.25**2
    assert math.isclose(math.hypot(p[0], p[1]), expected_radius, rel_tol=1e-14)
    assert p[2] == 1.25


def test_two_sheet_hyperboloid_implicit_equation():
    p = v2.hyperboloid_two_sheets(0.83, 1.17, 2.0, 1.5, 3.0)
    residual = v2.hyperboloid_two_sheets_residual(p, 2.0, 1.5, 3.0)
    assert abs(residual) < 1e-13


def test_elliptic_paraboloid_implicit_equation():
    p = v2.elliptic_paraboloid(2.7, 0.41, 2.0, 3.0, 1.25)
    residual = v2.elliptic_paraboloid_residual(p, 2.0, 3.0, 1.25)
    assert abs(residual) < 1e-13


def test_parabolic_cylinder_implicit_equation():
    p = v2.parabolic_cylinder(-1.7, 2.3, a=0.8, b=4.0)
    assert abs(v2.parabolic_cylinder_residual(p, 0.8)) < 1e-14


def test_catenary_relation_and_plane_embedding():
    p = v2.catenary(1.4, a=2.2)
    assert abs(v2.catenary_residual(p, 2.2)) < 1e-14
    assert p[1] == 0.0


def test_enneper_parameter_symmetry_at_origin():
    assert v2.enneper(0.0, 0.0) == (0.0, 0.0, 0.0)
    p = v2.enneper(0.4, -0.6)
    # z is an independently inspectable algebraic invariant of the source map.
    assert math.isclose(p[2], 0.4**2 - (-0.6) ** 2, abs_tol=1e-15)


def test_pseudosphere_radial_identity():
    theta, phi, a = 1.1, 0.7, 2.3
    p = v2.beltrami_pseudosphere(theta, phi, a)
    assert math.isclose(math.hypot(p[0], p[1]), abs(a * math.sin(theta)), rel_tol=1e-14)


def test_source_domain_guards():
    with pytest.raises(ValueError):
        v2.hyperboloid_two_sheets(-0.1, 0.0, 1.0, 1.0, 1.0)
    with pytest.raises(ValueError):
        v2.elliptic_paraboloid(-0.1, 0.0, 1.0, 1.0, 1.0)
    with pytest.raises(ValueError):
        v2.beltrami_pseudosphere(0.0, 0.0, 1.0)
    with pytest.raises(ValueError):
        v2.beltrami_pseudosphere(math.pi, 0.0, 1.0)
