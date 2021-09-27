from pieces.Piece import Piece
from pieces.King import King
from pieces.Queen import Queen
from pieces.Rook import Rook
from pieces.Bishop import Bishop
from pieces.Knight import Knight
from pieces.Pawn import Pawn
from Constants import *

class PieceFactory:
    def __init__(self):
        self.horizontals =  CHARS
        self.verticals =    NUMS
        self.pieces =       {}
        self.create_pieces()

    def __str__(self):
        str = ''
        for piece in self.pieces:
            str += str(piece)
        return str

    def create_piece(self, type, colour, char, num):
        if(type == 'K'):
            piece = King(type, colour, char, num)
        elif(type == 'Q'):
            piece = Queen(type, colour, char, num)
        elif(type == 'B'):
            piece = Bishop(type, colour, char, num)
        elif(type == 'H'):
            piece = Knight(type, colour, char, num)
        elif(type == 'R'):
            piece = Rook(type, colour, char, num)
        elif(type == 'P'):
            piece = Pawn(type, colour, char, num)
        else:
            return

        key = char + str(num)
        self.pieces[key] = piece

    def get_pieces(self):
        return self.pieces

    def create_pieces(self):
        for piece_data in PIECES_DATA:
            self.create_piece(*piece_data)
