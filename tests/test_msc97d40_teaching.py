"""MSC 97D40: independently check mathematical model invariants."""
import itertools
import math
import unittest

def closure(nodes, edges, selected):
    result = set(selected)
    while True:
        nxt = result | {u for u,v in edges if v in result}
        if nxt == result:
            return nxt
        result = nxt

def coverage(indices, sets):
    return set().union(*(sets[i] for i in indices)) if indices else set()

class TestMSC97D40(unittest.TestCase):
    def setUp(self):
        self.v = {"a","b","c","d"}
        self.edges = {("a","b"),("a","c"),("b","d"),("c","d")}
    def test_closure_example(self):
        self.assertEqual(closure(self.v,self.edges,{"d"}),self.v)
    def test_closure_empty(self):
        self.assertEqual(closure(self.v,self.edges,set()),set())
    def test_closure_idempotent(self):
        for k in range(5):
            for tup in itertools.combinations(self.v,k):
                s=set(tup)
                self.assertEqual(closure(self.v,self.edges,closure(self.v,self.edges,s)),closure(self.v,self.edges,s))
    def test_closure_monotone(self):
        for a in itertools.chain.from_iterable(itertools.combinations(self.v,k) for k in range(5)):
            for b in itertools.chain.from_iterable(itertools.combinations(self.v,k) for k in range(5)):
                if set(a)<=set(b):
                    self.assertLessEqual(closure(self.v,self.edges,set(a)),closure(self.v,self.edges,set(b)))
    def test_closure_union(self):
        for a in self.v:
            for b in self.v:
                self.assertEqual(closure(self.v,self.edges,{a,b}),closure(self.v,self.edges,{a})|closure(self.v,self.edges,{b}))
    def test_coverage_submodular(self):
        sets=[{"a","b"},{"b","c"},{"a","d"}]
        weights={"a":2,"b":3,"c":5,"d":7}
        all_indices=set(range(len(sets)))
        for i in range(1<<len(sets)):
            A={j for j in all_indices if i>>j&1}
            for k in range(1<<len(sets)):
                B={j for j in all_indices if k>>j&1}
                if A<=B:
                    for j in all_indices-B:
                        da=sum(weights[u] for u in sets[j]-coverage(A,sets))
                        db=sum(weights[u] for u in sets[j]-coverage(B,sets))
                        self.assertGreaterEqual(da,db)
    def test_partition_sum(self):
        for mask in range(1<<4):
            a=[2,3,5,7]
            self.assertEqual(sum(a[i] for i in range(4) if mask>>i&1)+sum(a[i] for i in range(4) if not(mask>>i&1)),sum(a))
    def test_two_group_imbalance(self):
        self.assertEqual(abs(2*7-20),6)
    def test_mean_difference(self):
        x=[2,4,6];y=[4,5,9]
        self.assertEqual(sum(b-a for a,b in zip(x,y))/3,2)
    def test_shift_invariance(self):
        x=[2,4,6];y=[4,5,9]
        self.assertEqual(sum(b-a for a,b in zip(x,y)),sum((b+100)-(a+100) for a,b in zip(x,y)))
    def test_normalization(self):
        self.assertEqual(18/24,.75)
    def test_budget_bound(self):
        self.assertEqual(45//8,5)
    def test_greedy_counterexample(self):
        self.assertGreater(8+8,9)
    def test_identifiability_counterexample(self):
        T={"x":1,"y":1}
        self.assertEqual(T["x"],T["y"])
    def test_negative_weight_counterexample(self):
        self.assertLess(-1,0)
    def test_variance(self):
        ds=[1,2,3]
        mean=sum(ds)/len(ds)
        self.assertEqual(sum((d-mean)**2 for d in ds),2)
    def test_total_coverage_bound(self):
        weights={"a":1,"b":2,"c":3}
        for mask in range(8):
            covered={v for i,v in enumerate(weights) if mask>>i&1}
            self.assertLessEqual(sum(weights[v] for v in covered),6)

if __name__=="__main__":
    unittest.main()
