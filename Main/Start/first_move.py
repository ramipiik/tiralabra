"""User interface for asking which one gets to go first - computer or human"""
import time
from parameters import DELAY, ERROR_MESSAGE


def get_first_move(players):
    """User interface for asking which one gets to go first - computer or human"""
    first_move = 1
    if players == 1:
        while True:
            print("Which one goes first - computer or human?")
            print("1: Human")
            print("2: Computer")
            print("----------------")
            first_move = input("Your choice: ")
            print("----------------")
            time.sleep(DELAY)
            try:
                first_move = int(first_move)
                if first_move == 1:
                    print("All right. Humans first")
                    print("----------------")
                    break
                if first_move == 2:
                    print("All right. Computer goes first")
                    print("----------------")
                    break
                print(ERROR_MESSAGE)
                print("----------------")
            except (TypeError, ValueError):
                print(ERROR_MESSAGE)
                print("----------------")
    return first_move
