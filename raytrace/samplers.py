import math
import random

class Sampler(object):
    def __init__(self, num_samples_per_set, num_sets):
        self._samples_sets = []
        self._num_samples_per_set = int(math.pow(int(math.sqrt(num_samples_per_set)), 2))
        self._num_sets = num_sets
        self._generate_samples()

    def _generate_samples(self, num_samples_per_set, num_sets):
        raise NotImplemented

    def __iter__(self):
        
        while True:
            print self._samples_sets
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

class Jittered(Sampler):
    def _generate_samples(self):
        n = int(math.sqrt(self.num_samples_per_set()))

        for p in xrange(self.num_sets()):
            new_set = []
            self._samples_sets.append(new_set) 
            for i in xrange(n):
                for j in xrange(n):
                    new_set.append( ((i + random.random())/float(n), (j + random.random())/float(n)) ) 

        
class Regular(Sampler):
    def _generate_samples(self):
        n = int(math.sqrt(self.num_samples_per_set()))

        for p in xrange(self.num_sets()):
            new_set = []
            self._samples_sets.append(new_set)
            for i in xrange(n):
                for j in xrange(n):
                    new_set.append( ( (i+0.5)/float(n), 
                                      (j+0.5)/float(n)
                                    ) 
                                  ) 

class Random(Sampler):
    def _generate_samples(self):
        n = int(math.sqrt(self.num_samples_per_set()))

        for p in xrange(self.num_sets()):
            new_set = []
            self._samples_sets.append(new_set)
            for i in xrange(n):
                for j in xrange(n):
                    new_set.append( (random.random(), random.random()) ) 

class NRooks(Sampler):
    def _generate_samples(self):
        num_samples = self.num_samples_per_set()
        for p in xrange(self.num_sets()):
            new_set = []
            self._samples_sets.append(new_set)
            for i in xrange(self.num_samples_per_set()):
                new_set.append( ( (i+random.random())/float(num_samples), (i+random.random())/float(num_samples)) ) 

        for set_index in xrange(len(self._samples_sets)):
            sset = self._samples_sets[set_index]
            x_coords = [v[0] for v in sset]
            random.shuffle(x_coords)
            y_coords = [v[1] for v in sset]
            random.shuffle(y_coords)
            self._samples_sets[set_index] = zip(x_coords, y_coords)


        
