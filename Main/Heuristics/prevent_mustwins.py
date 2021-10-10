"""Checks the board for opponent's mustwin situations that must be prevented"""
from Heuristics.helper import line_checker
from tictactoe import TicTacToe


def prevent_mustwins(tictactoe: TicTacToe, mark: str, n_to_win: int):
    combos = []

    if n_to_win == 3:
        combos.append(("-" + mark + "-" + mark + "-", 1))
        combos.append(("-" + mark + mark + "-" + "-", 1))
        combos.append(("-" + "-" + mark + mark + "-", 1))

    if n_to_win == 4:
        combos.append(("-" + mark + "-" + mark + mark + "-", 1))
        combos.append(("-" + mark + mark + "-" + mark + "-", 1))
        combos.append(("-" + mark + mark + mark + "-" + "-", 1))
        combos.append(("-" + "-" + mark + mark + mark + "-", 1))

    count = line_checker(combos, tictactoe, n_to_win)
    return count
