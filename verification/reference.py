from math import prod

def maximal_prime_powers(n: int) -> dict[int, int]:
    """
    Return {p: p^v_p(n)} for every prime p dividing n.
    Uses trial division: intended for small verification cases.
    """
    if n < 1:
        raise ValueError("n must be positive")

    factors = {}
    remaining = n
    p = 2

    while p * p <= remaining:
        if remaining % p == 0:
            q = 1

            while remaining % p == 0:
                remaining //= p
                q *= p

            factors[p] = q

        p = 3 if p == 2 else p + 2

    if remaining > 1:
        factors[remaining] = remaining

    return factors


def validate(n: int, k: int) -> None:
    if n < 1 or k < 0:
        raise ValueError("Require n >= 1 and k >= 0")


def original_direct(n: int, k: int) -> int:
    """Original Erdős 889 definition."""
    validate(n, k)

    primes = set(maximal_prime_powers(n + k))

    for i in range(k):
        primes -= set(maximal_prime_powers(n + i))

    return len(primes)


def original_fast(n: int, k: int) -> int:
    """Count distinct prime divisors p > k."""
    validate(n, k)

    return sum(
        p > k
        for p in maximal_prime_powers(n + k)
    )


def prime_power_direct(n: int, k: int) -> int:
    """
    Count maximal prime-power components of n+k
    which divide none of n,...,n+k-1.
    """
    validate(n, k)

    powers = maximal_prime_powers(n + k).values()

    return sum(
        all((n + i) % q != 0 for i in range(k))
        for q in powers
    )


def prime_power_fast(n: int, k: int) -> int:
    """Count maximal prime-power components q > k."""
    validate(n, k)

    return sum(
        q > k
        for q in maximal_prime_powers(n + k).values()
    )


def lower_bound(k: int, r: int) -> int:
    """
    Necessary bound for r pairwise coprime,
    distinct factors of n+k, all exceeding k.
    """
    if k < 0 or r < 1:
        raise ValueError("Require k >= 0 and r >= 1")

    return prod(k + j for j in range(1, r + 1)) - k


def verify_small(n_max: int = 200, k_max: int = 30):
    for n in range(1, n_max + 1):
        for k in range(k_max + 1):
            a = original_direct(n, k)
            b = original_fast(n, k)

            assert a == b, (n, k, a, b)

            c = prime_power_direct(n, k)
            d = prime_power_fast(n, k)

            assert c == d, (n, k, c, d)

            if a >= 2:
                assert n >= lower_bound(k, 2)

            if c >= 2:
                assert n >= lower_bound(k, 2)


if __name__ == "__main__":
    verify_small()
    print("Reference checks passed.")
