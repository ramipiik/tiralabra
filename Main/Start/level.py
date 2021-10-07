from parameters import delay, error_message
import time

# User interface for asking which level of AI the user wants to play against


def get_level(players):
    if players == 0 or players == 1:
        level = 0
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
            time.sleep(delay)
            try:
                level = int(level)
                if level == 1 or level == 2:
                    print("Rock'n roll!")
                    print("----------------")
                    time.sleep(delay)
                    break
                else:
                    print(error_message)
                    print("----------------")
            except:
                print(error_message)
                print("----------------")
        return level
