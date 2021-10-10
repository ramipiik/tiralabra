"""Contains all the "magic numbers" to fine tune and adjust the algorithm"""

CENTER_WEIGHT = 0.02  # how much value to give for center positions
LARGE_NUMBER = 1000000  # needed for getting started with optimization
ALPHA = -1
BETA = 1
DELAY = 0  # Delay between steps. The experience might improve if things don't happen too quickly.

ERROR_MESSAGE = "Well - that was not a valid choice. Please try again."

def how_much_to_win(board_size):
    """How many marks in a row are required to win"""
    if board_size == 3:
        return 3
    if board_size == 5:
        return 4
    if board_size == 7:
        return 4
    return 5


def closeness_weight(level):
    """Defines the importance of having marks close to each other"""
    if level == 2:
        return 0.25
    return 0
