# Start the tests by running:
# python3 -m unittest -v Tests.Test_start

import unittest
from unittest.mock import patch
from Start.players import get_players
from Start.board import get_board
from Start.first_move import get_first_move
from Start.level import get_level
from Start.start import start
from Start.confirm import confirm
from Start.recap import recap


class Test_start_class(unittest.TestCase):
    @patch("builtins.input", side_effect=["a", "", "\n", -1, 1, 2])
    def test_get_players(self, mock_input):
        result1 = get_players()
        result2 = get_players()
        self.assertEqual(result1, 1)
        self.assertEqual(result2, 2)

        with self.assertRaises(TypeError):
            get_players(1)

    @patch(
        "builtins.input",
        side_effect=[9, "asdfadsf", "", "\n", "a", "b", "c", "d", "e", "f"],
    )
    def test_get_board(self, mock_input):
        result1 = get_board()
        result2 = get_board()
        result3 = get_board()
        result4 = get_board()
        result5 = get_board()
        result6 = get_board()
        self.assertEqual(result1, 3)
        self.assertEqual(result2, 5)
        self.assertEqual(result3, 7)
        self.assertEqual(result4, 10)
        self.assertEqual(result5, 15)
        self.assertEqual(result6, 20)

        with self.assertRaises(TypeError):
            get_board(1)

    @patch("builtins.input", side_effect=["a", "", "\n", -1, 1, 2])
    def test_get_first_move(self, mock_input):
        result1 = get_first_move(1)
        result2 = get_first_move(1)
        self.assertEqual(result1, 1)
        self.assertEqual(result2, 2)

        result3 = get_first_move(0)
        result4 = get_first_move(0)
        self.assertEqual(result3, 1)
        self.assertEqual(result4, 1)

        result5 = get_first_move(2)
        result6 = get_first_move(2)
        self.assertEqual(result5, 1)
        self.assertEqual(result6, 1)

        result7 = get_first_move("a")
        self.assertEqual(result7, 1)

        with self.assertRaises(TypeError):
            get_first_move()

        with self.assertRaises(TypeError):
            get_first_move(1, 2)

    @patch("builtins.input", side_effect=["a", "", "\n", -1, 1, 2, 1, 2, 1])
    def test_get_level(self, mock_input):
        result1 = get_level(1)
        result2 = get_level(1)
        self.assertEqual(result1, 1)
        self.assertEqual(result2, 2)

        result3 = get_level(0)
        result4 = get_level(0)
        self.assertEqual(result3, 1)
        self.assertEqual(result4, 2)

        result5 = get_level(2)
        self.assertIsNone(result5)

        result6 = get_level("a")
        self.assertIsNone(result6)

        with self.assertRaises(TypeError):
            get_level()

        with self.assertRaises(TypeError):
            get_level(1, 2)

    def test_recap(self):
        self.assertIsNone(recap(1, 3, 1, 1))

    @patch("builtins.input", side_effect=["fff", "", "c"])
    def test_confirm(self, mock_input):
        self.assertTrue(confirm())
        self.assertFalse(confirm())
        with self.assertRaises(TypeError):
            confirm(1, 2, 3)

    @patch("Start.start.get_players")
    @patch("Start.start.get_board")
    @patch("Start.start.get_level")
    @patch("Start.start.get_first_move")
    @patch("Start.start.confirm")
    def test_start(
        self,
        mock_confirm,
        mock_get_first_move,
        mock_get_level,
        mock_get_board,
        mock_get_players,
    ):
        mock_get_players.return_value = 1
        mock_get_board.return_value = 3
        mock_get_level.return_value = 1
        mock_get_first_move.return_value = 1
        mock_confirm.return_value = True
        result = start()
        self.assertEqual(result, (1, 3, 1, 1))

        mock_get_players.return_value = 0
        mock_get_board.return_value = 9
        mock_get_level.return_value = 2
        mock_get_first_move.return_value = 2
        mock_confirm.return_value = True
        result = start()
        self.assertEqual(result, (0, 9, 2, 2))

        with self.assertRaises(TypeError):
            start(1)


if __name__ == "__main__":
    unittest.main()
