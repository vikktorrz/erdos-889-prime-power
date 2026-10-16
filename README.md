
# Erdős Problem 889: A Prime-Power Investigation

Independent notes on a prime-power variant of Erdős
Problem 889, combining elementary number theory,
Diophantine reductions and exact computation.

**Author:** Victor Manuel Mesa Solano

**Status:** Ongoing independent research.
The original Erdős problem remains open.

## Overview

Erdős Problem 889 asks whether the maximum number
of new distinct prime factors appearing among
consecutive integers tends to infinity.

This repository investigates a related formulation
involving maximal prime-power components.

The main objectives are:

1. Establish precise arithmetic characterizations.
2. Derive necessary conditions and reductions.
3. Investigate the resulting Diophantine constraints.
4. Implement independently verifiable computations.
5. Identify what remains unresolved.

The project does not claim a solution to the
original Erdős problem.

## Mathematical scope

The original counting function is

$$
v(n,k)=
\#\{p\mid n+k:
p\nmid n+i\text{ for }0\le i<k\}.
$$

A maximal-prime-power version is

$$
V(n,k)=
\#\{p\mid n+k:
p^{v_p(n+k)}>k\}.
$$

The second identity describes the variant counting
new maximal prime-power components.

These two quantities are generally different.

## Verification

A small-input reference implementation is provided
under `verification/`.

Run:

```bash
python -m unittest discover -s verification -v
```

The reference tests compare direct definitions with
equivalent arithmetic characterizations.

Large-scale computations require separate validation
of the optimized implementation.

## Research transparency

See [Research Status](docs/RESEARCH_STATUS.md) for:

- Proved elementary statements
- Computational evidence
- Outstanding verification tasks
- Open questions and limitations

## References

- https://www.erdosproblems.com/889
- https://github.com/google-deepmind/formal-conjectures/issues/1006
