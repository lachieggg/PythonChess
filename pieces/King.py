from pieces.Piece import Piece
from Constants import *

class King(Piece):
    def __init__(self, type, colour, char, num):
        """Initializer for the King class"""
        super().__init__(type, colour, char, num)
        pass

    def moveable(self, board, _to):
        """Determines whether the piece can move to a given square"""
        to_char, to_num = _to[0], int(_to[1])
        diff_char = abs(ord(self.char) - ord(to_char))
        diff_num = abs(self.num - to_num)
        
        # 1. Standard King move (1 square in any direction)
        if diff_char <= 1 and diff_num <= 1:
            # Check for friendly piece at target
            victim = board.get_squares_piece(to_char, to_num)
            if victim and victim.colour == self.colour:
                return False
            return True

        # 2. Castling
        if not self.moved and diff_num == 0 and diff_char == 2:
            return self.can_castle(board, _to)

        return False

    def can_castle(self, board, _to):
        """Check if castling is legal"""
        # king shouldn't be in check
        if board.is_in_check(self.colour):
            return False

        to_char = _to[0]
        is_kingside = (to_char == 'G')
        rook_char = 'H' if is_kingside else 'A'
        rook = board.get_squares_piece(rook_char, self.num)

        # Rook must exist, be a Rook, and not have moved
        from pieces.Rook import Rook
        if not rook or not isinstance(rook, Rook) or rook.moved:
            return False

        # Path must be clear
        step = 1 if is_kingside else -1
        # Kingside: F, G. Queenside: B, C, D. 
        # But we only need to check the squares the king passes through for check.
        # Check all squares between King and Rook for pieces
        check_chars = ['F', 'G'] if is_kingside else ['D', 'C', 'B']
        for c in check_chars:
            if board.get_squares_piece(c, self.num):
                return False

        # King must not pass through or end in check
        test_chars = ['F', 'G'] if is_kingside else ['D', 'C']
        import copy
        for c in test_chars:
            temp_board = copy.deepcopy(board)
            # Move king to the intermediate square
            king_ref = temp_board.pieces.get(self.char + str(self.num))
            temp_board.pieces[c + str(self.num)] = king_ref
            del temp_board.pieces[self.char + str(self.num)]
            king_ref.char = c
            if temp_board.is_in_check(self.colour):
                return False

        return True
