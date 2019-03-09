from Characters.Players.Player import Player
class Dwarf(Player):
    def __init__(self, name):
        self.stats_attack = 2
        self.stats_defend = 2
        self.stats_body = 7
        self.stats_mind = 3
        self.stats_move = 2
        self.stats_weapon = "axe"
        self.stats_armour = None
        self.stats_name = name
        print("initialized")

