class Node:
    def __init__(self, board=None, move=None, children=[]):
        self.board = board
        self.move = move
        self.children = children
        self.score = None

    def __repr__(self):
        return str(self.move) + " " + str(self.score)