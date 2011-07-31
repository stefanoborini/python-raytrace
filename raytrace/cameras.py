import itertools
import math
import sys
import numpy
from PIL import Image
import pygame

class Ray(object):
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

class Tracer(object):
    def __init__(self, world):
        self.world = world

    def trace_ray(self, ray):
        foremost = self.world.hit_bare_bones_object(ray)
        if foremost:
            return foremost.color
        else:
            return self.world.background_color

    
class BaseCamera(object):
    def __init__(self, eye_point, look_at, up_vector, viewplane_distance):
        self._eye_point = eye_point
        self._look_at = look_at
        self._up_vector = up_vector
        self._viewplane_distance = viewplane_distance
        self.zoom = 1.0
        self._compute_uvw()
    def _compute_uvw(self):
        view_direction = numpy.array(( self._look_at[0] - self._eye_point[0], 
                           self._look_at[1] - self._eye_point[1],
                           self._look_at[2] - self._eye_point[2]))

        w = -view_direction / numpy.linalg.norm(view_direction)
        u = numpy.cross(self._up_vector, w)
        u = u/numpy.linalg.norm(u)
        v = numpy.cross(w,u)
        self._w = tuple(w)
        self._u = tuple(u)
        self._v = tuple(v)
    def render(self, world):
        raise NotImplementedError

class PinholeCamera(BaseCamera):
    def render(self,world):
        pygame.init() 
        window = pygame.display.set_mode(world.viewplane.resolution) 
        pxarray = pygame.PixelArray(window)
        im = Image.new("RGB", world.viewplane.resolution)
        tracer = Tracer(world)
        
        num_samples = world.sampler.num_samples_per_set()
        pixel_size = world.viewplane.pixel_size / self.zoom

        for row in world.viewplane:
            pxarray[:,world.viewplane.resolution[1]-row.current_row()-1] = (255,255,255)
            pygame.display.flip() 
            
            for pixel in row:
                imagePxPos = (pixel[0], world.viewplane.resolution[1]-pixel[1]-1)
                color = (0.0, 0.0, 0.0)
                for subsample in itertools.islice(world.sampler.squareiter(),world.sampler.num_samples_per_set()):
                    plane_point = ( world.viewplane.pixel_size*(pixel[0] - world.viewplane.resolution[0] / 2 + subsample[0]),
                                    world.viewplane.pixel_size*(pixel[1] - world.viewplane.resolution[1] / 2 + subsample[1])
                                  )
                    direction = numpy.array( (plane_point[0] * numpy.array(self._u) 
                                            + plane_point[1] * numpy.array(self._v) 
                                            - self._viewplane_distance * numpy.array(self._w)) )
                    direction = tuple( direction / numpy.linalg.norm(direction))
                    ray = Ray(origin = self._eye_point, direction = direction )

                    c = tracer.trace_ray(ray)
                    color = (   color[0] + c[0],
                                color[1] + c[1],
                                color[2] + c[2])

                color = ( color[0]/num_samples,
                            color[1]/num_samples,
                            color[2]/num_samples)

                im.putpixel(imagePxPos, (int(color[0]*255), int(color[1]*255), int(color[2]*255)))
                pxarray[imagePxPos[0]][imagePxPos[1]] = (int(color[0]*255), int(color[1]*255), int(color[2]*255))


        pygame.display.flip() 
        im.save("render.png", "PNG")
        #while True: 
        #   for event in pygame.event.get(): 
        #      if event.type == pygame.QUIT: 
        #          sys.exit(0) 
        #      else: 
        #          print event 
