import time
from parameters import delay

def confirm():
    while True:
        confirmation=input ("Press Enter to confirm or c to change the selections: ")
        print("----------------")
        time.sleep(delay)
        if confirmation =="":
            print("Great! Game on!")
            print("----------------")
            return True
        elif confirmation=="c" or confirmation=="C":
            # print("----------------")
            print("Sure, let's take it from the beginning.")
            return False
        else:
            print("Come on - are you trying to hack me?! That's neither Enter nor c. Please try again.")