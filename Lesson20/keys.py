import pygame, sys, random
from pygame.locals import *
import time 

# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window.
WINDOWWIDTH = 800
WINDOWHEIGHT = 200
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),0, 32)
pygame.display.set_caption('Dino')

# Set up the colors.
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

bigSprite  = pygame.image.load('sprite.png')
bigSpriteRect = bigSprite.get_rect()

rect = pygame.Rect((1336,0,88,96))
dinoStanding = bigSprite.subsurface(rect)
dinoStandingRect=dinoStanding.get_rect()

rect= pygame.Rect((2,104,2400,26))
terrain=bigSprite.subsurface(rect)
terrainRect=terrain.get_rect()
terrainRect.bottom=WINDOWHEIGHT-1

rect=pygame.Rect((166,2,92,27))
cloud=bigSprite.subsurface(rect)
cloudRect=cloud.get_rect()
cloudRect.top=20
cloudRect.left=100

#rect=pygame.Rect(())
#cactus=bigSprite.subsurface(rect)
#cactusRect=cactus.get_rect()

dinoRunning=[0,0,0,0]
for i in range(4):
    rect=pygame.Rect((1516+i*88,0,88,96))
    dinoRunning[i]=bigSprite.subsurface(rect)

SPEED = 1
SPEED2= 10
SPEED3= 20

windowSurface.fill(WHITE)

move=True
jump=False
dino=dinoStanding
dinoRect=dinoStandingRect
dinoRect.bottom=WINDOWHEIGHT-5
counter=0
diff=-1
isUP=False
# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_SPACE or event.key == K_UP: 
                jump = True
                move=False
                isUP=True
                #counter=0 
        if event.type==KEYUP:
            if event.key == K_SPACE or event.key == K_UP:
                isUP=False


    if move==True:
        dino=dinoRunning[int(counter/SPEED2)%4]
        counter=(counter+1)
    if jump==True:
        dino=dinoStanding
        dinoRect.top=dinoRect.top+diff
        if dinoRect.top<30:
            diff=-diff
        if dinoRect.bottom==WINDOWHEIGHT-5:
            diff=-diff
            if not isUP:
                jump=False
                move=True



    

    windowSurface.fill(WHITE)
    windowSurface.blit(dino,dinoRect)
    windowSurface.blit(terrain,terrainRect)
    windowSurface.blit(terrain,(terrainRect.right,terrainRect.top))
    terrainRect=terrainRect.move((-1,0))
    if terrainRect.right<0:
        terrainRect.left=0
    windowSurface.blit(cloud,cloudRect)
    windowSurface.blit(cloud,(cloudRect.left+WINDOWWIDTH,cloudRect.top)) 
    cloudRect=cloudRect.move((-1,0))
    if cloudRect.right<0:
        cloudRect.right=WINDOWWIDTH-1
    #Draw the white background onto the surface.
    pygame.display.update()
    #time.sleep(1.0/200.0)

    # Draw the window onto the screen.
    mainClock.tick(200)
