import time
import heapq
from node import Node
from core import is_goal, expand, reconstruct

def a_star(start, heuristic_func):
    start_time = time.time()
    nodes_expanded = 0
    
    frontier = []
    heapq.heappush(frontier, Node(start, 0, heuristic_func(start)))
    g_costs = {start: 0}
    
    while frontier:
        current = heapq.heappop(frontier)
        if is_goal(current.state):
            return True, reconstruct(current), nodes_expanded, time.time() - start_time
            
        if current.g > g_costs.get(current.state, float('inf')):
            continue
            
        nodes_expanded += 1
        for next_state, move_name in expand(current.state):
            new_g = current.g + 1
            if new_g < g_costs.get(next_state, float('inf')):
                g_costs[next_state] = new_g
                h = heuristic_func(next_state)
                child = Node(next_state, new_g, h, current, move_name)
                heapq.heappush(frontier, child)
    return False, [], nodes_expanded, time.time() - start_time