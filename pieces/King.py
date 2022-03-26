from pieces.Piece import Piece
from Constants import *

class King(Piece):
    def __init__(self, type, colour, char, num):
        """Initializer for the King class"""
        super().__init__(type, colour, char, num)
        pass


    def moveable(self, board, to_char, to_num):
        """Determines whether the piece can move to a given square"""

        if(not self.path_clear(board, to_char, to_num)):
            if(VERBOSE): print("Piece is in your way!")
            return False

        victim = board.get_squares_piece(to_char, to_num)
        # Attempting to take a piece
        if(victim):
            if(self.colour == victim.colour):
                if(VERBOSE): print("You cannot take a piece on your own team!")
                return False


        if(abs(self.num - to_num) > 1):
            return False
        if(abs(ord(self.char) - ord(to_char)) > 1):
            return False
        if(abs(self.num - to_num) + abs(ord(self.char) - ord(to_char)) > 2):
            return False

        return True
