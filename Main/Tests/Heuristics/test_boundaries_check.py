# Execute the test class by running the following comman from command line:
# python3 -m unittest Tests.Heuristics.Test_boundaries_check

import unittest
from unittest.mock import patch
from Heuristics.boundaries_check import boundaries_check
from tictactoe import TicTacToe


class Test_boundaries_check_class(unittest.TestCase):
    def test_boundaries(self):
        test_board = "---------"
        test_state = TicTacToe(test_board, False, 1, 2)
        result = boundaries_check(test_state, "X")
        self.assertEqual(result, 0)

        test_board = "---" + "-X-" + "---"
        test_state = TicTacToe(test_board, False, 1, 2)
        result = boundaries_check(test_state, "X")
        self.assertAlmostEqual(result, 0.148, 3)

        test_board = "XXX" + "XXX" + "XXX"
        test_state = TicTacToe(test_board, False, 1, 2)
        result = boundaries_check(test_state, "X")
        self.assertAlmostEqual(result, 0.8888, 3)

        test_board = "XXX" + "XXX" + "XXX"
        test_state = TicTacToe(test_board, False, 1, 2)
        result = boundaries_check(test_state, "o")
        self.assertEqual(result, 0)

        test_board = "OOO" + "OXO" + "OOO"
        test_state = TicTacToe(test_board, False, 1, 2)
        result = boundaries_check(test_state, "X")
        self.assertAlmostEqual(result, 0.148, 3)

        test_board = "OOO" + "OXO" + "OOO"
        test_state = TicTacToe(test_board, False, 1, 2)
        result = boundaries_check(test_state, "")
        self.assertEqual(result, 0)

    # Tests faulty input parameters
    def test_faulty_inputs(self):
        with self.assertRaises(TypeError):
            boundaries_check()

        with self.assertRaises(AttributeError):
            test_board = "XX-XX----"
            test_state = TicTacToe(test_board, False, 1, 2)
            boundaries_check("X", test_state)

        with self.assertRaises(AttributeError):
            test_board = "XX-XX----"
            boundaries_check(test_board, "X")


if __name__ == "__main__":
    unittest.main()
