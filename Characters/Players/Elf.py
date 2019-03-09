from Characters.Players.Player import Player
class elf(Player):
    def __init__(self, name):
        self.stats_attack = 2
        self.stats_defend = 2
        self.stats_body = 6
        self.stats_mind = 4
        self.stats_move = 2
        self.stats_weapon = "shortsword"
        self.stats_armour = None
        self.stats_name = name
        print("initialized")

