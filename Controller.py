
from Player import Player
from Piece import Piece
from Board import Board
from Window import Window

class Controller:
    def __init__(self):
        self.board = Board()
        self.window = Window()
        self.window.main()
        print(repr(self.board))


controller = Controller()
