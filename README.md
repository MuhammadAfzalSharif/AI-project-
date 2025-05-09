# Smart Fire Fighter AI Project

## Project Overview

This project implements an AI agent that can navigate through a world to extinguish fires using various search algorithms. The agent (firefighter) can move in a grid-based environment, collect water buckets, fill them at hydrants, and use the water to extinguish fires.

## Features

- **Multiple Search Algorithms**:
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Uniform Cost Search (UCS)
  - Greedy Search
  - A* Search

- **Interactive GUI**: Visualize the agent's path and actions in a colorful interface
- **Performance Metrics**: Compare algorithms based on:
  - Number of expanded nodes
  - Tree depth
  - Computation time
  - Path cost

## Project Structure

- **Main Components**:
  - `agent.py`: Defines the firefighter agent and its capabilities
  - `board.py`: Implements the world grid environment
  - `cell.py` and `firecell.py`: Define the grid cells and fire cells
  - `bucket.py`: Implements the water bucket functionality
  - `move.py`: Handles agent movement logic
  - `state.py`: Represents the state of the environment and agent
  - `node.py`: Implements nodes for search algorithms

- **Search Algorithms**:
  - `bfs.py`: Breadth-First Search implementation
  - `dfs.py`: Depth-First Search implementation
  - `ucs.py`: Uniform Cost Search implementation
  - `greedysearch.py`: Greedy Search implementation
  - `astartsearch.py`: A* Search implementation

- **Utility Functions**:
  - `utils/validation.py`: Validates agent moves
  - `utils/selector.py`: Helps with selection operations
  - `utils/printer.py`: Handles printing information
  - `utils/filemanager.py`: Manages file operations
  - `utils/count.py`: Counts active fires and other metrics
  - `utils/converter.py`: Converts data formats

- **User Interface**:
  - `gui.py`: Implements the graphical user interface
  - `main.py`: Command-line interface for the project

## How to Run

1. Run the GUI version:
   ```
   python AI/gui.py
   ```

2. Run the command-line version:
   ```
   python AI/main.py
   ```

3. When prompted, load a map file (e.g., `AI/path.txt`)

4. Select a search algorithm to watch the agent solve the fire-fighting problem

## Environment Legend

- `0`: Free cell
- `1`: Wall
- `2`: Fire
- `3`: 1-liter bucket
- `4`: 2-liter bucket
- `5`: Start position
- `6`: Hydrant

## Algorithm Comparison

Each algorithm has different characteristics:
- **BFS**: Optimal for shortest path (number of moves)
- **DFS**: Can find solutions quickly but not optimal
- **UCS**: Optimal for weighted paths
- **Greedy**: Fast but may not find optimal solution
- **A***: Combines UCS and Greedy for efficiency and optimality

## Documentation

For more detailed information, refer to the included project documents:
- `AI_Project_Proposal_Smart_Fire_Fighter.docx`
- `AI_Project_Report_Smart_Fire_Fighter.docx`
