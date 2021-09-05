from pieces.Piece import Piece
from pieces.King import King
from pieces.Queen import Queen
from pieces.Rook import Rook
from pieces.Bishop import Bishop
from pieces.Knight import Knight
from pieces.Pawn import Pawn

class PieceFactory:
    def __init__(self):
        self.horizontals =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.verticals =    [1, 2, 3, 4, 5, 6, 7, 8]
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
        initial_pieces_data = [
            ['K', 'W', 'E', 1],
            ['Q', 'W', 'D', 1],
            ['R', 'W', 'A', 1],
            ['R', 'W', 'H', 1],
            ['H', 'W', 'B', 1],
            ['H', 'W', 'G', 1],
            ['B', 'W', 'C', 1],
            ['B', 'W', 'F', 1],
            ['P', 'W', 'A', 2],
            ['P', 'W', 'B', 2],
            ['P', 'W', 'C', 2],
            ['P', 'W', 'D', 2],
            ['P', 'W', 'E', 2],
            ['P', 'W', 'F', 2],
            ['P', 'W', 'G', 2],
            ['P', 'W', 'H', 2],
            ['K', 'B', 'E', 8],
            ['Q', 'B', 'D', 8],
            ['R', 'B', 'A', 8],
            ['R', 'B', 'H', 8],
            ['H', 'B', 'B', 8],
            ['H', 'B', 'G', 8],
            ['B', 'B', 'C', 8],
            ['B', 'B', 'F', 8],
            ['P', 'B', 'A', 7],
            ['P', 'B', 'B', 7],
            ['P', 'B', 'C', 7],
            ['P', 'B', 'D', 7],
            ['P', 'B', 'E', 7],
            ['P', 'B', 'F', 7],
            ['P', 'B', 'G', 7],
            ['P', 'B', 'H', 7]
        ]
        for piece_data in initial_pieces_data:
            self.create_piece(*piece_data)
