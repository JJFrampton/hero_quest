#!/usr/bin/env python
import unittest
from Characters.Players.Elf import Elf
from Resources.Board import Board


class TestInit(unittest.TestCase):
    def setUp(self):
        board = Board(4,4)
        self.elf = Elf("Mr. Anderson", [0,0], board)
    def tearDown(self):
        del self.elf
    # init
    def test_init_name(self):
        self.assertEqual(self.elf.stats_name, "Mr. Anderson")
    def test_init_tag(self):
        self.assertEqual(self.elf.tag, "M")
    def test_init_position(self):
        self.assertEqual(self.elf.position, [0,0])
    def test_init_board_position(self):
        self.assertEqual(self.elf.board.map[self.elf.position[0]][self.elf.position[1]], self.elf.tag)

class TestAction(unittest.TestCase):
    def setUp(self):
        board = Board(4,4)
        self.elf = Elf("Mr. Anderson", [0,0], board)
    def tearDown(self):
        del self.elf
    # action
    def test_action_turn_start(self):
        self.elf.turn_start()
        self.assertEqual(self.elf.movement, 0)
    def test_action_movement(self):
        old_position = self.elf.position.copy()
        self.elf.movement_roll()
        self.elf.move_right(1)
        self.assertEqual(self.elf.board.map[old_position[0]][old_position[1]], 'o')
        self.assertEqual(self.elf.board.map[self.elf.position[0]][self.elf.position[1]], self.elf.tag)

if __name__ == '__main__':
    unittest.main()
