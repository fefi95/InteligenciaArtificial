"""
    Universidad Simon Bolivar
    CI-5438 - Inteligencia Artificial
    Edward Fernandez 10-11121
    Carlos Ferreira 11-10323
    Stefani Castellanos 11-11394

    Description:

"""

import unittest
from heuristic import *

class TestHeuristics(unittest.TestCase):

    def setUp(self):
		# See doc/test_board.png for a clearer version of this board.
        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 7, 1, 0, 0, 0, 0],
            [0, 1, 1, 7, 7, 7, 1, 0, 0, 2],
            [0, 1, 1, 0, 6, 7, 6, 6, 6, 2],
            [1, 1, 1, 7, 6, 7, 4, 4, 2, 2],
            [1, 1, 1, 0, 6, 7, 4, 1, 2, 2],
            [1, 1, 6, 6, 6, 7, 4, 2, 2, 2],
        ]

    def test_agregate_height(self):
        self.assertEqual(aggregateHeight(self.board), 48)

    def test_complete_lines(self):
        self.assertEqual(completeLines(self.board), 2)

    def test_holes(self):
        self.assertEqual(holes(self.board), 2)

    def test_bumpiness(self):
        self.assertEqual(bumpiness(self.board), 6)

	# def test_num_holes(self):
	# 	self.assertEqual(num_holes(self.board), 22)
    #
	# def test_num_blocks_above_holes(self):
	# 	self.assertEqual(num_blocks_above_holes(self.board), 25)
    #
	# def test_num_gaps(self):
	# 	self.assertEqual(num_gaps(self.board), 7)
    #
	# def test_max_height(self):
	# 	self.assertEqual(max_height(self.board), 13)
    #
	# def test_avg_height(self):
	# 	total_height = 13*2 + 12*1 + 11*1 + 10*1 + 9*2 + 8*2 + 7*3 + 6*4 + 5*3 + 4*5 + 3*8 + 2*5 + 1*5 + 0*6
	# 	self.assertEqual(avg_height(self.board), total_height / num_blocks(self.board))
    #
	# def test_num_blocks(self):
	# 	self.assertEqual(num_blocks(self.board), 48)

if __name__ == '__main__':
		unittest.main()
