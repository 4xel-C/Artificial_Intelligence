# CS50 Artificial Intelligence Projects and Exercises

In this repository, you will find all the source code, exercises, and projects written for the CS50 AI certification.

## [Search](Search)
Contains all codes related to search algorithms.

* **degrees**: Project to find the connection between two actors using a movies database. Makes use of the **Depth-First Search** algorithm with a *StackFrontier* or the **Breadth-First Search** algorithm with a *QueueFrontier*.
* **maze**: Project to draw a maze and its solution to visualize how the algorithm solves the problem. Uses the **Depth-First Search** algorithm with a *StackFrontier* or the **Breadth-First Search** algorithm with a *QueueFrontier*, and outputs the result as a `.png` image file.
* **tictactoe**: Project using Pygame for a Tic-Tac-Toe game, implementing the **Minimax** algorithm with *alpha-beta pruning* optimization.

## Knowledge
Contains all codes related to knowledge (propositional logic algorithms) and inference.

* **knights**: Project representing the Knights and Knaves puzzle, where knights tell the truth and knaves lie. The objective is to determine who is a knight and who is a knave.
* **minesweeper**: Minesweeper implemented with Pygame, where an AI plays the best moves using logic. It maintains a knowledge base to track which areas are potentially mined or safe and infers safe areas.

## Uncertainty
Contains all soruce codes related to Bayesian Networks and Markov Chain models.

* **bayesnet**: Bayesian model implemented using Python's pomegranate library. Represents the probability of missing an appointment depending on other variables like train maintenance and weather. Tests various possibilities to compute probabilities and inference, using or not using likelihood weighting and sampling.
* **chain**: Example of a Markov Chain implemented with pomegranate.
* **pagerank**: Representation of Larry Page's algorithm for determining the quality of a page by ranking them based on the number of times they are clicked, using a Markov Chain representation.
* **heredity**: Implementation from scratch of a Bayesian model used to determine the probability of parents in a family passing down the GJB2 gene mutation (related to hearing impairment) to their children, depending on whether they themselves carry the trait.
* **hmm**: Implementation of a simple hidden markov chain using pomegranate package to predict sunny from rainy days depending on wether or not peoples are bring umbrellas.

## Optimization
Contains all source codes related to optimization algorithms developed using AI.

* **hospital**: Demonstrates an example of AI-based optimization in a scenario where we aim to implement a certain number of hospitals closest to a maximum number of houses on a map. For this script, we use the *Hill Climbing* algorithm. We then utilize the *PIL* library to draw and visualize the result of the optimization.
* **production**: A source code example of linear programming that optimizes a linear equation (from *y = a₁x₁ + a₂x₂ + a₃x₃...*) with a cost function we want to minimize, including constraints and individual bounds on variables. It uses the `scipy.optimize` package to solve the problem.
* **scheduling**: This source code implements a *Constraint Satisfaction Problem* (CSP) solution algorithm in a scenario where different students are taking 3 classes out of 6, and we try to plan the exams so all students can attend on certain dates.
  * In the first `schedule0` file: We implement the algorithm from scratch using *backtracking* and an *AC-3* function to enforce arc consistency between our variables.
  * In the second version, `schedule1`: We use the `constraint` package to solve the same problem without coding the algorithms from scratch.
* **crossword**: A project to generate a crossword from an empty crossword grid and a dictionary of words. It uses *CSP* algorithms with backtracking and an *AC-3* function to ensure arc consistency. Various optimization algorithms are employed to allow the AI to make better decisions by heuristically selecting words that create fewer constraints and have the most compatibility with other words, reducing the chance of conflicts during the backtracking algorithm. *AC-3* is also implemented during the backtracking process to enable the AI to make inferences and pertinently select possible next words without relying heavily on random selections.



