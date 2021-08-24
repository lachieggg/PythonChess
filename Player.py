from Piece import Piece

class Player:
    def __init__(self, team):
        self.team = team
        self.setup_pieces()
        pass

    def setup_pieces(self):
        pawn = Piece('pawn', self.team, 1, 1)
        self.pieces = [pawn]

    def __repr__(self):
        str = "Player " + repr(self.team) + '\n'

        for piece in self.pieces:
            str += repr(piece)

        return '\n' + str
