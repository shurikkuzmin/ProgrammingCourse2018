import pygame, sys
from pygame.locals import *
import random

pygame.init()

windowSurface = pygame.display.set_mode((300,300),0,32)
pygame.display.set_caption("TIC TAC TOE")

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
pygame.display.update()


field=[" "," "," "," "," "," "," "," "," "]
def drawField(field): 
    for i in range(9):
        if field[i]=="X":
             crossRect.center = ((i%3)*100+50,int(i/3)*100+50)
             windowSurface.blit(cross,crossRect)
        if field[i]=="O":
             circleRect.center = ((i%3)*100+50,int(i/3)*100+50)
             windowSurface.blit(circle,circleRect)
    pygame.display.update()

def checkWin(field,token):
    field[0]==token
    if field[0]==token and field[1]==token and field[2]==token:
        return True    
    if field[3]==token and field[4]==token and field[5]==token:  
        return True
    if field[6]==token and field[7]==token and field[8]==token:
        return True
    if field[0]==token and field[3]==token and field[6]==token:
        return True
    if field[1]==token and field[4]==token and field[7]==token:
        return True
    if field[2]==token and field[5]==token and field[8]==token:
        return True
    if field[0]==token and field[4]==token and field[8]==token:
        return True
    if field[2]==token and field[4]==token and field[6]==token:
        return True
    return False  

def playComputer(field):
    free=[ ]
    for i in range(9):
        if field[i]==" ":
            free.append(i)
    for i in free:
        field2=field.copy()
        field2[i]="O"
        if checkWin(field2,"O")==True:
            return i
    for i in free:
        field2=field.copy()
        field2[i]="X"
        if checkWin(field2,"X")==True:
            return i
    
    if len(free) != 0:
        randomIndex= random.randint(0,len(free)-1)
        return free[randomIndex] 
    else:
        return -1     

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            x=event.pos[0]
            y=event.pos[1]
            col=int(x/100)
            row=int(y/100)
            i = row*3+col 
            if field[i]==" ":
                field[i]="X"

                if checkWin(field,"X") == True:
                    print("X  win!")
                    drawField(field)
                    pygame.quit()
                    sys.exit()

                i2 = playComputer(field)
                if i2 != -1:
                    field[playComputer(field)]="O"
                    if checkWin(field,"O") == True:
                        print("O win!")
                        drawField(field)
                        pygame.quit()
                        sys.exit()

                drawField(field)
            



