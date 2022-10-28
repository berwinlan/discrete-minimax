import minimax, abpruning, boardhelpers, play, time

def main():

    algorithms:dict = {"1": minimax.computer_turn,
                       "2": abpruning.computer_turn_alpha_beta}

    gametype = algorithms[input("Enter 1 for Minimax, 2 for alpha-beta pruning: ")]

    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    over = False

    while boardhelpers.eval_board(board) == 0 and boardhelpers.count_turns(board) < 9:
        if over:
            break
        
        boardhelpers.draw_board(board)
        board, over = play.player_turn(board)

        boardhelpers.draw_board(board)
        start = time.time()
        board, over = gametype(board)
        end = time.time()
        print(f"Evaluation time: {round(end - start, 6)} sec.")
    
    boardhelpers.draw_board(board)
    print("Game over")


if __name__ == '__main__':
    main()