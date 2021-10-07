from parameters import delay, error_message
import time

# User interface for asking for the board size from the user


def get_board():
    while True:
        print("Choose the size of the board that you want to play with.")
        print("A: 3x3 (takes three in a row to win)")
        print("B: 5x5 (takes four in a row to win)")
        print("C: 7x7 (takes four in a row to win)")
        print("D: 10x10 (takes five in a row to win)")
        print("E: 15x15 (takes five in a row to win)")
        print("F: 20x20 (takes five in a row to win)")
        print("----------------")
        board_letter = input("Your choice: ")
        print("----------------")
        time.sleep(delay)

        try:
            board_letter = board_letter.capitalize()
        except:
            continue
        board_size = 0
        if board_letter == "A":
            board_size = 3
            print(str(board_size) + "x" + str(board_size), "board - good choice!")
            print("----------------")
            break
        elif board_letter == "B":
            board_size = 5
            print(str(board_size) + "x" + str(board_size), "board - good choice!")
            print("----------------")
            break
        elif board_letter == "C":
            board_size = 7
            print(str(board_size) + "x" + str(board_size), "board - good choice!")
            print("----------------")
            break
        elif board_letter == "D":
            board_size = 10
            print(str(board_size) + "x" + str(board_size), "board - good choice!")
            print("----------------")
            break
        elif board_letter == "E":
            board_size = 15
            print(str(board_size) + "x" + str(board_size), "board - good choice!")
            print("----------------")
            break
        elif board_letter == "F":
            board_size = 20
            print(str(board_size) + "x" + str(board_size), "board - good choice!")
            print("----------------")
            break
        else:
            print(error_message)
            print("----------------")
    return board_size
