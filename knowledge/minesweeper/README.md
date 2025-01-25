# Minesweeper Game with AI

This project is a graphical implementation of the classic **Minesweeper** game using **Pygame**. The game features an AI agent capable of making safe moves and using a random strategy when no safe moves are available by maintaining a knowledge base. The objective is to reveal all non-mine cells while avoiding mines. The AI helps the player by suggesting safe moves and can even make random moves when stuck.

## Table of Contents
- [Project Overview](#project-overview)
- [Installation Instructions](#installation-instructions)
- [Gameplay Instructions](#gameplay-instructions)
- [AI Functionality](#ai-functionality)
- [Game Reset](#game-reset)
- [Project Structure](#project-structure)

## Project Overview

This Minesweeper game is built using **Pygame**, a set of Python modules designed for writing video games. The game consists of two parts:
- **Minesweeper Gameplay**: The user interacts with a grid of cells, trying to avoid mines while revealing the safe ones.
- **AI Player**: The AI agent attempts to make the best move based on the current state of the board.

### Features
- A grid-based Minesweeper game.
- **AI integration**: The AI can suggest safe moves or make random moves when no safe options exist.
- **Game reset**: Users can reset the game and start over at any time.
- **User-friendly UI**: Display of game status (win, loss, etc.), instructions, and interactive buttons.

## Installation Instructions

### Prerequisites
To run the project, you need to have Python and Pygame installed.

1. Install Python (if not already installed)
2. Install Pygame via pip:
   ```bash
   pip install pygame
   ```
3. Install the requirements
    ```bash
    pip install -r requirements.txt
    ```

## Gameplay Instructions

1. **Start Game**: Upon launching the game, you'll be presented with instructions on how to play.
    * Left-click to reveal a cell.
    * Right-click to flag a cell as containing a mine.
    * Reveal all non-mine cells to win.
    * Flag all mines to secure a win!

2. **Play Button**: Click the "Play Game" button to start the game.

3. **AI Moves**:
    * You can let the AI suggest safe moves by clicking the **AI Move** button. If the AI is unsure, it will make a random move.
    * The AI will attempt to help you avoid triggering mines.

4. **Game Over**: If you click on a cell containing a mine, the game will display the mine, and you will lose.
    * If you reveal all non-mine cells or flag all mines correctly, you win.

## AI Functionality

The AI agent is built using the **MinesweeperAI** class and integrates with the game state. The agent can:
* **Make safe moves**: Based on its knowledge of neighboring mines.
* **Make random moves**: When it has no knowledge of safe moves and is forced to guess.
* **Flag mines**: When it detects potential mines based on its knowledge.

The AI uses logic based on its knowledge of the revealed cells and the number of surrounding mines to make safe moves.

## Game Reset

At any point during the game, you can reset the game state by clicking the **Reset** button. This will clear the current state and restart the game.

## Project Structure

### `runner.py`
* This is the main script that runs the game.
* It initializes Pygame, sets up the display, and handles user input (left-click, right-click, button presses).
* It creates the game board, displays the minesweeper grid, and manages the state of the game (win/loss).
* It also integrates the AI and allows it to make moves.

### `minesweeper.py`
* Contains the core game logic for **Minesweeper** and **MinesweeperAI**.
* **Minesweeper class**: Handles the game grid, cell revealing, and mine detection.
* **MinesweeperAI class**: Keeps track of known safe and mine cells, and decides which move to make.

### Assets
* **Fonts**: Used for rendering text on the screen, e.g., Open Sans Regular font.
* **Images**: Flag and mine images are used to represent flagged cells and mines.
