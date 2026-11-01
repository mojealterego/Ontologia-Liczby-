"""Finite-model checks for E0-02; Python standard library only."""
import itertools
import unittest


def digits(n: int) -> str:
    if n < 0:
        raise ValueError("Only nonnegative integers")
    return str(n)


def evaluate_decimal(word: str) -> int:
    if not word or any(c not in "0123456789" for c in word):
        raise ValueError("Invalid decimal word")
    return sum(int(c) * 10 ** i for i, c in enumerate(reversed(word)))


def round_half_up(n: int, q: int) -> int:
    if n < 0 or q <= 0:
        raise ValueError("Domain: n>=0, q>0")
    a, r = divmod(n, q)
    return q * (a + (2 * r >= q))


class TestNaturalNumbersE002(unittest.TestCase):
    def test_cardinality_permutation_invariance(self):
        for n in range(7):
            values = tuple(range(n))
            for p in itertools.permutations(values):
                self.assertEqual(len(p), n)
                self.assertEqual(set(p), set(values))

    def test_cardinality_new_element(self):
        for n in range(150):
            a = set(range(n))
            self.assertEqual(len(a | {n}), n + 1)
            if n:
                self.assertEqual(len(a | {0}), n)

    def test_successor_injective(self):
        self.assertEqual(len({n + 1 for n in range(500)}), 500)

    def test_zero_is_natural(self):
        self.assertEqual(digits(0), "0")
        self.assertEqual(evaluate_decimal("0"), 0)

    def test_decimal_roundtrip(self):
        for n in range(10001):
            self.assertEqual(evaluate_decimal(digits(n)), n)

    def test_leading_zero_same_value(self):
        for n in range(1000):
            self.assertEqual(evaluate_decimal("000" + digits(n)), n)

    def test_decimal_length_bounds(self):
        for n in range(1, 100001):
            k = len(digits(n))
            self.assertLessEqual(10 ** (k - 1), n)
            self.assertLessEqual(n, 10 ** k - 1)

    def test_decimal_uniqueness_small_exhaustive(self):
        words = ["0"] + [str(n) for n in range(1, 10000)]
        self.assertEqual(len({evaluate_decimal(w) for w in words}), len(words))

    def test_lex_order_matches_integer(self):
        for a in range(100):
            for b in range(100):
                sa, sb = str(a), str(b)
                self.assertEqual((len(sa), sa) < (len(sb), sb), a < b)

    def test_largest_three_digit(self):
        self.assertEqual(max(range(100, 1000)), 999)

    def test_count_two_digit(self):
        self.assertEqual(len(range(10, 100)), 90)

    def test_carry_equivalence(self):
        for j in range(7):
            self.assertEqual(10 * 10 ** j, 10 ** (j + 1))

    def test_rounding_error(self):
        for q in (10, 100, 1000):
            for n in range(3001):
                self.assertLessEqual(2 * abs(round_half_up(n, q) - n), q)

    def test_rounding_multiple(self):
        for q in (10, 100, 1000):
            for n in range(3001):
                self.assertEqual(round_half_up(n, q) % q, 0)

    def test_tie_rounds_up(self):
        for q in (10, 100, 1000):
            for a in range(8):
                self.assertEqual(round_half_up(a * q + q // 2, q), (a + 1) * q)

    def test_rounding_examples(self):
        self.assertEqual(round_half_up(347, 10), 350)
        self.assertEqual(round_half_up(347, 100), 300)
        self.assertEqual(round_half_up(345, 10), 350)
        self.assertEqual(round_half_up(950, 100), 1000)

    def test_rounding_noncommutative_with_sum(self):
        self.assertEqual(round_half_up(14, 10) * 2, 20)
        self.assertEqual(round_half_up(28, 10), 30)

    def test_error_sum_bound(self):
        for x in range(0, 101):
            for y in range(0, 101):
                self.assertLessEqual(abs(round_half_up(x, 10) + round_half_up(y, 10) - x - y), 10)

    def test_interval_sum_bound(self):
        for a in range(0, 10):
            for b in range(a, 15):
                for c in range(0, 8):
                    for d in range(c, 10):
                        self.assertLessEqual(a + c, b + d)

    def test_problem_b_candidates(self):
        candidates = [n for n in range(100, 1000) if 450 < n < 480 and n // 100 == 4 and n % 10 == 7]
        self.assertEqual(candidates, [457, 467, 477])

    def test_problem_c_preimage(self):
        candidates = [n for n in range(400, 601) if round_half_up(n, 100) == 500]
        self.assertEqual(candidates, list(range(450, 550)))

    def test_problem_d_intervals(self):
        a = [n for n in range(100) if round_half_up(n, 10) == 40]
        b = [n for n in range(100) if round_half_up(n, 10) == 70]
        self.assertEqual((min(a), max(a), min(b), max(b)), (35, 44, 65, 74))
        self.assertEqual({x + y for x in a for y in b}, set(range(100, 119)))

    def test_exercise_carry(self):
        self.assertEqual(9 * 10 + 12, 102)

    def test_exercise_digits(self):
        self.assertEqual(evaluate_decimal("6205"), 6205)
        self.assertEqual(evaluate_decimal("4009"), 4009)

    def test_exercise_digit_permutations(self):
        values = [int("".join(p)) for p in itertools.permutations("0137") if p[0] != "0"]
        self.assertEqual(min(values), 1037)
        values = [int("".join(p)) for p in itertools.permutations("2805") if p[0] != "0"]
        self.assertEqual(max(values), 8520)

    def test_invalid_inputs(self):
        for n in (-1, -2):
            with self.assertRaises(ValueError):
                digits(n)
        for word in ("", "-1", "1x"):
            with self.assertRaises(ValueError):
                evaluate_decimal(word)
        with self.assertRaises(ValueError):
            round_half_up(1, 0)


if __name__ == "__main__":
    unittest.main()
