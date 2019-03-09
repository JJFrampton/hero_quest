from Actions.Dice import Dice
class Character:
    d = Dice()
    def __init__(self, position):
        print("initializing")
    def attack(self):
        print("attacking")
    def defend(self):
        print("defending")
        # this should be automatic response to being attacked
    def attack(self):
        return self.d.roll('w', self.stats_attack)
    def defend(self):
        return self.d.roll('w', self.stats_defend)
    def turn_start(self):
        # set booleans
        self.movement = 0
        self.moved = False
        self.actioned = False
        print("Start turn")
    def turn_end(self):
        # wipe out unused movement
        self.movement = 0
        print("End turn")
