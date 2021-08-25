
from Player import Player
from Piece import Piece

class Board:
    def __init__(self):
        # board number const
        self.chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.nums = [1, 2, 3, 4, 5, 6, 7, 8]
        # setup board
        self.setup_players()
        self.setup_pieces()
        self.setup_squares()

    def __repr__(self):
        players = '\nPlayers: \n' + ''.join([repr(player) for player in self.players])
        pieces = '\nPieces: \n' + ''.join([repr(piece) for piece in self.pieces])
        squares = '\nSquares: \n' + str(self.squares)
        return players + pieces + squares

    def setup_squares(self):
        self.squares = {}
        for char in self.chars:
            for num in self.nums:
                key = char + str(num)
                self.squares[key] = 'E' # empty

        for piece in self.pieces:
            self.squares[piece.char + str(piece.num)] = piece.type


    def setup_players(self, algorithms=None):
        self.players = [Player('B'), Player('W')]

    def setup_pieces(self):
        self.pieces = []
        # kings
        self.pieces.append(Piece('WK', 1, 'E', 1))
        self.pieces.append(Piece('BK', 0, 'E', 8))
        # queens
        self.pieces.append(Piece('WQ', 1, 'D', 1))
        self.pieces.append(Piece('BQ', 0, 'D', 8))
        # rooks
        self.pieces.append(Piece('WR', 1, 'A', 1))
        self.pieces.append(Piece('WR', 1, 'H', 1))
        self.pieces.append(Piece('BR', 0, 'A', 8))
        self.pieces.append(Piece('BR', 0, 'H', 8))
        # knights
        self.pieces.append(Piece('WH', 1, 'B', 1))
        self.pieces.append(Piece('WH', 1, 'G', 1))
        self.pieces.append(Piece('BH', 0, 'B', 8))
        self.pieces.append(Piece('BH', 0, 'G', 8))
        # bishops
        self.pieces.append(Piece('WB', 1, 'C', 1))
        self.pieces.append(Piece('WB', 1, 'F', 1))
        self.pieces.append(Piece('BB', 0, 'C', 8))
        self.pieces.append(Piece('BB', 0, 'F', 8))
        # pawns
        for char in self.chars:
            self.pieces.append(Piece('WP', 1, char, 1))
            self.pieces.append(Piece('BP', 0, char, 7))
