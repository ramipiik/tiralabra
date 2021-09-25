max_empty_cells=40
center_weight=0.02
LARGE_NUMBER = 1000000
alpha=-1
beta=1
delay=0

#How many marks in a row are required to win
def how_much_to_win(board_size:int):
        if board_size==3:
            return 3
        if board_size==4:
            return 4
        if board_size==5:
            return 4
        if board_size==7:
            return 4
        return 5

#How many recursion rounds are run before switching to heuristics
def recursion_depth(board_size:int):
    if board_size==3:
        return 7
    return 3

#Defines the importance of having marks close to each other
def closeness_weight(level:int):
    if level==2:
        return 0.25
    return 0