from alphabeta import TicTacToe
from alphabeta import alpha_beta_value
from alphabeta import LARGE_NUMBER
from alphabeta import get_rounds
from alphabeta import get_max_depth
import time

def play(state:TicTacToe):  
    time.sleep(2)
    # if state.crosses_turn:
    #     print("x:n vuoro siirtää")
    # else:
    #     print("o:n vuoro siirtää")

    print(state)
     
    
    if state.crosses_turn:
        arvo=-LARGE_NUMBER
    else:
        arvo=LARGE_NUMBER
    new_state=""
    lapset=state.generate_children(True)
    # print("lasten määrä", len(lapset))
    for i, siirto in enumerate (lapset):
        siirron_arvo=alpha_beta_value(siirto)
        # print("------------")
        # print(siirto)
        # print("siirron", i, "arvo", siirron_arvo)
        # print("------------")
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
    
    print(new_state)
    if new_state.is_end_state():
        voittaja=""
        print("----------------")
        if new_state.won('o'):
            print("Voittaja: o")
        elif new_state.won('x'):
            print("Voittaja: x")
        else:
            print("Tasapeli")
        print("----------------")
        print("Stats:")
        print("-Rekursiokutsuja: ", get_rounds())
        print("-Max depth:", get_max_depth() )
        print("----------------")
        return
    
    else:
        play (new_state)
 
    # Implement me

# def create_empty_board(size:int):


def settings():
    while True:
        while True:
            print("----------------")
            time.sleep(1)
            print("Kuinka monta pelaajaa? (0, 1 tai 2):")
            print("----------------")
            players=input("Your choice: ")
            print("----------------")
            if int(players)==99:
                return (1,'B',3)
            try:
                players=int(players)
                if players==0 or players==2:
                    print("Got it!", players, "players.")
                    break
                if players==1:
                    print("Got it -", players, "player.")
                    break
                else:
                    print("Hmm. Tuo ei ollut vaihtoehtona. Yritä ystävällisesti uudelleen.")
            except:
                print("Hmm. Tuo ei ollut vaihtoehtona. Yritä ystävällisesti uudelleen.")

        print("----------------")
        time.sleep(1)
        while True:
            print("Minkä kokoisella laudalla haluat pelata?")
            print("A: 3x3 (voittoon vaaditaan kolme peräkkäistä merkkiä)")
            print("B: 5x5 (voittoon vaaditaan neljä peräkkäistä merkkiä)")
            print("C: 7x7 (voittoon vaaditaan neljä peräkkäistä merkkiä)")
            print("D: 10x10 (voittoon vaaditaan viisi peräkkäistä merkkiä)")
            print("E: 15x15 (voittoon vaaditaan viisi peräkkäistä merkkiä)")
            print("F: 20x20 (voittoon vaaditaan viisi peräkkäistä merkkiä)")
            print("G: 25x25 (voittoon vaaditaan viisi peräkkäistä merkkiä)")
            print("----------------")
            board_letter:str=input("Your choice: ")
            print("----------------")
            board_letter=board_letter.capitalize()
            board_size=0
            if board_letter=='A':
                board_size=3
                print(str(board_size)+"x"+str(board_size), "on hyvä valinta!")
                print("----------------")
                break
            elif board_letter=='B':
                board_size=5
                print(str(board_size)+"x"+str(board_size), "on hyvä valinta!")
                print("----------------")
                break
            elif board_letter=='C':
                board_size=7
                print(str(board_size)+"x"+str(board_size), "on hyvä valinta!")
                print("----------------")
                break
            elif board_letter=='D':
                board_size=10
                print(str(board_size)+"x"+str(board_size), "on hyvä valinta!")
                print("----------------")
                break
            elif board_letter=='E':
                board_size=15
                print(str(board_size)+"x"+str(board_size), "on hyvä valinta!")
                print("----------------")
                break
            elif board_letter=='F':
                board_size=20
                print(str(board_size)+"x"+str(board_size), "on hyvä valinta!")
                print("----------------")
                break
            elif board_letter=='G':
                board_size=25
                print(str(board_size)+"x"+str(board_size), "on hyvä valinta!")
                print("----------------")
                break
            else:
                print("Oho. Tuli huti. Yritä uudelleen. :)")   
        time.sleep(1)
        level=0
        if players==0 or players==1:
            while True:
                print("Valitse tekoälyn taso.")
                print("1: helpoin")
                print("2: keskitaso")
                print("3: vaikein")
                print("----------------")
                level=int(input("Please choose: "))
                print("----------------")
                time.sleep(1)
                if level==1 or level==2 or level==3:
                    print("Awesome! Let's recap your choices.")
                    print("----------------")
                    break    
        time.sleep(1)
        print("Players:", players)
        print("Board size:", str(board_size)+"x"+str(board_size))
        if players==0 or players==1:
            print("Level:", level)
        print("----------------")
        time.sleep(1)
        while True:
            print("Press Enter to confirm or c to change the selections.")
            print("----------------")
            confirmation=input()
            print("----------------")
            if confirmation =="":
                print("Great! Game on!")
                print("----------------")
                return (players, board_size, level)
            elif confirmation=="c" or confirmation=="C":
                print("Ok, let's take it one more time from the beginning.")
                break
            else:
                print("That's neither Enter nor c. Please try again :)")
        

def main():
    choices=settings()
    players=choices[0]
    board_size=choices[1]
    level=choices[2]
    # time.sleep(2)
    empty_board = 3 * '???'
    test_board='?x???????'
    # print(type(empty_board))
    state = TicTacToe(test_board, False)
    # print(state)
    play(state)


if __name__ == '__main__':
    main()
