from pygame.time import Clock
import pygame

# settings
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 800
FRAMES_PER_SECOND = 60
BALL_COLOR = pygame.Color(255, 0, 0)
BALL_RADIUS = 16

# init
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = Clock()
running = True

# run loop
while running:

    # handle events
    for event in pygame.event.get():
        # exit button
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # draw
    pygame.draw.circle(screen, BALL_COLOR, (WINDOW_WIDTH / 2.0, WINDOW_HEIGHT / 2.0), BALL_RADIUS)
    pygame.display.flip()

    # handle time
    clock.tick(FRAMES_PER_SECOND)
