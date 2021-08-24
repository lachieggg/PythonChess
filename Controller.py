
from Player import Player
from Piece import Piece
from Board import Board

class Controller:
    def __init__(self):
        self.players = [Player(1), Player(2)]
        self.board = Board(self.players)
        print(repr(self.board))
        pass

controller = Controller()
