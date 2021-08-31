from pieces import Piece

class Player:
    def __init__(self, colour):
        self.moved = False
        self.colour = colour

    def __str__(self):
        return "Player " + str(self.colour) + "\n"

    def move_piece(self, piece, position):
        if not piece.colour == self.colour:
            return

        piece.char = position.get('char')
        piece.num = position.get('num')
