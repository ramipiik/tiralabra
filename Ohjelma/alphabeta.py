LARGE_NUMBER = 1000000
import string
from Heuristics import basic_check
from Heuristics import boundaries_check
from Heuristics import closeness_check


class TicTacToe():
    def __init__(self, state, board_size, crosses_turn, level, players,latest_move:tuple, first_turn=False):
        self.state = state
        self.board_size=board_size
        self.crosses_turn = crosses_turn
        self.to_win=5
        self.players=players
        self.level=level
        self.latest_move=latest_move

        if self.board_size==3:
            self.to_win=3
        if self.board_size==4:
            self.to_win=4
        if self.board_size==5:
            self.to_win=4
        if self.board_size==7:
            self.to_win=4
        

        self.max_depth=3
        if board_size==3:
            self.max_depth=7
        if board_size==5:
            self.max_depth=4
        
        self.closeness_weight=0
        if level==2:
            self.closeness_weight=0.25

        self.center_weight=0.02

        self.heuristics_limit=40

        self.first_turn=first_turn

    def is_end_state(self):
        if ('-' not in self.state) or self.won('X', self.to_win) or self.won('O', self.to_win):
            return True
        else:
            return False



    def won(self, mark, n):
        combo = n * mark

        #checks horizontal_lines
        for i in range (self.board_size):
            rivi:str=self.state[i*self.board_size:i*self.board_size+self.board_size]
            # print(rivi)
            if rivi.__contains__(combo):
                # print("voitto")
                return True
        
        #checks vertical_lines
        for i in range (self.board_size):
            rivi=""
            for j in range (self.board_size):
                rivi+=self.state[j*self.board_size+i]
            # print(rivi)
            if rivi.__contains__(combo):
                # print("voitto")
                return True
        
        #checks diagonal lines from top row to right-down
        for i in range (self.board_size):
            rivi=""
            if i<=self.board_size-self.to_win:
                for j in range(self.board_size):
                    if i+j*(self.board_size+1)<self.board_size**2:
                        rivi+=self.state[i+j*(self.board_size+1)]
                # print(rivi)
            if rivi.__contains__(combo):
                # print("voitto")
                return True

        #checks diagonal lines from top row to left-down
        # print("checkpoint 1")
        for i in range (self.board_size-1,-1,-1):
            max_length=i+1
            rivi=""
            if i>=self.to_win-1:
                for j in range(self.board_size):
                    if len(rivi)<max_length:
                        rivi+=self.state[i+j*(self.board_size-1)]
                # print(rivi)
            if rivi.__contains__(combo):
                # print("voitto")
                return True
            

        #checks diagonal lines from left column to right-down
        for j in range (1, self.board_size): #top-left corner has already been checked. Thus starting from row 1.
            max_length=self.board_size-j
            rivi=""
            if j<=self.board_size-self.to_win:
                for i in range(self.board_size):
                    if len(rivi)<max_length:
                        rivi+=self.state[j*self.board_size+i*(self.board_size+1)]
                # print(rivi)
            if rivi.__contains__(combo):
                # print("voitto")
                return True

        #checks diagonal lines from right column to left-down
        # print("checkpoint 2")
        for j in range (1, self.board_size): #top-right corner has already been checked. Thus starting from row 1.
            max_length=self.board_size-j
            rivi=""
            if j<=self.board_size-self.to_win:
                for i in range(self.board_size):
                    if len(rivi)<max_length:
                        rivi+=self.state[(self.board_size-1)+j*(self.board_size)+i*(self.board_size-1)]
                # print(rivi)
            if rivi.__contains__(combo):
                # print("voitto")
                return True

        return False


    def heuristics_check_mustwins(self, mark, n):
        combos=[]
        winning_combos_2=[]
        winning_combos_3=[]
        winning_combos_4=[]
        
        if n==2:
            combo='-'+mark+mark+'-'
            winning_combos_2.append(combo)

        if n==3:
            combo='-'+mark+mark+mark+'-'
            winning_combos_3.append(combo)
      
        if n==4:
            combo='-'+mark+mark+mark+mark+'-'
            winning_combos_4.append(combo)

        
        if n==2:
            combos=winning_combos_2
        if n==3:
            combos=winning_combos_3
        if n==4:
            combos=winning_combos_4
        
        count=0

        #checks horizontal_lines
        for i in range (self.board_size):
            rivi:str=self.state[i*self.board_size:i*self.board_size+self.board_size]
            # print(rivi)
            for combo in combos:
                if rivi.__contains__(combo):
                    # print("mark", mark, "osuma rivillä", rivi)
                    count+=1
                    # print("count", count)
        
        #checks vertical_lines
        for i in range (self.board_size):
            rivi=""
            for j in range (self.board_size):
                rivi+=self.state[j*self.board_size+i]
            # print(rivi)
            for combo in combos:
                if rivi.__contains__(combo):
                    # print("mark", mark, "osuma rivillä", rivi)
                    count+=1
                    # print("count", count)
        
        #checks diagonal lines from top row to right-down
        for i in range (self.board_size):
            rivi=""
            if i<=self.board_size-n-1: ######### CORRECTION
                for j in range(self.board_size):
                    if i+j*(self.board_size+1)<self.board_size**2:
                        rivi+=self.state[i+j*(self.board_size+1)]
                # print(rivi)
            for combo in combos:
                if rivi.__contains__(combo):
                    # print("mark", mark, "osuma rivillä", rivi)
                    count+=1
                    # print("count", count)

        #checks diagonal lines from top row to left-down
        # print("checkpoint 1")
        for i in range (self.board_size-1,-1,-1):
            max_length=i+1
            rivi=""
            if i>=n: ######### CORRECTION
                for j in range(self.board_size):
                    if len(rivi)<max_length:
                        rivi+=self.state[i+j*(self.board_size-1)]
                # print(rivi)
            for combo in combos:
                if rivi.__contains__(combo):
                    # print("mark", mark, "osuma rivillä", rivi)
                    count+=1
                    # print("count", count)

        #checks diagonal lines from left column to right-down
        for j in range (1, self.board_size): #top-left corner has already been checked. Thus starting from row 1.
            max_length=self.board_size-j
            rivi=""
            if j<=self.board_size-n-1:  ######### CORRECTION
                for i in range(self.board_size):
                    if len(rivi)<max_length:
                        rivi+=self.state[j*self.board_size+i*(self.board_size+1)]
                # print(rivi)
            for combo in combos:
                if rivi.__contains__(combo):
                    # print("mark", mark, "osuma rivillä", rivi)
                    count+=1
                    # print("count", count)

        #checks diagonal lines from right column to left-down
        # print("checkpoint 2")
        for j in range (1, self.board_size): #top-right corner has already been checked. Thus starting from row 1.
            max_length=self.board_size-j
            rivi=""
            if j<=self.board_size-n-1:  ######### CORRECTION
                for i in range(self.board_size):
                    if len(rivi)<max_length:
                        rivi+=self.state[(self.board_size-1)+j*(self.board_size)+i*(self.board_size-1)]
                # print(rivi)
            for combo in combos:
                if rivi.__contains__(combo):
                    # print("mark", mark, "osuma rivillä", rivi)
                    count+=1
                    # print("count", count)

        return count


    def heuristics_prevent_mustwins(self, mark, n):
        combos=[]
        winning_combos_2=[]
        winning_combos_3=[]
        winning_combos_4=[]

        if n==3:
            combo='-'+mark+'-'+mark+'-'
            winning_combos_3.append(combo)
            combo='-'+mark+mark+'-'+'-'
            winning_combos_3.append(combo)
            combo='-'+'-'+mark+mark+'-'
            winning_combos_3.append(combo)

        if n==4:
            combo='-'+mark+'-'+mark+mark+'-'
            winning_combos_4.append(combo)
            combo='-'+mark+mark+'-'+mark+'-'
            winning_combos_4.append(combo)
            combo='-'+mark+mark+mark+'-'+'-'
            winning_combos_4.append(combo)
            combo='-'+'-'+mark+mark+mark+'-'
            winning_combos_4.append(combo)

        if n==3:
            combos=winning_combos_3
        if n==4:
            combos=winning_combos_4
        
        count=0

        #checks horizontal_lines
        for i in range (self.board_size):
            rivi:str=self.state[i*self.board_size:i*self.board_size+self.board_size]
            # print(rivi)
            for combo in combos:
                if rivi.__contains__(combo):
                    # print("mark", mark, "osuma rivillä", rivi)
                    count+=1
                    # print("count", count)
        
        #checks vertical_lines
        for i in range (self.board_size):
            rivi=""
            for j in range (self.board_size):
                rivi+=self.state[j*self.board_size+i]
            # print(rivi)
            for combo in combos:
                if rivi.__contains__(combo):
                    # print("mark", mark, "osuma rivillä", rivi)
                    count+=1
                    # print("count", count)
        
        #checks diagonal lines from top row to right-down
        for i in range (self.board_size):
            rivi=""
            if i<=self.board_size-n-1: ######### CORRECTION
                for j in range(self.board_size):
                    if i+j*(self.board_size+1)<self.board_size**2:
                        rivi+=self.state[i+j*(self.board_size+1)]
                # print(rivi)
            for combo in combos:
                if rivi.__contains__(combo):
                    # print("mark", mark, "osuma rivillä", rivi)
                    count+=1
                    # print("count", count)

        #checks diagonal lines from top row to left-down
        # print("checkpoint 1")
        for i in range (self.board_size-1,-1,-1):
            max_length=i+1
            rivi=""
            if i>=n: ######### CORRECTION
                for j in range(self.board_size):
                    if len(rivi)<max_length:
                        rivi+=self.state[i+j*(self.board_size-1)]
                # print(rivi)
            for combo in combos:
                if rivi.__contains__(combo):
                    # print("mark", mark, "osuma rivillä", rivi)
                    count+=1
                    # print("count", count)

        #checks diagonal lines from left column to right-down
        for j in range (1, self.board_size): #top-left corner has already been checked. Thus starting from row 1.
            max_length=self.board_size-j
            rivi=""
            if j<=self.board_size-n-1:  ######### CORRECTION
                for i in range(self.board_size):
                    if len(rivi)<max_length:
                        rivi+=self.state[j*self.board_size+i*(self.board_size+1)]
                # print(rivi)
            for combo in combos:
                if rivi.__contains__(combo):
                    # print("mark", mark, "osuma rivillä", rivi)
                    count+=1
                    # print("count", count)

        #checks diagonal lines from right column to left-down
        # print("checkpoint 2")
        for j in range (1, self.board_size): #top-right corner has already been checked. Thus starting from row 1.
            max_length=self.board_size-j
            rivi=""
            if j<=self.board_size-n-1:  ######### CORRECTION
                for i in range(self.board_size):
                    if len(rivi)<max_length:
                        rivi+=self.state[(self.board_size-1)+j*(self.board_size)+i*(self.board_size-1)]
                # print(rivi)
            for combo in combos:
                if rivi.__contains__(combo):
                    # print("mark", mark, "osuma rivillä", rivi)
                    count+=1
                    # print("count", count)

        return count


    def heuristics_sanity_check(self, mark, n):
        combos=[]
        combos_2=[]
        combos_3=[]
        combos_4=[]
        
        
        if n==2:
            combo='-'+mark+mark
            combos_2.append(combo)

            combo=mark+mark+'-'
            combos_2.append(combo)

            combo=mark+'-'+mark
            combos_2.append(combo)


        if n==3:
            combo=mark+'-'+mark+mark
            combos_3.append(combo)
            
            combo=mark+mark+'-'+mark
            combos_3.append(combo)

            combo=mark+mark+mark+'-'
            combos_3.append(combo)

            combo='-'+mark+mark+mark
            combos_3.append(combo)

        if n==4:
            combo=mark+'-'+mark+mark+mark
            combos_4.append(combo)

            combo=mark+mark+'-'+mark+mark
            combos_4.append(combo)

            combo=mark+mark+mark+'-'+mark
            combos_4.append(combo)

            combo='-'+mark+mark+mark+mark
            combos_4.append(combo)

            combo=mark+mark+mark+mark+'-'
            combos_4.append(combo)
        
        if n==2:
            combos=combos_2
        if n==3:
            combos=combos_3
        if n==4:
            combos=combos_4
        
        count=0

        #checks horizontal_lines
        for i in range (self.board_size):
            rivi:str=self.state[i*self.board_size:i*self.board_size+self.board_size]
            # print(rivi)
            for combo in combos:
                if rivi.__contains__(combo):
                    # print("mark", mark, "osuma rivillä", rivi)
                    count+=1
                    # print("count", count)
        
        #checks vertical_lines
        for i in range (self.board_size):
            rivi=""
            for j in range (self.board_size):
                rivi+=self.state[j*self.board_size+i]
            # print(rivi)
            for combo in combos:
                if rivi.__contains__(combo):
                    # print("mark", mark, "osuma rivillä", rivi)
                    count+=1
                    # print("count", count)
        
        #checks diagonal lines from top row to right-down
        for i in range (self.board_size):
            rivi=""
            if i<=self.board_size-n-1: #######CORRECTION
                for j in range(self.board_size):
                    if i+j*(self.board_size+1)<self.board_size**2:
                        rivi+=self.state[i+j*(self.board_size+1)]
                # print(rivi)
            for combo in combos:
                if rivi.__contains__(combo):
                    # print("checkpoint 1. mark", mark, "osuma rivillä", rivi)
                    count+=1
                    # print("count", count)

        #checks diagonal lines from top row to left-down
        # print("checkpoint 1")
        for i in range (self.board_size-1,-1,-1):
            max_length=i+1
            rivi=""
            if i>=n: ########CORRECTION
                for j in range(self.board_size):
                    if len(rivi)<max_length:
                        rivi+=self.state[i+j*(self.board_size-1)]
                # print(rivi)
            for combo in combos:
                if rivi.__contains__(combo):
                    # print("checkpoint 2. mark", mark, "osuma rivillä", rivi)
                    count+=1
                    # print("count", count)

        #checks diagonal lines from left column to right-down
        for j in range (1, self.board_size): #top-left corner has already been checked. Thus starting from row 1.
            max_length=self.board_size-j
            rivi=""
            if j<=self.board_size-n-1: #########CORRECTION
                for i in range(self.board_size):
                    if len(rivi)<max_length:
                        rivi+=self.state[j*self.board_size+i*(self.board_size+1)]
                # print(rivi)
            for combo in combos:
                if rivi.__contains__(combo):
                    # print("checkpoint 3. mark", mark, "osuma rivillä", rivi)
                    count+=1
                    # print("count", count)

        #checks diagonal lines from right column to left-down
        # print("checkpoint 2")
        for j in range (1, self.board_size): #top-right corner has already been checked. Thus starting from row 1.
            max_length=self.board_size-j
            rivi=""
            if j<=self.board_size-n-1: #########CORRECTION
                for i in range(self.board_size):
                    if len(rivi)<max_length:
                        rivi+=self.state[(self.board_size-1)+j*(self.board_size)+i*(self.board_size-1)]
                # print(rivi)
            for combo in combos:
                if rivi.__contains__(combo):
                    # print("checkpoitn 4. mark", mark, "osuma rivillä", rivi)
                    count+=1
                    # print("count", count)

        return count  

    
    def heuristics_coordinator(self):        
        x_closeness_bonus=closeness_check.closeness_check(self,'X')*self.closeness_weight
        o_closeness_bonus=closeness_check.closeness_check(self,'O')*self.closeness_weight
        
        #Reverses the closeness check for the first turn. Purpose is to steer computers first move close to humans first move.
        if self.count_empty()==self.board_size**2-2:
            x_closeness_bonus=closeness_check.closeness_check(self, 'X', True)*self.closeness_weight

        # center_weight=0.02
        x_center_bonus=boundaries_check.boundaries_check(self, 'X')*self.center_weight
        o_center_bonus=boundaries_check.boundaries_check(self, 'O')*self.center_weight

        if self.to_win==3:
            if self.crosses_turn:
                x_2_wins=self.heuristics_sanity_check('X', 2)
                if x_2_wins>0:
                    return 0.9 + x_closeness_bonus +  x_center_bonus
            
            if not self.crosses_turn:
                o_2_wins=self.heuristics_sanity_check('O', 2)
                if o_2_wins>0:
                    return -0.9 - o_closeness_bonus -  o_center_bonus
        
        if self.to_win==4:
            if self.crosses_turn:
                x_3_wins=self.heuristics_sanity_check('X', 3)
                if x_3_wins>0:
                # print (self)
                # print("HÄLYTYS! seuraavaksi on x:n vuoro. Älä laita o:aa tähän")
                # print("-------------------")
                # input("press any key 1..")
                    return 0.9 + x_closeness_bonus +  x_center_bonus
            if not self.crosses_turn:
                o_3_wins=self.heuristics_sanity_check('O', 3)
                if o_3_wins>0:
                    # print (self)
                    # print("HÄLYTYS! seuraavaksi on o:n vuoro. Älä laita x:ää tähän")
                    # input("press any key 2..")
                    # print("-------------------")
                    return -0.9 - o_closeness_bonus -  o_center_bonus
        
        if self.to_win==5:
            if self.crosses_turn:
                x_4_wins=self.heuristics_sanity_check('X', 4)
                if x_4_wins>0:
                    return 0.9 + x_closeness_bonus +  x_center_bonus
            if not self.crosses_turn:
                o_4_wins=self.heuristics_sanity_check('O', 4)
                if o_4_wins>0:
                    return -0.9 - o_closeness_bonus -  o_center_bonus



        if self.to_win==3:
            x_2_wins=self.heuristics_check_mustwins('X', 2)
            if x_2_wins>0:
                return 0.8 + x_closeness_bonus +  x_center_bonus
            o_2_wins=self.heuristics_check_mustwins('O', 2)
            if o_2_wins>0:
                return -0.8 - o_closeness_bonus -  o_center_bonus
        
        if self.to_win==4:
            x_3_wins=self.heuristics_check_mustwins('X', 3)
            if x_3_wins>0:
                return 0.8 + x_closeness_bonus +  x_center_bonus
            o_3_wins=self.heuristics_check_mustwins('O', 3)
            if o_3_wins>0:
                return -0.8 - o_closeness_bonus -  o_center_bonus

        
        if self.to_win==5:
            x_4_wins=self.heuristics_check_mustwins('X', 4)
            if x_4_wins>0:
                return 0.8 + x_closeness_bonus +  x_center_bonus
            o_4_wins=self.heuristics_check_mustwins('O', 4)
            if o_4_wins>0:
                return -0.8 - o_closeness_bonus -  o_center_bonus
    


        if self.to_win==4:
            x_3_wins=self.heuristics_prevent_mustwins('X', 3)
            if x_3_wins>0 and self.crosses_turn:
                return 0.7 + x_closeness_bonus +  x_center_bonus
            o_3_wins=self.heuristics_prevent_mustwins('O', 3)
            if o_3_wins>0 and not self.crosses_turn:
                return -0.7 - o_closeness_bonus -  o_center_bonus
        
        if self.to_win==5:
            if self.crosses_turn:
                x_4_wins=self.heuristics_prevent_mustwins('X', 4)
                if x_4_wins>0:
                    return 0.7 + x_closeness_bonus +  x_center_bonus
            if not self.crosses_turn:
                o_4_wins=self.heuristics_prevent_mustwins('O', 4)
                if o_4_wins>0:
                    return -0.7 - o_closeness_bonus -  o_center_bonus

        outcome=x_closeness_bonus +  x_center_bonus-o_closeness_bonus -  o_center_bonus
        impact=0

        x_2_result=basic_check.basic_check(self,'X', 2 )
        o_2_result=basic_check.basic_check(self,'O', 2 )
        if o_2_result==0:
            o_2_result=0.0000000000001
        if x_2_result==0:
            x_2_result=0.0000000000001    
        sum=x_2_result+o_2_result
        diff=x_2_result-o_2_result
        weight=0.1
        try:
            impact=diff/sum*weight
        except:
            pass
        outcome+=impact

        if self.to_win==3:
            return outcome 
        
        outcome=x_closeness_bonus +  x_center_bonus-o_closeness_bonus -  o_center_bonus
        impact=0

        x_3_result=basic_check.basic_check(self,'X', 3 )
        o_3_result=basic_check.basic_check(self,'O', 3 )
        if o_3_result==0:
            o_3_result=0.0000000000001
        if x_3_result==0:
            x_3_result=0.0000000000001    
        sum=x_3_result+o_3_result
        diff=x_3_result-o_3_result
        weight=0.1
        try:
            impact=diff/sum*weight
        except:
            pass
        outcome+=impact

        if self.to_win==4:
            return outcome

        outcome=x_closeness_bonus +  x_center_bonus-o_closeness_bonus -  o_center_bonus
        impact=0
        
        x_4_result=basic_check.basic_check(self,'X', 4 )
        o_4_result=basic_check.basic_check(self,'O', 4 )
        if o_4_result==0:
            o_4_result=0.0000000000001
        if x_4_result==0:
            x_4_result=0.0000000000001    
        sum=x_4_result+o_4_result
        diff=x_4_result-o_4_result
        weight=0.1
        try:
            impact=diff/sum*weight
        except:
            pass
        outcome+=impact

        if self.to_win==5:
            return outcome


    def __str__(self):
        top_row='  '
        for numero in range(1, self.board_size+1):
            if numero<=10:
                top_row+='   '+str(numero)
            else:
                top_row+='  ' +str(numero)
        top_row+='\n'
        field=top_row
        for i in range(self.board_size):
            row=string.ascii_uppercase[i]+' '
            row+=self.board_size*' | a'
            row+=' |\n'
            field+=row
        for character in self.state:
            field = field.replace('a', character, 1)
        return field

    def is_max_node(self):
        return self.crosses_turn

    def generate_children(self, new=False):
        possible_states=[]
        if self.crosses_turn:
            mark='X'
        else:
            mark='O'
        
        # print("latest_move")
        # print(self.latest_move)

        #------------------------
        #THIS IS AN ATTEMPT TO LIMIT THE SEARCH AREA OF THE MINIMAX-ALGORITHM
        # closest=[]
        # min_row=string.ascii_uppercase.find(self.latest_move[0].upper())-(self.to_win-2)
        # if min_row<0:
        #     min_row=0
        # max_row=string.ascii_uppercase.find(self.latest_move[0].upper())+(self.to_win-2)
        # if max_row>self.board_size-1:
        #     max_row=self.board_size-1
        # min_column=self.latest_move[1]-1-(self.to_win-2)
        # if min_column<0:
        #     min_column=0
        # max_column=self.latest_move[1]-1+(self.to_win-2)
        # if max_column>self.board_size-1:
        #     max_column=self.board_size-1
        
        # for row in range(min_row, max_row+1):
        #     for column in range (min_column, max_column):
        #         closest.append(row*self.board_size+column)
        
        # for i in closest:
        #     aux=self.state
        #     if self.state[i]=='-':
        #         aux=aux[:i]+mark+aux[i+1:]
        #         row=(i+1)//self.board_size
        #         column=i%self.board_size
        #         latest_move=(string.ascii_uppercase[row], column+1)
        #         new_state=TicTacToe(aux, self.board_size, not self.crosses_turn, self.level, self.players, latest_move)
        #         possible_states.append(new_state)
        #------------------------


        for i in range (len(self.state)):
            aux=self.state
            if self.state[i]=='-':
                aux=aux[:i]+mark+aux[i+1:]
                row=(i+1)//self.board_size
                column=i%self.board_size
                latest_move=(string.ascii_uppercase[row], column+1)
                new_state=TicTacToe(aux, self.board_size, not self.crosses_turn, self.level, self.players, latest_move)
                possible_states.append(new_state)
        # for taulukko in possible_states:
        #     print(taulukko)
        return possible_states

    def value(self):
        if self.won('X', self.to_win):
            return 1
        if self.won('O', self.to_win):
            return -1
        return 0
    
    def count_empty(self):
        count=0
        for char in self.state:
            if char=='-':
                count+=1
        return count

