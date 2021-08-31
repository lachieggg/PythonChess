
from Player import Player
from pieces import Piece


### Constants
#   Positions
CHARS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
NUMS = [1, 2, 3, 4, 5, 6, 7, 8]
#   Widths
SQUARE_WIDTH = 75           # Width of each square
BORDER_WIDTH = 35           # Border widith for the purposes of rendering
BORDER_WIDTH_REAL = 50      # Real border width

class Board:
    def __init__(self):
        # setup board
        self.setup_players()
        self.setup_squares()
        print(self)
        self.map()

    def __str__(self):
        players = '\nPlayers: \n' + ''.join([str(player) for player in self.players])
        squares = '\nSquares: \n' + str(self.squares)
        return players + squares

    def map(self):
        """
        Map board squares to screen pixels for rendering and making moves
        """
        self.render_mapping = {}
        x = BORDER_WIDTH-SQUARE_WIDTH/2

        # Map for rendering pieces
        for char in CHARS:
            y = BORDER_WIDTH-SQUARE_WIDTH/2
            x += SQUARE_WIDTH
            for num in NUMS:
                y += SQUARE_WIDTH
                key = char + str(num)
                self.render_mapping[key] = [x,y]


        # Map for making moves
        self.square_mapping = {}

        x = BORDER_WIDTH_REAL
        for char in CHARS:
            y = BORDER_WIDTH_REAL
            x += SQUARE_WIDTH
            for num in NUMS:
                y += SQUARE_WIDTH
                key = char + str(num)
                self.square_mapping[key] = (x, y)


        print('\n')
        print(self.render_mapping)

    def get_square_from_mouse_position(self, x, y, screen_width, screen_height):
        """Returns the square id from mouse position"""

        if x < BORDER_WIDTH_REAL or x > screen_width - BORDER_WIDTH_REAL:
            return False
        if y < BORDER_WIDTH_REAL or y > screen_height - BORDER_WIDTH_REAL:
            return False

        x = x - BORDER_WIDTH_REAL
        y = screen_height - BORDER_WIDTH_REAL - y

        num = NUMS[int(float(y)/SQUARE_WIDTH)]
        char = CHARS[int(float(x)/SQUARE_WIDTH)]

        return char + str(num)

    def get_square_pixel_limits(self, char, num):
        """Returns the pixel limits that constitute the mouse being over a square"""
        x_min, y_min = self.square_mapping.get(char + str(num))
        return [(x_min, x_min+SQUARE_WIDTH), (y_min, y_min+SQUARE_WIDTH)]

    def setup_squares(self):
        self.squares = {}
        for char in CHARS:
            for num in NUMS:
                key = char + str(num)
                self.squares[key] = 'E' # empty

    def setup_players(self, algorithms=None):
        self.players = [Player('B'), Player('W')]
