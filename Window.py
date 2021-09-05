import os
import pygame

import Board
from Constants import *

class Window:
    def __init__(self):
        """Initializer for the Window"""
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.fill((255, 255, 255))
        self.board_img = pygame.image.load_extended(BOARD_IMG_PATH)
        self.screen.blit(self.board_img, (0, 0))

    def render_piece(self, board, piece):
        """Render a piece in the window"""
        pos = piece.get_position() # Position eg. 'H5' or 'A3'
        [x, y] = board.get_pixels_from_square(*pos)
        print(piece.filename)
        icon = pygame.image.load_extended(piece.filename)
        self.screen.blit(icon, (x+PIECE_WIDTH, y+SQUARE_WIDTH/2-PIECE_WIDTH))

    def render_pieces(self, board):
        """Render all the pieces on the board"""
        for piece in list(board.get_pieces().values()):
            self.render_piece(board, piece)

    def get_square_rgb(self, board, char, num):
        """Get the square RGB from char and num coords"""
        if board.get_square_colour(char, num):
            return CREAM_RGB
        return BROWN_RGB

    def remove_prev_highlight(self, board, selected_sq):
        """Remove highlight from previously highlighted square"""
        if not selected_sq:
            return

        char, num = list(selected_sq.values())
        pixel_coords = board.get_pixels_from_square(char, num)
        square_rgb = self.get_square_rgb(board, *list(selected_sq.values()))
        sq_width = SQUARE_WIDTH
        pygame.draw.rect(
            self.screen,
            square_rgb,
            (*pixel_coords, sq_width, sq_width),
            1
        )

    def highlight_sq(self, board, char, num):
        """Highlight a square on the Window"""
        coords = board.get_pixels_from_square(char, num)
        x, y = coords

        pygame.draw.rect(
            self.screen,
            RED_RGB,
            (x, y, SQUARE_WIDTH, SQUARE_WIDTH),
            1
        )

    def get_screen_dimensions(self):
        """Return the dimensions of the screen as  a tuple"""
        return SCREEN_DIMENSIONS
