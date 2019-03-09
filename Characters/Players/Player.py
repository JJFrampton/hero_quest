from Characters.Character import Character
from Actions.Dice import Dice
class Player(Character):
    d = Dice()
    def move(self):
        return self.d.roll('r', self.stats_move)

# might be better to have the character class inheret the dice class?

