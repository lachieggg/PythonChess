from pieces.Piece import Piece

from Constants import *

class Rook(Piece):
    def __init__(self, type, colour, char, num):
        """Initializer for the Rook class"""
        super().__init__(type, colour, char, num)


    def moveable(self, board, _to):
            """Determines whether the piece can move to a given square"""
            to_char, to_num = _to[0], int(_to[1])

            if(not self.path_clear(board, to_char, to_num)):
                if(VERBOSE): print("Piece is in your way!")
                return False

            if(not self.num == to_num):
                if(not self.char == to_char):
                    return False

            victim = board.get_squares_piece(to_char, to_num)
            # Attempting to take a piece
            if(victim):
                if(self.colour == victim.colour):
                    if(VERBOSE): print("You cannot take a piece on your own team!")
                    return False

            return True
