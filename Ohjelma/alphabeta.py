TEMPLATE_FIELD = '|e|e|e|\n|e|e|e|\n|e|e|e|\n'
LARGE_NUMBER = 1000000

depth=0
max_depth=0

class TicTacToe():
    def __init__(self, state, crosses_turn):
        super().__init__()
        self.state = state
        self.crosses_turn = crosses_turn

    def is_end_state(self):
        return ('?' not in self.state) or self.won('x') or self.won('o')

    def won(self, c):
        triples = [self.state[0:3], self.state[3:6], self.state[6:9], self.state[::3], self.state[1::3],
                   self.state[2::3], self.state[0] + self.state[4] + self.state[8],
                   self.state[2] + self.state[4] + self.state[6]]
        combo = 3 * c
        
        return combo in triples

    def __str__(self):
        field = TEMPLATE_FIELD
        for c in self.state:
            field = field.replace('e', c, 1)

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
            merkki='x'
        else:
            merkki='o'
        for i in range (len(self.state)):
            # print(i)
            aux=self.state
            if self.state[i]=='?':
                aux=aux[:i]+merkki+aux[i+1:]
                new_state=TicTacToe(aux, not self.crosses_turn)
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

round=0

def alpha_beta_value(node):
    alpha=-1
    beta=1
    if node.crosses_turn:
        # print("x:n vuoro")
        arvo=max_value(node, alpha, beta)
    else:
        # print("o:n vuoro")
        arvo=min_value(node, alpha, beta)
    # print("ollaan alpha_beta_value metodissa")
    # print("arvo", arvo)
    return arvo


def max_value(node:TicTacToe, alpha, beta):
    global round
    global depth
    global max_depth
    round+=1
    depth+=1
    # print("tultiin max-value haaraan")
    # print(node)
    if node.is_end_state():
        # print("node value", node.value())
        # print("depth", depth)
        if depth>max_depth:
            max_depth=depth
        depth=0
        return node.value()
    v=-LARGE_NUMBER
    for child in node.generate_children():
        # print(child)
        v=max(v, min_value(child, alpha, beta))
        alpha=max(alpha,v)
        if alpha>=beta:
            # print("pruned!")
            return v
    # print("v", v)
    return v
    # return HUGE_NUMBER

def get_max_depth():
    return max_depth

def min_value(node, alpha, beta):
    global round
    global depth
    global max_depth
    round+=1
    depth+=1
    # print("tultiin min-value haaraan")
    # print(node)
    if node.is_end_state():
        # print("node value", node.value())
        # print("depth", depth)
        if depth>max_depth:
            max_depth=depth
        depth=0
        return node.value()
    v=LARGE_NUMBER
    for child in node.generate_children():
        # print(child)
        v=min(v, max_value(child, alpha, beta))
        beta=min(beta,v)
        if alpha>=beta:
            # print("pruned!")
            return v
    # print("v", v)
    return v
    # return +HUGE_NUMBER

def get_rounds():
    return round