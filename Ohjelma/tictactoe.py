from parameters import how_much_to_win, recursion_depth, closeness_weight, center_weight, max_empty_cells
import string

class TicTacToe():
    def __init__(self, state, board_size, crosses_turn, level, players,latest_move:tuple, first_turn=False):
        self.state = state
        self.board_size=board_size
        self.crosses_turn = crosses_turn
        self.players=players
        self.level=level
        self.latest_move=latest_move
        self.first_turn=first_turn
        self.to_win=how_much_to_win(self.board_size)      
        self.max_depth=recursion_depth(self.board_size)
        self.closeness_weight=closeness_weight(level)
        self.center_weight=center_weight
        self.heuristics_limit=max_empty_cells

    #Checks whether the state ends the game. Either the board is full, or one player won.
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
            if rivi.__contains__(combo):
                return True
        
        #checks diagonal lines from top row to right-down
        for i in range (self.board_size):
            rivi=""
            if i<=self.board_size-self.to_win:
                for j in range(self.board_size):
                    if i+j*(self.board_size+1)<self.board_size**2:
                        rivi+=self.state[i+j*(self.board_size+1)]
            if rivi.__contains__(combo):
                return True

        #checks diagonal lines from top row to left-down
        for i in range (self.board_size-1,-1,-1):
            max_length=i+1
            rivi=""
            if i>=self.to_win-1:
                for j in range(self.board_size):
                    if len(rivi)<max_length:
                        rivi+=self.state[i+j*(self.board_size-1)]
            if rivi.__contains__(combo):
                return True
            

        #checks diagonal lines from left column to right-down
        for j in range (1, self.board_size): #top-left corner has already been checked. Thus starting from row 1.
            max_length=self.board_size-j
            rivi=""
            if j<=self.board_size-self.to_win:
                for i in range(self.board_size):
                    if len(rivi)<max_length:
                        rivi+=self.state[j*self.board_size+i*(self.board_size+1)]
            if rivi.__contains__(combo):
                return True

        #checks diagonal lines from right column to left-down
        for j in range (1, self.board_size): #top-right corner has already been checked. Thus starting from row 1.
            max_length=self.board_size-j
            rivi=""
            if j<=self.board_size-self.to_win:
                for i in range(self.board_size):
                    if len(rivi)<max_length:
                        rivi+=self.state[(self.board_size-1)+j*(self.board_size)+i*(self.board_size-1)]
            if rivi.__contains__(combo):
                return True

        return False  

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

    def is_crosses_turn(self):
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
                row=(i+1)//self.board_size
                column=i%self.board_size
                latest_move=(string.ascii_uppercase[row], column+1)
                new_state=TicTacToe(aux, self.board_size, not self.crosses_turn, self.level, self.players, latest_move)
                possible_states.append(new_state)
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