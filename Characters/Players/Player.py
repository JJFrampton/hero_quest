class Player(Character):
    def move(self):
        return roll('r', self.stats_move)

