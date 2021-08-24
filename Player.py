from Piece import Piece

class Player:
    def __init__(self, team):
        self.team = team
        self.colour = "White" if team else "Black"

    def __repr__(self):
        return "Player " + str(self.colour) + "\n"
