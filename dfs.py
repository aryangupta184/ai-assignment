import time
from node import Node
from core import is_goal, expand, reconstruct

def dfs(start):
    start_time = time.time()
    nodes_expanded = 0
    
    frontier = [Node(start, 0, 0)]
    explored = set()
    
    while frontier:
        current = frontier.pop()
        if is_goal(current.state):
            return True, reconstruct(current), nodes_expanded, time.time() - start_time
            
        if current.state in explored: continue
        explored.add(current.state)
        
        nodes_expanded += 1
        for next_state, move_name in expand(current.state):
            if next_state not in explored:
                frontier.append(Node(next_state, current.g + 1, 0, current, move_name))
    return False, [], nodes_expanded, time.time() - start_time