import numpy
from . import Ray

class ViewPlane(object):
    def __init__(self, resolution, pixel_size):
        self.resolution = resolution
        self.pixel_size = pixel_size

    def iter_row(self, row):
        for column in xrange(self.resolution[0]):
            yield (column,row)

    def __iter__(self):
        for row in xrange(self.resolution[1]):
            yield self.iter_row(row) 

