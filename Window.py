
import pygame

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP
)

import Board

# Screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN_DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)
# Colours
CREAM_RGB = (248, 248, 151)
BROWN_RGB = (107, 73, 4)
RED_RGB   = (255, 0, 0)


class Window:
    def __init__(self, board):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.fill((255, 255, 255))
        self.board = board
        self.board_img = pygame.image.load_extended(self.board.board_img_path)
        self.screen.blit(self.board_img, (0, 0))
        self.highlighted_sq = False

    def render_piece(self, piece):
        pos = piece.get_position() # Position eg. 'H5' or 'A3'
        piece_width = self.board.get_piece_width()
        square_width = self.board.get_square_width()
        [x, y] = self.board.get_pixels_from_square(*pos)
        icon = pygame.image.load_extended(piece.filename)
        self.screen.blit(icon, (x+piece_width, y+square_width/2-piece_width))

    def render_pieces(self):
        for piece in list(self.board.get_pieces().values()):
            self.render_piece(piece)

    def get_square_rgb(self, char, num):
        """Get the square RGB from char and num coords"""
        if self.board.get_square_colour(char, num):
            return CREAM_RGB
        return BROWN_RGB

    def remove_prev_highlight(self):
        """Remove highlight from previously highlighted square"""
        if not self.highlighted_sq:
            return

        char, num = list(self.highlighted_sq.values())

        pixel_coords = self.board.get_pixels_from_square(char, num)
        square_rgb = self.get_square_rgb(*list(self.highlighted_sq.values()))
        sq_width = self.board.get_square_width()
        pygame.draw.rect(
            self.screen,
            square_rgb,
            (*pixel_coords, sq_width, sq_width),
            1
        )


    def highlight_square(self, char, num):
        new_coords = self.board.get_pixels_from_square(char, num)
        if not new_coords:
            return
        sq_width = self.board.get_square_width()

        self.remove_prev_highlight()

        x, y = new_coords

        pygame.draw.rect(
            self.screen,
            RED_RGB,
            (x, y, self.board.get_square_width(), self.board.get_square_width()),
            1
        )

        self.highlighted_sq = {'char': char,  'num': num}


    def main(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                elif event.type == QUIT:
                    running = False

                if event.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    sq = self.board.get_square_from_pixels(x, y, SCREEN_WIDTH, SCREEN_HEIGHT)
                    if not sq:
                        continue
                    print("Selecting square: " + sq)

                    self.highlight_square(sq[0], int(sq[1]))

            pygame.display.flip()

        pygame.quit()
