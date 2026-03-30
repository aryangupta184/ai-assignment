from core import is_goal, get_vehicles

def h1_primary_blockers(state_str):
    if is_goal(state_str): return 0
    vehicles = get_vehicles(state_str)
    x_right = vehicles['X']['indices'][-1]
    
    blockers = set()
    for i in range(x_right + 1, 18):
        if state_str[i] != '.' and state_str[i] != 'x':
            blockers.add(state_str[i])
    return 1 + len(blockers)

def h2_secondary_blockers(state_str):
    if is_goal(state_str): return 0
    vehicles = get_vehicles(state_str)
    x_right = vehicles['X']['indices'][-1]
    
    primary_blockers = set()
    for i in range(x_right + 1, 18):
        if state_str[i] != '.' and state_str[i] != 'x':
            primary_blockers.add(state_str[i])
            
    secondary_blockers = set()
    for b in primary_blockers:
        b_info = vehicles[b]
        if b_info['orientation'] == 'V':
            top = b_info['indices'][0]
            bottom = b_info['indices'][-1]
            
            can_move_up = (top >= 6 and state_str[top-6] == '.')
            can_move_down = (bottom < 30 and state_str[bottom+6] == '.')
            
            if not can_move_up and not can_move_down:
                up_char = state_str[top-6] if top >= 6 else None
                down_char = state_str[bottom+6] if bottom < 30 else None
                
                if up_char and up_char.isalpha() and up_char != 'X':
                    secondary_blockers.add(up_char)
                if down_char and down_char.isalpha() and down_char != 'X':
                    secondary_blockers.add(down_char)
                    
    return 1 + len(primary_blockers) + len(secondary_blockers)