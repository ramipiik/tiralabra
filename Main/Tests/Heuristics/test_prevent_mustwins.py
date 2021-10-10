"""Test heuristics.prevent_mustwins module"""
# Execute the test class by running the following comman from command line:
# python3 -m unittest Tests.Heuristics.Test_prevent_mustwins

import unittest
from Heuristics.prevent_mustwins import prevent_mustwins
from tictactoe import TicTacToe


class TestPreventMustwins(unittest.TestCase):
    def test_mustwin(self):
        test_board = (
            "---XXX----"
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
        result = prevent_mustwins(test_state, "X", 4)
        self.assertEqual(result, 2)

        test_board = (
            "---XX-X---"
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
        result = prevent_mustwins(test_state, "X", 4)
        self.assertEqual(result, 1)

        test_board = (
            "---X-XX---"
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
        result = prevent_mustwins(test_state, "X", 4)
        self.assertEqual(result, 1)

        test_board = (
            "--X-X-X---"
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
        result = prevent_mustwins(test_state, "X", 4)
        self.assertEqual(result, 0)

        test_board = (
            "----------"
            + "----------"
            + "--O-------"
            + "---O------"
            + "----O-----"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
        )
        test_state = TicTacToe(test_board, False, 1, 2)
        result = prevent_mustwins(test_state, "O", 4)
        self.assertEqual(result, 2)

        test_board = (
            "----------"
            + "----------"
            + "----------"
            + "---O------"
            + "--O-------"
            + "----------"
            + "O---------"
            + "----------"
            + "----------"
            + "----------"
        )
        test_state = TicTacToe(test_board, False, 1, 2)
        result = prevent_mustwins(test_state, "O", 4)
        self.assertEqual(result, 0)

        test_board = (
            "----------"
            + "-----O----"
            + "----------"
            + "---O------"
            + "--O-------"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
        )
        test_state = TicTacToe(test_board, False, 1, 2)
        result = prevent_mustwins(test_state, "O", 4)
        self.assertEqual(result, 1)

        test_board = (
            "----------"
            + "----------"
            + "----------"
            + "---------X"
            + "--------X-"
            + "----------"
            + "------X---"
            + "----------"
            + "----------"
            + "----------"
        )
        test_state = TicTacToe(test_board, False, 1, 2)
        result = prevent_mustwins(test_state, "O", 4)
        self.assertEqual(result, 0)

        test_board = (
            "----------"
            + "----------"
            + "----------"
            + "----------"
            + "--------X-"
            + "----------"
            + "------X---"
            + "-----X----"
            + "----------"
            + "----------"
        )
        test_state = TicTacToe(test_board, False, 1, 2)
        result = prevent_mustwins(test_state, "O", 4)
        self.assertEqual(result, 0)

    # Tests faulty input parameters
    def test_faulty_inputs(self):
        with self.assertRaises(TypeError):
            prevent_mustwins()

        with self.assertRaises(TypeError):
            test_board = "XX-XX----"
            test_state = TicTacToe(test_board, False, 1, 2)
            prevent_mustwins(test_state, "X")

        with self.assertRaises(AttributeError):
            test_board = "XX-XX----"
            prevent_mustwins(test_board, "X", 2)


if __name__ == "__main__":
    unittest.main()
