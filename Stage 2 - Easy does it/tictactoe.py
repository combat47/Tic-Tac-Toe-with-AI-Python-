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


def make_easy_move(board):
    available_moves = [i for i, x in enumerate(board) if x == " "]
    move = random.choice(available_moves)
    board[move] = "O"


def main():
    board = [" "] * 9
    print_board(board)
    while True:
        user_input = input("Enter the coordinates: > ").split()
        if len(user_input) != 2:
            print("Invalid input. Please enter two numbers separated by a space.")
            continue
        try:
            x, y = map(int, user_input)
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
            continue
        if x < 1 or x > 3 or y < 1 or y > 3:
            print("Coordinates should be from 1 to 3!")
            continue
        if board[(x - 1) * 3 + (y - 1)] != " ":
            print("This cell is occupied! Choose another one.")
            continue
        board[(x - 1) * 3 + (y - 1)] = "X"
        print_board(board)
        result = check_win(board)
        if result != "Game not finished":
            print(result)
            break
        print("Making move level \"easy\"")
        make_easy_move(board)
        print_board(board)
        result = check_win(board)
        if result != "Game not finished":
            print(result)
            break


if __name__ == "__main__":
    main()
