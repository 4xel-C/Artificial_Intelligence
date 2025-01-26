# Nim Game with AI

This repository contains an implementation of the Nim game and an AI agent that uses Q-learning to play the game. The game allows humans to play against the AI or train the AI by letting it play against itself.

## Table of Contents
- [Overview](#overview)
- [Classes and Methods](#classes-and-methods)
- [How to Use](#how-to-use)
  - [Training the AI](#training-the-ai)
  - [Playing Against the AI](#playing-against-the-ai)
- [Q-Learning Explained](#q-learning-explained)
- [Dependencies](#dependencies)
- [License](#license)

---

## Overview
The Nim game starts with a set of piles, each containing a certain number of objects. Two players take turns, removing objects from a single pile. The player forced to take the last object loses.

This implementation includes:
- A `Nim` class to manage the game state.
- A `NimAI` class to implement an AI agent using Q-learning.
- Functions to train the AI and allow a human to play against it.

---

## Classes and Methods

### `Nim` Class
Handles the core mechanics of the game.
- **Attributes**:
  - `piles`: List of integers representing the current state of piles.
  - `player`: The current player (0 or 1).
  - `winner`: Indicates the winner (`None`, `0`, or `1`).
- **Methods**:
  - `available_actions(piles)`: Returns all valid actions `(i, j)` for the current piles.
  - `other_player(player)`: Returns the opposite player.
  - `switch_player()`: Changes the current player.
  - `move(action)`: Executes a move `(i, j)`.

### `NimAI` Class
Implements a Q-learning AI to play the Nim game.
- **Attributes**:
  - `q`: Dictionary storing Q-values for `(state, action)` pairs.
  - `alpha`: Learning rate.
  - `epsilon`: Probability of choosing a random action for exploration.
- **Methods**:
  - `update(old_state, action, new_state, reward)`: Updates the Q-value based on experience.
  - `get_q_value(state, action)`: Returns the Q-value for a given state-action pair.
  - `update_q_value(state, action, old_q, reward, future_rewards)`: Updates Q-value using the Q-learning formula.
  - `best_future_reward(state)`: Returns the highest Q-value for possible actions in a given state.
  - `choose_action(state, epsilon=True)`: Chooses an action based on Q-values and exploration.

### Functions
- `train(n)`: Trains the AI by letting it play `n` games against itself.
- `play(ai, human_player=None)`: Allows a human to play against the AI.

---

## How to Use

### Training the AI
Run the `train(n)` function to train the AI with `n` self-play games. The AI improves by updating its Q-values based on the outcomes of these games.

```python
from nim import train

ai = train(10000)  # Train the AI with 10,000 games
```

## Q-Learning Explained

The AI uses Q-learning to learn optimal strategies:

- **Q-value**: Represents the expected utility of taking an action in a given state.
- **Update Formula**:  
  \( Q(s, a) \gets Q(s, a) + \alpha \times (reward + \max_{a'} Q(s', a') - Q(s, a)) \)
  - \( s \): Current state.
  - \( a \): Action taken.
  - \( s' \): New state after the action.
  - \( \alpha \): Learning rate.

The AI explores actions with a probability of epsilon (\( \epsilon \)) and exploits known Q-values otherwise.

## Dependencies

- Python 3.x  
- Standard Python libraries:
  - `math`
  - `random`
  - `time`
