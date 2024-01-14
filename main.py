from pygame.time import Clock
import pygame

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 800
FRAMES_PER_SECOND = 60

if __name__ == '__main__':
    # initialize pygame
    pygame.init()
    # set window size
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # create time object
    clock = Clock()
    # run loop
    running = True
    while running:
        # handle events
        for event in pygame.event.get():
            # exit button
            if event.type == pygame.QUIT:
                running = False
            # key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Spacebar was pressed")
        # draw
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), (50, 50), 16)
        pygame.display.flip()
        # handle time
        clock.tick(FRAMES_PER_SECOND)
