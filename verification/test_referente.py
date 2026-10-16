
import unittest

from verification.reference import (
    maximal_prime_powers,
    original_direct,
    original_fast,
    prime_power_direct,
    prime_power_fast,
    lower_bound,
    verify_small,
)


class TestReference(unittest.TestCase):

    def test_factorization(self):
        self.assertEqual(
            maximal_prime_powers(360),
            {2: 8, 3: 9, 5: 5},
        )

    def test_original(self):
        self.assertEqual(original_direct(5, 1), 2)
        self.assertEqual(original_fast(5, 1), 2)

    def test_variants_differ(self):
        self.assertEqual(original_fast(6, 3), 0)
        self.assertEqual(prime_power_fast(6, 3), 1)
        self.assertEqual(prime_power_direct(6, 3), 1)

    def test_bound(self):
        self.assertEqual(lower_bound(1, 2), 5)
        self.assertEqual(lower_bound(3, 2), 17)

    def test_exhaustive_small(self):
        verify_small(n_max=200, k_max=30)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            original_fast(0, 2)


if __name__ == "__main__":
    unittest.main()
