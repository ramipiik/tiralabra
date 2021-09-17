LARGE_NUMBER = 1000000

depth=0
max_depth=0

class TicTacToe():
    def __init__(self, state, board_size, crosses_turn):
        self.state = state
        self.board_size=board_size
        self.crosses_turn = crosses_turn
        self.to_win=5
        if self.board_size==3:
            self.to_win=3
        if self.board_size==4:
            self.to_win=4
        if self.board_size==5:
            self.to_win=4
        if self.board_size==7:
            self.to_win=4

    def is_end_state(self):
        # print("is end state function is called")
        if ('-' not in self.state) or self.won('x') or self.won('o'):
            return (True, count_moves(self.state))
            # return True
        else:
            return (False, count_moves(self.state))
            return False

    def won(self, mark):
        # print("won function is called")
        combo = self.to_win * mark
        # print("combo", combo)
        # print("board size", self.board_size)

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

    def __str__(self):
        row=self.board_size*'|a'
        row+='|\n'
        field=self.board_size*row
        # print("field")
        # print(field)
        for character in self.state:
            field = field.replace('a', character, 1)

        return field

    def is_max_node(self):
        return self.crosses_turn


    def generate_children(self, new=False):
        global depth
        if new:
            # print("uusi kutsu")
            depth=0
        # Implement me
        possible_states=[]
        # print("---------")
        # print(self)
        # print("---------")
        if self.crosses_turn:
            mark='x'
        else:
            mark='o'
        for i in range (len(self.state)):
            # print(i)
            aux=self.state
            if self.state[i]=='-':
                aux=aux[:i]+mark+aux[i+1:]
                new_state=TicTacToe(aux, self.board_size, not self.crosses_turn)
                possible_states.append(new_state)
                # print (aux)
        # print("---------")
        # for taulukko in possible_states:
        #     print(taulukko)
        return possible_states

    def value(self):
        """
        Current score of the game (0, 1, -1)
        :return: int
        """
        if self.won('x'):
            # print("x:n voitto!")
            return 1
        if self.won('o'):
            # print("o:n voitto!")
            return -1
        return 0


def count_moves(siirto:TicTacToe):
    moves=0
    # print(siirto.state)
    for mark in siirto:
        if mark=='o' or mark=='x':
            moves+=1
    # print("moves", moves)
    # exit()
    return moves

round=0

def alpha_beta_value(node):
    alpha=-1
    beta=1
    if node.crosses_turn:
        # print("x:n vuoro")
        value=max_value(node, alpha, beta)
    else:
        # print("o:n vuoro")
        value=min_value(node, alpha, beta)
    # print("ollaan alpha_beta_value metodissa")
    # print("arvo", arvo)
    return value


def max_value(node:TicTacToe, alpha, beta):
    # print("max value function is called")

    global round
    global depth
    global max_depth
    round+=1
    depth+=1
    # print("tultiin max-value haaraan")
    # print(node)
    (is_end_state, moves)=node.is_end_state()
    # print(is_end_state)
    # exit()
    if is_end_state:
        # print("node value", node.value())
        # print("depth", depth)
        if depth>max_depth:
            max_depth=depth
        depth=0
        # print("moves-testi B", moves)
        return (node.value(), moves, moves)
    v=-LARGE_NUMBER
    store_min_steps=1000
    store_max_steps=-1
    for child in node.generate_children():
        # print(child)
        (new_value,min_steps, max_steps)=min_value(child, alpha, beta)
        if new_value>v:
            answer=child
            v=new_value
            store_min_steps=min_steps
            store_max_steps=max_steps
        if new_value==v:
            if min_steps<store_min_steps:
                store_min_steps=min_steps
            if max_steps>store_max_steps:
                store_max_steps=max_steps
        # v=max(v, min_value(child, alpha, beta)[0])
        alpha=max(alpha,v)
        if alpha>=beta:
            # print("pruned!")
            # s=steps
            return (v, store_min_steps, store_max_steps)
    # print("v", v)
    return (v, store_min_steps, store_max_steps)
    # return HUGE_NUMBER

def get_max_depth():
    return max_depth

def min_value(node, alpha, beta):
    # print("min value function is called")
    global round
    global depth
    global max_depth
    round+=1
    depth+=1
    # print("tultiin min-value haaraan")
    # print(node)
    (is_end_state, moves)=node.is_end_state()
    # print(is_end_state)
    # exit()
    if is_end_state:
        # print("node value", node.value())
        # print("depth", depth)
        if depth>max_depth:
            max_depth=depth
        depth=0
        # print("checkpoint A")
        # print("------")
        # print(node.state)
        # print("moves", moves)
        # print("------")
        return (node.value(), moves, moves)
    v=LARGE_NUMBER

    # IMPLEMENT HEURISTICS CHECK HERE
    #IF DEPTH == MAX DEPTH (depth kulkee min ja max_value looppien mukana)
       # RETURN node.heuristics()
    # node.heuristics on funktio joka arvioi kuinka arvokas laudan tilanne on.
    # heuristics palauttaa arvon -1:n j 1:n väliltä
    #testaa ensin siten, että se palauttaa aina nollan ja varmista siten, että syvyysrajoitin toimii ja 4x4-lauta saadaan pelattua läpi
    #logiikka:
    # 1) jos löytyy molemmista päistä avoin suora -ooo-, niin se on melkein voitto eli 0.99 plussaa tai miinusta. heuristiikka loppuu tähän, koska se pakko hoittaa
    # 2) jos tarkistettavalta riviltä löytyy vaadittavan pituinen suora yhdellä -:lla se on 0.8. Jos näitä löytyy useampi kuin yksi, niin 0.95
    # 3) jos löytyy suora kahdella aukolla se on 0.2. Jos useampia, niin +0.1 jokaisesta
    # kysymys: pitäisikö kakkosia ja kolmosia summata yhteen, vai palauttaa ainoastaan paras tilanne. 

    store_min_steps=1000
    store_max_steps=-1
    for child in node.generate_children():
        # print(child)
        (new_value, min_steps, max_steps)=max_value(child, alpha, beta)
        if new_value<v:
            answer=child
            v=new_value
            store_min_steps=min_steps
            store_max_steps=max_steps
        if new_value==v:
            if min_steps<store_min_steps:
                store_min_steps=min_steps
            if max_steps>store_max_steps:
                store_max_steps=max_steps
        
        # min(v, max_value(child, alpha, beta)[0])
        beta=min(beta,v)
        if alpha>=beta:
            
            # print("pruned!")
            # s=steps
            return (v, store_min_steps, store_max_steps)
    # print("v", v)
    # print("------")
    # print("checkpoint A")
    # print(answer.state)
    # print("siirrot", count_moves(answer.state))
    # print("------")

    return (v, store_min_steps, store_max_steps)
    # return +HUGE_NUMBER

def get_rounds():
    return round