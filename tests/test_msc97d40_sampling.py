"""MSC 97D40 III-F: exact exhaustive verification of sampling and randomization."""
import itertools
import math
import unittest

def finite_variance(x):
    mean = sum(x) / len(x)
    return sum((v - mean) ** 2 for v in x) / (len(x) - 1)

def sample_mean(x, ids):
    return sum(x[i] for i in ids) / len(ids)

def enumerate_samples(n, k):
    return list(itertools.combinations(range(n), k))

class FinitePopulationTests(unittest.TestCase):
    def test_inclusion_probabilities(self):
        for N in range(2, 8):
            for n in range(1, N + 1):
                samples = enumerate_samples(N, n)
                self.assertAlmostEqual(sum(0 in s for s in samples)/len(samples), n/N)
                self.assertAlmostEqual(sum(0 in s and 1 in s for s in samples)/len(samples),
                                       n*(n-1)/(N*(N-1)))
    def test_unbiased_mean_and_variance_exhaustive(self):
        for N in range(2, 6):
            for population in itertools.product((-1, 0, 2), repeat=N):
                mu = sum(population)/N
                S2 = finite_variance(population)
                for n in range(1, N+1):
                    means = [sample_mean(population, s) for s in enumerate_samples(N,n)]
                    self.assertAlmostEqual(sum(means)/len(means),mu)
                    empirical_var = sum((m-mu)**2 for m in means)/len(means)
                    self.assertAlmostEqual(empirical_var,(1-n/N)*S2/n)
    def test_ht_unbiased(self):
        for N in range(2, 8):
            for n in range(1, N+1):
                y = [i*i-3 for i in range(N)]
                pi = n/N
                estimates = [sum(y[i]/pi for i in s) for s in enumerate_samples(N,n)]
                self.assertAlmostEqual(sum(estimates)/len(estimates),sum(y))
    def test_ht_variance(self):
        for N in range(2, 7):
            for n in range(1,N+1):
                y = [i-2 for i in range(N)]
                pi = n/N
                estimates = [sum(y[i]/pi for i in s) for s in enumerate_samples(N,n)]
                empirical = sum((v-sum(y))**2 for v in estimates)/len(estimates)
                formula = 0
                for i in range(N):
                    for j in range(N):
                        pij = pi if i == j else n*(n-1)/(N*(N-1))
                        formula += (pij-pi*pi)/(pi*pi)*y[i]*y[j]
                self.assertAlmostEqual(empirical,formula)
    def test_neyman_randomization_exhaustive(self):
        for N in (3,4,5):
            for y0 in itertools.product((0,2),repeat=N):
                for y1 in itertools.product((0,1),repeat=N):
                    tau = sum(a-b for a,b in zip(y1,y0))/N
                    S1 = finite_variance(y1)
                    S0 = finite_variance(y0)
                    St = finite_variance([a-b for a,b in zip(y1,y0)])
                    for n1 in range(1,N):
                        estimates = []
                        for treated in enumerate_samples(N,n1):
                            group=set(treated)
                            mean1 = sum(y1[i] for i in group)/n1
                            mean0 = sum(y0[i] for i in range(N) if i not in group)/(N-n1)
                            estimates.append(mean1-mean0)
                        actual_mean=sum(estimates)/len(estimates)
                        actual_var=sum((e-tau)**2 for e in estimates)/len(estimates)
                        neyman=S1/n1+S0/(N-n1)-St/N
                        self.assertAlmostEqual(actual_mean,tau)
                        self.assertAlmostEqual(actual_var,neyman)
                        self.assertLessEqual(actual_var,S1/n1+S0/(N-n1)+1e-10)
    def test_textbook_examples(self):
        y=(1,3,5)
        means=[sample_mean(y,s) for s in enumerate_samples(3,2)]
        self.assertEqual(sorted(means),[2,3,4])
        self.assertAlmostEqual(sum((v-3)**2 for v in means)/3,2/3)
        y0=(0,0,0,0); y1=(0,0,2,2)
        tau=sum(a-b for a,b in zip(y1,y0))/4
        estimates=[sample_mean(y1,s) for s in enumerate_samples(4,2)]
        self.assertEqual(tau,1)
        self.assertAlmostEqual(sum((e-tau)**2 for e in estimates)/6,1/3)

if __name__ == "__main__":
    unittest.main()
