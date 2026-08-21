import graph3;
size(500);
currentprojection=perspective(4,3,2);

triple gamma(real t) { return (cos(t), sin(t), 0.18*t); }
triple tangent(real t) {
  triple d=(-sin(t),cos(t),0.18);
  return unit(d);
}
triple normal(real t) {
  triple dd=(-cos(t),-sin(t),0);
  triple T=tangent(t);
  return unit(dd-dot(dd,T)*T);
}
triple binormal(real t) { return unit(cross(tangent(t),normal(t))); }

path3 p=graph(gamma,0,4*pi,operator ..);
draw(p,linewidth(1.1));

real t0=2.2*pi;
triple P=gamma(t0);
draw(P--P+0.8*tangent(t0),Arrow3);
draw(P--P+0.8*normal(t0),Arrow3);
draw(P--P+0.8*binormal(t0),Arrow3);
label("$T$",P+0.85*tangent(t0));
label("$N$",P+0.85*normal(t0));
label("$B$",P+0.85*binormal(t0));
