# Erdős–Selfridge Problem #889 — Prime-Power Variant

Independent research project in number theory studying the prime-power variant of the Erdős–Selfridge Problem #889.

The project combines **Diophantine analysis**, structural reductions, and **exact computation** to investigate the exceptional integers in the prime-power variant.

> **Status:** The problem remains open.
> This repository does **not** claim a complete solution.

## Problem

For an integer \(m \ge 2\), write

$$
m=\prod_{p\mid m}p^{\nu_p(m)}
$$

and consider its full prime-power components

$$
p^{\nu_p(m)}.
$$

For \(n,k\ge1\), define

$$
V(n,k)
=
\#\left\{
p:\;p^{\nu_p(n+k)}>k
\right\},
$$

and

$$
V_1(n)=\max_{k\ge1}V(n,k).
$$

The Erdős–Selfridge prime-power variant asks whether

$$
\{n\ge1:V_1(n)=1\}
$$

is finite.

The known values are

$$
1,2,3,4,6,7,8,12,15,16,24,30,48,80.
$$

The question remains open.

## Main Mathematical Ideas

### Interval formulation

Let \(Q_2(m)\) denote the second-largest prime-power component of \(m\).

Then

$$
V(n,k)\ge2
\iff
Q_2(n+k)>k,
$$

which gives the interval condition

$$
n+k-Q_2(n+k)+1\le n\le n+k-1.
$$

Equivalently, every integer \(m\) contributes the interval

$$
m-Q_2(m)+1\le n\le m-1.
$$

Thus the problem can be interpreted as a covering problem for these intervals.

### A universal bound

If \(V(n,k)\ge2\), then two distinct prime-power components \(A,B>k\) divide \(n+k\). Since they are coprime,

$$
AB\mid n+k
$$

and therefore

$$
n>k^2-k.
$$

This gives a finite bound on the values of \(k\) that must be checked for any finite computational range.

### Divisor decomposition

Under the assumption \(V_1(n)=1\), the non-dominant prime-power components of \(n+k\) divide

$$
\operatorname{lcm}(1,\ldots,k).
$$

This yields the decomposition

$$
n+k=d_kq_k,
\qquad
d_k\mid\operatorname{lcm}(1,\ldots,k),
$$

together with the compatibility condition

$$
\gcd(d_i,d_j)\mid |i-j|.
$$

This converts the original problem into a collection of constrained Diophantine branches.

## Partial Results

The project currently contains proofs and reductions for several branches.

In particular:

* The branch \(d_2=1\) is completely resolved, producing only

  $$
  1,2,3,6,7,15,30.
  $$

* The \(d_2=2,\ d_3=1\) branch is substantially reduced. In particular, certain exponent configurations collapse to the known exception \(n=24\), while the remaining cases reduce to explicit simultaneous-primality conditions.

* Further branches such as \(d_2=2,\ d_3=3\) are reduced to increasingly restrictive Diophantine systems.

The manuscript deliberately keeps unresolved branches explicit rather than treating computational evidence as proof.

## Exact Computational Verification

An exact sieve computes the second-largest prime-power component \(Q_2(m)\) using **smallest-prime-factor preprocessing**.

The resulting intervals are accumulated using a difference-array technique.

For

$$
N=50\,000\,000,
$$

the computation verifies exactly the set

$$
\boxed{
\{1,2,3,4,6,7,8,12,15,16,24,30,48,80\}
}
$$

as the integers satisfying \(V_1(n)=1\) throughout the range \(n\le 5\cdot10^7\).

This is a **finite computational result** and is not intended as evidence of a proof for the infinite problem.

The computation also records the minimal witness

$$
\kappa(n)=\min\{k\ge1:V(n,k)\ge2\}
$$

for every non-exceptional \(n\) in the computed range.

## Repository Structure

```text
.
├── data/          # Computational data and recorded results
├── paper/         # Research manuscript
├── src/           # Exact computational implementation
├── Makefile       # Build / reproduction commands
└── README.md
```

## Reproducibility

The computational experiments are designed to be reproducible from the source code in `src/`.

The mathematical derivations and proofs are documented in the manuscript in `paper/`.

## Research Status

This is an ongoing independent research project.

The goal is to obtain further structural reductions and understand the remaining Diophantine branches of the Erdős–Selfridge prime-power variant.

---

### Paper

The full mathematical development is available in:

[`paper/main.tex`](paper/main.tex)

### Author

**Victor Manuel Mesa Solano**

Undergraduate student in Mathematics and Engineering Physics at CFIS, Universitat Politècnica de Catalunya.
