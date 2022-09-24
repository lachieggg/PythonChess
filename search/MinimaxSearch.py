from search.Node import Node

import copy 

class MinimaxSearch:
    def __init__(self):
        pass

    def minimaxSearch(self, board, depth, player):
        self.player = player
        self.tree = Node(board)
        self.board = board
        self.buildTree(self.tree, depth, player, True)
        print(len(self.tree.children))
        print(self.tree.children)
    
    def buildTree(self, node, depth, player, me):
        if(depth == 0):
            return
        # Build a Minimax search tree
        moves = self.player.get_possible_moves_for_player(node.board, me)
        for move in moves:
            n = Node()
            # TODO
            # Alpha beta pruning
            b = copy.deepcopy(self.board)
            b.move_piece(move[0], move[1])
            n.board = b
            print(move)
            n.move = move
            n.score = self.board.score(player.colour)
            node.children.append(n)
            self.buildTree(n, depth-1, player, not me)

        pass