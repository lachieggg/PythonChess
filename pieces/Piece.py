
class Piece:
    def __init__(self, type, colour, char, num):
        self.type = type        # eg. K for King, Q for Queen
        self.char = char        # horizontal position
        self.num = num          # vertical position
        self.colour = colour    # 'W' or 'B'

    def __repr__(self):
        str = self.colour + ' '
        str += self.type + ' ' + repr(self.char) + ' ' + repr(self.num) + '\n'
        return str
