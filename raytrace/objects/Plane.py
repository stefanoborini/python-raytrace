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
