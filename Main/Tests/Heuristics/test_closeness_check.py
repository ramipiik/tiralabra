# Execute the test class by running the following comman from command line:
# python3 -m unittest Tests.Heuristics.Test_closeness_check

import unittest
from unittest.mock import patch
from Heuristics.closeness_check import closeness_check
from tictactoe import TicTacToe


class Test_closeness_check_class(unittest.TestCase):
    def test_closeness(self):
        test_board = "---------"
        test_state = TicTacToe(test_board, False, 1, 2)
        result = closeness_check(test_state, "X")
        self.assertEqual(result, 0)

        test_board = "---OX----"
        test_state = TicTacToe(test_board, False, 1, 2)
        result = closeness_check(test_state, "X")
        self.assertEqual(result, 0)

        test_board = "XXXXXXXXX"
        test_state = TicTacToe(test_board, False, 1, 2)
        result = closeness_check(test_state, "X")
        self.assertAlmostEqual(result, 0.8888, 3)

        test_board = "XXXXXXXXX"
        test_state = TicTacToe(test_board, False, 1, 2)
        result = closeness_check(test_state, "O")
        self.assertEqual(result, 0)

        test_board = "OOOOOOOOO"
        test_state = TicTacToe(test_board, False, 1, 2)
        result = closeness_check(test_state, "X", True)
        self.assertAlmostEqual(result, 0.8888, 3)

        test_board_1 = "X-------X"
        test_board_2 = "---XX----"
        test_state_1 = TicTacToe(test_board_1, False, 1, 2)
        test_state_2 = TicTacToe(test_board_2, False, 1, 2)
        result_1 = closeness_check(test_state_1, "X")
        result_2 = closeness_check(test_state_2, "X")
        self.assertTrue(result_2 > result_1)

    # Tests faulty input parameters
    def test_faulty_inputs(self):
        with self.assertRaises(TypeError):
            closeness_check()

        with self.assertRaises(AttributeError):
            test_board = "XX-XX----"
            test_state = TicTacToe(test_board, False, 1, 2)
            closeness_check("X", test_state)

        with self.assertRaises(AttributeError):
            test_board = "XX-XX----"
            closeness_check(test_board, "X")


if __name__ == "__main__":
    unittest.main()
