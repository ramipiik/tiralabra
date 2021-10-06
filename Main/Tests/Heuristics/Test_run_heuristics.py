# Execute the test class by running the following comman from command line:
# python3 -m unittest Tests.Heuristics.Test_run_heuristics

import unittest
from unittest.mock import patch
from Heuristics.run_heuristics import run_heuristics
from tictactoe import TicTacToe


class Test_run_heuristics_class(unittest.TestCase):
    def test_run_heuristics(self):
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
        result = run_heuristics(test_state)
        self.assertAlmostEqual(result, 0.1, 1)

        #X one move away from winning, X's turn
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
        test_state = TicTacToe(test_board, True, 1, 2)
        result = run_heuristics(test_state)
        self.assertAlmostEqual(result, 0.9, 1)

        #X one move away from winning, O's turn
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
        result = run_heuristics(test_state)
        self.assertAlmostEqual(result, 0.1, 1)

        #O one move away from winning, O's turn
        test_board = (
            "--OOOOX---"
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
        result = run_heuristics(test_state)
        self.assertAlmostEqual(result, -0.9, 1)

        #O one move away from winning, X's turn
        test_board = (
            "--OOOOX---"
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
        result = run_heuristics(test_state)
        self.assertAlmostEqual(result, -0.1, 1)

        #X has a better position, heuristics score should be positive
        test_board = (
            "----------"
            + "----------"
            + "----------"
            + "----------"
            + "---O------"
            + "---XX-----"
            + "---X------"
            + "---O------"
            + "----------"
            + "----------"
        )
        test_state = TicTacToe(test_board, True, 1, 2)
        result = run_heuristics(test_state)
        self.assertTrue(result>0)

        test_state = TicTacToe(test_board, False, 1, 2)
        result = run_heuristics(test_state)
        self.assertTrue(result>0)

        #Both players have a must-win position
        test_board = (
            "----------"
            + "----------"
            + "----------"
            + "---XO-----"
            + "---XO-----"
            + "---XO-----"
            + "---XO-----"
            + "----------"
            + "----------"
            + "----------"
        )
        test_state = TicTacToe(test_board, True, 1, 2)
        result = run_heuristics(test_state)
        self.assertAlmostEqual(result, 0.9, 1)

        test_state = TicTacToe(test_board, False, 1, 2)
        result = run_heuristics(test_state)
        self.assertAlmostEqual(result, -0.9, 1)
    
        #Both players have a must-win position
        test_board = (
            "----------"
            + "----------"
            + "----------"
            + "---XO-----"
            + "---XO-----"
            + "---XO-----"
            + "---XO-----"
            + "----------"
            + "----------"
            + "----------"
        )
        test_state = TicTacToe(test_board, True, 1, 2)
        result = run_heuristics(test_state)
        self.assertAlmostEqual(result, 0.9, 1)

        test_state = TicTacToe(test_board, False, 1, 2)
        result = run_heuristics(test_state)
        self.assertAlmostEqual(result, -0.9, 1)

        #Both players can get a must-win position with their next move
        test_board = (
            "----------"
            + "----------"
            + "----------"
            + "----------"
            + "---XO-----"
            + "---XO-----"
            + "---XO-----"
            + "----------"
            + "----------"
            + "----------"
        )
        test_state = TicTacToe(test_board, True, 1, 2)
        result = run_heuristics(test_state)
        self.assertAlmostEqual(result, 0.7, 1)

        test_state = TicTacToe(test_board, False, 1, 2)
        result = run_heuristics(test_state)
        self.assertAlmostEqual(result, -0.7, 1)

         #X's marks are closer to centre. X should get a higher score.
        test_board_1 = (
            "----------"
            + "----------"
            + "----------"
            + "----------"
            + "----XX----"
            + "----XX----"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
        )
        test_state_1 = TicTacToe(test_board_1, True, 1, 2)
        result_1 = run_heuristics(test_state_1)

        test_board_2 = (
            "----------"
            + "----------"
            + "----------"
            + "----OO----"
            + "----OO----"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
            + "----------"
        )
        test_state_2 = TicTacToe(test_board_2, True, 1, 2)
        result_2 = run_heuristics(test_state_2)
        test_state_2 = TicTacToe(test_board_2, False, 1, 2)
        result_2 = run_heuristics(test_state)
        self.assertTrue(result_1>result_2)        


    # Tests faulty input parameters
    def test_faulty_inputs(self):
        with self.assertRaises(TypeError):
            run_heuristics()

        with self.assertRaises(TypeError):
            test_board = "XX-XX----"
            test_state = TicTacToe(test_board, False, 1, 2)
            run_heuristics(test_state, "X")

        with self.assertRaises(AttributeError):
            test_board = "XX-XX----"
            run_heuristics(test_board)


if __name__ == "__main__":
    unittest.main()
