
from Player import Player
from pieces import Piece

### Constants
#   Positions
CHARS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
NUMS = [1, 2, 3, 4, 5, 6, 7, 8]
#   Widths
SQUARE_WIDTH = 75
BORDER_WIDTH = 35

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
        Map board numbers to screen pixels
        """
        self.mapping = {}
        x = y = BORDER_WIDTH-SQUARE_WIDTH/2

        for char in CHARS:
            y = BORDER_WIDTH-SQUARE_WIDTH/2
            x += SQUARE_WIDTH
            for num in NUMS:
                y += SQUARE_WIDTH
                key = char + str(num)
                self.mapping[key] = [x,y]

        print('\n')
        print(self.mapping)



    def setup_squares(self):
        self.squares = {}
        for char in CHARS:
            for num in NUMS:
                key = char + str(num)
                self.squares[key] = 'E' # empty

    def setup_players(self, algorithms=None):
        self.players = [Player('B'), Player('W')]
