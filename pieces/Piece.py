import os
import sys
import copy

from Constants import *

class Piece:
    def __init__(self, type, colour, char, num):
        """Initializer for the Piece class"""
        self.type = type        # K for King, Q for Queen
        self.char = char        # horizontal position
        self.num = num          # vertical position
        self.colour = colour    # colour of the piece
        self.moved = False      # whether or not a piece has moved previously
        self.value = PIECE_VALUES.get(self.type)
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
    
    def get_possible_moves_for_piece(self, board):
        """
        Get all the possible moves for the piece, filtering out moves that leave
        the King in check.
        """
        moves = []
        curr_square = self.char + str(self.num)
        
        # 1. Find all pseudo-legal moves (geometric/rule-based)
        pseudo_moves = []
        for future_square in SQUARES:
            if(self.moveable(board, future_square)):
                pseudo_moves.append(future_square)
        
        # 2. Filter out moves that result in check
        for move_to in pseudo_moves:
            # Create a deepcopy to simulate the move
            temp_board = copy.deepcopy(board)
            
            # Execute the move on the temp board
            # move_piece might print if VERBOSE is on, so we accept that risk
            # given it's a simple project without logging config
            temp_board.move_piece(curr_square, move_to)
            
            # Check if this move leaves our King in check
            if not temp_board.is_in_check(self.colour):
                moves.append([curr_square, move_to])
                
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
            for x in range(start, end):
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
