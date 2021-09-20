from alphabeta import TicTacToe
from alphabeta import alpha_beta_value
from alphabeta import LARGE_NUMBER
from alphabeta import get_rounds
import time
import string

delay=0
def input_move():
    print("What's your move?")

def play(state:TicTacToe):  
    time.sleep(delay)
    if state.crosses_turn:
        print("TURN: x")
    else:
        print("TURN: o")
    print("")
    print(state)
    time.sleep(delay)
    if state.players==2 or (state.players==1 and not state.crosses_turn):        
        print("------------")
        while True:
            print("What's your move? (A1, B2, C3, etc.)")
            print("------------")
            coordinate=input("Your choice: ")
            try:
                letter=coordinate[0]
                number=int(coordinate[1:])
                aux=string.ascii_uppercase.find(letter.capitalize())
                if aux>state.board_size or number>state.board_size or number<1:
                    print("------------")
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
                    new_state=TicTacToe(aux, state.board_size, not state.crosses_turn, state.max_depth, state.players)
                    break
                else:
                    print("------------")
                    print("Sorry, but that one is already taken. Please try again.")
            except:
                print("------------")
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
        
        # print("new_state")
        # print(new_state)
    print("---------------")  
    
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
 

error_message="Well - that was not a valid choice. Please try again."

def settings():
    while True:
        while True:
            print("----------------")
            time.sleep(delay)
            print("0, 1 or 2 players game?")
            print("----------------")
            players=input("Your choice: ")
            print("----------------")
            time.sleep(delay)
            try:
                players=int(players)
                if players==99:
                    return (0,3,3,1)
                if players==0 or players==2:
                    print("Got it!", players, "players.")
                    break
                if players==1:
                    print("Got it -", players, "player.")
                    break
                else:
                    print(error_message)
            except:
                print(error_message)

        print("----------------")
        time.sleep(delay)
        while True:
            print("Choose the size of the board that you want to play with.")
            print("A: 3x3 (takes three in a row to win)")
            print("B: 5x5 (takes four in a row to win)")
            print("C: 7x7 (takes four in a row to win)")
            print("D: 10x10 (takes five in a row to win)")
            print("E: 15x15 (takes five in a row to win)")
            print("F: 20x20 (takes five in a row to win)")
            print("----------------")
            board_letter:str=input("Your choice: ")
            print("----------------")
            time.sleep(delay)
            board_letter=board_letter.capitalize()
            board_size=0
            if board_letter=='A':
                board_size=3
                print(str(board_size)+"x"+str(board_size), "board - good choice!")
                print("----------------")
                break
            elif board_letter=='B':
                board_size=5
                print(str(board_size)+"x"+str(board_size), "board - good choice!")
                print("----------------")
                break
            elif board_letter=='C':
                board_size=7
                print(str(board_size)+"x"+str(board_size), "board - good choice!")
                print("----------------")
                break
            elif board_letter=='D':
                board_size=10
                print(str(board_size)+"x"+str(board_size), "board - good choice!")
                print("----------------")
                break
            elif board_letter=='E':
                board_size=15
                print(str(board_size)+"x"+str(board_size), "board - good choice!")
                print("----------------")
                break
            elif board_letter=='F':
                board_size=20
                print(str(board_size)+"x"+str(board_size), "board - good choice!")
                print("----------------")
                break
            else:
                print(error_message)
                print("----------------")   
        
        time.sleep(delay)
        level=0
        if players==0 or players==1:
            while True:
                print("Choose the level of AI that you want to play against?")
                print("1: Easy")
                print("2: Pro")
                print("3: Deep Blue")
                print("----------------")
                level=input("Your choice: ")
                print("----------------")
                time.sleep(delay)
                try:
                    level=int(level)
                    if level==1 or level==2 or level==3:
                        print("Rock'n roll!")
                        print("----------------")
                        time.sleep(delay)
                        break
                    else:
                        print(error_message)
                        print("----------------")    
                except:
                    print(error_message)
                    print("----------------")
        
        first_move=1

        if players==1:    
            while True:
                print("Which one goes first - computer or human?")
                print("1: Computer")
                print("2: Human")
                print("----------------")
                first_move=input("Your choice: ")
                print("----------------")
                time.sleep(delay)
                try:
                    first_move=int(first_move)
                    if first_move==1:
                        print("All right. Computer goes first")
                        print("----------------")
                        break
                    if first_move==2:
                        print("All right. Humans first")
                        print("----------------")
                        break
                    else:
                        print(error_message)
                        print("----------------")    
                except:
                    print(error_message)
                    print("----------------")
               
        time.sleep(delay)
        print("Awesome! Let's recap your choices.")
        print("----------------")
        print("Players:", players)
        print("Board size:", str(board_size)+"x"+str(board_size))
        if players==0 or players==1:
            if level==1 or level=='1':
                print("Level of AI: 1 (Easy)")
            if level==2:
                print("Level of AI: 2 (Pro)") 
            if level==3:
                print("Level of AI: 3 (Deep Blue)") 
        if players==1:
            if first_move==1:
                print("First move: Computer")
            if first_move==2:
                print("First move: Human")
        print("----------------")
        time.sleep(delay)
        while True:
            confirmation=input ("Press Enter to confirm or c to change the selections: ")
            print("----------------")
            time.sleep(delay)
            # confirmation=input()
            # print("----------------")
            if confirmation =="":
                print("Great! Game on!")
                print("----------------")
                return (players, board_size, level, first_move)
            elif confirmation=="c" or confirmation=="C":
                # print("----------------")
                print("Sure, let's take it from the beginning.")
                break
            else:
                print("Come on - are you trying to hack me?! That's neither Enter nor c. Please try again.")
        

def main():
    user_choices=settings()
    players=user_choices[0]
    board_size=user_choices[1]
    level=user_choices[2]
    first_move=user_choices[3]

    x_starts=False 
    if players==1 and first_move==1:
        x_starts=True #computer plays crosses and gets to go first

    empty_board = 3 * '---'
    # test_board='ABCDEFGHIJKLMNOPQRSTUVWXY'
    test_board_2='oxoxox-----------oxoxoxox'
    test_board_3='oxoxoo--o-----xoxoxoxoxxo'
    test_board_4='------o-o'
    custom_board=(board_size**2) * '-'
    state = TicTacToe(custom_board, board_size, x_starts, level, players)
    play(state)


if __name__ == '__main__':
    main()
