import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def visualize_game(path, delay=0.4):
    colors = {'X': '\033[91m', '.': '\033[90m', 'x': '\033[37m'}
    color_pool = ['\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[97m']
    color_idx = 0
    
    for step, node in enumerate(path):
        clear_screen()
        print(f"Step {step}/{len(path)-1}")
        print(f"Move: {node.move}" if node.move else "Initial State")
        print("-" * 15)
        
        state = node.state
        for r in range(6):
            row_str = "|"
            for c in range(6):
                char = state[r*6 + c]
                if char not in colors:
                    colors[char] = color_pool[color_idx % len(color_pool)]
                    color_idx += 1
                
                if char == '.':
                    row_str += f" {colors[char]}. \033[0m"
                else:
                    row_str += f" {colors[char]}{char} \033[0m"
            if r == 2: row_str += " EXIT"
            print(row_str)
        print("-" * 15)
        time.sleep(delay)