NO_PLAYER = 0
PLAYER_1_SIGN = 'X'
PLAYER_2_SIGN = 'O'

GAME_STATUS_WINNER_PLAYER_1 = 1
GAME_STATUS_WINNER_PLAYER_2 = 2
GAME_STATUS_TIE = 3
GAME_STATUS_NO_RESULT_YET = 0


def print_board(the_board):
    for i in range(len(the_board)):
        for j in range(len(the_board)):
            print(" ", end="")
            if the_board[i][j] != NO_PLAYER:
                print(the_board[i][j], end="")
            else:
                print(" ", end="")
            print(" |", end="")
        print()
        for j in range(len(the_board)):
            print("____", end="")
        print()

def play_game(the_board):
    current_player = 1
    while check_game_status(the_board) == GAME_STATUS_NO_RESULT_YET:
        is_cell_free = False
        while is_cell_free is False:
            print_board(the_board)
            row = int(input("Please enter row for player #" + str(current_player) + ": "))
            col = int(input("Please enter col for player #" + str(current_player) + ": "))
            while row < 1 or row > len(the_board) or col < 1 or col > len(the_board):
                print("Invalid location")
                row = int(input("Enter row again: "))
                col = int(input("Enter col again: "))

            if the_board[row - 1][col - 1] != NO_PLAYER:
                print("The cell is already taken!\n")
                continue
            print()

            is_cell_free = True
            if current_player == 1:
                the_board[row - 1][col - 1] = PLAYER_1_SIGN
                current_player = 2
            else:
                the_board[row - 1][col - 1] = PLAYER_2_SIGN
                current_player = 1

    print_board(the_board)
    return check_game_status(the_board)


def check_game_status(the_board):
    res = check_if_winner_in_row(the_board)
    if res == GAME_STATUS_WINNER_PLAYER_1 or res == GAME_STATUS_WINNER_PLAYER_2:
        return res

    res = check_if_winner_in_col(the_board)
    if res == GAME_STATUS_WINNER_PLAYER_1 or res == GAME_STATUS_WINNER_PLAYER_2:
        return res

    res = check_if_winner_in_main_diagonal(the_board)
    if res == GAME_STATUS_WINNER_PLAYER_1 or res == GAME_STATUS_WINNER_PLAYER_2:
        return res

    res = check_if_winner_in_secondary_diagonal(the_board)
    if res == GAME_STATUS_WINNER_PLAYER_1 or res == GAME_STATUS_WINNER_PLAYER_2:
        return res

    for i in range(len(the_board)):
        for j in range(len(the_board)):
            if the_board[i][j] == NO_PLAYER:
                return GAME_STATUS_NO_RESULT_YET

    return GAME_STATUS_TIE


def check_if_winner_in_row(the_board):
    for i in range(len(the_board)):
        has_winner_in_current_check = True
        for j in range(1, len(the_board)):
            if the_board[i][j] != the_board[i][0] or the_board[i][j] == NO_PLAYER:
                has_winner_in_current_check = False

        if has_winner_in_current_check:
            if the_board[i][0] == PLAYER_1_SIGN:
                return GAME_STATUS_WINNER_PLAYER_1
            else:
                return GAME_STATUS_WINNER_PLAYER_2

    return GAME_STATUS_NO_RESULT_YET


def check_if_winner_in_col(the_board):
    for i in range(len(the_board)):
        has_winner_in_current_check = True
        for j in range(1, len(the_board)):
            if the_board[j][i] != the_board[0][i] or the_board[j][i] == NO_PLAYER:
                has_winner_in_current_check = False

        if has_winner_in_current_check:
            if the_board[0][i] == PLAYER_1_SIGN:
                return GAME_STATUS_WINNER_PLAYER_1
            else:
                return GAME_STATUS_WINNER_PLAYER_2

    return GAME_STATUS_NO_RESULT_YET

def check_if_winner_in_main_diagonal(the_board):
    has_winner_in_current_check = True
    for i in range(0, len(the_board)):
        if the_board[i][i] != the_board[0][0] or the_board[i][i] == NO_PLAYER:
            has_winner_in_current_check = False

    if has_winner_in_current_check:
        if the_board[0][0] == PLAYER_1_SIGN:
            return GAME_STATUS_WINNER_PLAYER_1
        else:
            return GAME_STATUS_WINNER_PLAYER_2
    return GAME_STATUS_NO_RESULT_YET


def check_if_winner_in_secondary_diagonal(the_board):
    has_winner_in_current_check = True
    for i in range(len(the_board) - 2, -1, -1):
        if the_board[i][len(the_board) - 1 - i] != the_board[len(the_board) - 1][0] or the_board[i][
            len(the_board) - 1 - i] == NO_PLAYER:
            has_winner_in_current_check = False

    if has_winner_in_current_check:
        if the_board[len(the_board) - 1][0] == PLAYER_1_SIGN:
            return GAME_STATUS_WINNER_PLAYER_1
        else:
            return GAME_STATUS_WINNER_PLAYER_2
    return GAME_STATUS_NO_RESULT_YET


def start_game():
    play_again = True
    while play_again:
        board = [[0]*3 for i in range(3)]
        res = play_game(board)

        if res == GAME_STATUS_WINNER_PLAYER_1:
            print("Player 1 is the winner!")
        elif res == GAME_STATUS_WINNER_PLAYER_2:
            print("Player 2 is the winner!" )
        else:
            print("It's a Tie!\n")
            print_board(board)

        answer = input("Would you like to play again? (y/n) ")
        if answer == 'n' or answer == 'N':
            play_again = False


