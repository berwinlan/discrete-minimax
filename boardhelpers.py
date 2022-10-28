# Helper functions for the game board.

# This function evaluates the state of the current board and returns a score.
# Returns 0 if no one won, or the number associated with the player who won
def eval_board(board):
    # Check if horizontal is won
    for row in board:
        if sum(row) == 3:
            return 1
        elif sum(row) == -3:
            return -1
    
    # check if vertical is won
    for i in range(len(board[0])):
        if sum([row[i] for row in board]) == 3:
            return 1
        elif sum([row[i] for row in board]) == -3:
            return -1
    
    # check diagonals
    if sum(board[i][i] for i in range(3)) == 3:
        return 1
    elif sum(board[i][i] for i in range(3)) == -3:
        return -1

    if sum(board[2-i][i] for i in range(3)) == 3:
        return 1
    elif sum(board[2-i][i] for i in range(3)) == -3:
        return -1
    
    return 0

def draw_board(board):
    print("\n")
    print("\n-----\n".join(["|".join([("X" if cell == 1 else ("O" if cell == -1 else " ")) for cell in row]) for row in board]))
    print("\n")

# Counts the number of turns that have already gone
def count_turns(board):
    return sum(sum([abs(i) for i in row]) for row in board)

# moves are defined as the square that you will place your marker in as a (row, col) tuple
def get_possible_moves(board):
    moves = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                moves.append((row, col))
    return moves