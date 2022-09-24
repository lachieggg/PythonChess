class Node:
    def __init__(self, board=None, move=None, children=[]):
        self.board = board
        self.move = move
        self.children = children