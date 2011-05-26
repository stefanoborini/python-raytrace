from . import ViewPlane
from . import Tracer
from PIL import Image
import pygame
import math
import numpy
import sys


epsilon = 1.0e-7

class World(object):
    def __init__(self):
        self.viewplane = ViewPlane.ViewPlane(resolution=(500,200), pixel_size=1.0)
        self.background_color = (0.0,0.0,0.0)
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
            for ray, pixel in row:
                print pixel
                imagePxPos = (pixel[0], self.viewplane.resolution[1]-pixel[1]-1)

                color = tracer.trace_ray(ray)
                im.putpixel(imagePxPos, (int(color[0]*255), int(color[1]*255), int(color[2]*255)))
                pxarray[imagePxPos[0]][imagePxPos[1]] = (int(color[0]*255), int(color[1]*255), int(color[2]*255))

            pygame.display.flip() 

        im.save("render.png", "PNG")
        while True: 
           for event in pygame.event.get(): 
              if event.type == pygame.QUIT: 
                  sys.exit(0) 
              else: 
                  print event 

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
   

                
