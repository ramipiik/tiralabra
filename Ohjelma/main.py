from tictactoe import TicTacToe
from start import start
from play import play

def main():
    user_choices=start()
    players=user_choices[0]
    board_size=user_choices[1]
    level=user_choices[2]
    first_move=user_choices[3]

    if first_move==2:
        x_starts=True
    else:
        x_starts=False

    custom_board=(board_size**2) * '-'
    state = TicTacToe(custom_board, board_size, x_starts, level, players, True)
    play(state)

main()
