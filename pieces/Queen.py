from pieces.Piece import Piece
from pieces.Rook import Rook
from pieces.Bishop import Bishop

from Constants import *

class Queen(Piece):
    def __init__(self, type, colour, char, num):
        """Initializer for the Queen class"""
        super().__init__(type, colour, char, num)

    def moveable(self, board, _to):
            """Determines whether the piece can move to a given square"""
            to_char, to_num = _to[0], int(_to[1])

            # A queen is just a bishop and a rook rolled into one piece
            #
            rook = Rook(self.type, self.colour, self.char, self.num)
            bishop = Bishop(self.type, self.colour, self.char, self.num)

            # Make sure at least one of thsee sub-pieces can move to that square
            #
            if(rook.moveable(board, _to)):
                return True
            if(bishop.moveable(board, _to)):
                return True

            return False
