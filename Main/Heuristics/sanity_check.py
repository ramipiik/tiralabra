from Heuristics.helper import line_checker
from tictactoe import TicTacToe

# Checks whether there are situations requiring immediate defensive action
# Input parameters: 
    # tictactoe: state of the board
    # mark: X or O
    # n: How many in a row are required to win

def sanity_check(tictactoe:TicTacToe, mark:str, n:int):
 
    combos = []
    combos_2 = []
    combos_3 = []
    combos_4 = []

    if n == 2:
        combo = "-" + mark + mark
        combos_2.append((combo,1))

        combo = mark + mark + "-"
        combos_2.append((combo,1))

        combo = mark + "-" + mark
        combos_2.append((combo,1))

    if n == 3:
        combo = mark + "-" + mark + mark
        combos_3.append((combo,1))

        combo = mark + mark + "-" + mark
        combos_3.append((combo,1))

        combo = mark + mark + mark + "-"
        combos_3.append((combo,1))

        combo = "-" + mark + mark + mark
        combos_3.append((combo,1))

    if n == 4:
        combo = mark + "-" + mark + mark + mark
        combos_4.append((combo,1))

        combo = mark + mark + "-" + mark + mark
        combos_4.append((combo,1))

        combo = mark + mark + mark + "-" + mark
        combos_4.append((combo,1))

        combo = "-" + mark + mark + mark + mark
        combos_4.append((combo,1))

        combo = mark + mark + mark + mark + "-"
        combos_4.append((combo,1))

    if n == 2:
        combos = combos_2
    if n == 3:
        combos = combos_3
    if n == 4:
        combos = combos_4

    count = line_checker(combos, tictactoe, n)

    return count
