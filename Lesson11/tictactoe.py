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

cross = pygame.Surface((90,90))
crossRect = cross.get_rect()
cross.fill(WHITE)

pygame.draw.line(cross, RED,(20,20),(70,70),3) 
pygame.draw.line(cross, RED,(70,20),(20,70),3) 
 
circle = pygame.Surface((90,90))
circle.fill(WHITE)
circleRect = circle.get_rect()
pygame.draw.circle(circle, GREEN,(45,45),30,3)  



pygame.draw.line(windowSurface, BLUE, (100, 0), (100, 300), 3)
pygame.draw.line(windowSurface, BLUE, (200, 0), (200, 300), 3)
pygame.draw.line(windowSurface, BLUE, (0, 100), (300, 100), 3)
pygame.draw.line(windowSurface, BLUE, (0, 200), (300, 200), 3)

field=["X"," ","0","X"," ","0"," "," ","X"]
for i in range(9):
    if field[i]=="X":
         crossRect.center = ((i%3)*100+50,int(i/3)*100+50)
         windowSurface.blit(cross,crossRect)
    if field[i]=="0":
         circleRect.center = ((i%3)*100+50,int(i/3)*100+50)
         windowSurface.blit(circle,circleRect)


pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            print(event.pos)
            print(event.button)
