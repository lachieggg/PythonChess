
from Player import Player
from Board import Board
from Window import Window

from pieces.Piece import Piece
from PieceFactory import PieceFactory

class Controller:
    def __init__(self):
        self.pieceFactory = PieceFactory()
        self.pieceFactory.create_pieces_init()
        self.board = Board()
        self.window = Window(self.board)
        self.render_pieces()
        self.setup_players()
        self.window.main()
        # ..


    def render_pieces(self):
        pieces = self.pieceFactory.pieces
        for piece in pieces:
            print(piece)
        self.window.render_pieces(pieces)

    def setup_players(self, algorithms=None):
        self.players = [Player('B'), Player('W')]

    def play(self):
        pass

    def setup_squares(self):
        self.squares = {}
        for char in self.chars:
            for num in self.nums:
                key = char + str(num)
                self.squares[key] = 'E' # empty


controller = Controller()
