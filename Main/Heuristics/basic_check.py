"""Gives a score to the board based on the combinations found"""
from Heuristics.helper import line_checker
from tictactoe import TicTacToe


def basic_check(tictactoe: TicTacToe, mark: str, n_to_win: int):
    # Combination is a tuple. 1st parameter is the string/combination. 2nd parameter is its value

    combos = []

    if n_to_win == 2:
        combos.append((mark + "-" + mark, 1))
        combos.append(("-" + mark + mark, 1))
        combos.append((mark + mark + "-", 1))

    if n_to_win == 3:
        combos.append((mark + "-" + mark, 1))
        combos.append(("-" + mark + mark, 1))
        combos.append((mark + mark + "-", 1))
        combos.append((mark + "-" + mark + mark, 5))
        combos.append((mark + "-" + mark + mark, 5))
        combos.append(("-" + mark + mark + mark, 7))
        combos.append((mark + mark + mark + "-", 7))

    if n_to_win == 4:
        combos.append((mark + "-" + mark, 1))
        combos.append(("-" + mark + mark, 1))
        combos.append((mark + mark + "-", 1))
        combos.append((mark + "-" + mark + mark, 3))
        combos.append((mark + mark + "-" + mark, 3))
        combos.append(("-" + mark + mark + mark, 7))
        combos.append((mark + mark + mark + "-", 7))
        combos.append((mark + "-" + mark + mark + mark, 15))
        combos.append((mark + mark + "-" + mark + mark, 15))
        combos.append((mark + mark + mark + "-" + mark, 15))
        combos.append(("-" + mark + mark + mark + mark, 20))
        combos.append((mark + mark + mark + mark + "-", 20))

    count = line_checker(combos, tictactoe, n_to_win)

    return count
