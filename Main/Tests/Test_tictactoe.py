from tictactoe import TicTacToe
import unittest, sys, io
from unittest.mock import patch


class Test_tictactoe_class(unittest.TestCase):
    def test_tictactoe(self):
        # Horizontal winning line
        test_board_1 = "XXX------"
        test_state_1 = TicTacToe(test_board_1, False, 1, 2)
        self.assertTrue(test_state_1.is_end_state())
        self.assertFalse(test_state_1.crosses_turn)
        self.assertTrue(test_state_1.value(), 1)
        self.assertEqual(test_state_1.count_empty(), 6)

        test_board_2 = 400 * "-"
        test_state_2 = TicTacToe(test_board_2, True, 1, 2)
        self.assertFalse(test_state_2.is_end_state())
        self.assertTrue(test_state_2.crosses_turn)
        self.assertEqual(test_state_2.count_empty(), 400)

        # Vertical winning line
        test_board_3 = "X--X--X--"
        test_state_3 = TicTacToe(test_board_3, False, 1, 2)
        self.assertTrue(test_state_3.is_end_state())
        self.assertEqual(test_state_3.value(), 1)
        self.assertEqual(test_state_3.count_empty(), 6)

        # Diagonal winning line 1
        test_board_4 = "--O-O-O--"
        test_state_4 = TicTacToe(test_board_4, False, 1, 2)
        self.assertTrue(test_state_4.is_end_state())
        self.assertEqual(test_state_4.value(), -1)
        self.assertEqual(test_state_4.count_empty(), 6)

        # Diagonal winning line 2
        test_board_4 = "X---X---X"
        test_state_4 = TicTacToe(test_board_4, False, 1, 2)
        self.assertTrue(test_state_4.is_end_state())
        self.assertEqual(test_state_4.count_empty(), 6)

        # Diagonal winning line 3
        test_board_5 = "OO-----------------------------------------------------------------------------------------------------------------------------OOX------------------X-O--------------OXXXXO---------------XOXOX--------------X-XOOOX--------------XX----O------------O----------------------------------------------------------------------------------------------------------------------------------------------------------"
        test_state_5 = TicTacToe(test_board_5, False, 1, 2)
        self.assertTrue(test_state_5.is_end_state())
        self.assertEqual(test_state_5.value(), 1)
        self.assertEqual(test_state_5.count_empty(), 372)

        # Test printing of the board
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  #  and redirect stdout.
        print(test_state_1)  # Print
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertTrue(
            capturedOutput.getvalue().__contains__(
                "     1   2   3\nA  | X | X | X |\nB  | - | - | - |\nC  | - | - | - |"
            )
        )

        # Makes sure that the right amount of children are generated
        children = test_state_4.generate_children()
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
