"""Test heuristics.mustwin_check module"""
# Execute the test class by running the following comman from command line:
# python3 -m unittest Tests.Heuristics.Test_mustwin_check

import unittest
from Heuristics.mustwin_check import check_mustwins
from tictactoe import TicTacToe


class TestMustwinCheck(unittest.TestCase):
    def test_mustwin(self):
        test_board = "---------"
        test_state = TicTacToe(test_board, False, 1, 2)
        result = check_mustwins(test_state, "X", 2)
        self.assertEqual(result, 0)

        test_board = "---XX----"
        test_state = TicTacToe(test_board, False, 1, 2)
        result = check_mustwins(test_state, "X", 2)
        self.assertEqual(result, 0)

        test_board = "-XXX-" + "-----" + "-----" + "-----" + "-----"
        test_state = TicTacToe(test_board, False, 1, 2)
        result = check_mustwins(test_state, "X", 3)
        self.assertEqual(result, 1)

        test_board = "-----" + "-X--_" + "-X---" + "-X---" + "-----"
        test_state = TicTacToe(test_board, False, 1, 2)
        result = check_mustwins(test_state, "X", 3)
        self.assertEqual(result, 1)

        test_board = "-----" + "-X---" + "--X--" + "---X-" + "-----"
        test_state = TicTacToe(test_board, False, 1, 2)
        result = check_mustwins(test_state, "X", 3)
        self.assertEqual(result, 1)

        test_board = "-----" + "---X-" + "--X--" + "-X---" + "-----"
        test_state = TicTacToe(test_board, False, 1, 2)
        result = check_mustwins(test_state, "X", 3)
        self.assertEqual(result, 1)

        test_board = "-XXX-" + "-----" + "-----" + "-----" + "-----"
        test_state = TicTacToe(test_board, False, 1, 2)
        result = check_mustwins(test_state, "O", 3)
        self.assertEqual(result, 0)

        test_board = (
            "---XXXX---"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
        )
        test_state = TicTacToe(test_board, False, 1, 2)
        result = check_mustwins(test_state, "X", 4)
        self.assertEqual(result, 1)

    # Tests faulty input parameters
    def test_faulty_inputs(self):
        with self.assertRaises(TypeError):
            check_mustwins()

        with self.assertRaises(TypeError):
            test_board = "XX-XX----"
            test_state = TicTacToe(test_board, False, 1, 2)
            check_mustwins(test_state, "X")

        with self.assertRaises(AttributeError):
            test_board = "XX-XX----"
            check_mustwins(test_board, "X", 2)


if __name__ == "__main__":
    unittest.main()
