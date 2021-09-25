import time
from parameters import delay
error_message="Well - that was not a valid choice. Please try again."

def start():
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
                    return (1,20,2,1)
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
                print("(There is no hard, because I ran out of time fine tuning the algorithm..)")
                print("1: Easy")
                print("2: Medium")
                print("----------------")
                level=input("Your choice: ")
                print("----------------")
                time.sleep(delay)
                try:
                    level=int(level)
                    if level==1 or level==2:
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
                print("1: Human")
                print("2: Computer")
                print("----------------")
                first_move=input("Your choice: ")
                print("----------------")
                time.sleep(delay)
                try:
                    first_move=int(first_move)
                    if first_move==1:
                        print("All right. Humans first")
                        print("----------------")
                        break
                    if first_move==2:
                        print("All right. Computer goes first")
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
                print("Level of AI: 2 (Medium)") 
        if players==1:
            if first_move==1:
                print("First move: Human")
            if first_move==2:
                print("First move: Computer")
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
        