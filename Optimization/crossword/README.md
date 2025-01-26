# Crossword Puzzle Generator

This project implements a **Constraint Satisfaction Problem (CSP)** solver to generate and solve crossword puzzles. The solver uses **backtracking search** with heuristics and enforces **arc consistency** to ensure valid solutions.

## Features

- **Constraint Satisfaction Problem (CSP)**: Efficiently solves the crossword puzzle using advanced CSP techniques like **node consistency**, **arc consistency (AC-3)**, and **backtracking**.
- **Heuristics**: Includes Minimum Remaining Values (MRV) and Degree heuristics for variable selection and Least Constraining Value (LCV) for value ordering.
- **Output Options**:
  - Print the crossword solution to the terminal.
  - Save the solved crossword as an image.

## Getting Started

### Prerequisites

- Python 3.x
- [Pillow](https://python-pillow.org/) (for saving crosswords as images)
- Fonts (e.g., OpenSans): Place the required fonts in the `assets/fonts/` directory.

Install dependencies:
```bash
pip install pillow
```

## Usage

Run the program with:
```bash
python generate.py <structure> <words> [output]
```
- '<structure>': Path to the crossword structure file.
- '<words>': Path to the list of words for the crossword.
- '[output]' (optional): Fil path to save the crossword solution image.

# Input File Formats

## Structure File
- A `.txt` file defining the crossword grid.
- Use `#` for blank spaces and `█` for blocked spaces.

## Words File
- A `.txt` file containing a list of words for the crossword.

---

# Code Explanation

## Key Components

### **CrosswordCreator Class**

#### Initialization:
- Initializes the CSP and domains for all variables.

#### Methods:
1. **`letter_grid(assignment)`**:
   - Converts an assignment to a 2D grid representation.
2. **`print(assignment)`**:
   - Prints the solved crossword in the terminal.
3. **`save(assignment, filename)`**:
   - Saves the crossword as an image file.
4. **`solve()`**:
   - Solves the crossword using CSP techniques.
5. **`enforce_node_consistency()`**:
   - Removes inconsistent values based on variable constraints.
6. **`revise(x, y)`**:
   - Ensures arc consistency between variables `x` and `y`.
7. **`ac3(arcs=None)`**:
   - Enforces arc consistency for all arcs in the CSP.
8. **`assignment_complete(assignment)`**:
   - Checks if the assignment is complete.
9. **`consistent(assignment)`**:
   - Verifies if the assignment is consistent with the constraints.
10. **`order_domain_values(var, assignment)`**:
    - Orders domain values based on the Least Constraining Value (LCV) heuristic.
11. **`select_unassigned_variable(assignment)`**:
    - Selects an unassigned variable using MRV and Degree heuristics.
12. **`backtrack(assignment)`**:
    - Implements the backtracking search algorithm.

---

### **`main()` Function**
- Parses command-line arguments.
- Initializes the crossword puzzle.
- Solves the puzzle and outputs the result.

---

## CSP Techniques Used

1. **Node Consistency**:
   - Ensures that variables meet unary constraints.
2. **Arc Consistency (AC-3)**:
   - Removes values from domains that are inconsistent with binary constraints.
3. **Backtracking Search**:
   - Explores possible assignments to solve the puzzle.

### Heuristics:
- **Minimum Remaining Values (MRV)**:
  - Selects the variable with the fewest legal values.
- **Degree Heuristic**:
  - Prefers variables with the most neighbors, constraining more nodes and accelerating the algorithm
- **Least Constraining Value (LCV)**:
  - Orders values to minimize conflicts.

---

## Outputs

1. **Terminal Output**:
   - The solved crossword is displayed with spaces for letters and `█` for blocked cells.
