LARGE_NUMBER = 1000000
import string

class TicTacToe():
    def __init__(self, state, board_size, crosses_turn, level, players):
        self.state = state
        self.board_size=board_size
        self.crosses_turn = crosses_turn
        self.to_win=5
        self.players=players
        self.level=level
        if self.board_size==3:
            self.to_win=3
        if self.board_size==4:
            self.to_win=4
        if self.board_size==5:
            self.to_win=4
        if self.board_size==7:
            self.to_win=4
        
        # self.max_depth=int(level)
        if board_size==3:
            if level==1:
                self.max_depth=3
            if level==2:
                self.max_depth=5
            if level==3:
                self.max_depth=7
        if board_size==5:
            if level==1:
                self.max_depth=2
            if level==2:
                self.max_depth=3
            if level==3:
                self.max_depth=4
        if board_size==7:
            if level==1:
                self.max_depth=2
            if level==2:
                self.max_depth=3
            if level==3:
                self.max_depth=4 #liian hidas
        
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

    def heuristics_check(self, mark, n):
        combo = n * mark
        count=0

        #checks horizontal_lines
        for i in range (self.board_size):
            rivi:str=self.state[i*self.board_size:i*self.board_size+self.board_size]
            # print(rivi)
            if rivi.__contains__(combo+'-') or rivi.__contains__('-'+combo):
                # print("mark", mark, "osuma rivillä", rivi)
                count+=1
                # print("count", count)
        
        #checks vertical_lines
        for i in range (self.board_size):
            rivi=""
            for j in range (self.board_size):
                rivi+=self.state[j*self.board_size+i]
            # print(rivi)
            if rivi.__contains__(combo+'-') or rivi.__contains__('-'+combo):
                # print("mark", mark, "osuma rivillä", rivi)
                count+=1
                # print("count", count)
        
        #checks diagonal lines from top row to right-down
        for i in range (self.board_size):
            rivi=""
            if i<=self.board_size-n:
                for j in range(self.board_size):
                    if i+j*(self.board_size+1)<self.board_size**2:
                        rivi+=self.state[i+j*(self.board_size+1)]
                # print(rivi)
            if rivi.__contains__(combo+'-') or rivi.__contains__('-'+combo):
                # print("mark", mark, "osuma rivillä", rivi)
                count+=1
                # print("count", count)

        #checks diagonal lines from top row to left-down
        # print("checkpoint 1")
        for i in range (self.board_size-1,-1,-1):
            max_length=i+1
            rivi=""
            if i>=n-1:
                for j in range(self.board_size):
                    if len(rivi)<max_length:
                        rivi+=self.state[i+j*(self.board_size-1)]
                # print(rivi)
            if rivi.__contains__(combo+'-') or rivi.__contains__('-'+combo):
                # print("mark", mark, "osuma rivillä", rivi)
                count+=1
                # print("count", count)

        #checks diagonal lines from left column to right-down
        for j in range (1, self.board_size): #top-left corner has already been checked. Thus starting from row 1.
            max_length=self.board_size-j
            rivi=""
            if j<=self.board_size-n:
                for i in range(self.board_size):
                    if len(rivi)<max_length:
                        rivi+=self.state[j*self.board_size+i*(self.board_size+1)]
                # print(rivi)
            if rivi.__contains__(combo+'-') or rivi.__contains__('-'+combo):
                # print("mark", mark, "osuma rivillä", rivi)
                count+=1
                # print("count", count)

        #checks diagonal lines from right column to left-down
        # print("checkpoint 2")
        for j in range (1, self.board_size): #top-right corner has already been checked. Thus starting from row 1.
            max_length=self.board_size-j
            rivi=""
            if j<=self.board_size-n:
                for i in range(self.board_size):
                    if len(rivi)<max_length:
                        rivi+=self.state[(self.board_size-1)+j*(self.board_size)+i*(self.board_size-1)]
                # print(rivi)
            if rivi.__contains__(combo+'-') or rivi.__contains__('-'+combo):
                # print("mark", mark, "osuma rivillä", rivi)
                count+=1
                # print("count", count)

        return count

    def heuristics(self):
        
        # 1) jos löytyy molemmista päistä avoin suora -ooo-, niin se on melkein voitto eli 0.99 plussaa tai miinusta. heuristiikka loppuu tähän, koska se pakko hoittaa
        # 2) jos tarkistettavalta riviltä löytyy vaadittavan pituinen suora yhdellä -:lla se on 0.8. Jos näitä löytyy useampi kuin yksi, niin 0.95
        # 3) jos löytyy suora kahdella aukolla se on 0.2. Jos useampia, niin +0.1 jokaisesta
        # kysymys: pitäisikö kakkosia ja kolmosia summata yhteen, vai palauttaa ainoastaan paras tilanne.     
        # print("heuristics called")
        
        # print(self)

        outcome=0

        x_2_result=self.heuristics_check('X', 2)
        o_2_result=self.heuristics_check('O', 2)
        if x_2_result>o_2_result:
            outcome+=0.05
        elif o_2_result>x_2_result:
            outcome+= -0.05
        else:
            outcome=+0

        if self.to_win==3:
            if self.crosses_turn:
                return outcome
            else:
                return -outcome
                
        x_3_result=self.heuristics_check('X', 3)
        o_3_result=self.heuristics_check('O', 3)
        if x_3_result>o_3_result:
            outcome+=0.2
        elif o_2_result>x_2_result:
            outcome+=-0.2
        else:
            outcome+=0

        if self.to_win==4:
            if self.crosses_turn:
                # print("outcome 4",outcome)
                return outcome
            else:
                # print("-outcome 4", -outcome)
                return -outcome

        x_4_result=self.heuristics_check('X', 4)
        o_4_result=self.heuristics_check('O', 4)
        if x_4_result>o_4_result:
            outcome+=0.4
        elif o_2_result>x_2_result:
            outcome+=-0.4
        else:
            outcome+=0

        if self.to_win==5:
            if self.crosses_turn:
                return outcome
            else:
                return -outcome


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
        for i in range (len(self.state)):
            aux=self.state
            if self.state[i]=='-':
                aux=aux[:i]+mark+aux[i+1:]
                new_state=TicTacToe(aux, self.board_size, not self.crosses_turn, self.level, self.players)
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
    
    if node.is_end_state():
        return node.value() 
    if depth>=node.max_depth:
        estimate = node.heuristics()
        # print("-----------")
        # print(node)
        # print("Turn: 'X'")
        # print("estimate", estimate)
        # # input("press any key to continue")
        # print("-----------")
        return estimate
    
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
    if depth>=node.max_depth:
        estimate=node.heuristics()
        # print("-----------")
        # print(node)
        # print("Turn: 'O'")
        # print("estimate", estimate)
        # # input("press any key to continue")
        # print("-----------")
        return estimate

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