# Execute the test class by running the following comman from command line:
# python3 -m unittest -v Tests.Test_parameters

from parameters import how_much_to_win, closeness_weight, LARGE_NUMBER
from tictactoe import TicTacToe
import unittest
from unittest.mock import patch


class Test_parameters_class(unittest.TestCase):
    def test_how_much_to_win(self):
        self.assertEquals(how_much_to_win(3), 3)
        self.assertEquals(how_much_to_win(5), 4)
        self.assertEquals(how_much_to_win(7), 4)
        self.assertEquals(how_much_to_win(10), 5)
        self.assertEquals(how_much_to_win(15), 5)
        self.assertEquals(how_much_to_win(20), 5)
        self.assertEquals(how_much_to_win(100), 5)
        self.assertEquals(how_much_to_win(0), 5)
        self.assertEquals(how_much_to_win(-1), 5)
        self.assertEquals(how_much_to_win("-"), 5)

        with self.assertRaises(TypeError):
            how_much_to_win()

        with self.assertRaises(TypeError):
            how_much_to_win(3, 4)

    def test_get_max_depth(self):
        board = "XXX------"
        node = TicTacToe(board, False, 1, 2)
        self.assertEquals(node.get_max_depth(), 0)

        node = TicTacToe(board, False, 2, 2)
        self.assertEquals(node.get_max_depth(), LARGE_NUMBER)


        board = "-------------------------"
        node = TicTacToe(board, False, 2, 2)
        self.assertEquals(node.get_max_depth(), 4)


        board = "------------------------------"
        node = TicTacToe(board, False, 2, 2)
        self.assertEquals(node.get_max_depth(), 3)

        board = "------------------------------------------------------------"
        node = TicTacToe(board, False, 2, 2)
        self.assertEquals(node.get_max_depth(), 2)

        with self.assertRaises(TypeError):
            node.get_max_depth(1)

        with self.assertRaises(TypeError):
            node.get_max_depth(3, 4)

    def test_closeness_weight(self):
        self.assertEquals(closeness_weight(2), 0.25)
        self.assertEquals(closeness_weight(1), 0)
        self.assertEquals(closeness_weight(0), 0)
        self.assertEquals(closeness_weight(-1), 0)
        self.assertEquals(closeness_weight("-"), 0)

        with self.assertRaises(TypeError):
            closeness_weight()

        with self.assertRaises(TypeError):
            closeness_weight(3, 4)


if __name__ == "__main__":
    unittest.main()
