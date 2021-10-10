"""Checks whether there is a possibility to gain a mustwin position"""
from Heuristics.helper import line_checker

def check_mustwins(tictactoe, mark: str, n_to_win: int):
    combos = []
    winning_combos_2 = []
    winning_combos_3 = []
    winning_combos_4 = []

    if n_to_win == 2:
        combo = "-" + mark + mark + "-"
        winning_combos_2.append((combo, 1))

    if n_to_win == 3:
        combo = "-" + mark + mark + mark + "-"
        winning_combos_3.append((combo, 1))

    if n_to_win == 4:
        combo = "-" + mark + mark + mark + mark + "-"
        winning_combos_4.append((combo, 1))

    if n_to_win == 2:
        combos = winning_combos_2
    if n_to_win == 3:
        combos = winning_combos_3
    if n_to_win == 4:
        combos = winning_combos_4

    count = line_checker(combos, tictactoe, n_to_win)

    return count
