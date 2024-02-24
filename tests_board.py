import unittest
from board import Board


class TestBoard(unittest.TestCase):
    """ Test Cases for the Board class in board.py """
    def test_check_for_win_example_01(self):
        """ starting board. game continues """
        board = Board(player_x='playerX', player_o='playerO')
        board.board = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
        actual = board.check_for_win()
        expected = True
        self.assertEqual(actual, expected)

    def test_check_for_win_example_02(self):
        """ col 1 win. game ends """
        board = Board(player_x='playerX', player_o='playerO')
        board.board = [['X', 'B', 'C'], ['X', 'E', 'F'], ['X', 'H', 'I']]
        actual = board.check_for_win()
        expected = False
        self.assertEqual(actual, expected)

    def test_check_for_win_example_03(self):
        """ col 2 win. game ends """
        board = Board(player_x='playerX', player_o='playerO')
        board.board = [['A', 'X', 'C'], ['D', 'X', 'F'], ['G', 'X', 'I']]
        actual = board.check_for_win()
        expected = False
        self.assertEqual(actual, expected)

    def test_check_for_win_example_04(self):
        """ col 3 win. game ends """
        board = Board(player_x='playerX', player_o='playerO')
        board.board = [['A', 'B', 'O'], ['D', 'E', 'O'], ['G', 'H', 'O']]
        actual = board.check_for_win()
        expected = False
        self.assertEqual(actual, expected)

    def test_check_for_win_example_05(self):
        """ row 1 win. game ends """
        board = Board(player_x='playerX', player_o='playerO')
        board.board = [['O', 'O', 'O'], ['D', 'E', 'F'], ['G', 'H', 'I']]
        actual = board.check_for_win()
        expected = False
        self.assertEqual(actual, expected)

    def test_check_for_win_example_06(self):
        """ row 2 win. game ends """
        board = Board(player_x='playerX', player_o='playerO')
        board.board = [['A', 'X', 'C'], ['O', 'O', 'O'], ['G', 'H', 'I']]
        actual = board.check_for_win()
        expected = False
        self.assertEqual(actual, expected)

    def test_check_for_win_example_07(self):
        """ row 3 win. game ends """
        board = Board(player_x='playerX', player_o='playerO')
        board.board = [['A', 'B', 'C'], ['D', 'E', 'F'], ['O', 'O', 'O']]
        actual = board.check_for_win()
        expected = False
        self.assertEqual(actual, expected)

    def test_check_for_win_example_08(self):
        """ diag 1 win. game ends """
        board = Board(player_x='playerX', player_o='playerO')
        board.board = [['X', 'B', 'C'], ['D', 'X', 'F'], ['G', 'H', 'X']]
        actual = board.check_for_win()
        expected = False
        self.assertEqual(actual, expected)

    def test_check_for_win_example_09(self):
        """ diag 2 win. game ends """
        board = Board(player_x='playerX', player_o='playerO')
        board.board = [['A', 'B', 'O'], ['D', 'O', 'F'], ['O', 'H', 'I']]
        actual = board.check_for_win()
        expected = False
        self.assertEqual(actual, expected)

    def test_check_for_win_example_10(self):
        """ cats - no remaining valid positions. game ends """
        board = Board(player_x='playerX', player_o='playerO')
        board.valid_positions = []
        actual = board.check_for_win()
        expected = False
        self.assertEqual(actual, expected)
