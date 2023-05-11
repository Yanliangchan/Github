tic_tac_toe_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
turn = 'X'

while True:

    print(tic_tac_toe_board[0], '|', tic_tac_toe_board[1], '|', tic_tac_toe_board[2])
    print('--+---+--')
    print(tic_tac_toe_board[3], '|', tic_tac_toe_board[4], '|', tic_tac_toe_board[5])
    print('--+---+--')
    print(tic_tac_toe_board[6], '|', tic_tac_toe_board[7], '|', tic_tac_toe_board[8])

    row = input("row: ")
    if int(row) > 3 or int(row) < 1:
        print("row invalid")
        continue
    col = input("col: ")
    if int(col) > 3 or int(col) < 1:
        print("col invalid")
        continue

    location = 3 * (int(row) - 1) + int(col) - 1

    if tic_tac_toe_board[location] != ' ':
        print("location is occupied")
        continue

    tic_tac_toe_board[3 * (int(row) - 1) + int(col) - 1] = turn

    if tic_tac_toe_board[0] == turn and tic_tac_toe_board[1] == turn and tic_tac_toe_board[2] == turn:
        print("you win")
        exit()
    elif tic_tac_toe_board[3] == turn and tic_tac_toe_board[4] == turn and tic_tac_toe_board[5] == turn:
        print("you win")
        exit()
    elif tic_tac_toe_board[6] == turn and tic_tac_toe_board[7] == turn and tic_tac_toe_board[8] == turn:
        print("you win")
        exit()
    elif tic_tac_toe_board[0] == turn and tic_tac_toe_board[3] == turn and tic_tac_toe_board[6] == turn:
        print("you win")
        exit()
    elif tic_tac_toe_board[1] == turn and tic_tac_toe_board[4] == turn and tic_tac_toe_board[7] == turn:
        print("you win")
        exit()
    elif tic_tac_toe_board[2] == turn and tic_tac_toe_board[5] == turn and tic_tac_toe_board[8] == turn:
        print("you win")
        exit()
    elif tic_tac_toe_board[0] == turn and tic_tac_toe_board[4] == turn and tic_tac_toe_board[8] == turn:
        print("you win")
        exit()
    elif tic_tac_toe_board[2] == turn and tic_tac_toe_board[4] == turn and tic_tac_toe_board[6] == turn:
        print("you win")
        exit()
    else:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'