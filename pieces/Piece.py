import os
import sys

from Constants import *

class Piece:
    def __init__(self, type, colour, char, num):
        """Initializer for the Piece class"""
        self.type = type        # eg. K for King, Q for Queen
        self.char = char        # horizontal position
        self.num = num          # vertical position
        self.colour = colour    # 'W' or 'B'
        self.filename = self.get_filename()

    def get_position(self):
        return [self.char, self.num]

    def get_filename(self):
        return ASSETS_IMG_PATH + self.get_colour_name() + self.get_type_name() + '.png'

    def get_type_name(self):
        if self.type in PIECE_MAPPING.keys():
            return PIECE_MAPPING[self.type]

    def get_colour_name(self):
        return WHITE if self.colour == 'W' else BLACK

    def __str__(self):
        name = self.get_colour_name() + ' ' + self.get_type_name() + ' '
        pos = self.char + str(self.num)
        return name + pos
