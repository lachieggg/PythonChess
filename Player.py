import copy 

from pieces import Piece

from search.MinimaxSearch import MinimaxSearch

from Constants import DEPTH

class Player:
    def __init__(self, colour):
        self.moved = False
        self.colour = colour
        self.minimax = MinimaxSearch()
        
    def __str__(self):
        """Represent the player as a string"""
        return "Player " + str(self.colour) + "\n"

    def get_possible_moves_for_player(self, board, me=True):
        """
        Get all the possible moves for a player
        'me' => True will return this player's moves, 
        'me' => False will return opponent's movies
        """
        moves = []
        for piece in board.pieces.values():
            if((piece.colour == self.colour) == me):
                pieces_moves = piece.get_possible_moves_for_piece(board)
                moves += pieces_moves

        return moves

    def get_greedy_move_for_player(self, board):
        """Greedy approach for best move one move ahead"""
        moves = self.get_possible_moves_for_player(board)

        best_move = None

        for move in moves:
            # Create a new board to evaluate the score for
            # this particular move
            b = copy.deepcopy(board)

            _from = move[0]
            _to = move[1]

            b.move_piece(_from, _to)
            score = b.score(self.colour)
            if(not best_move or score > best_score ):
                best_score = score
                best_move = move
            
        print("Best score = {}".format(best_score))
        return best_move
    
    def get_minimax_best_move_for_player(self, board, window=None):
        """Minimax approach for best move N moves ahead"""
        return self.minimax.minimaxSearch(board, DEPTH, self, window)
