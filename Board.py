import os

from Player import Player
from pieces.Piece import Piece
from Constants import *

class Board:
    def __init__(self, pieces):
        """Initializes the board object"""
        # setup board
        self.setup_players()
        self.pieces = pieces
        self.setup_squares()

    def setup_squares(self):
        """Sets up the initial squares on the board"""
        self.squares = {}
        for char in CHARS:
            for num in NUMS[::-1]:
                key = char + str(num)
                self.squares[key] = None # empty

        for piece in self.pieces.values():
            if not piece:
                continue
            self.squares[piece.char + str(piece.num)] = piece

    def get_squares_piece(self, char, num):
        return self.squares.get(char + str(num))

    def setup_players(self, algorithms=None):
        """Sets up the players on the board"""
        self.players = [Player('B'), Player('W')]

    def move_piece(self, piece, from_char, from_num, to_char, to_num):
        """Move the piece on the board without rendering"""
        # Create position strings
        from_pos = from_char + str(from_num)
        to_pos = to_char + str(to_num)
        # Move piece
        piece.char = to_char
        piece.num = to_num
        self.squares[from_pos] = piece
