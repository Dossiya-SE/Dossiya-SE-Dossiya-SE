# Coupled infrastructure viability demonstrator

State:

\[
x(t)=[P,W,T,SW]^\top
\]

where each component is normalized service availability.

Reference dynamics:

\[
\dot x=A(t)x+b-u_{\mathrm{loss}}(t),
\]

with negative diagonal recovery/damping terms, positive cross-sector support terms, and hazard losses.

The example is deliberately small. Its purpose is to demonstrate:

- explicit state definition;
- dynamic coupling;
- climate/hazard forcing;
- numerical integration;
- viable-set evaluation;
- testing.

It is **not** a calibrated empirical model.

The reference viable set is

\[
\mathcal V=\{x:\min_i x_i\ge 0.35,\;\bar x\ge0.55\}.
\]

Both thresholds are demonstrator assumptions and must not be interpreted as evidence-based infrastructure standards.
