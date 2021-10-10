"""
Asks for user inputted parameters and starts the game.
"""

import datetime
from tictactoe import TicTacToe
from play import play
from Start.start import start


def main():
    """Asks for user inputted parameters and starts the game."""
    user_choices = start()
    players = user_choices[0]
    board_size = user_choices[1]
    level = user_choices[2]
    first_move = user_choices[3]
    x_starts = first_move == 2

    custom_board = (board_size ** 2) * "-"
    state = TicTacToe(custom_board, x_starts, level, players, True)
    current_time = datetime.datetime.now()
    play(state, current_time)


main()
