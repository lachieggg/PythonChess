
class Piece:
    def __init__(self, type, colour, char, num, filename):
        self.type = type        # eg. K for King, Q for Queen
        self.char = char        # horizontal position
        self.num = num          # vertical position
        self.colour = colour    # 'W' or 'B'
        self.filename = filename
