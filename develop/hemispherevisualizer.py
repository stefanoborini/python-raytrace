import math
import time
import pygame
import sys
import random
import itertools
from raytrace import samplers
pygame.init() 

class HemisphereVisualizer:
    def __init__(self):
        self.window = pygame.display.set_mode((300,450))
        self.pxarray = pygame.PixelArray(self.window)
        self.plot()
    def plot(self):
        self.window.fill((255,255,255))
        pygame.draw.circle(self.window, (200,200,200), (150,150), 150, 0)
        pygame.draw.circle(self.window, (200,200,200), (150,450), 150, 0 )
        pygame.display.flip() 

    def add_point(self, p, color):
        x=p[0]
        y=p[1]
        z=p[2]
        pos1 = (int(x*150+150), int(y*150+150))
        pygame.draw.circle(self.window, color, pos1, 2, 0)
        pos2 = (int(x*150+150), int(450-(z*150)))
        pygame.draw.circle(self.window, color, pos2, 2, 0)
    def clear(self):
        self.plot()
    def refresh(self):
        pygame.display.flip() 
v=HemisphereVisualizer()
j=samplers.Jittered(256,5)
while True:
    v.clear()
    for point in itertools.islice(j.hemisphereiter(10),256):
        v.add_point(point, (0,0,0))
    v.refresh()
    time.sleep(1)

while True: 
   for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
          sys.exit(0) 
      else: 
           print event 

