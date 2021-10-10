"""Class, which is used for defining the state of the play."""
import string
from math import sqrt
from parameters import (
    LARGE_NUMBER,
    how_much_to_win,
    closeness_weight,
    CENTER_WEIGHT,
)
from Heuristics.helper import line_checker


class TicTacToe:
    """Class, which is used for defining the state of the play."""

    def __init__(self, state, crosses_turn, level, players, first_turn=False):
        self.state = state
        self.board_size = int(sqrt(len(self.state)))
        self.crosses_turn = crosses_turn
        self.players = players
        self.level = level
        self.first_turn = first_turn
        self.to_win = how_much_to_win(self.board_size)
        self.closeness_weight = closeness_weight(level)
        self.center_weight = CENTER_WEIGHT

    def is_end_state(self):
        """Checks whether the state ends the game. Either the board is full, or one player won."""
        return (
            "-" not in self.state
            or self.won("X", self.to_win)
            or self.won("O", self.to_win)
        )

    def won(self, mark, board_size):
        """Checks whether the board contains a winning combination"""
        combo = board_size * mark
        combos = []
        combos.append((combo, 1))

        result = line_checker(combos, self, board_size - 1)
        if result > 0:
            return True

        return False

    def __str__(self):
        """Prints the board"""
        top_row = "  "
        for numero in range(1, self.board_size + 1):
            if numero <= 10:
                top_row += "   " + str(numero)
            else:
                top_row += "  " + str(numero)
        top_row += "\n"
        field = top_row
        for i in range(self.board_size):
            row = string.ascii_uppercase[i] + " "
            row += self.board_size * " | a"
            row += " |\n"
            field += row
        for character in self.state:
            field = field.replace("a", character, 1)
        return field

    def generate_children(self):
        """Creates all possible following states of the current board"""
        possible_states = []
        if self.crosses_turn:
            mark = "X"
        else:
            mark = "O"

        for i in range(len(self.state)):
            aux = self.state
            if self.state[i] == "-":
                aux = aux[:i] + mark + aux[i + 1 :]
                new_state = TicTacToe(
                    aux, not self.crosses_turn, self.level, self.players
                )
                possible_states.append(new_state)
        return possible_states

    def value(self):
        """Returns 1 if x wins, and -1 if o wins"""
        if self.won("X", self.to_win):
            return 1
        if self.won("O", self.to_win):
            return -1
        return 0

    def count_empty(self):
        """Counts the number of empty cells on the board."""
        count = 0
        for char in self.state:
            if char == "-":
                count += 1
        return count

    def get_max_depth(self):
        """Calculates dynamically the max recursion depth depending on the nr. of empty cells."""
        if self.level == 1:  # easy level uses only heuristics
            return 0
        empty = self.count_empty()
        if empty <= 10:
            return LARGE_NUMBER  # no need to restrict depth when only a few cells left
        if empty <= 25:
            return 4
        if empty <= 50:
            return 3
        return 2
