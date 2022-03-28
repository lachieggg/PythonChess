import os

from Player import Player
from pieces.Piece import Piece
from Constants import *
from pieces.Pawn import Pawn

class Board:
    def __init__(self, pieces):
        """Initializes the board object"""
        # Setup board
        self.setup_players()
        self.pieces = pieces
        self.squares = SQUARES

    def get_squares_piece(self, char, num):
        """Get a piece that sits on a square"""
        return self.pieces.get(char + str(num))

    def score(self, colour):
        """Calculate the score of a player"""
        score = 0
        for piece in self.pieces.values():
            if(piece.colour == colour):
                score += piece.value
            else:
                score -= piece.value
        return score

    def setup_players(self, algorithms=None):
        """Sets up the players on the board"""
        self.players = [Player('B'), Player('W')]

    def move_piece(self, _from, _to, scoring=False):
        """Move the piece on the board without rendering"""
        # Create position strings
        if(VERBOSE): print("From = " + _from)
        if(VERBOSE): print("To = " + _to)
        # Piece
        
        piece = self.pieces.get(_from)
        if(type(piece) == Pawn) and scoring:
            # Allow all movement for pawns in scoring
            piece.moved = False

        if not piece:
            print("Could not find piece on that square {}.".format(_from))
            return False

        if not piece.moveable(self, _to) and not GOD_MODE and not scoring:
            # God mode allows you to move any piece anywhere
            # If we are scoring a board allow undoing moves for pawns
            print("Piece = {}, from = {} to = {}".format(piece, _from, _to))
            print("That piece cannot move there.")
            return False

        # Move piece
        piece.char = _to[0]
        piece.num = int(_to[1])
        piece.moved = True
        # Set
        self.pieces[_to] = piece
        del self.pieces[_from]

        return True