round=0

def alpha_beta_value(node):
    alpha=-1
    beta=1
    depth=0
    if node.crosses_turn:
        value=max_value(node, alpha, beta, depth)
    else:
        value=min_value(node, alpha, beta, depth)
    return value


def max_value(node:TicTacToe, alpha, beta, depth):
    depth+=1  
    global round
    round+=1
    # print ("depth", depth) 
    # print("max depth", node.max_depth)
    
    if node.is_end_state():
        return node.value() 
    
    if node.count_empty()>node.heuristics_limit or depth>=node.max_depth:

        # print("*************")
        # print(node)
        result=node.heuristics_coordinator()
        # print("yo. taulukon heuristics result max-valuesta", result)
        # print("*************")
        return result
    
    v=-LARGE_NUMBER
    for child in node.generate_children():
        v=max(v, min_value(child, alpha, beta, depth))
        alpha=max(alpha,v)
        if alpha>=beta:
            # print("max value pruned!")
            return v           
    return v


def min_value(node:TicTacToe, alpha, beta, depth):
    depth+=1
    global round
    round+=1
    
    if node.is_end_state():
        return node.value()    
    
    if node.count_empty()>node.heuristics_limit or depth>=node.max_depth:
        result=node.heuristics_coordinator()
        # print(node)
        # print("yo. taulukon heuristics result min-valuesta", result)
        # print("---------")
        return result

    v=LARGE_NUMBER

    for child in node.generate_children():
        v=min(v, max_value(child, alpha, beta, depth))
        beta=min(beta,v)
        if alpha>=beta:                
            # print("min value pruned!")
            return v
    return v

def get_rounds():
    return round