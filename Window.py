
import pygame
import os

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

class Window:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.fill((0, 0, 0))
        self.board_img = pygame.image.load_extended(os.getcwd() + '/assets/board.png')

    def main(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                elif event.type == QUIT:
                    running = False

            #self.screen.fill((255, 253, 195))
            #pygame.draw.circle(self.screen, (255, 255, 255), (250, 250), 75)

            pygame.display.flip()
            #print(os.getcwd() + '/assets/board.png')
            self.screen.blit(self.board_img, (50, 50))

        pygame.quit()
