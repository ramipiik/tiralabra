from parameters import LARGE_NUMBER, alpha, beta
from Heuristics import run_heuristics
from tictactoe import TicTacToe

round=0

def alpha_beta_value(node:TicTacToe):
    depth=0
    if node.crosses_turn:
        value=max_value(node, alpha, beta, depth)
    else:
        value=min_value(node, alpha, beta, depth)
    return value


def max_value(node:TicTacToe, alpha:int, beta:int, depth:int):
    depth+=1  
    global round
    round+=1
    
    if node.is_end_state():
        return node.value() 
    
    if node.count_empty()>node.heuristics_limit or depth>=node.max_depth:
        return run_heuristics.run_heuristics(node)
    
    v=-LARGE_NUMBER
    for child in node.generate_children():
        v=max(v, min_value(child, alpha, beta, depth))
        alpha=max(alpha,v)
        if alpha>=beta:
            return v           
    return v


def min_value(node:TicTacToe, alpha, beta, depth):
    depth+=1
    global round
    round+=1
    
    if node.is_end_state():
        return node.value()    
    
    if node.count_empty()>node.heuristics_limit or depth>=node.max_depth:
        return run_heuristics.run_heuristics(node)

    v=LARGE_NUMBER
    for child in node.generate_children():
        v=min(v, max_value(child, alpha, beta, depth))
        beta=min(beta,v)
        if alpha>=beta:                
            return v
    return v

def get_rounds():
    return round