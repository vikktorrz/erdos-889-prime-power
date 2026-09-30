from collections import defaultdict
from math import isqrt


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


def discrete_log_classes(a, target, p):
    order = multiplicative_order(a, p)

    x = 1

    for r in range(order):
        if x == target:
            return order, r

        x = x * a % p

    return order, None


def main():
    PRIME_LIMIT = 5000
    R_LIMIT = 10000

    is_prime = sieve(PRIME_LIMIT)
    forbidden_A = defaultdict(set)

    forbidden_B = defaultdict(set)

    forbidden_P = defaultdict(set)

    print("Residual modular sieve")
    print(f"prime limit = {PRIME_LIMIT}")
    print(f"r range = 1..{R_LIMIT}")
    print()

    for q in range(7, PRIME_LIMIT + 1):
        if not is_prime[q] or q == 5:
            continue

        a = pow(5, 6, q)

        inv3 = pow(3, q - 2, q)

        target_A = 2 * inv3 % q

        order, residue = discrete_log_classes(
            a,
            target_A,
            q,
        )

        if residue is not None and q % 5 != 3:
            forbidden_A[order].add(residue)

            print(
                f"A: q={q:4d}, "
                f"order={order:4d}, "
                f"r ≡ {residue:4d} (mod {order})"
            )


        target_B = (-inv3) % q

        order, residue = discrete_log_classes(
            a,
            target_B,
            q,
        )

        if residue is not None and q % 5 == 1:
            forbidden_B[order].add(residue)

            print(
                f"B: q={q:4d}, "
                f"order={order:4d}, "
                f"r ≡ {residue:4d} (mod {order})"
            )
        target_P = (-2 * inv3) % q

        order, residue = discrete_log_classes(
            a,
            target_P,
            q,
        )

        if residue is not None:
            forbidden_P[order].add(residue)

            print(
                f"P: q={q:4d}, "
                f"order={order:4d}, "
                f"r ≡ {residue:4d} (mod {order})"
            )

    def survives(r):
        for modulus, residues in forbidden_A.items():
            if r % modulus in residues:
                return False

        for modulus, residues in forbidden_B.items():
            if r % modulus in residues:
                return False

        for modulus, residues in forbidden_P.items():
            if r % modulus in residues:
                return False

        return True

    survivors = [
        r
        for r in range(1, R_LIMIT + 1)
        if survives(r)
    ]

    print()
    print("Summary")
    print("-------")

    print(f"Forbidden A moduli: {len(forbidden_A)}")
    print(f"Forbidden B moduli: {len(forbidden_B)}")
    print(f"Forbidden P moduli: {len(forbidden_P)}")

    print(f"R range: 1..{R_LIMIT}")
    print(f"Survivors: {len(survivors)}")
    print(f"Survival rate: {len(survivors) / R_LIMIT:.4f}")

    print()
    print("First survivors:")
    print(survivors[:100])


if __name__ == "__main__":
    main()