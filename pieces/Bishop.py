from pieces.Piece import Piece

class Bishop(Piece):
    def __init__(self, type, colour, char, num):
        """Initializer for the Bishop class"""
        super().__init__(type, colour, char, num)

    def moveable(self, board, to_char, to_num):
            """Determines whether the piece can move to a given square"""

            abs_delta_x = abs(ord(to_char) - ord(self.char))
            abs_delta_y = abs(to_num - self.num)

            # Knights can move to positions where the absolute
            # value of the sum of the differences between the squares
            # is exactly 3
            if(abs_delta_x + abs_delta_y == 3):
                return True
            return False
