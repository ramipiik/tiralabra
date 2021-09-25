LARGE_NUMBER = 1000000
import string
from Heuristics import basic_check
from Heuristics import boundaries_check
from Heuristics import closeness_check
from Heuristics import sanity_check
from Heuristics import mustwin_check
from Heuristics import prevent_mustwins


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


  
    
     
    def heuristics_coordinator(self):        
        #scores the position based on number of connection to other own marks. The more own marks are connected, the better it is.
        x_closeness_bonus=closeness_check.closeness_check(self,'X')*self.closeness_weight
        o_closeness_bonus=closeness_check.closeness_check(self,'O')*self.closeness_weight
        
        #Reverses the closeness check for the first turn. Purpose is to steer computers first move close to humans first move.
        if self.count_empty()==self.board_size**2-2:
            x_closeness_bonus=closeness_check.closeness_check(self, 'X', True)*self.closeness_weight

        #scores the position based on distance from the center. Closer to centre is better. Small impact.
        x_center_bonus=boundaries_check.boundaries_check(self, 'X')*self.center_weight
        o_center_bonus=boundaries_check.boundaries_check(self, 'O')*self.center_weight

        #Priority 1: Check whether there are situation requiring immediate defensive action
        if self.crosses_turn:
            x_wins=sanity_check.sanity_check(self, 'X', self.to_win-1)
            if x_wins>0:
                return 0.9 + x_closeness_bonus +  x_center_bonus
        
        if not self.crosses_turn:
            o_wins=sanity_check.sanity_check(self, 'O', self.to_win-1)
            if o_wins>0:
                return -0.9 - o_closeness_bonus -  o_center_bonus
        
        #Priority 2: Check whether a mustwin situation gan be gained
        x_wins=mustwin_check.check_mustwins(self,'X', self.to_win-1)
        if x_wins>0:
            return 0.8 + x_closeness_bonus +  x_center_bonus
        o_wins=mustwin_check.check_mustwins(self,'O', self.to_win-1)
        if o_wins>0:
            return -0.8 - o_closeness_bonus -  o_center_bonus  

        #Priority 3: Check competitor is about to get a mustwin situation that must be prevented 
        x_wins=prevent_mustwins.prevent_mustwins(self, 'X', self.to_win-1)
        if x_wins>0 and self.crosses_turn:
            return 0.7 + x_closeness_bonus +  x_center_bonus
        o_wins=prevent_mustwins.prevent_mustwins(self, 'O', self.to_win-1)
        if o_wins>0 and not self.crosses_turn:
            return -0.7 - o_closeness_bonus -  o_center_bonus

        #Calculates scoring for the position if there were no obvious plays dominating the situation
        x_result=basic_check.basic_check(self,'X', self.to_win-1 )
        o_result=basic_check.basic_check(self,'O', self.to_win-1 )
        if o_result==0:
            o_result=0.0000000000001
        if x_result==0:
            x_result=0.0000000000001    
        sum=x_result+o_result
        diff=x_result-o_result
        weight=0.1
        impact=0
        try:
            impact=diff/sum*weight
        except:
            pass
        outcome=impact+x_closeness_bonus +  x_center_bonus-o_closeness_bonus -  o_center_bonus
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