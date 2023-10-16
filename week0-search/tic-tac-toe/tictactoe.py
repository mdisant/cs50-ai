"""
Tic Tac Toe Player
"""

import math
import copy

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
    x_count = 0
    o_count = 0

    for row in board:
        for val in row:
            if val == X:
                x_count += 1
            elif val == O:
                o_count += 1

    if x_count <= o_count:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_list = set()

    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == EMPTY:
                action_list.add((i, j))

    return list(action_list)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    possible_actions = actions(board)

    if action not in possible_actions:
        raise ValueError("Invalid action")

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows and columns for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]  # Row win
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]  # Column win

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]  # Diagonal win
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]  # Diagonal win

    return None  # No winner yet


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or not any(EMPTY in row for row in board):
        return True
    return False


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


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    alpha = -math.inf
    beta = math.inf

    if player(board) == X:
        best_score = -math.inf
        best_action = None
        for action in actions(board):
            new_score = min_value(result(board, action), alpha, beta)
            if new_score > best_score:
                best_score = new_score
                best_action = action
            alpha = max(alpha, best_score)
    else:
        best_score = math.inf
        best_action = None
        for action in actions(board):
            new_score = max_value(result(board, action), alpha, beta)
            if new_score < best_score:
                best_score = new_score
                best_action = action
            beta = min(beta, best_score)

    return best_action


def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v


def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v
