import time
from parameters import DELAY, ERROR_MESSAGE

# User interface for asking how many human players: 0,1 or 2.


def get_players():
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
            if players == 0 or players == 2:
                print("Got it!", players, "players.")
                break
            if players == 1:
                print("Got it -", players, "player.")
                break
            else:
                print(ERROR_MESSAGE)
        except:
            print(ERROR_MESSAGE)
    print("----------------")
    return players
