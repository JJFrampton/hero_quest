#!/usr/bin/env python3

import random

def roll_red(dimensions):
    return random.randint(1, dimensions)

def roll_white():
    # 3 white skull
    # 2 shield
    # 1 black skull
    roll = random.randint(1, 6)
    result = "white_skull"
    if roll == 1:
        result = "black_skull"
    if roll == 2 or roll == 3:
        result = "shield"
    return result

def roll(color, amount):
    if color == 'w' or color == 'white':
        result = {}
        for i in range(amount):
            r = roll_white()
            if r in result:
                result[r] += 1
            else:
                result[r] = 1
        return result
    if color == 'r' or color == 'red':
        result = 0
        for i in range(amount):
            result += roll_red(6)
        return result

