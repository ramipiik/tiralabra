"""Calculates the distance of the marks from the boundaries"""
from tictactoe import TicTacToe


def boundaries_check(tictactoe: TicTacToe, mark: str):
    """Calculates the distance from edges. Center positions are valued higher than edge positions"""
    # Input parameters:
    # tictactoe: state of the board
    # mark: X or O
    # first_time: If computer goes second, steers it put its mark connected to opponent's mark

    distance = 0
    table = []
    for i in range(tictactoe.board_size):
        rivi = tictactoe.state[
            i * tictactoe.board_size : (i + 1) * tictactoe.board_size
        ]
        table.append(rivi)

    for i in range(tictactoe.board_size):
        for j in range(tictactoe.board_size):
            if table[j][i] == mark:
                distance += min(j, tictactoe.board_size - j) + min(
                    i, tictactoe.board_size - i
                )

    maximum = (tictactoe.board_size / 2) * tictactoe.board_size ** 2
    relation = distance / maximum
    return relation
