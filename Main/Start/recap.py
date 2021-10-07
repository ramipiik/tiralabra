# Recaps the choices made by the user

def recap(players, board_size, level, first_move):
    print("Awesome! Let's recap your choices.")
    print("----------------")
    print("Players:", players)
    print("Board size:", str(board_size) + "x" + str(board_size))
    if players == 0 or players == 1:
        if level == 1 or level == "1":
            print("Level of AI: 1 (Easy)")
        if level == 2:
            print("Level of AI: 2 (Medium)")
    if players == 1:
        if first_move == 1:
            print("First move: Human")
        if first_move == 2:
            print("First move: Computer")
    print("----------------")
