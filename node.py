class Node:
    def __init__(self, state, g, h, parent=None, move=""):
        self.state = state
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent
        self.move = move

    def __lt__(self, other):
        if self.f == other.f:
            return self.h < other.h
        return self.f < other.f