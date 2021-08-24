
class Board:
    def __init__(self, players):
        self.players = players
        pass

    def __repr__(self):
        str = ''
        for player in self.players:
            str += repr(player)

        return str
