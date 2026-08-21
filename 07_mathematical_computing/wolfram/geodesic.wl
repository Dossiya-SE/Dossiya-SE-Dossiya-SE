(* Standard torus: symbolic metric, Christoffel symbols and geodesic equations. *)
ClearAll[u, v, R, r, s];
x = {(R + r Cos[v]) Cos[u], (R + r Cos[v]) Sin[u], r Sin[v]};
coords = {u, v};
g = Simplify@Table[D[x, coords[[i]]].D[x, coords[[j]]], {i, 2}, {j, 2}];
ginv = Simplify[Inverse[g]];

Gamma = Simplify@Table[
  1/2 Sum[
    ginv[[k, l]] (
      D[g[[j, l]], coords[[i]]] +
      D[g[[i, l]], coords[[j]]] -
      D[g[[i, j]], coords[[l]]]
    ), {l, 2}],
  {k, 2}, {i, 2}, {j, 2}
];

q = {u[s], v[s]};
geodesicEquations = Table[
  D[q[[k]], {s, 2}] +
    Sum[(Gamma[[k, i, j]] /. Thread[coords -> q]) D[q[[i]], s] D[q[[j]], s],
        {i, 2}, {j, 2}] == 0,
  {k, 2}
] // Simplify;
