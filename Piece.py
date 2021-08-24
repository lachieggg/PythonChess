
class Piece:
    def __init__(self, type, team, x, y):
        self.type = type
        self.team = team
        self.x = x
        self.y = y
        pass

    def __repr__(self):
        str = self.type + ' ' + repr(self.x) + ' ' + repr(self.y)
        return str
