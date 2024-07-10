from random import randint


class TicTacToe:
    def __init__(self):
        self.win = None
        self.grid = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
        self.counter = 0

    def move(self, **turn):
        for key, value in turn.items():
            if value == "user":
                while True:
                    move = input("Enter the coordinates: ").split()
                    try:
                        y, x = int(move[0]), int(move[1])
                    except ValueError:
                        print("You should enter numbers!\n")
                        continue
                    if not 1 <= y <= 3 or not 1 <= x <= 3:
                        print("Coordinates should be from 1 to 3!\n")
                        continue
                    elif self.grid[y - 1][x - 1] != "_":
                        print("This cell is occupied! Choose another one!\n")
                        continue
                    else:
                        self.grid[y - 1][x - 1] = key
                        self.counter += 1
                        break
            elif value == "easy":
                print('Making move level "easy"')
                while True:
                    y = randint(0, 2)
                    x = randint(0, 2)
                    if self.grid[y][x] == "_":
                        self.grid[y][x] = key
                        self.counter += 1
                        break
            elif value == "medium":
                print('Making move level "medium"')
                if key == "X":
                    other = "O"
                else:
                    other = "X"
                for i in range(3):
                    for j in range(3):
                        if self.grid[i][j] == "_":
                            self.grid[i][j] = key
                            self.winning()
                            for line in self.win:
                                if line.count(key) == 3:
                                    self.counter += 1
                                    return
                            self.grid[i][j] = other
                            self.winning()
                            for line in self.win:
                                if line.count(other) == 3:
                                    self.grid[i][j] = key
                                    self.counter += 1
                                    return
                            self.grid[i][j] = "_"
                while True:
                    y = randint(0, 2)
                    x = randint(0, 2)
                    if self.grid[y][x] == "_":
                        self.grid[y][x] = key
                        self.counter += 1
                        return
            elif value == "hard":
                print('Making move level "hard"')
                if key == "X":
                    other = "O"
                else:
                    other = "X"
                self.winning()
                m, i, j = self.max_alg(key, other)
                print(m)
                self.grid[i][j] = key
                self.counter += 1

    def min_alg(self, key, other):
        self.winning()
        for line in self.win:
            if line.count(key) == 3:
                return 1, 0, 0
            if line.count(other) == 3:
                return -1, 0, 0
        if self.counter == 9:
            return 0, 0, 0
        minv = 2
        min_i = None
        min_j = None
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == "_":
                    self.grid[i][j] = other
                    self.counter += 1
                    m, max_i, max_j = self.max_alg(key, other)
                    if m < minv:
                        minv = m
                        min_i = i
                        min_j = j
                    self.grid[i][j] = "_"
                    self.counter -= 1
        return minv, min_i, min_j

    def max_alg(self, key, other):
        self.winning()
        for line in self.win:
            if line.count(key) == 3:
                return 1, 0, 0
            if line.count(other) == 3:
                return -1, 0, 0
        if self.counter == 9:
            return 0, 0, 0
        maxv = -2
        max_i = None
        max_j = None
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == "_":
                    self.grid[i][j] = key
                    self.counter += 1
                    m, min_i, min_j = self.min_alg(key, other)
                    if m > maxv:
                        maxv = m
                        max_i = i
                        max_j = j
                    self.grid[i][j] = "_"
                    self.counter -= 1
        return maxv, max_i, max_j

    def winning(self):
        self.win = ["".join(self.grid[0]), "".join(self.grid[1]), "".join(self.grid[2]),
                    "".join([self.grid[0][0], self.grid[1][0], self.grid[2][0]]),
                    "".join([self.grid[0][1], self.grid[1][1], self.grid[2][1]]),
                    "".join([self.grid[0][2], self.grid[1][2], self.grid[2][2]]),
                    "".join([self.grid[0][0], self.grid[1][1], self.grid[2][2]]),
                    "".join([self.grid[0][2], self.grid[1][1], self.grid[2][0]])]

    def game_state(self):
        self.winning()
        for i in self.win:
            if i.count("X") == 3:
                print("X wins")
                return True
            elif i.count("O") == 3:
                print("O wins")
                return True
            elif self.counter == 9:
                print("Draw")
                return True
        return False

    def __str__(self):
        out = "---------\n"
        for i in range(len(self.grid)):
            out += f"| {' '.join(self.grid[i])} |\n"
        out += "---------"
        return out


def start():
    accept = ("user", "easy", "medium", "hard")
    while True:
        command = input("Input command: ")
        if command == "exit":
            exit()
        command = command.split()
        if len(command) != 3:
            print("Bad parameters!")
            continue
        if command[0] == "start" and command[1] in accept and command[2] in accept:
            return {"X": command[1]}, {"O": command[2]}
        else:
            print("Bad parameters!")
            continue


p1, p2 = start()
s = TicTacToe()
print(s)
while True:
    s.move(**p1)
    print(s)
    if s.game_state():
        exit()
    s.move(**p2)
    print(s)
    if s.game_state():
        exit()
