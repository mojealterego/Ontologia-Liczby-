"""Exact rational regression for F28.2-DO. Run: python -m unittest tests/test_f28_2do.py"""
import unittest
from fractions import Fraction as F

def h_of_atoms(atoms, t):
    """atoms: sorted (value, mass) with total mass one."""
    remaining = t
    total = F(0)
    for value, mass in reversed(atoms):
        take = min(mass, remaining)
        total += value * take
        remaining -= take
        if remaining == 0:
            break
    return total

class QuantileBudgetTests(unittest.TestCase):
    def test_endpoint_and_concavity(self):
        for n in range(2, 13):
            atoms = [(F(i,n),F(1,n+1)) for i in range(n+1)]
            vals = [h_of_atoms(atoms,F(k,2*n)) for k in range(2*n+1)]
            self.assertEqual(vals[0],0)
            self.assertEqual(vals[-1],F(1,2))
            slopes=[vals[k+1]-vals[k] for k in range(2*n)]
            self.assertTrue(all(slopes[k]>=slopes[k+1] for k in range(len(slopes)-1)))
    def test_transport_and_uniform_error(self):
        for n in range(2,17):
            mu=[(F(0),F(1,2)),(F(1),F(1,2))]
            nu=[(F(0),F(1,n)),(F(1),1-F(1,n))]
            w=abs(F(1,2)-F(1,n))
            errors=[abs(h_of_atoms(mu,F(k,2*n))-h_of_atoms(nu,F(k,2*n))) for k in range(2*n+1)]
            self.assertLessEqual(max(errors),w)
    def test_grid_reconstruction_bound(self):
        for n in range(2,20):
            atoms=[(F(0),F(1,3)),(F(1,2),F(1,3)),(F(1),F(1,3))]
            # grid slope is mean reversed quantile on each cell; W1 via exact common refinement
            grid=[F(i,n) for i in range(n+1)]
            slopes=[(h_of_atoms(atoms,grid[i+1])-h_of_atoms(atoms,grid[i]))*n for i in range(n)]
            cuts=sorted(set(grid+[F(1,3),F(2,3)]))
            cost=F(0)
            for left,right in zip(cuts,cuts[1:]):
                mid=(left+right)/2
                original=F(1) if mid<F(1,3) else (F(1,2) if mid<F(2,3) else F(0))
                reconstructed=slopes[min(int(mid*n),n-1)]
                cost+=(right-left)*abs(original-reconstructed)
            self.assertLessEqual(cost,F(1,n))
    def test_nonidentifiability(self):
        mu=[(F(1,2),F(1))]
        nu=[(F(0),F(1,2)),(F(1),F(1,2))]
        for t in [F(0),F(1)]:
            self.assertEqual(h_of_atoms(mu,t),h_of_atoms(nu,t))
        self.assertNotEqual(h_of_atoms(mu,F(1,2)),h_of_atoms(nu,F(1,2)))

if __name__=="__main__":
    unittest.main()
