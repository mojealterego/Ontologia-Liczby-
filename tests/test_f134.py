import unittest

def convolution(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result

def mass(a): return sum(a)
def moment(a): return sum(i*x for i, x in enumerate(a))

class TestF134(unittest.TestCase):
    def test_mass(self):
        for a in ([1,2], [1,-1], [0,3,2]):
            for b in ([2,4], [1,-1,3]):
                self.assertEqual(mass(convolution(a,b)), mass(a)*mass(b))
    def test_first_moment(self):
        for a in ([1,2], [1,-1], [0,3,2]):
            for b in ([2,4], [1,-1,3]):
                self.assertEqual(moment(convolution(a,b)), moment(a)*mass(b)+mass(a)*moment(b))
    def test_associativity(self):
        self.assertEqual(convolution(convolution([1,2],[3,-1]),[2,0,4]), convolution([1,2],convolution([3,-1],[2,0,4])))
    def test_examples(self):
        self.assertEqual(convolution([2,3],[4,5]),[8,22,15])
        self.assertEqual(convolution([1,2,1],[1,-1]),[1,1,-1,-1])
        self.assertEqual(convolution([1,2],[3,4]),[3,10,8])
    def test_counterexamples(self):
        self.assertEqual(mass([1,2,1]),mass([2,0,2]))
        self.assertNotEqual([1,2,1],[2,0,2])
        self.assertEqual(mass(convolution([1,-1],[1,1])),0)


    def test_second_moment_exhaustive(self):
        from itertools import product
        for la in (1,2,3):
            for lb in (1,2,3):
                for a in product((-1,0,1),repeat=la):
                    for b in product((-1,0,1),repeat=lb):
                        c=convolution(a,b)
                        second=lambda seq:sum(i*i*x for i,x in enumerate(seq))
                        expected=second(a)*mass(b)+2*moment(a)*moment(b)+mass(a)*second(b)
                        self.assertEqual(second(c),expected)
    def test_formal_derivative_identity(self):
        for a in ([1,2,1],[1,-2,1],[0,0,4]):
            second=sum(i*i*x for i,x in enumerate(a))
            factorial=sum(i*(i-1)*x for i,x in enumerate(a))
            self.assertEqual(second,factorial+moment(a))
    def test_shift(self):
        for a in ([2,3],[1,-2,1],[0,3]):
            for r in range(5):
                shifted=[0]*r+list(a)
                self.assertEqual(mass(shifted),mass(a))
                self.assertEqual(moment(shifted),moment(a)+r*mass(a))
                second=lambda s:sum(i*i*x for i,x in enumerate(s))
                self.assertEqual(second(shifted),second(a)+2*r*moment(a)+r*r*mass(a))
    def test_nonidentifiability_moments(self):
        a,b=[1,0,3,0],[0,3,0,1]
        self.assertNotEqual(a,b)
        for k in range(3):
            self.assertEqual(sum(i**k*x for i,x in enumerate(a)),sum(i**k*x for i,x in enumerate(b)))

if __name__ == "__main__": unittest.main()
