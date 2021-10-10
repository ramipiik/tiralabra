"""User interface for confirming the selections made"""
import time
from parameters import DELAY


def confirm():
    """User interface for confirming the selections made"""
    while True:
        confirmation = input("Press Enter to confirm or c to change the selections: ")
        print("----------------")
        time.sleep(DELAY)
        if confirmation == "":
            print("Great! Game on!")
            print("----------------")
            return True
        if confirmation in ("c", "C"):
            print("Sure, let's take it from the beginning.")
            return False
        print("Come on man! That's neither Enter nor c. Please try again.")
