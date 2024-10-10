"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"  # noqa: E741
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # counting the number of X and O on the board.
    count_x = 0
    count_o = 0
    
    for row in board:
        for value in row:
            if value == X:
                count_x += 1
            elif value == O:
                count_o += 1
                
    # Choosing which symbol plays considering X always start the game.
    if count_x == count_o:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    set_actions = set()
    # checking each tile of the board to see if it's empty and can thus accept a move
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                set_actions.add((row, col))
    return set_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # updating the board to the position given by action by X or Y depending of player turn.
    row, col = action
    symbol = player(board)
    # Creating a copy of the board to avoid direct modification of the global board scope
    new_board = copy.deepcopy(board)
    
    # Error handling
    if row < 0 or col < 0 or row >= len(new_board) or col >= len(new_board[0]):
        raise IndexError("The action tried is not valid")
    if new_board[row][col] != EMPTY:
        raise IndexError
    
    # updating the new board
    new_board[row][col] = symbol
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check lines
    for row in board:
        if set(row) == {X}:
            return X
        elif set(row) == {O}:
            return O
    
    # check columns
    for col in range(len(board[0])):
        column = set()
        for row in range(len(board)):
            column.add(board[row][col])
        if column == {X}:
            return X
        elif column == {O}:
            return O
    
    # check main diagonals
    main_diagonal = set()
    for i in range(len(board)):
        main_diagonal.add(board[i][i])
    if main_diagonal == {X}:
        return X
    elif main_diagonal == {O}:
        return O
    
    # check other diagonal
    other_diagonal = set()
    for i in range(len(board)):
        other_diagonal.add(board[len(board) -1 - i][i])
    if other_diagonal == {X}:
        return X
    elif other_diagonal == {O}:
        return O
        
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for row in board:
        for value in row:
            if value is EMPTY:
                return False
    return True
                

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def max_value(board):
    """
    Returns the maximum value a board could reach if tried to be maximized
    """
    # if board in terminal state, return the value of the outcome (utility)
    if terminal(board):
        return utility(board)
    v = -math.inf
    # check all the actions possibles to go to the nieghbors boards
    for action in actions(board):
        next_board = result(board, action)
        v = max(v, min_value(next_board))
    return v
        
def min_value(board):
    """
    Returns the minimum value a board could reach if tried to be minimized
    """
    # if board in terminal state, return the value of the outcome (utility)
    if terminal(board):
        return utility(board)
    
    v = math.inf
    # check all the actions possibles to go to the nieghbors boards
    for action in actions(board):
        next_board = result(board, action)
        v = min(v, max_value(next_board))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # return None if the game is over and no move is possible
    if terminal(board):
        return None
    
    # keep track of the best action as a dictionnary action: value
    possible_actions = {}
    play = player(board)
    
    if play == X:
        for action in actions(board):
            possible_actions[action] = min_value(result(board, action))
        print(possible_actions)
        return max(possible_actions, key=possible_actions.get)
            
    if play == O:
        for action in actions(board):
            possible_actions[action] = max_value(result(board, action))
        return min(possible_actions, key=possible_actions.get)


# test = [[EMPTY, EMPTY, O],
#         [X, X, O],
#         [EMPTY, EMPTY, EMPTY]]

# print(actions(test))
# print(player(test))
# print(minimax(test))

# print(min_value(test))