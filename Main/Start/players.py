import time
from parameters import delay, error_message

# User interface for asking how many human players: 0,1 or 2.


def get_players():
    while True:
        print("----------------")
        time.sleep(delay)
        print("0, 1 or 2 players game?")
        print("----------------")
        players = input("Your choice: ")
        print("----------------")
        time.sleep(delay)
        try:
            players = int(players)
            if players == 0 or players == 2:
                print("Got it!", players, "players.")
                break
            if players == 1:
                print("Got it -", players, "player.")
                break
            else:
                print(error_message)
        except:
            print(error_message)
    print("----------------")
    return players
