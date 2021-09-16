from alphabeta import TicTacToe
from alphabeta import alpha_beta_value
from alphabeta import LARGE_NUMBER
from alphabeta import get_rounds
from alphabeta import get_max_depth
import time




def play(state:TicTacToe):  
    time.sleep(1)
    # if state.crosses_turn:
    #     print("x:n vuoro siirtää")
    # else:
    #     print("o:n vuoro siirtää")

    # print(state)
     
    
    if state.crosses_turn:
        arvo=-LARGE_NUMBER
    else:
        arvo=LARGE_NUMBER
    new_state=""
    children=state.generate_children(True)
    # print("lasten määrä", len(lapset))
    moves=LARGE_NUMBER

    for i, siirto in enumerate (children):
        (siirron_arvo, nr_moves)=alpha_beta_value(siirto)
        
        # print("------------")
        # print(siirto)
        # print("siirron", i, "arvo", siirron_arvo)
        # print("------------")
        
        if state.crosses_turn:
            if siirron_arvo>arvo:
                arvo=siirron_arvo
                new_state=siirto
                moves=nr_moves
                # if arvo==1: #lopetetaan heti kun löytyy voittava peli. nopeuttaa algoritmia, mutta johtaa joskus oudon oloisiin peleihin, kun voittavan siirron näkee suoraan silmällä
                #     break
            if arvo==1 and siirron_arvo==1:
                if nr_moves<moves:
                    new_state=siirto

        if not state.crosses_turn:
            if siirron_arvo<arvo:
                arvo=siirron_arvo
                new_state=siirto
                moves=nr_moves
                # moves=count_moves(siirto)
                # if arvo==-1:#lopetetaan heti kun löytyy voittava peli. nopeuttaa algoritmia, mutta johtaa joskus oudon oloisiin peleihin, kun voittavan siirron näkee suoraan silmällä
                #     break
            if arvo==-1 and siirron_arvo==-1:
                if nr_moves<moves:
                    new_state=siirto
    
    # print("checkpoint")
    print(new_state)
    if new_state.is_end_state()[0]:
        voittaja=""
        print("----------------")
        if new_state.won('o'):
            print("AND THE WINNER IS: o")
        elif new_state.won('x'):
            print("AND THE WINNER IS: x")
        else:
            print("DRAW")
        print("----------------")
        print("Stats:")
        print("-Recursion calls:", get_rounds())
        print("-Max depth:", get_max_depth() )
        print("----------------")
        return
    
    else:
        play (new_state)
 
    # Implement me

# def create_empty_board(size:int):

error_message="Well - that was not a valid choice. Let's try again."

def settings():
    while True:
        while True:
            print("----------------")
            time.sleep(1)
            print("0, 1 or 2 players game?")
            print("----------------")
            players=input("Your choice: ")
            print("----------------")
            time.sleep(1)
            try:
                players=int(players)
                if players==99:
                    return (1,5,3)
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
        time.sleep(1)
        while True:
            print("Choose the size of the board that you want to play with.")
            print("A: 3x3 (takes three in a row to win)")
            print("B: 5x5 (takes four in a row to win)")
            print("C: 7x7 (takes four in a row to win)")
            print("D: 10x10 (takes five in a row to win)")
            print("E: 15x15 (takes five in a row to win)")
            print("F: 20x20 (takes five in a row to win)")
            print("G: 25x25 (takes five in a row to win)")
            print("----------------")
            board_letter:str=input("Your choice: ")
            print("----------------")
            time.sleep(1)
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
            elif board_letter=='G':
                board_size=25
                print(str(board_size)+"x"+str(board_size), "board - good choice!")
                print("----------------")
                break
            else:
                print(error_message)
                print("----------------")   
        
        time.sleep(1)
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
                time.sleep(1)
                try:
                    level=int(level)
                    if level==1 or level==2 or level==3:
                        print("Awesome! Let's recap your choices.")
                        print("----------------")
                        break
                    else:
                        print(error_message)
                        print("----------------")    
                except:
                    print(error_message)
                    print("----------------")
               
        time.sleep(1)
        print("Players:", players)
        print("Board size:", str(board_size)+"x"+str(board_size))
        if players==0 or players==1:
            if level==1:
                print("Level of AI: 1 (Easy)")
            if level==2:
                print("Level of AI: 2 (Pro)") 
            if level==3:
                print("Level of AI: 3 (Deep Blue)") 
        print("----------------")
        time.sleep(1)
        while True:
            confirmation=input ("Press Enter to confirm or c to change the selections: ")
            print("----------------")
            time.sleep(1)
            # confirmation=input()
            # print("----------------")
            if confirmation =="":
                print("Great! Game on!")
                print("----------------")
                return (players, board_size, level)
            elif confirmation=="c" or confirmation=="C":
                # print("----------------")
                print("Sure, let's take it from the beginning.")
                break
            else:
                print("Come on man! That's neither Enter nor c. Please try again.")
        

def main():
    user_choices=settings()
    players=user_choices[0]
    board_size=user_choices[1]
    level=user_choices[2]
    # time.sleep(2)
    empty_board = 3 * '???'
    # test_board='ABCDEFGHIJKLMNOPQRSTUVWXY'
    test_board_2='oxoxox----x------oxoxoxox'
    custom_board=(board_size**2) * '-'
    # print(type(empty_board))
    state = TicTacToe(test_board_2, board_size, False)
    # state = TicTacToe(custom_board, board_size, False)
    
    # state.won('x')
    print(state)
    play(state)


if __name__ == '__main__':
    main()
