#!/usr/bin/env python3

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
