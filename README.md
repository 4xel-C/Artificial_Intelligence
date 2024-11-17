# CS50 Artificial Intelligence Projects and Exercises

In this repository, you will find all the source code, exercises, and projects written for the CS50 AI certification.

## Search
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
Contains all soruce codes concerning optimization algorithm made using AI.
* **hospital**: Shows an exemple of optimization AI in a scenario where we try to implement a certain number of hospital closest to a maximum of house on a map. For this script, we'll use *Hill climbing* algorithm. We then make use of the *Pil* library to draw and vizualise the result of the optimization.
*  **hroduction**:; A source code showing an exemple of linear programming that optimize linear equation. (form *y = ax1 + ax2 + ax3...*) with a cost function we want to minimize, constraints, and individual bounds on variables. Use scipy.optimize package to solve the problem.
* **scheduling**: This source code shows the implementation of a *Constraint Stisfaction problem* solution algorithm in a scenario where differents students are taking 3 classes among 6 and we try to plan the exams so all students can attend on a certains date.
  * In the first *schedule0* file: we are implementing the algorithm from scratch using *backtracking* and an *AC-3* function to force arc consistency betweens our variables.
  * In the seconde version *shedule1*: we are using the constraint package to solve the same problem without coding the algorithms from scratch.
* **crossword**: Project to generate a crossword from an empty crossword grid and a dictionnary of word. Use *CSP* algorithms, with backtracking and a *AC-3* function to ensure arc consistency. Use various optimization algorithms to let the AI make better decision by selecting heuristicly words creating the less constraints and having the most compatibility with other words to reduce the chance of having a possible conflict during the backtracking algorithm. *AC-3* is also implemented during the backtracking algorithm to let the AI make inference and pertinently select possibles next words without abusing of random selections.


