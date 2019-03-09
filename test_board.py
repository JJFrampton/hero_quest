#!/usr/bin/env python3
import pandas as pd

# NOTE not a production implimentation

board = pd.read_csv('hero_quest_board.csv', header=None)
board = board.replace('x','-')
board = board.replace('y','|')
board = board.replace('t',',')
board = board.replace('b','\'')
board = board.replace('j','+')
board = board.replace('o',' ')
print(board)
