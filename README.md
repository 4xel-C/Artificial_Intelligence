# CS50 Artificial Intelligence Projects and Exercises

In this repository, you will find all the source code, exercises, and projects written for the CS50 AI certification.

## Search
Contains all code related to search algorithms.
* **degrees**: Project to find the connection between two actors using a movies database. Makes use of the **Depth-First Search** algorithm with a *StackFrontier* or the **Breadth-First Search** algorithm with a *QueueFrontier*.
* **maze**: Project to draw a maze and its solution to visualize how the algorithm solves the problem. Uses the **Depth-First Search** algorithm with a *StackFrontier* or the **Breadth-First Search** algorithm with a *QueueFrontier*, and outputs the result as a `.png` image file.
* **tictactoe**: Project using Pygame for a Tic-Tac-Toe game, implementing the **Minimax** algorithm with *alpha-beta pruning* optimization.

## Knowledge
Contains all code related to knowledge (propositional logic algorithms) and inference.
* **knights**: Project representing the Knights and Knaves puzzle, where knights tell the truth and knaves lie. The objective is to determine who is a knight and who is a knave.
* **minesweeper**: Minesweeper implemented with Pygame, where an AI plays the best moves using logic. It maintains a knowledge base to track which areas are potentially mined or safe and infers safe areas.

## Uncertainty
Contains all code related to Bayesian Networks and Markov Chain models.
* **bayesnet**: Bayesian model implemented using Python's pomegranate library. Represents the probability of missing an appointment depending on other variables like train maintenance and weather. Tests various possibilities to compute probabilities and inference, using or not using likelihood weighting and sampling.
* **chain**: Example of a Markov Chain implemented with pomegranate.
* **pagerank**: Representation of Larry Page's algorithm for determining the quality of a page by ranking them based on the number of times they are clicked, using a Markov Chain representation.
* **heredity**: Implementation from scratch of a Bayesian model used to determine the probability of parents in a family passing down the GJB2 gene mutation (related to hearing impairment) to their children, depending on whether they themselves carry the trait.
