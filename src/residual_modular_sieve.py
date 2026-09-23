#!/usr/bin/env python3

from collections import defaultdict


def sieve(n):
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[:2] = b"\x00\x00"

    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            is_prime[p * p : n + 1 : p] = b"\x00" * (
                (n - p * p) // p + 1
            )

    return is_prime


def factorize(n):
    factors = []

    p = 2

    while p * p <= n:
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p

        p += 1 if p == 2 else 2

    if n > 1:
        factors.append(n)

    return factors


def multiplicative_order(a, p):
    order = p - 1

    for q in factorize(p - 1):
        while order % q == 0 and pow(a, order // q, p) == 1:
            order //= q

    return order


def discrete_log_classes(a, target, p):
    """
    Return all r modulo ord_p(a) such that

        a^r = target (mod p).

    There is at most one such residue modulo the order.
    """
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

    forbidden_a = defaultdict(set)
    forbidden_b = defaultdict(set)

    print("Residual modular sieve")
    print(f"prime limit = {PRIME_LIMIT}")
    print()

    for q in range(7, PRIME_LIMIT + 1):
        if not is_prime[q] or q == 5:
            continue

        a = pow(5, 6, q)
        inv3 = pow(3, q - 2, q)

        # A_r = 3*5^(6r) - 2.
        #
        # q | A_r  <=>  a^r = 2/3 (mod q).
        target_a = 2 * inv3 % q

        order, residue = discrete_log_classes(a, target_a, q)

        if residue is not None and q % 5 != 3:
            forbidden_a[order].add(residue)

            print(
                f"A: q={q:4d}, "
                f"order={order:4d}, "
                f"r ≡ {residue:4d} (mod {order})"
            )

        # B_r = (3*5^(6r)+1)/4.
        #
        # q | B_r  <=>  a^r = -1/3 (mod q).
        target_b = (-inv3) % q

        order, residue = discrete_log_classes(a, target_b, q)

        if residue is not None and q % 5 == 1:
            forbidden_b[order].add(residue)

            print(
                f"B: q={q:4d}, "
                f"order={order:4d}, "
                f"r ≡ {residue:4d} (mod {order})"
            )

    def survives(r):
        for modulus, residues in forbidden_a.items():
            if r % modulus in residues:
                return False

        for modulus, residues in forbidden_b.items():
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
    print(f"Forbidden A moduli: {len(forbidden_a)}")
    print(f"Forbidden B moduli: {len(forbidden_b)}")
    print(f"R range: 1..{R_LIMIT}")
    print(f"Survivors: {len(survivors)}")
    print(f"Survival rate: {len(survivors) / R_LIMIT:.4f}")
    print()
    print("First survivors:")
    print(survivors[:100])


if __name__ == "__main__":
    main()

