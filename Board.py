import os

from Player import Player
from pieces.Piece import Piece
from Constants import *
from pieces.Pawn import Pawn
from pieces.King import King

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

    def move_piece(self, _from, _to):
        """Move the piece on the board without rendering"""
        # Create position strings
        if(VERBOSE): print("From = " + _from)
        if(VERBOSE): print("To = " + _to)

        # Piece
        piece = self.pieces.get(_from)

        if not piece:
            print("Could not find piece on that square {}.".format(_from))
            return False

        if not piece.moveable(self, _to) and not GOD_MODE:
            # God mode allows you to move any piece anywhere
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
    
    def is_in_check(self, colour):
        """Checks if the King of the given colour is under attack"""
        king_pos = None
        for piece in self.pieces.values():
            if isinstance(piece, King) and piece.colour == colour:
                king_pos = piece.char + str(piece.num)
                break
        
        if not king_pos:
            return False 

        # Iterate all enemy pieces to see if any can attack the King
        for piece in self.pieces.values():
            if piece.colour != colour:
                if piece.moveable(self, king_pos):
                    return True
        return False

    def is_terminal(self):
        """
        Determines whether the board is in a terminal state.
        Returns:
            WHITE if White wins
            BLACK if Black wins
            'Stalemate' if draw
            False if game continues
        """
        # Improved terminal check using legal moves will be implemented 
        # via Player.get_possible_moves_for_player checking for checkmate
        # For now, keep the king capture logic as fallback until move filtering is in place
        
        kings = [p for p in self.pieces.values() if isinstance(p, King)]
        if len(kings) < 2:
            return WHITE if any(k.colour == WHITE for k in kings) else BLACK
            
        return False
