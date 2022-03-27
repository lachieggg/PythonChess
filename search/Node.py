class Node:
    def __init__(self, value, children, move, pieces):
        self.value = value
        self.children = children
        self.move = move
        self.pieces = pieces
    
    def generate_children(self):
        pass