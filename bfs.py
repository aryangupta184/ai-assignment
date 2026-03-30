import time
from collections import deque
from node import Node
from core import is_goal, expand, reconstruct

def bfs(start):
    start_time = time.time()
    nodes_expanded = 0
    
    frontier = deque([Node(start, 0, 0)])
    explored = {start}
    
    while frontier:
        current = frontier.popleft()
        if is_goal(current.state):
            return True, reconstruct(current), nodes_expanded, time.time() - start_time
            
        nodes_expanded += 1
        for next_state, move_name in expand(current.state):
            if next_state not in explored:
                explored.add(next_state)
                frontier.append(Node(next_state, current.g + 1, 0, current, move_name))
    return False, [], nodes_expanded, time.time() - start_time