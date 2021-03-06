from pieces.Piece import Piece
from Constants import *

class Bishop(Piece):
    def __init__(self, type, colour, char, num):
        """Initializer for the Bishop class"""
        super().__init__(type, colour, char, num)

    def moveable(self, board, _to):
            """Determines whether the piece can move to a given square"""
            to_char, to_num = _to[0], int(_to[1])

            if(not self.path_clear(board, to_char, to_num)):
                if(VERBOSE): print("Piece is in your way!")
                return False

            victim = board.get_squares_piece(to_char, to_num)
            # Attempting to take a piece
            if(victim):
                if(self.colour == victim.colour):
                    if(VERBOSE): print("You cannot take a piece on your own team!")
                    return False

            if(to_num > self.num):
                # UP
                if(to_char > self.char):
                    height = to_num - self.num + 1
                    for n in range(1, height):
                        char = chr(ord(self.char) + n)
                        num = self.num + n
                        if((char, num) == (to_char, to_num)):
                            return True
                else:
                    # LEFT
                    height = to_num - self.num + 1
                    for n in range(1, height):
                        char = chr(ord(self.char) - n)
                        num = self.num + n
                        if((char, num) == (to_char, to_num)):
                            return True
            else:
                # DOWN
                if(to_char > self.char):
                    # RIGHT
                    height = self.num - to_num + 1
                    for n in range(1, height):
                        char = chr(ord(self.char) + n)
                        num = self.num - n
                        if((char, num) == (to_char, to_num)):
                            return True
                else:
                    # LEFT
                    height = self.num - to_num + 1
                    for n in range(1, height):
                        char = chr(ord(self.char) - n)
                        num = self.num - n


                        if((char, num) == (to_char, to_num)):
                            return True

            return False
