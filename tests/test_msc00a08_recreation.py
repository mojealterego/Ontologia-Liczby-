"""Independent finite checks for MSC 00A08. No external dependencies."""
import collections
import itertools
import math
import unittest
from pathlib import Path


def domino_count(n):
    """Count tilings by column-mask transfer, independently of Fibonacci recurrence."""
    states = {0: 1}
    for _ in range(n):
        nxt = collections.defaultdict(int)
        for mask, count in states.items():
            def fill(row, occupied, future):
                if row == 2:
                    nxt[future] += count
                    return
                if occupied & (1 << row):
                    fill(row + 1, occupied, future)
                    return
                if row == 0 and not (occupied & 2):
                    fill(2, occupied | 3, future)
                fill(row + 1, occupied | (1 << row), future | (1 << row))
            fill(0, mask, 0)
        states = nxt
    return states.get(0, 0)


def is_bipartite(n, edges):
    adjacency = [set() for _ in range(n)]
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    colors = {}
    for start in range(n):
        if start in colors:
            continue
        colors[start] = 0
        q = collections.deque([start])
        while q:
            u = q.popleft()
            for v in adjacency[u]:
                if v in colors:
                    if colors[v] == colors[u]:
                        return False
                else:
                    colors[v] = 1 - colors[u]
                    q.append(v)
    return True


def has_odd_cycle(n, edges):
    """Enumerate all simple cycles of odd length; independent of BFS coloring."""
    adjacency = [set() for _ in range(n)]
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    def walk(start, current, visited):
        if len(visited) >= 3 and len(visited) % 2 == 1 and start in adjacency[current]:
            return True
        for v in adjacency[current]:
            if v not in visited and walk(start, v, visited | {v}):
                return True
        return False
    return any(walk(s, s, {s}) for s in range(n))


def has_euler_walk(n, edges, require_closed):
    if not edges:
        return True
    incidence = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        incidence[u].append((v, i))
        incidence[v].append((u, i))
    for start in range(n):
        if not incidence[start]:
            continue
        def walk(v, used):
            if used == (1 << len(edges)) - 1:
                return not require_closed or v == start
            return any(walk(w, used | (1 << eid)) for w, eid in incidence[v] if not (used >> eid) & 1)
        if walk(start, 0):
            return True
    return False


def josephus_sim(n):
    persons = list(range(1, n + 1))
    index = 0
    while len(persons) > 1:
        index = (index + 1) % len(persons)
        persons.pop(index)
        if persons:
            index %= len(persons)
    return persons[0]


def hanoi_distance(n):
    start = (0,) * n
    goal = (2,) * n
    q = collections.deque([(start, 0)])
    seen = {start}
    while q:
        state, dist = q.popleft()
        if state == goal:
            return dist
        top = {}
        for disk, peg in enumerate(state):
            top.setdefault(peg, disk)
        for source, disk in top.items():
            for target in range(3):
                if source == target or (target in top and top[target] < disk):
                    continue
                new = list(state)
                new[disk] = target
                new = tuple(new)
                if new not in seen:
                    seen.add(new)
                    q.append((new, dist + 1))
    raise AssertionError("Unreachable")


