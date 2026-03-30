# Rush Hour AI Solver

A Python-based AI solver for the classic sliding block puzzle *Rush Hour*.

The objective is simple: move the red car (`X`) out of a congested 6×6 parking grid. The challenge lies in finding the most efficient sequence of moves while navigating through other vehicles blocking the path.

This project is designed both as a working solver and as a practical way to understand how different search algorithms behave on the same problem.

---

## Features
 
- **Multiple Search Algorithms**  
  Includes Breadth-First Search (BFS), Depth-First Search (DFS), Uniform Cost Search (UCS), and A* Search.

- **Custom Heuristics for A\***  
  Two heuristics are implemented to improve search efficiency:
  - `h1_primary_blockers`: Counts vehicles directly blocking the red car.
  - `h2_secondary_blockers`: Extends h1 by including vehicles blocking the blockers.

- **Terminal Visualization**  
  Step-by-step CLI-based visualization of the puzzle with a clear, color-coded grid.

- **Performance Metrics**  
  Outputs execution time, number of moves in the solution, and total nodes expanded for comparison across algorithms.

---

## Project Structure

```
.
├── main.py             # Entry point with CLI and test cases
├── core.py             # Game logic, state transitions, validation
├── node.py             # Node representation for search trees
├── bfs.py              # Breadth-First Search implementation
├── dfs.py              # Depth-First Search implementation
├── ucs.py              # Uniform Cost Search implementation
├── astar.py            # A* Search implementation
├── heuristics.py       # Heuristic functions for A*
└── visualization.py    # CLI-based board visualization
```

---

## Requirements

This project uses only Python’s standard library.

- Python 3.x

No external dependencies are required.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd <repo-folder>
   ```

2. Run the main script:
   ```bash
   python main.py
   ```

3. Follow the prompts to:
   - Select a test case (Easy to Hard)
   - Choose a search algorithm
   - View the solution step-by-step
   - Analyze performance metrics

---

## State Representation

The board is represented as a single string of 36 characters (a flattened 6×6 grid).

- `X` → Target vehicle (needs to exit)
- `.` → Empty space
- `x` → Blocked/wall space
- `A-Z` (except `X`) → Other vehicles

Vehicles are automatically inferred as horizontal or vertical based on their positions.

The exit is located at the right edge of the third row (indices 16 and 17).

---

## Algorithms Overview

- **BFS (Breadth-First Search)**  
  Guarantees the shortest solution but can consume significant memory.

- **DFS (Depth-First Search)**  
  Explores deeply first. Faster in some cases, but does not guarantee optimal solutions.

- **UCS (Uniform Cost Search)**  
  Equivalent to BFS in this problem since all moves have equal cost.

- **A\***  
  Uses heuristics to guide the search, significantly reducing unnecessary exploration while still ensuring optimality.

---

## Why Not IDA*?

Although Iterative Deepening A* (IDA*) is a well-known algorithm, it is not included in this project.

Rush Hour has a highly repetitive state space where vehicles can move back and forth, creating many duplicate configurations. Without maintaining memory of visited states (e.g., a transposition table), IDA* repeatedly explores the same states, making it inefficient for this problem.

In practice, A* with good heuristics performs much better for Rush Hour.

---
