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
        return self.pieces.get(char + str(num))

    def setup_players(self, algorithms=None):
        """Sets up the players on the board"""
        self.players = [Player('B'), Player('W')]

    def move_piece(self, player, turn, from_char, from_num, to_char, to_num):
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
            return False

        if not player.colour == piece.colour and not SANDBOX_MODE and not GOD_MODE:
            # Sandbox mode allows you to use any piece
            print("That is not your piece to move.")
            return False

        if not turn == player and not SANDBOX_MODE and not GOD_MODE:
            # God mode allows you to skip opposition's turn
            print("It is not currently your turn.")
            return False

        if not piece.moveable(self, to_char, to_num) and not GOD_MODE:
            # God mode allows you to move any piece anywhere
            print("That piece cannot move there.")
            return False

        # Move piece
        piece.char = to_char
        piece.num = to_num
        piece.moved = True
        # Set
        self.pieces[to_pos] = piece
        self.pieces[from_pos] = None

        return True
