
# Research Status

## Scope

This repository investigates a prime-power variant of
Erdős Problem 889.

The original problem concerns distinct prime divisors.
The proposed variant concerns maximal prime-power
components. These definitions must be distinguished.

## Definitions

Let n >= 1 and k >= 0.

The original counting function v(n,k) counts distinct
primes dividing n+k which divide none of the integers
n, ..., n+k-1.

In the maximal-prime-power variant, V(n,k) counts
components p^a || n+k which divide none of these
preceding integers.

## Established elementary identities

For the original problem:

    v(n,k) = #{p | n+k : p > k}.

For the maximal-prime-power variant:

    V(n,k) = #{p | n+k : p^v_p(n+k) > k}.

Both follow from divisibility of the differences
(n+k)-(n+i).

## A necessary size bound

If V(n,k) >= r, with r distinct maximal prime-power
components, then

    n+k >= (k+1)(k+2)...(k+r).

The same necessary bound holds for v(n,k) >= r.

These are elementary observations, not claims of
original mathematical novelty.

## Computational verification

The reference implementation compares the direct
definitions with their arithmetic characterizations
for small inputs.

Any large-scale search claim must specify:

- Exact parameter ranges and boundary conventions
- Source code version / commit
- Compiler, flags and platform
- Independent verification procedure
- Data or reproducible output
- What the computation does and does not establish

## Open questions

The original Erdős Problem 889 remains open.

Computational verification over a finite domain does
not establish the conjecture for all sufficiently
large integers.

Further claims and proposed reductions must be
checked individually before being classified as
proved results.

## References

- Erdős Problems, Problem 889:
  https://www.erdosproblems.com/889
- Google DeepMind Formal Conjectures, issue 1006:
  https://github.com/google-deepmind/formal-conjectures/issues/1006
