import numpy

class Ray(object):
    def __init__(self, origin, direction):
        self.origin = numpy.array(origin)
        self.direction = numpy.array(direction)

