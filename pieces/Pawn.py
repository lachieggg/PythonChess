from pieces.Piece import Piece
from Constants import *

class Pawn(Piece):
    def __init__(self, type, colour, char, num):
        """Initializer for the Pawn class"""
        super().__init__(type, colour, char, num)

    def moveable(self, board, to_char, to_num):
        """Determines whether the piece can move to a given square"""

        victim = board.get_squares_piece(to_char, to_num)
        # Attempting to take a piece
        #
        if(victim):
            if(self.colour == victim.colour):
                print("You cannot take a piece on your own team!")
                return False
            if(self.colour == WHITE): # White
                if(to_num - self.num == 1):
                    if(not to_char == self.char):
                        return True
            else:
                if(self.num - to_num == 1):
                    if(not to_char == self.char):
                        return True
            return False

        # Attempting to move to a different column without taking a piece
        #
        if(not to_char == self.char):
            return False

        # Attempting to move when a another piece is in path
        #
        if(self.piece_in_move_path(board, to_char, to_num)):
            print("Piece in your way!")
            return False

        return True
