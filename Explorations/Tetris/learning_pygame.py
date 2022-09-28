"""Code from introduction page on pygame"""

import sys, pygame
import numpy as np
pygame.init()

size = width, height = 300, 600 # window size
black = 0, 0, 0 # background color
gray = 100, 100, 100 # shape color

screen = pygame.display.set_mode(size) # set screen to size

# ----- read in image file -----
# NOTE: in future: use os.path.join to build path and concatenate with relative file path
# ball = pygame.image.load("c:/GitHub/Python-Andreas-Svensson/Explorations/Tetris/assets/intro_ball.gif")
# ballrect = ball.get_rect()

shape_x = 0
shape_y = 0
shape_width = 30
shape_height = 30

# ----- position and velocity variables -----
vel = 30 # change factor of velocity for input move commands

while 1:
    pygame.time.delay(10) # set a delay of n ms

    # ----- events -----
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: sys.exit() # exit if exit

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and shape_x - vel >= 0:
                shape_x -= vel

            if event.key == pygame.K_RIGHT and shape_x + vel < width:
                shape_x += vel

            if event.key == pygame.K_UP and shape_y - vel >= 0:
                shape_y -= vel

            if event.key == pygame.K_DOWN and shape_y + vel < height:
                shape_y += vel

    # ----- overwrite old screen with black, draw new screen, and show (flip) it -----
    screen.fill(black)
    
    for i in range(600):
        screen.set_at((150, i), gray)
        screen.set_at((i, 300), gray)

    #screen.blit(screen, pygame.draw.rect(screen, gray, square)) # NOTE: Drawing test rect on screen
    pygame.draw.rect(screen, gray, (shape_x, shape_y, shape_width, shape_height))
    pygame.display.flip()