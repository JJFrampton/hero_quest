class Board:
    def __init__(self,y,x):
        self.map = [ ['o'] * x for i in range(y) ]
        print(map)
    def update_position(self, old_position, new_position, character):
        print('here')
        y = old_position[0]
        x = old_position[1]
        print("old %s %s" %(y, x))
        self.map[y][x] = 'o'
        y = new_position[0]
        x = new_position[1]
        print("new %s %s" %(y, x))
        self.map[y][x] = character.tag

# board = [
#         ['o','o','o','o'],
#         ['o','o','o','o'],
#         ['o','o','o','o'],
#         ['o','o','o','o']
#       ]
