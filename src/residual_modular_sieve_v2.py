from collections import defaultdict
from math import isqrt

PRIME_LIMIT = 5000
R_LIMIT = 10000

MAX_P_PRIMALITY_CHECKS = 100

def sieve(n):
    is_prime = bytearray(b"\x01") * (n + 1)

    if n >= 0:
        is_prime[0] = 0

    if n >= 1:
        is_prime[1] = 0

    for p in range(2, isqrt(n) + 1):
        if is_prime[p]:
            start = p * p
            length = (n - start) // p + 1
            is_prime[start:n + 1:p] = b"\x00" * length

    return is_prime


def factorize(n):
    factors = []

    if n % 2 == 0:
        factors.append(2)

        while n % 2 == 0:
            n //= 2

    p = 3

    while p * p <= n:
        if n % p == 0:
            factors.append(p)

            while n % p == 0:
                n //= p

        p += 2

    if n > 1:
        factors.append(n)

    return factors


def multiplicative_order(a, p):
    order = p - 1

    for q in factorize(order):
        while order % q == 0 and pow(a, order // q, p) == 1:
            order //= q

    return order


def discrete_log_class(a, target, p):
    order = multiplicative_order(a, p)

    x = 1

    for r in range(order):
        if x == target:
            return order, r

        x = x * a % p

    return order, None

_SMALL_PRIMES = [
    2, 3, 5, 7, 11, 13, 17, 19,
    23, 29, 31, 37, 41, 43, 47
]


def is_probable_prime(n):
    if n < 2:
        return False

    for p in _SMALL_PRIMES:
        if n == p:
            return True

        if n % p == 0:
            return False

    d = n - 1
    s = 0

    while d % 2 == 0:
        s += 1
        d //= 2
    bases = [
        2, 3, 5, 7, 11, 13,
        17, 19, 23, 29, 31, 37
    ]

    for a in bases:
        if a >= n:
            continue

        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = x * x % n

            if x == n - 1:
                break
        else:
            return False

    return True

def A_value(r):

    return 3 * pow(5, 6 * r) - 2


def B_value(r):
    return (3 * pow(5, 6 * r) + 1) // 4


def P_value(r):
    return 3 * pow(5, 6 * r) + 2

def main():
    is_prime = sieve(PRIME_LIMIT)

    A_divisors = [set() for _ in range(R_LIMIT + 1)]
    B_divisors = [set() for _ in range(R_LIMIT + 1)]
    P_divisors = [set() for _ in range(R_LIMIT + 1)]

    print("Residual modular sieve v2")
    print(f"prime limit = {PRIME_LIMIT}")
    print(f"r range = 1..{R_LIMIT}")
    print()
    for q in range(7, PRIME_LIMIT + 1):
        if not is_prime[q]:
            continue
        a = pow(5, 6, q)

        inv3 = pow(3, q - 2, q)

        order = multiplicative_order(a, q)

        target_A = 2 * inv3 % q
        _, residue_A = discrete_log_class(
            a,
            target_A,
            q,
        )

        if residue_A is not None:
            for r in range(residue_A, R_LIMIT + 1, order):
                if r >= 1:
                    A_divisors[r].add(q)

        target_B = (-inv3) % q

        _, residue_B = discrete_log_class(
            a,
            target_B,
            q,
        )

        if residue_B is not None:
            for r in range(residue_B, R_LIMIT + 1, order):
                if r >= 1:
                    B_divisors[r].add(q)

        target_P = (-2 * inv3) % q

        _, residue_P = discrete_log_class(
            a,
            target_P,
            q,
        )

        if residue_P is not None:
            for r in range(residue_P, R_LIMIT + 1, order):
                if r >= 1:
                    P_divisors[r].add(q)

    survivors = []

    rejected_P_composite = 0
    rejected_A_bad_base = 0
    rejected_A_multiple = 0
    rejected_B_bad_base = 0
    rejected_B_multiple = 0

    for r in range(1, R_LIMIT + 1):
        A = A_divisors[r]
        B = B_divisors[r]
        P = P_divisors[r]

        rejected = False

        if P:
            rejected_P_composite += 1
            rejected = True

        if not rejected:
            bad_A = [q for q in A if q % 5 != 3]

            if bad_A:
                rejected_A_bad_base += 1
                rejected = True

        if not rejected and len(A) >= 2:
            rejected_A_multiple += 1
            rejected = True

        if not rejected:
            bad_B = [q for q in B if q % 5 == 1]

            if bad_B:
                rejected_B_bad_base += 1
                rejected = True

        if not rejected and len(B) >= 2:
            rejected_B_multiple += 1
            rejected = True

        if not rejected:
            survivors.append(r)


    print("Summary")
    print("-------")

    print(f"R range:                 1..{R_LIMIT}")
    print(f"Initial candidates:      {R_LIMIT}")
    print()

    print(f"Rejected by P_r:         {rejected_P_composite}")
    print(f"Rejected by A base:      {rejected_A_bad_base}")
    print(f"Rejected by A factors:   {rejected_A_multiple}")
    print(f"Rejected by B base:      {rejected_B_bad_base}")
    print(f"Rejected by B factors:   {rejected_B_multiple}")
    print()

    print(f"Survivors:               {len(survivors)}")
    print(f"Survival rate:           {len(survivors) / R_LIMIT:.4f}")
    print()

    print("First survivors:")
    print(survivors[:100])

    if MAX_P_PRIMALITY_CHECKS > 0:
        checked = survivors[:MAX_P_PRIMALITY_CHECKS]

        print()
        print(
            f"Probable-prime test for P_r "
            f"on first {len(checked)} survivors"
        )
        print("---------------------------------------------")

        probable_primes = []
        composites = []

        for r in checked:
            p = P_value(r)

            if is_probable_prime(p):
                probable_primes.append(r)
            else:
                composites.append(r)

        print(f"Probable primes: {probable_primes}")
        print(f"Composite:       {composites}")


if __name__ == "__main__":
    main()