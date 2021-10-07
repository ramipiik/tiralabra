from parameters import (
    how_much_to_win,
    recursion_depth,
    closeness_weight,
    center_weight,
    max_empty_cells,
)
import string
from math import sqrt
from Heuristics.helper import line_checker

# Defines the Tictactoe class, which is used for defining the state of the play. 
class TicTacToe:
    def __init__(self, state, crosses_turn, level, players, first_turn=False):
        self.state = state
        self.board_size = int(sqrt(len(self.state)))
        self.crosses_turn = crosses_turn
        self.players = players
        self.level = level
        self.first_turn = first_turn
        self.to_win = how_much_to_win(self.board_size)
        self.max_depth = recursion_depth(self.board_size)
        self.closeness_weight = closeness_weight(level)
        self.center_weight = center_weight
        self.heuristics_limit = max_empty_cells

    # Checks whether the state ends the game. Either the board is full, or one player won.
    def is_end_state(self):
        if (
            ("-" not in self.state)
            or self.won("X", self.to_win)
            or self.won("O", self.to_win)
        ):
            return True
        else:
            return False

    # Check whether the board contains a winning combination
    def won(self, mark, n):
        combo = n * mark
        combos=[]
        combos.append((combo,1))

        result=line_checker(combos, self, n-1)
        if result>0:
            return True
        
        return False


    # Prints the board
    def __str__(self):
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

    # Important function. Creates all possible following states of the current board
    def generate_children(self):
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

    # returns 1 if x wins, and -1 if o wins
    def value(self):
        if self.won("X", self.to_win):
            return 1
        if self.won("O", self.to_win):
            return -1
        return 0

    # Counts the number of empty cells on the board.
    def count_empty(self):
        count = 0
        for char in self.state:
            if char == "-":
                count += 1
        return count
