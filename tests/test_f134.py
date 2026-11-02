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

if __name__ == "__main__": unittest.main()
