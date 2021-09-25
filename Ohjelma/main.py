from alphabeta import TicTacToe
from alphabeta import alpha_beta_value
from parameters import LARGE_NUMBER
from alphabeta import get_rounds
from tictactoe import TicTacToe
import time
import string
from start import start
from parameters import delay


latest_move=""

def input_move():
    print("What's your move?")

def play(state:TicTacToe):  
    time.sleep(delay)
    global latest_move
    if state.crosses_turn:
        print("TURN: X")
    else:
        print("TURN: O")
    print("")
    print(state)
    time.sleep(delay)
    if state.players==2 or (state.players==1 and not state.crosses_turn):        
        print("------------")
        while True:
            print("What's your move? (A1, B2, C3, etc.)")
            print("------------")
            coordinate=input("Your choice: ")
            print("------------")
            try:
                letter=coordinate[0]
                number=int(coordinate[1:])
                aux=string.ascii_uppercase.find(letter.capitalize())
                if aux>state.board_size or number>state.board_size or number<1:
                    # print("------------")
                    print(error_message)
                    print("------------")
                    continue   
                index=int(aux*state.board_size+number-1)
                if state.crosses_turn:
                    mark="X"
                else:
                    mark="O"
                if state.state[index]=='-':
                    aux=state.state[:index]+mark+state.state[index+1:]
                    latest_move=(letter, number)
                    # print("latest move from play", latest_move)
                    new_state=TicTacToe(aux, state.board_size, not state.crosses_turn, state.level, state.players, latest_move)
                    break
                else:
                    # print("------------")
                    print("Sorry, but that one is already taken. Please try again.")
            except:
                # print("------------")
                print(error_message)
                print("------------")
            
    
    else:
        if state.crosses_turn:
            arvo=-LARGE_NUMBER
        else:
            arvo=LARGE_NUMBER
        new_state=""
        children=state.generate_children(True)
        for i, siirto in enumerate (children):
            siirron_arvo=alpha_beta_value(siirto)                     
            
            if state.crosses_turn:
                if siirron_arvo>arvo:
                    arvo=siirron_arvo
                    new_state=siirto
                    if arvo==1:
                        break
            if not state.crosses_turn:
                if siirron_arvo<arvo:
                    arvo=siirron_arvo
                    new_state=siirto
                    if arvo==-1:
                        break
        
        old=state.state
        new=new_state.state
        index=""
        for i, letter in enumerate (new):
            if letter!=old[i]:
                index=i
                break
        row=(index+1)//state.board_size
        column=index%state.board_size
        latest_move=(string.ascii_uppercase[row], (column+1))
        if state.crosses_turn:
            player="X"
        else:
            player="O"
        print(player+" plays to", latest_move[0]+str(latest_move[1]))
        print("---------------")

    new_state.first_turn=False
    if new_state.is_end_state():
        print(new_state)
        print("----------------")
        if new_state.won('O', new_state.to_win):
            print("AND THE WINNER IS: O")
        elif new_state.won('X', new_state.to_win):
            print("AND THE WINNER IS: X")
        else:
            print("DRAW")
        print("----------------")
        print("Stats:")
        print("-Recursion calls:", get_rounds())
        print("----------------")
        return    
    else:
        play (new_state)
 



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
    midpoint=(string.ascii_uppercase[board_size//2], board_size//2)
    state = TicTacToe(custom_board, board_size, x_starts, level, players, midpoint, True)
    play(state)

if __name__ == '__main__':
    main()
