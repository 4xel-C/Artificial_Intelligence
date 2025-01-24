# Degrees of Separation - Movie Connection Finder

This project implements a program that calculates the degrees of separation between two actors based on their shared movie appearances. It uses a graph search algorithm to find the shortest path connecting two individuals in a movie database.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Data Files](#data-files)
- [How It Works](#how-it-works)
- [Code Explanation](#code-explanation)
- [Requirements](#requirements)

## Installation

To run this project, ensure you have Python installed on your machine. This project relies on standard Python libraries, so no additional installations are required.

## Usage

1. Prepare the CSV data files for people, movies, and stars. Ensure they are structured as follows:
   - `people.csv`: Contains columns for `id`, `name`, and `birth`.
   - `movies.csv`: Contains columns for `id`, `title`, and `year`.
   - `stars.csv`: Contains columns for `movie_id` and `person_id`.

   You can use the data available in the 'small' folder as an exemple.

2. Run the script from the command line with the path to the data directory:

```bash
python degrees.py [directory]
```

If no directory is specified, it defaults to the `small` directory.  
Input the names of two actors when prompted. The program will output the degrees of separation and the movies they starred in together.

3. You can edit l.103 of `degress.py` file to use either:
    - the  QueueFrontier: Using a *FIFO* logic to ensures nodes are explored in the order they were added ensuring finding the target node via the **shortest path**
    - or the StackFrontier, Using a *LIFO* logic to explore as far down a branch as possible before backtracking. The StackFrontier by his bahvior does **not ensure finding the shortest path**.
    
    `frontier = QueueFrontier()`  <=> `frontier = StackFrontier()`

## Data Files

The program expects the following CSV files in the specified directory:

- `people.csv`
- `movies.csv`
- `stars.csv`

## How It Works

- **Loading Data**: The program loads data from the specified CSV files into memory, mapping names to person IDs, and person IDs to their associated movies.

- **Finding Connections**: When two names are entered, the program uses a graph search algorithm (depth-first search or breadth-first search) to find the shortest path of connections (movies) between the two actors.

- **Output**: It prints the number of degrees of separation and details of the movies they starred in together.

## Code Explanation

### Main Components

#### Data Structures:

- **names**: A dictionary that maps actor names to their corresponding person IDs.
- **people**: A dictionary that maps person IDs to a dictionary containing actor details (name, birth year, and movies).
- **movies**: A dictionary that maps movie IDs to a dictionary containing movie details (title, year, and stars).

#### Node Class:

The `Node` class represents a node in the search tree. It stores the current state (person ID), the parent node, and the action taken to reach this node (the movie).

```python
class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
```

#### Frontier Classes

- **StackFrontier**: Implements a stack-based frontier (LIFO) for depth-first search. It allows adding nodes, checking if a state is already in the frontier, and removing nodes from the top of the stack.
- **QueueFrontier**: Inherits from the StackFrontier but implements a queue-based frontier (FIFO) for breadth-first search.

#### Searching for Connections

The `shortest_path` function uses the `Node` and `StackFrontier`/`QueueFrontier` classes to find the shortest path between two actors. It explores neighbors (co-stars) and tracks explored nodes to avoid cycles.

#### Finding Neighbors

The `neighbors_for_person` function retrieves all movies an actor has starred in and returns pairs of `(movie_id, person_id)` for all co-stars.

## Requirements

- Python 3.x
- No external libraries required beyond the standard library.