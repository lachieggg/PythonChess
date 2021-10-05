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

    def get_squares_piece(self, char, num):
        print(self.pieces)
        key = char + str(num)
        print(key)
        print(self.pieces.get(key))
        return self.pieces.get(char + str(num))

    def setup_players(self, algorithms=None):
        """Sets up the players on the board"""
        self.players = [Player('B'), Player('W')]

    def move_piece(self, from_char, from_num, to_char, to_num):
        """Move the piece on the board without rendering"""
        # Create position strings
        from_pos = from_char + str(from_num)
        to_pos = to_char + str(to_num)
        print("From = " + from_pos)
        print("To = " + to_pos)
        # Piece
        piece = self.pieces.get(from_pos)
        if not piece:
            print("Could not find piece on that square {}.".format(from_pos))
            return
        # Move piece
        piece.char = to_char
        piece.num = to_num
        # Set
        self.pieces[to_pos] = piece
        self.pieces[from_pos] = None
