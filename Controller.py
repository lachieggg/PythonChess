
from Player import Player
from Board import Board
from Window import Window

from pieces.Piece import Piece
from PieceFactory import PieceFactory

class Controller:
    def __init__(self):
        self.board = Board()
        self.window = Window()
        self.window.main()
        self.pieceFactory = PieceFactory()
        print(repr(self.board))


controller = Controller()
