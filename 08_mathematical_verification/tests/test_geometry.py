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


torus_mod = load("03_mathematical_examples/differential_geometry/torus_geometry.py", "torus_geometry")
geo_mod = load("07_mathematical_computing/python/geodesic.py", "geodesic")
gb_mod = load("04_mathematical_reproductions/gauss_bonnet/verify.py", "gauss_bonnet")
eng_mod = load("10_mathematical_engineering_applications/infrastructure_viability/model.py", "infra_model")


def test_torus_metric_and_curvature_outer_equator():
    t = torus_mod.Torus(2.0, 0.75)
    g = t.metric(0.0)
    assert math.isclose(g[0][0], 2.75**2, rel_tol=1e-14)
    assert math.isclose(g[1][1], 0.75**2, rel_tol=1e-14)
    expected = 1.0 / (0.75 * 2.75)
    assert math.isclose(t.gaussian_curvature(0.0), expected, rel_tol=1e-14)


def test_torus_curvature_changes_sign():
    t = torus_mod.Torus(2.0, 0.75)
    assert t.gaussian_curvature(0.0) > 0
    assert t.gaussian_curvature(math.pi) < 0


def test_gauss_bonnet_benchmarks():
    sphere, sphere_error = gb_mod.sphere_gauss_bonnet(n=120)
    torus, torus_error = gb_mod.torus_gauss_bonnet(n=120)
    assert sphere_error < 2e-3
    assert torus_error < 1e-10


def test_geodesic_energy_conservation_short_run():
    path = geo_mod.integrate(h=2e-3, steps=1000)
    e0 = geo_mod.energy(path[0])
    e1 = geo_mod.energy(path[-1])
    assert abs(e1-e0)/abs(e0) < 1e-9


def test_engineering_state_stays_bounded_for_reference_case():
    ts, xs = eng_mod.simulate_reference(t_end=12.0, h=0.02)
    assert len(ts) == len(xs)
    assert all(0.0 <= xi <= 1.2 for x in xs for xi in x)
