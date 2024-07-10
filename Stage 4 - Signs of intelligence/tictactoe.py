import random


def print_board(board):
    print("---------")
    for i in range(3):
        print("|", " ".join(board[i * 3:(i + 1) * 3]), "|")
    print("---------")


def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return board[condition[0]] + " wins"
    if " " not in board:
        return "Draw"
    return "Game not finished"


def make_easy_move(board, player):
    available_moves = [i for i, x in enumerate(board) if x == " "]
    move = random.choice(available_moves)
    board[move] = player


def make_medium_move(board, player):
    opponent = "O" if player == "X" else "X"
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == player and board[condition[2]] == " ":
            board[condition[2]] = player
            return
        if board[condition[0]] == board[condition[2]] == player and board[condition[1]] == " ":
            board[condition[1]] = player
            return
        if board[condition[1]] == board[condition[2]] == player and board[condition[0]] == " ":
            board[condition[0]] = player
            return
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == opponent and board[condition[2]] == " ":
            board[condition[2]] = player
            return
        if board[condition[0]] == board[condition[2]] == opponent and board[condition[1]] == " ":
            board[condition[1]] = player
            return
        if board[condition[1]] == board[condition[2]] == opponent and board[condition[0]] == " ":
            board[condition[0]] = player
            return
    make_easy_move(board, player)


def main():
    while True:
        command = input("Input command: > ").split()
        if command[0] == "exit":
            break
        elif command[0] == "start":
            if len(command) != 3:
                print("Bad parameters!")
                continue
            player1, player2 = command[1], command[2]
            if player1 not in ["user", "easy", "medium"] or player2 not in ["user", "easy", "medium"]:
                print("Bad parameters!")
                continue
            board = [" "] * 9
            print_board(board)
            current_player = "X"
            while True:
                if current_player == "X":
                    if player1 == "user":
                        x, y = map(int, input("Enter the coordinates: > ").split())
                        board[(x - 1) * 3 + (y - 1)] = "X"
                    elif player1 == "easy":
                        print("Making move level \"easy\"")
                        make_easy_move(board, "X")
                    else:
                        print("Making move level \"medium\"")
                        make_medium_move(board, "X")
                else:
                    if player2 == "user":
                        x, y = map(int, input("Enter the coordinates: > ").split())
                        board[(x - 1) * 3 + (y - 1)] = "O"
                    elif player2 == "easy":
                        print("Making move level \"easy\"")
                        make_easy_move(board, "O")
                    else:
                        print("Making move level \"medium\"")
                        make_medium_move(board, "O")
                print_board(board)
                result = check_win(board)
                if result != "Game not finished":
                    print(result)
                    break
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Bad parameters!")


if __name__ == "__main__":
    main()
