"""Goes through all lines on the board"""


def line_checker(combos: list, tictactoe, n_to_win: int):
    # Searches for the combinations in combos parameter
    # Combos is a list of tuples (string, int).
    # First parameter of the tuple is the string/combination to search for.
    # Second parameter is the points given for that combination.
    # Retuns the sum of combinations

    count = 0
    # checks horizontal_lines
    for i in range(tictactoe.board_size):
        rivi: str = tictactoe.state[
            i * tictactoe.board_size : i * tictactoe.board_size + tictactoe.board_size
        ]
        for combo in combos:
            if rivi.__contains__(combo[0]):
                count += combo[1]

    # checks vertical_lines
    for i in range(tictactoe.board_size):
        rivi = ""
        for j in range(tictactoe.board_size):
            rivi += tictactoe.state[j * tictactoe.board_size + i]
        for combo in combos:
            if rivi.__contains__(combo[0]):
                count += combo[1]

    # checks diagonal lines from top row to right-down
    for i in range(tictactoe.board_size):
        max_length = tictactoe.board_size - i
        rivi = ""
        if i <= tictactoe.board_size - n_to_win - 1:
            for j in range(tictactoe.board_size):
                if len(rivi) < max_length:
                    rivi += tictactoe.state[i + j * (tictactoe.board_size + 1)]
        for combo in combos:
            if rivi.__contains__(combo[0]):
                count += combo[1]

    # checks diagonal lines from top row to left-down
    for i in range(tictactoe.board_size - 1, -1, -1):
        max_length = i + 1
        rivi = ""
        if i >= n_to_win - 1:
            for j in range(tictactoe.board_size):
                if len(rivi) < max_length:
                    rivi += tictactoe.state[i + j * (tictactoe.board_size - 1)]
        for combo in combos:
            if rivi.__contains__(combo[0]):
                count += combo[1]

    # checks diagonal lines from left column to right-down
    for j in range(
        1, tictactoe.board_size
    ):  # top-left corner has already been checked. Thus starting from row 1.
        max_length = tictactoe.board_size - j
        rivi = ""
        if j <= tictactoe.board_size - n_to_win - 1:
            for i in range(tictactoe.board_size):
                if len(rivi) < max_length:
                    rivi += tictactoe.state[
                        j * tictactoe.board_size + i * (tictactoe.board_size + 1)
                    ]
        for combo in combos:
            if rivi.__contains__(combo[0]):
                count += combo[1]

    # checks diagonal lines from right column to left-down
    for j in range(
        1, tictactoe.board_size
    ):  # top-right corner has already been checked. Thus starting from row 1.
        max_length = tictactoe.board_size - j
        rivi = ""
        if j <= tictactoe.board_size - n_to_win - 1:
            for i in range(tictactoe.board_size):
                if len(rivi) < max_length:
                    rivi += tictactoe.state[
                        (tictactoe.board_size - 1)
                        + j * (tictactoe.board_size)
                        + i * (tictactoe.board_size - 1)
                    ]
        for combo in combos:
            if rivi.__contains__(combo[0]):
                count += combo[1]

    return count
