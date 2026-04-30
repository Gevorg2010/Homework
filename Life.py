# # - # < 2 dies
# # - # > 3 dies
# _ - # == 3 births

board = [["_" for i in range(10)] for i in range(10)]
board[3][3] = "#"
board[3][5] = "#"
board[4][4] = "#"
board[4][5] = "#"
board[5][4] = "#"

def show(arr):
    for i in arr:
        for j in i:
            print(j, end = "")
        print()

neighbors = [(-1, -1), (-1, 0), (-1, 1), 
             (0, -1),           (0, 1), 
             (1, -1),  (1, 0),  (1, 1)]

def check_cell(x, y):
    count_cells = 0
    for i, j in neighbors:
        nx = x + i
        ny = y + j
        if 0 <= nx + i < 10 and 0 <= ny + j < 10:
            if board[nx][ny] == "#":
                count_cells += 1
    return count_cells

def check_space(x,y):
    count_cells = 0
    for i, j in neighbors:
        nx = x + i
        ny = y + j
        if 0 <= nx + i < 10 and 0 <= ny + j < 10:
            if board[nx][ny] == "#":
                count_cells += 1
    return count_cells

while True:
    show(board)
    input("Press ENTER to see next generations.")

    surr_cell_quant = [[0 for i in range(10)] for i in range(10)] #surrounding cells' quantity

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "_":
                surr_cell_quant[i][j] = check_space(i, j)
            else:
                surr_cell_quant[i][j] = check_cell(i, j)

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "#" and (surr_cell_quant[i][j] < 2 or surr_cell_quant[i][j] > 3):
                board[i][j] = "_"
            elif board[i][j] == "_" and surr_cell_quant[i][j] == 3:
                board[i][j] = "#"
