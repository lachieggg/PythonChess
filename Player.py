from pieces import Piece

class Player:
    def __init__(self, team):
        self.team = team
        self.colour = "White" if team == 'W' else "Black"

    def __repr__(self):
        return "Player " + str(self.colour) + "\n"
