# Helper functions for running the Minimax algorithm

import play, boardhelpers

# Computer is +1 Maximizer
def minimax(board, recursion_depth=0):
    """
    Returns:
        tuple (next_move, next_score)
            next_move: Two-ple with (row: int, col: int)
            next_score: an int representing the score of the next move to be played
    """
    # Setting initial conditions for players
    if recursion_depth % 2 == 0:
        # max player
        current_player = 1
    else:
        # min player
        current_player = -1

    # get all possible moves: recursion

    # Base case: winner / all moves played
    if boardhelpers.eval_board(board) != 0 or boardhelpers.count_turns(board) == 9:
        return ((None, None), (boardhelpers.eval_board(board) * 10) / boardhelpers.count_turns(board))

    # Otherwise, determine next move
    moves = play.get_possible_moves(board)   # gets all possible places to put the next move
    next_scores = {}    # dict where k:v is move:score
    for move in moves:
        try:
            next_board = play.make_move(board, move, current_player)
        except Exception:
            continue
        _, next_scores[move] = minimax(next_board, recursion_depth + 1)

    # Using next_scores, pick the min or max move
    if current_player == 1:     # MAX player
        next_move = max(next_scores, key=next_scores.get)
        next_score = next_scores[next_move]
    else:     # MIN player
        next_move = min(next_scores, key=next_scores.get)
        next_score = next_scores[next_move]
    return (next_move, next_score)

def computer_turn(board):
    next_move, next_score = minimax(board)
    if next_move[0] is None:
        return board, True

    next_board = play.make_move(board, next_move, 1)
    return next_board, boardhelpers.eval_board(next_board)