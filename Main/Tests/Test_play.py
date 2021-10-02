# Execute the test class by running the following comman from command line:
# python3 -m unittest -v Tests.Test_play

import sys
import io
from play import play_human_turn, play_computer_turn, play
from tictactoe import TicTacToe
import unittest
from unittest.mock import patch


class Test_play_class(unittest.TestCase):
    @patch(
        "builtins.input",
        side_effect=[
            "a1",
            "b2",
            "c3",
            "a1",
            "b2",
            "c3",
            "a1",
            "a2",
            "",
            "a4",
            "b-1",
            "bc",
            22,
            "a3",
        ],
    )
    def test_play_human(self, mock_input):
        empty_board = 9 * "-"

        # Puts O's to A1, B2 and C3
        test_state_1 = TicTacToe(empty_board, False, 1, 2)

        result = play_human_turn(test_state_1)
        self.assertEqual(result.state, "O--------")

        result = play_human_turn(test_state_1)
        self.assertEqual(result.state, "----O----")

        result = play_human_turn(test_state_1)
        self.assertEqual(result.state, "--------O")

        # Puts X's to A1, B2 and C3
        test_state_2 = TicTacToe(empty_board, True, 1, 2)

        result = play_human_turn(test_state_2)
        self.assertEqual(result.state, "X--------")

        result = play_human_turn(test_state_2)
        self.assertEqual(result.state, "----X----")

        result = play_human_turn(test_state_2)
        self.assertEqual(result.state, "--------X")

        # Tries to put an X on top of the O on A1, which should not work. After that puts the X to A2.
        test_board = "O--------"
        test_state_3 = TicTacToe(test_board, True, 1, 2)
        result = play_human_turn(test_state_3)
        self.assertEqual(result.state, "OX-------")

        # Tries several invalid inputs. Finally puts the O to A3.
        result = play_human_turn(test_state_1)
        self.assertEqual(result.state, "--O------")

        # tries to run the play method without an input parameter
        with self.assertRaises(TypeError):
            play()

        # tries to run the play method with an invalid input parameter
        with self.assertRaises(AttributeError):
            play("123")

    # Does computer find the right moves given different boards
    def test_play_computer(self):
        test_board_1 = "XX-------"
        test_state_1 = TicTacToe(test_board_1, True, 1, 0)
        result = play_computer_turn(test_state_1)
        self.assertEqual(result.state, "XXX------")

        test_state_1 = TicTacToe(test_board_1, False, 1, 0)
        result = play_computer_turn(test_state_1)
        self.assertEqual(result.state, "XXO------")

        test_board_2 = "XOOOXX-X-"
        test_state_2 = TicTacToe(test_board_2, False, 2, 0)
        result = play_computer_turn(test_state_2)
        self.assertEqual(result.state, "XOOOXX-XO")

        test_board_2 = "XOOOXX-X-"
        test_state_2 = TicTacToe(test_board_2, True, 2, 0)
        result = play_computer_turn(test_state_2)
        self.assertEqual(result.state, "XOOOXX-XX")

        test_board_3 = 42 * "-" + "OOO" + 55 * "-"
        test_state_3 = TicTacToe(test_board_3, True, 2, 0)
        result = play_computer_turn(test_state_3)
        self.assertEqual(result.state, (42 * "-" + "OOOX" + 54 * "-"))

        test_board_4 = "-------------------------------------------O-O--------OX-------O-X---------X------------------------"
        test_state_4 = TicTacToe(test_board_4, True, 2, 0)
        result = play_computer_turn(test_state_4)
        self.assertEqual(
            result.state,
            (
                "------------------------------------X------O-O--------OX-------O-X---------X------------------------"
            ),
        )

    def test_play(self):
        # This situation should in end in a draw
        test_board = "XOOOXX-XO"
        test_state = TicTacToe(test_board, True, 2, 0)
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  #  and redirect stdout.
        play(test_state)  # Call play-function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertTrue(capturedOutput.getvalue().__contains__("DRAW"))

        # X should win this play
        test_board = "XOOOXXOX-"
        test_state = TicTacToe(test_board, True, 2, 0)
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  #  and redirect stdout.
        play(test_state)  # Call play-function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertTrue(capturedOutput.getvalue().__contains__("AND THE WINNER IS: X"))

        # The first mover should be able to win 7x7 board which requires 4 to win
        test_board = 49 * "-"
        test_state = TicTacToe(test_board, False, 2, 0)
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  #  and redirect stdout.
        play(test_state)  # Call play-function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertTrue(capturedOutput.getvalue().__contains__("AND THE WINNER IS: O"))

        # The first mover should be able to win 7x7 board which requires 4 to win
        test_board = 49 * "-"
        test_state = TicTacToe(test_board, True, 2, 0)
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  #  and redirect stdout.
        play(test_state)  # Call play-function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        self.assertTrue(capturedOutput.getvalue().__contains__("AND THE WINNER IS: X"))


if __name__ == "__main__":
    unittest.main()
