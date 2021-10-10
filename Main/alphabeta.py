"""Minimax algorithm with alpha-beta pruning and depth limitation"""
from parameters import LARGE_NUMBER, ALPHA, BETA
from Heuristics import run_heuristics
from tictactoe import TicTacToe

ROUND = 0


def alpha_beta_value(node: TicTacToe):
    """Starts the minimax-algorithm"""
    depth = 1
    max_depth = node.get_max_depth()
    if node.crosses_turn:
        value = max_value(node, ALPHA, BETA, depth, max_depth)
    else:
        value = min_value(node, ALPHA, BETA, depth, max_depth)
    return value

def max_value(node: TicTacToe, param_alpha: int, param_beta: int, depth: int, max_depth: int):
    """Core of the minimax-algorithm. Selects the optimum position for X."""
    depth += 1
    global ROUND
    ROUND += 1

    if node.is_end_state():
        return node.value()

    if depth >= max_depth:
        return run_heuristics.run_heuristics(node)

    value = -LARGE_NUMBER
    for child in node.generate_children():
        value = max(value, min_value(child, param_alpha, param_beta, depth, max_depth))
        param_alpha = max(param_alpha, value)
        if param_alpha >= param_beta:
            return value
    return value



def min_value(node: TicTacToe, param_alpha, param_beta, depth, max_depth: int):
    """Core of the minimax-algorithm. Selects the optimum position for O."""
    depth += 1
    global ROUND
    ROUND += 1

    if node.is_end_state():
        return node.value()

    if depth >= max_depth:
        return run_heuristics.run_heuristics(node)

    value = LARGE_NUMBER
    for child in node.generate_children():
        value = min(value, max_value(child, param_alpha, param_beta, depth, max_depth))
        param_beta = min(param_beta, value)
        if param_alpha >= param_beta:
            return value
    return value


def get_rounds():
    """Returns the total number of recursion calls during the game"""
    return ROUND
