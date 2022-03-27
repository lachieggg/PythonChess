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
        self.value = PIECE_VALUES.get(self.type)

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
    
    def get_possible_moves_for_piece(self, board):
        """
        Get all the possible moves for the piece, 'simple and readable' edition.

        Simply iterates over all squares and uses the movable method to check.

        For more efficiency, we could limit the search to only the squares
        for which the individual pieces can actually reach, rather than checking
        every single square, since, for instance, a rook cannot ever travel 
        diagonally, so we can significantly limit the search space.

        However this would be less elegant than a single parent class implementation,
        and currently, efficiency is not the focus of this project.
        """
        moves = []
        curr_square = self.char + str(self.num)
        for future_square in SQUARES:
            if(VERBOSE): print(future_square)
            if(self.moveable(board, future_square[0], int(future_square[1]))):
                moves.append([curr_square, future_square])
                
        return moves

    def path_clear(self, board, to_char, to_num):
        """Determines if there is a piece in the path of the piece moving to the new square"""
        # Vertical move
        if(self.char == to_char):
            (start, end) = (self.num+1, to_num) if to_num > self.num else (to_num+1, self.num)
            for y in range(start, end):
                if(board.get_squares_piece(self.char, y)):
                    if(VERBOSE): print("Piece found at position " + self.char + " " + str(y))
                    return False
        elif(self.num == to_num):
            # Horizontal move
            (start, end) = (ord(self.char)+1, ord(to_char)) if ord(to_char) > ord(self.char) else (ord(to_char)+1, ord(self.char))
            for x in range(ord(self.char)+1, ord(to_char)):
                if(board.get_squares_piece(chr(x), self.num)):
                    return False
        else:
            # Diagonal
            if(to_num > self.num):
                # UP
                if(to_char > self.char):
                    height = to_num - self.num
                    for n in range(1, height):
                        char = chr(ord(self.char) + n)
                        num = self.num + n

                        if(board.get_squares_piece(char, num)):
                            return False
                else:
                    # LEFT
                    height = to_num - self.num
                    for n in range(1, height):
                        char = chr(ord(self.char) - n)
                        num = self.num + n
                        if(board.get_squares_piece(char, num)):
                            return False
            else:
                # DOWN
                if(to_char > self.char):
                    # RIGHT
                    height = self.num - to_num
                    for n in range(1, height):
                        char = chr(ord(self.char) + n)
                        num = self.num - n
                        if(board.get_squares_piece(char, num)):
                            return False
                else:
                    # LEFT
                    height = self.num - to_num
                    for n in range(1, height):
                        char = chr(ord(self.char) - n)
                        num = self.num - n
                        if(board.get_squares_piece(char, num)):
                            return False
        return True
