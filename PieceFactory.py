from pieces.Piece import Piece
from pieces.King import King
from pieces.Queen import Queen
from pieces.Castle import Castle
from pieces.Bishop import Bishop
from pieces.Knight import Knight
from pieces.Pawn import Pawn

class PieceFactory:
    def __init__(self):
        self.horizontals =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.verticals =    [1, 2, 3, 4, 5, 6, 7, 8]

    def __repr__(self):
        pass

    def create_init_pieces():
        pieces = []
        # Whites
        pieces.append(create_piece('K', 'W', 'E', 1))
        pieces.append(create_piece('Q', 'W', 'D', 1))
        pieces.append(create_piece('R', 'W', 'A', 1))
        pieces.append(create_piece('R', 'W', 'H', 1))
        pieces.append(create_piece('H', 'W', 'B', 1))
        pieces.append(create_piece('H', 'W', 'G', 1))
        pieces.append(create_piece('B', 'W', 'C', 1))
        pieces.append(create_piece('B', 'W', 'F', 1))
        # Blacks
        pieces.append(create_piece('K', 'B', 'E', 8))
        pieces.append(create_piece('Q', 'B', 'D', 8))
        pieces.append(create_piece('R', 'B', 'A', 8))
        pieces.append(create_piece('R', 'B', 'H', 8))
        pieces.append(create_piece('H', 'B', 'B', 8))
        pieces.append(create_piece('H', 'B', 'G', 8))
        pieces.append(create_piece('B', 'B', 'C', 8))
        pieces.append(create_piece('B', 'B', 'F', 8))
        # Pawns
        for x in self.horizontals:
            pieces.append(create_piece('P', 'W', x, 2))
            pieces.append(create_piece('P', 'B', x, 7))

        return pieces

    def create_piece(self, colour, type, char, num):
        if(type == "K"):
            piece = King(type, colour, char, num)
        elif(type == "Q"):
            piece = Queen(type, colour, char, num)
        elif(type == "B"):
            piece = Bishop(type, colour, char, num)
        elif(type == "H"):
            piece = Knight(type, colour, char, num)
        elif(type == "C"):
            piece = Castle(type, colour, char, num)
        elif(type == "P"):
            piece = Pawn(type, colour, char, num)
        else:
            raise Exception("No piece defined for letter {}".format(type))
        return piece


if __name__ == "__main__":
    pieceFactory = PieceFactory()
    king = pieceFactory.create_piece("W", "K", 1, 1)
    print(repr(king))
    print(king.type)
