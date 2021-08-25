
from Player import Player
from Board import Board
from Window import Window

from pieces import Piece

class Controller:
    def __init__(self):
        self.board = Board()
        self.window = Window()
        self.window.main()
        print(repr(self.board))


controller = Controller()
