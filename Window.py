import os
import pygame

import Board
from Constants import *

class Window:
    def __init__(self):
        """Initializer for the Window"""
        pygame.init()
        pygame.display.set_caption('PythonChess')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.fill((255, 255, 255))
        self.bgimg = pygame.image.load_extended(BOARD_IMG_PATH)
        self.screen.blit(self.bgimg, (0, 0))
        self.map()

    def render_square(self, sq):
        """Render a _blank_ square on the board"""
        char = sq[0]
        num = int(sq[1])
        colour = self.get_square_rgb(char, num)
        pos = self.get_pixels_from_square(char, num)
        rgb = self.get_square_rgb(char, num)
        pygame.draw.rect(self.screen, rgb, [pos[0], pos[1], SQUARE_WIDTH, SQUARE_WIDTH])

    def render_piece(self, piece):
        """Render a piece in the window"""
        if not piece:
            return
        pos = piece.get_position() # Position eg. 'H5' or 'A3'
        [x, y] = self.get_pixels_from_square(*pos)
        icon = pygame.image.load_extended(piece.filename)
        self.screen.blit(icon, (x+PIECE_WIDTH, y+SQUARE_WIDTH/2-PIECE_WIDTH))

    def render_pieces(self, pieces_list):
        """Render all the pieces on the board"""
        for piece in pieces_list:
            self.render_piece(piece)

    def get_square_rgb(self, char, num):
        """Get the square RGB from char and num coords"""
        if self.get_square_colour(char, num):
            return CREAM_RGB
        return BROWN_RGB

    def get_square_colour(self, char, num):
        """Returns the square colour as a bool given the coordinates"""
        char_as_num = ord(char) - ord('A') + 1
        if ((char_as_num + num) % 2) == 0:
            return False
        return True

    def remove_prev_highlight(self, selected_sq):
        """Remove highlight from previously highlighted square"""
        if not selected_sq:
            return

        char, num = selected_sq[0], int(selected_sq[1])
        pixel_coords = self.get_pixels_from_square(char, num)
        square_rgb = self.get_square_rgb(char, num)
        sq_width = SQUARE_WIDTH
        pygame.draw.rect(
            self.screen,
            square_rgb,
            (*pixel_coords, sq_width, sq_width),
            HIGHLIGHTING_WIDTH
        )

    def highlight_sq(self, sq):
        """Highlight a square on the Window"""
        char, num = sq[0], int(sq[1])
        coords = self.get_pixels_from_square(char, num)
        x, y = coords

        pygame.draw.rect(
            self.screen,
            RED_RGB,
            (x, y, SQUARE_WIDTH, SQUARE_WIDTH),
            HIGHLIGHTING_WIDTH
        )

    def get_screen_dimensions(self):
        """Return the dimensions of the screen as  a tuple"""
        return SCREEN_DIMENSIONS

    def map(self):
        """Map board squares to screen pixels for rendering and selecting squares"""
        self.pmap = {} # PMAP i.e. Pixel Map

        x = BORDER_WIDTH - SQUARE_WIDTH
        for char in CHARS:
            y = BORDER_WIDTH - SQUARE_WIDTH
            x += SQUARE_WIDTH
            for num in NUMS[::-1]:
                y += SQUARE_WIDTH
                key = char + str(num)
                self.pmap[key] = (x, y)

        print('\n')

    def get_square_from_pixels(self, x, y, screen_width, screen_height):
        """Returns the square id from mouse position"""

        num_index = int(float(y - BORDER_WIDTH)/SQUARE_WIDTH)
        char_index = int(float(x - BORDER_WIDTH)/SQUARE_WIDTH)

        if num_index >= len(NUMS) or char_index >= len(CHARS):
            return False

        num = NUMS[::-1][num_index]
        char = CHARS[char_index]

        return char + str(num)

    def get_pixels_from_square(self, char, num):
        """Returns the mouse position from square char and number"""

        if char not in CHARS or num not in NUMS:
            return False

        return self.pmap.get(char + str(num))


    def get_square_pixel_limits(self, char, num):
        """Returns the pixel limits that constitute the mouse being over a square"""
        x_min, y_min = self.pmap.get(char + str(num))
        return [(x_min, x_min+SQUARE_WIDTH), (y_min, y_min+SQUARE_WIDTH)]
