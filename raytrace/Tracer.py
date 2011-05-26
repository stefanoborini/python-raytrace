class Tracer(object):
    def __init__(self, world):
        self.world = world

    def trace_ray(self, ray):
        foremost = self.world.hit_bare_bones_object(ray)
        if foremost:
            return foremost.color
        else:
            return self.world.background_color



