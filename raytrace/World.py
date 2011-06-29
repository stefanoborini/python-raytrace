from . import ViewPlane
from . import Ray
from . import Tracer
from . import samplers
from PIL import Image
import pygame
import itertools
import math
import numpy
import sys


epsilon = 1.0e-7

class World(object):
    def __init__(self):
        self.viewplane = ViewPlane.ViewPlane(resolution=(200,200), pixel_size=1.0)
        self.background_color = (0.0,0.0,0.0)
        self.sampler = samplers.Regular(9,10)
        self.objects=[]

    def set_bgcolor(self,bgcolor):
        self.background_color = bgcolor

    def render(self):
        pygame.init() 
        window = pygame.display.set_mode(self.viewplane.resolution) 
        pxarray = pygame.PixelArray(window)
        im = Image.new("RGB", self.viewplane.resolution)
        tracer = Tracer.Tracer(self)
        for row in self.viewplane:
            for pixel in row:
                print pixel
                imagePxPos = (pixel[0], self.viewplane.resolution[1]-pixel[1]-1)
                color = numpy.array([0.0, 0.0, 0.0])
                for subsample in itertools.islice(self.sampler,self.sampler.num_samples_per_set()):
                    origin = numpy.zeros(3)
                    origin[0] = self.viewplane.pixel_size*(pixel[0] - self.viewplane.resolution[0] / 2 + subsample[0])
                    origin[1] = self.viewplane.pixel_size*(pixel[1] - self.viewplane.resolution[1] / 2 + subsample[1])
                    origin[2] = 100.0
                    ray = Ray.Ray(origin = origin, direction = (0.0,0.0,-1.0))

                    color += numpy.array(tracer.trace_ray(ray))
                color /= self.sampler.num_samples_per_set()

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

