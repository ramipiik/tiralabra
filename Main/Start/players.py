"""User interface for asking how many human players: 0,1 or 2."""
import time
from parameters import DELAY, ERROR_MESSAGE


def get_players():
    """User interface for asking how many human players: 0,1 or 2."""
    while True:
        print("----------------")
        time.sleep(DELAY)
        print("0, 1 or 2 players game?")
        print("----------------")
        players = input("Your choice: ")
        print("----------------")
        time.sleep(DELAY)
        try:
            players = int(players)
            if players in (0, 2):
                print("Got it!", players, "players.")
                break
            if players == 1:
                print("Got it -", players, "player.")
                break
            print(ERROR_MESSAGE)
        except (TypeError, AttributeError, ValueError):
            print(ERROR_MESSAGE)
    print("----------------")
    return players
