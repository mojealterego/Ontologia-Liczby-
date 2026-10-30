import unittest
from itertools import product
from math import comb


def subrectangles(m, n):
    return [(a,b,c,d) for a in range(m) for b in range(a,m)
            for c in range(n) for d in range(c,n)]


def prefix(matrix):
    m, n = len(matrix), len(matrix[0]) if matrix else 0
    p = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            p[i][j] = matrix[i-1][j-1] + p[i-1][j] + p[i][j-1] - p[i-1][j-1]
    return p


class TestF132(unittest.TestCase):
    def test_count_subrectangles(self):
        for m,n in product(range(7), repeat=2):
            self.assertEqual(len(subrectangles(m,n)), comb(m+1,2)*comb(n+1,2))

    def test_fixed_dimensions(self):
        for m,n in product(range(1,6), repeat=2):
            blocks=subrectangles(m,n)
            for h in range(1,m+1):
                for w in range(1,n+1):
                    self.assertEqual(sum(b-a+1==h and d-c+1==w for a,b,c,d in blocks),(m-h+1)*(n-w+1))

    def test_containing_cell(self):
        for m,n in product(range(1,6), repeat=2):
            blocks=subrectangles(m,n)
            for i in range(m):
                for j in range(n):
                    self.assertEqual(sum(a<=i<=b and c<=j<=d for a,b,c,d in blocks),(i+1)*(m-i)*(j+1)*(n-j))

    def test_total_area(self):
        for m,n in product(range(7),repeat=2):
            self.assertEqual(sum((b-a+1)*(d-c+1) for a,b,c,d in subrectangles(m,n)),comb(m+2,3)*comb(n+2,3))

    def test_grid_edges_and_four_cycles(self):
        for m,n in product(range(1,8),repeat=2):
            vertices=list(product(range(m),range(n)))
            edges={(x,y) for ix,x in enumerate(vertices) for y in vertices[ix+1:] if abs(x[0]-y[0])+abs(x[1]-y[1])==1}
            self.assertEqual(len(edges),m*(n-1)+(m-1)*n)
            adj={v:set() for v in vertices}
            for x,y in edges:
                adj[x].add(y); adj[y].add(x)
            cycles=set()
            for a in vertices:
                for b in adj[a]:
                    for c in adj[b]-{a}:
                        for d in (adj[c] & adj[a])-{b}:
                            if len({a,b,c,d})==4:
                                cycles.add(frozenset((a,b,c,d)))
            self.assertEqual(len(cycles),(m-1)*(n-1))

    def test_checkerboard(self):
        for m,n in product(range(1,11),repeat=2):
            plus=sum((i+j)%2==0 for i,j in product(range(m),range(n)))
            self.assertEqual(abs(2*plus-m*n),m*n%2)

    def test_prefix_and_rect_queries(self):
        for m,n in product(range(1,5),repeat=2):
            matrix=[[((i*7+j*5)%11)-5 for j in range(n)] for i in range(m)]
            p=prefix(matrix)
            for a,b,c,d in subrectangles(m,n):
                direct=sum(matrix[i][j] for i in range(a,b+1) for j in range(c,d+1))
                self.assertEqual(direct,p[b+1][d+1]-p[a][d+1]-p[b+1][c]+p[a][c])
                self.assertEqual(p[b+1][d+1]-p[b][d+1]-p[b+1][d]+p[b][d],matrix[b][d])

    def test_margins_not_unique(self):
        a=[[1,0],[0,1]]
        b=[[0,1],[1,0]]
        self.assertNotEqual(a,b)
        self.assertEqual([sum(row) for row in a],[sum(row) for row in b])
        self.assertEqual([sum(col) for col in zip(*a)],[sum(col) for col in zip(*b)])

    def test_rank_one_minors(self):
        for u in product(range(-2,3),repeat=2):
            for v in product(range(-2,3),repeat=2):
                a=[[x*y for y in v] for x in u]
                self.assertEqual(a[0][0]*a[1][1]-a[0][1]*a[1][0],0)
        self.assertEqual(2*9-6*3,0)

    def test_rank_one_converse_mod_prime(self):
        for entries in product(range(3),repeat=6):
            a=[list(entries[:3]),list(entries[3:])]
            minors=[(a[0][j]*a[1][k]-a[0][k]*a[1][j])%3 for j in range(3) for k in range(j+1,3)]
            if all(v==0 for v in minors):
                pivot=next(((i,j) for i in range(2) for j in range(3) if a[i][j]),None)
                if pivot is None:
                    self.assertTrue(all(x==0 for row in a for x in row))
                else:
                    r,c=pivot
                    inv=pow(a[r][c],-1,3)
                    u=[a[i][c] for i in range(2)]
                    v=[a[r][j]*inv%3 for j in range(3)]
                    self.assertEqual([[x*y%3 for y in v] for x in u],a)

    def test_boundary_vertices(self):
        for m,n in product(range(1,9),repeat=2):
            pts=list(product(range(m+1),range(n+1)))
            self.assertEqual(sum(i in (0,m) or j in (0,n) for i,j in pts),2*(m+n))

    def test_exercises(self):
        self.assertEqual(comb(4,2)*comb(5,2),60)
        self.assertEqual((5-2+1)*(7-3+1),20)
        self.assertEqual(2*4*4*3,96)
        self.assertEqual(comb(4,3)*comb(5,3),40)
        self.assertEqual(4*4+3*5,31)
        self.assertEqual(3*4,12)
        self.assertEqual(45-6-12+1,28)
        self.assertEqual(8-1-5+2,4)
        self.assertEqual(2*(4+6),20)


if __name__ == '__main__':
    unittest.main()
