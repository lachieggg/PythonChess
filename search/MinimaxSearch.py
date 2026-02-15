from search.Node import Node
import copy
import pygame
import sys

class MinimaxSearch:
    def __init__(self):
        self.transposition_table = {}
        self.nodes_visited = 0

    def minimaxSearch(self, board, depth, player, window=None):
        """Run minimax and return the best move for the given player."""
        self.player = player
        self.window = window
        self.transposition_table.clear()  # Clear cache for new search
        self.nodes_visited = 0
        root = Node(board)
        best_score = self._buildTree(root, depth, player.colour, True, float('-inf'), float('inf'))

        # Find the child whose score matches the best
        for child in root.children:
            if child.score == best_score:
                return child.move

        return None

    def _buildTree(self, node, depth, colour, maximizing, alpha, beta):
        """
        Build the minimax tree recursively with alpha-beta pruning.
        Returns the minimax score for this node.
        """
        self.nodes_visited += 1
        
        # Poll events every 300 nodes to keep UI responsive
        if self.nodes_visited % 300 == 0:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Accurate hit-testing using the Window reference
                    if self.window:
                        if self.window.is_quit_clicked(event.pos):
                            pygame.quit()
                            sys.exit()
                        # We don't handle PAUSE here as it's harder to sync state recursively,
                        # but we can at least make QUIT work perfectly.
                        if self.window.is_pause_clicked(event.pos):
                            pass

        # Early termination: Check depth first before generating moves
        if depth == 0:
            node.score = node.board.score(colour)
            return node.score
        
        # Check transposition table
        board_hash = self._hash_board(node.board)
        if board_hash in self.transposition_table:
            cached_entry = self.transposition_table[board_hash]
            if cached_entry['depth'] >= depth:
                return cached_entry['score']
        
        current_colour = colour if maximizing else ('W' if colour == 'B' else 'B')
        
        moves = self.player.get_possible_moves_for_player(node.board, maximizing)

        # Terminal state check
        if not moves:
            if node.board.is_in_check(current_colour):
                score = float('-inf') if maximizing else float('inf')
            else:
                score = 0  # Stalemate
            return score

        # Order moves for better pruning
        moves = self._order_moves(moves, node.board)

        if maximizing:
            best = float('-inf')
            for move in moves:
                b = copy.deepcopy(node.board)
                b.move_piece(move[0], move[1])
                child = Node(board=b, move=move)
                node.children.append(child)
                
                child_score = self._buildTree(child, depth - 1, colour, False, alpha, beta)
                best = max(best, child_score)
                alpha = max(alpha, best)
                
                if beta <= alpha:
                    break  # Beta cutoff
            
            node.score = best
        else:
            best = float('inf')
            for move in moves:
                b = copy.deepcopy(node.board)
                b.move_piece(move[0], move[1])
                child = Node(board=b, move=move)
                node.children.append(child)
                
                child_score = self._buildTree(child, depth - 1, colour, True, alpha, beta)
                best = min(best, child_score)
                beta = min(beta, best)
                
                if beta <= alpha:
                    break  # Alpha cutoff
            
            node.score = best

        # Store in transposition table
        self.transposition_table[board_hash] = {
            'score': best,
            'depth': depth
        }
        
        return best

    def _order_moves(self, moves, board):
        """Order moves to improve alpha-beta pruning efficiency"""
        captures = []
        non_captures = []
    
        for move in moves:
            # move[1] is the destination position like "e4"
            target_pos = move[1]
            char = target_pos[0]
            num = int(target_pos[1])
            
            # Check if there's a piece at the destination
            target_piece = board.get_squares_piece(char, num)
            
            if target_piece is not None:
                captures.append(move)
            else:
                non_captures.append(move)
        
        return captures + non_captures

    def _hash_board(self, board):
        """
        Create a hash of the board state for transposition table.
        Uses a string representation of piece positions.
        """
        # Create a simple hash based on piece positions
        # You could implement Zobrist hashing for better performance
        pieces_str = []
        for piece in board.pieces.values():
            pieces_str.append(f"{piece.colour}{piece.type}{piece.char}{piece.num}")
        
        return hash(tuple(sorted(pieces_str)))