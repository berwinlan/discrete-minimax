# Helper functions for running the game.
from copy import deepcopy
import boardhelpers

# moves are defined as the square that you will place your marker in as a (row, col) tuple
def get_possible_moves(board):
    moves = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                moves.append((row, col))
    return moves

def make_move(board, move, player):
    # Returns the board after the move 
    row, col = move
    new_board = deepcopy(board)
    if new_board[row][col] != 0:
        raise Exception(f"Trying to overwrite a filled square. board[{row}][{col}] = {board[row][col]}")
    new_board[row][col] = player
    return new_board

def player_turn(board):
    row = int(input("Row: "))
    col = int(input("Col: "))

    next_board = make_move(board, (row, col), -1)
    over = (boardhelpers.eval_board(next_board) != 0)
    return next_board, over