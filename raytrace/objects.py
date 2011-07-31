from __future__ import absolute_import
import math
import sys
from . import math as rtmath

class Sphere(object):
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color

    def hit(self, ray):
        temp = (ray.origin[0] - self.center[0],
                ray.origin[1] - self.center[1],
                ray.origin[2] - self.center[2])

        a = rtmath.dot(ray.direction, ray.direction)
        b = 2.0 * rtmath.dot(temp, ray.direction)
        c = rtmath.dot(temp, temp) - self.radius * self.radius
        disc = b * b - 4.0 * a * c
        
        if (disc < 0.0):
            return None
        else:
            e = math.sqrt(disc)
            denom = 2.0 * a
            t = (-b - e) / denom
            if (t > 1.0e-7):
                normal = ( (temp[0] + t * ray.direction[0]) / self.radius,
                           (temp[1] + t * ray.direction[1]) / self.radius,
                           (temp[2] + t * ray.direction[2]) / self.radius,
                           )
                hit_point = ( ray.origin[0] + t * ray.direction[0],
                                ray.origin[1] + t * ray.direction[1],
                                ray.origin[2] + t * ray.direction[2]
                                )

                return ShadeRecord(normal=normal, hit_point=hit_point, parameter=t, color=self.color)

            t = (-b + e) / denom

            if (t > 1.0e-7):
                normal = ( (temp[0] + t * ray.direction[0]) / self.radius,
                           (temp[1] + t * ray.direction[1]) / self.radius,
                           (temp[2] + t * ray.direction[2]) / self.radius,
                           )
                hit_point = ( ray.origin[0] + t * ray.direction[0],
                                ray.origin[1] + t * ray.direction[1],
                                ray.origin[2] + t * ray.direction[2]
                                )
                return ShadeRecord.ShadeRecord(normal=normal, hit_point=hit_point, parameter=t, color=self.color)

        return None    


#from .. import ShadeRecord
#from .. import math
#class Plane(object):
#    def __init__(self, point, normal, color):
#        self.point = point
#        self.normal = normal
#        self.color = color
#    def hit(self, ray):
#        t = math.dot((self.point - ray.origin), self.normal) / math.dot(ray.direction, self.normal)
#        if (t > 1.0e-7):
#            return ShadeRecord.ShadeRecord(normal=self.normal, hit_point=(ray.origin + t * ray.direction), parameter=t, color=self.color)
#
#        return None

class ShadeRecord(object):
    def __init__(self, hit_point, normal, parameter, color):
        self.hit_point = hit_point
        self.normal = normal
        self.color = color
        self.parameter = parameter
