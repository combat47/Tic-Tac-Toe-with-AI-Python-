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


def main():
    board = input("Enter the cells: ").replace("_", " ")
    board = list(board)
    print_board(board)

    while True:
        coordinates = input("Enter the coordinates: ").split()
        if not coordinates[0].isdigit() or not coordinates[1].isdigit():
            print("You should enter numbers!")
            continue
        x, y = int(coordinates[0]), int(coordinates[1])
        if x < 1 or x > 3 or y < 1 or y > 3:
            print("Coordinates should be from 1 to 3!")
            continue
        index = (x - 1) * 3 + (y - 1)
        if board[index] != " ":
            print("This cell is occupied! Choose another one!")
            continue
        symbol = "X" if board.count("X") == board.count("O") else "O"
        board[index] = symbol
        print_board(board)
        state = check_win(board)
        print(state)
        if state != "Game not finished":
            break


if __name__ == "__main__":
    main()
