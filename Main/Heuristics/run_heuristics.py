"""Starts and coordinates the heuristics routines"""
from tictactoe import TicTacToe
from Heuristics import basic_check
from Heuristics import boundaries_check
from Heuristics import closeness_check
from Heuristics import sanity_check
from Heuristics import mustwin_check
from Heuristics import prevent_mustwins


def run_heuristics(tictactoe: TicTacToe):
    # scores the position based on number of connection to other own marks.
    # The more own marks are connected, the higher the score.
    x_closeness_bonus = (
        closeness_check.closeness_check(tictactoe, "X") * tictactoe.closeness_weight
    )
    o_closeness_bonus = (
        closeness_check.closeness_check(tictactoe, "O") * tictactoe.closeness_weight
    )

    # Reverses the closeness check for the first turn.
    # Purpose is to steer computers first move close to humans first move.
    if tictactoe.count_empty() == tictactoe.board_size ** 2 - 2:
        x_closeness_bonus = (
            closeness_check.closeness_check(tictactoe, "X", True)
            * tictactoe.closeness_weight
        )

    # scores the position based on distance from the center.
    # Closer to centre is better. Small impact.
    x_center_bonus = (
        boundaries_check.boundaries_check(tictactoe, "X") * tictactoe.center_weight
    )
    o_center_bonus = (
        boundaries_check.boundaries_check(tictactoe, "O") * tictactoe.center_weight
    )

    # Priority 1: Check whether there are situations requiring immediate defensive action
    if tictactoe.crosses_turn:
        x_wins = sanity_check.sanity_check(tictactoe, "X", tictactoe.to_win - 1)
        if x_wins > 0:
            return 0.9 + x_closeness_bonus + x_center_bonus

    if not tictactoe.crosses_turn:
        o_wins = sanity_check.sanity_check(tictactoe, "O", tictactoe.to_win - 1)
        if o_wins > 0:
            return -0.9 - o_closeness_bonus - o_center_bonus

    # Priority 2: Check whether a mustwin situation gan be gained
    x_wins = mustwin_check.check_mustwins(tictactoe, "X", tictactoe.to_win - 1)
    if x_wins > 0:
        return 0.8 + x_closeness_bonus + x_center_bonus
    o_wins = mustwin_check.check_mustwins(tictactoe, "O", tictactoe.to_win - 1)
    if o_wins > 0:
        return -0.8 - o_closeness_bonus - o_center_bonus

    # Priority 3: Check whether the competitor is about to get a mustwin situation.
    x_wins = prevent_mustwins.prevent_mustwins(tictactoe, "X", tictactoe.to_win - 1)
    if x_wins > 0 and tictactoe.crosses_turn:
        return 0.7 + x_closeness_bonus + x_center_bonus
    o_wins = prevent_mustwins.prevent_mustwins(tictactoe, "O", tictactoe.to_win - 1)
    if o_wins > 0 and not tictactoe.crosses_turn:
        return -0.7 - o_closeness_bonus - o_center_bonus

    # Calculates scoring for the position if there were no obvious plays dominating the situation
    x_result = basic_check.basic_check(tictactoe, "X", tictactoe.to_win - 1)
    o_result = basic_check.basic_check(tictactoe, "O", tictactoe.to_win - 1)
    if o_result == 0:
        o_result = 0.0000000000001
    if x_result == 0:
        x_result = 0.0000000000001
    total = x_result + o_result
    diff = x_result - o_result
    weight = 0.1
    impact = 0
    try:
        impact = diff / total * weight
    except (TypeError, ZeroDivisionError):
        pass
    outcome = (
        impact + x_closeness_bonus + x_center_bonus - o_closeness_bonus - o_center_bonus
    )
    return outcome
