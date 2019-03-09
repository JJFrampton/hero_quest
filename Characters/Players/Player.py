from Characters.Character import Character
class Player(Character):
    def move(self):
        return roll('r', self.stats_move)

