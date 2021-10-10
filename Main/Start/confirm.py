import time
from parameters import DELAY

# User interface for confirming the selections made


def confirm():
    while True:
        confirmation = input("Press Enter to confirm or c to change the selections: ")
        print("----------------")
        time.sleep(DELAY)
        if confirmation == "":
            print("Great! Game on!")
            print("----------------")
            return True
        elif confirmation == "c" or confirmation == "C":
            print("Sure, let's take it from the beginning.")
            return False
        else:
            print(
                "Come on - are you trying to hack me?! That's neither Enter nor c. Please try again."
            )
