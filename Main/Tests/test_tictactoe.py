"""Tests for tictactoe module"""

# Start the tests by running:
# python3 -m unittest -v Tests.Test_tictactoe

import unittest
import sys
import io
from tictactoe import TicTacToe


class TestTictactoe(unittest.TestCase):
    def test_tictactoe(self):
        # Horizontal winning line
        test_board = "XXX------"
        test_state = TicTacToe(test_board, False, 1, 2)
        self.assertTrue(test_state.is_end_state())
        self.assertFalse(test_state.crosses_turn)
        self.assertTrue(test_state.value(), 1)
        self.assertEqual(test_state.count_empty(), 6)

        test_board = 400 * "-"
        test_state = TicTacToe(test_board, True, 1, 2)
        self.assertFalse(test_state.is_end_state())
        self.assertTrue(test_state.crosses_turn)
        self.assertEqual(test_state.count_empty(), 400)

        # Vertical winning line
        test_board = "X--X--X--"
        test_state = TicTacToe(test_board, False, 1, 2)
        self.assertTrue(test_state.is_end_state())
        self.assertEqual(test_state.value(), 1)
        self.assertEqual(test_state.count_empty(), 6)

        # Diagonal winning line 1
        test_board = "--O-O-O--"
        test_state = TicTacToe(test_board, False, 1, 2)
        self.assertTrue(test_state.is_end_state())
        self.assertEqual(test_state.value(), -1)
        self.assertEqual(test_state.count_empty(), 6)

        # Diagonal winning line 2
        test_board = "X---X---X"
        test_state = TicTacToe(test_board, False, 1, 2)
        self.assertTrue(test_state.is_end_state())
        self.assertEqual(test_state.count_empty(), 6)

        # Diagonal winning line 3
        test_board = "OO-----------------------------------------------------------------------------------------------------------------------------OOX------------------X-O--------------OXXXXO---------------XOXOX--------------X-XOOOX--------------XX----O------------O----------------------------------------------------------------------------------------------------------------------------------------------------------"
        test_state = TicTacToe(test_board, False, 1, 2)
        self.assertTrue(test_state.is_end_state())
        self.assertEqual(test_state.value(), 1)
        self.assertEqual(test_state.count_empty(), 372)

        # Test printing of the board
        captured_output = io.StringIO()  # Create StringIO object
        sys.stdout = captured_output  #  and redirect stdout.
        test_board = "XXX------"
        test_state = TicTacToe(test_board, False, 1, 2)
        print(test_state)  # Print
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertTrue(
            captured_output.getvalue().__contains__(
                "     1   2   3\nA  | X | X | X |\nB  | - | - | - |\nC  | - | - | - |"
            )
        )

    def test_childen(self):
        # Makes sure that the right amount of children are generated
        test_board = "X---X---X"
        test_state = TicTacToe(test_board, False, 1, 2)
        children = test_state.generate_children()
        self.assertEqual(len(children), 6)

        # Tests whether the two children below are generated
        child1 = "X--OX---X"
        child2 = "X---X--OX"
        found1 = False
        found2 = False
        for i in children:
            if i.state == child1:
                found1 = True
            if i.state == child2:
                found2 = True
        self.assertTrue(found1 and found2)

        # Makes sure all children have 5 empty cells
        five_empty = True
        for i in children:
            if i.count_empty() != 5:
                five_empty = False
                break
        self.assertTrue(five_empty)
