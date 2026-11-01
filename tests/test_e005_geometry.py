"""E0-05 — executable invariants of Euclidean geometry and grid routes."""
import math
import unittest
from itertools import product


def d2(a, b):
    return sum((a[i] - b[i]) ** 2 for i in (0, 1))


def translation(p, v):
    return (p[0] + v[0], p[1] + v[1])


def reflection(p):
    return (-p[0], p[1])


def quarter_turn(p):
    return (-p[1], p[0])


class E005GeometryTests(unittest.TestCase):
    def test_distance_symmetry_and_separation(self):
        points = list(product(range(-3, 4), repeat=2))
        for a in points:
            for b in points:
                self.assertEqual(d2(a, b), d2(b, a))
                self.assertEqual(d2(a, b) == 0, a == b)

    def test_translation_isometry(self):
        points = list(product(range(-2, 3), repeat=2))
        for a in points:
            for b in points:
                for v in ((0, 0), (4, -7), (-2, 9)):
                    self.assertEqual(d2(translation(a, v), translation(b, v)), d2(a, b))

    def test_reflection_isometry_involution(self):
        points = list(product(range(-3, 4), repeat=2))
        for a in points:
            self.assertEqual(reflection(reflection(a)), a)
            for b in points:
                self.assertEqual(d2(reflection(a), reflection(b)), d2(a, b))

    def test_quarter_turn_isometry_order_four(self):
        points = list(product(range(-3, 4), repeat=2))
        for a in points:
            r = a
            for _ in range(4):
                r = quarter_turn(r)
            self.assertEqual(r, a)
            for b in points:
                self.assertEqual(d2(quarter_turn(a), quarter_turn(b)), d2(a, b))

    def test_manhattan_lower_bound_and_examples(self):
        for a in product(range(-3, 4), repeat=2):
            for b in product(range(-3, 4), repeat=2):
                manhattan = abs(a[0]-b[0]) + abs(a[1]-b[1])
                self.assertGreaterEqual(manhattan * manhattan, d2(a, b))
        self.assertEqual(abs(3)+abs(4), 7)
        self.assertEqual(math.isqrt(d2((0,0),(3,4))), 5)

    def test_square_and_rectangle(self):
        for a in range(1, 12):
            self.assertEqual(4*a, 2*(a+a))
            self.assertEqual(a*a, len(list(product(range(a), repeat=2))))
        self.assertEqual(2*(1+5), 2*(2+4))
        self.assertNotEqual(1*5, 2*4)

    def test_cuboid_combinatorics(self):
        vertices = list(product((0,1), repeat=3))
        edges = [(a,b) for i,a in enumerate(vertices) for b in vertices[i+1:] if sum(x != y for x,y in zip(a,b)) == 1]
        self.assertEqual(len(vertices), 8)
        self.assertEqual(len(edges), 12)
        self.assertEqual(8-12+6, 2)

    def test_six_square_rectangle_has_adjacency_cycle(self):
        cells = list(product(range(2), range(3)))
        adj = [(a,b) for i,a in enumerate(cells) for b in cells[i+1:] if abs(a[0]-b[0])+abs(a[1]-b[1]) == 1]
        self.assertEqual(len(cells), 6)
        self.assertEqual(len(adj), 7)
        self.assertGreater(len(adj), len(cells)-1)

    def test_book_exercise_values(self):
        self.assertEqual(8*5,40)
        self.assertEqual(2*(8+5),26)
        self.assertEqual((2+3-1,1+4),(4,5))
        self.assertEqual(abs(4-2)+abs(5-1),6)
        self.assertEqual(2*(2*3+2*4+3*4),52)


if __name__ == '__main__':
    unittest.main()
