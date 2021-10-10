"""User interface for asking which level of AI the user wants to play against"""
import time
from parameters import DELAY, ERROR_MESSAGE


def get_level(players):
    """User interface for asking which level of AI the user wants to play against"""
    level = None
    if players in (0, 1):
        while True:
            print("Choose the level of AI that you want to play against?")
            print(
                "(There is no hard, because I ran out of time fine tuning the algorithm..)"
            )
            print("1: Easy")
            print("2: Medium")
            print("----------------")
            level = input("Your choice: ")
            print("----------------")
            time.sleep(DELAY)
            try:
                level = int(level)
                if level in (1, 2):
                    print("Rock'n roll!")
                    print("----------------")
                    time.sleep(DELAY)
                    break
                print(ERROR_MESSAGE)
                print("----------------")
            except (TypeError, ValueError):
                print(ERROR_MESSAGE)
                print("----------------")
    return level
