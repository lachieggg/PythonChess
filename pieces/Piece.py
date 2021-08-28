import os

ASSETS_PATH = os.getcwd() + '/assets/'

class Piece:
    def __init__(self, type, colour, char, num):
        self.type = type        # eg. K for King, Q for Queen
        self.char = char        # horizontal position
        self.num = num          # vertical position
        self.colour = colour    # 'W' or 'B'
        self.filename = self.get_filename()

    def get_position(self):
        return self.char + str(self.num)

    def get_filename(self):
        return ASSETS_PATH + self.get_colour_name() + self.get_type_name() + '.png'

    def get_type_name(self):
        mapping = {
        'K':'King',
        'Q':'Queen',
        'R':'Rook',
        'B':'Bishop',
        'H':'Horse',
        'P':'Pawn'
        }
        if self.type in mapping.keys():
            return mapping[self.type]

    def get_colour_name(self):
        return 'White' if self.colour == 'W' else 'Black'

    def __str__(self):
        name = self.get_colour_name() + ' ' + self.get_type_name() + ' '
        pos = self.char + str(self.num)
        return name + pos
