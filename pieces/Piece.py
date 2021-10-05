import os
import sys

from Constants import *

class Piece:
    def __init__(self, type, colour, char, num):
        """Initializer for the Piece class"""
        self.type = type        # K for King, Q for Queen
        self.char = char        # horizontal position
        self.num = num          # vertical position
        self.colour = colour
        self.filename = self.get_filename()

    def get_position(self):
        """Returns the position as a list"""
        return [self.char, self.num]

    def get_filename(self):
        """Returns the filename of the image for the piece"""
        return ASSETS_IMG_PATH + self.colour + self.get_type_name() + '.png'

    def get_type_name(self):
        """Return the type of piece"""
        if self.type in PIECE_MAPPING.keys():
            return PIECE_MAPPING[self.type]

    def __str__(self):
        """Represent the piece object as a string"""
        name = self.colour + ' ' + self.get_type_name() + ' '
        pos = self.char + str(self.num)
        return name + pos
