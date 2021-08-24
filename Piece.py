
class Piece:
    def __init__(self, type, team, char, num):
        self.type = type
        self.team = team
        self.char = char
        self.num = num
        self.colour = "White" if team else "Black"
        pass

    def __repr__(self):
        str = self.colour + ' '
        str += self.type + ' ' + repr(self.char) + ' ' + repr(self.num) + '\n'
        return str
