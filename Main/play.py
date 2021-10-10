import time
import datetime
import string
from alphabeta import alpha_beta_value, get_rounds, min_value, max_value
from parameters import delay
from parameters import LARGE_NUMBER, error_message
from tictactoe import TicTacToe


# Handles humans turn
def play_human_turn(state: TicTacToe):
    print("------------")
    while True:
        print("What's your move? (A1, B2, C3, etc.)")
        print("------------")
        coordinate = input("Your choice: ")
        print("------------")
        try:
            letter = coordinate[0]
            number = int(coordinate[1:])
            aux = string.ascii_uppercase.find(letter.capitalize())
            if aux > state.board_size or number > state.board_size or number < 1:
                print(error_message)
                print("------------")
                continue
            index = int(aux * state.board_size + number - 1)
            if state.crosses_turn:
                mark = "X"
            else:
                mark = "O"
            if state.state[index] == "-":
                aux = state.state[:index] + mark + state.state[index + 1 :]
                latest_move = (letter, number)
                new_state = TicTacToe(
                    aux, not state.crosses_turn, state.level, state.players, latest_move
                )
                return new_state
            else:
                print("Sorry, but that one is already taken. Please try again.")
        except:
            print(error_message)
            print("------------")


# Handles computer's turns. Calls the minimax algorithm to find the best position.
nr_of_computer_moves = 0


def play_computer_turn(state: TicTacToe):
    global nr_of_computer_moves
    nr_of_computer_moves += 1
    if state.crosses_turn:
        arvo = -LARGE_NUMBER
    else:
        arvo = LARGE_NUMBER
    new_state = ""
    children = state.generate_children()
    for i, siirto in enumerate(children):
        siirron_arvo = alpha_beta_value(siirto)

        if state.crosses_turn:
            if siirron_arvo > arvo:
                arvo = siirron_arvo
                new_state = siirto
                if arvo == 1:
                    break
        if not state.crosses_turn:
            if siirron_arvo < arvo:
                arvo = siirron_arvo
                new_state = siirto
                if arvo == -1:
                    break

    old = state.state
    new = new_state.state
    index = ""
    for i, letter in enumerate(new):
        if letter != old[i]:
            index = i
            break
    row = (index + 1) // state.board_size
    column = index % state.board_size
    latest_move = (string.ascii_uppercase[row], (column + 1))
    if state.crosses_turn:
        player = "X"
    else:
        player = "O"
    print("------------------------------------------------------")
    print(player + " plays to", latest_move[0] + str(latest_move[1]))
    return new_state


start_time = 0
# Coordinates whether to play human or computer turn. Ends the game if the board is full or one of the players won.
def play(state: TicTacToe, input_time=False):
    global start_time
    if not input_time == False:
        start_time = input_time
    time.sleep(delay)
    if state.crosses_turn:
        print("Next turn: X")
    else:
        print("Next turn: O")
    print("")
    print(state)
    time.sleep(delay)

    if state.players == 2 or (state.players == 1 and not state.crosses_turn):
        new_state = play_human_turn(state)
    else:
        new_state = play_computer_turn(state)

    new_state.first_turn = False

    if new_state.is_end_state():
        print(new_state)
        print("----------------")
        if new_state.won("O", new_state.to_win):
            print("AND THE WINNER IS: O")
        elif new_state.won("X", new_state.to_win):
            print("AND THE WINNER IS: X")
        else:
            print("DRAW")
        print("----------------")
        end_time = datetime.datetime.now()
        duration = end_time - start_time
        seconds = duration.total_seconds()
        milliseconds = seconds * 1000
        average = milliseconds / nr_of_computer_moves
        average_rounded = int(round(average, 0))
        print("STATS")
        print("-Recursion calls:", get_rounds())
        print("-Number of computer moves:", nr_of_computer_moves)
        if state.players == 0:
            print(
                "-Average duration per computer move:", average_rounded, "milliseconds"
            )
        return
    else:
        play(new_state)
