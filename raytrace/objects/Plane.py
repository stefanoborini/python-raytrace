import numpy
from .. import ShadeRecord
class Plane(object):
    def __init__(self, point, normal, color):
        self.point = numpy.array(point)
        self.normal = numpy.array(normal)
        self.color = color
    def hit(self, ray):
        t = numpy.dot((self.point - ray.origin), self.normal) / numpy.dot(ray.direction, self.normal)
        if (t > 1.0e-7):
            return ShadeRecord.ShadeRecord(normal=self.normal, hit_point=(ray.origin + t * ray.direction), parameter=t, color=self.color)

        return None