class RecreationalMathematicsTests(unittest.TestCase):
    def test_chessboard_corner_parity(self):
        board = [(r, c) for r in range(8) for c in range(8)]
        rest = [p for p in board if p not in {(0, 0), (7, 7)}]
        self.assertEqual(sum((r + c) % 2 == 0 for r, c in rest), 30)
        self.assertEqual(sum((r + c) % 2 == 1 for r, c in rest), 32)

    def test_domino_count_by_transfer(self):
        a, b = 1, 1
        self.assertEqual(domino_count(0), 1)
        self.assertEqual(domino_count(1), 1)
        for n in range(2, 11):
            a, b = b, a + b
            self.assertEqual(domino_count(n), b)

    def test_polyomino_perimeter(self):
        samples = [
            {(0, 0)},
            {(0, 0), (1, 0), (2, 0)},
            {(0, 0), (0, 1), (1, 0)},
            {(0, 0), (0, 1), (1, 0), (1, 1)},
        ]
        for cells in samples:
            e = sum(((r + 1, c) in cells) + ((r, c + 1) in cells) for r, c in cells)
            boundary = sum((r + dr, c + dc) not in cells
                           for r, c in cells for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
            self.assertEqual(boundary, 4 * len(cells) - 2 * e)

    def test_handshake_all_graphs_on_five_vertices(self):
        pairs = list(itertools.combinations(range(5), 2))
        for mask in range(1 << len(pairs)):
            edges = [p for i, p in enumerate(pairs) if mask & (1 << i)]
            degrees = [sum(v in e for e in edges) for v in range(5)]
            self.assertEqual(sum(degrees), 2 * len(edges))
            self.assertEqual(sum(d % 2 for d in degrees) % 2, 0)

    def test_bipartite_odd_cycle_all_graphs_on_five_vertices(self):
        pairs = list(itertools.combinations(range(5), 2))
        for mask in range(1 << len(pairs)):
            edges = [p for i, p in enumerate(pairs) if mask & (1 << i)]
            self.assertEqual(is_bipartite(5, edges), not has_odd_cycle(5, edges))

    def test_euler_circuit_brute_force_four_vertices(self):
        pairs = list(itertools.combinations(range(4), 2))
        for mask in range(1 << len(pairs)):
            edges = [p for i, p in enumerate(pairs) if mask & (1 << i)]
            if not edges:
                continue
            degrees = [sum(v in e for e in edges) for v in range(4)]
            adj = [set() for _ in range(4)]
            for u, v in edges:
                adj[u].add(v)
                adj[v].add(u)
            nonzero = [i for i in range(4) if degrees[i]]
            reached = {nonzero[0]}
            frontier = [nonzero[0]]
            while frontier:
                for v in adj[frontier.pop()]:
                    if v not in reached:
                        reached.add(v)
                        frontier.append(v)
            expected = len(reached) == len(nonzero) and all(d % 2 == 0 for d in degrees)
            self.assertEqual(has_euler_walk(4, edges, True), expected)

    def test_euler_open_walk_four_vertices(self):
        pairs = list(itertools.combinations(range(4), 2))
        for mask in range(1 << len(pairs)):
            edges = [p for i, p in enumerate(pairs) if mask & (1 << i)]
            if not edges:
                continue
            degrees = [sum(v in e for e in edges) for v in range(4)]
            adj = [set() for _ in range(4)]
            for u, v in edges:
                adj[u].add(v)
                adj[v].add(u)
            nonzero = [i for i in range(4) if degrees[i]]
            reached = {nonzero[0]}
            frontier = [nonzero[0]]
            while frontier:
                for v in adj[frontier.pop()]:
                    if v not in reached:
                        reached.add(v)
                        frontier.append(v)
            expected = len(reached) == len(nonzero) and sum(d % 2 for d in degrees) == 2
            self.assertEqual(
                has_euler_walk(4, edges, False) and not has_euler_walk(4, edges, True),
                expected)

    def test_planar_grid_euler(self):
        for rows in range(1, 7):
            for cols in range(1, 7):
                v = (rows + 1) * (cols + 1)
                e = rows * (cols + 1) + cols * (rows + 1)
                f = rows * cols + 1
                self.assertEqual(v - e + f, 2)

    def test_subtraction_12(self):
        win = [False]
        for n in range(1, 300):
            win.append(any(not win[n - m] for m in (1, 2) if n >= m))
            self.assertEqual(win[n], n % 3 != 0)

    def test_subtraction_13(self):
        win = [False]
        for n in range(1, 300):
            win.append(any(not win[n - m] for m in (1, 3) if n >= m))
            self.assertEqual(win[n], n % 2 != 0)

    def test_grundy_zero_equivalence(self):
        g = [0]
        win = [False]
        for n in range(1, 150):
            options = {g[n - m] for m in (1, 2) if n >= m}
            mex = next(x for x in range(4) if x not in options)
            g.append(mex)
            win.append(any(not win[n - m] for m in (1, 2) if n >= m))
            self.assertEqual(g[n] == 0, not win[n])

    def test_hanoi_shortest_path_bfs(self):
        for n in range(0, 6):
            self.assertEqual(hanoi_distance(n), 2 ** n - 1)

    def test_josephus_simulation(self):
        for n in range(1, 301):
            power = 1 << (n.bit_length() - 1)
            self.assertEqual(josephus_sim(n), 2 * (n - power) + 1)

    def test_ramsey_six_exhaustive_two_colorings(self):
        triples = list(itertools.combinations(range(6), 3))
        pairs = list(itertools.combinations(range(6), 2))
        pair_id = {p: i for i, p in enumerate(pairs)}
        triangle_masks = [
            sum(1 << pair_id[p] for p in itertools.combinations(t, 2))
            for t in triples
        ]
        for coloring in range(1 << len(pairs)):
            self.assertTrue(any(
                coloring & triangle == 0 or coloring & triangle == triangle
                for triangle in triangle_masks
            ))

    def test_five_cycle_counterexample(self):
        vertices = range(5)
        red = {tuple(sorted((i, (i + 1) % 5))) for i in vertices}
        for t in itertools.combinations(vertices, 3):
            red_count = sum(tuple(sorted(p)) in red for p in itertools.combinations(t, 2))
            self.assertNotIn(red_count, (0, 3))

    def test_weighing_information_lower_bound(self):
        for n in range(1, 1000):
            k = 0
            while 3 ** k < n:
                k += 1
            self.assertLess(3 ** (k - 1), n) if k else self.assertEqual(n, 1)
            self.assertGreaterEqual(3 ** k, n)

    def test_odd_board_closed_knight_tour_parity(self):
        for n in (1, 3, 5, 7, 9):
            self.assertEqual((n * n) % 2, 1)
            for r in range(n):
                for c in range(n):
                    for dr, dc in ((1, 2), (2, 1), (-1, 2), (-2, 1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            self.assertNotEqual((r + c) % 2, (nr + nc) % 2)

    def test_odd_sum_identity(self):
        for n in range(0, 1001):
            self.assertEqual(sum(2 * i - 1 for i in range(1, n + 1)), n * n)

    def test_modular_obstruction(self):
        reached = {0}
        for _ in range(10):
            reached |= {x + d for x in list(reached) for d in (-4, 4)}
        self.assertNotIn(2, reached)
        self.assertTrue(all(x % 4 == 0 for x in reached))

    def test_markdown_structure(self):
        src = Path(__file__).resolve().parents[1] / "manuscript/tom-01/MSC00/00A08_MATEMATYKA_REKREACYJNA.md"
        text = src.read_text(encoding="utf-8")
        for prefix, count in (("D", 12), ("T", 20), ("K", 10), ("Z", 24)):
            for i in range(1, count + 1):
                self.assertIn(f"**{prefix}{i:02d}", text)
        self.assertNotIn("TODO", text)
        self.assertIn("585 stron bez zmian", text)


if __name__ == "__main__":
    unittest.main()
