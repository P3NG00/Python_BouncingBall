import math
import random

import pygame
from pygame.time import Clock


def random_unit_vector() -> pygame.Vector2:
    angle = random.uniform(0, 2.0 * math.pi)
    x = math.cos(angle)
    y = math.sin(angle)
    return pygame.Vector2(x, y)


# settings
fps = 60
window = {
    'width': 1280,
    'height': 800,
}
ball = {
    'color': pygame.Color(255, 0, 0),
    'radius': 16,
    'position': pygame.Vector2(window['width'] / 2.0, window['height'] / 2.0),
    'direction': random_unit_vector(),
}

# init
pygame.init()
screen = pygame.display.set_mode((window['width'], window['height']))
clock = Clock()
running = True

# run loop
while running:

    # handle events
    for event in pygame.event.get():
        # exit button
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # update ball position
    ball['position'] += ball['direction']
    # TODO bounce off walls

    # draw ball
    pygame.draw.circle(screen, ball['color'], ball['position'], ball['radius'])
    pygame.display.flip()
    # handle time
    clock.tick(fps)
