from pieces.Piece import Piece

class Rook(Piece):
    def __init__(self, type, colour, char, num):
        """Initializer for the Rook class"""
        super().__init__(type, colour, char, num)


    def moveable(self, board, to_char, to_num):
            """Determines whether the piece can move to a given square"""

            char = self.char
            num = self.num

            if(not self.path_clear(board, to_char, to_num)):
                print("Piece is in your way!")
                return False

            if(not self.num == to_num):
                if(not self.char == to_char):
                    return False

            victim = board.get_squares_piece(to_char, to_num)
            # Attempting to take a piece
            if(victim):
                if(self.colour == victim.colour):
                    print("You cannot take a piece on your own team!")
                    return False

            return True
