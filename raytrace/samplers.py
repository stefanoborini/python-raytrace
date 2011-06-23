import math
import random

class BaseSampler(object):
    def __init__(self, num_samples_per_set, num_sets):
        self._samples_sets = []
        self._num_samples_per_set = num_samples_per_set
        self._num_sets = num_sets
        self._generate_samples()

    def _generate_samples(self, num_samples_per_set, num_sets):
        raise NotImplemented

    def __iter__(self):
        
        while True:
            sample_set = random.choice(self._samples_sets)
            shuffled_set = sample_set[:]
            random.shuffle(shuffled_set)
            for sample in shuffled_set:
                yield sample

    def num_samples_per_set(self):
        return self._num_samples_per_set
    def num_sets(self):
        return self._num_sets
    def periodicity(self):
        return self._num_samples_per_set * self._num_sets

class Jittered(BaseSampler):
    def _generate_samples(self):
        n = int(math.sqrt(self.num_samples_per_set()))
  
        if n*n != self.num_samples_per_set():
            raise Exception("The Jittered Sampler requires the number of samples to be a perfect square")

        for p in xrange(self.num_sets()):
            new_set = []
            self._samples_sets.append(new_set) 
            for i in xrange(n):
                for j in xrange(n):
                    new_set.append( ((i + random.random())/float(n), (j + random.random())/float(n)) ) 

class Regular(BaseSampler):
    def _generate_samples(self):
        n = int(math.sqrt(self.num_samples_per_set()))

        if n*n != self.num_samples_per_set():
            raise Exception("The Regular Sampler requires the number of samples to be a perfect square")

        for p in xrange(self.num_sets()):
            new_set = []
            self._samples_sets.append(new_set)
            for i in xrange(n):
                for j in xrange(n):
                    new_set.append( ( (i+0.5)/float(n), 
                                      (j+0.5)/float(n)
                                    ) 
                                  ) 

class Random(BaseSampler):
    def _generate_samples(self):
        n = int(math.sqrt(self.num_samples_per_set()))

        if n*n != self.num_samples_per_set():
            raise Exception("The Random Sampler requires the number of samples to be a perfect square")

        for p in xrange(self.num_sets()):
            new_set = []
            self._samples_sets.append(new_set)
            for i in xrange(n):
                for j in xrange(n):
                    new_set.append( (random.random(), random.random()) ) 

