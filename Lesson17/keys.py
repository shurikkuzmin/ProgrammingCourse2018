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


dinoRunning=[0,0,0,0]
for i in range(4):
    rect=pygame.Rect((1516+i*88,0,88,96))
    dinoRunning[i]=bigSprite.subsurface(rect)
#dinoRun1=pygame.Rect((1516,0,90,96))
#dinoRun2=pygame.Rect((1516,0,90,96))


SPEED = 1
SPEED2= 10

windowSurface.fill(WHITE)

moveRight=False
dino=dinoStanding
dinoRect=dinoStandingRect
counter=0
# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT: 
                moveRight = True
                counter=0

        if event.type == KEYUP:
            if event.key == K_RIGHT:
                    moveRight = False
    if moveRight==True:

        if dinoRect.right + SPEED >= WINDOWWIDTH:
            dinoRect.right = WINDOWWIDTH-1
        else: 
            dinoRect.right = dinoRect.right+SPEED
        dino=dinoRunning[int(counter/SPEED2)%4]
        counter=(counter+1)
    else:

        dino=dinoStanding
        
    windowSurface.fill(WHITE)
    windowSurface.blit(dino,dinoRect)

    #Draw the white background onto the surface.
    pygame.display.update()
    #time.sleep(1.0/200.0)

    # Draw the window onto the screen.
    mainClock.tick(200)