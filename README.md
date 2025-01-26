# CS50 Artificial Intelligence Projects and Exercises

In this repository, you will find all the source code, exercises, and projects written for the CS50 AI certification using Python.

## [Search](search)
Contains all codes related to search algorithms.

* **[Degrees](search/degrees)**: Project to find the connection between two actors using a movies database. Makes use of the **Depth-First Search** algorithm with a *StackFrontier* or the **Breadth-First Search** algorithm with a *QueueFrontier*.
* **[Maze](search/maze/)**: Project to draw a maze and its solution to visualize how the algorithm solves the problem. Uses the **Depth-First Search** algorithm with a *StackFrontier* or the **Breadth-First Search** algorithm with a *QueueFrontier*, and outputs the result as a `.png` image file.
* **[Tictactoe](search/tictactoe/)**: Project using Pygame for a Tic-Tac-Toe game, implementing the **Minimax** algorithm with *alpha-beta pruning* optimization.

## [Knowledge](knowledge/)
Contains all codes related to knowledge (propositional logic algorithms) and inference.

* **[Knights](knowledge/knights/)**: Project representing the Knights and Knaves puzzle, where knights tell the truth and knaves lie. The objective is to determine who is a knight and who is a knave.
* **[Minesweeper](knowledge/minesweeper/)**: Minesweeper implemented with Pygame, where an AI plays the best moves using logic. It maintains a knowledge base to track which areas are potentially mined or safe and infers safe areas.

##  [Uncertainty](/uncertainty)
Contains all soruce codes related to Bayesian Networks and Markov Chain models.

* **[Pagerank](/uncertainty/pagerank/)**: Representation of Larry Page's algorithm for determining the quality of a page by ranking them based on the number of times they are clicked, using a Markov Chain representation.
* **[Heredity](/uncertainty/heredity/)**: Implementation from scratch of a Bayesian model used to determine the probability of parents in a family passing down the GJB2 gene mutation (related to hearing impairment) to their children, depending on whether they themselves carry the trait.

## [Optimization](/optimization/)
Contains all source codes related to optimization algorithms developed using AI.

* **[Crossword](/optimization/crossword/)**: A project to generate a crossword from an empty crossword grid and a dictionary of words. It uses *CSP* algorithms with backtracking and an *AC-3* function to ensure arc consistency. Various optimization algorithms are employed to allow the AI to make better decisions by heuristically selecting words that create fewer constraints and have the most compatibility with other words, reducing the chance of conflicts during the backtracking algorithm. *AC-3* is also implemented during the backtracking process to enable the AI to make inferences and pertinently select possible next words without relying heavily on random selections.
* **[Hospital](/optimization/lecture_source_codes/hospitals/)**: Demonstrates an example of AI-based optimization in a scenario where we aim to implement a certain number of hospitals closest to a maximum number of houses on a map. For this script, we use the *Hill Climbing* algorithm. We then utilize the *PIL* library to draw and visualize the result of the optimization.
* **[Production](/optimization/lecture_source_codes/production/)**: A source code example of linear programming that optimizes a linear equation (from *y = a₁x₁ + a₂x₂ + a₃x₃...*) with a cost function we want to minimize, including constraints and individual bounds on variables. It uses the `scipy.optimize` package to solve the problem.
* **[Scheduling](/optimization/lecture_source_codes/scheduling/)**: This source code implements a *Constraint Satisfaction Problem* (CSP) solution algorithm in a scenario where different students are taking 3 classes out of 6, and we try to plan the exams so all students can attend on certain dates.
  * In the first `schedule0` file: We implement the algorithm from scratch using *backtracking* and an *AC-3* function to enforce arc consistency between our variables.
  * In the second version, `schedule1`: We use the `constraint` package to solve the same problem without coding the algorithms from scratch.

## **Learning**
Contains all source code related to machine learning using sklearn package in Python.

* **Shopping**: Build a nearest-neighbor classifier over a 12 000 user sessions to determine if a user will end up going through a purshase or not.
* **Nim**: Train an IA using the Q-learning algorithm playing Nim game to compete against the player.
* **Banknotes**: Use sklearn with varioous model to try to predict if a banknote is a counterfeit or not.

## **Neural Network**
Contains all source code related to Neural Network.
* **Traffic**: Use TensorFlow to build neural network to recognize traffic sign on photographs.
* **Digits**: Use TensorFlow to build a model to recognize handwritten digits on a PyGame interface.

## **Language**
Contains source code related to processing natural language.
* **Sentiment**: Use Naive Bayes Classifier using NLTK library to implements a sentiment analysis tool.
* **Cfg**: Implementation of a simple sentence parser using Context Free Grammar using NLTK.
* **Parser**: Implementation of a more ocmplex sentence parser using Context Free Grammar with NL
* **Markov**: Simple text generator using Markov chains with the `markovify` library.
* **Language**: Implementation of a BERT-based masked language model using the transfomers library to visualizes the attention scores from the model. 


