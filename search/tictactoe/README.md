# Tic Tac Toe Player

This project implements a Tic Tac Toe game with a player that uses the Minimax algorithm with alpha-beta pruning to make optimal moves. The game can be played between two players, X and O, where X always starts first. It also features a graphical user interface using Pygame.

## Table of Contents
- [Installation](#installation)
- [Files](#files)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Code Explanation](#code-explanation)
- [Requirements](#requirements)

## Installation

To run this project, ensure you have Python installed on your machine. You will also need the Pygame library. You can install it using pip:

```bash
pip install pygame
```

## Files
- **tictactoe.py:** Contains all the log functions for the adversarial search.
- **runner.py**: Contains all the graphic interface and the initialization calls. 

## Usage

The game can be played by calling functions defined in the code. The initial state of the board can be obtained using the `initial_state()` function.

Players can take turns by calling the `player(board)` function to determine whose turn it is.

Possible actions can be retrieved using the `actions(board)` function, and the board can be updated using the `result(board, action)` function.

The game can be evaluated for a winner using the `winner(board)` function, and whether the game has reached a terminal state can be checked with `terminal(board)`.

The optimal move for the current player can be determined using the `minimax(board)` function.

To play the game with a graphical interface, run the Pygame script provided `runner.py`

## How It Works

- **Game State**: The game board is represented as a 3x3 list, where each cell can be empty, contain an X, or contain an O.

- **Player Turns**: The game alternates turns between players X and O, with X always going first.

- **Minimax Algorithm**: The algorithm evaluates all possible future states of the game to determine the optimal move. It uses recursion to explore all possible actions and their outcomes, applying alpha-beta pruning to optimize the search.

- **Utility Function**: The utility function evaluates the board state, returning 1 if X wins, -1 if O wins, and 0 for a draw.

- **Graphical User Interface**: The Pygame script allows users to play Tic Tac Toe against the AI. Players can select their character (X or O) and make moves by clicking on the game board.

## Code Explanation

### Main Components

- **Node Class**: Represents a state in the game, storing the current position, the parent node, and the action taken to reach this node.

### Functions:

- `initial_state()`: Returns the starting state of the board.
- `player(board)`: Returns the player who has the next turn.
- `actions(board)`: Returns a set of all possible actions available on the board.
- `result(board, action)`: Returns the board that results from making a move.
- `winner(board)`: Returns the winner of the game, if there is one.
- `terminal(board)`: Returns True if the game is over, False otherwise.
- `utility(board)`: Returns the utility value of the board state.
- `max_value(board, alpha, beta)`: Returns the maximum value for the current player.
- `min_value(board, alpha, beta)`: Returns the minimum value for the opponent.
- `minimax(board)`: Returns the optimal action for the current player.

- **Pygame Interface**: The Pygame script initializes the game window, handles user input, and displays the game state on the screen.

## Requirements
- Python 3.X
- Pygame library