from astar import a_star

def ucs(start):
    # UCS is just A* with a heuristic that always returns 0
    return a_star(start, lambda state: 0)