# Scientific governance

## Evidence classes

- **A — proved/derived:** complete derivation or formal proof is present.
- **B — verified:** independent symbolic or numerical checks pass.
- **C — reproduced:** an external published result is independently regenerated.
- **D — exploratory:** hypothesis, conjecture, prototype, or unvalidated numerical experiment.

Exploratory work must not be promoted to a stable module until verification criteria are satisfied.

## Numerical rigor

For every numerical claim record:

- algorithm and order of accuracy;
- tolerances;
- discretization or step size;
- convergence check;
- random seed if stochastic;
- floating-point precision;
- units;
- reference solution when available.

## Reproduction rigor

A reproduction must distinguish:

- source-stated values;
- inferred values;
- newly chosen values;
- unavailable values.

Never silently repair a source. Report deviations using an explicit error metric.

## Code rigor

- deterministic tests where possible;
- pure functions for core equations;
- no hidden global state in reference implementations;
- CI must run the minimal verification suite;
- generated figures must be reproducible from source code.

## Promotion gate

`research_lab -> verification -> stable module`

A result becomes `validated` only if its stated tests pass and its assumptions are documented.
