import math
import random

def create_iter(samples_sets):
    def it():
        while True:
            sample_set = random.choice(samples_sets)
            shuffled_set = sample_set[:]
            random.shuffle(shuffled_set)
            for sample in shuffled_set:
                yield sample

    return it()

class BaseSampler(object):
    def __init__(self, num_samples_per_set, num_sets):
        self._samples_sets = []
        self._num_samples_per_set = num_samples_per_set
        self._num_sets = num_sets
        self._generate_samples()

    def _generate_samples(self, num_samples_per_set, num_sets):
        raise NotImplemented

    def squareiter(self):
        return create_iter(self._samples_sets)
    def diskiter(self):
        self._map_to_unit_disk()
        return create_iter(self._disk_samples_sets)
    def hemisphereiter(self, e):
        self._map_to_hemisphere(e)
        return create_iter(self._hemisphere_samples_sets)

    def num_samples_per_set(self):
        return self._num_samples_per_set
    def num_sets(self):
        return self._num_sets
    def periodicity(self):
        return self._num_samples_per_set * self._num_sets
    def _map_to_unit_disk(self):
        self._disk_samples_sets = []
        for s in self._samples_sets:
            new_set = []
            self._disk_samples_sets.append(new_set)
            for p in s:
                x,y = (2.0 * p[0] - 1.0, 2.0 * p[1] - 1.0)
                if x > -y:
                    if x > y:
                        r = x
                        phi = y/x
                    else:
                        r = y
                        phi = 2.0 - x/y
                else:
                    if x < y:
                        r = - x
                        phi = 4.0 + y/x
                    else:
                        r = -y
                        if y != 0.0:
                            phi = 6.0 - x/y
                        else:
                            phi = 0.0
                phi *= (math.pi / 4.0)

                new_set.append( (r*math.cos(phi), r*math.sin(phi)) )

    def _map_to_hemisphere(self, e):
        self._hemisphere_samples_sets = []
        for s in self._samples_sets:
            new_set = []
            self._hemisphere_samples_sets.append(new_set)
            for p in s:
                cos_phi = math.cos(2.0 * math.pi * p[0])
                sin_phi = math.sin(2.0 * math.pi * p[0])
                cos_theta = math.pow( (1.0 - p[1]), 1.0/(e + 1.0) )
                sin_theta = math.sqrt( 1.0 - cos_theta * cos_theta)
                
                new_set.append( (sin_theta * cos_phi, sin_theta * sin_phi, cos_theta))

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

