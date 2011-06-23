import unittest
import itertools
import raytrace
from raytrace import samplers

class Test(unittest.TestCase):

    def test_foo(self):
        self.assertEqual(0,0)

class TestSamplers(unittest.TestCase):
    def test_jittered(self):
        s = samplers.Jittered(10, 2)
        self.assertEqual(s.num_samples_per_set(), 10)
        self.assertEqual(s.num_sets(), 2)
        self.assertEqual(s.periodicity(), 20)
    def test_regular(self):
        s = samplers.Regular(10, 2)
        self.assertEqual(s.num_samples_per_set(), 10)
        self.assertEqual(s.num_sets(), 2)
        self.assertEqual(s.periodicity(), 20)
        a = list(enumerate(itertools.islice(iter(s), 0, 20)))
        print a


if __name__ == "__main__":
    unittest.main()

