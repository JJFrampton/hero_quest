from Actions.Dice import Dice
class Character:
    def __init__(self):
        print("initializing")
    def attack(self):
        print("attacking")
    def defend(self):
        print("defending")
        # this should be automatic response to being attacked
    def attack(self):
        return Dice.roll('w', self.stats_attack)
    def defend(self):
        return Dice.roll('w', self.stats_defend)
