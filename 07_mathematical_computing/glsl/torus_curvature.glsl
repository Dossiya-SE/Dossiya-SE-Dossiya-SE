// Gaussian curvature field for a standard torus.
// R > r > 0; v is the poloidal angle in radians.
float torusGaussianCurvature(float R, float r, float v) {
    return cos(v) / (r * (R + r * cos(v)));
}

// Signed scientific mapping helper: normalize against analytic extrema supplied
// by the host application rather than choosing arbitrary visual thresholds.
float normalizeCurvature(float K, float Kmin, float Kmax) {
    return clamp((K - Kmin) / (Kmax - Kmin), 0.0, 1.0);
}
