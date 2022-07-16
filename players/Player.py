import copy 

from pieces import Piece
from sys import maxsize as MAX_INT

class Player:
    def __init__(self, colour):
        self.moved = False
        self.colour = colour

    def __str__(self):
        """Represent the player as a string"""
        return "Player " + str(self.colour) + "\n"

    def get_possible_moves_for_player(self, board):
        """Get all the possible moves for a player"""
        moves = []
        for piece in board.pieces.values():
            if(piece.colour == self.colour):
                pieces_moves = piece.get_possible_moves_for_piece(board)
                moves += pieces_moves

        return moves

    def get_greedy_move_for_player(self, board):
        """Greedy approach for best move one move ahead"""
        moves = self.get_possible_moves_for_player(board)

        best_score = -MAX_INT
        best_move = None
        b = copy.deepcopy(board)

        for move in moves:
            # Create a new board to evaluate the score for
            # this particular move
            b = copy.deepcopy(board)

            _from = move[0]
            _to = move[1]

            b.move_piece(_from, _to)
            score = b.score(self.colour)
            if(score > best_score):
                best_score = score
                best_move = move
            

        print("Best score = {}".format(best_score))
        return best_move
    
    def get_minimax_best_move_for_player(self, board):
        pass