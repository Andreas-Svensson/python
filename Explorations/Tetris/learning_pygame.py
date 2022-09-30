"""Code from introduction page on pygame"""

import sys, pygame
import numpy as np
pygame.init()

size = width, height = 350, 700 # window size
black = 0, 0, 0 # background color
gray = 100, 100, 100 # shape color

screen = pygame.display.set_mode(size) # set screen to size

# ----- read in image file -----
# NOTE: in future: use os.path.join to build path and concatenate with relative file path
# ball = pygame.image.load("c:/GitHub/Python-Andreas-Svensson/Explorations/Tetris/assets/intro_ball.gif")
# ballrect = ball.get_rect()

board = np.zeros((22, 10))  # 10x20 size board, top 2 rows are outside of visible game board

move_distance = 35 # change factor of velocity for input move commands

x_pos = 3 * move_distance # starting pos of shape is always 3 steps to the right (shapes start centered of offset 1 to the left)
y_pos = 0 # starting pos of shape
shape_width = 35
shape_height = 35

I = np.array(([0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0])) # I-shape
O = np.array(([0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0])) # O-shape
T = np.array(([0, 1, 0], [1, 1, 1], [0, 0, 0])) # T-shape
J = np.array(([1, 0, 0], [1, 1, 1], [0, 0, 0])) # J-shape
L = np.array(([0, 0, 1], [1, 1, 1], [0, 0, 0])) # L-shape
S = np.array(([0, 1, 1], [1, 1, 0], [0, 0, 0])) # S-shape
Z = np.array(([1, 1, 0], [0, 1, 1], [0, 0, 0])) # Z-shape

shape = I
# ----- position and velocity variables -----

while 1:
    # pygame.time.delay(10) # set a delay of n ms

    # ----- events -----
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: sys.exit() # exit if exit

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x_pos - move_distance >= 0:
                x_pos -= move_distance

            if event.key == pygame.K_RIGHT and x_pos + move_distance < width:
                x_pos += move_distance

            if event.key == pygame.K_UP and y_pos - move_distance >= 0:
                y_pos -= move_distance

            if event.key == pygame.K_DOWN and y_pos + move_distance < height:
                y_pos += move_distance

    # ----- overwrite old screen with black, draw new screen, and show (flip) it -----
    screen.fill(black)

    #screen.blit(screen, pygame.draw.rect(screen, gray, square)) # NOTE: Drawing test rect on screen
    x, y = np.where(shape == 1)
    for a, b in zip(x, y):
        pygame.draw.rect(screen, gray, (x_pos + a, y_pos + b, shape_width, shape_height))

    pygame.display.flip()