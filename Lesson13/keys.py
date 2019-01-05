import pygame, sys, random
from pygame.locals import *

# Set up pygame.
pygame.init()
#mainClock = pygame.time.Clock()

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

rect = pygame.Rect((1336,0,90,96))
dino = bigSprite.subsurface(rect)
dinoRect=dino.get_rect()


SPEED = 6

windowSurface.blit(dino,dinoRect)
pygame.display.update()

# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_LEFT: 
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT: 
                moveLeft = False
                moveRight = True
            if event.key == K_UP: 
                moveDown = False
                moveUp = True
            if event.key == K_DOWN: 
                moveUp = False
                moveDown = True
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
#             if event.key == K_LEFT or event.key == K_a:
#                 moveLeft = False
#             if event.key == K_RIGHT or event.key == K_d:
#                 moveRight = False
#             if event.key == K_UP or event.key == K_w:
#                 moveUp = False
#             if event.key == K_DOWN or event.key == K_s:
#                 moveDown = False
#             if event.key == K_x:
#                 player.top = random.randint(0, WINDOWHEIGHT -
#                   player.height)
#                 player.left = random.randint(0, WINDOWWIDTH -
#                   player.width)

#    # Draw the white background onto the surface.
#    windowSurface.fill(WHITE)

#     # Move the player.
#     if moveDown and playerRect.bottom < WINDOWHEIGHT:
#         playerRect.top += MOVESPEED
#     if moveUp and playerRect.top > 0:
#         playerRect.top -= MOVESPEED
#     if moveLeft and playerRect.left > 0:
#         playerRect.left -= MOVESPEED
#     if moveRight and playerRect.right < WINDOWWIDTH:
#         playerRect.right += MOVESPEED

#     # Draw the player onto the surface.
#     #pygame.draw.rect(windowSurface, BLACK, player)
#     windowSurface.blit(player, playerRect)

#     # Check whether the player has intersected with any food squares.
#     for food in foods[:]:
#         if playerRect.colliderect(food):
#             foods.remove(food)


#     # Draw the window onto the screen.
#     pygame.display.update()
#     mainClock.tick(40)