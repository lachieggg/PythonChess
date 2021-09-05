import os

from Player import Player
from pieces import Piece

### Constants
#   Positions
CHARS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
NUMS =  [1, 2, 3, 4, 5, 6, 7, 8]
#   Widths
SQUARE_WIDTH = 75
BORDER_WIDTH = 50
PIECE_WIDTH = 20
# Image
BOARD_IMG_PATH = os.getcwd() + '/assets/board/board.png'

class Board:
    def __init__(self, pieces):
        # setup board
        self.setup_players()
        self.setup_squares()
        self.pieces = pieces
        self.map()
        self.board_img_path  = BOARD_IMG_PATH

    def get_pieces(self):
        return self.pieces

    def get_piece_width(self):
        return PIECE_WIDTH

    def get_square_width(self):
        return SQUARE_WIDTH

    def get_border_width(self):
        return BORDER_WIDTH

    def __str__(self):
        players = '\nPlayers: \n' + ''.join([str(player) for player in self.players])
        squares = '\nSquares: \n' + str(self.squares)
        return players + squares

    def map(self):
        """
        Map board squares to screen pixels for rendering and selecting squares
        """

        # Map for making moves
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
        print(self.square_to_pixel_mapping)

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
        """
        Returns the square colour as a bool given the coordinates
        Even results are black squares (eg. A1 or C3)
        Odd results are white squares (eg. B1 or C2)
        """
        char_as_num = ord(char) - ord('A') + 1
        if ((char_as_num + num) % 2) == 0:
            return False
        return True

    def get_square_pixel_limits(self, char, num):
        """Returns the pixel limits that constitute the mouse being over a square"""
        x_min, y_min = self.square_to_pixel_mapping.get(char + str(num))
        return [(x_min, x_min+SQUARE_WIDTH), (y_min, y_min+SQUARE_WIDTH)]

    def setup_squares(self):
        self.squares = {}
        for char in CHARS:
            for num in NUMS[::-1]:
                key = char + str(num)
                self.squares[key] = 'E' # empty

    def setup_players(self, algorithms=None):
        self.players = [Player('B'), Player('W')]
