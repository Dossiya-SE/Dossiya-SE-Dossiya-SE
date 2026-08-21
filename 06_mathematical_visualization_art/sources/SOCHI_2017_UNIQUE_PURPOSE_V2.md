# Sochi 2017 - Mathematical Visualization Grammar V2

**Unique purpose:** regenerate the book's geometric ideas as new, higher-quality scientific visualizations whose visual channels encode mathematical quantities. Original source figures are not copied.

## Source-design boundary

The source states that its illustrations, typesetting, cover, and overall design were made by the author, with LaTeX and LyX acknowledged. We therefore use the figures only to identify **mathematical concepts to reconstruct**, never as assets to reproduce pixel-for-pixel.

## Visual grammar

Every visual object must map to a defined mathematical quantity:

| Visual element | Mathematical meaning |
|---|---|
| surface mesh | parameter-coordinate curves `(u,v)` |
| tangent arrows | `E_1,E_2` or curve tangent `T` |
| normal arrow | unit surface normal `n` or principal normal `N` |
| binormal arrow | curve binormal `B` |
| local frame | Frenet/Darboux/surface basis |
| color field | explicitly named scalar such as `K`, `H`, `kappa_g`, residual, uncertainty |
| line thickness | optional magnitude encoding with legend |
| transparency | optional confidence/layer distinction, never hidden data |
| contour lines | level sets of a named scalar |
| highlighted path | geodesic, principal line, asymptotic line, or other identified curve |

No rainbow palette is used merely for decoration in publication figures; a color map must have a mathematical legend and appropriate normalization.

## V1 figure families to regenerate

1. **Parametric-surface atlas**: torus, ellipsoid, hyperboloids, paraboloids, catenoid, helicoid, Enneper, monkey saddle, pseudosphere.
2. **Frenet frame**: curve plus `T,N,B`, osculating/normal/rectifying planes.
3. **Surface frame**: `E_1,E_2,n`, tangent plane and coordinate grid.
4. **Intrinsic versus extrinsic**: plane-to-cylinder isometry with identical metric and different second fundamental form.
5. **Curvature maps**: `K` and `H` on sphere, torus, saddle, catenoid.
6. **Principal curvature**: principal directions and Dupin-style local geometry.
7. **Gauss-Weingarten**: basis-vector derivatives decomposed into tangent and normal parts.
8. **Gauss-Bonnet**: local curvature field + global topology summary for sphere/torus/genus surfaces.
9. **Geodesics**: chart-space trajectory mapped to the embedded surface.
10. **Laplace-Beltrami**: scalar field on a curved surface with gradient/flux overlays.

## Rendering pipeline

```text
source equation/page
      -> symbolic expression
      -> numerical sampling
      -> geometric mesh/curve
      -> mathematical field computation
      -> invariant verification
      -> scientific rendering
      -> LaTeX/vector labels
      -> SVG/PDF + high-resolution raster export
```

Recommended role separation:

- **SymPy / Wolfram Language**: symbolic geometry and exact labels;
- **NumPy / Julia**: numerical sampling;
- **PyVista/VTK or Makie**: scientific 3D geometry;
- **Blender Python**: cinematic/high-resolution rendering after numerical truth is frozen;
- **Asymptote / TikZ/PGFPlots**: publication vector graphics;
- **Manim**: mathematical animation;
- **GLSL/WebGL**: interactive/high-density field rendering.

## Geometric QA

A rendered surface must pass the same checks as its computational object before export. Examples:

- torus implicit residual;
- mesh regularity (`EG-F^2>0`) away from chart singularities;
- normal orthogonality to tangent basis;
- curvature field cross-check by independent formulas;
- geodesic residual for highlighted geodesic lines;
- Gauss-Bonnet total-curvature residual where applicable.

## Publication QA

Every final figure must have:

- equation/source anchor in metadata;
- declared coordinate system;
- mathematical legend;
- units if quantities have units;
- accessible axis/label typography;
- vector output when practical;
- reproducible script and parameter file;
- no copied source image.

A visually attractive output that fails its geometric invariant tests is rejected.
