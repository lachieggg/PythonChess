
from Player import Player
from pieces import Piece

class Board:
    def __init__(self):
        # board number const
        self.chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.nums = [1, 2, 3, 4, 5, 6, 7, 8]
        # setup board
        self.setup_players()
        self.setup_squares()

    def __repr__(self):
        players = '\nPlayers: \n' + ''.join([repr(player) for player in self.players])
        squares = '\nSquares: \n' + str(self.squares)
        return players + squares

    def setup_squares(self):
        self.squares = {}
        for char in self.chars:
            for num in self.nums:
                key = char + str(num)
                self.squares[key] = 'E' # empty

    def setup_players(self, algorithms=None):
        self.players = [Player('B'), Player('W')]
