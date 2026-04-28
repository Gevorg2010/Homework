N = 8

def safe(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def printBoard(board):
    for i in board:
        for j in i:
            print(j, "", end="")
        print()

def recurse(curr_x, curr_y, steps, board, move_x, move_y):
    if steps == N * N:
        return True

    for i in range(8):
        next_x = curr_x + move_x[i]
        next_y = curr_y + move_y[i]

        if safe(next_x, next_y, board):
            board[next_x][next_y] = steps

            if recurse(next_x, next_y, steps + 1, board, move_x, move_y):
                return True

            # bakctrack
            board[next_x][next_y] = -1

    return False

board = [[-1 for i in range(N)] for i in range(N)]
move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]
board[0][0] = 0

if recurse(0, 0, 1, board, move_x, move_y):
    printBoard(board)
else:
    print("No solution.")
