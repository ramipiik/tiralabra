from Heuristics.helper import line_checker
from tictactoe import TicTacToe

# Checks whether there are situations which must be blocked so that the opponent doesn't gain a mustwin position
# Input parameters:
# tictactoe: state of the board
# mark: X or O
# n: How many in a row are required to win


def prevent_mustwins(tictactoe: TicTacToe, mark: str, n: int):
    combos = []
    winning_combos_3 = []
    winning_combos_4 = []

    if n == 3:
        combo = "-" + mark + "-" + mark + "-"
        winning_combos_3.append((combo, 1))
        combo = "-" + mark + mark + "-" + "-"
        winning_combos_3.append((combo, 1))
        combo = "-" + "-" + mark + mark + "-"
        winning_combos_3.append((combo, 1))

    if n == 4:
        combo = "-" + mark + "-" + mark + mark + "-"
        winning_combos_4.append((combo, 1))
        combo = "-" + mark + mark + "-" + mark + "-"
        winning_combos_4.append((combo, 1))
        combo = "-" + mark + mark + mark + "-" + "-"
        winning_combos_4.append((combo, 1))
        combo = "-" + "-" + mark + mark + mark + "-"
        winning_combos_4.append((combo, 1))

    if n == 3:
        combos = winning_combos_3
    if n == 4:
        combos = winning_combos_4

    count = line_checker(combos, tictactoe, n)

    return count
