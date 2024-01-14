from pygame.time import Clock
import pygame

# settings
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 800
FRAMES_PER_SECOND = 60

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
        if event.type == pygame.QUIT:
            running = False

    # draw
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), (50, 50), 16)
    pygame.display.flip()

    # handle time
    clock.tick(FRAMES_PER_SECOND)
