# Contains all the "magic numbers" to fine tune and adjust the algorithm

max_empty_cells = 40  # if too many options go directly for heuristics
center_weight = 0.02  # how much value to give for center positions
LARGE_NUMBER = 1000000  # needed for getting started with optimization
alpha = -1
beta = 1
delay = 0  # how long delay to have between steps. The interaction/experience might be better if things don't happen too quickly.

error_message = "Well - that was not a valid choice. Please try again."

# How many marks in a row are required to win
def how_much_to_win(board_size):
    if board_size == 3:
        return 3
    if board_size == 5:
        return 4
    if board_size == 7:
        return 4
    return 5


# How many recursion rounds are run before switching to heuristics
def recursion_depth(board_size):
    if board_size == 3:
        return 11
    return 3


# Defines the importance of having marks close to each other
def closeness_weight(level):
    if level == 2:
        return 0.25
    return 0
