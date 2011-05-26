import math
import numpy
import sys
from .. import ShadeRecord

class Sphere(object):
    def __init__(self, center, radius, color):
        self.center = numpy.array(center)
        self.radius = numpy.array(radius)
        self.color = color

    def hit(self, ray):
        temp = ray.origin - self.center
        a = numpy.dot(ray.direction, ray.direction)
        b = 2.0 * numpy.dot(temp, ray.direction)
        c = numpy.dot(temp, temp) - self.radius * self.radius
        disc = b * b - 4.0 * a * c
        
        if (disc < 0.0):
            return None
        else:
            e = math.sqrt(disc)
            denom = 2.0 * a
            t = (-b - e) / denom
            if (t > 1.0e-7):
                normal = (temp + t * ray.direction) / self.radius
                hit_point = ray.origin + t * ray.direction
                return ShadeRecord.ShadeRecord(normal=normal, hit_point=hit_point, parameter=t, color=self.color)

            t = (-b + e) / denom

            if (t > 1.0e-7):
                normal = (temp + t * ray.direction) / self.radius
                hit_point = ray.origin + t * ray.direction
                return ShadeRecord.ShadeRecord(normal=normal, hit_point=hit_point, parameter=t, color=self.color)

        return None    

