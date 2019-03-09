from Characters.Players.Player import Player
class Barbarian(Player):
    def __init__(self, name):
        self.stats_attack = 3
        self.stats_defend = 2
        self.stats_body = 8
        self.stats_mind = 2
        self.stats_move = 2
        self.stats_weapon = "broadsword"
        self.stats_armour = None
        self.stats_name = name
        print("initialized")

