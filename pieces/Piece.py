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
        self.moved = False      # whether or not a piece has moved previously

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

    def moveable(self, board, to_char, to_num):
        return False

    def piece_in_move_path(self, board, to_char, to_num):
        """Determines if there is a piece in the path of the piece moving to the new square"""
        # Vertical move
        if(self.char == to_char):
            (start, end) = (self.num+1, to_num) if to_num > self.num else (to_num+1, self.num)
            for y in range(start, end):
                if(board.get_squares_piece(self.char, y)):
                    print("Piece found at position " + self.char + " " + str(y))
                    return True
        # Horizontal move
        if(self.num == to_num):
            for x in range(ord(self.char)+1, ord(to_char)):
                if(board.get_squares_piece(ord(x), self.num)):
                    return True

        # Diagonal move
        for x in range(ord(self.char)+1, ord(to_char)):
            for y in range(self.num+1, to_num):
                if(board.get_squares_piece(ord(x), y)):
                    return True

        return False
