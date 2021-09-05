#!/usr/bin/env python3

from Player import Player
from Board import Board
from Window import Window

from pieces.Piece import Piece
from PieceFactory import PieceFactory

class Controller:
    def __init__(self):
        # Piece Factory
        self.piece_factory = PieceFactory()
        pieces = self.piece_factory.get_pieces()
        # Board
        self.board = Board(pieces)
        # Window
        self.window = Window(self.board)
        self.window.render_pieces()
        # Players
        self.setup_players()
        # Main
        self.window.main()

    def setup_players(self, algorithms=None):
        self.players = {'B': Player('B'), 'W': Player('W')}

    def play(self):
        return
        playing = True
        player = self.players.get('W')
        while playing:
            while not player.moved:
                sleep(1)

    def setup_squares(self):
        self.squares = {}
        for char in self.chars:
            for num in self.nums:
                key = char + str(num)
                self.squares[key] = 'E' # empty


controller = Controller()
