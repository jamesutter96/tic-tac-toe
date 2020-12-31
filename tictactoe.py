"""
Tic Tac Toe Player
"""

import math as m 
import collections
import copy
import random as r 

X = "X"
O = "O"
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

    if board == initial_state():
        user = X

    else:
        # the counter for the game 
        counter = collections.Counter()
        # iterate over the entire board 
        for i in board:
            counter.update(i)

        # sees which of the two players turn it is to move 
        if counter['X'] > counter['O']:
            user = O

        else:
            user = X

    return user





def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_moves.add((i,j))
    # return the possible moves the AI can make 
    return possible_moves

    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action 


    if i < 3 and j < 3and board[i][j] is EMPTY:
        player_name     = player(board)
        new_board       = copy.deepcopy(board)
        new_board[i][j] = player_name
        return new_board

    else:
        raise Exception('Not a valid action')







def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # looks to see if either party has 3 in the same row 
    for i in range(3):

        if board[i][0] == board[i][1] == board[i][2] == "X":
            return "X"
        elif board[i][0] == board[i][1] == board[i][2] == "O":
            return "O"

    # looks to see if either party has 3 in the same col                 
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == "X":
            return "X"
        elif board[0][i] == board[1][i] == board[2][i] == "O":
            return "O"

    # checks if there is 3 in a diagonal 

    if board[0][0] == board[1][1] == board[2][2] == "X":
        return "X"

    if board[0][0] == board[1][1] == board[2][2] == "O":
        return "O"  

    if board[2][0] == board[1][1] == board[0][2] == "X":
        return "X" 

    if board[2][0] == board[1][1] == board[0][2] == "O":
        return "O"

    return None 

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True 
    if any(None in row for row in board):
        return False 
    else:
        return True 


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    win = winner(board)
    if win == "X":
        return 1

    elif win == "O":
        return -1 

    else:
        return 0 


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # if the game is finshed then there is no need to return anything
    if terminal(board) == True:
        return None

    else:
        # randomly generating i and j values 
        i    = r.randint(0, 2)
        j    = r.randint(0, 2)
        move = (i, j)

        if player(board) == X:
            if board == initial_state():
                return move

            v = -m.inf
            for action in actions(board):
                new_v = min_value(result(board, action))

                if new_v > v:
                    v    = new_v
                    move = action

        else:
            if board == initial_state():
                return move

            v = m.inf
            for action in actions(board):
                new_v = max_value(result(board, action))

                if new_v < v:
                    v    = new_v
                    move = action

        return move 




def min_value(board):
    if terminal(board) == True:
        return utility(board)

    v = 0
    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v


def max_value(board):
    if terminal(board) ==  True:
        return utility(board)

    v = 0
    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v

