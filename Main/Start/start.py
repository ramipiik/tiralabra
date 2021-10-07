import time
from parameters import delay
from Start.players import get_players
from Start.board import get_board
from Start.level import get_level
from Start.recap import recap
from Start.confirm import confirm
from Start.first_move import get_first_move


# Coordinates the start of the game by calling the individual user interface methods
def start():
    while True:
        players = get_players()
        time.sleep(delay)
        board_size = get_board()
        time.sleep(delay)
        level = get_level(players)
        time.sleep(delay)
        first_move = get_first_move(players)
        time.sleep(delay)
        recap(players, board_size, level, first_move)
        time.sleep(delay)
        if confirm():
            return (players, board_size, level, first_move)
