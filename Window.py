
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

import Board

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
BOARD_IMG_PATH = os.getcwd() + '/assets/board/board.png'

class Window:
    def __init__(self, board):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.fill((255, 255, 255))
        self.board_img = pygame.image.load_extended(BOARD_IMG_PATH)
        self.board = board
        self.screen.blit(self.board_img, (0, 0))

    def render_piece(self, piece):
        mapping = self.board.mapping
        board_position = piece.get_position()   # Position eg. 'H5' or 'A3'
        (x, y) = mapping.get(board_position) # Position eg. (700, 400)
        print("x, y = " + str(x) + ' ' +  str(y))
        print(piece.filename)
        icon = pygame.image.load_extended(piece.filename)
        self.screen.blit(icon, (x, y))


    def render_pieces(self, pieces):
        for piece in pieces:
            self.render_piece(piece)

    def main(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                elif event.type == QUIT:
                    running = False


            pygame.display.flip()

        pygame.quit()
