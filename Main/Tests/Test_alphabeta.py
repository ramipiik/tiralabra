# Execute the test class by running the following comman from command line:
# python3 -m unittest -v Tests.Test_alphabeta

import unittest
from unittest.mock import patch
from alphabeta import alpha_beta_value, max_value, min_value
from tictactoe import TicTacToe
from parameters import LARGE_NUMBER, alpha, beta


class Test_alphabeta_class(unittest.TestCase):
    @patch("alphabeta.max_value")
    @patch("alphabeta.min_value")
    def test_alpha_beta_value(self, mock_min_value, mock_max_value):
        mock_min_value.return_value = "min"
        mock_max_value.return_value = "max"
        custom_board = 9 * "-"
        state1 = TicTacToe(custom_board, False, 1, 1)
        state2 = TicTacToe(custom_board, True, 1, 1)

        self.assertEqual(alpha_beta_value(state1), "min")
        self.assertEqual(alpha_beta_value(state2), "max")

        with self.assertRaises(TypeError):
            alpha_beta_value(1, 2, 3)

    def test_min_win(self):
        test_board = "----O----"
        node = TicTacToe(test_board, False, 1, 1)
        depth = 0
        result = min_value(node, alpha, beta, depth)
        self.assertEqual(result, -1)

    def test_max_win(self):
        test_board = "X--------"
        node = TicTacToe(test_board, True, 1, 1)
        depth = 0
        result = max_value(node, alpha, beta, depth)
        self.assertEqual(result, 1)

    def test_draw_1(self):
        test_board = "---------"
        node = TicTacToe(test_board, True, 2, 1)
        depth = 0
        result = max_value(node, alpha, beta, depth)
        self.assertEqual(result, 0)

    def test_draw_2(self):
        test_board = "---------"
        node = TicTacToe(test_board, False, 2, 1)
        depth = 0
        result = min_value(node, alpha, beta, depth)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
