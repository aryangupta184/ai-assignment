import sys
from visualization import clear_screen, visualize_game
from heuristics import h1_primary_blockers, h2_secondary_blockers

# Import Algorithms
from bfs import bfs
from dfs import dfs
from ucs import ucs
from astar import a_star

def main():
    
    test_cases = {
        "1": {"name": "Easy 1", "state": "BB.J...H.JCCGHXXKLGDD.KL..IEE.FFI..."},
        "2": {"name": "Easy 2", "state": "BBH..KF.H.JKFXX.JL.GCC.L.G.IDDEE.I.."},
        "3": {"name": "Medium 1", "state": "G..x..GCCJ.LXXIJ.L.HIDDM.HEEKMFF..K."},
        "4": {"name": "Medium 2", "state": "...xx.IDDLMNIXXLMNEEK....JKFF..JGGHH"},
        "5": {"name": "Hard 1", "state": "IBBx..I..LDDJXXL..J.KEEMFFK..MGGHHHM"},
        "6": {"name": "Hard 2", "state": "BB.KMxDDDKM.IXXL..I.JLEE..JFFN.GG.xN"}
    }
    
    while True:
        clear_screen()
        print("Rush Hour AI Solver")
        print("Select a Test Case:")
        for k, v in test_cases.items():
            print(f"{k}. {v['name']}")
        print("0. Exit")
        
        tc_choice = input("Choice: ")
        if tc_choice == "0": break
        if tc_choice not in test_cases:
            continue
        
        print("\nSelect Algorithm:")
        print("1. BFS")
        print("2. DFS (Warning: Unoptimal Paths)")
        print("3. Uniform Cost Search (UCS)")
        print("4. A* (h1 - Primary Blockers)")
        print("5. A* (h2 - Secondary Interlocking)")
        
        algo_choice = input("Choice: ")
        if algo_choice not in [str(i) for i in range(1, 6)]: continue
        
        start_state = test_cases[tc_choice]["state"]
        
        print("\nSolving... Please wait.")
        
        if algo_choice == "1":
            success, path, nodes, t = bfs(start_state)
            algo_name = "BFS"
        elif algo_choice == "2":
            success, path, nodes, t = dfs(start_state)
            algo_name = "DFS"
        elif algo_choice == "3":
            success, path, nodes, t = ucs(start_state)
            algo_name = "UCS"
        elif algo_choice == "4":
            success, path, nodes, t = a_star(start_state, h1_primary_blockers)
            algo_name = "A* (h1)"
        elif algo_choice == "5":
            success, path, nodes, t = a_star(start_state, h2_secondary_blockers)
            algo_name = "A* (h2)"

        if success:
            visualize_game(path)
            print("\nEvaluation Metrics")
            print(f"Algorithm      : {algo_name}")
            print(f"Puzzle         : {test_cases[tc_choice]['name']}")
            print(f"Path Length    : {len(path)-1} moves")
            print(f"Nodes Expanded : {nodes}")
            print(f"Execution Time : {t:.4f} seconds")
        else:
            print("\nFailed to find a solution.")
            
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()