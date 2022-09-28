"""Code from introduction page on pygame"""

import sys, pygame
pygame.init()

size = width, height = 720, 480
speed = [4, 3]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

# NOTE: in future: use os.path.join to build path and concatenate with relative file path

ball = pygame.image.load("c:/GitHub/Python-Andreas-Svensson/Explorations/Tetris/assets/intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    # create a delay of 10 ms
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()