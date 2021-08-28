from pieces.Piece import Piece

class Bishop(Piece):
    def __init__(self, type, colour, char, num):
        filename = 'WhiteBishop.png' if colour == 'W' else 'BlackBishop.png'

        super().__init__(type, colour, char, num, filename)
