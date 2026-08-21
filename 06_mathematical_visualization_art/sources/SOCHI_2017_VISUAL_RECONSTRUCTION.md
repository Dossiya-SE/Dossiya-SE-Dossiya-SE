# Sochi 2017 — Mathematical Visualization Reconstruction Program

**Unique purpose:** regenerate the book's geometric ideas as higher-resolution mathematical art while keeping every visual encoding mathematically interpretable. Original source figures are reference targets only and are not copied into the repository.

**Primary source:** Sochi (2017). The book states in its preface that its graphic illustrations were prepared by the author and uses them extensively to support visualization of abstract concepts.

## Visual reconstruction principles

1. **Geometry first.** Every surface is generated from an explicit parameterization or implicit equation.
2. **Field-aware appearance.** Color or opacity should encode a declared quantity such as `K`, `H`, `|X_u×X_v|`, geodesic distance, or parameter value—not arbitrary decoration when the figure is presented as scientific.
3. **Coordinate truth.** Mesh lines represent actual coordinate curves unless explicitly labeled as rendering mesh.
4. **Domain visibility.** Singularities, excluded parameter values, chart boundaries, and self-intersections are identified.
5. **Vector semantics.** `T,N,B,n,E_1,E_2` arrows are normalized/scaled according to a documented convention.
6. **Reproducibility.** Figure metadata records code commit, parameters, camera, resolution, and mathematical field mapping.

## Source figure reconstruction matrix

| Source idea | Source anchor | Rebuild objective | Scientific enhancement |
|---|---|---|---|
| Möbius strip | Fig. 1, printed p. 15 | one-sided surface | show chart/orientation behavior and seam handling |
| helix | Fig. 2, p. 18 | curve + geometric parameters | overlay Frenet frame and `κ,τ` invariants |
| torus | Fig. 3, p. 19 | surface of revolution | map Gaussian curvature and show outer/inner sign change |
| ellipsoid | Fig. 4, p. 20 | regular quadratic surface | principal-curvature field |
| hyperboloids/paraboloids | Figs. 5–8, pp. 20–22 | positive/negative/saddle geometry | curvature-sign regions and tangent planes |
| catenoid | Fig. 10, p. 24 | minimal surface | verify and encode `H≈0`, show `K<0` away from limiting behavior |
| helicoid | Fig. 11, p. 24 | ruled/minimal surface | rulings + local isometry comparison with catenoid |
| monkey saddle | Fig. 12, p. 25 | higher-order saddle | critical-point/local-shape visualization |
| Enneper surface | Fig. 13, p. 26 | self-intersecting minimal surface | explicitly distinguish immersion from embedding |
| pseudosphere | Fig. 14, p. 27 | tractrix surface of revolution | constant-negative-curvature interpretation where appropriate |
| Frenet frame | Fig. 23, p. 61 | `T,N,B` and planes | animate moving frame along curve |
| Frenet planes | Fig. 24, p. 65 | osculating/rectifying/normal planes | dynamic local frame + equation labels |
| Gauss–Bonnet diagrams | Chapter 4 | local/global geometry-topology bridge | link curvature integral to Euler characteristic numerically |
| geodesic sphere examples | §5.7 | local geodesic vs global shortest path | compare multiple geodesic arcs with lengths |

## Output tiers

### Tier A — publication vector

Use LaTeX/TikZ/PGFPlots or Asymptote for diagrams dominated by exact annotation, frames, coordinate systems, and equations.

### Tier B — scientific 3-D

Use PyVista/VTK or Makie for surfaces, meshes, scalar fields, normals, streamlines, and interactive inspection.

### Tier C — symbolic-to-visual

Use SymPy or Wolfram Language to derive equations, then export numerically evaluated geometry to the rendering layer.

### Tier D — cinematic mathematical art

Use Blender/Python or GPU shaders only after the mathematical field has been defined and verified. Cinematic rendering is downstream of scientific truth, not a substitute for it.

### Tier E — animation

Use Manim or Makie animations for moving frames, geodesics, parallel transport, surface deformations, and theorem demonstrations.

## Figure provenance template

```yaml
figure_id: SOCHI_RECON_###
source: SOCHI-DG-2017-UPLOADED
source_anchor: "Fig. xx / Eq. yy / printed p. zz"
geometry_definition: "..."
encoded_fields:
  - quantity: Gaussian curvature
    symbol: K
    mapping: face scalar
parameters: {}
domain: {}
singularities_or_exclusions: []
software: []
verification_links: []
commit: "<git sha>"
```

## Example: torus curvature art

The source torus parameterization (Sochi, 2017, Eqs. 7–9) defines the geometry. A rigorous enhanced rendering computes `K(θ,φ)` and maps it to appearance. The outer region is positive and the inner region negative for the standard ring torus. The resulting image is simultaneously mathematical art and a curvature diagram.

## Copyright and scientific integrity

Do not trace or redistribute the source's original figures. Reconstruct the mathematical objects from their definitions. A reconstructed figure must cite the source mathematical anchor and separately cite the software used to produce the visualization.

## Citation

Sochi, T. (2017). *Introduction to Differential Geometry of Space Curves and Surfaces*. User-supplied PDF; internal preface date March 2017.
