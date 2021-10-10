"""Scores the board based on number of connection to other own marks."""
from tictactoe import TicTacToe


def closeness_check(tictactoe: TicTacToe, mark: str, first_time=False):
    # The more own marks are connected, the higher the score.

    counter = 0
    table = []
    for i in range(tictactoe.board_size):
        rivi = tictactoe.state[
            i * tictactoe.board_size : (i + 1) * tictactoe.board_size
        ]
        if first_time:  # If computer goes 2nd, play close to opponent's mark
            rivi = rivi.replace("O", "X")
        table.append(rivi)

    for i in range(tictactoe.board_size):
        for j in range(tictactoe.board_size):
            if i - 1 >= 0 and table[j][i] == mark and table[j][i - 1] == mark:
                counter += 1
            if j - 1 >= 0 and table[j][i] == mark and table[j - 1][i] == mark:
                counter += 1
            if (
                i + 1 < tictactoe.board_size
                and table[j][i] == mark
                and table[j][i + 1] == mark
            ):
                counter += 1
            if (
                j + 1 < tictactoe.board_size
                and table[j][i] == mark
                and table[j + 1][i] == mark
            ):
                counter += 1
            if (
                j + 1 < tictactoe.board_size
                and i + 1 < tictactoe.board_size
                and table[j][i] == mark
                and table[j + 1][i + 1] == mark
            ):
                counter += 1
            if (
                j - 1 >= 0
                and i - 1 >= 0
                and table[j][i] == mark
                and table[j - 1][i - 1] == mark
            ):
                counter += 1
            if (
                j - 1 > 0
                and i + 1 < tictactoe.board_size
                and table[j][i] == mark
                and table[j - 1][i + 1] == mark
            ):
                counter += 1
            if (
                i - 1 > 0
                and j + 1 < tictactoe.board_size
                and table[j][i] == mark
                and table[j + 1][i - 1] == mark
            ):
                counter += 1

    maximum = ((tictactoe.board_size ** 2) / 2) * 9
    relation = counter / maximum
    return relation
