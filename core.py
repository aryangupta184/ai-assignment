def get_vehicles(state_str):
    vehicles = {}
    for i, char in enumerate(state_str):
        if char != '.' and char != 'x':
            if char not in vehicles:
                vehicles[char] = []
            vehicles[char].append(i)
    
    parsed = {}
    for char, indices in vehicles.items():
        if len(indices) >= 2:
            orientation = 'H' if indices[1] - indices[0] == 1 else 'V'
            parsed[char] = {
                'indices': indices,
                'orientation': orientation,
                'size': len(indices)
            }
    return parsed

def is_goal(state_str):
    return state_str[16] == 'X' and state_str[17] == 'X'

def apply_move(state, char, direction, steps=1):
    state_list = list(state)
    indices = [i for i, c in enumerate(state) if c == char]
    
    for i in indices:
        state_list[i] = '.'
        
    for i in indices:
        if direction == 'UP':
            state_list[i - 6 * steps] = char
        elif direction == 'DOWN':
            state_list[i + 6 * steps] = char
        elif direction == 'LEFT':
            state_list[i - steps] = char
        elif direction == 'RIGHT':
            state_list[i + steps] = char
        
    return "".join(state_list)

def expand(state):
    neighbors = []
    vehicles = get_vehicles(state)
    
    for char, info in vehicles.items():
        indices = info['indices']
        if info['orientation'] == 'H':
            left_edge = indices[0]
            steps = 0
            while left_edge % 6 > 0 and state[left_edge - 1] == '.':
                steps += 1
                left_edge -= 1
                neighbors.append((apply_move(state, char, 'LEFT', steps), f"Car {char} LEFT {steps}"))

            right_edge = indices[-1]
            steps = 0
            while right_edge % 6 < 5 and state[right_edge + 1] == '.':
                steps += 1
                right_edge += 1
                neighbors.append((apply_move(state, char, 'RIGHT', steps), f"Car {char} RIGHT {steps}"))
        else:
            top = indices[0]
            steps = 0
            while top >= 6 and state[top - 6] == '.':
                steps += 1
                top -= 6
                neighbors.append((apply_move(state, char, 'UP', steps), f"Car {char} UP {steps}"))

            bottom = indices[-1]
            steps = 0
            while bottom < 30 and state[bottom + 6] == '.':
                steps += 1
                bottom += 6
                neighbors.append((apply_move(state, char, 'DOWN', steps), f"Car {char} DOWN {steps}"))
    return neighbors

def reconstruct(node):
    path = []
    while node:
        path.append(node)
        node = node.parent
    return path[::-1]