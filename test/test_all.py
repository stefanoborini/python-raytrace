import unittest
import itertools
import raytrace
from raytrace import samplers

class Test(unittest.TestCase):

    def test_foo(self):
        self.assertEqual(0,0)

class TestSamplers(unittest.TestCase):
    def test_jittered(self):
        s = samplers.Jittered(9, 2)
        self.assertEqual(s.num_samples_per_set(), 9)
        self.assertEqual(s.num_sets(), 2)
        self.assertEqual(s.periodicity(), 18)

        self.assertRaises(Exception, samplers.Jittered, 10, 2)
    def test_regular(self):
        s = samplers.Regular(9, 2)
        self.assertEqual(s.num_samples_per_set(), 9)
        self.assertEqual(s.num_sets(), 2)
        self.assertEqual(s.periodicity(), 18)

        self.assertRaises(Exception, samplers.Regular, 10, 2)

    def test_jittered_behavior(self):
        s = samplers.Jittered(100,50)
        it = iter(s)

        for i in xrange(500):
            bins = {}
            for i in xrange(10):
                for j in xrange(10):
                    bins[(i,j)] = 0
            for j in xrange(100):
                p = tuple(map( lambda q: int(q*10), it.next()))
                bins[p] += 1
            self.assertTrue(all(map(lambda q: q == 1, bins.values())))

if __name__ == "__main__":
    unittest.main()

