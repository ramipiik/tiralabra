import time
from parameters import delay, error_message


def get_first_move(players):
    first_move = 1
    if players == 1:
        while True:
            print("Which one goes first - computer or human?")
            print("1: Human")
            print("2: Computer")
            print("----------------")
            first_move = input("Your choice: ")
            print("----------------")
            time.sleep(delay)
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
                else:
                    print(error_message)
                    print("----------------")
            except:
                print(error_message)
                print("----------------")
    return first_move
