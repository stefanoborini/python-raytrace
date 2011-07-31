from . import ViewPlane
from . import cameras
from . import samplers


epsilon = 1.0e-7

class World(object):
    def __init__(self):
        self.viewplane = ViewPlane.ViewPlane(resolution=(200,200), pixel_size=1.0)
        self.background_color = (0.0,0.0,0.0)
        self.sampler = samplers.Regular(9,10)
        self.camera = cameras.PinholeCamera(eye_point = (300,400,500), look_at = (0,0,-50), up_vector=(0,1,0), viewplane_distance=400)
        self.objects=[]

    def set_bgcolor(self,bgcolor):
        self.background_color = bgcolor

    def add_object(self, o):
        self.objects.append(o)

    def hit_bare_bones_object(self,ray):
        def f(o):
            shadeRec = o.hit(ray)
 
            if shadeRec:
                return (shadeRec.parameter, o)
            else:
                return None
       
        try:
            foremost=sorted(filter(lambda x: x is not None, map(f, self.objects)), key=lambda x: x[0])[0][1]
        except IndexError:
            return None

        return foremost

    def set_sampler(self, sampler):
        self.sampler = sampler

    def render(self):
        self.camera.render(self)
