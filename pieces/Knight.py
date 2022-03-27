from pieces.Piece import Piece
from Constants import *

class Knight(Piece):
    def __init__(self, type, colour, char, num):
        """Initializer for the Knight class"""
        super().__init__(type, colour, char, num)
        pass

    def moveable(self, board, to_char, to_num):
        """Determines whether the piece can move to a given square"""


        victim = board.get_squares_piece(to_char, to_num)
        # Attempting to take a piece
        if(victim):
            if(self.colour == victim.colour):
                if(VERBOSE): print("You cannot take a piece on your own team!")
                return False
                
        abs_delta_x = abs(ord(to_char) - ord(self.char))
        abs_delta_y = abs(to_num - self.num)

        # Knights can move to positions where the absolute
        # value of the sum of the differences between the squares
        # is exactly 3
        if((abs_delta_x == 2 and abs_delta_y) == 1 or (abs_delta_x == 1 and abs_delta_y == 2)):
            return True
        return False
