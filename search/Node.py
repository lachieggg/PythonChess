class Node:
    def __init__(self, board=None, move=None, children=None):
        self.board = board
        self.move = move
        self.children = children if children is not None else []
        self.score = None

    def __repr__(self):
        return str(self.move) + " " + str(self.score)