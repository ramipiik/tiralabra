from alphabeta import TicTacToe
from alphabeta import alpha_beta_value
from alphabeta import LARGE_NUMBER
from alphabeta import get_rounds
import time


delay=0.3

def input_move():
    print("What's your move?")


def play(state:TicTacToe):  
    time.sleep(delay)
    if state.crosses_turn:
        print("x:n vuoro siirtää")
        print("")
        print("")
    else:
        print("o:n vuoro siirtää")
        print("")
        print("")

    # print(state)
     
    
    if state.crosses_turn:
        arvo=-LARGE_NUMBER
    else:
        arvo=LARGE_NUMBER
    new_state=""
    children=state.generate_children(True)
    # print("lasten määrä", len(lapset))
    # moves=LARGE_NUMBER
    min_depth=999
    max_depth=-999

    for i, siirto in enumerate (children):
        # print("siirto_state from play")
        # print(siirto.state)
        (siirron_arvo, min_moves, max_moves, min_depth, max_depth)=alpha_beta_value(siirto)
        print("------------")
        # print("depth", depth)
        print("siirron", i, "arvo", siirron_arvo)
        print("min_depth",min_depth)
        print("max_depth",max_depth)
        print("------------")
        # print(siirto)
        
        # print("------------")
        
        if state.crosses_turn:
            # print("min_moves at checkpoint 0", min_moves)
            # print("max_moves at checkpoint 0", max_moves)
            # print("siirron arvo", siirron_arvo)
            # print("siirron numero", i)
            # print(siirto)
            
            if i==0:
                arvo=siirron_arvo
                new_state=siirto
                moves=min_moves
                depth=(min_depth, max_depth)
                valittu_siirto= i
            else:
                if siirron_arvo>arvo:
                    arvo=siirron_arvo
                    new_state=siirto
                    moves=min_moves
                    depth=min_depth
                    valittu_siirto= i
                    # if arvo==1: #lopetetaan heti kun löytyy voittava peli. nopeuttaa algoritmia, mutta johtaa joskus oudon oloisiin peleihin, kun voittavan siirron näkee suoraan silmällä
                    #     break
                elif arvo==1 and siirron_arvo==1:
                    # if max_moves<moves:
                    #     moves=max_moves
                    #     new_state=siirto
                    #     valittu_siirto= i
                    try:
                        if max_depth<depth:
                            depth=max_depth
                            new_state=siirto
                            valittu_siirto= i
                    except:
                        if max_depth<depth[1]:
                            depth=max_depth
                            new_state=siirto
                            valittu_siirto= i

                elif arvo==-1 and siirron_arvo==-1:
                    # if max_moves>moves:
                    #     moves=max_moves
                    #     new_state=siirto
                    #     valittu_siirto= i
                    try:
                        if min_depth>depth:
                            depth=min_depth
                            new_state=siirto
                            valittu_siirto= i
                    except:
                        if min_depth>depth[0]:
                            depth=min_depth
                            new_state=siirto
                            valittu_siirto= i

        if not state.crosses_turn:
            # print("nr_moves at checkpoint 1", nr_moves)
            # print("siirron arvo", siirron_arvo)
            # print("siirron numero", i)
            # print(siirto)
            
            if i==0:
                arvo=siirron_arvo
                new_state=siirto
                moves=min_moves
                depth=(min_depth, max_depth)
                valittu_siirto=i 
            else:

                if siirron_arvo<arvo:
                    arvo=siirron_arvo
                    new_state=siirto
                    valittu_siirto= i
                    moves=min_moves
                    depth=min_depth
                    # print("yo. valittu A")
                
                    # if arvo==-1:#lopetetaan heti kun löytyy voittava peli. nopeuttaa algoritmia, mutta johtaa joskus oudon oloisiin peleihin, kun voittavan siirron näkee suoraan silmällä
                    #     break
                elif arvo==-1 and siirron_arvo==-1:
                    # if max_moves<moves:
                    #     moves=max_moves
                    #     new_state=siirto
                    #     valittu_siirto= i
                    #     # print("yo. valittu B")
                    try:
                        if max_depth<depth:
                            depth=max_depth
                            new_state=siirto
                            valittu_siirto= i
                    except:
                        if max_depth<depth[1]:
                            depth=max_depth
                            new_state=siirto
                            valittu_siirto= i
                elif arvo==1 and siirron_arvo==1:
                    # print("moves", moves)
                    # print("nr_moves", nr_moves)
                    # print("i", i)
                    # if min_moves>moves:
                    #     moves=min_moves
                    #     new_state=siirto
                    #     valittu_siirto= i
                        # print("yo. valittu C")
                    try:
                        if min_depth>depth:
                            depth=min_depth
                            new_state=siirto
                            valittu_siirto= i
                    except:
                        if min_depth>depth[0]:
                            depth=min_depth
                            new_state=siirto
                            valittu_siirto= i
        # print("----------")
    # 
    # print("valitun siirron movesit", moves)
    print("valitun siirron arvo", arvo)
    print("valitun siirron min_syvyys", min_depth)
    print("valitun siirron max_syvyys", max_depth)
    print("valitun siiron numero", valittu_siirto)
    print("---------------")  
    print("checkpoint")
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
            time.sleep(delay)
            print("0, 1 or 2 players game?")
            print("----------------")
            players=input("Your choice: ")
            print("----------------")
            time.sleep(delay)
            try:
                players=int(players)
                if players==99:
                    return (1,3,1,1)
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
            print("G: 25x25 (takes five in a row to win)")
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
            elif board_letter=='G':
                board_size=25
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
                print("Come on man! That's neither Enter nor c. Please try again.")
        

def main():
    user_choices=settings()
    players=user_choices[0]
    board_size=user_choices[1]
    level=user_choices[2]
    first_move=user_choices[3]
    # time.sleep(2)
    empty_board = 3 * '---'
    # test_board='ABCDEFGHIJKLMNOPQRSTUVWXY'
    test_board_2='oxoxox-----------oxoxoxox'
    test_board_3='oxoxoo--o-----xoxoxoxoxxo'
    custom_board=(board_size**2) * '-'
    test_board_4='-----o--o'
    # print(type(empty_board))
    x_starts=False 
    if players==1 and first_move==1:
        x_starts=True #computer plays crosses and gets to go first
    state = TicTacToe(test_board_4, board_size, x_starts)
    # state = TicTacToe(custom_board, board_size, False)
    if x_starts:
        print("x starts from the below position")
    else:
        print("o starts from the below position")
    print("--------------")
    # state.won('x')
    
    print(state)
    play(state)


if __name__ == '__main__':
    main()
