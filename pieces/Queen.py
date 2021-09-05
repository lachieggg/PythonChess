from pieces.Piece import Piece

class Queen(Piece):
    def __init__(self, type, colour, char, num):
        """Initializer for the Queen class"""
        super().__init__(type, colour, char, num)
