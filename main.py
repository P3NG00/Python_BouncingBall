import math
import random

import pygame
from pygame import Vector2, Color
from pygame.time import Clock


def random_unit_vector() -> Vector2:
    angle = random.uniform(0, 2.0 * math.pi)
    x = math.cos(angle)
    y = math.sin(angle)
    return Vector2(x, y)


# settings
window = {
    'width': 1280,
    'height': 800,
    'fps': 60,
    'background': Color(0, 0, 0),
}
ball = {
    'color': Color(255, 0, 0),
    'radius': 16,
    'speed': 10,
    # TODO replace position with 'Vector2(0, 0)' and implement camera
    'position': Vector2(0, 0),
    'direction': random_unit_vector(),
}
digits = {
    'decimals': 4,
    'position': 5,
    'direction': 3,
}

# init
pygame.init()
screen = pygame.display.set_mode((window['width'], window['height']))
clock = Clock()
running = True
camera_offset = -Vector2(window['width'] / 2, window['height'] / 2)
output_format = f' | pos_x: {{:>{digits['decimals'] + digits['position']},.{digits['decimals']}f}}' \
                f' | pos_y: {{:>{digits['decimals'] + digits['position']},.{digits['decimals']}f}}' \
                f' | dir_x: {{:>{digits['decimals'] + digits['direction']},.{digits['decimals']}f}}' \
                f' | dir_y: {{:>{digits['decimals'] + digits['direction']},.{digits['decimals']}f}} |'

# run loop
while running:

    # handle events
    for event in pygame.event.get():
        # exit button
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # update ball position
    ball['position'] += (ball['direction'] * ball['speed'])
    print(output_format.format(ball['position'].x, ball['position'].y, ball['direction'].x, ball['direction'].y))
    # TODO bounce off walls

    # clear screen
    screen.fill(window['background'])
    # draw ball
    pygame.draw.circle(screen, ball['color'], ball['position'] - camera_offset, ball['radius'])
    pygame.display.flip()
    # handle time
    clock.tick(window['fps'])
