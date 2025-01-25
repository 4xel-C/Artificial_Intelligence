# Knights: Logical Sentences and Model Checking

## Overview

This project implements a logic-based framework to evaluate logical sentences and solve puzzles involving knights and knaves. It provides classes to define logical constructs such as symbols, negations, conjunctions, disjunctions, implications, and biconditionals. The program uses model checking to determine logical entailments.

## Features

- **Logical Constructs**: Classes to represent logical statements (`Symbol`, `Not`, `And`, `Or`, `Implication`, `Biconditional`).
- **Model Checking**: Functionality to check if a set of knowledge entails a query.
- **Knights and Knaves Puzzles**: Implementation of multiple puzzles where knights always tell the truth and knaves always lie.

## Project Files

### `logic.py`

This file contains the main logic framework, including:

- `Sentence`: A base class for logical sentences.
- `Symbol`: Represents a propositional symbol.
- `Not`, `And`, `Or`, `Implication`, `Biconditional`: Represent logical operations.
- `model_check`: A function to evaluate if knowledge entails a query.

### `knights.py`

This file defines and solves four knights and knaves puzzles using the logic framework.

#### Puzzles

1. **Puzzle 0**:
   - A says, "I am both a knight and a knave."
   - Logical Representation:
     - A can only be a knight or a knave, but not both.
     - If A is a knight, the statement must be true; if A is a knave, the statement must be false.

2. **Puzzle 1**:
   - A says, "We are both knaves."
   - B says nothing.
   - Logical Representation:
     - Includes constraints on A and B being knights or knaves and the truthfulness of A's statement.

3. **Puzzle 2**:
   - A says, "We are the same kind."
   - B says, "We are of different kinds."
   - Logical Representation:
     - Defines relationships between A and B's roles as knights or knaves based on their statements.

4. **Puzzle 3**:
   - A says, "I am a knight" or "I am a knave."
   - B says, "A said 'I am a knave'" and "C is a knave."
   - C says, "A is a knight."
   - Logical Representation:
     - Defines the truthfulness of statements based on A, B, and C's roles.

## Installation

1. Ensure Python 3.x is installed
2. Run the program:
    ```bash
    python puzzle.py
    ```
