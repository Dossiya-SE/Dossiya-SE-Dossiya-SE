"""Publication-oriented torus curvature visualization."""

from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def render_torus(R=2.0, r=0.75, nu=240, nv=160, output="torus_curvature.png"):
    if not (R > r > 0):
        raise ValueError("Require R > r > 0.")
    u = np.linspace(0.0, 2.0*np.pi, nu)
    v = np.linspace(0.0, 2.0*np.pi, nv)
    U, V = np.meshgrid(u, v)
    A = R + r*np.cos(V)
    X = A*np.cos(U)
    Y = A*np.sin(U)
    Z = r*np.sin(V)
    K = np.cos(V) / (r*A)

    # Curvature controls appearance; the mapping is mathematical, not decorative.
    norm = (K - K.min()) / (K.max() - K.min())
    face = cm.viridis(norm)

    fig = plt.figure(figsize=(10, 8), constrained_layout=True)
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, facecolors=face, rstride=2, cstride=2,
                    linewidth=0.15, antialiased=True, shade=False)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.set_zlabel(r"$z$")
    ax.set_title(r"Torus: appearance mapped to Gaussian curvature $K$")
    ax.set_box_aspect((1, 1, 0.45))
    fig.savefig(output, dpi=300)
    plt.close(fig)
    return output


if __name__ == "__main__":
    render_torus()
