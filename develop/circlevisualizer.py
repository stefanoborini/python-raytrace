import time
import pygame
import sys
import random
import itertools
from raytrace import samplers
pygame.init() 

class CircleVisualizer:
    def __init__(self):
        self.window = pygame.display.set_mode((500,500))
        self.pxarray = pygame.PixelArray(self.window)
        #self.pxarray[imagePxPos[0]][imagePxPos[1]] = (int(color[0]*255), int(color[1]*255), int(color[2]*255))
        self.plot_circle()
    def plot_circle(self):
        self.window.fill((255,255,255))
        pygame.draw.circle(self.window, (200,200,200), (250,250), 250, 0)
        pygame.display.flip() 
    def add_point(self, p, color):
        x=p[0]
        y=p[1]
        pos = (int(x*250+250), int(y*250+250))
        pygame.draw.circle(self.window, color, pos, 2, 0)
    def clear(self):
        self.plot_circle()
    def refresh(self):
        pygame.display.flip() 
v=CircleVisualizer()
j=samplers.Jittered(256,5)
v.clear()
for point in itertools.islice(j.diskiter(),256):
    v.add_point(point, (0,0,0))
v.refresh()

while True: 
   for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
          sys.exit(0) 
      else: 
           print event 

