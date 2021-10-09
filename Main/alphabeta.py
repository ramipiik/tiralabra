from parameters import LARGE_NUMBER, alpha, beta
from Heuristics import run_heuristics
from tictactoe import TicTacToe

round = 0

# Starts the minimax-algorithm. If crosses turn -> calls max_value. If not crosses turn -> calls min_value
def alpha_beta_value(node: TicTacToe):
    depth = 1
    max_depth = node.get_max_depth()
    if node.crosses_turn:
        value = max_value(node, alpha, beta, depth, max_depth)
    else:
        value = min_value(node, alpha, beta, depth, max_depth)
    return value


# Core of the minimax-algorithm. Selects the optimum position for X.
def max_value(node: TicTacToe, alpha: int, beta: int, depth: int, max_depth: int):
    depth += 1
    global round
    round += 1

    if node.is_end_state():
        return node.value()

    if depth >= max_depth:
        return run_heuristics.run_heuristics(node)

    v = -LARGE_NUMBER
    for child in node.generate_children():
        v = max(v, min_value(child, alpha, beta, depth, max_depth))
        alpha = max(alpha, v)
        if alpha >= beta:
            return v
    return v


# Core of the minimax-algorithm. Selects the optimum position for O.
def min_value(node: TicTacToe, alpha, beta, depth, max_depth: int):
    depth += 1
    global round
    round += 1

    if node.is_end_state():
        return node.value()

    if depth >= max_depth:
        return run_heuristics.run_heuristics(node)

    v = LARGE_NUMBER
    for child in node.generate_children():
        v = min(v, max_value(child, alpha, beta, depth, max_depth))
        beta = min(beta, v)
        if alpha >= beta:
            return v
    return v


def get_rounds():
    return round
