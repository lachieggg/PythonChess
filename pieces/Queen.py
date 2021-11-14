from pieces.Piece import Piece
from pieces.Rook import Rook
from pieces.Bishop import Bishop

class Queen(Piece):
    def __init__(self, type, colour, char, num):
        """Initializer for the Queen class"""
        super().__init__(type, colour, char, num)

    def moveable(self, board, to_char, to_num):
            """Determines whether the piece can move to a given square"""

            # A queen is just a bishop and a rook rolled into one piece
            #
            rook = Rook(self.type, self.colour, self.char, self.num)
            bishop = Bishop(self.type, self.colour, self.char, self.num)

            # Make sure at least one of thsee sub-pieces can move to that square
            #
            if(rook.moveable(board, to_char, to_num)):
                return True
            if(bishop.moveable(board, to_char, to_num)):
                return True

            return False
