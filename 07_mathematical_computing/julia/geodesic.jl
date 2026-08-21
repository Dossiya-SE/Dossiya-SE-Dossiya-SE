# Torus geodesic equations in local coordinates.

function torus_geodesic!(du, y, p, t)
    R, r = p
    u, v, u̇, v̇ = y
    a = R + r*cos(v)
    Γu_uv = -r*sin(v)/a
    Γv_uu = a*sin(v)/r
    du[1] = u̇
    du[2] = v̇
    du[3] = -2Γu_uv*u̇*v̇
    du[4] = -Γv_uu*u̇^2
end

# Intended use with DifferentialEquations.jl:
# prob = ODEProblem(torus_geodesic!, [0.0,0.6,0.45,0.9], (0.0,10.0), (2.0,0.75))
# sol = solve(prob, Vern9(), abstol=1e-12, reltol=1e-12)
