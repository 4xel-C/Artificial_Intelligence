# Maze Solver

This project implements a maze-solving algorithm using either a depth-first or a breadth-first search approach. The maze is represented in a text file, and the program finds a path from the starting point (A) to the goal (B). After finding the solution, the program generate a png image showing all the explored path and the solution proposed.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Code Explanation](#code-explanation)
- [Requirements](#requirements)

## Installation

To run this project, ensure you have Python installed on your machine. You will also need the Pillow library for image output. You can install it using pip:

```bash
pip install Pillow
```

## Usage

1) Prepare a text file representing the maze. The maze should use:

- `A` for the starting point
- `B` for the goal
- `█` for walls
- Spaces for open paths

Exemple of maze are available in the folder.

2) Run the script from the command line with the path to the maze file: 

```
python maze.py maze.txt
```

The program will display the maze, solve it, and output the solution along with the number of states explored. It will also save an image of the maze with the solution highlighted as maze.png, allowing the user to observe the result of the algorithm. 

3) (optionnal) By modifying line 127 of `maze.py`, you can swap the algorithm used between Deepth-First search or Breadth-Frist search with the `StackFrontier` or `QueueFrontier`.

## How It Works

- **Loading the Maze**: The program reads the maze from a specified text file, validating the presence of exactly one start point (A) and one goal (B). It also determines the dimensions of the maze and tracks walls.

- **Solving the Maze**: The `solve` method uses a depth-first search algorithm to explore the maze. It keeps track of explored nodes to avoid cycles and uses a stack-based frontier to manage the nodes to explore.

- **Output**: After finding a solution, the program prints the number of states explored and displays the maze with the solution path marked.

## Code Explanation

### Main Components

- **Node Class**: Represents a state in the maze, storing the current position, the parent node, and the action taken to reach this node.

- **StackFrotier Class**: Implements a stack-based frontier for depth-first search. It allows adding nodes, checking for existing states, and removing nodes from the stack.

- **Maze Class**: Contains methods to load the maze, find neighbors, solve the maze, and output the maze as an image.

## Requirements
- Python 3.X
- Pillow library (for image output)

