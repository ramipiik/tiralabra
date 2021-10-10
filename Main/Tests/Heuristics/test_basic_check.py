"""Test heuristics.basic_check"""
# Execute the test class by running the following comman from command line:
# python3 -m unittest Tests.Heuristics.Test_basic_check

import unittest
from Heuristics.basic_check import basic_check
from tictactoe import TicTacToe


class TestHeuristicsBasicCheck(unittest.TestCase):
    # Tests whether Heuristics finds the correct combinations on a 3x3 board
    def test_basic_check_3(self):
        test_board = "XX-------"
        test_state = TicTacToe(test_board, False, 1, 2)
        score = basic_check(test_state, "X", 2)
        self.assertEqual(1, score)

        test_board = "XX-X-----"
        test_state = TicTacToe(test_board, False, 1, 2)
        score = basic_check(test_state, "X", 2)
        self.assertEqual(2, score)

        test_board = "XX-XX----"
        test_state = TicTacToe(test_board, False, 1, 2)
        score = basic_check(test_state, "X", 2)
        self.assertEqual(5, score)

        test_board = "-XX-XX---"
        test_state = TicTacToe(test_board, False, 1, 2)
        score = basic_check(test_state, "X", 2)
        self.assertEqual(5, score)

        test_board = "---XX-XX-"
        test_state = TicTacToe(test_board, False, 1, 2)
        score = basic_check(test_state, "X", 2)
        self.assertEqual(5, score)

        test_board = "----XX-XX"
        test_state = TicTacToe(test_board, False, 1, 2)
        score = basic_check(test_state, "X", 2)
        self.assertEqual(5, score)

    # Tests whether Heuristics finds the correct combinations on a 4x4 board
    # test_board = "----" + "----" + "----" + "----"
    def test_basic_check_4(self):
        test_board = "XXX--" + "XXX--" + "XXX--" + "-----" + "-----"
        test_state = TicTacToe(test_board, False, 1, 2)
        score = basic_check(test_state, "X", 3)
        self.assertEqual(60, score)

        test_board = "--OOO" + "--OOO" + "--OOO" + "-----" + "-----"
        test_state = TicTacToe(test_board, False, 1, 2)
        score = basic_check(test_state, "O", 3)
        self.assertEqual(60, score)

        test_board = "-----" + "-----" + "--XXX" + "--XXX" + "--XXX"
        test_state = TicTacToe(test_board, False, 1, 2)
        score = basic_check(test_state, "X", 3)
        self.assertEqual(60, score)

        test_board = "-----" + "-----" + "OOO--" + "OOO--" + "OOO--"
        test_state = TicTacToe(test_board, False, 1, 2)
        score = basic_check(test_state, "O", 3)
        self.assertEqual(60, score)

    # Tests whether Heuristics finds the correct combinations on a 5x5 board
    def test_basic_check_5(self):
        test_board = (
            "XXXX------"
            + "XXXX------"
            + "XXXX------"
            + "XXXX------"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
        )
        test_state = TicTacToe(test_board, False, 1, 2)
        score = basic_check(test_state, "X", 4)
        self.assertEqual(288, score)

        test_board = (
            "----------"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
            + "OOOO------"
            + "OOOO------"
            + "OOOO------"
            + "OOOO------"
        )
        test_state = TicTacToe(test_board, False, 1, 2)
        score = basic_check(test_state, "O", 4)
        self.assertEqual(288, score)

        test_board = (
            "----------"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
            + "------XXXX"
            + "------XXXX"
            + "------XXXX"
            + "------XXXX"
        )
        test_state = TicTacToe(test_board, False, 1, 2)
        score = basic_check(test_state, "X", 4)
        self.assertEqual(288, score)

        test_board = (
            "------OOOO"
            + "------OOOO"
            + "------OOOO"
            + "------OOOO"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
        )
        test_state = TicTacToe(test_board, False, 1, 2)
        score = basic_check(test_state, "O", 4)
        self.assertEqual(288, score)

    # Tests faulty input parameters
    def test_basic_check_faulty_input(self):
        with self.assertRaises(TypeError):
            basic_check()

        with self.assertRaises(TypeError):
            test_board = "XX-XX----"
            basic_check("X", 2)

        with self.assertRaises(AttributeError):
            test_board = "XX-XX----"
            basic_check(test_board, "X", 2)


if __name__ == "__main__":
    unittest.main()
