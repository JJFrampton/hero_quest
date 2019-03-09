from Characters.Character import Character
class Player(Character):
    def movement_roll(self):
        Character.moved = True
        self.movement = Character.d.roll('r', self.stats_move)
