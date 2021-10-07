# Execute the test class by running the following comman from command line:
# python3 -m unittest Tests.Heuristics.Test_sanity_check

import unittest
from unittest.mock import patch
from Heuristics.sanity_check import sanity_check
from tictactoe import TicTacToe


class Test_sanity_check_class(unittest.TestCase):
    def test_sanity_check(self):
        test_board = (
            "--OXXXX---"
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
        result = sanity_check(test_state, "X", 4)
        self.assertEqual(result, 1)

        test_board = (
            "---XX-XX--"
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
        result = sanity_check(test_state, "X", 4)
        self.assertEqual(result, 1)

        test_board = (
            "--XX-XX---"
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
        test_state = TicTacToe(test_board, True, 1, 2)
        result = sanity_check(test_state, "0", 4)
        self.assertAlmostEqual(result, 0, 1)

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
        result = sanity_check(test_state, "X", 4)
        self.assertAlmostEqual(result, 0, 1)

        test_board = (
            "----------"
            + "----------"
            + "--O-------"
            + "---O------"
            + "----O-----"
            + "-----O----"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
        )
        test_state = TicTacToe(test_board, False, 1, 2)
        result = sanity_check(test_state, "O", 4)
        self.assertEqual(result, 2)

        test_board = (
            "----------"
            + "----------"
            + "--O-------"
            + "---O------"
            + "----O-----"
            + "-----O----"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
        )
        test_state = TicTacToe(test_board, False, 1, 2)
        result = sanity_check(test_state, "X", 4)
        self.assertAlmostEqual(result, 0, 1)

        test_board = (
            "----------"
            + "----------"
            + "----------"
            + "---O------"
            + "--O-------"
            + "-O--------"
            + "O---------"
            + "----------"
            + "----------"
            + "----------"
        )
        test_state = TicTacToe(test_board, False, 1, 2)
        result = sanity_check(test_state, "O", 4)
        self.assertEqual(result, 1)

        test_board = (
            "----------"
            + "-----O----"
            + "----O-----"
            + "---O------"
            + "--O-------"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
        )
        test_state = TicTacToe(test_board, False, 1, 2)
        result = sanity_check(test_state, "O", 4)
        self.assertEqual(result, 2)

        test_board = (
            "----------"
            + "----------"
            + "----------"
            + "---------X"
            + "--------X-"
            + "-------X--"
            + "------X---"
            + "----------"
            + "----------"
            + "----------"
        )
        test_state = TicTacToe(test_board, False, 1, 2)
        result = sanity_check(test_state, "X", 4)
        self.assertEqual(result, 1)

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
        result = sanity_check(test_state, "X", 4)
        self.assertEqual(result, 0)

    # Tests faulty input parameters
    def test_faulty_inputs(self):
        with self.assertRaises(TypeError):
            sanity_check()

        with self.assertRaises(TypeError):
            test_board = "XX-XX----"
            test_state = TicTacToe(test_board, False, 1, 2)
            sanity_check(test_state, "X")

        with self.assertRaises(AttributeError):
            test_board = "XX-XX----"
            sanity_check(test_board, "X", 2)


if __name__ == "__main__":
    unittest.main()
