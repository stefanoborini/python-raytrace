import time
import pygame
import sys
import random
import itertools
from raytrace import samplers
pygame.init() 

class PlaneVisualizer:
    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.window = pygame.display.set_mode((510,510))
        self.pxarray = pygame.PixelArray(self.window)
        #self.pxarray[imagePxPos[0]][imagePxPos[1]] = (int(color[0]*255), int(color[1]*255), int(color[2]*255))
        self.plot_grid()
    def plot_grid(self):
        pygame.draw.rect(self.window, (200,200,200), pygame.Rect(0,0,10,510), 0)
        pygame.draw.rect(self.window, (200,200,200), pygame.Rect(0,0,510,10), 0)
        pygame.draw.rect(self.window, (255,255,255), pygame.Rect(10,10,510,510), 0)
        for r in xrange(self.rows):
            pygame.draw.rect(self.window, (200+35*(r%2),200+35*(r%2),200+35*(r%2)), pygame.Rect(0, 10+r*(500/self.rows), 10, (r+1)*(500/self.rows)), 0)
            for c in xrange(self.columns):
                pygame.draw.rect(self.window, (200+35*(c%2),200+35*(c%2),200+35*(c%2)), pygame.Rect( 10+c*(500/self.columns), 0,(c+1)*(500/self.rows), 10), 0)

                pygame.draw.rect(self.window, (255,255,200+55*((c+r)%2)), pygame.Rect( 
                                                                                        10+c*(500/self.columns), 
                                                                                        10+r*(500/self.rows),
                                                                                        (c+1)*(500/self.rows),
                                                                                        (r+1)*(500/self.rows)), 0)

        pygame.display.flip() 
    def add_point(self, p, color):
        x=p[0]
        y=p[1]
        pos = (10+int(x*500), 10+int(y*500))
        pygame.draw.circle(self.window, color, pos, 2, 0)
        pygame.draw.circle(self.window, color, (pos[0],5), 2, 0)
        pygame.draw.circle(self.window, color, (5,pos[1]), 2, 0)
    def clear(self):
        self.plot_grid()
    def refresh(self):
        pygame.display.flip() 
v=PlaneVisualizer(8,8)
j=samplers.Jittered(64,5)
while True:
    v.clear()
    for point in itertools.islice(j.squareiter(),64):
        v.add_point(point, (0,0,0))
    v.refresh()
    time.sleep(1)

while True: 
   for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
          sys.exit(0) 
      else: 
           print event 

