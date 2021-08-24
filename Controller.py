
from Player import Player
from Piece import Piece
from Board import Board

class Controller:
    def __init__(self):
        self.board = Board()
        print(repr(self.board))


controller = Controller()
