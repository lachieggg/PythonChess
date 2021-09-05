from pieces.Piece import Piece

class Pawn(Piece):
    def __init__(self, type, colour, char, num):
        """Initializer for the Pawn class"""
        super().__init__(type, colour, char, num)
