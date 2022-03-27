from pieces import Piece

class Player:
    def __init__(self, colour):
        self.moved = False
        self.colour = colour

    def __str__(self):
        return "Player " + str(self.colour) + "\n"

    def get_possible_moves_for_player(self, board):
        """Get all the possible moves for a player"""
        moves = []
        for piece in board.pieces.values():
            if(piece.colour == self.colour):
                pieces_moves = piece.get_possible_moves_for_piece(board)
                moves += pieces_moves

        return moves