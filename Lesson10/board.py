import pygame, sys
from pygame.locals import *

pygame.init()

windowSurface = pygame.display.set_mode((300,300),0,32)
pygame.display.set_caption("TIC TAC TOC")

# Set up the colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

windowSurface.fill(WHITE)

cross = pygame.Surface((100,100))
crossRect = cross.get_rect()
cross.fill(WHITE)

pygame.draw.line(cross, RED,(20,20),(80,80),3) 
pygame.draw.line(cross, RED,(80,20),(20,80),3) 
 
circle = pygame.Surface((100,100))
circle.fill(WHITE)
circleRect = circle.get_rect()
pygame.draw.circle(circle, GREEN,(50,50),30)  


pygame.draw.line(windowSurface, BLUE, (100, 0), (100, 300), 3)
pygame.draw.line(windowSurface, BLUE, (200, 0), (200, 300), 3)
pygame.draw.line(windowSurface, BLUE, (0, 100), (300, 100), 3)
pygame.draw.line(windowSurface, BLUE, (0, 200), (300, 200), 3)

crossRect.center = (50,50)
windowSurface.blit(cross,crossRect)
crossRect.center = (150,150)
windowSurface.blit(cross,crossRect)

circleRect.center = (250,50)
windowSurface.blit(circle,circleRect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()