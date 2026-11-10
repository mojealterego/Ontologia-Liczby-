from fractions import Fraction as F
import unittest

def q(edges, costs, scenarios):
    return max(sum(-a*b for a,b in zip(d,k))/g for d,g in zip(edges,costs) for k in scenarios)

class CertificateTests(unittest.TestCase):
    def test_exact_interval(self):
        for a in range(1,12):
            for b in range(1,12):
                for delta in range(0,12):
                    edges=[(F(1),)]
                    costs=[F(a)]
                    S=[(F(-b),)]
                    K=[(F(-b),),(F(-b-delta),)]
                    qs=q(edges,costs,S)
                    qk=q(edges,costs,K)
                    self.assertTrue(qs<=qk<=qs+F(delta,a))
                    self.assertEqual(qk,F(b+delta,a))
    def test_asymmetry(self):
        self.assertEqual(q([(F(1),)],[F(1)],[(F(2),)]),F(-2))
    def test_two_dimensional(self):
        self.assertEqual(q([(F(1),F(0)),(F(0),F(1))],[F(2),F(4)],[(F(-1),F(0)),(F(0),F(-2))]),F(1,2))
    def test_sharpness(self):
        for delta in range(1,100):
            self.assertEqual(q([(F(1),)],[F(1)],[(F(0),),(F(-delta),)])-q([(F(1),)],[F(1)],[(F(0),)]),F(delta))

if __name__=='__main__':
    unittest.main()
