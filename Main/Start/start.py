import time
from parameters import DELAY
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
        time.sleep(DELAY)
        board_size = get_board()
        time.sleep(DELAY)
        level = get_level(players)
        time.sleep(DELAY)
        first_move = get_first_move(players)
        time.sleep(DELAY)
        recap(players, board_size, level, first_move)
        time.sleep(DELAY)
        if confirm():
            return (players, board_size, level, first_move)
