import time
import string
from alphabeta import alpha_beta_value, get_rounds
from parameters import delay
from parameters import LARGE_NUMBER, error_message
from tictactoe import TicTacToe


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


def play_computer_turn(state: TicTacToe):
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


def play(state: TicTacToe):
    time.sleep(delay)
    if state.crosses_turn:
        print("Next turn: X")
    else:
        print("Next turn: O")
    print("")
    print(state.state)
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
        print("Stats:")
        print("-Recursion calls:", get_rounds())
        print("----------------")
        print(new_state.state)
        return
    else:
        play(new_state)
