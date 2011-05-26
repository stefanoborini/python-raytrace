import numpy
from . import Ray

class ViewPlane(object):
    def __init__(self, resolution, pixel_size):
        self.resolution = resolution
        self.pixel_size = pixel_size


    def iter_row(self, row):
        for column in xrange(self.resolution[0]):
            origin = numpy.zeros(3)
            origin[0] = self.pixel_size*(column - self.resolution[0] / 2 + 0.5)
            origin[1] = self.pixel_size*(row - self.resolution[1] / 2 + 0.5)
            origin[2] = 100.0
            yield ( Ray.Ray(origin = origin, direction = (0.0,0.0,-1.0)), (column,row))

    def __iter__(self):
        for row in xrange(self.resolution[1]):
            yield self.iter_row(row) 

