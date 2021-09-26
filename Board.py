import os

from Player import Player
from pieces.Piece import Piece
from Constants import *

class Board:
    def __init__(self, pieces):
        """Initializes the board object"""
        # setup board
        self.setup_players()
        self.pieces = pieces
        self.setup_squares()
        self.map()

    def map(self):
        """Map board squares to screen pixels for rendering and selecting squares"""
        self.square_to_pixel_mapping = {}

        x = BORDER_WIDTH - SQUARE_WIDTH
        for char in CHARS:
            y = BORDER_WIDTH - SQUARE_WIDTH
            x += SQUARE_WIDTH
            for num in NUMS[::-1]:
                y += SQUARE_WIDTH
                key = char + str(num)
                self.square_to_pixel_mapping[key] = (x, y)


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

        return self.square_to_pixel_mapping.get(char + str(num))

    def get_square_colour(self, char, num):
        """Returns the square colour as a bool given the coordinates"""
        char_as_num = ord(char) - ord('A') + 1
        if ((char_as_num + num) % 2) == 0:
            return False
        return True

    def get_square_pixel_limits(self, char, num):
        """Returns the pixel limits that constitute the mouse being over a square"""
        x_min, y_min = self.square_to_pixel_mapping.get(char + str(num))
        return [(x_min, x_min+SQUARE_WIDTH), (y_min, y_min+SQUARE_WIDTH)]

    def setup_squares(self):
        """Sets up the initial squares on the board"""
        self.squares = {}
        for char in CHARS:
            for num in NUMS[::-1]:
                key = char + str(num)
                self.squares[key] = None # empty

        for piece in self.pieces.values():
            if not piece:
                continue
            self.squares[piece.char + str(piece.num)] = piece

    def get_squares_piece(self, char, num):
        return self.squares.get(char + str(num))

    def setup_players(self, algorithms=None):
        """Sets up the players on the board"""
        self.players = [Player('B'), Player('W')]

    def move_piece(self, piece, from_char, from_num, to_char, to_num):
        # Create position strings
        from_pos = from_char + str(from_num)
        to_pos = to_char + str(to_num)
        # Move piece
        piece.char = to_char
        piece.num = to_num
        self.squares[from_pos] = piece
