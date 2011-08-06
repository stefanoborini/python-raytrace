import itertools
from . import samplers
import math
import sys
from PIL import Image
import pygame
from . import mathop

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
    def __init__(self, **kwargs):
        self._eye_point = kwargs["eye_point"]
        self._look_at = kwargs["look_at"]
        self._up_vector = kwargs["up_vector"]
        self._viewplane_distance = kwargs["viewplane_distance"]
        self.zoom = 1.0
        self._compute_uvw()
    def _compute_uvw(self):
        view_direction = mathop.vecsum(self._look_at, mathop.vecmul(-1, self._eye_point))

        self._w = mathop.vecmul(-1.0, mathop.normalized(view_direction))
        self._u = mathop.normalized(mathop.cross(self._up_vector, self._w))
        self._v = mathop.cross(self._w,self._u)
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
                    direction = mathop.normalized( mathop.vecsum(
                                                mathop.vecsum(
                                                    mathop.vecmul(plane_point[0],self._u),
                                                    mathop.vecmul(plane_point[1],self._v)
                                                ),
                                            mathop.vecmul(-self._viewplane_distance, self._w)
                                        )
                                    )
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

class LensCamera(BaseCamera):
    def __init__(self,**kwargs):
        self._lens_radius = kwargs.pop("lens_radius")
        self._focal_plane_distance = kwargs.pop("focal_plane_distance")
        print kwargs
        super(LensCamera, self).__init__(**kwargs)
        self._sampler = samplers.Jittered(16,4)
    def ray_direction(self, pixel_point, lens_point):
        p = ( pixel_point[0] * self._focal_plane_distance / self._viewplane_distance,
              pixel_point[1] * self._focal_plane_distance / self._viewplane_distance)
        
        return mathop.normalized( mathop.vecsum( 
                                    mathop.vecmul(p[0] - lens_point[0], self._u),
                                    mathop.vecsum(
                                        mathop.vecmul(p[1] - lens_point[1], self._v),
                                        mathop.vecmul(-self._focal_plane_distance, self._w)
                                                )
                                    )
                                )
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
                for subsample, lens_sample in itertools.izip( 
                                itertools.islice(world.sampler.squareiter(),world.sampler.num_samples_per_set()),
                                itertools.islice(self._sampler.diskiter(),world.sampler.num_samples_per_set())
                                ):
                    plane_point = ( world.viewplane.pixel_size*(pixel[0] - world.viewplane.resolution[0] / 2 + subsample[0]),
                                    world.viewplane.pixel_size*(pixel[1] - world.viewplane.resolution[1] / 2 + subsample[1])
                                  )
                    lens_point = ( self._lens_radius * lens_sample[0], self._lens_radius * lens_sample[1])

                    origin = mathop.vecsum(self._eye_point, mathop.vecsum(mathop.vecmul(lens_point[0],self._u), mathop.vecmul(lens_point[1], self._v)))
                    direction = self.ray_direction(plane_point, lens_point)
                    ray = Ray(origin = origin, direction = direction )

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

