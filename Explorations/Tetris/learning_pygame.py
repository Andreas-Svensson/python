"""Code from introduction page on pygame"""

import sys, pygame
import numpy as np
pygame.init()

size = width, height = 300, 600 # window size
black = 0, 0, 0 # background color
gray = 100, 100, 100

screen = pygame.display.set_mode(size) # set screen to size

# ----- read in image file -----
# NOTE: in future: use os.path.join to build path and concatenate with relative file path
# ball = pygame.image.load("c:/GitHub/Python-Andreas-Svensson/Explorations/Tetris/assets/intro_ball.gif")
# ballrect = ball.get_rect()

square = pygame.Rect(0, 0, 30, 30) # NOTE: Test creation of rect

# ----- position and velocity variables -----
vel = 15 # change factor of velocity for input move commands

while 1:
    pygame.time.delay(100) # set a delay of n ms

    # ----- events -----
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: sys.exit() # exit if exit

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and square.left - vel >= 0:
                square = square.move(-vel, 0)
            if event.key == pygame.K_RIGHT and square.right + vel < 300:
                square = square.move(vel, 0)
            if event.key == pygame.K_UP and square.top - vel >= 0:
                square = square.move(0, -vel)
            if event.key == pygame.K_DOWN and square.bottom < height - vel:
                square = square.move(0, vel)

    # ----- overwrite old screen with black, draw new screen, and show (flip) it -----
    screen.fill(black)
    screen.blit(screen, pygame.draw.rect(screen, gray, square)) # NOTE: Drawing test rect on screen
    pygame.display.flip()